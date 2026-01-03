<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ef3a50368712b1a7483d0def1f70c490",
  "translation_date": "2025-12-21T09:37:48+00:00",
  "source_file": "README.md",
  "language_code": "fr"
}
-->
# Phi Cookbook: Exemples pratiques avec les modèles Phi de Microsoft

[![Ouvrez et utilisez les exemples dans GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Ouvrir dans Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![Contributeurs GitHub](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![Problèmes GitHub](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![Pull-requests GitHub](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PRs Bienvenus](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![Observateurs GitHub](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![Forks GitHub](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![Étoiles GitHub](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Discord Microsoft Azure AI Foundry](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi est une série de modèles d'IA open source développés par Microsoft. 

Phi est actuellement le modèle de langage petit (SLM) le plus puissant et le plus rentable, avec d'excellents benchmarks en multilingue, raisonnement, génération de texte/chat, codage, images, audio et autres scénarios. 

Vous pouvez déployer Phi dans le cloud ou sur des appareils en périphérie, et vous pouvez facilement construire des applications d'IA générative avec une puissance de calcul limitée.

Suivez ces étapes pour commencer à utiliser ces ressources :
1. **Forker le dépôt**: Cliquez [![Forks GitHub](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **Cloner le dépôt**:   `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Rejoignez la communauté Discord Microsoft AI et rencontrez des experts et d'autres développeurs**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![couverture](../../translated_images/cover.eb18d1b9605d754b.fr.png)

### 🌐 Prise en charge multilingue

#### Pris en charge via GitHub Action (Automatisé et Toujours à jour)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabe](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgare](../bg/README.md) | [Birmane (Myanmar)](../my/README.md) | [Chinois (Simplifié)](../zh/README.md) | [Chinois (Traditionnel, Hong Kong)](../hk/README.md) | [Chinois (Traditionnel, Macao)](../mo/README.md) | [Chinois (Traditionnel, Taïwan)](../tw/README.md) | [Croate](../hr/README.md) | [Tchèque](../cs/README.md) | [Danois](../da/README.md) | [Néerlandais](../nl/README.md) | [Estonien](../et/README.md) | [Finnois](../fi/README.md) | [Français](./README.md) | [Allemand](../de/README.md) | [Grec](../el/README.md) | [Hébreu](../he/README.md) | [Hindi](../hi/README.md) | [Hongrois](../hu/README.md) | [Indonésien](../id/README.md) | [Italien](../it/README.md) | [Japonais](../ja/README.md) | [Kannada](../kn/README.md) | [Coréen](../ko/README.md) | [Lituanien](../lt/README.md) | [Malais](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Népalais](../ne/README.md) | [Pidgin nigérian](../pcm/README.md) | [Norvégien](../no/README.md) | [Persan (Farsi)](../fa/README.md) | [Polonais](../pl/README.md) | [Portugais (Brésil)](../br/README.md) | [Portugais (Portugal)](../pt/README.md) | [Pendjabi (Gurmukhi)](../pa/README.md) | [Roumain](../ro/README.md) | [Russe](../ru/README.md) | [Serbe (Cyrillique)](../sr/README.md) | [Slovaque](../sk/README.md) | [Slovène](../sl/README.md) | [Espagnol](../es/README.md) | [Swahili](../sw/README.md) | [Suédois](../sv/README.md) | [Tagalog (Philippines)](../tl/README.md) | [Tamoul](../ta/README.md) | [Télougou](../te/README.md) | [Thaï](../th/README.md) | [Turc](../tr/README.md) | [Ukrainien](../uk/README.md) | [Ourdou](../ur/README.md) | [Vietnamien](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## Table des matières

- Introduction
  - [Bienvenue dans la famille Phi](./md/01.Introduction/01/01.PhiFamily.md)
  - [Configuration de votre environnement](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [Comprendre les technologies clés](./md/01.Introduction/01/01.Understandingtech.md)
  - [Sécurité de l'IA pour les modèles Phi](./md/01.Introduction/01/01.AISafety.md)
  - [Support matériel pour Phi](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Modèles Phi et disponibilité selon les plateformes](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Utiliser Guidance-ai et Phi](./md/01.Introduction/01/01.Guidance.md)
  - [Modèles GitHub Marketplace](https://github.com/marketplace/models)
  - [Catalogue de modèles Azure AI](https://ai.azure.com)

- Inférence de Phi dans différents environnements
    -  [Hugging Face](./md/01.Introduction/02/01.HF.md)
    -  [Modèles GitHub](./md/01.Introduction/02/02.GitHubModel.md)
    -  [Catalogue de modèles Azure AI Foundry](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    -  [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md)

- Inférence de la famille Phi
    - [Inférence de Phi sur iOS](./md/01.Introduction/03/iOS_Inference.md)
    - [Inférence de Phi sur Android](./md/01.Introduction/03/Android_Inference.md)
    - [Inférence de Phi sur Jetson](./md/01.Introduction/03/Jetson_Inference.md)
    - [Inférence de Phi sur AI PC](./md/01.Introduction/03/AIPC_Inference.md)
    - [Inférence de Phi avec le framework Apple MLX](./md/01.Introduction/03/MLX_Inference.md)
    - [Inférence de Phi sur serveur local](./md/01.Introduction/03/Local_Server_Inference.md)
    - [Inférence de Phi sur serveur distant en utilisant AI Toolkit](./md/01.Introduction/03/Remote_Interence.md)
    - [Inférence de Phi avec Rust](./md/01.Introduction/03/Rust_Inference.md)
    - [Inférence Phi--Vision en local](./md/01.Introduction/03/Vision_Inference.md)
    - [Inférence de Phi avec Kaito AKS, Azure Containers (prise en charge officielle)](./md/01.Introduction/03/Kaito_Inference.md)
-  [Quantification de la famille Phi](./md/01.Introduction/04/QuantifyingPhi.md)
    - [Quantification de Phi-3.5 / 4 en utilisant llama.cpp](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [Quantification de Phi-3.5 / 4 en utilisant les extensions Generative AI pour onnxruntime](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Quantification de Phi-3.5 / 4 en utilisant Intel OpenVINO](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Quantification de Phi-3.5 / 4 en utilisant le framework Apple MLX](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

-  Évaluation de Phi
    - [IA responsable](./md/01.Introduction/05/ResponsibleAI.md)
    - [Azure AI Foundry pour l'évaluation](./md/01.Introduction/05/AIFoundry.md)
    - [Utiliser Promptflow pour l'évaluation](./md/01.Introduction/05/Promptflow.md)
 
- RAG avec Azure AI Search
    - [Comment utiliser Phi-4-mini et Phi-4-multimodal(RAG) avec Azure AI Search](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Exemples d'applications Phi
  - Applications texte et chat
    - Exemples Phi-4 🆕
      - [📓] [Chat avec le modèle Phi-4-mini ONNX](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Chat avec le modèle ONNX Phi-4 local (.NET)](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Application console .NET de chat avec Phi-4 ONNX utilisant Semantic Kernel](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Exemples Phi-3 / 3.5
      - [Chatbot local dans le navigateur utilisant Phi3, ONNX Runtime Web et WebGPU](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [Chat OpenVINO](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [Multi-modèle - Phi-3-mini interactif et OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - Création d'un wrapper et utilisation de Phi-3 avec MLFlow](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [Optimisation du modèle - Comment optimiser le modèle Phi-3-min pour ONNX Runtime Web avec Olive](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [Application WinUI3 avec Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      -[Exemple d'application WinUI3 de notes alimentée par l'IA multi-modèle](https://github.com/microsoft/ai-powered-notes-winui3-sample)
      - [Affiner et intégrer des modèles Phi-3 personnalisés avec Prompt flow](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
      - [Affiner et intégrer des modèles Phi-3 personnalisés avec Prompt flow dans Azure AI Foundry](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
      - [Évaluer le modèle Phi-3 / Phi-3.5 affiné dans Azure AI Foundry en se concentrant sur les principes d'IA responsable de Microsoft](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
      - [📓] [Exemple de prédiction linguistique Phi-3.5-mini-instruct (chinois/anglais)](./md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
      - [Chatbot RAG Phi-3.5-Instruct WebGPU](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
      - [Utiliser le GPU Windows pour créer une solution Prompt flow avec Phi-3.5-Instruct ONNX](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
      - [Utiliser Microsoft Phi-3.5 tflite pour créer une application Android](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
      - [Exemple Q&A .NET utilisant un modèle ONNX Phi-3 local avec Microsoft.ML.OnnxRuntime](../../md/04.HOL/dotnet/src/LabsPhi301)
      - [Application console de chat .NET avec Semantic Kernel et Phi-3](../../md/04.HOL/dotnet/src/LabsPhi302)

  - Exemples basés sur le code pour Azure AI Inference SDK 
    - Exemples Phi-4 🆕 
      - [📓] [Générer le code du projet en utilisant Phi-4-multimodal](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
    - Exemples Phi-3 / 3.5
      - [Créez votre propre Chat GitHub Copilot pour Visual Studio Code avec la famille Microsoft Phi-3](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
      - [Créez votre propre agent Chat Copilot pour Visual Studio Code avec Phi-3.5 par GitHub Models](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

  - Exemples de raisonnement avancé
    - Exemples Phi-4 🆕 
      - [📓] [Exemples Phi-4-mini-reasoning ou Phi-4-reasoning](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
      - [📓] [Affinage de Phi-4-mini-reasoning avec Microsoft Olive](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Affinage de Phi-4-mini-reasoning avec Apple MLX](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Phi-4-mini-reasoning avec GitHub Models](./md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
      - [📓] [Phi-4-mini-reasoning avec Azure AI Foundry Models](./md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
  - Démos
      - [Démos Phi-4-mini hébergées sur Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
      - [Démos Phi-4-multimodal hébergées sur Hugginge Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
  - Exemples Vision
    - Exemples Phi-4 🆕 
      - [📓] [Utiliser Phi-4-multimodal pour lire des images et générer du code](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
    - Exemples Phi-3 / 3.5
      -  [📓][Phi-3-vision Image texte à texte](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
      - [📓][Phi-3-vision CLIP Embedding](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [DEMO : Phi-3 Recycling](https://github.com/jennifermarsman/PhiRecycling/)
      - [Phi-3-vision - Assistant de langage visuel - avec Phi3-Vision et OpenVINO](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
      - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
      - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
      - [📓][Exemple Phi-3.5 Vision multi-frame ou multi-image](./md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
      - [Modèle ONNX local Phi-3 Vision utilisant Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi303)
      - [Modèle ONNX local Phi-3 Vision basé sur menu utilisant Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi304)

  - Exemples Mathématiques
    -  Exemples Phi-4-Mini-Flash-Reasoning-Instruct 🆕 [Démonstration mathématique avec Phi-4-Mini-Flash-Reasoning-Instruct](./md/02.Application/09.Math/MathDemo.ipynb)

  - Exemples audio
    - Exemples Phi-4 🆕 
      - [📓] [Extraction de transcriptions audio avec Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
      - [📓] [Exemple audio Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
      - [📓] [Exemple de traduction de la parole Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
      - [.NET console application using Phi-4-multimodal Audio to analyze an audio file and generate transcript](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

  - Exemples MOE
    - Exemples Phi-3 / 3.5
      - [📓] [Exemple de médias sociaux pour les modèles Mixture of Experts Phi-3.5 (MoEs)](./md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
      - [📓] [Construire un pipeline de Retrieval-Augmented Generation (RAG) avec NVIDIA NIM Phi-3 MOE, Azure AI Search et LlamaIndex](./md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)
      - 
  - Exemples d'appel de fonction
    - Exemples Phi-4 🆕 
      -  [📓] [Utiliser l'appel de fonction avec Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
      -  [📓] [Utiliser l'appel de fonction pour créer des multi-agents avec Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
      -  [📓] [Utiliser l'appel de fonction avec Ollama](./md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
      -  [📓] [Utiliser l'appel de fonction avec ONNX](./md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)
  - Exemples de mélange multimodal
    - Exemples Phi-4 🆕 
      -  [📓] [Utiliser Phi-4-multimodal en tant que journaliste technologique](./md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
      - [.NET console application using Phi-4-multimodal to analyze images](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Exemples d'affinage Phi
  - [Scénarios d'affinage](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [Affinage vs RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [Affinage - Faire de Phi-3 un expert industriel](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [Affinage de Phi-3 avec AI Toolkit pour VS Code](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Affinage de Phi-3 avec Azure Machine Learning Service](./md/03.FineTuning/Introduce_AzureML.md)
  - [Affinage de Phi-3 avec Lora](./md/03.FineTuning/FineTuning_Lora.md)
  - [Affinage de Phi-3 avec QLora](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Affinage de Phi-3 avec Azure AI Foundry](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Affinage de Phi-3 avec Azure ML CLI/SDK](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Affinage avec Microsoft Olive](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Atelier pratique d'affinage avec Microsoft Olive](./md/03.FineTuning/olive-lab/readme.md)
  - [Affinage de Phi-3-vision avec Weights and Bias](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [Affinage de Phi-3 avec le framework Apple MLX](./md/03.FineTuning/FineTuning_MLX.md)
  - [Affinage de Phi-3-vision (support officiel)](./md/03.FineTuning/FineTuning_Vision.md)
  - [Affinage de Phi-3 avec Kaito AKS , Azure Containers (support officiel)](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Affinage de Phi-3 et Phi-3.5 Vision](https://github.com/2U1/Phi3-Vision-Finetune)

- Atelier pratique
  - [Explorer des modèles de pointe : LLMs, SLMs, développement local et plus](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [Libérer le potentiel du NLP : Affinage avec Microsoft Olive](https://github.com/azure/Ignite_FineTuning_workshop)

- Articles de recherche et publications académiques
  - [Textbooks Are All You Need II : rapport technique phi-1.5](https://arxiv.org/abs/2309.05463)
  - [Rapport technique Phi-3 : Un modèle de langage très performant localement sur votre téléphone](https://arxiv.org/abs/2404.14219)
  - [Rapport technique Phi-4](https://arxiv.org/abs/2412.08905)
  - [Rapport technique Phi-4-Mini : modèles linguistiques multimodaux compacts mais puissants via Mixture-of-LoRAs](https://arxiv.org/abs/2503.01743)
  - [Optimisation des petits modèles linguistiques pour l'appel de fonctions à bord des véhicules](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) Ajustement fin de PHI-3 pour les questions à choix multiple : méthodologie, résultats et défis](https://arxiv.org/abs/2501.01588)
  - [Rapport technique Phi-4-reasoning](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Rapport technique Phi-4-mini-reasoning](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Utilisation des modèles Phi

### Phi sur Azure AI Foundry

Vous pouvez apprendre à utiliser Microsoft Phi et à concevoir des solutions E2E sur vos différents appareils matériels. Pour découvrir Phi par vous-même, commencez par expérimenter les modèles et personnaliser Phi pour vos scénarios en utilisant le [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai) vous pouvez en savoir plus dans Getting Started with [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md)

**Playground**
Chaque modèle dispose d'un playground dédié pour tester le modèle [Azure AI Playground](https://aka.ms/try-phi3).

### Phi sur GitHub Models

Vous pouvez apprendre à utiliser Microsoft Phi et à concevoir des solutions E2E sur vos différents appareils matériels. Pour découvrir Phi par vous-même, commencez par expérimenter le modèle et personnaliser Phi pour vos scénarios en utilisant le [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) vous pouvez en savoir plus dans Getting Started with [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md)

**Playground**
Chaque modèle dispose d'un [playground dédié pour tester le modèle](/md/02.QuickStart/GitHubModel_QuickStart.md).

### Phi sur Hugging Face

Vous pouvez également trouver le modèle sur [Hugging Face](https://huggingface.co/microsoft)

**Playground**
 [Hugging Chat playground](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

 ## 🎒 Other Courses

Notre équipe propose d'autres cours ! Découvrez :

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j for Beginners](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js for Beginners](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

---

### Azure / Edge / MCP / Agents
[![AZD for Beginners](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI for Beginners](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP for Beginners](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Agents for Beginners](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Generative AI Series
[![Generative AI for Beginners](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generative AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generative AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generative AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Core Learning
[![ML for Beginners](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science for Beginners](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI for Beginners](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Cybersecurity for Beginners](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Web Dev for Beginners](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT for Beginners](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR Development for Beginners](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot Series
[![Copilot for AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## IA responsable 

Microsoft s'engage à aider ses clients à utiliser nos produits d'IA de manière responsable, à partager nos enseignements et à établir des partenariats fondés sur la confiance grâce à des outils tels que les Transparency Notes et les Impact Assessments. Beaucoup de ces ressources sont disponibles sur [https://aka.ms/RAI](https://aka.ms/RAI).
L'approche de Microsoft en matière d'IA responsable repose sur nos principes d'IA : équité, fiabilité et sécurité, confidentialité et sécurité, inclusion, transparence et responsabilité.

Les modèles à grande échelle de langage naturel, d'image et de parole — comme ceux utilisés dans cet exemple — peuvent potentiellement se comporter de façon injuste, peu fiable ou offensante, provoquant ainsi des préjudices. Veuillez consulter la [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) pour vous informer sur les risques et les limites.

La démarche recommandée pour atténuer ces risques est d'inclure un système de sécurité dans votre architecture capable de détecter et d'empêcher les comportements nuisibles. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) fournit une couche de protection indépendante, capable de détecter le contenu nuisible généré par les utilisateurs et par l'IA dans les applications et services. Azure AI Content Safety inclut des API pour le texte et l'image qui vous permettent de détecter du contenu potentiellement préjudiciable. Au sein d'Azure AI Foundry, le service Content Safety vous permet de visualiser, d'explorer et d'essayer des exemples de code pour détecter du contenu nuisible à travers différentes modalités. La [documentation quickstart suivante](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) vous guide pour effectuer des requêtes vers le service.

Un autre aspect à prendre en compte est la performance globale de l'application. Avec les applications multi-modales et multi-modèles, nous entendons par performance que le système fonctionne comme vous et vos utilisateurs l'attendez, y compris en n'engendrant pas de sorties nuisibles. Il est important d'évaluer la performance de votre application globale en utilisant les [Performance and Quality and Risk and Safety evaluators](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in). Vous avez également la possibilité de créer et d'évaluer avec des [custom evaluators](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators).

Vous pouvez évaluer votre application d'IA dans votre environnement de développement en utilisant le [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html). À partir d'un jeu de données de test ou d'un objectif, les générations de votre application d'IA générative sont mesurées quantitativement avec des évaluateurs intégrés ou des évaluateurs personnalisés de votre choix. Pour commencer avec l'azure ai evaluation sdk afin d'évaluer votre système, vous pouvez suivre le [guide quickstart](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Une fois que vous avez exécuté un cycle d'évaluation, vous pouvez [visualiser les résultats dans Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results). 

## Marques déposées
Ce projet peut contenir des marques ou des logos pour des projets, des produits ou des services. L'utilisation autorisée des marques ou des logos Microsoft est soumise et doit respecter [Directives sur les marques et l'image de marque de Microsoft](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).
L'utilisation des marques ou des logos Microsoft dans des versions modifiées de ce projet ne doit pas prêter à confusion ni laisser entendre que Microsoft en est le sponsor. Toute utilisation de marques ou de logos de tiers est soumise aux politiques de ces tiers.

## Obtenir de l'aide

Si vous êtes bloqué ou avez des questions sur la création d'applications IA, rejoignez:

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

Si vous avez des retours sur le produit ou rencontrez des erreurs lors du développement, visitez:

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Avis de non-responsabilité :
Ce document a été traduit à l'aide du service de traduction par IA Co-op Translator (https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatiques peuvent comporter des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un traducteur humain. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->