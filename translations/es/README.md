<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8f2577190cbe70305b9de13df37e1c9a",
  "translation_date": "2025-04-03T05:52:21+00:00",
  "source_file": "README.md",
  "language_code": "es"
}
-->
# Phi Cookbook: Ejemplos Prácticos con los Modelos Phi de Microsoft

[![Abrir y usar los ejemplos en GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Abrir en Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![Contribuidores en GitHub](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![Problemas en GitHub](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![Solicitudes de extracción en GitHub](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PRs Bienvenidos](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![Seguidores en GitHub](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![Forks en GitHub](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![Estrellas en GitHub](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Azure AI Community Discord](https://dcbadge.vercel.app/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

Phi es una serie de modelos de inteligencia artificial de código abierto desarrollados por Microsoft.

Actualmente, Phi es el modelo de lenguaje pequeño (SLM) más potente y rentable, con excelentes resultados en pruebas de multilingüismo, razonamiento, generación de texto/chat, programación, imágenes, audio y otros escenarios.

Puedes implementar Phi en la nube o en dispositivos de borde, y construir aplicaciones de IA generativa fácilmente con recursos computacionales limitados.

Sigue estos pasos para comenzar a usar estos recursos:
1. **Haz un Fork del Repositorio**: Haz clic en [![Forks en GitHub](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **Clona el Repositorio**: `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Únete a la Comunidad de Microsoft AI en Discord y conecta con expertos y otros desarrolladores**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/cover.2595d43b382944c601aebf88583314636768eece3d94e8e4448e03a4e5bedef4.es.png)

## 🌐 Soporte Multilingüe
[Francés](../fr/README.md) | [Español](./README.md) | [Alemán](../de/README.md) | [Ruso](../ru/README.md) | [Árabe](../ar/README.md) | [Persa (Farsi)](../fa/README.md) | [Urdu](../ur/README.md) | [Chino (Simplificado)](../zh/README.md) | [Chino (Tradicional, Macao)](../mo/README.md) | [Chino (Tradicional, Hong Kong)](../hk/README.md) | [Chino (Tradicional, Taiwán)](../tw/README.md) | [Japonés](../ja/README.md) | [Coreano](../ko/README.md) | [Hindi](../hi/README.md) | [Bengalí](../bn/README.md) | [Maratí](../mr/README.md) | [Nepalí](../ne/README.md) | [Punyabí (Gurmukhi)](../pa/README.md) | [Portugués (Portugal)](../pt/README.md) | [Portugués (Brasil)](../br/README.md) | [Italiano](../it/README.md) | [Polaco](../pl/README.md) | [Turco](../tr/README.md) | [Griego](../el/README.md) | [Tailandés](../th/README.md) | [Sueco](../sv/README.md) | [Danés](../da/README.md) | [Noruego](../no/README.md) | [Finlandés](../fi/README.md) | [Holandés](../nl/README.md) | [Hebreo](../he/README.md) | [Vietnamita](../vi/README.md) | [Indonesio](../id/README.md) | [Malayo](../ms/README.md) | [Tagalo (Filipino)](../tl/README.md) | [Suajili](../sw/README.md) | [Húngaro](../hu/README.md) | [Checo](../cs/README.md) | [Eslovaco](../sk/README.md) | [Rumano](../ro/README.md) | [Búlgaro](../bg/README.md) | [Serbio (Cirílico)](../sr/README.md) | [Croata](../hr/README.md) | [Esloveno](../sl/README.md)
## Tabla de Contenidos

- Introducción
  - [Bienvenido a la Familia Phi](./md/01.Introduction/01/01.PhiFamily.md)
  - [Configurando tu entorno](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [Entendiendo las Tecnologías Clave](./md/01.Introduction/01/01.Understandingtech.md)
  - [Seguridad de IA para Modelos Phi](./md/01.Introduction/01/01.AISafety.md)
  - [Soporte de Hardware para Phi](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Modelos Phi y Disponibilidad en diferentes plataformas](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Usando Guidance-ai y Phi](./md/01.Introduction/01/01.Guidance.md)
  - [Modelos en GitHub Marketplace](https://github.com/marketplace/models)
  - [Catálogo de Modelos de Azure AI](https://ai.azure.com)

- Inferencia de Phi en diferentes entornos
    - [Hugging Face](./md/01.Introduction/02/01.HF.md)
    - [Modelos de GitHub](./md/01.Introduction/02/02.GitHubModel.md)
    - [Catálogo de Modelos de Azure AI Foundry](./md/01.Introduction/02/03.AzureAIFoundry.md)
    - [Ollama](./md/01.Introduction/02/04.Ollama.md)
    - [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    - [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)

- Inferencia de la Familia Phi
    - [Inferencia de Phi en iOS](./md/01.Introduction/03/iOS_Inference.md)
    - [Inferencia de Phi en Android](./md/01.Introduction/03/Android_Inference.md)
    - [Inferencia de Phi en Jetson](./md/01.Introduction/03/Jetson_Inference.md)
    - [Inferencia de Phi en AI PC](./md/01.Introduction/03/AIPC_Inference.md)
    - [Inferencia de Phi con el Framework Apple MLX](./md/01.Introduction/03/MLX_Inference.md)
    - [Inferencia de Phi en un Servidor Local](./md/01.Introduction/03/Local_Server_Inference.md)
    - [Inferencia de Phi en un Servidor Remoto usando AI Toolkit](./md/01.Introduction/03/Remote_Interence.md)
    - [Inferencia de Phi con Rust](./md/01.Introduction/03/Rust_Inference.md)
    - [Inferencia de Phi--Vision en Local](./md/01.Introduction/03/Vision_Inference.md)
    - [Inferencia de Phi con Kaito AKS, Contenedores de Azure (soporte oficial)](./md/01.Introduction/03/Kaito_Inference.md)
- [Cuantificación de la Familia Phi](./md/01.Introduction/04/QuantifyingPhi.md)
    - [Cuantificación de Phi-3.5 / 4 usando llama.cpp](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [Cuantificación de Phi-3.5 / 4 usando extensiones de Generative AI para onnxruntime](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Cuantificación de Phi-3.5 / 4 usando Intel OpenVINO](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Cuantificación de Phi-3.5 / 4 usando el Framework Apple MLX](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

- Evaluación de Phi
- [Response AI](./md/01.Introduction/05/ResponsibleAI.md)  
    - [Azure AI Foundry para Evaluación](./md/01.Introduction/05/AIFoundry.md)  
    - [Usando Promptflow para Evaluación](./md/01.Introduction/05/Promptflow.md)  

- RAG con Azure AI Search  
    - [Cómo usar Phi-4-mini y Phi-4-multimodal (RAG) con Azure AI Search](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)  

- Ejemplos de desarrollo de aplicaciones Phi  
  - Aplicaciones de Texto y Chat  
    - Ejemplos Phi-4 🆕  
      - [📓] [Chat con el modelo Phi-4-mini ONNX](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)  
      - [Chat con el modelo local Phi-4 ONNX en .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)  
      - [Aplicación de consola .NET con Phi-4 ONNX usando Semantic Kernel](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)  
    - Ejemplos Phi-3 / 3.5  
      - [Chatbot local en el navegador usando Phi3, ONNX Runtime Web y WebGPU](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)  
      - [Chat con OpenVino](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)  
      - [Modelo múltiple - Phi-3-mini interactivo y OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)  
      - [MLFlow - Creando un wrapper y usando Phi-3 con MLFlow](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)  
      - [Optimización de modelos - Cómo optimizar el modelo Phi-3-min para ONNX Runtime Web con Olive](https://github.com/microsoft/Olive/tree/main/examples/phi3)  
      - [Aplicación WinUI3 con Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)  
      - [Aplicación de notas con IA de modelo múltiple en WinUI3](https://github.com/microsoft/ai-powered-notes-winui3-sample)  
      - [Ajuste fino e integración de modelos personalizados Phi-3 con Promptflow](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)  
      - [Ajuste fino e integración de modelos personalizados Phi-3 con Promptflow en Azure AI Foundry](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)  
      - [Evaluar el modelo ajustado Phi-3 / Phi-3.5 en Azure AI Foundry centrado en los principios de IA responsable de Microsoft](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)  
      - [📓] [Ejemplo de predicción de lenguaje con Phi-3.5-mini-instruct (Chino/Inglés)](../../md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)  
      - [Chatbot RAG WebGPU con Phi-3.5-Instruct](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)  
      - [Usando GPU de Windows para crear una solución Promptflow con Phi-3.5-Instruct ONNX](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)  
      - [Usando Microsoft Phi-3.5 tflite para crear una aplicación Android](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)  
      - [Ejemplo de preguntas y respuestas en .NET usando el modelo local Phi-3 ONNX con Microsoft.ML.OnnxRuntime](../../md/04.HOL/dotnet/src/LabsPhi301)  
      - [Aplicación de consola .NET con Semantic Kernel y Phi-3](../../md/04.HOL/dotnet/src/LabsPhi302)  

  - Ejemplos basados en código del SDK de inferencia de Azure AI  
    - Ejemplos Phi-4 🆕  
      - [📓] [Generar código de proyecto usando Phi-4-multimodal](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)  
    - Ejemplos Phi-3 / 3.5  
      - [Construye tu propio chat de GitHub Copilot en Visual Studio Code con la familia Phi-3 de Microsoft](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)  
      - [Crea tu propio agente de chat Copilot en Visual Studio Code con Phi-3.5 usando modelos de GitHub](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)  

  - Ejemplos de razonamiento avanzado  
    - Ejemplos Phi-4 🆕  
      - [📓] [Ejemplos de razonamiento con Phi-4-mini](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)  

  - Demos  
      - [Demos de Phi-4-mini alojados en Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)  
      - [Demos de Phi-4-multimodal alojados en Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)  

  - Ejemplos de visión  
    - Ejemplos Phi-4 🆕  
      - [📓] [Usar Phi-4-multimodal para leer imágenes y generar código](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md)  
    - Ejemplos Phi-3 / 3.5  
-  [📓][Phi-3-vision-Image text to text](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
      - [📓][Phi-3-vision CLIP Embedding](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [DEMO: Phi-3 Reciclaje](https://github.com/jennifermarsman/PhiRecycling/)
      - [Phi-3-vision - Asistente visual de lenguaje - con Phi3-Vision y OpenVINO](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
      - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
      - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
      - [📓][Phi-3.5 Vision muestra de múltiples cuadros o imágenes](../../md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
      - [Phi-3 Vision Modelo ONNX Local utilizando Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi303)
      - [Modelo ONNX Local Phi-3 Vision basado en menú utilizando Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi304)

  - Muestras de Audio
    - Muestras Phi-4 🆕
      - [📓] [Extracción de transcripciones de audio utilizando Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
      - [📓] [Muestra de audio Phi-4-multimodal](../../md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
      - [📓] [Muestra de traducción de voz Phi-4-multimodal](../../md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
      - [Aplicación de consola .NET utilizando Phi-4-multimodal para analizar un archivo de audio y generar transcripción](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

  - Muestras MOE
    - Muestras Phi-3 / 3.5
      - [📓] [Modelos Mixture of Experts (MoEs) Phi-3.5 muestra de redes sociales](../../md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
      - [📓] [Construcción de un pipeline de generación aumentada por recuperación (RAG) con NVIDIA NIM Phi-3 MOE, Azure AI Search y LlamaIndex](../../md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)
  - Muestras de Llamadas a Funciones
    - Muestras Phi-4 🆕
      -  [📓] [Uso de llamadas a funciones con Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
      -  [📓] [Uso de llamadas a funciones para crear múltiples agentes con Phi-4-mini](../../md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
      -  [📓] [Uso de llamadas a funciones con Ollama](../../md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
  - Muestras de Mezcla Multimodal
    - Muestras Phi-4 🆕
      -  [📓] [Uso de Phi-4-multimodal como periodista tecnológico](../../md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
      - [Aplicación de consola .NET utilizando Phi-4-multimodal para analizar imágenes](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Ajuste fino de muestras Phi
  - [Escenarios de ajuste fino](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [Ajuste fino vs RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [Ajuste fino Deja que Phi-3 se convierta en un experto en la industria](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [Ajuste fino Phi-3 con AI Toolkit para VS Code](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Ajuste fino Phi-3 con el servicio Azure Machine Learning](./md/03.FineTuning/Introduce_AzureML.md)
  - [Ajuste fino Phi-3 con Lora](./md/03.FineTuning/FineTuning_Lora.md)
  - [Ajuste fino Phi-3 con QLora](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Ajuste fino Phi-3 con Azure AI Foundry](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Ajuste fino Phi-3 con CLI/SDK de Azure ML](./md/03.FineTuning/FineTuning_MLSDK.md)
- [Ajuste fino con Microsoft Olive](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)  
  - [Laboratorio práctico de ajuste fino con Microsoft Olive](./md/03.FineTuning/olive-lab/readme.md)  
  - [Ajuste fino de Phi-3-vision con Weights and Bias](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)  
  - [Ajuste fino de Phi-3 con el framework Apple MLX](./md/03.FineTuning/FineTuning_MLX.md)  
  - [Ajuste fino de Phi-3-vision (soporte oficial)](./md/03.FineTuning/FineTuning_Vision.md)  
  - [Ajuste fino de Phi-3 con Kaito AKS, contenedores de Azure (soporte oficial)](./md/03.FineTuning/FineTuning_Kaito.md)  
  - [Ajuste fino de Phi-3 y Phi-3.5 Vision](https://github.com/2U1/Phi3-Vision-Finetune)  

- Laboratorio práctico  
  - [Explorando modelos de vanguardia: LLMs, SLMs, desarrollo local y más](https://github.com/microsoft/aitour-exploring-cutting-edge-models)  
  - [Liberando el potencial del NLP: Ajuste fino con Microsoft Olive](https://github.com/azure/Ignite_FineTuning_workshop)  

- Artículos de investigación académica y publicaciones  
  - [Textbooks Are All You Need II: informe técnico de phi-1.5](https://arxiv.org/abs/2309.05463)  
  - [Informe técnico de Phi-3: un modelo de lenguaje altamente capaz en tu teléfono](https://arxiv.org/abs/2404.14219)  
  - [Informe técnico de Phi-4](https://arxiv.org/abs/2412.08905)  
  - [Informe técnico de Phi-4-Mini: Modelos de lenguaje multimodal compactos pero potentes mediante Mixture-of-LoRAs](https://arxiv.org/abs/2503.01743)  
  - [Optimización de modelos de lenguaje pequeños para llamadas de funciones en vehículos](https://arxiv.org/abs/2501.02342)  
  - [(WhyPHI) Ajuste fino de PHI-3 para responder preguntas de opción múltiple: metodología, resultados y desafíos](https://arxiv.org/abs/2501.01588)  

## Uso de modelos Phi  

### Phi en Azure AI Foundry  

Puedes aprender cómo usar Microsoft Phi y cómo construir soluciones de extremo a extremo en tus diferentes dispositivos de hardware. Para experimentar Phi por ti mismo, comienza probando los modelos y personalizando Phi para tus escenarios usando el [Catálogo de Modelos de Azure AI Foundry](https://aka.ms/phi3-azure-ai). Puedes aprender más en Introducción a [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md).  

**Playground**  
Cada modelo tiene un playground dedicado para probar el modelo [Azure AI Playground](https://aka.ms/try-phi3).  

### Phi en Modelos de GitHub  

Puedes aprender cómo usar Microsoft Phi y cómo construir soluciones de extremo a extremo en tus diferentes dispositivos de hardware. Para experimentar Phi por ti mismo, comienza probando el modelo y personalizando Phi para tus escenarios usando el [Catálogo de Modelos de GitHub](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo). Puedes aprender más en Introducción al [Catálogo de Modelos de GitHub](/md/02.QuickStart/GitHubModel_QuickStart.md).  

**Playground**  
Cada modelo tiene un [playground dedicado para probar el modelo](/md/02.QuickStart/GitHubModel_QuickStart.md).  

### Phi en Hugging Face  

También puedes encontrar el modelo en [Hugging Face](https://huggingface.co/microsoft).  

**Playground**  
[Playground de Hugging Chat](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct).  

## IA Responsable  

Microsoft está comprometido a ayudar a nuestros clientes a usar nuestros productos de IA de manera responsable, compartiendo lo que hemos aprendido y construyendo asociaciones basadas en la confianza mediante herramientas como Notas de Transparencia y Evaluaciones de Impacto. Muchos de estos recursos se encuentran en [https://aka.ms/RAI](https://aka.ms/RAI).  
El enfoque de Microsoft hacia la IA responsable se basa en nuestros principios de IA: equidad, confiabilidad y seguridad, privacidad y protección, inclusión, transparencia y responsabilidad.  

Los modelos a gran escala de lenguaje natural, imágenes y voz, como los utilizados en este ejemplo, pueden comportarse de manera injusta, poco confiable o ofensiva, causando daños. Consulta la [Nota de Transparencia del servicio Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) para estar informado sobre riesgos y limitaciones.  

El enfoque recomendado para mitigar estos riesgos es incluir un sistema de seguridad en tu arquitectura que pueda detectar y prevenir comportamientos dañinos. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) proporciona una capa de protección independiente, capaz de detectar contenido dañino generado por usuarios y por IA en aplicaciones y servicios. Azure AI Content Safety incluye APIs de texto e imagen que permiten detectar material dañino. Dentro de Azure AI Foundry, el servicio Content Safety te permite ver, explorar y probar código de ejemplo para detectar contenido dañino en diferentes modalidades. La siguiente [documentación de inicio rápido](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) te guía a través de cómo realizar solicitudes al servicio.  

Otro aspecto a tener en cuenta es el rendimiento general de la aplicación. Con aplicaciones multimodales y multimodelos, consideramos el rendimiento como la capacidad del sistema de cumplir con las expectativas tuyas y de tus usuarios, incluyendo no generar resultados dañinos. Es importante evaluar el rendimiento de tu aplicación general usando [Evaluadores de Rendimiento y Calidad y Evaluadores de Riesgo y Seguridad](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in). También tienes la capacidad de crear y evaluar con [evaluadores personalizados](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators).  
Puedes evaluar tu aplicación de inteligencia artificial en tu entorno de desarrollo utilizando el [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html). Dado un conjunto de datos de prueba o un objetivo, las generaciones de tu aplicación de inteligencia artificial generativa se miden cuantitativamente con evaluadores integrados o evaluadores personalizados de tu elección. Para comenzar con el SDK de evaluación de Azure AI y evaluar tu sistema, puedes seguir la [guía de inicio rápido](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Una vez que ejecutes una evaluación, puedes [visualizar los resultados en Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Marcas Registradas

Este proyecto puede contener marcas registradas o logotipos de proyectos, productos o servicios. El uso autorizado de marcas registradas o logotipos de Microsoft está sujeto a y debe cumplir con las [Directrices de Marca y Logotipo de Microsoft](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).  
El uso de marcas registradas o logotipos de Microsoft en versiones modificadas de este proyecto no debe causar confusión ni implicar patrocinio por parte de Microsoft. Cualquier uso de marcas registradas o logotipos de terceros está sujeto a las políticas de esos terceros.

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por un humano. No nos hacemos responsables de ningún malentendido o interpretación errónea que surja del uso de esta traducción.