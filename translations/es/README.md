# Phi Cookbook: Ejemplos prácticos con los modelos Phi de Microsoft

[![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub issues](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub watchers](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub stars](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi es una serie de modelos de IA de código abierto desarrollados por Microsoft.

Phi es actualmente el modelo de lenguaje pequeño (SLM) más potente y rentable, con muy buenos resultados en múltiples idiomas, razonamiento, generación de texto/chats, codificación, imágenes, audio y otros escenarios.

Puedes desplegar Phi en la nube o en dispositivos de borde, y puedes crear fácilmente aplicaciones de IA generativa con potencia computacional limitada.

Sigue estos pasos para comenzar a usar estos recursos:
1. **Haz un Fork del repositorio**: Haz clic en [![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **Clona el repositorio**: `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Únete a la comunidad de Microsoft AI en Discord y conoce expertos y otros desarrolladores**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/es/cover.eb18d1b9605d754b.webp)

### 🌐 Soporte multilingüe

#### Soportado vía GitHub Action (Automatizado y siempre actualizado)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Árabe](../ar/README.md) | [Bengalí](../bn/README.md) | [Búlgaro](../bg/README.md) | [Birmano (Myanmar)](../my/README.md) | [Chino (Simplificado)](../zh-CN/README.md) | [Chino (Tradicional, Hong Kong)](../zh-HK/README.md) | [Chino (Tradicional, Macao)](../zh-MO/README.md) | [Chino (Tradicional, Taiwán)](../zh-TW/README.md) | [Croata](../hr/README.md) | [Checo](../cs/README.md) | [Danés](../da/README.md) | [Neerlandés](../nl/README.md) | [Estonio](../et/README.md) | [Finlandés](../fi/README.md) | [Francés](../fr/README.md) | [Alemán](../de/README.md) | [Griego](../el/README.md) | [Hebreo](../he/README.md) | [Hindi](../hi/README.md) | [Húngaro](../hu/README.md) | [Indonesio](../id/README.md) | [Italiano](../it/README.md) | [Japonés](../ja/README.md) | [Kannada](../kn/README.md) | [Coreano](../ko/README.md) | [Lituano](../lt/README.md) | [Malayo](../ms/README.md) | [Malayalam](../ml/README.md) | [Maratí](../mr/README.md) | [Nepalí](../ne/README.md) | [Pidgin Nigeriano](../pcm/README.md) | [Noruego](../no/README.md) | [Persa (Farsi)](../fa/README.md) | [Polaco](../pl/README.md) | [Portugués (Brasil)](../pt-BR/README.md) | [Portugués (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Rumano](../ro/README.md) | [Ruso](../ru/README.md) | [Serbio (Cirílico)](../sr/README.md) | [Eslovaco](../sk/README.md) | [Esloveno](../sl/README.md) | [Español](./README.md) | [Swahili](../sw/README.md) | [Sueco](../sv/README.md) | [Tagalo (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Tailandés](../th/README.md) | [Turco](../tr/README.md) | [Ucraniano](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamita](../vi/README.md)

> **¿Prefieres clonar localmente?**

> Este repositorio incluye traducciones en más de 50 idiomas, lo que aumenta significativamente el tamaño de la descarga. Para clonar sin traducciones, usa sparse checkout:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/PhiCookBook.git
> cd PhiCookBook
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> Esto te dará todo lo que necesitas para completar el curso con una descarga mucho más rápida.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## Tabla de contenidos

- Introducción
  - [Bienvenido a la familia Phi](./md/01.Introduction/01/01.PhiFamily.md)
  - [Configurando tu entorno](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [Entendiendo tecnologías clave](./md/01.Introduction/01/01.Understandingtech.md)
  - [Seguridad en IA para modelos Phi](./md/01.Introduction/01/01.AISafety.md)
  - [Soporte de hardware para Phi](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Modelos Phi y disponibilidad en plataformas](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Usando Guidance-ai y Phi](./md/01.Introduction/01/01.Guidance.md)
  - [Modelos de GitHub Marketplace](https://github.com/marketplace/models)
  - [Catálogo de modelos Azure AI](https://ai.azure.com)

- Inferencia Phi en diferentes entornos
    -  [Hugging face](./md/01.Introduction/02/01.HF.md)
    -  [Modelos en GitHub](./md/01.Introduction/02/02.GitHubModel.md)
    -  [Catálogo Foundry de Azure AI](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    -  [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md)

- Inferencia familia Phi
    - [Inferencia Phi en iOS](./md/01.Introduction/03/iOS_Inference.md)
    - [Inferencia Phi en Android](./md/01.Introduction/03/Android_Inference.md)
    - [Inferencia Phi en Jetson](./md/01.Introduction/03/Jetson_Inference.md)
    - [Inferencia Phi en AI PC](./md/01.Introduction/03/AIPC_Inference.md)
    - [Inferencia Phi con Apple MLX Framework](./md/01.Introduction/03/MLX_Inference.md)
    - [Inferencia Phi en servidor local](./md/01.Introduction/03/Local_Server_Inference.md)
    - [Inferencia Phi en servidor remoto usando AI Toolkit](./md/01.Introduction/03/Remote_Interence.md)
    - [Inferencia Phi con Rust](./md/01.Introduction/03/Rust_Inference.md)
    - [Inferencia Phi--visión en local](./md/01.Introduction/03/Vision_Inference.md)
    - [Inferencia Phi con Kaito AKS, contenedores Azure (soporte oficial)](./md/01.Introduction/03/Kaito_Inference.md)
-  [Cuantificación familia Phi](./md/01.Introduction/04/QuantifyingPhi.md)
    - [Cuantificando Phi-3.5 / 4 usando llama.cpp](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [Cuantificando Phi-3.5 / 4 usando extensiones de IA generativa para onnxruntime](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Cuantificando Phi-3.5 / 4 usando Intel OpenVINO](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Cuantificando Phi-3.5 / 4 usando Apple MLX Framework](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

-  Evaluación Phi
    - [IA responsable](./md/01.Introduction/05/ResponsibleAI.md)
    - [Azure AI Foundry para evaluación](./md/01.Introduction/05/AIFoundry.md)
    - [Usando Promptflow para evaluación](./md/01.Introduction/05/Promptflow.md)
 
- RAG con Azure AI Search
    - [Cómo usar Phi-4-mini y Phi-4-multimodal (RAG) con Azure AI Search](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Ejemplos de desarrollo de aplicaciones Phi
  - Aplicaciones de texto y chat
    - Phi-4 Ejemplos 🆕
      - [📓] [Chat con el modelo Phi-4-mini ONNX](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Chat con modelo ONNX local Phi-4 .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Aplicación consola Chat .NET con Phi-4 ONNX usando Semantic Kernel](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Phi-3 / 3.5 Ejemplos
      - [Chatbot local en navegador usando Phi3, ONNX Runtime Web y WebGPU](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [Chat OpenVino](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [Modelo múltiple - Phi-3-mini interactivo y OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - Construyendo un wrapper y usando Phi-3 con MLFlow](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [Optimización de modelo - Cómo optimizar el modelo Phi-3-min para ONNX Runtime Web con Olive](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [App WinUI3 con Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      - [Ejemplo de aplicación de notas con IA múltiple en WinUI3](https://github.com/microsoft/ai-powered-notes-winui3-sample)
      - [Ajuste fino e integración de modelos Phi-3 personalizados con Prompt flow](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
      - [Ajuste fino e integración de modelos Phi-3 personalizados con Prompt flow en Azure AI Foundry](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
      - [Evaluación del modelo Phi-3 / Phi-3.5 ajustado en Azure AI Foundry con enfoque en los principios de IA responsable de Microsoft](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
      - [📓] [Ejemplo de predicción de lenguaje Phi-3.5-mini-instruct (chino/inglés)](./md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
      - [Chatbot RAG WebGPU Phi-3.5-Instruct](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
      - [Uso de GPU de Windows para crear soluciones Prompt flow con Phi-3.5-Instruct ONNX](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
      - [Uso de Microsoft Phi-3.5 tflite para crear aplicación Android](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
      - [Ejemplo Q&A .NET usando modelo ONNX local Phi-3 con Microsoft.ML.OnnxRuntime](../../md/04.HOL/dotnet/src/LabsPhi301)
      - [App consola chat .NET con Semantic Kernel y Phi-3](../../md/04.HOL/dotnet/src/LabsPhi302)

  - Muestras basadas en código SDK Azure AI Inference
    - Muestras Phi-4 🆕
      - [📓] [Generar código para proyecto usando Phi-4-multimodal](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
    - Muestras Phi-3 / 3.5
      - [Construya su propio Visual Studio Code GitHub Copilot Chat con la familia Microsoft Phi-3](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
      - [Cree su propio agente Copilot Chat en Visual Studio Code con Phi-3.5 usando modelos GitHub](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

  - Muestras de Razonamiento Avanzado
    - Muestras Phi-4 🆕
      - [📓] [Muestras Phi-4-mini-reasoning o Phi-4-reasoning](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
      - [📓] [Ajuste fino Phi-4-mini-reasoning con Microsoft Olive](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Ajuste fino Phi-4-mini-reasoning con Apple MLX](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Phi-4-mini-reasoning con modelos GitHub](./md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
      - [📓] [Phi-4-mini-reasoning con modelos Azure AI Foundry](./md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
  - Demostraciones
      - [Demos Phi-4-mini alojados en Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
      - [Demos Phi-4-multimodal alojados en Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
  - Muestras de Visión
    - Muestras Phi-4 🆕
      - [📓] [Usar Phi-4-multimodal para leer imágenes y generar código](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
    - Muestras Phi-3 / 3.5
      -  [📓][Phi-3-visión - texto de imagen a texto](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [Phi-3-visión-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
      - [📓][Phi-3-visión CLIP Embedding](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [DEMO: Reciclaje Phi-3](https://github.com/jennifermarsman/PhiRecycling/)
      - [Phi-3-visión - asistente de lenguaje visual - con Phi3-Vision y OpenVINO](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
      - [Phi-3 Visión Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
      - [Phi-3 Visión OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
      - [📓][Phi-3.5 Visión multi-cuadro o muestra multi-imagen](./md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
      - [Modelo ONNX local Phi-3 Visión usando Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi303)
      - [Modelo ONNX local Phi-3 Visión basado en menú usando Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi304)

  - Muestras de Matemáticas
    - Muestras Phi-4-Mini-Flash-Reasoning-Instruct 🆕 [Demo de matemáticas con Phi-4-Mini-Flash-Reasoning-Instruct](./md/02.Application/09.Math/MathDemo.ipynb)

  - Muestras de Audio
    - Muestras Phi-4 🆕
      - [📓] [Extracción de transcripciones de audio usando Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
      - [📓] [Muestra de audio Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
      - [📓] [Muestra de traducción de voz Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
      - [Aplicación consola .NET usando audio Phi-4-multimodal para analizar un archivo de audio y generar transcripción](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

  - Muestras MOE
    - Muestras Phi-3 / 3.5
      - [📓] [Modelos Mixture of Experts (MoEs) Phi-3.5 ejemplo en redes sociales](./md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
      - [📓] [Construcción de una tubería de generación aumentada por recuperación (RAG) con NVIDIA NIM Phi-3 MOE, Azure AI Search y LlamaIndex](./md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)
      - 
  - Muestras de Llamada a Funciones
    - Muestras Phi-4 🆕
      -  [📓] [Uso de llamada a funciones con Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
      -  [📓] [Uso de llamada a funciones para crear multi-agentes con Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
      -  [📓] [Uso de llamada a funciones con Ollama](./md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
      -  [📓] [Uso de llamada a funciones con ONNX](./md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)
  - Muestras de Mezcla Multimodal
    - Muestras Phi-4 🆕
      -  [📓] [Uso de Phi-4-multimodal como periodista tecnológico](./md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
      - [Aplicación consola .NET usando Phi-4-multimodal para analizar imágenes](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Afinación fina de muestras Phi
  - [Escenarios de afinación fina](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [Afinación fina vs RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [Afinación fina para convertir Phi-3 en un experto industrial](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [Afinación fina de Phi-3 con AI Toolkit para VS Code](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Afinación fina de Phi-3 con Azure Machine Learning Service](./md/03.FineTuning/Introduce_AzureML.md)
  - [Afinación fina de Phi-3 con Lora](./md/03.FineTuning/FineTuning_Lora.md)
  - [Afinación fina de Phi-3 con QLora](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Afinación fina de Phi-3 con Azure AI Foundry](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Afinación fina de Phi-3 con Azure ML CLI/SDK](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Afinación fina con Microsoft Olive](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Laboratorio práctico de ajuste fino con Microsoft Olive](./md/03.FineTuning/olive-lab/readme.md)
  - [Afinación fina de Phi-3-vision con Weights and Bias](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [Afinación fina de Phi-3 con Apple MLX Framework](./md/03.FineTuning/FineTuning_MLX.md)
  - [Afinación fina de Phi-3-vision (soporte oficial)](./md/03.FineTuning/FineTuning_Vision.md)
  - [Afinación fina de Phi-3 con Kaito AKS, contenedores Azure (soporte oficial)](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Afinación fina de Phi-3 y 3.5 Visión](https://github.com/2U1/Phi3-Vision-Finetune)

- Laboratorio práctico
  - [Explorando modelos de vanguardia: LLMs, SLMs, desarrollo local y más](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [Desbloqueando el potencial del PLN: ajuste fino con Microsoft Olive](https://github.com/azure/Ignite_FineTuning_workshop)

- Artículos de investigación académica y publicaciones
  - [Los libros de texto son todo lo que necesitas II: informe técnico de phi-1.5](https://arxiv.org/abs/2309.05463)
  - [Informe Técnico Phi-3: Un modelo de lenguaje altamente capaz localmente en tu teléfono](https://arxiv.org/abs/2404.14219)
  - [Informe Técnico Phi-4](https://arxiv.org/abs/2412.08905)
  - [Informe Técnico Phi-4-Mini: Modelos de lenguaje multimodal compactos pero potentes mediante mezcla de LoRAs](https://arxiv.org/abs/2503.01743)
  - [Optimización de modelos de lenguaje pequeños para llamadas de función en vehículos](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) Ajuste fino de PHI-3 para preguntas de opción múltiple: metodología, resultados y desafíos](https://arxiv.org/abs/2501.01588)
  - [Informe técnico Phi-4-reasoning](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Informe técnico Phi-4-mini-reasoning](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Uso de modelos Phi

### Phi en Azure AI Foundry

Puedes aprender cómo usar Microsoft Phi y cómo construir soluciones E2E en tus diferentes dispositivos de hardware. Para experimentar Phi por ti mismo, comienza jugando con los modelos y personalizando Phi para tus escenarios usando el [Catálogo de modelos de Azure AI Foundry de Azure AI](https://aka.ms/phi3-azure-ai). Puedes obtener más información en Comenzando con [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md)

**Playground**  
Cada modelo tiene un playground dedicado para probar el modelo [Azure AI Playground](https://aka.ms/try-phi3).

### Phi en modelos de GitHub

Puedes aprender cómo usar Microsoft Phi y cómo construir soluciones E2E en tus diferentes dispositivos de hardware. Para experimentar Phi por ti mismo, comienza jugando con el modelo y personalizando Phi para tus escenarios usando el [Catálogo de Modelos de GitHub](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo). Puedes obtener más información en Comenzando con [Catálogo de Modelos de GitHub](/md/02.QuickStart/GitHubModel_QuickStart.md)

**Playground**  
Cada modelo tiene un [playground dedicado para probar el modelo](/md/02.QuickStart/GitHubModel_QuickStart.md).

### Phi en Hugging Face

También puedes encontrar el modelo en [Hugging Face](https://huggingface.co/microsoft)

**Playground**  
 [Playground de Hugging Chat](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

 ## 🎒 Otros cursos

¡Nuestro equipo produce otros cursos! Echa un vistazo:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j para principiantes](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js para principiantes](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![LangChain para principiantes](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### Azure / Edge / MCP / Agentes
[![AZD para principiantes](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI para principiantes](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP para principiantes](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Agentes de IA para principiantes](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Serie de IA Generativa
[![IA Generativa para principiantes](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![IA Generativa (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![IA Generativa (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![IA Generativa (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Aprendizaje Básico
[![ML para principiantes](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Ciencia de Datos para principiantes](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![IA para principiantes](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Ciberseguridad para principiantes](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Desarrollo web para principiantes](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT para principiantes](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![Desarrollo XR para principiantes](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Serie Copilot
[![Copilot para programación asistida por IA](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot para C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Aventura Copilot](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## IA Responsable

Microsoft está comprometido a ayudar a nuestros clientes a usar nuestros productos de IA de manera responsable, compartiendo nuestros aprendizajes y construyendo asociaciones basadas en la confianza mediante herramientas como Notas de Transparencia y Evaluaciones de Impacto. Muchos de estos recursos pueden encontrarse en [https://aka.ms/RAI](https://aka.ms/RAI).  
El enfoque de Microsoft hacia la IA responsable se basa en nuestros principios de IA de equidad, confiabilidad y seguridad, privacidad y seguridad, inclusión, transparencia y responsabilidad.

Los modelos a gran escala de lenguaje natural, imagen y voz —como los usados en este ejemplo— pueden comportarse potencialmente de maneras injustas, poco fiables u ofensivas, causando a su vez daños. Por favor, consulta la [nota de transparencia del servicio Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) para estar informado sobre riesgos y limitaciones.

El enfoque recomendado para mitigar estos riesgos es incluir un sistema de seguridad en tu arquitectura que pueda detectar y prevenir comportamientos dañinos. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) proporciona una capa independiente de protección, capaz de detectar contenido dañino generado por usuarios y generado por IA en aplicaciones y servicios. Azure AI Content Safety incluye APIs de texto e imagen que te permiten detectar material que es dañino. Dentro de Azure AI Foundry, el servicio Content Safety te permite ver, explorar y probar ejemplos de código para detectar contenido dañino en diferentes modalidades. La siguiente [documentación de inicio rápido](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) te guía sobre cómo hacer solicitudes al servicio.
Otro aspecto a tener en cuenta es el rendimiento general de la aplicación. Con aplicaciones multimodales y multimodelos, consideramos que el rendimiento significa que el sistema funciona como tú y tus usuarios esperan, incluyendo no generar resultados dañinos. Es importante evaluar el rendimiento de tu aplicación en su conjunto utilizando los [evaluadores de Rendimiento, Calidad, Riesgo y Seguridad](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in). También tienes la capacidad de crear y evaluar con [evaluadores personalizados](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators).

Puedes evaluar tu aplicación de IA en tu entorno de desarrollo usando el [SDK de Evaluación de Azure AI](https://microsoft.github.io/promptflow/index.html). Dados un conjunto de datos de prueba o un objetivo, las generaciones de tu aplicación de IA generativa se miden cuantitativamente con evaluadores incorporados o evaluadores personalizados de tu elección. Para comenzar con el sdk de evaluación azure ai y evaluar tu sistema, puedes seguir la [guía de inicio rápido](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Una vez que ejecutes una evaluación, puedes [visualizar los resultados en Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Marcas Registradas

Este proyecto puede contener marcas registradas o logos de proyectos, productos o servicios. El uso autorizado de las marcas registradas o logotipos de Microsoft está sujeto a y debe seguir las [Directrices de Marcas y Marca Comercial de Microsoft](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).  
El uso de marcas registradas o logotipos de Microsoft en versiones modificadas de este proyecto no debe causar confusión ni implicar patrocinio de Microsoft. Cualquier uso de marcas registradas o logotipos de terceros está sujeto a las políticas de dichos terceros.

## Obtener Ayuda

Si te quedas atascado o tienes alguna pregunta sobre cómo crear aplicaciones de IA, únete a:

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

Si tienes comentarios sobre el producto o errores mientras construyes, visita:

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos responsabilizamos por malentendidos o interpretaciones erróneas derivados del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->