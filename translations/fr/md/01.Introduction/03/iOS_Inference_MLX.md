<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9a626d7522772d8b7b6f188dc79108c4",
  "translation_date": "2025-03-27T07:16:23+00:00",
  "source_file": "md\\01.Introduction\\03\\iOS_Inference_MLX.md",
  "language_code": "fr"
}
-->
# Exécution de Phi-3 et Phi-4 sur iOS avec le framework Apple MLX

Ce tutoriel montre comment créer une application iOS qui exécute le modèle Phi-3 ou Phi-4 directement sur l'appareil, en utilisant le framework Apple MLX. [MLX](https://opensource.apple.com/projects/mlx/) est le framework de machine learning d'Apple, optimisé pour les puces Apple Silicon.

## Prérequis

- macOS avec Xcode 16 (ou une version ultérieure)
- Appareil cible iOS 18 (ou une version ultérieure) avec au moins 8 Go de RAM (iPhone ou iPad compatible avec les exigences d'Apple Intelligence, similaires aux exigences quantifiées de Phi)
- Connaissances de base en Swift et SwiftUI

## Étape 1 : Créer un nouveau projet iOS

Commencez par créer un nouveau projet iOS dans Xcode :

1. Lancez Xcode et sélectionnez « Créer un nouveau projet Xcode »
2. Choisissez « App » comme modèle
3. Nommez votre projet (par exemple, « Phi3-iOS-App ») et sélectionnez SwiftUI comme interface
4. Choisissez un emplacement pour enregistrer votre projet

## Étape 2 : Ajouter les dépendances nécessaires

Ajoutez le package [MLX Examples](https://github.com/ml-explore/mlx-swift-examples), qui contient toutes les dépendances et outils nécessaires pour précharger les modèles et effectuer des inférences :

```swift
// In Xcode: File > Add Package Dependencies
// URL: https://github.com/ml-explore/mlx-swift-examples
```

Bien que le package de base [MLX Swift](https://github.com/ml-explore/mlx-swift) soit suffisant pour les opérations de tenseurs et les fonctionnalités de base de ML, le package MLX Examples offre plusieurs composants supplémentaires conçus pour travailler avec des modèles de langage et simplifier le processus d'inférence :

- Outils de chargement de modèles qui gèrent les téléchargements depuis Hugging Face
- Intégration du tokenizer
- Aides à l'inférence pour la génération de texte
- Définitions de modèles préconfigurées

## Étape 3 : Configurer les droits

Pour permettre à notre application de télécharger des modèles et d'allouer suffisamment de mémoire, nous devons ajouter des droits spécifiques. Créez un fichier `.entitlements` pour votre application avec le contenu suivant :

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

> **Note :** Le droit `com.apple.developer.kernel.increased-memory-limit` est essentiel pour exécuter des modèles plus volumineux, car il permet à l'application de demander plus de mémoire que ce qui est normalement autorisé.

## Étape 4 : Créer le modèle de message de chat

Tout d'abord, créons une structure de base pour représenter nos messages de chat :

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

Ensuite, nous allons créer la classe `PhiViewModel`, qui gère le chargement du modèle et les inférences :

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

Le ViewModel démontre les principaux points d'intégration avec MLX :

- Définir les limites du cache GPU avec `MLX.GPU.set(cacheLimit:)` to optimize memory usage on mobile devices
- using `LLMModelFactory` to download the model on-demand and initialize the MLX-optimized model
- accessing the model's parameters and structure through the `ModelContainer`
- leveraging MLX's token-by-token generation through the `MLXLMCommon.generate` method
- managing the inference process with appropriate temperature settings and token limits

The streaming token generation approach provides immediate feedback to users as the model generates text. This is similar to how server-based models function, as they stream the tokens back to the user, but without the latency of network requests.

In terms of UI interaction, the two key functions are `loadModel()`, which initializes the LLM, and `fetchAIResponse()`, which processes user input and generates AI responses.

### Model format considerations

> **Important:** Phi models for MLX cannot be used in their default or GGUF format. They must be converted to the MLX format, which is handled by the MLX community. You can find pre-converted models at [huggingface.co/mlx-community](https://huggingface.co/mlx-community).

The MLX Examples package includes pre-configured registrations for several models, including Phi-3. When you call `ModelRegistry.phi3_5_4bit`, il fait référence à un modèle MLX spécifique préconverti qui sera automatiquement téléchargé :

```swift
static public let phi3_5_4bit = ModelConfiguration(
    id: "mlx-community/Phi-3.5-mini-instruct-4bit",
    defaultPrompt: "What is the gravity on Mars and the moon?",
    extraEOSTokens: ["<|end|>"]
)
```

Vous pouvez créer vos propres configurations de modèles pour pointer vers n'importe quel modèle compatible sur Hugging Face. Par exemple, pour utiliser Phi-4 mini, vous pourriez définir votre propre configuration :

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

> **Note :** La prise en charge de Phi-4 a été ajoutée au dépôt MLX Swift Examples fin février 2025 (dans [PR #216](https://github.com/ml-explore/mlx-swift-examples/pull/216)). En mars 2025, la dernière version officielle (2.21.2 de décembre 2024) n'inclut pas de prise en charge intégrée de Phi-4. Pour utiliser les modèles Phi-4, vous devrez référencer le package directement depuis la branche principale :
>
>```swift
> // In your Package.swift or via Xcode's package manager interface
> .package(url: "https://github.com/ml-explore/mlx-swift-examples.git", branch: "main")
> ```

Cela vous donne accès aux dernières configurations de modèles, y compris Phi-4, avant qu'elles ne soient incluses dans une version officielle. Vous pouvez utiliser cette approche pour utiliser différentes versions des modèles Phi ou même d'autres modèles convertis au format MLX.

## Étape 6 : Créer l'interface utilisateur

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

L'interface utilisateur se compose de trois principaux composants qui fonctionnent ensemble pour créer une interface de chat basique. `ContentView` creates a two-state interface that shows either a loading button or the chat interface depending on model readiness. `MessageView` renders individual chat messages differently based on whether they are user messages (right-aligned, blue background) or Phi model responses (left-aligned, gray background). `TypingIndicatorView` fournit un indicateur animé simple pour montrer que l'IA est en train de traiter.

## Étape 7 : Construire et exécuter l'application

Nous sommes maintenant prêts à construire et exécuter l'application.

> **Important !** MLX ne prend pas en charge le simulateur. Vous devez exécuter l'application sur un appareil physique avec une puce Apple Silicon. Voir [ici](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/running-on-ios#Developing-for-iOS) pour plus d'informations.

Lorsque l'application se lance, appuyez sur le bouton « Charger le modèle » pour télécharger et initialiser le modèle Phi-3 (ou, selon votre configuration, Phi-4). Ce processus peut prendre du temps selon votre connexion Internet, car il implique le téléchargement du modèle depuis Hugging Face. Notre implémentation inclut seulement un spinner pour indiquer le chargement, mais vous pouvez voir la progression réelle dans la console Xcode.

Une fois chargé, vous pouvez interagir avec le modèle en tapant des questions dans le champ de texte et en appuyant sur le bouton d'envoi.

Voici comment notre application devrait se comporter, exécutée sur un iPad Air M1 :

![Demo GIF](../../../../../imgs/01/01/01.phi3ipados.gif)

## Conclusion

Et voilà ! En suivant ces étapes, vous avez créé une application iOS qui exécute le modèle Phi-3 (ou Phi-4) directement sur l'appareil en utilisant le framework MLX d'Apple.

Félicitations !

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions de garantir l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de faire appel à une traduction professionnelle humaine. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.