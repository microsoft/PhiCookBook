# Recetario Phi: Ejemplos prácticos con los modelos Phi de Microsoft

[![Abrir y usar los ejemplos en GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Abrir en Contenedores Dev](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![Colaboradores en GitHub](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![Incidencias en GitHub](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![Pull requests en GitHub](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![Pull requests Bienvenidas](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![Seguidores en GitHub](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![Bifurcaciones en GitHub](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![Estrellas en GitHub](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Discord de Microsoft Foundry](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi es una serie de modelos de IA de código abierto desarrollados por Microsoft. 

Phi es actualmente el modelo de lenguaje pequeño (SLM) más potente y rentable, con muy buenos resultados en múltiples idiomas, razonamiento, generación de texto/chat, codificación, imágenes, audio y otros escenarios. 

Puedes implementar Phi en la nube o en dispositivos de borde, y puedes construir fácilmente aplicaciones de IA generativa con potencia informática limitada.

Sigue estos pasos para comenzar a usar estos recursos:
1. **Bifurca el Repositorio**: Haz clic en [![Bifurcaciones en GitHub](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **Clona el Repositorio**: `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Únete a la Comunidad de Microsoft AI en Discord y conoce a expertos y otros desarrolladores**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![portada](../../translated_images/es/cover.eb18d1b9605d754b.webp)

### 🌐 Soporte Multilingüe

#### Soportado a través de GitHub Action (Automatizado y Siempre Actualizado)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Árabe](../ar/README.md) | [Bengalí](../bn/README.md) | [Búlgaro](../bg/README.md) | [Birmano (Myanmar)](../my/README.md) | [Chino (Simplificado)](../zh-CN/README.md) | [Chino (Tradicional, Hong Kong)](../zh-HK/README.md) | [Chino (Tradicional, Macao)](../zh-MO/README.md) | [Chino (Tradicional, Taiwán)](../zh-TW/README.md) | [Croata](../hr/README.md) | [Checo](../cs/README.md) | [Danés](../da/README.md) | [Neerlandés](../nl/README.md) | [Estonio](../et/README.md) | [Finés](../fi/README.md) | [Francés](../fr/README.md) | [Alemán](../de/README.md) | [Griego](../el/README.md) | [Hebreo](../he/README.md) | [Hindi](../hi/README.md) | [Húngaro](../hu/README.md) | [Indonesio](../id/README.md) | [Italiano](../it/README.md) | [Japonés](../ja/README.md) | [Kannada](../kn/README.md) | [Jemer](../km/README.md) | [Coreano](../ko/README.md) | [Lituano](../lt/README.md) | [Malayo](../ms/README.md) | [Malabar](../ml/README.md) | [Maratí](../mr/README.md) | [Nepalí](../ne/README.md) | [Pidgin Nigeriano](../pcm/README.md) | [Noruego](../no/README.md) | [Persa (Farsi)](../fa/README.md) | [Polaco](../pl/README.md) | [Portugués (Brasil)](../pt-BR/README.md) | [Portugués (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Rumano](../ro/README.md) | [Ruso](../ru/README.md) | [Serbio (Cirílico)](../sr/README.md) | [Eslovaco](../sk/README.md) | [Esloveno](../sl/README.md) | [Español](./README.md) | [Swahili](../sw/README.md) | [Sueco](../sv/README.md) | [Tagalo (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Tailandés](../th/README.md) | [Turco](../tr/README.md) | [Ucraniano](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamita](../vi/README.md)

> **¿Prefieres clonar localmente?**
>
> Este repositorio incluye traducciones a más de 50 idiomas, lo cual incrementa significativamente el tamaño de la descarga. Para clonar sin las traducciones, usa checkout disperso:
>
> **Bash / macOS / Linux:**
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/PhiCookBook.git
> cd PhiCookBook
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
>
> **CMD (Windows):**
> ```cmd
> git clone --filter=blob:none --sparse https://github.com/microsoft/PhiCookBook.git
> cd PhiCookBook
> git sparse-checkout set --no-cone "/*" "!translations" "!translated_images"
> ```
>
> Esto te proporciona todo lo necesario para completar el curso con una descarga mucho más rápida.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## Tabla de Contenidos

- Introducción
  - [Bienvenido a la Familia Phi](./md/01.Introduction/01/01.PhiFamily.md)
  - [Configurando tu entorno](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [Entendiendo Tecnologías Clave](./md/01.Introduction/01/01.Understandingtech.md)
  - [Seguridad en IA para los modelos Phi](./md/01.Introduction/01/01.AISafety.md)
  - [Soporte de hardware para Phi](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Modelos Phi y disponibilidad en distintas plataformas](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Uso de Guidance-ai y Phi](./md/01.Introduction/01/01.Guidance.md)
  - [Modelos del Marketplace de GitHub](https://github.com/marketplace/models)
  - [Catálogo de modelos de IA en Azure](https://ai.azure.com)

- Inferencia Phi en diferentes entornos
    -  [Hugging face](./md/01.Introduction/02/01.HF.md)
    -  [Modelos en GitHub](./md/01.Introduction/02/02.GitHubModel.md)
    -  [Catálogo de modelos de Microsoft Foundry](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [Kit de Herramientas IA para VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    -  [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md)

- Inferencia en la Familia Phi
    - [Inferencia Phi en iOS](./md/01.Introduction/03/iOS_Inference.md)
    - [Inferencia Phi en Android](./md/01.Introduction/03/Android_Inference.md)
    - [Inferencia Phi en Jetson](./md/01.Introduction/03/Jetson_Inference.md)
    - [Inferencia Phi en PC de IA](./md/01.Introduction/03/AIPC_Inference.md)
    - [Inferencia Phi con el Framework MLX de Apple](./md/01.Introduction/03/MLX_Inference.md)
    - [Inferencia Phi en servidor local](./md/01.Introduction/03/Local_Server_Inference.md)
    - [Inferencia Phi en servidor remoto usando AI Toolkit](./md/01.Introduction/03/Remote_Interence.md)
    - [Inferencia Phi con Rust](./md/01.Introduction/03/Rust_Inference.md)
    - [Inferencia Phi--Visión local](./md/01.Introduction/03/Vision_Inference.md)
    - [Inferencia Phi con Kaito AKS, contenedores de Azure (soporte oficial)](./md/01.Introduction/03/Kaito_Inference.md)
-  [Cuantificación de la Familia Phi](./md/01.Introduction/04/QuantifyingPhi.md)
    - [Cuantificación de Phi-3.5 / 4 usando llama.cpp](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [Cuantificación de Phi-3.5 / 4 usando extensiones IA generativa para onnxruntime](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Cuantificación de Phi-3.5 / 4 usando Intel OpenVINO](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Cuantificación de Phi-3.5 / 4 usando el Framework MLX de Apple](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

-  Evaluación de Phi
    - [IA Responsable](./md/01.Introduction/05/ResponsibleAI.md)
    - [Microsoft Foundry para Evaluación](./md/01.Introduction/05/AIFoundry.md)
    - [Uso de Promptflow para Evaluación](./md/01.Introduction/05/Promptflow.md)
 
- RAG con Azure AI Search
    - [Cómo usar Phi-4-mini y Phi-4-multimodal (RAG) con Azure AI Search](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)
    - [RAG híbrido local sin nube con SQLite FTS5 y phi-4-mini](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-mini_Local_Hybrid_RAG_SQLite_FTS5.ipynb)

- Ejemplos de desarrollo de aplicaciones Phi
  - Aplicaciones de Texto y Chat
    - Ejemplos Phi-4 
      - [📓] [Chat con el modelo Phi-4-mini ONNX](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Chat con modelo ONNX local Phi-4 en .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [App Console Chat .NET con Phi-4 ONNX usando Sementic Kernel](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)

    - Phi-3 / 3.5 Ejemplos
      - [Chatbot local en el navegador usando Phi3, ONNX Runtime Web y WebGPU](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [Chat de OpenVino](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [Multi Modelo - Phi-3-mini interactivo y OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - Creando un wrapper y usando Phi-3 con MLFlow](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [Optimización de modelo - Cómo optimizar el modelo Phi-3-min para ONNX Runtime Web con Olive](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [App WinUI3 con Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      -[Ejemplo de aplicación WinUI3 de notas impulsada por IA Multimodelo](https://github.com/microsoft/ai-powered-notes-winui3-sample)
      - [Ajuste fino e integración de modelos personalizados Phi-3 con Prompt flow](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
      - [Ajuste fino e integración de modelos personalizados Phi-3 con Prompt flow en Microsoft Foundry](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
      - [Evaluar el modelo ajustado Phi-3 / Phi-3.5 en Microsoft Foundry enfocado en los principios de IA responsable de Microsoft](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
      - [📓] [Ejemplo de predicción de lenguaje Phi-3.5-mini-instruct (Chino/Inglés)](./md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
      - [Chatbot RAG WebGPU Phi-3.5-Instruct](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
      - [Uso de GPU de Windows para crear una solución Prompt flow con Phi-3.5-Instruct ONNX](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
      - [Uso de Microsoft Phi-3.5 tflite para crear una app Android](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
      - [Ejemplo Q&A .NET usando modelo local ONNX Phi-3 con Microsoft.ML.OnnxRuntime](../../md/04.HOL/dotnet/src/LabsPhi301)
      - [App chat consola .NET con Semantic Kernel y Phi-3](../../md/04.HOL/dotnet/src/LabsPhi302)

  - Ejemplos basados en código del SDK Azure AI Inference 
    - Ejemplos Phi-4 
      - [📓] [Generar código del proyecto usando Phi-4-multimodal](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
    - Ejemplos Phi-3 / 3.5
      - [Construye tu propio Visual Studio Code GitHub Copilot Chat con Microsoft Phi-3 Family](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
      - [Crea tu propio agente Visual Studio Code Chat Copilot con Phi-3.5 mediante modelos GitHub](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

  - Ejemplos de razonamiento avanzado
    - Ejemplos Phi-4 
      - [📓] [Ejemplos Phi-4-mini-reasoning o Phi-4-reasoning](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
      - [📓] [Ajuste fino Phi-4-mini-reasoning con Microsoft Olive](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Ajuste fino Phi-4-mini-reasoning con Apple MLX](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Phi-4-mini-reasoning con modelos GitHub](./md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
      - [📓] [Phi-4-mini-reasoning con modelos Microsoft Foundry](./md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
  - Demos
      - [Demos Phi-4-mini alojados en Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
      - [Demos Phi-4-multimodal alojados en Hugginge Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
  - Ejemplos de Visión
    - Ejemplos Phi-4 
      - [📓] [Usar Phi-4-multimodal para leer imágenes y generar código](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
    - Ejemplos Phi-3 / 3.5
      -  [📓][Phi-3-vision-Texto de imagen a texto](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
      - [📓][Phi-3-vision CLIP Embedding](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [DEMO: Reciclaje Phi-3](https://github.com/jennifermarsman/PhiRecycling/)
      - [Phi-3-vision - Asistente de lenguaje visual - con Phi3-Vision y OpenVINO](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
      - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
      - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
      - [📓][Ejemplo Phi-3.5 Vision multi-frame o multi-imagen](./md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
      - [Modelo local ONNX Phi-3 Vision usando Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi303)
      - [Modelo local ONNX Phi-3 Vision basado en menú usando Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi304)

  - Ejemplos de Razonamiento-Visión
    - Phi-4-Razonamiento-Visión-15B 
      - [📓] [Uso de Phi-4-Razonamiento-Visión-15B para detectar cruce temerario](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_Jaywalking.ipynb)
      - [📓] [Uso de Phi-4-Razonamiento-Visión-15B para matemáticas](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_Math.ipynb)
      - [📓] [Uso de Phi-4-Razonamiento-Visión-15B para detectar UI](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_ui.ipynb)

  - Ejemplos de Matemáticas
    -  Ejemplos Phi-4-Mini-Flash-Razonamiento-Instruct  [Demo de Matemáticas con Phi-4-Mini-Flash-Razonamiento-Instruct](./md/02.Application/09.Math/MathDemo.ipynb)

  - Ejemplos de Audio
    - Ejemplos Phi-4 
      - [📓] [Extracción de transcripciones de audio usando Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
      - [📓] [Ejemplo de Audio Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
      - [📓] [Ejemplo de traducción de voz Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
      - [Aplicación consola .NET usando Phi-4-multimodal Audio para analizar un archivo y generar transcripción](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

  - Ejemplos MOE
    - Ejemplos Phi-3 / 3.5
      - [📓] [Modelos Phi-3.5 Mixture of Experts (MoEs) Ejemplo en redes sociales](./md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
      - [📓] [Construcción de un pipeline Retrieval-Augmented Generation (RAG) con NVIDIA NIM Phi-3 MOE, Azure AI Search y LlamaIndex](./md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)
      - 
  - Ejemplos de llamada a función
    - Ejemplos Phi-4 🆕
      -  [📓] [Uso de llamada a función con Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
      -  [📓] [Uso de llamada a función para crear multi-agentes con Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
      -  [📓] [Uso de llamada a función con Ollama](./md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
      -  [📓] [Uso de llamada a función con ONNX](./md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)
  - Ejemplos de mezcla multimodal
    - Ejemplos Phi-4 🆕
      -  [📓] [Uso de Phi-4-multimodal como periodista tecnológico](./md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
      - [Aplicación consola .NET usando Phi-4-multimodal para analizar imágenes](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Ajuste fino de ejemplos Phi
  - [Escenarios de ajuste fino](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [Ajuste fino vs RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [Ajuste fino: Deja que Phi-3 se convierta en un experto de la industria](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [Ajuste fino de Phi-3 con AI Toolkit para VS Code](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Ajuste fino de Phi-3 con Azure Machine Learning Service](./md/03.FineTuning/Introduce_AzureML.md)
  - [Ajuste fino de Phi-3 con Lora](./md/03.FineTuning/FineTuning_Lora.md)
  - [Ajuste fino de Phi-3 con QLora](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Ajuste fino de Phi-3 con Microsoft Foundry](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Ajuste fino de Phi-3 con Azure ML CLI/SDK](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Ajuste fino con Microsoft Olive](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Laboratorio práctico de ajuste fino con Microsoft Olive](./md/03.FineTuning/olive-lab/readme.md)
  - [Ajuste fino de Phi-3-vision con Weights and Bias](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)

  - [Ajuste fino de Phi-3 con Apple MLX Framework](./md/03.FineTuning/FineTuning_MLX.md)
  - [Ajuste fino de Phi-3-vision (soporte oficial)](./md/03.FineTuning/FineTuning_Vision.md)
  - [Ajuste fino de Phi-3 con Kaito AKS, contenedores Azure (soporte oficial)](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Ajuste fino de Phi-3 y 3.5 Vision](https://github.com/2U1/Phi3-Vision-Finetune)

- Laboratorio práctico
  - [Explorando modelos de vanguardia: LLMs, SLMs, desarrollo local y más](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [Desbloqueando el potencial de NLP: ajuste fino con Microsoft Olive](https://github.com/azure/Ignite_FineTuning_workshop)

- Artículos y publicaciones académicas
  - [Los libros de texto son todo lo que necesitas II: informe técnico de phi-1.5](https://arxiv.org/abs/2309.05463)
  - [Informe técnico de Phi-3: un modelo de lenguaje altamente capaz localmente en tu teléfono](https://arxiv.org/abs/2404.14219)
  - [Informe técnico de Phi-4](https://arxiv.org/abs/2412.08905)
  - [Informe técnico de Phi-4-Mini: modelos multimodales compactos pero potentes mediante mezcla de LoRAs](https://arxiv.org/abs/2503.01743)
  - [Optimización de modelos de lenguaje pequeños para llamadas de función en vehículo](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) Ajuste fino de PHI-3 para respuesta a preguntas de opción múltiple: metodología, resultados y desafíos](https://arxiv.org/abs/2501.01588)
  - [Informe técnico de razonamiento Phi-4](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Informe técnico de razonamiento Phi-4-mini](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Uso de modelos Phi

### Phi en Microsoft Foundry

Puedes aprender cómo usar Microsoft Phi y cómo construir soluciones E2E en tus diferentes dispositivos de hardware. Para experimentar Phi por ti mismo, comienza jugando con los modelos y personalizando Phi para tus escenarios usando el [Catálogo de modelos de Azure AI de Microsoft Foundry](https://aka.ms/phi3-azure-ai) y puedes aprender más en Comenzando con [Microsoft Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md)

**Área de pruebas (Playground)**
Cada modelo tiene un área de pruebas dedicada para probar el modelo [Azure AI Playground](https://aka.ms/try-phi3).

### Phi en modelos de GitHub

Puedes aprender cómo usar Microsoft Phi y cómo construir soluciones E2E en tus diferentes dispositivos de hardware. Para experimentar Phi por ti mismo, comienza jugando con el modelo y personalizando Phi para tus escenarios usando el [Catálogo de modelos de GitHub](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) y puedes aprender más en Comenzando con [Catálogo de modelos de GitHub](/md/02.QuickStart/GitHubModel_QuickStart.md)

**Área de pruebas (Playground)**
Cada modelo tiene un [área de pruebas dedicada para probar el modelo](/md/02.QuickStart/GitHubModel_QuickStart.md).

### Phi en Hugging Face

También puedes encontrar el modelo en [Hugging Face](https://huggingface.co/microsoft)

**Área de pruebas (Playground)**
 [Área de pruebas de Hugging Chat](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

 ## 🎒 Otros cursos

¡Nuestro equipo produce otros cursos! Mira:

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
[![IA generativa para principiantes](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![IA generativa (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![IA generativa (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![IA generativa (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Aprendizaje principal
[![ML para principiantes](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Ciencia de datos para principiantes](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
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

Microsoft está comprometido a ayudar a nuestros clientes a usar nuestros productos de IA de manera responsable, compartiendo nuestros aprendizajes y construyendo asociaciones basadas en la confianza mediante herramientas como Notas de Transparencia y Evaluaciones de Impacto. Muchos de estos recursos se pueden encontrar en [https://aka.ms/RAI](https://aka.ms/RAI).
El enfoque de Microsoft para la IA responsable se basa en nuestros principios de IA de equidad, confiabilidad y seguridad, privacidad y seguridad, inclusión, transparencia y responsabilidad.

Modelos a gran escala de lenguaje natural, imagen y voz - como los usados en este ejemplo - pueden potencialmente comportarse de maneras que sean injustas, poco confiables u ofensivas, causando daños. Por favor, consulte la [nota de transparencia del servicio Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) para informarse sobre riesgos y limitaciones.


El enfoque recomendado para mitigar estos riesgos es incluir un sistema de seguridad en su arquitectura que pueda detectar y prevenir conductas dañinas. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) proporciona una capa independiente de protección, capaz de detectar contenido dañino generado por usuarios y por IA en aplicaciones y servicios. Azure AI Content Safety incluye APIs de texto e imagen que le permiten detectar material perjudicial. Dentro de Microsoft Foundry, el servicio Content Safety le permite ver, explorar y probar código de ejemplo para detectar contenido dañino en diferentes modalidades. La siguiente [documentación de inicio rápido](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) le guía para realizar solicitudes al servicio.

Otro aspecto a tener en cuenta es el desempeño general de la aplicación. En aplicaciones multimodales y multi-modelos, consideramos que el desempeño significa que el sistema funciona como usted y sus usuarios esperan, incluyendo no generar resultados dañinos. Es importante evaluar el desempeño de su aplicación general utilizando los [evaluadores de Desempeño y Calidad y de Riesgo y Seguridad](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in). También tiene la posibilidad de crear y evaluar con [evaluadores personalizados](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators).

Puede evaluar su aplicación de IA en su entorno de desarrollo utilizando el [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html). Dado un conjunto de datos de prueba o un objetivo, las generaciones de su aplicación de IA generativa se miden cuantitativamente con evaluadores integrados o evaluadores personalizados de su elección. Para comenzar con el Azure AI Evaluation SDK para evaluar su sistema, puede seguir la [guía de inicio rápido](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Una vez que ejecute una evaluación, puede [visualizar los resultados en Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Marcas Registradas

Este proyecto puede contener marcas registradas o logotipos de proyectos, productos o servicios. El uso autorizado de marcas o logotipos de Microsoft está sujeto a y debe seguir las [Directrices de Marcas y Marca Comercial de Microsoft](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).
El uso de marcas o logotipos de Microsoft en versiones modificadas de este proyecto no debe causar confusión ni implicar patrocinio por parte de Microsoft. Cualquier uso de marcas o logotipos de terceros está sujeto a las políticas de esos terceros.

## Obtener Ayuda

Si tiene problemas o alguna pregunta sobre la construcción de aplicaciones de IA, únase a:

[![Microsoft Foundry Discord](https://img.shields.io/badge/Discord-Microsoft_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

Si tiene comentarios del producto o errores durante la construcción, visite:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->