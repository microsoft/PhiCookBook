<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c2e4b490f4bd424b095f21e38c6af33b",
  "translation_date": "2026-01-05T13:54:49+00:00",
  "source_file": "README.md",
  "language_code": "pa"
}
-->
# ਫਾਈ ਕੂਕਬੁੱਕ: Microsoft ਦੇ ਫਾਈ ਮਾਡਲਾਂ ਨਾਲ ਹੈਂਡਸ-ਆਨ ਉਦਾਹਰਣਾਂ

[![GitHub ਕੋਡਸਪੇਸ ਵਿੱਚ ਨਮੂਨਿਆਂ ਨੂੰ ਖੋਲ੍ਹੋ ਅਤੇ ਵਰਤੋ](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)  
[![ਡੀਵ ਕন্টੇਨਰਜ਼ ਵਿੱਚ ਖੋਲ੍ਹੋ](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub ਯੋਗਦਾਨਕਰਤਾ](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)  
[![GitHub ਇਸ਼ੂਜ਼](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)  
[![GitHub ਪੁੱਲ-ਬੇਨਤੀਆਂ](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)  
[![ਪੁੱਲ-ਬੇਨਤੀਆਂ ਸਵਾਗਤ ਹੈ](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub ਦੇਖਣ ਵਾਲੇ](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)  
[![GitHub ਫੋਰਕ](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)  
[![GitHub ਸਿਤਾਰੇ](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

ਫਾਈ Microsoft ਵੱਲੋਂ ਵਿਕਸਤ ਕੀਤਾ ਗਿਆ ਖੁੱਲਾ ਸਰੋਤ AI ਮਾਡਲਾਂ ਦੀ ਇੱਕ ਸੀਰੀਜ਼ ਹੈ।

ਫਾਈ ਇਸ ਵੇਲੇ ਸਭ ਤੋਂ ਸ਼ਕਤੀਸ਼ালী ਅਤੇ ਲਾਗਤ-ਪ੍ਰਭਾਵੀ ਛੋਟਾ ਭਾਸ਼ਾਈ ਮਾਡਲ (SLM) ਹੈ, ਜਿਸਦਾ ਮਲਟੀ-ਭਾਸ਼ਾ, ਤਰਕ, ਟੈਕਸਟ/ਚੈਟ ਪੈਦਾਵਾਰ, ਕੋਡਿੰਗ, ਚਿੱਤਰਾਂ, ਆਡੀਓ ਅਤੇ ਹੋਰ ਸਥਿਤੀਆਂ ਵਿੱਚ ਬਹੁਤ ਵਧੀਆ ਬੈਂਚਮਾਰਕ ਹਨ।

ਤੁਸੀਂ ਫਾਈ ਨੂੰ ਕਲਾਉਡ ਜਾਂ ਐਡਜ ਡਿਵਾਈਸز ਵਿੱਚ ਤਾਇਨਾਤ ਕਰ ਸਕਦੇ ਹੋ, ਅਤੇ ਤੁਸੀਂ ਸੀਮਿਤ ਗਣਨਾਤਮਕ ਸ਼ਕਤੀ ਨਾਲ ਆਸਾਨੀ ਨਾਲ ਜਨਰੇਟਿਵ AI ਐਪਲਿਕੇਸ਼ਨਾਂ ਬਣਾ ਸਕਦੇ ਹੋ।

ਇਨ੍ਹਾਂ ਸਰੋਤਾਂ ਨੂੰ ਵਰਤਣਾ ਸ਼ੁਰੂ ਕਰਨ ਲਈ ਇਹ ਗਾਈਡ ਲਵੋ :  
1. **ਰਿਪੋਜ਼ਟਰੀ ਨੂੰ ਫੋਰਕ ਕਰੋ**: ਕਲਿੱਕ ਕਰੋ [![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)  
2. **ਰਿਪੋਜ਼ਟਰੀ ਨੂੰ ਕਲੋਨ ਕਰੋ**: `git clone https://github.com/microsoft/PhiCookBook.git`  
3. [**Microsoft AI Discord ਕਮਿਊਨਿਟੀ ਵਿੱਚ ਸ਼ਾਮਲ ਹੋਵੋ ਅਤੇ ਵਿਸ਼ੇਸ਼ਜ্ঞান ਅਤੇ ਹੋਰ ਵਿਕਾਸਕਾਰਾਂ ਨੂੰ ਮਿਲੋ**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/pa/cover.eb18d1b9605d754b.png)

### 🌐 ਬਹੁਭਾਸ਼ਾਈ ਸਮਰਥਨ

#### GitHub ਐਕਸ਼ਨ ਰਾਹੀਂ ਸਮਰਥਿਤ (ਸੁਤੰਤਰਤ ਅਤੇ ਹਮੇਸ਼ਾ ਅੱਪ ਟੂ ਡੇਟ)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../br/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](./README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **ਮੁੱਠੀ ਤੌਰ 'ਤੇ ਕਲੋਨ ਕਰਨਾ ਚਾਹੁੰਦੇ ਹੋ?**

> ਇਹ ਰਿਪੋਜ਼ਟਰੀ 50+ ਭਾਸ਼ਾ ਅਨੁਵਾਦ ਸ਼ਾਮਲ ਕਰਦੀ ਹੈ ਜੋ ਡਾਊਨਲੋਡ ਆਕਾਰ ਨੂੰ ਕਾਫੀ ਵਧਾ ਦਿੰਦੀ ਹੈ। ਅਨੁਵਾਦ ਬਿਨਾਂ ਕਲੋਨ ਕਰਨ ਲਈ sparse checkout ਵਰਤੋਂ ਕਰੋ:  
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/PhiCookBook.git
> cd PhiCookBook
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> ਇਸ ਨਾਲ ਤੁਹਾਨੂੰ ਕੋਰਸ ਪੂਰਾ ਕਰਨ ਲਈ ਸਾਰਾ ਸਮੱਗਰੀ ਬਹੁਤ ਤੇਜ਼ ਡਾਊਨਲੋਡ ਦੇ ਨਾਲ ਮਿਲ ਜਾਵੇਗਾ।  
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## ਮਾਦਾ ਸੂਚੀ

- ਪਰੇਚਾਰ  
  - [ਫਾਈ ਪਰਿਵਾਰ ਵਿੱਚ ਤੁਹਾਡਾ ਸੁਆਗਤ ਹੈ](./md/01.Introduction/01/01.PhiFamily.md)  
  - [ਆਪਣੇ ਵਾਤਾਵਰਨ ਦੀ ਸੈਟਅਪਿੰਗ](./md/01.Introduction/01/01.EnvironmentSetup.md)  
  - [ਮੁੱਖ ਤਕਨੀਕਾਂ ਦੀ ਸਮਝ](./md/01.Introduction/01/01.Understandingtech.md)  
  - [ਫਾਈ ਮਾਡਲਾਂ ਲਈ AI ਸੁਰੱਖਿਆ](./md/01.Introduction/01/01.AISafety.md)  
  - [ਫਾਈ ਹਾਰਡਵੇਅਰ ਸਮਰਥਨ](./md/01.Introduction/01/01.Hardwaresupport.md)  
  - [ਫਾਈ ਮਾਡਲ ਅਤੇ ਪਲੇਟਫਾਰਮਾਂ ਉੱਤੇ ਉਪਲਬਧਤਾ](./md/01.Introduction/01/01.Edgeandcloud.md)  
  - [Guidance-ai ਅਤੇ ਫਾਈ ਦੀ ਵਰਤੋਂ](./md/01.Introduction/01/01.Guidance.md)  
  - [GitHub ਮਾਰਕੀਟਪਲੇਸ ਮਾਡਲ](https://github.com/marketplace/models)  
  - [Azure AI ਮਾਡਲ ਕੈਟਲੌਗ](https://ai.azure.com)  

- ਵੱਖ-ਵੱਖ ਵਾਤਾਵਰਨ ਵਿੱਚ ਫਾਈ ਦਾ ਨਿਰਣੇ  
    - [Hugging face](./md/01.Introduction/02/01.HF.md)  
    - [GitHub ਮਾਡਲ](./md/01.Introduction/02/02.GitHubModel.md)  
    - [Azure AI Foundry Model Catalog](./md/01.Introduction/02/03.AzureAIFoundry.md)  
    - [Ollama](./md/01.Introduction/02/04.Ollama.md)  
    - [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)  
    - [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)  
    - [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md)  

- ਫਾਈ ਪਰਿਵਾਰ ਦਾ ਨਿਰਣੇ  
    - [iOS ਵਿੱਚ ਫਾਈ ਦਾ ਨਿਰਣੇ](./md/01.Introduction/03/iOS_Inference.md)  
    - [Android ਵਿੱਚ ਫਾਈ ਦਾ ਨਿਰਣੇ](./md/01.Introduction/03/Android_Inference.md)  
    - [Jetson ਵਿੱਚ ਫਾਈ ਦਾ ਨਿਰਣੇ](./md/01.Introduction/03/Jetson_Inference.md)  
    - [AI PC ਵਿੱਚ ਫਾਈ ਦਾ ਨਿਰਣੇ](./md/01.Introduction/03/AIPC_Inference.md)  
    - [Apple MLX ਫ੍ਰੇਮਵਰਕ ਨਾਲ ਫਾਈ ਦਾ ਨਿਰਣੇ](./md/01.Introduction/03/MLX_Inference.md)  
    - [ਲੋਕਲ ਸਰਵਰ ਵਿੱਚ ਫਾਈ ਦਾ ਨਿਰਣੇ](./md/01.Introduction/03/Local_Server_Inference.md)  
    - [AI Toolkit ਵਰਤੋਂ ਕਰਕੇ ਰਿਮੋਟ ਸਰਵਰ ਵਿੱਚ ਫਾਈ ਦਾ ਨਿਰਣੇ](./md/01.Introduction/03/Remote_Interence.md)  
    - [Rust ਨਾਲ ਫਾਈ ਦਾ ਨਿਰਣੇ](./md/01.Introduction/03/Rust_Inference.md)  
    - [ਲੋਕਲ ਵਿੱਚ ਫਾਈ-ਦ੍ਰਿਸ਼ਟੀ ਦਾ ਨਿਰਣੇ](./md/01.Introduction/03/Vision_Inference.md)  
    - [Kaito AKS, Azure Containers (ਸਰਕਾਰੀ ਸਮਰਥਨ) ਨਾਲ ਫਾਈ ਦਾ ਨਿਰਣੇ](./md/01.Introduction/03/Kaito_Inference.md)  
-  [ਫਾਈ ਪਰਿਵਾਰ ਦੀ ਮਾਤਰਾ ਜਾਣਚ](./md/01.Introduction/04/QuantifyingPhi.md)  
    - [llama.cpp ਵਰਤ ਕੇ ਫਾਈ-3.5 / 4 ਦੀ ਮਾਤਰਾ ਜਾਣਚ](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)  
    - [onnxruntime ਲਈ ਜਨਰੇਟਿਵ AI ਵਿਸ਼ਤਾਰ ਵਰਤ ਕੇ ਫਾਈ-3.5 / 4 ਦੀ ਮਾਤਰਾ ਜਾਣਚ](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)  
    - [Intel OpenVINO ਵਰਤ ਕੇ ਫਾਈ-3.5 / 4 ਦੀ ਮਾਤਰਾ ਜਾਣਚ](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)  
    - [Apple MLX ਫ੍ਰੇਮਵਰਕ ਵਰਤ ਕੇ ਫਾਈ-3.5 / 4 ਦੀ ਮਾਤਰਾ ਜਾਣਚ](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)  

- ਫਾਈ ਦਾ ਮੁਲਾਂਕਣ  
    - [ਜਵਾਬਦੇਹ AI](./md/01.Introduction/05/ResponsibleAI.md)  
    - [ਮੁਲਾਂਕਣ ਲਈ Azure AI Foundry](./md/01.Introduction/05/AIFoundry.md)  
    - [ਮੁਲਾਂਕਣ ਲਈ Promptflow ਦੀ ਵਰਤੋਂ](./md/01.Introduction/05/Promptflow.md)  
 
- Azure AI ਖੋਜ ਨਾਲ RAG  
    - [Azure AI ਖੋਜ ਦੇ ਨਾਲ Phi-4-mini ਅਤੇ Phi-4-multimodal(RAG) ਦੀ ਵਰਤੋਂ ਕਿਵੇਂ ਕਰੀਏ](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- ਫਾਈ ਐਪਲੀਕੇਸ਼ਨ ਵਿਕਾਸ ਨਮੂਨੇ  
  - ਟੈਕਸਟ ਅਤੇ ਚੈਟ ਐਪਲੀਕੇਸ਼ਨ  
    - ਫਾਈ-4 ਨਮੂਨੇ 🆕  
      - [📓] [Phi-4-mini ONNX ਮਾਡਲ ਨਾਲ ਚੈਟ ਕਰੋ](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)  
      - [Phi-4 ਲੋਕਲ ONNX ਮਾਡਲ ਨਾਲ ਚੈਟ .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)  
      - [ਸਮੈਂਟਿਕ ਕਰਨਲ ਵਰਤ ਕੇ Phi-4 ONNX ਨਾਲ .NET ਕੁਨਸੋਲ ਐਪ ਵਿੱਚ ਚੈਟ](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)  
    - Phi-3 / 3.5 ਨਮੂਨੇ  
      - [Phi3, ONNX Runtime Web ਅਤੇ WebGPU ਵਰਤ ਕੇ ਬ੍ਰਾਊਜ਼ਰ ਵਿੱਚ ਲੋਕਲ ਚੈਟਬੋਟ](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)  
      - [OpenVino ਚੈਟ](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)  
      - [ਮਲਟੀ ਮਾਡਲ - ਇੰਟਰਐਕਟਿਵ ਫਾਈ-3-ਮੀਨੀ ਅਤੇ ਓਪਨਏਆਈ ਵਿਸਪਰ](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [ਐਮਐਲਫਲੋ - ਇੱਕ ਰੈਪਰ ਬਣਾਉਣਾ ਅਤੇ Phi-3 ਨਾਲ ਐਮਐਲਫਲੋ ਦੀ ਵਰਤੋਂ](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [ਮਾਡਲ ਓਪਟੀਮਾਈਜੇਸ਼ਨ - ਕਿਸ ਤਰ੍ਹਾਂ Phi-3-ਮਿਨੀ ਮਾਡਲ ਨੂੰ ONNX ਰਨਟਾਈਮ ਵੈੱਬ ਲਈ ਓਪਟੀਮਾਈਜ਼ ਕਰਨਾ Olive ਨਾਲ](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [WinUI3 ਐਪ Phi-3 ਮਿਨੀ-4k-ਇੰਸਟਰੱਕ-onnx ਨਾਲ](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      -[WinUI3 ਮਲਟੀ ਮਾਡਲ ਏਆਈ ਚਲਿਤ ਨੋਟਸ ਐਪ ਸੈਂਪਲ](https://github.com/microsoft/ai-powered-notes-winui3-sample)
      - [ਕਸਟਮ Phi-3 ਮਾਡਲਾਂ ਨੂੰ ਫਾਈਨ-ਟਿਊਨ ਅਤੇ ਪ੍ਰਾਮਪਟ ਫਲੋ ਨਾਲ ਇੰਟੀਗ੍ਰੇਟ ਕਰੋ](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
      - [ਇਜ਼ਰ ਏਆਈ ਫਾਊਂਡਰੀ ਵਿੱਚ ਕਸਟਮ Phi-3 ਮਾਡਲਾਂ ਨੂੰ ਪ੍ਰਾਮਪਟ ਫਲੋ ਨਾਲ ਫਾਈਨ-ਟਿਊਨ ਅਤੇ ਇੰਟੀਗ੍ਰੇਟ ਕਰੋ](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
      - [ਮਾਈਕਰੋਸੌਫਟ ਦੇ ਜ਼ਿੰਮੇਵਾਰ ਏਆਈ ਨੀਤੀਆਂ ਤੇ ਧਿਆਨ ਕੇਂਦਰਿਤ ਕਰਦਿਆਂ Azure AI Foundry ਵਿੱਚ ਫਾਈਨ-ਟਿਊਨ ਕੀਤਾ ਗਿਆ Phi-3 / Phi-3.5 ਮਾਡਲ ਦਾ ਮੁਲਾਂਕਣ ਕਰੋ](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
      - [📓] [Phi-3.5-ਮੀਨੀ-ਇੰਸਟਰੱਕ ਭਾਸ਼ਾ ਭਵਿੱਖਬਾਣੀ ਸੈਂਪਲ (ਚੀਨੀ/ਅੰਗਰੇਜ਼ੀ)](./md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
      - [Phi-3.5-ਇੰਸਟਰੱਕ WebGPU RAG ਚੈਟਬੋਟ](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
      - [Windows GPU ਦੀ ਵਰਤੋਂ ਕਰਕੇ Phi-3.5-ਇੰਸਟਰੱਕ ONNX ਨਾਲ ਪ੍ਰਾਮਪਟ ਫਲੋ ਹੱਲ ਬਣਾਉਣ ਲਈ](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
      - [ਮਾਈਕਰੋਸੌਫਟ Phi-3.5 tflite ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਐਂਡਰਾਇਡ ਐਪ ਬਣਾਉਣਾ](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
      - [ਸਰਵਜਨਕ ONNX Phi-3 ਮਾਡਲ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਸਵਾਲ-ਜਵਾਬ .NET ਉਦਾਹਰਨ Microsoft.ML.OnnxRuntime ਨਾਲ](../../md/04.HOL/dotnet/src/LabsPhi301)
      - [ਸੈਮੈਂਟਿਕ ਕਰਨਲ ਅਤੇ Phi-3 ਨਾਲ ਕੰਸੋਲ ਚੈਟ .NET ਐਪ](../../md/04.HOL/dotnet/src/LabsPhi302)

  - ਐਜ਼ਿਊਰ ਏਆਈ ਇਨਫਿਰੈਂਸ SDK ਕੋਡ ਆਧਾਰਿਤ ਸੈਂਪਲ 
    - Phi-4 ਸੈਂਪਲ 🆕
      - [📓] [Phi-4-ਮਲਟੀਮੋਡਲ ਦੀ ਵਰਤੋਂ ਕਰ ਕੇ ਪ੍ਰੋਜੈਕਟ ਕੋਡ ਜਨਰੇਟ ਕਰੋ](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
    - Phi-3 / 3.5 ਸੈਂਪਲ
      - [ਮਾਈਕਰੋਸੌਫਟ Phi-3 ਪਰਿਵਾਰ ਨਾਲ ਆਪਣਾ ਵਿਜ਼ੂਅਲ ਸਟੂਡਿਓ ਕੋਡ GitHub ਕੋਪਾਇਲਟ ਚੈਟ ਬਣਾਓ](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
      - [GitHub ਮਾਡਲਾਂ ਨਾਲ Phi-3.5 ਦੁਆਰਾ ਆਪਣਾ ਵਿਜ਼ੂਅਲ ਸਟੂਡਿਓ ਕੋਡ ਚੈਟ ਕੋਪਾਇਲਟ ਏਜੰਟ ਬਣਾਓ](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

  - ਉੱਚ ਪੱਧਰ ਦੇ ਤਰਕਸ਼ੀਲ ਸੈਂਪਲ
    - Phi-4 ਸੈਂਪਲ 🆕
      - [📓] [Phi-4-ਮੀਨੀ-ਤਰਕਸ਼ੀਲ ਜਾਂ Phi-4-ਤਰਕਸ਼ੀਲ ਸੈਂਪਲ](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
      - [📓] [ਮਾਈਕਰੋਸੌਫਟ Olive ਨਾਲ Phi-4-ਮੀਨੀ-ਤਰਕਸ਼ੀਲ ਦੀ ਫਾਈਨ-ਟਿਊਨਿੰਗ](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [ਐਪਲ MLX ਨਾਲ Phi-4-ਮੀਨੀ-ਤਰਕਸ਼ੀਲ ਦੀ ਫਾਈਨ-ਟਿਊਨਿੰਗ](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [GitHub ਮਾਡਲਾਂ ਨਾਲ Phi-4-ਮੀਨੀ-ਤਰਕਸ਼ੀਲ](./md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
      - [📓] [Azure AI Foundry ਮਾਡਲਾਂ ਨਾਲ Phi-4-ਮੀਨੀ-ਤਰਕਸ਼ੀਲ](./md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
  - ਡੈਮੋਜ਼
      - [Phi-4-ਮੀਨੀ ਡੈਮੋਜ਼ Hugging Face Spaces 'ਤੇ ਮੇਜ਼ਬਾਨੀ ਕੀਤੇ ਗਏ](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
      - [Phi-4-ਮਲਟੀਮੋਡਲ ਡੈਮੋਜ਼ Hugging Face Spaces 'ਤੇ ਮੇਜ਼ਬਾਨੀ ਕੀਤੇ ਗਏ](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
  - ਵਿਜ਼ਨ ਸੈਂਪਲ
    - Phi-4 ਸੈਂਪਲ 🆕
      - [📓] [ਚਿੱਤਰਾਂ ਨੂੰ ਪੜ੍ਹਨ ਅਤੇ ਕੋਡ ਬਣਾਉਣ ਲਈ Phi-4-ਮਲਟੀਮੋਡਲ ਦੀ ਵਰਤੋਂ ਕਰੋ](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
    - Phi-3 / 3.5 ਸੈਂਪਲ
      -  [📓][Phi-3-ਵਿਜ਼ਨ-ਚਿੱਤਰ ਲੇਖ ਤੋਂ ਲੇਖ](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [Phi-3-ਵਿਜ਼ਨ-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
      - [📓][Phi-3-ਵਿਜ਼ਨ CLIP ਇੰਬੈਡਿੰਗ](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [ਡੈਮੋ: Phi-3 ਰੀਸਾਈਕਲਿੰਗ](https://github.com/jennifermarsman/PhiRecycling/)
      - [Phi-3-ਵਿਜ਼ਨ - ਵਿਜ਼ੂਅਲ ਭਾਸ਼ਾ ਸਹਾਇਕ - Phi3-Vision ਅਤੇ OpenVINO ਨਾਲ](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
      - [Phi-3 ਵਿਜ਼ਨ Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
      - [Phi-3 ਵਿਜ਼ਨ OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
      - [📓][Phi-3.5 ਵਿਜ਼ਨ ਮਲਟੀ-ਫ੍ਰੇਮ ਜਾਂ ਮਲਟੀ-ਚਿੱਤਰ ਸੈਂਪਲ](./md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
      - [Microsoft.ML.OnnxRuntime .NET ਦੀ ਵਰਤੋਂ ਨਾਲ Phi-3 ਵਿਜ਼ਨ ਸਥਾਨਕ ONNX ਮਾਡਲ](../../md/04.HOL/dotnet/src/LabsPhi303)
      - [ਮੈਂੂ ਆਧਾਰਿਤ Phi-3 ਵਿਜ਼ਨ ਸਥਾਨਕ ONNX ਮਾਡਲ Microsoft.ML.OnnxRuntime .NET ਦੀ ਵਰਤੋਂ ਨਾਲ](../../md/04.HOL/dotnet/src/LabsPhi304)

  - ਗਣਿਤ ਸੈਂਪਲ
    -  Phi-4-ਮੀਨੀ-ਫਲੈਸ਼-ਤਰਕਸ਼ੀਲ-ਇੰਸਟਰੱਕ ਸੈਂਪਲ 🆕 [ਗਣਿਤ ਡੈਮੋ Phi-4-ਮੀਨੀ-ਫਲੈਸ਼-ਤਰਕਸ਼ੀਲ-ਇੰਸਟਰੱਕ ਨਾਲ](./md/02.Application/09.Math/MathDemo.ipynb)

  - ਆਡੀਓ ਸੈਂਪਲ
    - Phi-4 ਸੈਂਪਲ 🆕
      - [📓] [Phi-4-ਮਲਟੀਮੋਡਲ ਦੀ ਵਰਤੋਂ ਨਾਲ ਆਡੀਓ ਟ੍ਰਾਂਸਕ੍ਰਿਪਟ ਨਿਕਾਲਣਾ](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
      - [📓] [Phi-4-ਮਲਟੀਮੋਡਲ ਆਡੀਓ ਸੈਂਪਲ](./md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
      - [📓] [Phi-4-ਮਲਟੀਮੋਡਲ ਭਾਸ਼ਣ ਅਨੁਵਾਦ ਸੈਂਪਲ](./md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
      - [.NET ਕੰਸੋਲ ਐਪਲੀਕੇਸ਼ਨ Phi-4-ਮਲਟੀਮੋਡਲ ਆਡੀਓ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਆਡੀਓ ਫਾਇਲ ਦਾ ਵਿਸ਼ਲੇਸ਼ਣ ਅਤੇ ਟ੍ਰਾਂਸਕ੍ਰਿਪਟ ਤਿਆਰ ਕਰਨਾ](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

  - MOE ਸੈਂਪਲ
    - Phi-3 / 3.5 ਸੈਂਪਲ
      - [📓] [Phi-3.5 ਮਿਸ਼ਰਣ ਮਾਹਿਰ ਮਾਡਲ (MoEs) ਸੋਸ਼ਲ ਮੀਡੀਆ ਸੈਂਪਲ](./md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
      - [📓] [NVIDIA NIM Phi-3 MOE, Azure AI Search, ਅਤੇ LlamaIndex ਨਾਲ ਰੀਟਰੀਵਲ-ਆਗਮੈਂਟਿਡ ਜਨਰੇਸ਼ਨ (RAG) ਪਾਈਪਲਾਈਨ ਬਣਾਉਣਾ](./md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)
      - 
  - ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਸੈਂਪਲ
    - Phi-4 ਸੈਂਪਲ 🆕
      -  [📓] [Phi-4-ਮੀਨੀ ਨਾਲ ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਦੀ ਵਰਤੋਂ ਕਰਨਾ](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
      -  [📓] [Phi-4-ਮੀਨੀ ਨਾਲ ਬਹੁ-ਏਜੰਟ ਬਣਾਉਣ ਲਈ ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਦੀ ਵਰਤੋਂ](./md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
      -  [📓] [Ollama ਨਾਲ ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਦੀ ਵਰਤੋਂ](./md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
      -  [📓] [ONNX ਨਾਲ ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਦੀ ਵਰਤੋਂ](./md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)
  - ਮਲਟੀਮੋਡਲ ਮਿਕਸਿੰਗ ਸੈਂਪਲ
    - Phi-4 ਸੈਂਪਲ 🆕
      -  [📓] [ਤਕਨਾਲੋਜੀ ਪੱਤਰਕਾਰ ਦੇ ਤੌਰ ਤੇ Phi-4-ਮਲਟੀਮੋਡਲ ਦੀ ਵਰਤੋਂ](./md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
      - [.NET ਕੰਸੋਲ ਐਪਲੀਕੇਸ਼ਨ Phi-4-ਮਲਟੀਮੋਡਲ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਤਸਵੀਰਾਂ ਦਾ ਵਿਸ਼ਲੇਸ਼ਣ](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Phi ਸੈਂਪਲਾਂ ਦੀ ਫਾਈਨ-ਟਿਊਨਿੰਗ
  - [ਫਾਈਨ-ਟਿਊਨਿੰਗ ਪਰਿਦ੍ਰਿਸ਼](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [ਫਾਈਨ-ਟਿਊਨਿੰਗ ਵਿਰੁੱਧ RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [Phi-3 ਨੂੰ ਉਦਯੋਗ ਵਿਸ਼ੇਸ਼ਜਖ਼ ਬਣਾਉਣ ਲਈ ਫਾਈਨ-ਟਿਊਨਿੰਗ](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [VS ਕੋਡ ਲਈ AI ਟੂਲਕਿਟ ਨਾਲ Phi-3 ਦੀ ਫਾਈਨ-ਟਿਊਨਿੰਗ](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Azure ਮਸ਼ੀਨ ਲਰਨਿੰਗ ਸਰਵਿਸ ਨਾਲ Phi-3 ਦੀ ਫਾਈਨ-ਟਿਊਨਿੰਗ](./md/03.FineTuning/Introduce_AzureML.md)
  - [Lora ਨਾਲ Phi-3 ਦੀ ਫਾਈਨ-ਟਿਊਨਿੰਗ](./md/03.FineTuning/FineTuning_Lora.md)
  - [QLora ਨਾਲ Phi-3 ਦੀ ਫਾਈਨ-ਟਿਊਨਿੰਗ](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Azure AI Foundry ਨਾਲ Phi-3 ਦੀ ਫਾਈਨ-ਟਿਊਨਿੰਗ](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Azure ML CLI/SDK ਨਾਲ Phi-3 ਦੀ ਫਾਈਨ-ਟਿਊਨਿੰਗ](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [ਮਾਈਕਰੋਸੌਫਟ Olive ਨਾਲ ਫਾਈਨ-ਟਿਊਨਿੰਗ](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [ਮਾਈਕਰੋਸੌਫਟ Olive ਹੈਂਡਜ਼-ਆਨ ਲੈਬ ਨਾਲ ਫਾਈਨ-ਟਿਊਨਿੰਗ](./md/03.FineTuning/olive-lab/readme.md)
  - [Weights and Bias ਨਾਲ Phi-3-ਵਿਜ਼ਨ ਦੀ ਫਾਈਨ-ਟਿਊਨਿੰਗ](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [ਐਪਲ MLX ਫ੍ਰੇਮਵਰਕ ਨਾਲ Phi-3 ਦੀ ਫਾਈਨ-ਟਿਊਨਿੰਗ](./md/03.FineTuning/FineTuning_MLX.md)
  - [Phi-3-ਵਿਜ਼ਨ ਦੀ ਫਾਈਨ-ਟਿਊਨਿੰਗ (ਆਧਿਕਾਰਿਕ ਸਹਾਇਤਾ)](./md/03.FineTuning/FineTuning_Vision.md)
  - [Kaito AKS, Azure Containers (ਆਧਿਕਾਰਿਕ ਸਹਾਇਤਾ) ਨਾਲ Phi-3 ਦੀ ਫਾਈਨ-ਟਿਊਨਿੰਗ](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Phi-3 ਅਤੇ 3.5 ਵਿਜ਼ਨ ਦੀ ਫਾਈਨ-ਟਿਊਨਿੰਗ](https://github.com/2U1/Phi3-Vision-Finetune)

- ਹੈਂਡਜ਼ ਆਨ ਲੈਬ
  - [ਕੱਟਿੰਗ-ਏਜ ਮਾਡਲਾਂ ਦੀ ਖੋਜ: LLMs, SLMs, ਸਥਾਨਕ ਵਿਕਾਸ ਅਤੇ ਹੋਰ](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [ਐਨਐਲਪੀ ਦੀ ਸੰਭਾਵਨਾ ਖੋਲ੍ਹਣਾ: ਮਾਈਕਰੋਸੌਫਟ Olive ਨਾਲ ਫਾਈਨ-ਟਿਊਨਿੰਗ](https://github.com/azure/Ignite_FineTuning_workshop)

- ਅਕਾਦਮਿਕ ਖੋਜ ਪੇਪਰ ਅਤੇ ਪ੍ਰਕਾਸ਼ਨ
  - [Textbooks Are All You Need II: phi-1.5 technical report](https://arxiv.org/abs/2309.05463)
  - [Phi-3 Technical Report: A Highly Capable Language Model Locally on Your Phone](https://arxiv.org/abs/2404.14219)
  - [Phi-4 Technical Report](https://arxiv.org/abs/2412.08905)
  - [Phi-4-Mini Technical Report: Compact yet Powerful Multimodal Language Models via Mixture-of-LoRAs](https://arxiv.org/abs/2503.01743)
  - [Optimizing Small Language Models for In-Vehicle Function-Calling](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) Fine-Tuning PHI-3 for Multiple-Choice Question Answering: Methodology, Results, and Challenges](https://arxiv.org/abs/2501.01588)
  - [Phi-4-reasoning Technical Report](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Phi-4-mini-reasoning Technical Report](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## ਫਾਈ ਮਾਡਲਾਂ ਦੀ ਵਰਤੋਂ

### ਅਜ਼ੂਰ ਏਆਈ ਫਾਊਂਡਰੀ 'ਤੇ ਫਾਈ

ਤੁਸੀਂ ਸਿੱਖ ਸਕਦੇ ਹੋ ਕਿ ਮਾਇਕ੍ਰੋਸਾਫਟ ਫਾਈ ਨੂੰ ਕਿਵੇਂ ਵਰਤਣਾ ਹੈ ਅਤੇ ਆਪਣੇ ਵੱਖ-ਵੱਖ ਹਾਰਡਵੇਅਰ ਡਿਵਾਈਸਾਂ ਵਿੱਚ E2E ਸਮਾਧਾਨ ਕਿਵੇਂ ਬਣਾਉਣੇ ਹਨ। ਫਾਈ ਨੂੰ ਆਪਣੇ ਲਈ ਅਨੁਭਵ ਕਰਨ ਲਈ, ਮਾਡਲਾਂ ਨਾਲ ਖੇਡਣਾ ਸ਼ੁਰੂ ਕਰੋ ਅਤੇ ਆਪਣੇ ਦੇਣ-ਦਰਸਾਉਣ ਲਈ ਫਾਈ ਨੂੰ ਕਸਟਮਾਈਜ਼ ਕਰੋ, ਇਸ ਲਈ ਤੁਸੀਂ [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai) ਦੀ ਵਰਤੋਂ ਕਰ ਸਕਦੇ ਹੋ। ਤੁਸੀਂ [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md) ਨਾਲ ਸ਼ੁਰੂਆਤ ਕਰਨ ਬਾਰੇ ਹੋਰ ਜਾਣ ਸਕਦੇ ਹੋ।

**ਪਲੇਗ੍ਰਾਊਂਡ**  
ਹਰ ਇੱਕ ਮਾਡਲ ਦੇਖਭਾਲ ਲਈ ਇੱਕ ਖਾਸ ਪਲੇਗ੍ਰਾਊਂਡ ਹੈ ਜਿਸ 'ਚ ਤੁਸੀਂ ਮਾਡਲ ਦਾ ਟੈਸਟ ਕਰ ਸਕਦੇ ਹੋ: [Azure AI Playground](https://aka.ms/try-phi3)।

### ਗਿਟਹਬ ਮਾਡਲਾਂ 'ਤੇ ਫਾਈ

ਤੁਸੀਂ ਸਿੱਖ ਸਕਦੇ ਹੋ ਕਿ ਮਾਇਕ੍ਰੋਸਾਫਟ ਫਾਈ ਨੂੰ ਕਿਵੇਂ ਵਰਤਣਾ ਹੈ ਅਤੇ ਆਪਣੇ ਵੱਖ-ਵੱਖ ਹਾਰਡਵੇਅਰ ਡਿਵਾਈਸਾਂ ਵਿੱਚ E2E ਸਮਾਧਾਨ ਕਿਵੇਂ ਬਣਾਉਣੇ ਹਨ। ਫਾਈ ਨੂੰ ਆਪਣੇ ਲਈ ਅਨੁਭਵ ਕਰਨ ਲਈ, ਮਾਡਲ ਨਾਲ ਖੇਡਣਾ ਸ਼ੁਰੂ ਕਰੋ ਅਤੇ ਆਪਣੇ ਦੇਣ-ਦਰਸਾਉਣ ਲਈ ਫਾਈ ਨੂੰ ਕਸਟਮਾਈਜ਼ ਕਰੋ, ਇਸ ਲਈ ਤੁਸੀਂ [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) ਦੀ ਵਰਤੋਂ ਕਰ ਸਕਦੇ ਹੋ। ਤੁਸੀਂ [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md) ਨਾਲ ਸ਼ੁਰੂਆਤ ਕਰਨ ਬਾਰੇ ਹੋਰ ਜਾਣ ਸਕਦੇ ਹੋ।

**ਪਲੇਗ੍ਰਾਊਂਡ**  
ਹਰ ਇੱਕ ਮਾਡਲ ਲਈ ਇੱਕ ਖਾਸ [ਪਲੇਗ੍ਰਾਊਂਡ ਮਾਡਲ ਦੇ ਜਾਂਚ ਲਈ](/md/02.QuickStart/GitHubModel_QuickStart.md) ਹੈ।

### ਹੱਗਿੰਗ ਫੇਸ 'ਤੇ ਫਾਈ

ਤੁਸੀਂ [Hugging Face](https://huggingface.co/microsoft) 'ਤੇ ਵੀ ਮਾਡਲ ਲੱਭ ਸਕਦੇ ਹੋ।

**ਪਲੇਗ੍ਰਾਊਂਡ**  
[Hugging Chat playground](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

 ## 🎒 ਹੋਰ ਕੋਰਸز

ਸਾਡੀ ਟੀਮ ਹੋਰ ਕੋਰਸਜ਼ ਤਿਆਰ ਕਰਦੀ ਹੈ! ਵੇਖੋ:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain  
[![LangChain4j for Beginners](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)  
[![LangChain.js for Beginners](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)  

---

### Azure / Edge / MCP / ਏਜੰਟ  
[![AZD for Beginners](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)  
[![Edge AI for Beginners](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)  
[![MCP for Beginners](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)  
[![AI Agents for Beginners](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)  

---
 
### ਜਨਰੇਟਿਵ ਏਆਈ ਸੀਰੀਜ਼  
[![Generative AI for Beginners](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)  
[![Generative AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)  
[![Generative AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)  
[![Generative AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)  

---
 
### ਕੋਰ ਸਿੱਖਿਆ  
[![ML for Beginners](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)  
[![Data Science for Beginners](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)  
[![AI for Beginners](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)  
[![Cybersecurity for Beginners](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)  
[![Web Dev for Beginners](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)  
[![IoT for Beginners](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)  
[![XR Development for Beginners](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)  

---
 
### ਕੋਪਾਇਲਟ ਸੀਰੀਜ਼  
[![Copilot for AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)  
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)  
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)  
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## ਜ਼ਿੰਮੇਵਾਰ ਏਆਈ

ਮਾਇਕ੍ਰੋਸਾਫਟ ਆਪਣੇ ਗਾਹਕਾਂ ਨੂੰ ਸਾਡੇ ਏਆਈ ਉਤਪਾਦਾਂ ਨੂੰ ਜ਼ਿੰਮੇਵਾਰੀ ਨਾਲ ਵਰਤਣ ਵਿੱਚ ਮਦਦ ਕਰਨ, ਸਾਨੂੰ ਸਿੱਖਣ ਵਾਲੀਆਂ ਗੱਲਾਂ ਸਾਂਝੀਆਂ ਕਰਨ ਅਤੇ ਟਰਾਂਸਪੇਰਨਸੀ ਨੋਟਾਂ ਅਤੇ ਪ੍ਰਭਾਵ ਮੂਲਾਂਕਣਾਂ ਵਰਗੀਆਂ ਸੰਦਾਂ ਰਾਹੀਂ ਭਰੋਸੇਮੰਦ ਭਾਈਚਾਰੇ ਬਣਾਉਣ ਲਈ ਵਚਨਬੱਧ ਹੈ। ਇਹਨਾਂ ਵਿਚੋਂ ਬਹੁਤ ਸਾਰੇ ਸਰੋਤ ਤੁਹਾਡੀ ਉਪਲਬਧਤਾ ਲਈ [https://aka.ms/RAI](https://aka.ms/RAI) 'ਤੇ ਮਿਲ ਸਕਦੇ ਹਨ।  
ਮਾਇਕ੍ਰੋਸਾਫਟ ਦਾ ਜ਼ਿੰਮੇਵਾਰ ਏਆਈ ਲਈ ਨਜ਼ਰੀਆ ਸਾਡੇ ਏਆਈ ਨੈਤਿਕ ਮੂਲ ਭਾਵਨਾਂ ਉੱਤੇ ਬਣਿਆ ਹੈ, ਜੋ ਹਨ: ਨਿਆਂ, ਭਰੋਸੇਯੋਗਤਾ ਅਤੇ ਸੁਰੱਖਿਆ, ਪ੍ਰਾਈਵੇਸੀ ਅਤੇ ਸੁਰੱਖਿਆ, ਸ਼ਾਮਿਲਤਾ, ਪਾਰਦਰਸ਼ਤਾ ਅਤੇ ਜ਼ਿੰਮੇਵਾਰੀ।

ਵੱਡੇ ਪੱਧਰ ਦੇ ਕੁਦਰਤੀ ਭਾਸ਼ਾ, ਚਿੱਤਰ ਅਤੇ ਸੱਭਿਆਚਾਰ ਮਾਡਲ - ਜਿਵੇਂ ਕਿ ਇਸ ਨਮੂਨੇ ਵਿਚ ਵਰਤੇ ਗਏ ਹਨ - ਸੰਭਵ ਹੈ ਕਿ ਵਿਅਵਹਾਰ ਵਿੱਚ ਨਿਆਂਯੋਗ, ਭਰੋਸੇਯੋਗ ਨਾ ਹੋਣ ਜਾਂ ਅਪਮਾਨਜਨਕ ਹੋਣ, ਜਿਸ ਨਾਲ ਨੁਕਸਾਨ ਹੋ ਸਕਦਾ ਹੈ। ਕਿਰਪਾ ਕਰਕੇ ਸੂਚਿਤ ਰਹਿਣ ਲਈ [Azure OpenAI ਸੇਵਾ ਟਰਾਂਸਪੇਰਨਸੀ ਨੋਟ](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) ਨੂੰ ਵੇਖੋ ਜਿੱਥੇ ਖਤਰੇ ਅਤੇ ਸੀਮਾਵਾਂ ਦਰਸਾਈ ਗਈਆਂ ਹਨ।  

ਇਹਨਾਂ ਖਤਰਿਆਂ ਨੂੰ ਘਟਾਉਣ ਲਈ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਗਈ ਪਹੁੰਚ ਇਹ ਹੈ ਕਿ ਤੁਸੀਂ ਆਪਣੀ ਆਰਕੀਟੈਕਚਰ ਵਿੱਚ ਇਕ ਸੁਰੱਖਿਆ ਪ੍ਰਣਾਲੀ ਸ਼ਾਮਿਲ ਕਰੋ ਜੋ ਨੁਕਸਾਨਦੇਹ ਵਿਅਵਹਾਰ ਪਛਾਣ ਸਕੇ ਅਤੇ ਰੋਕ ਸਕੇ। [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) ਇੱਕ ਸੁਤੰਤਰ ਪਰਤ ਮੁਹੱਈਆ ਕਰਦਾ ਹੈ ਜੋ ਐਪਲੀਕੇਸ਼ਨਾਂ ਅਤੇ ਸੇਵਾਵਾਂ ਵਿੱਚ ਨੁਕਸਾਨਦੇਹ ਯੂਜ਼ਰ ਅਤੇ ਏਆਈ ਬਣਾਇਆ ਸਮੱਗਰੀ ਪਛਾਣ ਸਕਦਾ ਹੈ। Azure AI Content Safety ਵਿੱਚ ਟੈਕਸਟ ਅਤੇ ਚਿੱਤਰ ਏਪੀਆਈਆਂ ਸ਼ਾਮਿਲ ਹਨ ਜੋ ਤੁਹਾਨੂੰ ਨੁਕਸਾਨਦੇਹ ਸਮੱਗਰੀ ਦਾ ਪਤਾ ਲਗਾਉਣ ਦੀ ਆਗਿਆ ਦਿੰਦੀਆਂ ਹਨ। Azure AI Foundry ਵਿੱਚ, Content Safety ਸੇਵਾ ਵੱਖ-ਵੱਖ ਮਾਡਲਾਂ ਵਿੱਚ ਨੁਕਸਾਨਦੇਹ ਸਮੱਗਰੀ ਦੀ ਪਛਾਣ ਲਈ ਨਮੂਨਾ ਕੋਡ ਵੇਖਣ, ਖੋਜਣ ਅਤੇ ਕੋਸ਼ਿਸ਼ ਕਰਨ ਦੀ ਆਗਿਆ ਦਿੰਦੀ ਹੈ। ਹੇਠਾਂ ਦਿੱਤੀ [quickstart ਦਸਤਾਵੇਜ਼ੀ](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) ਤੁਹਾਨੂੰ ਸੇਵਾ ਨੂੰ ਬੇਨਤੀ ਭੇਜਣ ਲਈ ਮਦਦ ਕਰਦਾ ਹੈ।  

ਇੱਕ ਹੋਰ ਪਹلو ਹੈ ਕੁੱਲ ਐਪਲੀਕੇਸ਼ਨ ਦੀ ਕਾਰਗੁਜ਼ਾਰੀ। ਬਹੁ-ਮਾਡਲ ਅਤੇ ਬਹੁ-ਮਾਡਲ ਵਾਲੀਆਂ ਐਪਲੀਕੇਸ਼ਨਾਂ ਦੇ ਨਾਲ, ਅਸੀਂ ਕਾਰਗੁਜ਼ਾਰੀ ਦਾ ਮਤਲਬ ਲੈਂਦੇ ਹਾਂ ਕਿ ਸਿਸਟਮ ਤਿਵਾਡੀ ਅਤੇ ਤੁਹਾਡੇ ਉਪਭੋਗਤਿਆਂ ਦੀ ਉਮੀਦਾਂ ਅਨੁਸਾਰ ਕਾਰਗੁਜ਼ਾਰੀ ਕਰਦਾ ਹੈ, ਜਿਸ ਵਿੱਚ ਨੁਕਸਾਨਦੇਹ ਨਤੀਜੇ ਬਣਾਉਣਾ ਸ਼ਾਮਿਲ ਨਹੀਂ ਹੈ। ਤੁਹਾਡੇ ਕੋਲ ਆਪਣੇ ਕੁੱਲ ਐਪਲੀਕੇਸ਼ਨ ਦੀ ਕਾਰਗੁਜ਼ਾਰੀ ਨੂੰ [ਪ੍ਰਦਰਸ਼ਨ ਅਤੇ ਗੁਣਵੱਤਾ ਅਤੇ ਜੋਖਮ ਅਤੇ ਸੁਰੱਖਿਆ ਮੂਲਾਂਕਣਕਾਰਾਂ](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅੰਕੜਾ ਕਰਨ ਦੀ ਯੋਗਤਾ ਵੀ ਹੈ। ਤੁਸੀਂ [ਕਸਟਮ ਮੂਲਾਂਕਣਕਾਰਾਂ](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators) ਨਾਲ ਬਣਾਉਣ ਅਤੇ ਅੰਕੜਾ ਕਰਨ ਦੀ ਵੀ ਸਮਰੱਥਾ ਰੱਖਦੇ ਹੋ।
ਤੁਸੀਂ ਆਪਣੇ ਵਿਕਾਸ ਵਾਤਾਵਰਣ ਵਿੱਚ ਆਪਣੇ AI ਐਪਲੀਕੇਸ਼ਨ ਦਾ ਮੂਲਾਂਕਣ [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕਰ ਸਕਦੇ ਹੋ। ਚਾਹੇ ਤੁਹਾਡੇ ਕੋਲ ਟੈਸਟ ਡੇਟਾਸੇਟ ਹੋਵੇ ਜਾਂ ਲਕੜੀ ਹੋਵੇ, ਤੁਹਾਡੇ ਜਨਰੇਟਿਵ AI ਐਪਲੀਕੇਸ਼ਨ ਦੀਆਂ ਜਨਰੇਸ਼ਨਾਂ ਦੀ ਗਿਣਤੀ ਅੰਦਰੂਨੀ ਮੁੱਲਾਂਕਸੀਕਾਰਾਂ ਜਾਂ ਤੁਹਾਡੇ ਚੋਣ ਦੇ ਕਸਟਮ ਮੁੱਲਾਂਕਸੀਕਾਰਾਂ ਨਾਲ ਮਾਪੀ ਜਾਂਦੀ ਹੈ। ਆਪਣੀ ਪ੍ਰਣਾਲੀ ਦਾ ਮੁੱਲਾਂਕਣ ਕਰਨ ਲਈ azure ai evaluation sdk ਨਾਲ ਸ਼ੁਰੂ ਕਰਨ ਲਈ, ਤੁਸੀਂ [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) ਦੀ ਪਾਲਣਾ ਕਰ ਸਕਦੇ ਹੋ। ਜਦੋਂ ਤੁਸੀਂ ਮੁੱਲਾਂਕਣ ਚਲਾਉਂਦੇ ਹੋ, ਤਾਂ ਤੁਸੀਂ ਨਤੀਜੇ [Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results) ਵਿੱਚ ਦਰਸਾ ਸਕਦੇ ਹੋ। 

## ਟ੍ਰੇਡਮਾਰਕ਼

ਇਹ ਪ੍ਰੋਜੈਕਟ ਪ੍ਰੋਜੈਕਟਾਂ, ਉਤਪਾਦਾਂ ਜਾਂ ਸੇਵਾਵਾਂ ਲਈ ਟ੍ਰੇਡਮਾਰਕ ਜਾਂ ਲੋਗੋ ਸ਼ਾਮਲ ਕਰ ਸਕਦਾ ਹੈ। Microsoft ਦੇ ਟ੍ਰੇਡਮਾਰਕ ਜਾਂ ਲੋਗੋ ਦੀ ਮਨਜ਼ੂਰਸ਼ੁਦਾ ਵਰਤੋਂ [Microsoft ਦੇ Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) ਦੇ ਅਧੀਨ ਹੈ ਅਤੇ ਇਸਦੀ ਪਾਲਣਾ ਲਾਜ਼ਮੀ ਹੈ। ਇਸ ਪ੍ਰੋਜੈਕਟ ਦੇ ਸੋਧੇ ਗਏ ਵਰਜਨਾਂ ਵਿੱਚ Microsoft ਦੇ ਟ੍ਰੇਡਮਾਰਕ ਜਾਂ ਲੋਗੋ ਦੀ ਵਰਤੋਂ ਭੁਲਬੁਲਾਹਟ ਨਹੀਂ ਪੈਦਾ ਕਰਨੀ ਚਾਹੀਦੀ ਜਾਂ Microsoft ਦੀ ਸਪਾਂਸਰਸ਼ਿਪ ਦਾ ਦਰਸਾਉਣਾ ਨਹੀਂ ਚਾਹੀਦਾ। ਕਿਸੇ ਤੀਜੇ ਪਾਸੇ ਦੇ ਟ੍ਰੇਡਮਾਰਕ ਜਾਂ ਲੋਗੋ ਦੀ ਵਰਤੋਂ ਉਹਨਾਂ ਤੀਜੇ ਪਾਸੇ ਦੀਆਂ ਨੀਤੀਆਂ ਦੇ ਅਧੀਨ ਹੈ। 

## ਮਦਦ ਪ੍ਰਾਪਤ ਕਰਨਾ

ਜੇ ਤੁਸੀਂ ਫਸ ਜਾਂਦੇ ਹੋ ਜਾਂ AI ਐਪ ਬਣਾਉਣ ਬਾਰੇ ਕੋਈ ਸਵਾਲ ਹੈ, ਤਾਂ ਸ਼ਾਮਿਲ ਹੋਵੋ:

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

ਜੇ ਤੁਹਾਨੂੰ ਉਤਪਾਦ ਬਾਰੇ ਫੀਡਬੈਕ ਜਾਂ ਗਲਤੀਆਂ ਮਿਲਦੀਆਂ ਹਨ, ਤਾਂ ਵੇਖੋ:

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਜ਼ਿੰਮੇਵਾਰੀ ਤੋਂ ਮੁਕਤੀ**:
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜੇਕਰਕਿ ਅਸੀਂ ਸਹੀ ਹੋਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਵਿੱਚ ਰੱਖੋ ਕਿ ਆਟੋਮੈਟਿਕ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਪਸ਼ਟਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਸਮਝਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਉਤਪੰਨ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->