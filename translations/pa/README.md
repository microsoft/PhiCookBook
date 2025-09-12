<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "698f7f3d48ebc9e25a273d7c8b7e31c5",
  "translation_date": "2025-09-12T13:42:00+00:00",
  "source_file": "README.md",
  "language_code": "pa"
}
-->
# ਫਾਈ ਕੂਕਬੁੱਕ: ਮਾਈਕਰੋਸਾਫਟ ਦੇ ਫਾਈ ਮਾਡਲਾਂ ਨਾਲ ਹੱਥ-ਵਧਾਈ ਉਦਾਹਰਨ

ਫਾਈ ਮਾਈਕਰੋਸਾਫਟ ਦੁਆਰਾ ਵਿਕਸਿਤ ਖੁੱਲੇ ਸਰੋਤ AI ਮਾਡਲਾਂ ਦੀ ਇੱਕ ਲੜੀ ਹੈ।

ਫਾਈ ਇਸ ਸਮੇਂ ਸਭ ਤੋਂ ਸ਼ਕਤੀਸ਼ਾਲੀ ਅਤੇ ਲਾਗਤ-ਪ੍ਰਭਾਵੀ ਛੋਟਾ ਭਾਸ਼ਾ ਮਾਡਲ (SLM) ਹੈ, ਜੋ ਬਹੁ-ਭਾਸ਼ਾ, ਤਰਕ, ਟੈਕਸਟ/ਚੈਟ ਜਨਰੇਸ਼ਨ, ਕੋਡਿੰਗ, ਚਿੱਤਰ, ਆਡੀਓ ਅਤੇ ਹੋਰ ਸਥਿਤੀਆਂ ਵਿੱਚ ਬਹੁਤ ਵਧੀਆ ਬੈਂਚਮਾਰਕ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ।

ਤੁਸੀਂ ਫਾਈ ਨੂੰ ਕਲਾਉਡ ਜਾਂ ਐਜ ਡਿਵਾਈਸਾਂ 'ਤੇ ਤੈਨਾਤ ਕਰ ਸਕਦੇ ਹੋ, ਅਤੇ ਤੁਸੀਂ ਘੱਟ ਗਣਨਾ ਸ਼ਕਤੀ ਨਾਲ ਜਨਰੇਟਿਵ AI ਐਪਲੀਕੇਸ਼ਨ ਆਸਾਨੀ ਨਾਲ ਬਣਾਉਣ ਦੇ ਯੋਗ ਹੋ।

ਇਹ ਸਰੋਤਾਂ ਦੀ ਵਰਤੋਂ ਸ਼ੁਰੂ ਕਰਨ ਲਈ ਹੇਠਾਂ ਦਿੱਤੇ ਕਦਮਾਂ ਦੀ ਪਾਲਣਾ ਕਰੋ:
1. **ਰਿਪੋਜ਼ਟਰੀ ਨੂੰ ਫੋਰਕ ਕਰੋ**: ਕਲਿੱਕ ਕਰੋ [![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **ਰਿਪੋਜ਼ਟਰੀ ਨੂੰ ਕਲੋਨ ਕਰੋ**: `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**ਮਾਈਕਰੋਸਾਫਟ AI ਡਿਸਕੋਰਡ ਕਮਿਊਨਿਟੀ ਵਿੱਚ ਸ਼ਾਮਲ ਹੋਵੋ ਅਤੇ ਮਾਹਰਾਂ ਅਤੇ ਸਾਥੀ ਡਿਵੈਲਪਰਾਂ ਨਾਲ ਮਿਲੋ**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../imgs/cover.png)

### 🌐 ਬਹੁ-ਭਾਸ਼ਾ ਸਹਾਇਤਾ

#### GitHub Action ਰਾਹੀਂ ਸਹਾਇਤ (ਆਟੋਮੈਟਿਕ ਅਤੇ ਹਮੇਸ਼ਾ ਅਪ-ਟੂ-ਡੇਟ)

[ਫਰੈਂਚ](../fr/README.md) | [ਸਪੈਨਿਸ਼](../es/README.md) | [ਜਰਮਨ](../de/README.md) | [ਰੂਸੀ](../ru/README.md) | [ਅਰਬੀ](../ar/README.md) | [ਫ਼ਾਰਸੀ](../fa/README.md) | [ਉਰਦੂ](../ur/README.md) | [ਚੀਨੀ (ਸਰਲ)](../zh/README.md) | [ਚੀਨੀ (ਰਵਾਇਤੀ, ਮਕਾਉ)](../mo/README.md) | [ਚੀਨੀ (ਰਵਾਇਤੀ, ਹਾਂਗਕਾਂਗ)](../hk/README.md) | [ਚੀਨੀ (ਰਵਾਇਤੀ, ਤਾਈਵਾਨ)](../tw/README.md) | [ਜਾਪਾਨੀ](../ja/README.md) | [ਕੋਰੀਆਈ](../ko/README.md) | [ਹਿੰਦੀ](../hi/README.md)  
[ਬੰਗਾਲੀ](../bn/README.md) | [ਮਰਾਠੀ](../mr/README.md) | [ਨੇਪਾਲੀ](../ne/README.md) | [ਪੰਜਾਬੀ (ਗੁਰਮੁਖੀ)](./README.md) | [ਪੁਰਤਗਾਲੀ (ਪੁਰਤਗਾਲ)](../pt/README.md) | [ਪੁਰਤਗਾਲੀ (ਬ੍ਰਾਜ਼ੀਲ)](../br/README.md) | [ਇਟਾਲੀਅਨ](../it/README.md) | [ਪੋਲਿਸ਼](../pl/README.md) | [ਤੁਰਕੀ](../tr/README.md) | [ਯੂਨਾਨੀ](../el/README.md) | [ਥਾਈ](../th/README.md) | [ਸਵੀਡਿਸ਼](../sv/README.md) | [ਡੈਨਿਸ਼](../da/README.md) | [ਨਾਰਵੇਜੀਅਨ](../no/README.md) | [ਫਿਨਿਸ਼](../fi/README.md) | [ਡੱਚ](../nl/README.md) | [ਹਿਬਰੂ](../he/README.md) | [ਵਿਯਤਨਾਮੀ](../vi/README.md) | [ਇੰਡੋਨੇਸ਼ੀਆਈ](../id/README.md) | [ਮਲੇ](../ms/README.md) | [ਟੈਗਾਲੋਗ (ਫਿਲੀਪੀਨੋ)](../tl/README.md) | [ਸਵਾਹਿਲੀ](../sw/README.md) | [ਹੰਗਰੀ](../hu/README.md) | [ਚੈਕ](../cs/README.md) | [ਸਲੋਵਾਕ](../sk/README.md) | [ਰੋਮਾਨੀ](../ro/README.md) | [ਬੁਲਗਾਰੀਆਈ](../bg/README.md) | [ਸਰਬੀਆਈ (ਸਿਰਿਲਿਕ)](../sr/README.md) | [ਕਰੋਏਸ਼ੀਆਈ](../hr/README.md) | [ਸਲੋਵੇਨੀਆਈ](../sl/README.md)

## ਸਮੱਗਰੀ ਦੀ ਸੂਚੀ

- ਪਰਿਚਯ
  - [ਫਾਈ ਪਰਿਵਾਰ ਵਿੱਚ ਤੁਹਾਡਾ ਸਵਾਗਤ ਹੈ](./md/01.Introduction/01/01.PhiFamily.md)
  - [ਆਪਣੇ ਵਾਤਾਵਰਣ ਨੂੰ ਸੈਟ ਕਰਨਾ](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [ਮੁੱਖ ਤਕਨਾਲੋਜੀਆਂ ਨੂੰ ਸਮਝਣਾ](./md/01.Introduction/01/01.Understandingtech.md)
  - [ਫਾਈ ਮਾਡਲਾਂ ਲਈ AI ਸੁਰੱਖਿਆ](./md/01.Introduction/01/01.AISafety.md)
  - [ਫਾਈ ਹਾਰਡਵੇਅਰ ਸਹਾਇਤਾ](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [ਫਾਈ ਮਾਡਲ ਅਤੇ ਪਲੇਟਫਾਰਮਾਂ 'ਤੇ ਉਪਲਬਧਤਾ](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Guidance-ai ਅਤੇ ਫਾਈ ਦੀ ਵਰਤੋਂ](./md/01.Introduction/01/01.Guidance.md)
  - [GitHub ਮਾਰਕੀਟਪਲੇਸ ਮਾਡਲ](https://github.com/marketplace/models)
  - [Azure AI ਮਾਡਲ ਕੈਟਾਲਾਗ](https://ai.azure.com)

- ਵੱਖ-ਵੱਖ ਵਾਤਾਵਰਣਾਂ ਵਿੱਚ ਫਾਈ ਇੰਫਰੈਂਸ
    - [Hugging face](./md/01.Introduction/02/01.HF.md)
    - [GitHub ਮਾਡਲ](./md/01.Introduction/02/02.GitHubModel.md)
    - [Azure AI Foundry ਮਾਡਲ ਕੈਟਾਲਾਗ](./md/01.Introduction/02/03.AzureAIFoundry.md)
    - [Ollama](./md/01.Introduction/02/04.Ollama.md)
    - [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    - [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    - [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md)

- ਫਾਈ ਪਰਿਵਾਰ ਇੰਫਰੈਂਸ
    - [iOS ਵਿੱਚ ਫਾਈ ਇੰਫਰੈਂਸ](./md/01.Introduction/03/iOS_Inference.md)
    - [ਐਂਡਰਾਇਡ ਵਿੱਚ ਫਾਈ ਇੰਫਰੈਂਸ](./md/01.Introduction/03/Android_Inference.md)
    - [Jetson ਵਿੱਚ ਫਾਈ ਇੰਫਰੈਂਸ](./md/01.Introduction/03/Jetson_Inference.md)
    - [AI PC ਵਿੱਚ ਫਾਈ ਇੰਫਰੈਂਸ](./md/01.Introduction/03/AIPC_Inference.md)
    - [Apple MLX Framework ਨਾਲ ਫਾਈ ਇੰਫਰੈਂਸ](./md/01.Introduction/03/MLX_Inference.md)
    - [ਲੋਕਲ ਸਰਵਰ ਵਿੱਚ ਫਾਈ ਇੰਫਰੈਂਸ](./md/01.Introduction/03/Local_Server_Inference.md)
    - [AI Toolkit ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਰਿਮੋਟ ਸਰਵਰ ਵਿੱਚ ਫਾਈ ਇੰਫਰੈਂਸ](./md/01.Introduction/03/Remote_Interence.md)
    - [Rust ਨਾਲ ਫਾਈ ਇੰਫਰੈਂਸ](./md/01.Introduction/03/Rust_Inference.md)
    - [ਲੋਕਲ ਵਿੱਚ ਫਾਈ--Vision ਇੰਫਰੈਂਸ](./md/01.Introduction/03/Vision_Inference.md)
    - [Kaito AKS, Azure Containers (ਅਧਿਕਾਰਤ ਸਹਾਇਤਾ) ਨਾਲ ਫਾਈ ਇੰਫਰੈਂਸ](./md/01.Introduction/03/Kaito_Inference.md)

- [ਫਾਈ ਪਰਿਵਾਰ ਦੀ ਮਾਤਰਾ](./md/01.Introduction/04/QuantifyingPhi.md)
    - [llama.cpp ਦੀ ਵਰਤੋਂ ਕਰਕੇ Phi-3.5 / 4 ਨੂੰ ਮਾਤਰਾ](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [onnxruntime ਲਈ Generative AI ਐਕਸਟੈਂਸ਼ਨ ਦੀ ਵਰਤੋਂ ਕਰਕੇ Phi-3.5 / 4 ਨੂੰ ਮਾਤਰਾ](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Intel OpenVINO ਦੀ ਵਰਤੋਂ ਕਰਕੇ Phi-3.5 / 4 ਨੂੰ ਮਾਤਰਾ](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Apple MLX Framework ਦੀ ਵਰਤੋਂ ਕਰਕੇ Phi-3.5 / 4 ਨੂੰ ਮਾਤਰਾ](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

- ਫਾਈ ਦਾ ਮੁਲਾਂਕਨ
    - [ਜਵਾਬਦੇਹ AI](./md/01.Introduction/05/ResponsibleAI.md)
    - [ਮੁਲਾਂਕਨ ਲਈ Azure AI Foundry](./md/01.Introduction/05/AIFoundry.md)
    - [ਮੁਲਾਂਕਨ ਲਈ Promptflow ਦੀ ਵਰਤੋਂ](./md/01.Introduction/05/Promptflow.md)

- Azure AI Search ਨਾਲ RAG
    - [Azure AI Search ਨਾਲ Phi-4-mini ਅਤੇ Phi-4-multimodal (RAG) ਦੀ ਵਰਤੋਂ ਕਰਨ ਦਾ ਤਰੀਕਾ](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- ਫਾਈ ਐਪਲੀਕੇਸ਼ਨ ਵਿਕਾਸ ਦੇ ਨਮੂਨੇ
  - ਟੈਕਸਟ ਅਤੇ ਚੈਟ ਐਪਲੀਕੇਸ਼ਨ
    - Phi-4 ਨਮੂਨੇ 🆕
      - [📓] [Phi-4-mini ONNX ਮਾਡਲ ਨਾਲ ਚੈਟ ਕਰੋ](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Phi-4 local ONNX ਮਾਡਲ .NET ਨਾਲ ਚੈਟ ਕਰੋ](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Sementic Kernel ਦੀ ਵਰਤੋਂ ਕਰਕੇ Phi-4 ONNX ਨਾਲ .NET Console ਐਪ ਚੈਟ](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Phi-3 / 3.5 ਨਮੂਨੇ
      - [ਬ੍ਰਾਊਜ਼ਰ ਵਿੱਚ Phi3, ONNX Runtime Web ਅਤੇ WebGPU ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਲੋਕਲ ਚੈਟਬੋਟ](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVino ਚੈਟ](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [ਮਲਟੀ ਮਾਡਲ - ਇੰਟਰਐਕਟਿਵ Phi-3-mini ਅਤੇ OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - ਇੱਕ ਰੈਪਰ ਬਣਾਉਣਾ ਅਤੇ MLFlow ਨਾਲ Phi-3 ਦੀ ਵਰਤੋਂ](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [ਮਾਡਲ ਅਪਟਿਮਾਈਜ਼ੇਸ਼ਨ - Olive ਨਾਲ ONNX Runtime Web ਲਈ Phi-3-min ਮਾਡਲ ਨੂੰ ਕਿਵੇਂ ਅਪਟਿਮਾਈਜ਼ ਕਰਨਾ ਹੈ](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [WinUI3 ਐਪ ਨਾਲ Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      - [WinUI3 ਮਲਟੀ ਮਾਡਲ AI Powered Notes ਐਪ ਨਮੂਨਾ](https://github.com/microsoft/ai-powered-notes-winui3-sample)
- [ਕਸਟਮ Phi-3 ਮਾਡਲਾਂ ਨੂੰ ਫਾਈਨ-ਟਿਊਨ ਅਤੇ ਪ੍ਰੌਮਪਟ ਫਲੋ ਨਾਲ ਇੰਟੀਗ੍ਰੇਟ ਕਰੋ](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)  
- [Azure AI Foundry ਵਿੱਚ ਕਸਟਮ Phi-3 ਮਾਡਲਾਂ ਨੂੰ ਫਾਈਨ-ਟਿਊਨ ਅਤੇ ਪ੍ਰੌਮਪਟ ਫਲੋ ਨਾਲ ਇੰਟੀਗ੍ਰੇਟ ਕਰੋ](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)  
- [Microsoft ਦੇ ਜ਼ਿੰਮੇਵਾਰ AI ਸਿਧਾਂਤਾਂ 'ਤੇ ਧਿਆਨ ਦੇਂਦੇ ਹੋਏ Azure AI Foundry ਵਿੱਚ ਫਾਈਨ-ਟਿਊਨ ਕੀਤੇ Phi-3 / Phi-3.5 ਮਾਡਲ ਦਾ ਮੁਲਾਂਕਨ ਕਰੋ](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)  
- [📓] [Phi-3.5-mini-instruct ਭਾਸ਼ਾ ਅਨੁਮਾਨ ਨਮੂਨਾ (ਚੀਨੀ/ਅੰਗਰੇਜ਼ੀ)](../../md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)  
- [Phi-3.5-Instruct WebGPU RAG ਚੈਟਬੋਟ](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)  
- [Windows GPU ਦੀ ਵਰਤੋਂ ਕਰਕੇ Phi-3.5-Instruct ONNX ਨਾਲ ਪ੍ਰੌਮਪਟ ਫਲੋ ਹੱਲ ਬਣਾਉਣਾ](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)  
- [Microsoft Phi-3.5 tflite ਦੀ ਵਰਤੋਂ ਕਰਕੇ Android ਐਪ ਬਣਾਉਣਾ](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)  
- [Microsoft.ML.OnnxRuntime ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਸਥਾਨਕ ONNX Phi-3 ਮਾਡਲ ਨਾਲ Q&A .NET ਉਦਾਹਰਨ](../../md/04.HOL/dotnet/src/LabsPhi301)  
- [Semantic Kernel ਅਤੇ Phi-3 ਨਾਲ Console ਚੈਟ .NET ਐਪ](../../md/04.HOL/dotnet/src/LabsPhi302)  

- Azure AI Inference SDK ਕੋਡ ਅਧਾਰਿਤ ਨਮੂਨੇ  
  - Phi-4 ਨਮੂਨੇ 🆕  
    - [📓] [Phi-4-multimodal ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਪ੍ਰੋਜੈਕਟ ਕੋਡ ਜਨਰੇਟ ਕਰੋ](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)  
  - Phi-3 / 3.5 ਨਮੂਨੇ  
    - [Microsoft Phi-3 ਪਰਿਵਾਰ ਨਾਲ ਆਪਣਾ Visual Studio Code GitHub Copilot Chat ਬਣਾਓ](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)  
    - [GitHub ਮਾਡਲਾਂ ਦੁਆਰਾ Phi-3.5 ਨਾਲ ਆਪਣਾ Visual Studio Code Chat Copilot Agent ਬਣਾਓ](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)  

- ਉੱਚ-ਸਤ੍ਹਾ ਤਰਕ ਨਮੂਨੇ  
  - Phi-4 ਨਮੂਨੇ 🆕  
    - [📓] [Phi-4-mini-reasoning ਜਾਂ Phi-4-reasoning ਨਮੂਨੇ](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)  
    - [📓] [Microsoft Olive ਨਾਲ Phi-4-mini-reasoning ਨੂੰ ਫਾਈਨ-ਟਿਊਨ ਕਰਨਾ](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)  
    - [📓] [Apple MLX ਨਾਲ Phi-4-mini-reasoning ਨੂੰ ਫਾਈਨ-ਟਿਊਨ ਕਰਨਾ](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)  
    - [📓] [GitHub ਮਾਡਲਾਂ ਨਾਲ Phi-4-mini-reasoning](../../md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)  
    - [📓] [Azure AI Foundry ਮਾਡਲਾਂ ਨਾਲ Phi-4-mini-reasoning](../../md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)  
- ਡੈਮੋ  
    - [Hugging Face Spaces 'ਤੇ ਹੋਸਟ ਕੀਤੇ Phi-4-mini ਡੈਮੋ](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)  
    - [Hugging Face Spaces 'ਤੇ ਹੋਸਟ ਕੀਤੇ Phi-4-multimodal ਡੈਮੋ](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)  
- ਵਿਜ਼ਨ ਨਮੂਨੇ  
  - Phi-4 ਨਮੂਨੇ 🆕  
    - [📓] [ਤਸਵੀਰਾਂ ਪੜ੍ਹਨ ਅਤੇ ਕੋਡ ਜਨਰੇਟ ਕਰਨ ਲਈ Phi-4-multimodal ਦੀ ਵਰਤੋਂ ਕਰੋ](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md)  
  - Phi-3 / 3.5 ਨਮੂਨੇ  
    - [📓][Phi-3-vision-ਤਸਵੀਰ ਟੈਕਸਟ ਤੋਂ ਟੈਕਸਟ](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)  
    - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)  
    - [📓][Phi-3-vision CLIP Embedding](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)  
    - [ਡੈਮੋ: Phi-3 ਰੀਸਾਈਕਲਿੰਗ](https://github.com/jennifermarsman/PhiRecycling/)  
    - [Phi-3-vision - ਵਿਜ਼ੁਅਲ ਭਾਸ਼ਾ ਸਹਾਇਕ - Phi3-Vision ਅਤੇ OpenVINO ਨਾਲ](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)  
    - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)  
    - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)  
    - [📓][Phi-3.5 Vision ਮਲਟੀ-ਫਰੇਮ ਜਾਂ ਮਲਟੀ-ਤਸਵੀਰ ਨਮੂਨਾ](../../md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)  
    - [Microsoft.ML.OnnxRuntime .NET ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਸਥਾਨਕ ONNX ਮਾਡਲ ਨਾਲ Phi-3 Vision](../../md/04.HOL/dotnet/src/LabsPhi303)  
    - [Microsoft.ML.OnnxRuntime .NET ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਮੀਨੂ ਅਧਾਰਿਤ Phi-3 Vision ਸਥਾਨਕ ONNX ਮਾਡਲ](../../md/04.HOL/dotnet/src/LabsPhi304)  

- ਗਣਿਤ ਨਮੂਨੇ  
  - Phi-4-Mini-Flash-Reasoning-Instruct ਨਮੂਨੇ 🆕 [Phi-4-Mini-Flash-Reasoning-Instruct ਨਾਲ ਗਣਿਤ ਡੈਮੋ](../../md/02.Application/09.Math/MathDemo.ipynb)  

- ਆਡੀਓ ਨਮੂਨੇ  
  - Phi-4 ਨਮੂਨੇ 🆕  
    - [📓] [Phi-4-multimodal ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਆਡੀਓ ਟ੍ਰਾਂਸਕ੍ਰਿਪਟ ਕੱਢਣਾ](./md/02.Application/05.Audio/Phi4/Transciption/README.md)  
    - [📓] [Phi-4-multimodal ਆਡੀਓ ਨਮੂਨਾ](../../md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)  
    - [📓] [Phi-4-multimodal ਸਪੀਚ ਅਨੁਵਾਦ ਨਮੂਨਾ](../../md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)  
    - [.NET console ਐਪਲੀਕੇਸ਼ਨ Phi-4-multimodal ਆਡੀਓ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਆਡੀਓ ਫਾਈਲ ਦਾ ਵਿਸ਼ਲੇਸ਼ਣ ਕਰਨ ਅਤੇ ਟ੍ਰਾਂਸਕ੍ਰਿਪਟ ਜਨਰੇਟ ਕਰਨ ਲਈ](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)  

- MOE ਨਮੂਨੇ  
  - Phi-3 / 3.5 ਨਮੂਨੇ  
    - [📓] [Phi-3.5 Mixture of Experts Models (MoEs) ਸੋਸ਼ਲ ਮੀਡੀਆ ਨਮੂਨਾ](../../md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)  
    - [📓] [NVIDIA NIM Phi-3 MOE, Azure AI Search, ਅਤੇ LlamaIndex ਨਾਲ Retrieval-Augmented Generation (RAG) ਪਾਈਪਲਾਈਨ ਬਣਾਉਣਾ](../../md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)  

- ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਨਮੂਨੇ  
  - Phi-4 ਨਮੂਨੇ 🆕  
    - [📓] [Phi-4-mini ਨਾਲ ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਦੀ ਵਰਤੋਂ](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)  
    - [📓] [Phi-4-mini ਨਾਲ ਮਲਟੀ-ਏਜੰਟ ਬਣਾਉਣ ਲਈ ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਦੀ ਵਰਤੋਂ](../../md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)  
    - [📓] [Ollama ਨਾਲ ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਦੀ ਵਰਤੋਂ](../../md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)  
    - [📓] [ONNX ਨਾਲ ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਦੀ ਵਰਤੋਂ](../../md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)  

- ਮਲਟੀਮੋਡਲ ਮਿਕਸਿੰਗ ਨਮੂਨੇ  
  - Phi-4 ਨਮੂਨੇ 🆕  
    - [📓] [ਟੈਕਨਾਲੋਜੀ ਜਰਨਲਿਸਟ ਵਜੋਂ Phi-4-multimodal ਦੀ ਵਰਤੋਂ](../../md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)  
    - [.NET console ਐਪਲੀਕੇਸ਼ਨ Phi-4-multimodal ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਤਸਵੀਰਾਂ ਦਾ ਵਿਸ਼ਲੇਸ਼ਣ ਕਰਨ ਲਈ](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)  

- Phi ਨਮੂਨਿਆਂ ਨੂੰ ਫਾਈਨ-ਟਿਊਨ ਕਰਨਾ  
  - [ਫਾਈਨ-ਟਿਊਨ ਕਰਨ ਦੇ ਸਥਿਤੀਆਂ](./md/03.FineTuning/FineTuning_Scenarios.md)  
  - [ਫਾਈਨ-ਟਿਊਨਿੰਗ ਵਿਰੁੱਧ RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)  
  - [Phi-3 ਨੂੰ ਉਦਯੋਗ ਵਿਸ਼ੇਸ਼ਗਿਆ ਬਣਨ ਦਿਓ](./md/03.FineTuning/LetPhi3gotoIndustriy.md)  
  - [Phi-3 ਨੂੰ VS Code ਲਈ AI Toolkit ਨਾਲ ਫਾਈਨ-ਟਿਊਨ ਕਰਨਾ](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)  
  - [Phi-3 ਨੂੰ Azure Machine Learning Service ਨਾਲ ਫਾਈਨ-ਟਿਊਨ ਕਰਨਾ](./md/03.FineTuning/Introduce_AzureML.md)  
  - [Phi-3 ਨੂੰ Lora ਨਾਲ ਫਾਈਨ-ਟਿਊਨ ਕਰਨਾ](./md/03.FineTuning/FineTuning_Lora.md)  
  - [Phi-3 ਨੂੰ QLora ਨਾਲ ਫਾਈਨ-ਟਿਊਨ ਕਰਨਾ](./md/03.FineTuning/FineTuning_Qlora.md)  
  - [Phi-3 ਨੂੰ Azure AI Foundry ਨਾਲ ਫਾਈਨ-ਟਿਊਨ ਕਰਨਾ](./md/03.FineTuning/FineTuning_AIFoundry.md)  
  - [Phi-3 ਨੂੰ Azure ML CLI/SDK ਨਾਲ ਫਾਈਨ-ਟਿਊਨ ਕਰਨਾ](./md/03.FineTuning/FineTuning_MLSDK.md)  
  - [Microsoft Olive ਨਾਲ ਫਾਈਨ-ਟਿਊਨ ਕਰਨਾ](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)  
  - [Microsoft Olive Hands-On Lab ਨਾਲ ਫਾਈਨ-ਟਿਊਨ ਕਰਨਾ](./md/03.FineTuning/olive-lab/readme.md)  
  - [Weights and Bias ਨਾਲ Phi-3-vision ਨੂੰ ਫਾਈਨ-ਟਿਊਨ ਕਰਨਾ](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)  
  - [Apple MLX Framework ਨਾਲ Phi-3 ਨੂੰ ਫਾਈਨ-ਟਿਊਨ ਕਰਨਾ](./md/03.FineTuning/FineTuning_MLX.md)  
  - [Phi-3-vision ਨੂੰ ਫਾਈਨ-ਟਿਊਨ ਕਰਨਾ (ਆਧਿਕਾਰਿਕ ਸਹਾਇਤਾ)](./md/03.FineTuning/FineTuning_Vision.md)  
  - [Kaito AKS, Azure Containers ਨਾਲ Phi-3 ਨੂੰ ਫਾਈਨ-ਟਿਊਨ ਕਰਨਾ (ਆਧਿਕਾਰਿਕ ਸਹਾਇਤਾ)](./md/03.FineTuning/FineTuning_Kaito.md)  
  - [Phi-3 ਅਤੇ 3.5 Vision ਨੂੰ ਫਾਈਨ-ਟਿਊਨ ਕਰਨਾ](https://github.com/2U1/Phi3-Vision-Finetune)  

- Hands-on Lab  
  - [ਅਗਰਗੰਨੀ ਮਾਡਲਾਂ ਦੀ ਖੋਜ ਕਰਨਾ: LLMs, SLMs, ਸਥਾਨਕ ਵਿਕਾਸ ਅਤੇ ਹੋਰ](https://github.com/microsoft/aitour-exploring-cutting-edge-models)  
  - [NLP ਸਮਰਥਾ ਨੂੰ ਅਨਲੌਕ ਕਰਨਾ: Microsoft Olive ਨਾਲ ਫਾਈਨ-ਟਿਊਨ ਕਰਨਾ](https://github.com/azure/Ignite_FineTuning_workshop)  

- ਅਕਾਦਮਿਕ ਰਿਸਰਚ ਪੇਪਰ ਅਤੇ ਪ੍ਰਕਾਸ਼ਨ  
  - [Textbooks Are All You Need II: phi-1.5 ਤਕਨੀਕੀ ਰਿਪੋਰਟ](https://arxiv.org/abs/2309.05463)  
  - [Phi-3 ਤਕਨੀਕੀ ਰਿਪੋਰਟ: ਤੁਹਾਡੇ ਫੋਨ 'ਤੇ ਸਥਾਨਕ ਤੌਰ 'ਤੇ ਇੱਕ ਬਹੁਤ ਸਮਰਥ ਭਾਸ਼ਾ ਮਾਡਲ](https://arxiv.org/abs/2404.14219)  
  - [Phi-4 ਤਕਨੀਕੀ ਰਿਪੋਰਟ](https://arxiv.org/abs/2412.08905)  
  - [Phi-4-Mini ਤਕਨੀਕੀ ਰਿਪੋਰਟ: Mixture-of-LoRAs ਦੁਆਰਾ ਸੰਕੁਚਿਤ ਪਰ ਸਮਰਥ ਮਲਟੀਮੋਡਲ ਭਾਸ਼ਾ ਮਾਡਲ](https://arxiv.org/abs/2503.01743)  
  - [In-Vehicle Function-Calling ਲਈ ਛੋਟੇ ਭਾਸ਼ਾ ਮਾਡਲਾਂ ਨੂੰ ਅਨੁਕੂਲਿਤ ਕਰਨਾ](https://arxiv.org/abs/2501.02342)  
  - [(WhyPHI) Multiple-Choice Question Answering ਲਈ PHI-3 ਨੂੰ ਫਾਈਨ-ਟਿਊਨ ਕਰਨਾ: ਵਿਧੀ, ਨਤੀਜੇ, ਅਤੇ ਚੁਣੌਤੀਆਂ](https://arxiv.org/abs/2501.01588)  
- [Phi-4-reasoning ਤਕਨੀਕੀ ਰਿਪੋਰਟ](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)  
- [Phi-4-mini-reasoning ਤਕਨੀਕੀ ਰਿਪੋਰਟ](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)  

## Phi ਮਾਡਲਾਂ ਦੀ ਵਰਤੋਂ  

### Azure AI Foundry 'ਤੇ Phi  

ਤੁਹਾਨੂੰ Microsoft Phi ਦੀ ਵਰਤੋਂ ਕਰਨ ਅਤੇ ਆਪਣੇ ਵੱਖ-ਵੱਖ ਹਾਰਡਵੇਅਰ ਡਿਵਾਈਸਾਂ ਵਿੱਚ E2E ਹੱਲ ਬਣਾਉਣ ਬਾਰੇ ਸਿੱਖਣ ਦਾ ਮੌਕਾ ਮਿਲੇਗਾ। ਆਪਣੇ ਲਈ Phi ਦਾ ਅਨੁਭਵ ਕਰਨ ਲਈ, ਮਾਡਲਾਂ ਨਾਲ ਖੇਡਣਾ ਸ਼ੁਰੂ ਕਰੋ ਅਤੇ ਆਪਣੇ ਸਥਿਤੀਆਂ ਲਈ Phi ਨੂੰ ਕਸਟਮਾਈਜ਼ ਕਰੋ। [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai) 'ਤੇ ਜਾ ਕੇ ਹੋਰ ਜਾਣਕਾਰੀ ਪ੍ਰਾਪਤ ਕਰੋ। [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md) ਨਾਲ ਸ਼ੁਰੂਆਤ ਕਰਨ ਬਾਰੇ ਸਿੱਖਣ ਲਈ।  

**ਪਲੇਗਰਾਊਂਡ**  
ਹਰ ਮਾਡਲ ਲਈ ਇੱਕ ਸਮਰਪਿਤ ਪਲੇਗਰਾਊਂਡ ਹੈ ਜਿਸ ਵਿੱਚ ਮਾਡਲ ਦੀ ਜਾਂਚ ਕੀਤੀ ਜਾ ਸਕਦੀ ਹੈ। [Azure AI Playground](https://aka.ms/try-phi3)।  

### GitHub ਮਾਡਲਾਂ 'ਤੇ Phi  

ਤੁਹਾਨੂੰ Microsoft Phi ਦੀ ਵਰਤੋਂ ਕਰਨ ਅਤੇ ਆਪਣੇ ਵੱਖ-ਵੱਖ ਹਾਰਡਵੇਅਰ ਡਿਵਾਈਸਾਂ ਵਿੱਚ E2E ਹੱਲ ਬਣਾਉਣ ਬਾਰੇ ਸਿੱਖਣ ਦਾ ਮੌਕਾ ਮਿਲੇਗਾ। ਆਪਣੇ ਲਈ Phi ਦਾ ਅਨੁਭਵ ਕਰਨ ਲਈ, ਮਾਡਲ ਨਾਲ ਖੇਡਣਾ ਸ਼ੁਰੂ ਕਰੋ ਅਤੇ ਆਪਣੇ ਸਥਿਤੀਆਂ ਲਈ Phi ਨੂੰ ਕਸਟਮਾਈਜ਼ ਕਰੋ। [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) 'ਤੇ ਜਾ ਕੇ ਹੋਰ ਜਾਣਕਾਰੀ ਪ੍ਰਾਪਤ ਕਰੋ। [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md) ਨਾਲ ਸ਼ੁਰੂਆਤ ਕਰਨ ਬਾਰੇ ਸਿੱਖਣ ਲਈ।  

**ਪਲੇਗਰਾਊਂਡ**  
ਹਰ ਮਾਡਲ ਲਈ ਇੱਕ [ਪਲੇਗਰਾਊਂਡ](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) ਹੈ ਜਿਸ ਵਿੱਚ ਮਾਡਲ ਦੀ ਜਾਂਚ ਕੀਤੀ ਜਾ ਸਕਦੀ ਹੈ।  

### Hugging Face 'ਤੇ Phi  

ਤੁਸੀਂ ਮਾਡਲ ਨੂੰ [Hugging Face](https://huggingface.co/microsoft) 'ਤੇ ਵੀ ਲੱਭ ਸਕਦੇ ਹੋ।  

**ਪਲੇਗਰਾਊਂਡ**  
[Hugging Chat ਪਲੇਗਰਾਊਂਡ](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)  

## ਜ਼ਿੰਮੇਵਾਰ AI  

Microsoft ਆਪਣੇ ਗਾਹਕਾਂ ਨੂੰ ਜ਼ਿੰਮੇਵਾਰੀ ਨਾਲ AI ਉਤਪਾਦਾਂ ਦੀ ਵਰਤੋਂ ਕਰਨ ਵਿੱਚ ਮਦਦ ਕਰਨ, ਸਾਡੇ ਅਨੁਭਵ ਸਾਂਝੇ ਕਰਨ ਅਤੇ ਭਰੋਸੇ-ਅਧਾਰਿਤ ਸਾਂਝੇਦਾਰੀਆਂ ਬਣਾਉਣ ਲਈ ਵਚਨਬੱਧ ਹੈ। Transparency Notes ਅਤੇ Impact Assessments ਵਰਗੇ ਟੂਲਾਂ ਰਾਹੀਂ ਇਹ ਸਹਾਇਤਾ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਹ ਸਾਧਨ [https://aka.ms/RAI](https://aka.ms/RAI) 'ਤੇ ਮਿਲ ਸਕਦੇ ਹਨ।  
Microsoft ਦਾ ਜ਼ਿੰਮੇਵਾਰ AI ਲਈ ਦ੍ਰਿਸ਼ਕੋਣ ਸਾਡੇ AI ਸਿਧਾਂਤਾਂ 'ਤੇ ਅਧਾਰਿਤ ਹੈ: ਨਿਰਪੱਖਤਾ, ਭਰੋਸੇਯੋਗਤਾ ਅਤੇ ਸੁਰੱਖਿਆ, ਗੋਪਨੀਯਤਾ ਅਤੇ ਸੁਰੱਖਿਆ, ਸ਼ਾਮਿਲਤਾ, ਪਾਰਦਰਸ਼ਤਾ, ਅਤੇ ਜਵਾਬਦੇਹੀ।  

ਵੱਡੇ ਪੱਧਰ ਦੇ ਕੁਦਰਤੀ ਭਾਸ਼ਾ, ਚਿੱਤਰ, ਅਤੇ ਬੋਲ ਮਾਡਲ - ਜਿਵੇਂ ਕਿ ਇਸ ਨਮੂਨੇ ਵਿੱਚ ਵਰਤੇ ਗਏ ਹਨ - ਅਨੁਚਿਤ, ਅਵਿਸ਼ਵਾਸ਼ਯੋਗ ਜਾਂ ਅਪਮਾਨਜਨਕ ਤਰੀਕੇ ਨਾਲ ਵਿਵਹਾਰ ਕਰ ਸਕਦੇ ਹਨ, ਜਿਸ ਨਾਲ ਨੁਕਸਾਨ ਹੋ ਸਕਦਾ ਹੈ। ਕਿਰਪਾ ਕਰਕੇ [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) ਨੂੰ ਪੜ੍ਹੋ ਤਾਂ ਜੋ ਖਤਰੇ ਅਤੇ ਸੀਮਾਵਾਂ ਬਾਰੇ ਜਾਣਕਾਰੀ ਪ੍ਰਾਪਤ ਕੀਤੀ ਜਾ ਸਕੇ।  

ਇਹ ਖਤਰੇ ਘਟਾਉਣ ਲਈ ਸਿਫਾਰਸ਼ੀ ਤਰੀਕਾ ਇਹ ਹੈ ਕਿ ਆਪਣੇ ਆਰਕੀਟੈਕਚਰ ਵਿੱਚ ਇੱਕ ਸੁਰੱਖਿਆ ਪ੍ਰਣਾਲੀ ਸ਼ਾਮਿਲ ਕਰੋ ਜੋ ਹਾਨਿਕਾਰਕ ਵਿਵਹਾਰ ਦੀ ਪਛਾਣ ਅਤੇ ਰੋਕਥਾਮ ਕਰ ਸਕੇ। [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) ਇੱਕ ਸਵਤੰਤਰ ਸੁਰੱਖਿਆ ਪਰਤ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ, ਜੋ ਐਪਲੀਕੇਸ਼ਨ ਅਤੇ ਸੇਵਾਵਾਂ ਵਿੱਚ ਉਪਭੋਗਤਾ-ਜਨਰੇਟ ਕੀਤੇ ਅਤੇ AI-ਜਨਰੇਟ ਕੀਤੇ ਸਮੱਗਰੀ ਦੀ ਪਛਾਣ ਕਰਨ ਦੇ ਯੋਗ ਹੈ। Azure AI Content Safety ਵਿੱਚ ਟੈਕਸਟ ਅਤੇ ਚਿੱਤਰ APIs ਸ਼ਾਮਿਲ ਹਨ ਜੋ ਹਾਨਿਕਾਰਕ ਸਮੱਗਰੀ ਦੀ ਪਛਾਣ ਕਰਨ ਦੀ ਆਗਿਆ ਦਿੰਦੇ ਹਨ। Azure AI Foundry ਵਿੱਚ, Content Safety ਸੇਵਾ ਤੁਹਾਨੂੰ ਵੱਖ-ਵੱਖ ਮੋਡੈਲਿਟੀਜ਼ 'ਤੇ ਹਾਨਿਕਾਰਕ ਸਮੱਗਰੀ ਦੀ ਪਛਾਣ ਕਰਨ ਲਈ ਨਮੂਨਾ ਕੋਡ ਦੇਖਣ, ਖੋਜਣ ਅਤੇ ਅਜ਼ਮਾਉਣ ਦੀ ਆਗਿਆ ਦਿੰਦੀ ਹੈ। ਹੇਠਾਂ ਦਿੱਤੀ [quickstart documentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) ਸੇਵਾ ਨੂੰ ਅਨੁਰੋਧ ਕਰਨ ਦੇ ਰਾਹਦਰਸ਼ਨ ਦਿੰਦੀ ਹੈ।  

ਇੱਕ ਹੋਰ ਪੱਖ ਜਿਸ ਨੂੰ ਧਿਆਨ ਵਿੱਚ ਰੱਖਣ ਦੀ ਲੋੜ ਹੈ, ਉਹ ਹੈ ਸਮੁੱਚੇ ਐਪਲੀਕੇਸ਼ਨ ਦੀ ਕਾਰਗੁਜ਼ਾਰੀ। ਬਹੁ-ਮੋਡਲ ਅਤੇ ਬਹੁ-ਮਾਡਲ ਐਪਲੀਕੇਸ਼ਨਾਂ ਨਾਲ, ਅਸੀਂ ਕਾਰਗੁਜ਼ਾਰੀ ਨੂੰ ਇਸ ਤਰੀਕੇ ਨਾਲ ਪਰਿਭਾਸ਼ਿਤ ਕਰਦੇ ਹਾਂ ਕਿ ਸਿਸਟਮ ਤੁਹਾਡੇ ਅਤੇ ਤੁਹਾਡੇ ਉਪਭੋਗਤਾਵਾਂ ਦੀ ਉਮੀਦਾਂ ਅਨੁਸਾਰ ਕੰਮ ਕਰਦਾ ਹੈ, ਜਿਸ ਵਿੱਚ ਹਾਨਿਕਾਰਕ ਨਤੀਜੇ ਪੈਦਾ ਨਾ ਕਰਨਾ ਸ਼ਾਮਿਲ ਹੈ। ਇਹ ਮਹੱਤਵਪੂਰਨ ਹੈ ਕਿ [Performance and Quality and Risk and Safety evaluators](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਆਪਣੇ ਸਮੁੱਚੇ ਐਪਲੀਕੇਸ਼ਨ ਦੀ ਕਾਰਗੁਜ਼ਾਰੀ ਦਾ ਮੁਲਾਂਕਨ ਕੀਤਾ ਜਾਵੇ। ਤੁਹਾਡੇ ਕੋਲ [custom evaluators](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators) ਬਣਾਉਣ ਅਤੇ ਮੁਲਾਂਕਨ ਕਰਨ ਦੀ ਯੋਗਤਾ ਵੀ ਹੈ।  

ਤੁਸੀਂ ਆਪਣੇ ਵਿਕਾਸ ਵਾਤਾਵਰਣ ਵਿੱਚ [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਆਪਣੀ AI ਐਪਲੀਕੇਸ਼ਨ ਦਾ ਮੁਲਾਂਕਨ ਕਰ ਸਕਦੇ ਹੋ। ਜਾਂਚ ਡਾਟਾਸੈਟ ਜਾਂ ਟਾਰਗਟ ਦੇ ਅਧਾਰ 'ਤੇ, ਤੁਹਾਡੇ ਜਨਰੇਟਿਵ AI ਐਪਲੀਕੇਸ਼ਨ ਦੇ ਨਤੀਜੇ ਬਣਾਏ ਗਏ ਮੁਲਾਂਕਨਕਰਤਾਵਾਂ ਜਾਂ ਤੁਹਾਡੇ ਚੋਣ ਦੇ ਕਸਟਮ ਮੁਲਾਂਕਨਕਰਤਾਵਾਂ ਨਾਲ ਮਾਤਰਾਤਮਕ ਤੌਰ 'ਤੇ ਮਾਪੇ ਜਾਂਦੇ ਹਨ। [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) ਦੀ ਪਾਲਣਾ ਕਰਕੇ ਆਪਣੇ ਸਿਸਟਮ ਦਾ ਮੁਲਾਂਕਨ ਕਰਨ ਲਈ Azure AI Evaluation SDK ਨਾਲ ਸ਼ੁਰੂਆਤ ਕਰੋ। ਜਦੋਂ ਤੁਸੀਂ ਇੱਕ ਮੁਲਾਂਕਨ ਚਲਾਉਣ ਦੀ ਪ੍ਰਕਿਰਿਆ ਨੂੰ ਅੰਜਾਮ ਦਿੰਦੇ ਹੋ, ਤਾਂ ਤੁਸੀਂ [Azure AI Foundry ਵਿੱਚ ਨਤੀਜਿਆਂ ਨੂੰ ਵਿਜ਼ੁਅਲਾਈਜ਼ ਕਰ ਸਕਦੇ ਹੋ](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results)।  

## ਟ੍ਰੇਡਮਾਰਕਸ  

ਇਹ ਪ੍ਰੋਜੈਕਟ ਪ੍ਰੋਜੈਕਟਾਂ, ਉਤਪਾਦਾਂ ਜਾਂ ਸੇਵਾਵਾਂ ਲਈ ਟ੍ਰੇਡਮਾਰਕਸ ਜਾਂ ਲੋਗੋ ਸ਼ਾਮਿਲ ਕਰ ਸਕਦਾ ਹੈ। Microsoft ਟ੍ਰੇਡਮਾਰਕਸ ਜਾਂ ਲੋਗੋ ਦੀ ਅਧਿਕ੍ਰਿਤ ਵਰਤੋਂ [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) ਦੀ ਪਾਲਣਾ ਕਰਨੀ ਚਾਹੀਦੀ ਹੈ।  
ਇਸ ਪ੍ਰੋਜੈਕਟ ਦੇ ਸੰਸ਼ੋਧਿਤ ਸੰਸਕਰਣਾਂ ਵਿੱਚ Microsoft ਟ੍ਰੇਡਮਾਰਕਸ ਜਾਂ ਲੋਗੋ ਦੀ ਵਰਤੋਂ ਗੁੰਝਲਦਾਰ ਨਹੀਂ ਹੋਣੀ ਚਾਹੀਦੀ ਅਤੇ ਨਾ ਹੀ Microsoft ਦੇ ਪ੍ਰਾਯੋਜਨ ਦਾ ਸੰਕੇਤ ਦੇਣਾ ਚਾਹੀਦਾ ਹੈ। ਕਿਸੇ ਵੀ ਤੀਜੀ ਪੱਖੀ ਟ੍ਰੇਡਮਾਰਕਸ ਜਾਂ ਲੋਗੋ ਦੀ ਵਰਤੋਂ ਉਹਨਾਂ ਤੀਜੀ ਪੱਖੀ ਦੀਆਂ ਨੀਤੀਆਂ ਦੇ ਅਧੀਨ ਹੈ।  

---

**ਅਸਵੀਕਰਤੀ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀ ਹੋਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁਚੱਜੇਪਣ ਹੋ ਸਕਦੇ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼, ਜੋ ਇਸਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਹੈ, ਨੂੰ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੇ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।