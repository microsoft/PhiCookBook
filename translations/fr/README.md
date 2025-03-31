<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1377ae1b0bc9daeaa6a989f750977aeb",
  "translation_date": "2025-03-27T02:38:39+00:00",
  "source_file": "README.md",
  "language_code": "fr"
}
-->
# Phi Cookbook : Des exemples pratiques avec les modèles Phi de Microsoft

Phi est une série de modèles d'IA open source développés par Microsoft.

Phi est actuellement le modèle de langage compact (SLM) le plus puissant et rentable, avec d'excellents résultats dans des benchmarks liés aux langues multiples, au raisonnement, à la génération de texte/chat, au codage, aux images, à l'audio et à d'autres scénarios.

Vous pouvez déployer Phi dans le cloud ou sur des appareils edge, et vous pouvez facilement créer des applications d'IA générative avec une puissance de calcul limitée.

Suivez ces étapes pour commencer à utiliser ces ressources :
1. **Forkez le dépôt** : Cliquez sur [![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **Clonez le dépôt** :   `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Rejoignez la communauté Discord IA de Microsoft et rencontrez des experts ainsi que d'autres développeurs**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/cover.2595d43b382944c601aebf88583314636768eece3d94e8e4448e03a4e5bedef4.fr.png)

## 🌐 Support multilingue
[Français](./README.md) | [Espagnol](../es/README.md) | [Allemand](../de/README.md) | [Russe](../ru/README.md) | [Arabe](../ar/README.md) | [Persan (Farsi)](../fa/README.md) | [Ourdou](../ur/README.md) | [Chinois (Simplifié)](../zh/README.md) | [Chinois (Traditionnel, Macao)](../mo/README.md) | [Chinois (Traditionnel, Hong Kong)](../hk/README.md) | [Chinois (Traditionnel, Taïwan)](../tw/README.md) | [Japonais](../ja/README.md) | [Coréen](../ko/README.md) | [Hindi](../hi/README.md) | [Bengali](../bn/README.md) | [Marathi](../mr/README.md) | [Népalais](../ne/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Portugais (Portugal)](../pt/README.md) | [Portugais (Brésil)](../br/README.md) | [Italien](../it/README.md) | [Polonais](../pl/README.md) | [Turc](../tr/README.md) | [Grec](../el/README.md) | [Thaï](../th/README.md) | [Suédois](../sv/README.md) | [Danois](../da/README.md) | [Norvégien](../no/README.md) | [Finnois](../fi/README.md) | [Néerlandais](../nl/README.md) | [Hébreu](../he/README.md) | [Vietnamien](../vi/README.md) | [Indonésien](../id/README.md) | [Malais](../ms/README.md) | [Tagalog (Philippin)](../tl/README.md) | [Swahili](../sw/README.md) | [Hongrois](../hu/README.md) | [Tchèque](../cs/README.md) | [Slovaque](../sk/README.md) | [Roumain](../ro/README.md) | [Bulgare](../bg/README.md) | [Serbe (Cyrillique)](../sr/README.md) | [Croate](../hr/README.md) | [Slovène](../sl/README.md)
## Table des matières

- Introduction
  - [Bienvenue dans la famille Phi](./md/01.Introduction/01/01.PhiFamily.md)
  - [Configurer votre environnement](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [Comprendre les technologies clés](./md/01.Introduction/01/01.Understandingtech.md)
  - [Sécurité IA pour les modèles Phi](./md/01.Introduction/01/01.AISafety.md)
  - [Support matériel pour Phi](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Modèles Phi et disponibilité sur différentes plateformes](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Utiliser Guidance-ai et Phi](./md/01.Introduction/01/01.Guidance.md)
  - [Modèles du Marketplace GitHub](https://github.com/marketplace/models)
  - [Catalogue de modèles Azure AI](https://ai.azure.com)

- Inférence Phi dans différents environnements
    - [Hugging face](./md/01.Introduction/02/01.HF.md)
    - [Modèles GitHub](./md/01.Introduction/02/02.GitHubModel.md)
    - [Catalogue de modèles Azure AI Foundry](./md/01.Introduction/02/03.AzureAIFoundry.md)
    - [Ollama](./md/01.Introduction/02/04.Ollama.md)
    - [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    - [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)

- Inférence famille Phi
    - [Inférence Phi sur iOS](./md/01.Introduction/03/iOS_Inference.md)
    - [Inférence Phi sur Android](./md/01.Introduction/03/Android_Inference.md)
    - [Inférence Phi sur Jetson](./md/01.Introduction/03/Jetson_Inference.md)
    - [Inférence Phi sur PC IA](./md/01.Introduction/03/AIPC_Inference.md)
    - [Inférence Phi avec le framework Apple MLX](./md/01.Introduction/03/MLX_Inference.md)
    - [Inférence Phi sur un serveur local](./md/01.Introduction/03/Local_Server_Inference.md)
    - [Inférence Phi sur un serveur distant avec AI Toolkit](./md/01.Introduction/03/Remote_Interence.md)
    - [Inférence Phi avec Rust](./md/01.Introduction/03/Rust_Inference.md)
    - [Inférence Phi--Vision en local](./md/01.Introduction/03/Vision_Inference.md)
    - [Inférence Phi avec Kaito AKS, conteneurs Azure (support officiel)](./md/01.Introduction/03/Kaito_Inference.md)

- [Quantification de la famille Phi](./md/01.Introduction/04/QuantifyingPhi.md)
    - [Quantification de Phi-3.5 / 4 avec llama.cpp](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [Quantification de Phi-3.5 / 4 avec des extensions d'IA générative pour onnxruntime](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Quantification de Phi-3.5 / 4 avec Intel OpenVINO](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Quantification de Phi-3.5 / 4 avec le framework Apple MLX](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

- Évaluation Phi
- [Response AI](./md/01.Introduction/05/ResponsibleAI.md)
    - [Azure AI Foundry pour l'évaluation](./md/01.Introduction/05/AIFoundry.md)
    - [Utiliser Promptflow pour l'évaluation](./md/01.Introduction/05/Promptflow.md)

- RAG avec Azure AI Search
    - [Comment utiliser Phi-4-mini et Phi-4-multimodal (RAG) avec Azure AI Search](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Échantillons de développement d'applications Phi
  - Applications de texte et de chat
    - Échantillons Phi-4 🆕
      - [📓] [Chat avec le modèle Phi-4-mini ONNX](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Chat avec le modèle Phi-4 local ONNX .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Application console .NET pour discuter avec Phi-4 ONNX en utilisant Semantic Kernel](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Échantillons Phi-3 / 3.5
      - [Chatbot local dans le navigateur avec Phi3, ONNX Runtime Web et WebGPU](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [Chat OpenVino](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [Multi-modèle - Interaction entre Phi-3-mini et OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - Créer un wrapper et utiliser Phi-3 avec MLFlow](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [Optimisation de modèle - Comment optimiser le modèle Phi-3-min pour ONNX Runtime Web avec Olive](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [Application WinUI3 avec Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      - [Exemple d'application de notes alimentée par l'IA avec WinUI3 Multi-Modèle](https://github.com/microsoft/ai-powered-notes-winui3-sample)
      - [Affiner et intégrer des modèles Phi-3 personnalisés avec Promptflow](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
      - [Affiner et intégrer des modèles Phi-3 personnalisés avec Promptflow dans Azure AI Foundry](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
      - [Évaluer le modèle affiné Phi-3 / Phi-3.5 dans Azure AI Foundry en se concentrant sur les principes de l'IA responsable de Microsoft](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
      - [📓] [Échantillon de prédiction linguistique Phi-3.5-mini-instruct (Chinois/Anglais)](../../md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
      - [Chatbot RAG WebGPU avec Phi-3.5-Instruct](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
      - [Utiliser le GPU Windows pour créer une solution Promptflow avec Phi-3.5-Instruct ONNX](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
      - [Créer une application Android en utilisant Microsoft Phi-3.5 tflite](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
      - [Exemple de Q&R .NET utilisant le modèle local ONNX Phi-3 avec Microsoft.ML.OnnxRuntime](../../md/04.HOL/dotnet/src/LabsPhi301)
      - [Application console .NET pour discuter avec Semantic Kernel et Phi-3](../../md/04.HOL/dotnet/src/LabsPhi302)

  - Échantillons de code basés sur le SDK d'inférence Azure AI
    - Échantillons Phi-4 🆕
      - [📓] [Générer du code de projet en utilisant Phi-4-multimodal](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
    - Échantillons Phi-3 / 3.5
      - [Créer votre propre chat GitHub Copilot dans Visual Studio Code avec Microsoft Phi-3 Family](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
      - [Créer votre propre agent de chat Copilot dans Visual Studio Code avec Phi-3.5 et les modèles GitHub](./md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

  - Échantillons de raisonnement avancé
    - Échantillons Phi-4 🆕
      - [📓] [Échantillons de raisonnement Phi-4-mini](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)

  - Démos
      - [Démos Phi-4-mini hébergées sur Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
      - [Démos Phi-4-multimodal hébergées sur Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
  - Échantillons de vision
    - Échantillons Phi-4 🆕
      - [📓] [Utiliser Phi-4-multimodal pour lire des images et générer du code](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md)
    - Échantillons Phi-3 / 3.5
- [📓][Phi-3-vision-Image texte vers texte](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)  
  - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)  
  - [📓][Phi-3-vision CLIP Embedding](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)  
  - [DEMO : Phi-3 Recycling](https://github.com/jennifermarsman/PhiRecycling/)  
  - [Phi-3-vision - Assistant visuel linguistique - avec Phi3-Vision et OpenVINO](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)  
  - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)  
  - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)  
  - [📓][Exemple multi-images ou multi-frames Phi-3.5 Vision](../../md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)  
  - [Phi-3 Vision Modèle ONNX local utilisant Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi303)  
  - [Modèle ONNX local basé sur un menu utilisant Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi304)  

- Échantillons audio  
  - Échantillons Phi-4 🆕  
    - [📓] [Extraction de transcriptions audio avec Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Transciption/README.md)  
    - [📓] [Échantillon audio Phi-4-multimodal](../../md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)  
    - [📓] [Échantillon de traduction vocale Phi-4-multimodal](../../md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)  
    - [Application console .NET utilisant Phi-4-multimodal Audio pour analyser un fichier audio et générer une transcription](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)  

- Échantillons MOE  
  - Échantillons Phi-3 / 3.5  
    - [📓] [Modèles Mixture of Experts (MoEs) Phi-3.5 Exemple de réseaux sociaux](../../md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)  
    - [📓] [Construction d'un pipeline Retrieval-Augmented Generation (RAG) avec NVIDIA NIM Phi-3 MOE, Azure AI Search, et LlamaIndex](../../md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)  

- Échantillons d'appel de fonctions  
  - Échantillons Phi-4 🆕  
    - [📓] [Utilisation de l'appel de fonctions avec Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)  
    - [📓] [Utilisation de l'appel de fonctions pour créer des multi-agents avec Phi-4-mini](../../md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)  
    - [📓] [Utilisation de l'appel de fonctions avec Ollama](../../md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)  

- Échantillons de mixage multimodal  
  - Échantillons Phi-4 🆕  
    - [📓] [Utilisation de Phi-4-multimodal comme journaliste technologique](../../md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)  
    - [Application console .NET utilisant Phi-4-multimodal pour analyser des images](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)  

- Échantillons de fine-tuning Phi  
  - [Scénarios de fine-tuning](./md/03.FineTuning/FineTuning_Scenarios.md)  
  - [Fine-tuning vs RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)  
  - [Fine-tuning : Permettre à Phi-3 de devenir un expert de l'industrie](./md/03.FineTuning/LetPhi3gotoIndustriy.md)  
  - [Fine-tuning Phi-3 avec AI Toolkit pour VS Code](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)  
  - [Fine-tuning Phi-3 avec Azure Machine Learning Service](./md/03.FineTuning/Introduce_AzureML.md)  
  - [Fine-tuning Phi-3 avec Lora](./md/03.FineTuning/FineTuning_Lora.md)  
  - [Fine-tuning Phi-3 avec QLora](./md/03.FineTuning/FineTuning_Qlora.md)  
  - [Fine-tuning Phi-3 avec Azure AI Foundry](./md/03.FineTuning/FineTuning_AIFoundry.md)  
  - [Fine-tuning Phi-3 avec Azure ML CLI/SDK](./md/03.FineTuning/FineTuning_MLSDK.md)  
- [Ajustement fin avec Microsoft Olive](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)  
  - [Atelier pratique : Ajustement fin avec Microsoft Olive](./md/03.FineTuning/olive-lab/readme.md)  
  - [Ajustement fin de Phi-3-vision avec Weights and Bias](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)  
  - [Ajustement fin de Phi-3 avec le framework Apple MLX](./md/03.FineTuning/FineTuning_MLX.md)  
  - [Ajustement fin de Phi-3-vision (support officiel)](./md/03.FineTuning/FineTuning_Vision.md)  
  - [Ajustement fin de Phi-3 avec Kaito AKS, Azure Containers (support officiel)](./md/03.FineTuning/FineTuning_Kaito.md)  
  - [Ajustement fin de Phi-3 et 3.5 Vision](https://github.com/2U1/Phi3-Vision-Finetune)  

- Atelier pratique  
  - [Explorer les modèles de pointe : LLMs, SLMs, développement local et plus](https://github.com/microsoft/aitour-exploring-cutting-edge-models)  
  - [Libérer le potentiel du NLP : Ajustement fin avec Microsoft Olive](https://github.com/azure/Ignite_FineTuning_workshop)  

- Articles de recherche académique et publications  
  - [Textbooks Are All You Need II : rapport technique phi-1.5](https://arxiv.org/abs/2309.05463)  
  - [Rapport technique Phi-3 : un modèle linguistique performant localement sur votre téléphone](https://arxiv.org/abs/2404.14219)  
  - [Rapport technique Phi-4](https://arxiv.org/abs/2412.08905)  
  - [Rapport technique Phi-4-Mini : modèles linguistiques multimodaux compacts mais puissants via Mixture-of-LoRAs](https://arxiv.org/abs/2503.01743)  
  - [Optimisation des petits modèles linguistiques pour les appels de fonctions dans les véhicules](https://arxiv.org/abs/2501.02342)  
  - [(WhyPHI) Ajustement fin de PHI-3 pour les questions à choix multiples : méthodologie, résultats et défis](https://arxiv.org/abs/2501.01588)  

## Utilisation des modèles Phi  

### Phi sur Azure AI Foundry  

Vous pouvez apprendre à utiliser Microsoft Phi et à créer des solutions de bout en bout sur vos différents appareils matériels. Pour expérimenter Phi par vous-même, commencez par tester les modèles et personnalisez Phi pour vos scénarios en utilisant le [Catalogue de modèles Azure AI Foundry](https://aka.ms/phi3-azure-ai). Vous pouvez en apprendre davantage dans la section Démarrage avec [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md).  

**Playground**  
Chaque modèle dispose d’un espace dédié pour tester le modèle [Azure AI Playground](https://aka.ms/try-phi3).  

### Phi sur les modèles GitHub  

Vous pouvez apprendre à utiliser Microsoft Phi et à créer des solutions de bout en bout sur vos différents appareils matériels. Pour expérimenter Phi par vous-même, commencez par tester le modèle et personnalisez Phi pour vos scénarios en utilisant le [Catalogue de modèles GitHub](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo). Vous pouvez en apprendre davantage dans la section Démarrage avec [Catalogue de modèles GitHub](/md/02.QuickStart/GitHubModel_QuickStart.md).  

**Playground**  
Chaque modèle dispose d’un [espace dédié pour tester le modèle](/md/02.QuickStart/GitHubModel_QuickStart.md).  

### Phi sur Hugging Face  

Vous pouvez également trouver le modèle sur [Hugging Face](https://huggingface.co/microsoft).  

**Playground**  
[Playground de Hugging Chat](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)  

## IA Responsable  

Microsoft s’engage à aider ses clients à utiliser ses produits d’IA de manière responsable, à partager ses apprentissages et à établir des partenariats fondés sur la confiance grâce à des outils comme les Notes de Transparence et les Évaluations d’Impact. Beaucoup de ces ressources sont disponibles à [https://aka.ms/RAI](https://aka.ms/RAI).  
L’approche de Microsoft en matière d’IA responsable repose sur nos principes d’IA : équité, fiabilité et sécurité, confidentialité et protection, inclusion, transparence et responsabilité.  

Les modèles de langage naturel, d’image et de parole à grande échelle – comme ceux utilisés dans cet exemple – peuvent potentiellement se comporter de manière injuste, peu fiable ou offensante, causant ainsi des préjudices. Veuillez consulter la [note de transparence du service Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) pour être informé des risques et des limitations.  

L’approche recommandée pour atténuer ces risques consiste à inclure un système de sécurité dans votre architecture capable de détecter et de prévenir les comportements nuisibles. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) offre une couche de protection indépendante, capable de détecter les contenus nuisibles générés par les utilisateurs et par l’IA dans les applications et services. Azure AI Content Safety comprend des API pour le texte et les images permettant de détecter les contenus préjudiciables. Au sein d’Azure AI Foundry, le service Content Safety vous permet de visualiser, explorer et tester des exemples de code pour détecter les contenus nuisibles à travers différentes modalités. La [documentation de démarrage rapide](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) vous guide pour effectuer des requêtes au service.  

Un autre aspect à prendre en compte est la performance globale de l’application. Avec des applications multimodales et multi-modèles, la performance signifie que le système répond à vos attentes ainsi qu’à celles de vos utilisateurs, y compris en évitant de générer des résultats nuisibles. Il est important d’évaluer la performance globale de votre application en utilisant les [évaluateurs de performance et qualité, ainsi que de risques et sécurité](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in). Vous avez également la possibilité de créer et d’évaluer avec des [évaluateurs personnalisés](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators).  
Vous pouvez évaluer votre application d'IA dans votre environnement de développement en utilisant le [SDK d'évaluation Azure AI](https://microsoft.github.io/promptflow/index.html). En fournissant soit un ensemble de données de test, soit une cible, les générations de votre application d'IA générative sont mesurées quantitativement avec des évaluateurs intégrés ou des évaluateurs personnalisés de votre choix. Pour commencer avec le SDK d'évaluation Azure AI afin d'évaluer votre système, vous pouvez suivre le [guide de démarrage rapide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Une fois que vous avez exécuté une évaluation, vous pouvez [visualiser les résultats dans Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Marques déposées

Ce projet peut contenir des marques déposées ou des logos pour des projets, produits ou services. L'utilisation autorisée des marques ou logos de Microsoft est soumise aux [Directives sur les marques et la marque de Microsoft](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) et doit les respecter. L'utilisation des marques ou logos de Microsoft dans des versions modifiées de ce projet ne doit pas provoquer de confusion ou impliquer un parrainage de Microsoft. Toute utilisation de marques ou logos tiers est soumise aux politiques de ces tiers.

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, une traduction humaine professionnelle est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.