<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5c07bb4c3c89a36c9be332a065a9a33c",
  "translation_date": "2025-07-16T15:09:07+00:00",
  "source_file": "README.md",
  "language_code": "br"
}
-->
# Phi Cookbook: Exemplos Práticos com os Modelos Phi da Microsoft

[![Abra e use os exemplos no GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)  
[![Abrir em Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![Contribuidores no GitHub](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)  
[![Issues no GitHub](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)  
[![Pull requests no GitHub](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)  
[![PRs Bem-vindos](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![Observadores no GitHub](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)  
[![Forks no GitHub](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)  
[![Estrelas no GitHub](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Comunidade Azure AI no Discord](https://dcbadge.vercel.app/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

Phi é uma série de modelos de IA open source desenvolvidos pela Microsoft.

Atualmente, Phi é o modelo de linguagem pequeno (SLM) mais poderoso e custo-efetivo, com benchmarks muito bons em múltiplos idiomas, raciocínio, geração de texto/chat, codificação, imagens, áudio e outros cenários.

Você pode implantar Phi na nuvem ou em dispositivos de borda, e construir facilmente aplicações de IA generativa mesmo com poder computacional limitado.

Siga estes passos para começar a usar esses recursos:  
1. **Faça um Fork do Repositório**: Clique em [![Forks no GitHub](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)  
2. **Clone o Repositório**: `git clone https://github.com/microsoft/PhiCookBook.git`  
3. [**Junte-se à Comunidade Microsoft AI no Discord e conheça especialistas e outros desenvolvedores**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![capa](../../translated_images/cover.eb18d1b9605d754b30973f4e17c6e11ea4f8473d9686ee378d6e7b44e3c70ac7.br.png)

### 🌐 Suporte Multilíngue

#### Suportado via GitHub Action (Automatizado e Sempre Atualizado)

[Francês](../fr/README.md) | [Espanhol](../es/README.md) | [Alemão](../de/README.md) | [Russo](../ru/README.md) | [Árabe](../ar/README.md) | [Persa (Farsi)](../fa/README.md) | [Urdu](../ur/README.md) | [Chinês (Simplificado)](../zh/README.md) | [Chinês (Tradicional, Macau)](../mo/README.md) | [Chinês (Tradicional, Hong Kong)](../hk/README.md) | [Chinês (Tradicional, Taiwan)](../tw/README.md) | [Japonês](../ja/README.md) | [Coreano](../ko/README.md) | [Hindi](../hi/README.md)  
[Bengali](../bn/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Português (Portugal)](../pt/README.md) | [Português (Brasil)](./README.md) | [Italiano](../it/README.md) | [Polonês](../pl/README.md) | [Turco](../tr/README.md) | [Grego](../el/README.md) | [Tailandês](../th/README.md) | [Sueco](../sv/README.md) | [Dinamarquês](../da/README.md) | [Norueguês](../no/README.md) | [Finlandês](../fi/README.md) | [Holandês](../nl/README.md) | [Hebraico](../he/README.md) | [Vietnamita](../vi/README.md) | [Indonésio](../id/README.md) | [Malaio](../ms/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Suaíli](../sw/README.md) | [Húngaro](../hu/README.md) | [Tcheco](../cs/README.md) | [Eslovaco](../sk/README.md) | [Romeno](../ro/README.md) | [Búlgaro](../bg/README.md) | [Sérvio (Cirílico)](../sr/README.md) | [Croata](../hr/README.md) | [Esloveno](../sl/README.md)

## Sumário

- Introdução  
  - [Bem-vindo à Família Phi](./md/01.Introduction/01/01.PhiFamily.md)  
  - [Configurando seu ambiente](./md/01.Introduction/01/01.EnvironmentSetup.md)  
  - [Entendendo Tecnologias-Chave](./md/01.Introduction/01/01.Understandingtech.md)  
  - [Segurança em IA para Modelos Phi](./md/01.Introduction/01/01.AISafety.md)  
  - [Suporte de Hardware Phi](./md/01.Introduction/01/01.Hardwaresupport.md)  
  - [Modelos Phi & Disponibilidade em plataformas](./md/01.Introduction/01/01.Edgeandcloud.md)  
  - [Usando Guidance-ai e Phi](./md/01.Introduction/01/01.Guidance.md)  
  - [Modelos no GitHub Marketplace](https://github.com/marketplace/models)  
  - [Catálogo de Modelos Azure AI](https://ai.azure.com)

- Inferência Phi em diferentes ambientes  
    -  [Hugging Face](./md/01.Introduction/02/01.HF.md)  
    -  [Modelos no GitHub](./md/01.Introduction/02/02.GitHubModel.md)  
    -  [Catálogo Azure AI Foundry](./md/01.Introduction/02/03.AzureAIFoundry.md)  
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)  
    -  [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)  
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)  
    -  [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md)

- Inferência Família Phi  
    - [Inferência Phi no iOS](./md/01.Introduction/03/iOS_Inference.md)  
    - [Inferência Phi no Android](./md/01.Introduction/03/Android_Inference.md)  
    - [Inferência Phi no Jetson](./md/01.Introduction/03/Jetson_Inference.md)  
    - [Inferência Phi no AI PC](./md/01.Introduction/03/AIPC_Inference.md)  
    - [Inferência Phi com Apple MLX Framework](./md/01.Introduction/03/MLX_Inference.md)  
    - [Inferência Phi em Servidor Local](./md/01.Introduction/03/Local_Server_Inference.md)  
    - [Inferência Phi em Servidor Remoto usando AI Toolkit](./md/01.Introduction/03/Remote_Interence.md)  
    - [Inferência Phi com Rust](./md/01.Introduction/03/Rust_Inference.md)  
    - [Inferência Phi–Visão Local](./md/01.Introduction/03/Vision_Inference.md)  
    - [Inferência Phi com Kaito AKS, Azure Containers (suporte oficial)](./md/01.Introduction/03/Kaito_Inference.md)  
-  [Quantização da Família Phi](./md/01.Introduction/04/QuantifyingPhi.md)  
    - [Quantizando Phi-3.5 / 4 usando llama.cpp](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)  
    - [Quantizando Phi-3.5 / 4 usando extensões Generative AI para onnxruntime](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)  
    - [Quantizando Phi-3.5 / 4 usando Intel OpenVINO](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)  
    - [Quantizando Phi-3.5 / 4 usando Apple MLX Framework](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

- Avaliação Phi  
    - [IA Responsável](./md/01.Introduction/05/ResponsibleAI.md)  
    - [Azure AI Foundry para Avaliação](./md/01.Introduction/05/AIFoundry.md)  
    - [Usando Promptflow para Avaliação](./md/01.Introduction/05/Promptflow.md)

- RAG com Azure AI Search  
    - [Como usar Phi-4-mini e Phi-4-multimodal (RAG) com Azure AI Search](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Exemplos de desenvolvimento de aplicações Phi  
  - Aplicações de Texto & Chat  
    - Exemplos Phi-4 🆕  
      - [📓] [Chat com o Modelo Phi-4-mini ONNX](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)  
      - [Chat com Modelo Phi-4 local ONNX .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)  
      - [App Console Chat .NET com Phi-4 ONNX usando Semantic Kernel](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)  
    - Exemplos Phi-3 / 3.5  
      - [Chatbot Local no navegador usando Phi3, ONNX Runtime Web e WebGPU](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)  
      - [Chat OpenVino](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)  
      - [Multi Modelo - Phi-3-mini interativo e OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)  
      - [MLFlow - Criando um wrapper e usando Phi-3 com MLFlow](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)  
      - [Otimização de Modelo - Como otimizar o modelo Phi-3-min para ONNX Runtime Web com Olive](https://github.com/microsoft/Olive/tree/main/examples/phi3)  
      - [App WinUI3 com Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)  
      - [Exemplo de App de Notas com IA Multi Modelo WinUI3](https://github.com/microsoft/ai-powered-notes-winui3-sample)
- [Ajustar e integrar modelos Phi-3 personalizados com Prompt flow](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
- [Ajustar e integrar modelos Phi-3 personalizados com Prompt flow no Azure AI Foundry](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
- [Avaliar o modelo Phi-3 / Phi-3.5 ajustado no Azure AI Foundry com foco nos Princípios de IA Responsável da Microsoft](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
- [📓] [Exemplo de previsão de linguagem Phi-3.5-mini-instruct (Chinês/Inglês)](../../md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
- [Chatbot RAG Phi-3.5-Instruct WebGPU](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
- [Usando GPU do Windows para criar solução Prompt flow com Phi-3.5-Instruct ONNX](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
- [Usando Microsoft Phi-3.5 tflite para criar app Android](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
- [Exemplo Q&A .NET usando modelo local ONNX Phi-3 com Microsoft.ML.OnnxRuntime](../../md/04.HOL/dotnet/src/LabsPhi301)
- [App de chat console .NET com Semantic Kernel e Phi-3](../../md/04.HOL/dotnet/src/LabsPhi302)

- Exemplos baseados em código do Azure AI Inference SDK  
  - Exemplos Phi-4 🆕  
    - [📓] [Gerar código de projeto usando Phi-4-multimodal](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)  
  - Exemplos Phi-3 / 3.5  
    - [Construa seu próprio GitHub Copilot Chat para Visual Studio Code com Microsoft Phi-3 Family](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)  
    - [Crie seu próprio agente de chat Copilot para Visual Studio Code com Phi-3.5 usando modelos do GitHub](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)  

- Exemplos de Raciocínio Avançado  
  - Exemplos Phi-4 🆕  
    - [📓] [Exemplos Phi-4-mini-reasoning ou Phi-4-reasoning](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)  
    - [📓] [Ajuste fino do Phi-4-mini-reasoning com Microsoft Olive](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)  
    - [📓] [Ajuste fino do Phi-4-mini-reasoning com Apple MLX](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)  
    - [📓] [Phi-4-mini-reasoning com modelos do GitHub](../../md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)  
    - [📓] [Phi-4-mini-reasoning com modelos do Azure AI Foundry](../../md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)  
- Demos  
    - [Demos Phi-4-mini hospedados no Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)  
    - [Demos Phi-4-multimodal hospedados no Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)  
- Exemplos de Visão  
  - Exemplos Phi-4 🆕  
    - [📓] [Use Phi-4-multimodal para ler imagens e gerar código](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md)  
  - Exemplos Phi-3 / 3.5  
    - [📓][Phi-3-vision-Texto de imagem para texto](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)  
    - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)  
    - [📓][Phi-3-vision CLIP Embedding](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)  
    - [DEMO: Phi-3 Reciclagem](https://github.com/jennifermarsman/PhiRecycling/)  
    - [Phi-3-vision - Assistente de linguagem visual - com Phi3-Vision e OpenVINO](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)  
    - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)  
    - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)  
    - [📓][Phi-3.5 Vision amostra multi-frame ou multi-imagem](../../md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)  
    - [Modelo local ONNX Phi-3 Vision usando Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi303)  
    - [Modelo local ONNX Phi-3 Vision baseado em menu usando Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi304)  

- Exemplos de Matemática  
  - Exemplos Phi-4-Mini-Flash-Reasoning-Instruct 🆕 [Demonstração matemática com Phi-4-Mini-Flash-Reasoning-Instruct](../../md/02.Application/09.Math/MathDemo.ipynb)  

- Exemplos de Áudio  
  - Exemplos Phi-4 🆕  
    - [📓] [Extração de transcrições de áudio usando Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Transciption/README.md)  
    - [📓] [Exemplo de áudio Phi-4-multimodal](../../md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)  
    - [📓] [Exemplo de tradução de fala Phi-4-multimodal](../../md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)  
    - [Aplicação console .NET usando Phi-4-multimodal Audio para analisar arquivo de áudio e gerar transcrição](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)  

- Exemplos MOE  
  - Exemplos Phi-3 / 3.5  
    - [📓] [Modelos Phi-3.5 Mixture of Experts (MoEs) - Exemplo em redes sociais](../../md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)  
    - [📓] [Construindo pipeline Retrieval-Augmented Generation (RAG) com NVIDIA NIM Phi-3 MOE, Azure AI Search e LlamaIndex](../../md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)  

- Exemplos de Chamada de Função  
  - Exemplos Phi-4 🆕  
    - [📓] [Usando Chamada de Função com Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)  
    - [📓] [Usando Chamada de Função para criar multi-agentes com Phi-4-mini](../../md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)  
    - [📓] [Usando Chamada de Função com Ollama](../../md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)  
    - [📓] [Usando Chamada de Função com ONNX](../../md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)  

- Exemplos de Mistura Multimodal  
  - Exemplos Phi-4 🆕  
    - [📓] [Usando Phi-4-multimodal como jornalista de tecnologia](../../md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)  
    - [Aplicação console .NET usando Phi-4-multimodal para analisar imagens](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)  

- Ajuste fino de amostras Phi  
  - [Cenários de ajuste fino](./md/03.FineTuning/FineTuning_Scenarios.md)  
  - [Ajuste fino vs RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)  
  - [Ajuste fino para transformar Phi-3 em especialista da indústria](./md/03.FineTuning/LetPhi3gotoIndustriy.md)  
  - [Ajuste fino Phi-3 com AI Toolkit para VS Code](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)  
  - [Ajuste fino Phi-3 com Azure Machine Learning Service](./md/03.FineTuning/Introduce_AzureML.md)  
  - [Ajuste fino Phi-3 com Lora](./md/03.FineTuning/FineTuning_Lora.md)  
  - [Ajuste fino Phi-3 com QLora](./md/03.FineTuning/FineTuning_Qlora.md)  
  - [Ajuste fino Phi-3 com Azure AI Foundry](./md/03.FineTuning/FineTuning_AIFoundry.md)  
  - [Ajuste fino Phi-3 com Azure ML CLI/SDK](./md/03.FineTuning/FineTuning_MLSDK.md)  
  - [Ajuste fino com Microsoft Olive](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)  
  - [Laboratório prático de ajuste fino com Microsoft Olive](./md/03.FineTuning/olive-lab/readme.md)  
  - [Ajuste fino Phi-3-vision com Weights and Bias](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)  
  - [Ajuste fino Phi-3 com Apple MLX Framework](./md/03.FineTuning/FineTuning_MLX.md)  
  - [Ajuste fino Phi-3-vision (suporte oficial)](./md/03.FineTuning/FineTuning_Vision.md)  
  - [Ajuste fino Phi-3 com Kaito AKS, Azure Containers (suporte oficial)](./md/03.FineTuning/FineTuning_Kaito.md)  
  - [Ajuste fino Phi-3 e 3.5 Vision](https://github.com/2U1/Phi3-Vision-Finetune)  

- Laboratórios práticos  
  - [Explorando modelos de ponta: LLMs, SLMs, desenvolvimento local e mais](https://github.com/microsoft/aitour-exploring-cutting-edge-models)  
  - [Desbloqueando o potencial de NLP: Ajuste fino com Microsoft Olive](https://github.com/azure/Ignite_FineTuning_workshop)  

- Artigos acadêmicos e publicações  
  - [Textbooks Are All You Need II: relatório técnico phi-1.5](https://arxiv.org/abs/2309.05463)  
  - [Relatório técnico Phi-3: um modelo de linguagem altamente capaz localmente no seu celular](https://arxiv.org/abs/2404.14219)  
  - [Relatório técnico Phi-4](https://arxiv.org/abs/2412.08905)  
  - [Relatório técnico Phi-4-Mini: modelos multimodais compactos e poderosos via Mixture-of-LoRAs](https://arxiv.org/abs/2503.01743)  
  - [Otimização de pequenos modelos de linguagem para chamada de função em veículos](https://arxiv.org/abs/2501.02342)  
  - [(WhyPHI) Ajuste fino PHI-3 para perguntas de múltipla escolha: metodologia, resultados e desafios](https://arxiv.org/abs/2501.01588)
- [Phi-4-reasoning Technical Report](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)  
- [Phi-4-mini-reasoning Technical Report](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Usando os Modelos Phi

### Phi no Azure AI Foundry

Você pode aprender como usar o Microsoft Phi e como construir soluções E2E em seus diferentes dispositivos de hardware. Para experimentar o Phi por conta própria, comece testando os modelos e personalizando o Phi para seus cenários usando o [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai). Você pode saber mais em Começando com [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md)

**Playground**  
Cada modelo possui um playground dedicado para testar o modelo [Azure AI Playground](https://aka.ms/try-phi3).

### Phi nos Modelos do GitHub

Você pode aprender como usar o Microsoft Phi e como construir soluções E2E em seus diferentes dispositivos de hardware. Para experimentar o Phi por conta própria, comece testando o modelo e personalizando o Phi para seus cenários usando o [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo). Você pode saber mais em Começando com [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md)

**Playground**  
Cada modelo possui um [playground dedicado para testar o modelo](/md/02.QuickStart/GitHubModel_QuickStart.md).

### Phi no Hugging Face

Você também pode encontrar o modelo no [Hugging Face](https://huggingface.co/microsoft)

**Playground**  
[Hugging Chat playground](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## IA Responsável

A Microsoft está comprometida em ajudar nossos clientes a usar nossos produtos de IA de forma responsável, compartilhando nossos aprendizados e construindo parcerias baseadas na confiança por meio de ferramentas como Transparency Notes e Impact Assessments. Muitos desses recursos podem ser encontrados em [https://aka.ms/RAI](https://aka.ms/RAI).  
A abordagem da Microsoft para IA responsável está fundamentada em nossos princípios de IA: justiça, confiabilidade e segurança, privacidade e segurança, inclusão, transparência e responsabilidade.

Modelos de linguagem natural, imagem e fala em larga escala – como os usados neste exemplo – podem se comportar de maneiras que sejam injustas, não confiáveis ou ofensivas, causando danos. Consulte a [Transparency note do serviço Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) para se informar sobre riscos e limitações.

A abordagem recomendada para mitigar esses riscos é incluir um sistema de segurança em sua arquitetura que possa detectar e prevenir comportamentos prejudiciais. O [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) oferece uma camada independente de proteção, capaz de detectar conteúdo prejudicial gerado por usuários e por IA em aplicações e serviços. O Azure AI Content Safety inclui APIs de texto e imagem que permitem detectar material prejudicial. Dentro do Azure AI Foundry, o serviço Content Safety permite visualizar, explorar e testar códigos de exemplo para detectar conteúdo prejudicial em diferentes modalidades. A seguinte [documentação de início rápido](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) orienta você a fazer requisições ao serviço.

Outro aspecto a considerar é o desempenho geral da aplicação. Em aplicações multimodais e com múltiplos modelos, consideramos desempenho como o sistema funcionando conforme o esperado por você e seus usuários, incluindo não gerar saídas prejudiciais. É importante avaliar o desempenho da sua aplicação geral usando os [avaliadores de Performance e Qualidade e de Risco e Segurança](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in). Você também pode criar e avaliar com [avaliadores personalizados](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators).

Você pode avaliar sua aplicação de IA no seu ambiente de desenvolvimento usando o [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html). Dado um conjunto de dados de teste ou um alvo, as gerações da sua aplicação de IA generativa são medidas quantitativamente com avaliadores integrados ou avaliadores personalizados de sua escolha. Para começar a usar o azure ai evaluation sdk para avaliar seu sistema, você pode seguir o [guia de início rápido](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Após executar uma avaliação, você pode [visualizar os resultados no Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Marcas Registradas

Este projeto pode conter marcas registradas ou logotipos de projetos, produtos ou serviços. O uso autorizado das marcas registradas ou logotipos da Microsoft está sujeito e deve seguir as [Diretrizes de Marcas e Identidade Visual da Microsoft](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).  
O uso das marcas registradas ou logotipos da Microsoft em versões modificadas deste projeto não deve causar confusão nem implicar patrocínio da Microsoft. Qualquer uso de marcas registradas ou logotipos de terceiros está sujeito às políticas desses terceiros.

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.