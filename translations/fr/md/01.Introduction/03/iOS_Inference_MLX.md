<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9a626d7522772d8b7b6f188dc79108c4",
  "translation_date": "2025-05-07T14:38:44+00:00",
  "source_file": "md/01.Introduction/03/iOS_Inference_MLX.md",
  "language_code": "fr"
}
-->
# Exécuter Phi-3 et Phi-4 sur iOS avec le framework Apple MLX

Ce tutoriel montre comment créer une application iOS qui exécute le modèle Phi-3 ou Phi-4 directement sur l’appareil, en utilisant le framework Apple MLX. [MLX](https://opensource.apple.com/projects/mlx/) est le framework d’apprentissage automatique d’Apple optimisé pour les puces Apple Silicon.

## Prérequis

- macOS avec Xcode 16 (ou version supérieure)  
- Appareil cible iOS 18 (ou version supérieure) avec au moins 8 Go de RAM (iPhone ou iPad compatible avec les exigences Apple Intelligence, similaires à celles de Phi quantifié)  
- Connaissances de base en Swift et SwiftUI  

## Étape 1 : Créer un nouveau projet iOS

Commencez par créer un nouveau projet iOS dans Xcode :

1. lancez Xcode et sélectionnez « Create a new Xcode project »  
2. choisissez le modèle « App »  
3. nommez votre projet (par exemple, « Phi3-iOS-App ») et sélectionnez SwiftUI comme interface  
4. choisissez un emplacement pour enregistrer votre projet  

## Étape 2 : Ajouter les dépendances requises

Ajoutez le package [MLX Examples](https://github.com/ml-explore/mlx-swift-examples) qui contient toutes les dépendances nécessaires et des utilitaires pour précharger les modèles et effectuer des inférences :

```swift
// In Xcode: File > Add Package Dependencies
// URL: https://github.com/ml-explore/mlx-swift-examples
```

Alors que le package de base [MLX Swift](https://github.com/ml-explore/mlx-swift) suffit pour les opérations tensoriales de base et les fonctionnalités ML élémentaires, le package MLX Examples fournit plusieurs composants supplémentaires conçus pour travailler avec des modèles de langage et faciliter le processus d’inférence :

- utilitaires de chargement de modèles qui gèrent le téléchargement depuis Hugging Face  
- intégration du tokenizer  
- aides à l’inférence pour la génération de texte  
- définitions de modèles préconfigurées  

## Étape 3 : Configurer les droits d’accès (Entitlements)

Pour permettre à notre application de télécharger les modèles et d’allouer suffisamment de mémoire, nous devons ajouter des droits spécifiques. Créez un fichier `.entitlements` pour votre application avec le contenu suivant :

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>com.apple.security.app-sandbox</key>
    <true/>
    <key>com.apple.security.files.user-selected.read-only</key>
    <true/>
    <key>com.apple.security.network.client</key>
    <true/>
    <key>com.apple.developer.kernel.increased-memory-limit</key>
    <true/>
</dict>
</plist>
```

> **Note :** Le droit `com.apple.developer.kernel.increased-memory-limit` est important pour exécuter des modèles plus volumineux, car il permet à l’application de demander plus de mémoire que la limite habituelle.

## Étape 4 : Créer le modèle de message de chat

Commençons par créer une structure basique pour représenter nos messages de chat :

```swift
import SwiftUI

enum MessageState {
    case ok
    case waiting
}

struct ChatMessage: Identifiable {
    let id = UUID()
    let text: String
    let isUser: Bool
    let state: MessageState
}
```

## Étape 5 : Implémenter le ViewModel

Ensuite, nous allons créer la classe `PhiViewModel` qui gère le chargement du modèle et l’inférence :

```swift
import MLX
import MLXLLM
import MLXLMCommon
import SwiftUI

@MainActor
class PhiViewModel: ObservableObject {
    @Published var isLoading: Bool = false
    @Published var isLoadingEngine: Bool = false
    @Published var messages: [ChatMessage] = []
    @Published var prompt: String = ""
    @Published var isReady: Bool = false
    
    private let maxTokens = 1024
    
    private var modelContainer: ModelContainer?
    
    func loadModel() async {
        DispatchQueue.main.async {
            self.isLoadingEngine = true
        }
        
        do {
            MLX.GPU.set(cacheLimit: 20 * 1024 * 1024)
            
            // Phi 3.5 mini is preconfigured in Swift MLX Examples
            let modelConfig = ModelRegistry.phi3_5_4bit
            
            // Phi 4 mini can be pulled from Hugging Face, but requires referencing Swift MLX Examples from the main branch
            //let modelConfig = ModelConfiguration(
            //    id: "mlx-community/Phi-4-mini-instruct-4bit",
            //    defaultPrompt: "You are a helpful assistant.",
            //    extraEOSTokens: ["<|end|>"]
            //)
            
            print("Loading \(modelConfig.name)...")
            self.modelContainer = try await LLMModelFactory.shared.loadContainer(
                configuration: modelConfig
            ) { progress in
                print("Download progress: \(Int(progress.fractionCompleted * 100))%")
            }
            
            // Log model parameters
            if let container = self.modelContainer {
                let numParams = await container.perform { context in
                    context.model.numParameters()
                }
                print("Model loaded. Parameters: \(numParams / (1024*1024))M")
            }
            
            DispatchQueue.main.async {
                self.isLoadingEngine = false
                self.isReady = true
            }
        } catch {
            print("Failed to load model: \(error)")
            
            DispatchQueue.main.async {
                self.isLoadingEngine = false
            }
        }
    }
    
    func fetchAIResponse() async {
        guard !isLoading, let container = self.modelContainer else {
            print("Cannot generate: model not loaded or already processing")
            return
        }
        
        let userQuestion = prompt
        let currentMessages = self.messages
        
        DispatchQueue.main.async {
            self.isLoading = true
            self.prompt = ""
            self.messages.append(ChatMessage(text: userQuestion, isUser: true, state: .ok))
            self.messages.append(ChatMessage(text: "", isUser: false, state: .waiting))
        }
        
        do {
            let _ = try await container.perform { context in
                var messageHistory: [[String: String]] = [
                    ["role": "system", "content": "You are a helpful assistant."]
                ]
                
                for message in currentMessages {
                    let role = message.isUser ? "user" : "assistant"
                    messageHistory.append(["role": role, "content": message.text])
                }
                
                messageHistory.append(["role": "user", "content": userQuestion])
                
                let input = try await context.processor.prepare(
                    input: .init(messages: messageHistory))
                let startTime = Date()
                
                let result = try MLXLMCommon.generate(
                    input: input,
                    parameters: GenerateParameters(temperature: 0.6),
                    context: context
                ) { tokens in
                    let output = context.tokenizer.decode(tokens: tokens)
                    Task { @MainActor in
                        if let index = self.messages.lastIndex(where: { !$0.isUser }) {
                            self.messages[index] = ChatMessage(
                                text: output,
                                isUser: false,
                                state: .ok
                            )
                        }
                    }
                    
                    if tokens.count >= self.maxTokens {
                        return .stop
                    } else {
                        return .more
                    }
                }
                
                let finalOutput = context.tokenizer.decode(tokens: result.tokens)
                Task { @MainActor in
                    if let index = self.messages.lastIndex(where: { !$0.isUser }) {
                        self.messages[index] = ChatMessage(
                            text: finalOutput,
                            isUser: false,
                            state: .ok
                        )
                    }
                    
                    self.isLoading = false
                    
                    print("Inference complete:")
                    print("Tokens: \(result.tokens.count)")
                    print("Tokens/second: \(result.tokensPerSecond)")
                    print("Time: \(Date().timeIntervalSince(startTime))s")
                }
                
                return result
            }
        } catch {
            print("Inference error: \(error)")
            
            DispatchQueue.main.async {
                if let index = self.messages.lastIndex(where: { !$0.isUser }) {
                    self.messages[index] = ChatMessage(
                        text: "Sorry, an error occurred: \(error.localizedDescription)",
                        isUser: false,
                        state: .ok
                    )
                }
                self.isLoading = false
            }
        }
    }
}

```

Le ViewModel illustre les points clés d’intégration avec MLX :

- définition des limites du cache GPU avec `MLX.GPU.set(cacheLimit:)`  
- `LLMModelFactory`  
- `ModelContainer`  
- `MLXLMCommon.generate`  
- `loadModel()`  
- `fetchAIResponse()`  
- `ModelRegistry.phi3_5_4bit`, qui fait référence à un modèle MLX pré-converti spécifique qui sera téléchargé automatiquement :

```swift
static public let phi3_5_4bit = ModelConfiguration(
    id: "mlx-community/Phi-3.5-mini-instruct-4bit",
    defaultPrompt: "What is the gravity on Mars and the moon?",
    extraEOSTokens: ["<|end|>"]
)
```

Vous pouvez créer vos propres configurations de modèles pour pointer vers n’importe quel modèle compatible sur Hugging Face. Par exemple, pour utiliser Phi-4 mini à la place, vous pourriez définir votre propre configuration :

```swift
let phi4_mini_4bit = ModelConfiguration(
    id: "mlx-community/Phi-4-mini-instruct-4bit",
    defaultPrompt: "Explain quantum computing in simple terms.",
    extraEOSTokens: ["<|end|>"]
)

// Then use this configuration when loading the model
self.modelContainer = try await LLMModelFactory.shared.loadContainer(
    configuration: phi4_mini_4bit
) { progress in
    print("Download progress: \(Int(progress.fractionCompleted * 100))%")
}
```

> **Note :** Le support de Phi-4 a été ajouté au dépôt MLX Swift Examples fin février 2025 (dans la [PR #216](https://github.com/ml-explore/mlx-swift-examples/pull/216)). En mars 2025, la dernière version officielle (2.21.2 de décembre 2024) ne comprend pas encore le support intégré de Phi-4. Pour utiliser les modèles Phi-4, vous devrez référencer le package directement depuis la branche principale :  
>  
>```swift
> // In your Package.swift or via Xcode's package manager interface
> .package(url: "https://github.com/ml-explore/mlx-swift-examples.git", branch: "main")
> ```

Cela vous donne accès aux dernières configurations de modèles, y compris Phi-4, avant leur inclusion dans une version officielle. Vous pouvez utiliser cette méthode pour exploiter différentes versions des modèles Phi ou même d’autres modèles convertis au format MLX.

## Étape 6 : Créer l’interface utilisateur

Implémentons maintenant une interface de chat simple pour interagir avec notre ViewModel :

```swift
import SwiftUI

struct ContentView: View {
    @ObservedObject var viewModel = PhiViewModel()

    var body: some View {
        NavigationStack {
            if !viewModel.isReady {
                Spacer()
                if viewModel.isLoadingEngine {
                    ProgressView()
                } else {
                    Button("Load model") {
                        Task {
                            await viewModel.loadModel()
                        }
                    }
                }
                Spacer()
            } else {
                VStack(spacing: 0) {
                    ScrollViewReader { proxy in
                        ScrollView {
                            VStack(alignment: .leading, spacing: 8) {
                                ForEach(viewModel.messages) { message in
                                    MessageView(message: message).padding(.bottom)
                                }
                            }
                            .id("wrapper").padding()
                            .padding()
                        }
                        .onChange(of: viewModel.messages.last?.id, perform: { value in
                            if viewModel.isLoading {
                                proxy.scrollTo("wrapper", anchor: .bottom)
                            } else if let lastMessage = viewModel.messages.last {
                                proxy.scrollTo(lastMessage.id, anchor: .bottom)
                            }
                            
                        })
                    }
                    
                    HStack {
                        TextField("Type a question...", text: $viewModel.prompt, onCommit: {
                            Task {
                                await viewModel.fetchAIResponse()
                            }
                        })
                        .padding(10)
                        .background(Color.gray.opacity(0.2))
                        .cornerRadius(20)
                        .padding(.horizontal)
                        
                        Button(action: {
                            Task {
                                await viewModel.fetchAIResponse()
                            }
                        }) {
                            Image(systemName: "paperplane.fill")
                                .font(.system(size: 24))
                                .foregroundColor(.blue)
                        }
                        .padding(.trailing)
                    }
                    .padding(.bottom)
                }
            }
        }.navigationTitle("Phi Sample")
    }
}

struct MessageView: View {
    let message: ChatMessage

    var body: some View {
        HStack {
            if message.isUser {
                Spacer()
                Text(message.text)
                    .padding()
                    .background(Color.blue)
                    .foregroundColor(.white)
                    .cornerRadius(10)
            } else {
                if message.state == .waiting {
                    TypingIndicatorView()
                } else {
                    VStack {
                        Text(message.text)
                            .padding()
                    }
                    .background(Color.gray.opacity(0.1))
                    .cornerRadius(10)
                    Spacer()
                }
            }
        }
        .padding(.horizontal)
    }
}

struct TypingIndicatorView: View {
    @State private var shouldAnimate = false

    var body: some View {
        HStack {
            ForEach(0..<3) { index in
                Circle()
                    .frame(width: 10, height: 10)
                    .foregroundColor(.gray)
                    .offset(y: shouldAnimate ? -5 : 0)
                    .animation(
                        Animation.easeInOut(duration: 0.5)
                            .repeatForever()
                            .delay(Double(index) * 0.2)
                    )
            }
        }
        .onAppear { shouldAnimate = true }
        .onDisappear { shouldAnimate = false }
    }
}

```

L’interface utilisateur se compose de trois composants principaux qui fonctionnent ensemble pour créer une interface de chat basique. `ContentView`, `MessageView` et `TypingIndicatorView` fournissent un indicateur animé simple pour montrer que l’IA est en train de traiter.

## Étape 7 : Compiler et lancer l’application

Nous sommes maintenant prêts à compiler et exécuter l’application.

> **Important !** MLX ne supporte pas le simulateur. Vous devez lancer l’application sur un appareil physique équipé d’une puce Apple Silicon. Voir [ici](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/running-on-ios#Developing-for-iOS) pour plus d’informations.

Au lancement de l’application, appuyez sur le bouton « Load model » pour télécharger et initialiser le modèle Phi-3 (ou, selon votre configuration, Phi-4). Ce processus peut prendre un certain temps selon votre connexion internet, car il implique de télécharger le modèle depuis Hugging Face. Notre implémentation inclut uniquement un indicateur de chargement, mais vous pouvez suivre la progression réelle dans la console Xcode.

Une fois chargé, vous pouvez interagir avec le modèle en tapant des questions dans le champ de texte et en appuyant sur le bouton d’envoi.

Voici à quoi devrait ressembler notre application, fonctionnant sur un iPad Air M1 :

![Demo GIF](../../../../../imgs/01/01/01.phi3ipados.gif)

## Conclusion

Et voilà ! En suivant ces étapes, vous avez créé une application iOS qui exécute directement sur l’appareil le modèle Phi-3 (ou Phi-4) en utilisant le framework MLX d’Apple.

Félicitations !

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant foi. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle humaine. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.