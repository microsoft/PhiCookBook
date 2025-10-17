<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4987daf30687ad3850757c9eae3f5411",
  "translation_date": "2025-10-17T10:02:46+00:00",
  "source_file": "README.md",
  "language_code": "fr"
}
-->
# Phi Cookbook : Exemples pratiques avec les modèles Phi de Microsoft

[![Ouvrir et utiliser les exemples dans GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Ouvrir dans Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![Contributeurs GitHub](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![Problèmes GitHub](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![Pull-requests GitHub](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PRs Bienvenus](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![Observateurs GitHub](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![Forks GitHub](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![Étoiles GitHub](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi est une série de modèles d'IA open source développés par Microsoft.

Phi est actuellement le modèle de langage compact (SLM) le plus puissant et le plus économique, avec d'excellents résultats dans les benchmarks pour les langues multiples, le raisonnement, la génération de texte/chat, le codage, les images, l'audio et d'autres scénarios.

Vous pouvez déployer Phi dans le cloud ou sur des appareils périphériques, et vous pouvez facilement créer des applications d'IA générative avec une puissance de calcul limitée.

Suivez ces étapes pour commencer à utiliser ces ressources :
1. **Forkez le dépôt** : Cliquez [![Forks GitHub](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **Clonez le dépôt** : `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Rejoignez la communauté Discord Microsoft AI et rencontrez des experts et d'autres développeurs**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![couverture](../../imgs/cover.png)

### 🌐 Support multilingue

#### Supporté via GitHub Action (Automatisé et toujours à jour)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabe](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgare](../bg/README.md) | [Birman (Myanmar)](../my/README.md) | [Chinois (Simplifié)](../zh/README.md) | [Chinois (Traditionnel, Hong Kong)](../hk/README.md) | [Chinois (Traditionnel, Macao)](../mo/README.md) | [Chinois (Traditionnel, Taïwan)](../tw/README.md) | [Croate](../hr/README.md) | [Tchèque](../cs/README.md) | [Danois](../da/README.md) | [Néerlandais](../nl/README.md) | [Estonien](../et/README.md) | [Finnois](../fi/README.md) | [Français](./README.md) | [Allemand](../de/README.md) | [Grec](../el/README.md) | [Hébreu](../he/README.md) | [Hindi](../hi/README.md) | [Hongrois](../hu/README.md) | [Indonésien](../id/README.md) | [Italien](../it/README.md) | [Japonais](../ja/README.md) | [Coréen](../ko/README.md) | [Lituanien](../lt/README.md) | [Malais](../ms/README.md) | [Marathi](../mr/README.md) | [Népalais](../ne/README.md) | [Norvégien](../no/README.md) | [Persan (Farsi)](../fa/README.md) | [Polonais](../pl/README.md) | [Portugais (Brésil)](../br/README.md) | [Portugais (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Roumain](../ro/README.md) | [Russe](../ru/README.md) | [Serbe (Cyrillique)](../sr/README.md) | [Slovaque](../sk/README.md) | [Slovène](../sl/README.md) | [Espagnol](../es/README.md) | [Swahili](../sw/README.md) | [Suédois](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamoul](../ta/README.md) | [Thaï](../th/README.md) | [Turc](../tr/README.md) | [Ukrainien](../uk/README.md) | [Ourdou](../ur/README.md) | [Vietnamien](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## Table des matières

- Introduction
  - [Bienvenue dans la famille Phi](./md/01.Introduction/01/01.PhiFamily.md)
  - [Configurer votre environnement](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [Comprendre les technologies clés](./md/01.Introduction/01/01.Understandingtech.md)
  - [Sécurité de l'IA pour les modèles Phi](./md/01.Introduction/01/01.AISafety.md)
  - [Support matériel pour Phi](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Modèles Phi et disponibilité sur différentes plateformes](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Utiliser Guidance-ai et Phi](./md/01.Introduction/01/01.Guidance.md)
  - [Modèles sur le Marketplace GitHub](https://github.com/marketplace/models)
  - [Catalogue de modèles Azure AI](https://ai.azure.com)

- Inférence de Phi dans différents environnements
    - [Hugging face](./md/01.Introduction/02/01.HF.md)
    - [Modèles GitHub](./md/01.Introduction/02/02.GitHubModel.md)
    - [Catalogue de modèles Azure AI Foundry](./md/01.Introduction/02/03.AzureAIFoundry.md)
    - [Ollama](./md/01.Introduction/02/04.Ollama.md)
    - [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    - [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    - [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md)

- Inférence de la famille Phi
    - [Inférence de Phi sur iOS](./md/01.Introduction/03/iOS_Inference.md)
    - [Inférence de Phi sur Android](./md/01.Introduction/03/Android_Inference.md)
    - [Inférence de Phi sur Jetson](./md/01.Introduction/03/Jetson_Inference.md)
    - [Inférence de Phi sur PC AI](./md/01.Introduction/03/AIPC_Inference.md)
    - [Inférence de Phi avec le framework Apple MLX](./md/01.Introduction/03/MLX_Inference.md)
    - [Inférence de Phi sur serveur local](./md/01.Introduction/03/Local_Server_Inference.md)
    - [Inférence de Phi sur serveur distant avec AI Toolkit](./md/01.Introduction/03/Remote_Interence.md)
    - [Inférence de Phi avec Rust](./md/01.Introduction/03/Rust_Inference.md)
    - [Inférence de Phi--Vision en local](./md/01.Introduction/03/Vision_Inference.md)
    - [Inférence de Phi avec Kaito AKS, conteneurs Azure (support officiel)](./md/01.Introduction/03/Kaito_Inference.md)
- [Quantification de la famille Phi](./md/01.Introduction/04/QuantifyingPhi.md)
    - [Quantification de Phi-3.5 / 4 avec llama.cpp](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [Quantification de Phi-3.5 / 4 avec les extensions d'IA générative pour onnxruntime](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Quantification de Phi-3.5 / 4 avec Intel OpenVINO](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Quantification de Phi-3.5 / 4 avec le framework Apple MLX](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

- Évaluation de Phi
    - [IA Responsable](./md/01.Introduction/05/ResponsibleAI.md)
    - [Azure AI Foundry pour l'évaluation](./md/01.Introduction/05/AIFoundry.md)
    - [Utilisation de Promptflow pour l'évaluation](./md/01.Introduction/05/Promptflow.md)

- RAG avec Azure AI Search
    - [Comment utiliser Phi-4-mini et Phi-4-multimodal (RAG) avec Azure AI Search](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Exemples de développement d'applications Phi
  - Applications de texte et de chat
    - Exemples Phi-4 🆕
      - [📓] [Chat avec le modèle Phi-4-mini ONNX](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Chat avec le modèle Phi-4 local ONNX .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Application console .NET de chat avec Phi-4 ONNX utilisant Semantic Kernel](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Exemples Phi-3 / 3.5
      - [Chatbot local dans le navigateur utilisant Phi3, ONNX Runtime Web et WebGPU](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [Chat OpenVino](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [Modèle interactif - Phi-3-mini et OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - Construire un wrapper et utiliser Phi-3 avec MLFlow](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [Optimisation de modèle - Comment optimiser le modèle Phi-3-min pour ONNX Runtime Web avec Olive](https://github.com/microsoft/Olive/tree/main/examples/phi3)
- [Application WinUI3 avec Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
- [Exemple d'application de prise de notes alimentée par l'IA avec WinUI3](https://github.com/microsoft/ai-powered-notes-winui3-sample)
- [Affiner et intégrer des modèles Phi-3 personnalisés avec Prompt flow](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
- [Affiner et intégrer des modèles Phi-3 personnalisés avec Prompt flow dans Azure AI Foundry](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
- [Évaluer le modèle Phi-3 / Phi-3.5 affiné dans Azure AI Foundry en mettant l'accent sur les principes d'IA responsable de Microsoft](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
- [📓] [Exemple de prédiction linguistique Phi-3.5-mini-instruct (Chinois/Anglais)](../../md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
- [Chatbot RAG WebGPU Phi-3.5-Instruct](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
- [Utiliser le GPU Windows pour créer une solution Prompt flow avec Phi-3.5-Instruct ONNX](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
- [Utiliser Microsoft Phi-3.5 tflite pour créer une application Android](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
- [Exemple de Q&A .NET utilisant le modèle local ONNX Phi-3 avec Microsoft.ML.OnnxRuntime](../../md/04.HOL/dotnet/src/LabsPhi301)
- [Application console de chat .NET avec Semantic Kernel et Phi-3](../../md/04.HOL/dotnet/src/LabsPhi302)

- Exemples de code SDK d'inférence Azure AI 
  - Exemples Phi-4 🆕
    - [📓] [Générer du code de projet avec Phi-4-multimodal](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
  - Exemples Phi-3 / 3.5
    - [Créer votre propre chat GitHub Copilot dans Visual Studio Code avec la famille Phi-3 de Microsoft](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
    - [Créer votre propre agent de chat Copilot dans Visual Studio Code avec Phi-3.5 et les modèles GitHub](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

- Exemples de raisonnement avancé
  - Exemples Phi-4 🆕
    - [📓] [Exemples Phi-4-mini-reasoning ou Phi-4-reasoning](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
    - [📓] [Affiner Phi-4-mini-reasoning avec Microsoft Olive](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
    - [📓] [Affiner Phi-4-mini-reasoning avec Apple MLX](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
    - [📓] [Phi-4-mini-reasoning avec les modèles GitHub](../../md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
    - [📓] [Phi-4-mini-reasoning avec les modèles Azure AI Foundry](../../md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
- Démos
    - [Démos Phi-4-mini hébergées sur Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
    - [Démos Phi-4-multimodal hébergées sur Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
- Exemples de vision
  - Exemples Phi-4 🆕
    - [📓] [Utiliser Phi-4-multimodal pour lire des images et générer du code](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
  - Exemples Phi-3 / 3.5
    - [📓][Phi-3-vision-Image texte vers texte](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
    - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
    - [📓][Phi-3-vision CLIP Embedding](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
    - [DEMO : Phi-3 Recycling](https://github.com/jennifermarsman/PhiRecycling/)
    - [Phi-3-vision - Assistant visuel linguistique - avec Phi3-Vision et OpenVINO](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
    - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
    - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
    - [📓][Exemple multi-images ou multi-cadres Phi-3.5 Vision](../../md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
    - [Modèle local ONNX Phi-3 Vision utilisant Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi303)
    - [Modèle local ONNX Phi-3 Vision basé sur un menu utilisant Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi304)

- Exemples de mathématiques
  - Exemples Phi-4-Mini-Flash-Reasoning-Instruct 🆕 [Démo mathématique avec Phi-4-Mini-Flash-Reasoning-Instruct](../../md/02.Application/09.Math/MathDemo.ipynb)

- Exemples audio
  - Exemples Phi-4 🆕
    - [📓] [Extraction de transcriptions audio avec Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
    - [📓] [Exemple audio Phi-4-multimodal](../../md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
    - [📓] [Exemple de traduction vocale Phi-4-multimodal](../../md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
    - [Application console .NET utilisant Phi-4-multimodal Audio pour analyser un fichier audio et générer une transcription](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

- Exemples MOE
  - Exemples Phi-3 / 3.5
    - [📓] [Exemple de modèles Mixture of Experts (MoEs) Phi-3.5 pour les réseaux sociaux](../../md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
    - [📓] [Construire un pipeline de génération augmentée par récupération (RAG) avec NVIDIA NIM Phi-3 MOE, Azure AI Search et LlamaIndex](../../md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)

- Exemples d'appel de fonction
  - Exemples Phi-4 🆕
    - [📓] [Utiliser l'appel de fonction avec Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
    - [📓] [Utiliser l'appel de fonction pour créer des multi-agents avec Phi-4-mini](../../md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
    - [📓] [Utiliser l'appel de fonction avec Ollama](../../md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
    - [📓] [Utiliser l'appel de fonction avec ONNX](../../md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)

- Exemples de mélange multimodal
  - Exemples Phi-4 🆕
    - [📓] [Utiliser Phi-4-multimodal en tant que journaliste technologique](../../md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
    - [Application console .NET utilisant Phi-4-multimodal pour analyser des images](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Exemples d'affinage Phi
  - [Scénarios d'affinage](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [Affinage vs RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [Affinage pour que Phi-3 devienne un expert industriel](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [Affinage de Phi-3 avec AI Toolkit pour VS Code](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Affinage de Phi-3 avec Azure Machine Learning Service](./md/03.FineTuning/Introduce_AzureML.md)
  - [Affinage de Phi-3 avec Lora](./md/03.FineTuning/FineTuning_Lora.md)
  - [Affinage de Phi-3 avec QLora](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Affinage de Phi-3 avec Azure AI Foundry](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Affinage de Phi-3 avec Azure ML CLI/SDK](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Affinage avec Microsoft Olive](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Affinage avec Microsoft Olive Hands-On Lab](./md/03.FineTuning/olive-lab/readme.md)
  - [Affinage de Phi-3-vision avec Weights and Bias](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [Affinage de Phi-3 avec le framework Apple MLX](./md/03.FineTuning/FineTuning_MLX.md)
  - [Affinage de Phi-3-vision (support officiel)](./md/03.FineTuning/FineTuning_Vision.md)
  - [Affinage de Phi-3 avec Kaito AKS, Azure Containers (support officiel)](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Affinage de Phi-3 et 3.5 Vision](https://github.com/2U1/Phi3-Vision-Finetune)

- Laboratoire pratique
  - [Explorer les modèles de pointe : LLMs, SLMs, développement local et plus](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [Libérer le potentiel du NLP : Affinage avec Microsoft Olive](https://github.com/azure/Ignite_FineTuning_workshop)

- Articles de recherche académique et publications
  - [Textbooks Are All You Need II : rapport technique phi-1.5](https://arxiv.org/abs/2309.05463)
  - [Rapport technique Phi-3 : un modèle de langage très performant localement sur votre téléphone](https://arxiv.org/abs/2404.14219)
  - [Rapport technique Phi-4](https://arxiv.org/abs/2412.08905)
  - [Rapport technique Phi-4-Mini : modèles de langage multimodal compacts mais puissants via Mixture-of-LoRAs](https://arxiv.org/abs/2503.01743)
  - [Optimisation des petits modèles de langage pour l'appel de fonctions dans les véhicules](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) Affiner PHI-3 pour répondre à des questions à choix multiples : méthodologie, résultats et défis](https://arxiv.org/abs/2501.01588)
  - [Rapport technique sur le raisonnement Phi-4](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Rapport technique sur le raisonnement Phi-4-mini](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Utilisation des modèles Phi

### Phi sur Azure AI Foundry

Vous pouvez apprendre à utiliser Microsoft Phi et à construire des solutions de bout en bout sur vos différents appareils matériels. Pour découvrir Phi par vous-même, commencez par tester les modèles et personnaliser Phi pour vos scénarios en utilisant le [Catalogue de modèles Azure AI Foundry](https://aka.ms/phi3-azure-ai). Vous pouvez en savoir plus en consultant le guide de démarrage [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md).

**Playground**  
Chaque modèle dispose d'un espace dédié pour tester le modèle [Azure AI Playground](https://aka.ms/try-phi3).

### Phi sur les modèles GitHub

Vous pouvez apprendre à utiliser Microsoft Phi et à construire des solutions de bout en bout sur vos différents appareils matériels. Pour découvrir Phi par vous-même, commencez par tester le modèle et personnaliser Phi pour vos scénarios en utilisant le [Catalogue de modèles GitHub](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo). Vous pouvez en savoir plus en consultant le guide de démarrage [Catalogue de modèles GitHub](/md/02.QuickStart/GitHubModel_QuickStart.md).

**Playground**  
Chaque modèle dispose d'un [espace dédié pour tester le modèle](/md/02.QuickStart/GitHubModel_QuickStart.md).

### Phi sur Hugging Face

Vous pouvez également trouver le modèle sur [Hugging Face](https://huggingface.co/microsoft).

**Playground**  
[Playground Hugging Chat](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct).

## IA Responsable

Microsoft s'engage à aider ses clients à utiliser ses produits d'IA de manière responsable, à partager ses apprentissages et à établir des partenariats basés sur la confiance grâce à des outils tels que les Notes de transparence et les Évaluations d'impact. Beaucoup de ces ressources sont disponibles sur [https://aka.ms/RAI](https://aka.ms/RAI).  
L'approche de Microsoft en matière d'IA responsable repose sur nos principes d'IA : équité, fiabilité et sécurité, confidentialité et sécurité, inclusivité, transparence et responsabilité.

Les modèles de langage naturel, d'image et de parole à grande échelle - comme ceux utilisés dans cet exemple - peuvent potentiellement se comporter de manière injuste, peu fiable ou offensante, causant ainsi des préjudices. Veuillez consulter la [Note de transparence du service Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) pour être informé des risques et des limitations.

L'approche recommandée pour atténuer ces risques est d'inclure un système de sécurité dans votre architecture capable de détecter et de prévenir les comportements nuisibles. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) fournit une couche de protection indépendante, capable de détecter les contenus nuisibles générés par les utilisateurs et par l'IA dans les applications et services. Azure AI Content Safety inclut des API de texte et d'image permettant de détecter les contenus nuisibles. Dans Azure AI Foundry, le service Content Safety vous permet de visualiser, explorer et tester des exemples de code pour détecter les contenus nuisibles dans différents formats. La [documentation de démarrage rapide](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) vous guide pour effectuer des requêtes au service.

Un autre aspect à prendre en compte est la performance globale de l'application. Avec des applications multi-modales et multi-modèles, nous considérons la performance comme la capacité du système à répondre aux attentes de vous et de vos utilisateurs, y compris en évitant de générer des résultats nuisibles. Il est important d'évaluer la performance globale de votre application en utilisant les [Évaluateurs de performance et qualité et de risques et sécurité](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in). Vous avez également la possibilité de créer et d'évaluer avec des [évaluateurs personnalisés](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators).

Vous pouvez évaluer votre application d'IA dans votre environnement de développement en utilisant le [SDK d'évaluation Azure AI](https://microsoft.github.io/promptflow/index.html). À partir d'un jeu de données de test ou d'un objectif, les générations de votre application d'IA générative sont mesurées quantitativement avec des évaluateurs intégrés ou personnalisés de votre choix. Pour commencer avec le SDK d'évaluation Azure AI afin d'évaluer votre système, vous pouvez suivre le [guide de démarrage rapide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Une fois que vous avez exécuté une évaluation, vous pouvez [visualiser les résultats dans Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Marques déposées

Ce projet peut contenir des marques ou logos pour des projets, produits ou services. L'utilisation autorisée des marques ou logos Microsoft est soumise et doit respecter les [Directives sur les marques et logos de Microsoft](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).  
L'utilisation des marques ou logos Microsoft dans des versions modifiées de ce projet ne doit pas causer de confusion ou impliquer un parrainage de Microsoft. Toute utilisation de marques ou logos tiers est soumise aux politiques de ces tiers.

## Obtenir de l'aide

Si vous êtes bloqué ou avez des questions sur la création d'applications d'IA, rejoignez :

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

Si vous avez des retours sur le produit ou rencontrez des erreurs lors de la création, visitez :

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.