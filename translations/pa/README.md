# Phi Cookbook: Microsoft ਦੇ Phi ਮਾਡਲਾਂ ਨਾਲ ਹੱਥ-ਉੱਤੇ ਉਦਾਹਰਨਾਂ

[![GitHub Codespaces ਵਿੱਚ ਸੈਂਪਲ ਖੋਲ੍ਹੋ ਅਤੇ ਵਰਤੋ](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Dev Containers ਵਿੱਚ ਖੋਲ੍ਹੋ](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub ਯੋਗਦਾਨਕਾਰ](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub ਮੁੱਦੇ](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub ਪੁੱਲ-ਰਿਕਵੇਸਟ](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![ਪੀ.ਆਰ.ਸਵਾਗਤ ਹੈ](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub ਨਿਗਰਾਨ](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub ਫੋਰਕ](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub ਸਿਤਾਰੇ](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi Microsoft ਵੱਲੋਂ ਵਿਕਸਤ ਖੁੱਲ੍ਹਾ ਸਰੋਤ AI ਮਾਡਲਾਂ ਦੀ ਇੱਕ ਕੜੀ ਹੈ।

Phi ਇਸ ਸਮੇਂ ਸਭ ਤੋਂ ਸ਼ਕਤੀਸ਼ਾਲੀ ਅਤੇ ਲਾਗਤ ਪ੍ਰਭਾਵਸ਼ਾਲੀ ਛੋਟਾ ਭਾਸ਼ਾ ਮਾਡਲ (SLM) ਹੈ, ਜਿਸਦਾ ਬਹੁਭਾਸ਼ੀ, ਤਰਕਸ਼ੀਲ, ਪਾਠ/ਚੈੱਟ ਉਤਪਾਦਨ, ਕੋਡਿੰਗ, ਚਿੱਤਰ, ਆਡੀਓ ਅਤੇ ਹੋਰ ਪਰਿਸ਼ਥਿਤੀਆਂ ਵਿੱਚ ਬਹੁਤ ਵਧੀਆ ਬੈਂਚਮਾਰਕ ਹੈ।

ਤੁਸੀਂ Phi ਨੂੰ ਕਲਾਉਡ ਜਾਂ ਏਜ ਡਿਵਾਈਸਾਂ 'ਤੇ ਡਿਪਲੋਇ ਕਰ ਸਕਦੇ ਹੋ, ਅਤੇ ਸੀਮਿਤ ਕਮਪਿਊਟਿੰਗ ਪਾਵਰ ਨਾਲ ਆਸਾਨੀ ਨਾਲ ਜਨਰੇਟਿਵ AI ਐਪਲੀਕੇਸ਼ਨ ਬਣਾ ਸਕਦੇ ਹੋ।

ਇਹਨਾਂ ਸਾਧਨਾਂ ਨਾਲ ਸ਼ੁਰੂਆਤ ਕਰਨ ਲਈ ਇਹ ਕਦਮ ਕਰੋ:
1. **ਰੀਪੋਜ਼ਿਟਰੀ ਫੋਰਕ ਕਰੋ**: ਕਲਿੱਕ ਕਰੋ [![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **ਰੀਪੋਜ਼ਿਟਰੀ ਕਲੋਨ ਕਰੋ**: `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Microsoft AI Discord ਕਮਿਊਨਿਟੀ ਵਿੱਚ ਸ਼ਾਮਿਲ ਹੋਵੋ ਅਤੇ ਮਾਹਰਾਂ ਅਤੇ ਹੋਰ ਵਿਕਾਸਕਾਰਾਂ ਨਾਲ ਮਿਲੋ**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/pa/cover.eb18d1b9605d754b.webp)

### 🌐 ਬਹੁ-ਭਾਸ਼ਾਈ ਸਹਿਯੋਗ

#### GitHub ਐਕਸ਼ਨ ਵੱਲੋਂ ਸਹਿਯੋਗਤ (ਆਟੋਮੈਟਡ ਅਤੇ ਸਦਾ ਅਪ-ਟੂ-ਡੇਟ)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](./README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **ਕੀ ਤੁਸੀਂ ਸਥਾਨਕ ਤੌਰ 'ਤੇ ਕਲੋਨ ਕਰਨਾ ਪਸੰਦ ਕਰਦੇ ਹੋ?**

> ਇਸ ਰੀਪੋਜ਼ਿਟਰੀ ਵਿੱਚ 50+ ਭਾਸ਼ਾਈ ਅਨੁਵਾਦ ਸ਼ਾਮਿਲ ਹਨ ਜੋ ਡਾਉਨਲੋਡ ਆਕਾਰ ਨੂੰ ਕਾਫ਼ੀ ਵਧਾਉਂਦੇ ਹਨ। ਅਨੁਵਾਦਾਂ ਤੋਂ ਬਿਨਾਂ ਕਲੋਨ ਕਰਨ ਲਈ, sparse checkout ਵਰਤੋ:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/PhiCookBook.git
> cd PhiCookBook
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> ਇਹ ਤੁਹਾਨੂੰ ਕੋਰਸ ਪੂਰਾ ਕਰਨ ਲਈ ਸਾਰੀ ਜ਼ਰੂਰੀ ਚੀਜ਼ ਤੇਜ਼ ਡਾਉਨਲੋਡ ਨਾਲ ਦਿੰਦਾ ਹੈ।
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## ਸਮੱਗਰੀ ਸੂਚੀ

- ਪਰਿਚਯ
  - [Phi ਪਰਿਵਾਰ ਵਿੱਚ ਤੁਹਾਡਾ ਸਵਾਗਤ ਹੈ](./md/01.Introduction/01/01.PhiFamily.md)
  - [ਆਪਣਾ ਵਾਤਾਵਰਨ ਸੈੱਟਅੱਪ ਕਰਨਾ](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [ਮੁੱਖ ਤਕਨਾਲੋਜੀਆਂ ਬਾਰੇ ਸਮਝ](./md/01.Introduction/01/01.Understandingtech.md)
  - [Phi ਮਾਡਲਾਂ ਲਈ AI ਸੁਰੱਖਿਆ](./md/01.Introduction/01/01.AISafety.md)
  - [Phi ਹਾਰਡਵੇਅਰ ਸਹਿਯੋਗ](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [ਪਲੇਟਫਾਰਮਾਂ ਤੱਕ Phi ਮਾਡਲ ਅਤੇ ਉਪਲਬਧਤਾ](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Guidance-ai ਅਤੇ Phi ਦੀ ਵਰਤੋਂ](./md/01.Introduction/01/01.Guidance.md)
  - [GitHub ਮਾਰਕੀਟਪਲੇਸ ਮਾਡਲ](https://github.com/marketplace/models)
  - [Azure AI ਮਾਡਲ ਕੈਟਲੌਗ](https://ai.azure.com)

- ਵੱਖ-ਵੱਖ ਵਾਤਾਵਰਣ ਵਿੱਚ Phi ਇੰਫਰੈਂਸ
    -  [Hugging face](./md/01.Introduction/02/01.HF.md)
    -  [GitHub ਮਾਡਲ](./md/01.Introduction/02/02.GitHubModel.md)
    -  [Azure AI Foundry ਮਾਡਲ ਕੈਟਲੌਗ](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    -  [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md)

- Phi ਪਰਿਵਾਰ ਇੰਫਰੈਂਸ
    - [iOS ਵਿੱਚ Phi ਇੰਫਰੈਂਸ](./md/01.Introduction/03/iOS_Inference.md)
    - [ਐਂਡਰਾਇਡ ਵਿੱਚ Phi ਇੰਫਰੈਂਸ](./md/01.Introduction/03/Android_Inference.md)
    - [ਜੇਟਸਨ ਵਿੱਚ Phi ਇੰਫਰੈਂਸ](./md/01.Introduction/03/Jetson_Inference.md)
    - [AI PC ਵਿੱਚ Phi ਇੰਫਰੈਂਸ](./md/01.Introduction/03/AIPC_Inference.md)
    - [Apple MLX ਫ੍ਰੇਮਵਰਕ ਨਾਲ Phi ਇੰਫਰੈਂਸ](./md/01.Introduction/03/MLX_Inference.md)
    - [ਲੋਕਲ ਸਰਵਰ ਵਿੱਚ Phi ਇੰਫਰੈਂਸ](./md/01.Introduction/03/Local_Server_Inference.md)
    - [AI Toolkit ਦੀ ਵਰਤੋਂ ਨਾਲ ਰਿਮੋਟ ਸਰਵਰ ਵਿੱਚ Phi ਇੰਫਰੈਂਸ](./md/01.Introduction/03/Remote_Interence.md)
    - [Rust ਨਾਲ Phi ਇੰਫਰੈਂਸ](./md/01.Introduction/03/Rust_Inference.md)
    - [ਲੋਕਲ ਵਿੱਚ Phi-ਵਿਜ਼ਨ ਇੰਫਰੈਂਸ](./md/01.Introduction/03/Vision_Inference.md)
    - [Kaito AKS, Azure Containers (ਆਧਿਕਾਰਿਕ ਸਹਿਯੋਗ) ਨਾਲ Phi ਇੰਫਰੈਂਸ](./md/01.Introduction/03/Kaito_Inference.md)
-  [Phi ਪਰਿਵਾਰ ਦੀ ਮਾਤਰਾ ਨਿਰਧਾਰਿਤ ਕਰਨਾ](./md/01.Introduction/04/QuantifyingPhi.md)
    - [llama.cpp ਦੀ ਵਰਤੋਂ ਨਾਲ Phi-3.5 / 4 ਦਾ ਕੋਆਂਟਾਈਜ਼ਿੰਗ](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [onnxruntime ਲਈ ਜਨਰੇਟਿਵ AI ਐਕਸਟੈਨਸ਼ਨ ਨਾਲ Phi-3.5 / 4 ਦਾ ਕੋਆਂਟਾਈਜ਼ਿੰਗ](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Intel OpenVINO ਦੀ ਵਰਤੋਂ ਨਾਲ Phi-3.5 / 4 ਦਾ ਕੋਆਂਟਾਈਜ਼ਿੰਗ](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Apple MLX ਫ੍ਰੇਮਵਰਕ ਦੀ ਵਰਤੋਂ ਨਾਲ Phi-3.5 / 4 ਦਾ ਕੋਆਂਟਾਈਜ਼ਿੰਗ](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

- Phi ਮੁਲਾਂਕਣ
    - [ਜਵਾਬਦੇਹ AI](./md/01.Introduction/05/ResponsibleAI.md)
    - [ਮੁਲਾਂਕਣ ਲਈ Azure AI Foundry](./md/01.Introduction/05/AIFoundry.md)
    - [ਮੁਲਾਂਕਣ ਲਈ Promptflow ਦੀ ਵਰਤੋਂ](./md/01.Introduction/05/Promptflow.md)
 
- Azure AI Search ਨਾਲ RAG
    - [Phi-4-mini ਅਤੇ Phi-4-multimodal (RAG) ਨੂੰ Azure AI Search ਨਾਲ ਕਿਵੇਂ ਵਰਤਣਾ ਹੈ](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Phi ਐਪਲੀਕੇਸ਼ਨ ਵਿਕਾਸ ਸੈਂਪਲ
  - ਪਾਠ & ਚੈਟ ਐਪਲੀਕੇਸ਼ਨ
    - Phi-4 ਸੈਂਪਲ 🆕
      - [📓] [Phi-4-mini ONNX ਮਾਡਲ ਨਾਲ ਚੈਟ ਕਰੋ](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Phi-4 ਲੋਕਲ ONNX ਮਾਡਲ ਨਾਲ ਚੈਟ .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Sementic Kernel ਦੀ ਵਰਤੋਂ ਨਾਲ Phi-4 ONNX ਦੇ ਨਾਲ .NET ਕਨਸੋਲ ਐਪ ਵਿਚ ਚੈਟ](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Phi-3 / 3.5 ਸੈਂਪਲ
      - [Phi3, ONNX ਰਨਟਾਈਮ ਵੈੱਬ ਅਤੇ WebGPU ਦੀ ਵਰਤੋਂ ਨਾਲ ਬ੍ਰਾਊਜਰ ਵਿੱਚ ਲੋਕਲ ਚੈਟਬੌਟ](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVino ਚੈਟ](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [ਮਲਟੀ ਮਾਡਲ - ਇੰਟਰਐਕਟਿਵ ਫਾਈ-3-ਮਿਨੀ ਅਤੇ ਓਪਨਏਆਈ ਵਿਸਪਰ](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - ਇੱਕ ਰੈਪਰ ਬਣਾਉਣਾ ਅਤੇ MLFlow ਨਾਲ ਫਾਈ-3 ਦੀ ਵਰਤੋਂ](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [ਮਾਡਲ ਅਪਟੀਮਾਈਜ਼ੇਸ਼ਨ - ਓਨਐਕਸ ਰਨਟਾਈਮ ਵੈੱਬ ਲਈ ਫਾਈ-3-ਮਿਨੀ ਮਾਡਲ ਨੂੰ ਔਲਿਵ ਨਾਲ ਕਿਵੇਂ ਅਪਟੀਮਾਈਜ਼ ਕਰੀਏ](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [ਫਾਈ-3 ਮਿਨੀ-4k-ਇੰਸਟ੍ਰਕਟ-onnx ਦੇ ਨਾਲ WinUI3 ਐਪ](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      -[WinUI3 ਮਲਟੀ ਮਾਡਲ ਏਆਈ ਪਾਵਰਡ ਨੋਟਸ ਐਪ ਸੈਂਪਲ](https://github.com/microsoft/ai-powered-notes-winui3-sample)
      - [ਪ੍ਰਾਂਪਟ ਫਲੋ ਨਾਲ ਕਸਟਮ ਫਾਈ-3 ਮਾਡਲਾਂ ਨੂੰ ਫਾਈਨ-ਟਿਊਨ ਅਤੇ ਇੰਟੀਗਰੇਟ ਕਰੋ](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
      - [ਅਜ਼ੂਰ ਏਆਈ ਫਾਊਂਡਰੀ ਵਿੱਚ ਪ੍ਰਾਂਪਟ ਫਲੋ ਨਾਲ ਕਸਟਮ ਫਾਈ-3 ਮਾਡਲਾਂ ਨੂੰ ਫਾਈਨ-ਟਿਊਨ ਅਤੇ ਇੰਟੀਗਰੇਟ ਕਰੋ](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
      - [ਮਾਈਕ੍ਰੋਸੌਫਟ ਦੇ ਜ਼ਿੰਮੇਵਾਰ ਏਆਈ ਨੀਤੀਆਂ ਉੱਤੇ ਧਿਆਨ ਕੇਂਦਰਿਤ ਅਜ਼ੂਰ ਏਆਈ ਫਾਊਂਡਰੀ ਵਿੱਚ ਫਾਈਨ-ਟਿਊਨ ਕੀਤੇ ਫਾਈ-3 / ਫਾਈ-3.5 ਮਾਡਲ ਦਾ ਮੁਲਾਂਕਣ ਕਰੋ](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
      - [📓] [ਫਾਈ-3.5-ਮਿਨੀ-ਇੰਸਟ੍ਰਕਟ ਭਾਸ਼ਾ ਪੂਰਵਾਨੁਮਾਨ ਸੈਂਪਲ (ਚੀਨੀ/ਅੰਗਰੇਜ਼ੀ)](./md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
      - [ਫਾਈ-3.5-ਇੰਸਟ੍ਰਕਟ WebGPU RAG ਚੈਟਬੋਟ](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
      - [ਫਾਈ-3.5-ਇੰਸਟ੍ਰਕਟ ONNX ਨਾਲ ਪ੍ਰਾਂਪਟ ਫਲੋ ਸਾਧਨ ਬਣਾਉਣ ਲਈ Windows GPU ਦੀ ਵਰਤੋਂ](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
      - [ਐਂਡਰਾਇਡ ਐਪ ਬਣਾਉਣ ਲਈ ਮਾਈਕ੍ਰੋਸੌਫਟ ਫਾਈ-3.5 ਟੀਐੱਫਲਾਈਟ ਦੀ ਵਰਤੋਂ](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
      - [ਮਾਈਕ੍ਰੋਸੌਫਟ.ML.OnnxRuntime ਦੀ ਵਰਤੋਂ ਨਾਲ ਸਥਾਨਕ ONNX ਫਾਈ-3 ਮਾਡਲ ਵਾਪਰਦਾ Q&A .NET ਉਦਾਹਰਨ](../../md/04.HOL/dotnet/src/LabsPhi301)
      - [ਸੈਮਾਂਟਿਕ ਕਰਨਲ ਅਤੇ ਫਾਈ-3 ਨਾਲ ਕੰਸੋਲੇ ਚੈਟ .NET ਐਪ](../../md/04.HOL/dotnet/src/LabsPhi302)

  - ਅਜ਼ੂਰ ਏਆਈ ਇੰਫਰੈਂਸ SDK ਕੋਡ ਅਧਾਰਿਤ ਸੈਂਪਲ 
    - ਫਾਈ-4 ਸੈਂਪਲ 🆕
      - [📓] [ਫਾਈ-4-ਮਲਟੀਮੋਡਲ ਦੀ ਵਰਤੋਂ ਨਾਲ ਪ੍ਰੋਜੈਕਟ ਕੋਡ ਤਿਆਰ ਕਰੋ](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
    - ਫਾਈ-3 / 3.5 ਸੈਂਪਲ
      - [ਮਾਈਕ੍ਰੋਸੌਫਟ ਫਾਈ-3 ਪਰਿਵਾਰ ਨਾਲ ਆਪਣਾ ਵਿਜ਼ੂਅਲ ਸਟੂਡੀਓ ਕੋਡ ਗਿਟਹੱਬ ਕੋਪਾਇਲਟ ਚੈਟ ਬਣਾਓ](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
      - [ਗਿਟਹੱਬ ਮਾਡਲਾਂ ਦੁਆਰਾ ਫਾਈ-3.5 ਨਾਲ ਆਪਣਾ ਵਿਜ਼ੂਅਲ ਸਟੂਡੀਓ ਕੋਡ ਚੈਟ ਕੋਪਾਇਲਟ ਏਜੰਟ ਬਣਾਓ](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

  - ਅਡਵਾਂਸਡ ਰੀਜ਼ਨਿੰਗ ਸੈਂਪਲ
    - ਫਾਈ-4 ਸੈਂਪਲ 🆕
      - [📓] [ਫਾਈ-4-ਮਿਨੀ-ਰੀਜ਼ਨਿੰਗ ਜਾਂ ਫਾਈ-4-ਰੀਜ਼ਨਿੰਗ ਸੈਂਪਲ](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
      - [📓] [ਮਾਈਕ੍ਰੋਸੌਫਟ ਔਲਿਵ ਨਾਲ ਫਾਈਨ-ਟਿਊਨਿੰਗ ਫਾਈ-4-ਮਿਨੀ-ਰੀਜ਼ਨਿੰਗ](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [ਐਪਲ ਐਮਐਲਐਕਸ ਨਾਲ ਫਾਈਨ-ਟਿਊਨਿੰਗ ਫਾਈ-4-ਮਿਨੀ-ਰੀਜ਼ਨਿੰਗ](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [ਗਿਟਹੱਬ ਮਾਡਲਾਂ ਨਾਲ ਫਾਈ-4-ਮਿਨੀ-ਰੀਜ਼ਨਿੰਗ](./md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
      - [📓] [ਅਜ਼ੂਰ ਏਆਈ ਫਾਊਂਡਰੀ ਮਾਡਲਾਂ ਨਾਲ ਫਾਈ-4-ਮਿਨੀ-ਰੀਜ਼ਨਿੰਗ](./md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
  - ਡੈਮੋ
      - [ਫਾਈ-4-ਮਿਨੀ ਡੈਮੋਜ਼ ਜੋ ਹੱਗਿੰਗ ਫੇਸ ਸਪੇਸ ਤੇ ਮੇਜ਼ਬਾਨ ਹਨ](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
      - [ਫਾਈ-4-ਮਲਟੀਮੋਡਲ ਡੈਮੋਜ਼ ਜੋ ਹੱਗਿੰਗ ਫੇਸ ਸਪੇਸ ਤੇ ਮੇਜ਼ਬਾਨ ਹਨ](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
  - ਵਿਜ਼ਨ ਸੈਂਪਲ
    - ਫਾਈ-4 ਸੈਂਪਲ 🆕
      - [📓] [ਫਾਈ-4-ਮਲਟੀਮੋਡਲ ਦੀ ਵਰਤੋਂ ਨਾਲ ਤਸਵੀਰਾਂ ਪੜ੍ਹੋ ਅਤੇ ਕੋਡ ਬਣਾਓ](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
    - ਫਾਈ-3 / 3.5 ਸੈਂਪਲ
      -  [📓][ਫਾਈ-3-ਵਿਜ਼ਨ-ਤਸਵੀਰ ਤੋਂ ਪਾਠ](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [ਫਾਈ-3-ਵਿਜ਼ਨ-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
      - [📓][ਫਾਈ-3-ਵਿਜ਼ਨ CLIP ਐੰਬੈਡਿੰਗ](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [ਡੈਮੋ: ਫਾਈ-3 ਰੀਸਾਇਕਲਿੰਗ](https://github.com/jennifermarsman/PhiRecycling/)
      - [ਫਾਈ-3-ਵਿਜ਼ਨ - ਦ੍ਰਿਸ਼ਟੀ ਭਾਸ਼ਾ ਸਹਾਇਕ - ਫਾਈ3-ਵਿਜ਼ਨ ਅਤੇ ਓਪਨਵੀਨੋ ਨਾਲ](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
      - [ਫਾਈ-3 ਵਿਜ਼ਨ NVIDIA NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
      - [ਫਾਈ-3 ਵਿਜ਼ਨ ਓਪਨਵੀਨੋ](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
      - [📓][ਫਾਈ-3.5 ਵਿਜ਼ਨ ਮਲਟੀ-ਫਰੇਮ ਜਾਂ ਮਲਟੀ-ਤਸਵੀਰ ਸੈਂਪਲ](./md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
      - [ਫਾਈ-3 ਵਿਜ਼ਨ ਸਥਾਨਕ ONNX ਮਾਡਲ ਮਾਈਕ੍ਰੋਸੌਫਟ.ML.OnnxRuntime .NET ਦੀ ਵਰਤੋਂ ਨਾਲ](../../md/04.HOL/dotnet/src/LabsPhi303)
      - [ਮੇਨੂ ਅਧਾਰਿਤ ਫਾਈ-3 ਵਿਜ਼ਨ ਸਥਾਨਕ ONNX ਮਾਡਲ ਮਾਈਕ੍ਰੋਸੌਫਟ.ML.OnnxRuntime .NET ਦੀ ਵਰਤੋਂ ਨਾਲ](../../md/04.HOL/dotnet/src/LabsPhi304)

  - ਗਣਿਤ ਸੈਂਪਲ
    -  ਫਾਈ-4-ਮਿਨੀ-ਫਲੈਸ਼-ਰੀਜ਼ਨਿੰਗ-ਇੰਸਟ੍ਰਕਟ ਸੈਂਪਲ 🆕 [ਫਾਈ-4-ਮਿਨੀ-ਫਲੈਸ਼-ਰੀਜ਼ਨਿੰਗ-ਇੰਸਟ੍ਰਕਟ ਨਾਲ ਮੈਥ ਡੈਮੋ](./md/02.Application/09.Math/MathDemo.ipynb)

  - ਆਡੀਓ ਸੈਂਪਲ
    - ਫਾਈ-4 ਸੈਂਪਲ 🆕
      - [📓] [ਫਾਈ-4-ਮਲਟੀਮੋਡਲ ਦੀ ਵਰਤੋਂ ਨਾਲ ਆਡੀਓ ਟ੍ਰਾਂਸਕ੍ਰਿਪਟ ਐਕਸਟਰੈਕਟ ਕਰਨਾ](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
      - [📓] [ਫਾਈ-4-ਮਲਟੀਮੋਡਲ ਆਡੀਓ ਸੈਂਪਲ](./md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
      - [📓] [ਫਾਈ-4-ਮਲਟੀਮੋਡਲ ਸਪੀਚ ਟ੍ਰਾਂਸਲੇਸ਼ਨ ਸੈਂਪਲ](./md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
      - [.NET ਕਨਸੋਲੇ ਐਪਲੀਕੇਸ਼ਨ ਜੋ ਫਾਈ-4-ਮਲਟੀਮੋਡਲ ਆਡੀਓ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇੱਕ ਆਡੀਓ ਫਾਇਲ ਦਾ ਵਿਸ਼ਲੇਸ਼ਣ ਕਰਦਾ ਹੈ ਅਤੇ ਟ੍ਰਾਂਸਕ੍ਰਿਪਟ ਤਿਆਰ ਕਰਦਾ ਹੈ](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

  - MOE ਸੈਂਪਲ
    - ਫਾਈ-3 / 3.5 ਸੈਂਪਲ
      - [📓] [ਫਾਈ-3.5 ਮਿਕਸਚਰ ਆਫ਼ ਐਕਸਪਰਨਟਸ ਮਾਡਲ (MoEs) ਸੋਸ਼ਲ ਮੀਡੀਆ ਸੈਂਪਲ](./md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
      - [📓] [NVIDIA NIM ਫਾਈ-3 MOE, ਅਜ਼ੂਰ ਏਆਈ ਖੋਜ ਅਤੇ LlamaIndex ਨਾਲ ਰੀਟਰੀਵਲ-ਆਗਮੈਂਟਿਡ ਜਨਰੇਸ਼ਨ (RAG) ਪਾਈਪਲਾਈਨ ਬਣਾਉਣਾ](./md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)
      - 
  - ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਸੈਂਪਲ
    - ਫਾਈ-4 ਸੈਂਪਲ 🆕
      -  [📓] [ਫਾਈ-4-ਮਿਨੀ ਨਾਲ ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਦੀ ਵਰਤੋਂ](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
      -  [📓] [ਫਾਈ-4-ਮਿਨੀ ਨਾਲ ਮਲਟੀ-ਏਜੰਟ ਬਣਾਉਣ ਲਈ ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਦੀ ਵਰਤੋਂ](./md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
      -  [📓] [ਓਲਾਮਾ ਨਾਲ ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਦੀ ਵਰਤੋਂ](./md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
      -  [📓] [ONNX ਨਾਲ ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਦੀ ਵਰਤੋਂ](./md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)
  - ਮਲਟੀਮੋਡਲ ਮਿਕਸਿੰਗ ਸੈਂਪਲ
    - ਫਾਈ-4 ਸੈਂਪਲ 🆕
      -  [📓] [ਫਾਈ-4-ਮਲਟੀਮੋਡਲ ਨੂੰ ਇੱਕ ਟੈਕਨੋਲੋਜੀ ਪੱਤਰਕਾਰ ਵਜੋਂ ਵਰਤਣਾ](./md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
      - [.NET ਕਨਸੋਲੇ ਐਪਲੀਕੇਸ਼ਨ ਜੋ ਫਾਈ-4-ਮਲਟੀਮੋਡਲ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਤਸਵੀਰਾਂ ਦਾ ਵਿਸ਼ਲੇਸ਼ਣ ਕਰਦਾ ਹੈ](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- ਫਾਈਨ-ਟਿਊਨਿੰਗ ਫਾਈ ਸੈਂਪਲ
  - [ਫਾਈਨ-ਟਿਊਨਿੰਗ ਸीनਾਰਿਓ](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [ਫਾਈਨ-ਟਿਊਨਿੰਗ ਬਨਾਮ RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [ਫਾਈ-3 ਨੂੰ ਉਦਯੋਗਿਕ ਮਾਹਿਰ ਬਣਾਉਣਾ](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [VS ਕੋਡ ਲਈ ਏਆਈ ਟੂਲਕਿਟ ਨਾਲ ਫਾਈ-3 ਦੀ ਫਾਈਨ-ਟਿਊਨਿੰਗ](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [ਅਜ਼ੂਰ ਮਸ਼ੀਨ ਲਰਨਿੰਗ ਸਰਵਿਸ ਨਾਲ ਫਾਈ-3 ਦੀ ਫਾਈਨ-ਟਿਊਨਿੰਗ](./md/03.FineTuning/Introduce_AzureML.md)
  - [ਲੋਰਾ ਨਾਲ ਫਾਈ-3 ਦੀ ਫਾਈਨ-ਟਿਊਨਿੰਗ](./md/03.FineTuning/FineTuning_Lora.md)
  - [ਕਿਊਲੋਰਾ ਨਾਲ ਫਾਈ-3 ਦੀ ਫਾਈਨ-ਟਿਊਨਿੰਗ](./md/03.FineTuning/FineTuning_Qlora.md)
  - [ਅਜ਼ੂਰ ਏਆਈ ਫਾਊਂਡਰੀ ਨਾਲ ਫਾਈ-3 ਦੀ ਫਾਈਨ-ਟਿਊਨਿੰਗ](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [ਅਜ਼ੂਰ ML CLI/SDK ਨਾਲ ਫਾਈ-3 ਦੀ ਫਾਈਨ-ਟਿਊਨਿੰਗ](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [ਮਾਈਕ੍ਰੋਸੌਫਟ ਔਲਿਵ ਨਾਲ ਫਾਈਨ-ਟਿਊਨਿੰਗ](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [ਮਾਈਕ੍ਰੋਸੌਫਟ ਔਲਿਵ ਹੈਂਡਸ-ਆਨ ਲੈਬ ਨਾਲ ਫਾਈਨ-ਟਿਊਨਿੰਗ](./md/03.FineTuning/olive-lab/readme.md)
  - [ਵੈਟਸ ਐਂਡ ਬਿਆਸ ਨਾਲ ਫਾਈ-3-ਵਿਜ਼ਨ ਦੀ ਫਾਈਨ-ਟਿਊਨਿੰਗ](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [ਐਪਲ ਐਮਐਲਐਕਸ ਫਰੇਮਵਰਕ ਨਾਲ ਫਾਈ-3 ਦੀ ਫਾਈਨ-ਟਿਊਨਿੰਗ](./md/03.FineTuning/FineTuning_MLX.md)
  - [ਫਾਈ-3-ਵਿਜ਼ਨ ਦੀ ਫਾਈਨ-ਟਿਊਨਿੰਗ (ਅਧਿਕਾਰਿਕ ਸਹਾਇਤਾ)](./md/03.FineTuning/FineTuning_Vision.md)
  - [ਕੈਟੋ ਏਕੇਐਸ, ਅਜ਼ੂਰ ਕੰਟੇਨਰ (ਅਧਿਕਾਰਿਕ ਸਹਾਇਤਾ) ਨਾਲ ਫਾਈ-3 ਦੀ ਫਾਈਨ-ਟਿਊਨਿੰਗ](./md/03.FineTuning/FineTuning_Kaito.md)
  - [ਫਾਈ-3 ਅਤੇ 3.5 ਵਿਜ਼ਨ ਦੀ ਫਾਈਨ-ਟਿਊਨਿੰਗ](https://github.com/2U1/Phi3-Vision-Finetune)

- ਹੈਂਡਜ਼ ਆਨ ਲੈਬ
  - [ਕੱਟਿੰਗ-ਏਜ ਮਾਡਲਾਂ ਦਾ ਪਤਾ ਲਗਾਉਣਾ: LLMs, SLMs, ਸਥਾਨਕ ਡਿਵੈਲਪਮੈਂਟ ਅਤੇ ਹੋਰ](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [ਐਨਐਲਪੀ ਸਾਂਭਣਾ: ਮਾਈਕ੍ਰੋਸੌਫਟ ਔਲਿਵ ਨਾਲ ਫਾਈਨ-ਟਿਊਨਿੰਗ](https://github.com/azure/Ignite_FineTuning_workshop)

- ਅਕਾਦਮਿਕ ਰਿਸਰਚ ਪੇਪਰ ਅਤੇ ਪ੍ਰਕਾਸ਼ਨ  

  - [ਪਾਠਪੁਸਤਕ ਹੀ ਤੁਹਾਨੂੰ ਸਭ ਕੁਝ ਦੇਂਦੇ ਹਨ II: phi-1.5 ਤਕਨੀਕੀ ਰਿਪੋਰਟ](https://arxiv.org/abs/2309.05463)
  - [Phi-3 ਤਕਨੀਕੀ ਰਿਪੋਰਟ: ਤੁਹਾਡੇ ਫ਼ੋਨ ਤੇ ਸਥਾਨਿਕ ਤੌਰ 'ਤੇ ਇੱਕ ਬਹੁਤ ਯੋਗ ਭਾਸ਼ਾ ਮਾਡਲ](https://arxiv.org/abs/2404.14219)
  - [Phi-4 ਤਕਨੀਕੀ ਰਿਪੋਰਟ](https://arxiv.org/abs/2412.08905)
  - [Phi-4-Mini ਤਕਨੀਕੀ ਰਿਪੋਰਟ: ਮਿਸ਼ਰਣ-ਆਫ-ਲੋਰਾਜ਼ ਰਾਹੀਂ ਸੰਕੁਚਿਤ ਪਰ ਸ਼ਕਤੀਸ਼ালী ਬਹੁਮੁੱਖੀ ਭਾਸ਼ਾ ਮਾਡਲ](https://arxiv.org/abs/2503.01743)
  - [ਵਾਹਨ-ਅੰਦਰ ਕਾਰਜ-ਕਾਲਿੰਗ ਲਈ ਛੋਟੇ ਭਾਸ਼ਾ ਮਾਡਲਾਂ ਨੂੰ ਉਤਕ੍ਰਿਸ਼ਟ ਕਰਨਾ](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) ਬਹੁ-ਚੋਣ ਸਵਾਲ ਦੇ ਜਵਾਬ ਲਈ PHI-3 ਦਾ ਫਾਈਨ-ਟਿਊਨਿੰਗ: ਵਿਧੀ, ਨਤੀਜੇ ਅਤੇ ਚੁਣੌਤੀਆਂ](https://arxiv.org/abs/2501.01588)
  - [Phi-4 ਸ਼ੌਕਤਾਰਕ ਤਕਨੀਕੀ ਰਿਪੋਰਟ](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Phi-4-mini-ਸ਼ੌਕਤਾਰਕ ਤਕਨੀਕੀ ਰਿਪੋਰਟ](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## ਫਾਈ ਮਾਡਲ ਦੀ ਵਰਤੋਂ

### Azure AI Foundry 'ਤੇ Phi

ਤੁਸੀਂ ਸਿੱਖ ਸਕਦੇ ਹੋ ਕਿ ਮਾਈਕ੍ਰੋਸਾਫਟ Phi ਨੂੰ ਕਿਵੇਂ ਵਰਤਣਾ ਹੈ ਅਤੇ ਆਪਣੀਆਂ ਵੱਖ-ਵੱਖ ਹਾਰਡਵੇਅਰ ਯੰਤਰਾਂ ਵਿੱਚ E2E ਹੱਲ ਕਿਵੇਂ ਬਣਾਏ ਜਾਣ। ਆਪਣੇ ਲਈ Phi ਦਾ ਅਨੁਭਵ ਕਰਨ ਲਈ, ਮਾਡਲਾਂ ਨਾਲ ਖੇਡਣਾ ਸ਼ੁਰੂ ਕਰੋ ਅਤੇ [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਆਪਣੇ ਮਾਮਲਿਆਂ ਲਈ Phi ਨੂੰ ਮੁਕਰਰ ਕਰੋ। ਤੁਸੀਂ ਹੋਰ ਜਾਣਕਾਰੀ ਲਈ [Azure AI Foundry ਨਾਲ ਸ਼ੁਰੂਆਤ](/md/02.QuickStart/AzureAIFoundry_QuickStart.md) ਵੇਖ ਸਕਦੇ ਹੋ।

**ਪਲੇਂਗ੍ਰਾਊਂਡ**  
ਹਰ ਮਾਡਲ ਲਈ ਇਕ ਸਮਰਪਿਤ ਪਲੇਂਗ੍ਰਾਊਂਡ ਹੈ ਮਾਡਲ ਟੈਸਟ ਕਰਨ ਲਈ [Azure AI Playground](https://aka.ms/try-phi3)।

### GitHub Models 'ਤੇ Phi

ਤੁਸੀਂ ਸਿੱਖ ਸਕਦੇ ਹੋ ਕਿ ਮਾਈਕ੍ਰੋਸਾਫਟ Phi ਨੂੰ ਕਿਵੇਂ ਵਰਤਣਾ ਹੈ ਅਤੇ ਆਪਣੀਆਂ ਵੱਖ-ਵੱਖ ਹਾਰਡਵੇਅਰ ਯੰਤਰਾਂ ਵਿੱਚ E2E ਹੱਲ ਕਿਵੇਂ ਬਣਾਏ ਜਾਣ। ਆਪਣੇ ਲਈ Phi ਦਾ ਅਨੁਭਵ ਕਰਨ ਲਈ, ਮਾਡਲ ਨਾਲ ਖੇਡਣਾ ਸ਼ੁਰੂ ਕਰੋ ਅਤੇ [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਆਪਣੇ ਮਾਮਲਿਆਂ ਲਈ Phi ਨੂੰ ਮੁਕਰਰ ਕਰੋ। ਤੁਸੀਂ ਹੋਰ ਜਾਣਕਾਰੀ ਲਈ [GitHub Model Catalog ਨਾਲ ਸ਼ੁਰੂਆਤ](/md/02.QuickStart/GitHubModel_QuickStart.md) ਵੇਖ ਸਕਦੇ ਹੋ।

**ਪਲੇਂਗ੍ਰਾਊਂਡ**  
ਹਰ ਮਾਡਲ ਲਈ ਇੱਕ ਸਮਰਪਿਤ [ਪਲੇਂਗ੍ਰਾਊਂਡ ਮਾਡਲ ਟੈਸਟ ਕਰਨ ਲਈ](/md/02.QuickStart/GitHubModel_QuickStart.md) ਹੈ।

### Hugging Face 'ਤੇ Phi

ਤੁਸੀਂ ਮਾਡਲ ਨੂੰ [Hugging Face](https://huggingface.co/microsoft) 'ਤੇ ਵੀ ਲੱਭ ਸਕਦੇ ਹੋ।

**ਪਲੇਂਗ੍ਰਾਊਂਡ**  
[Hugging Chat playground](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

 ## 🎒 ਹੋਰ ਕੋਰਸ

ਸਾਡੀ ਟੀਮ ਹੋਰ ਕੋਰਸ ਵੀ ਤਿਆਰ ਕਰਦੀ ਹੈ! ਚੈੱਕ ਕਰੋ:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain  
[![LangChain4j ਸ਼ੁਰੂਆਤ ਲਈ](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)  
[![LangChain.js ਸ਼ੁਰੂਆਤ ਲਈ](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)  
[![LangChain ਸ਼ੁਰੂਆਤ ਲਈ](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)  
---

### Azure / Edge / MCP / ਏਜੰਟ  
[![AZD ਸ਼ੁਰੂਆਤ ਲਈ](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)  
[![Edge AI ਸ਼ੁਰੂਆਤ ਲਈ](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)  
[![MCP ਸ਼ੁਰੂਆਤ ਲਈ](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)  
[![AI ਏਜੰਟ ਸ਼ੁਰੂਆਤ ਲਈ](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)  

---

### ਜਨਰੇਟਿਵ AI ਸੀਰੀਜ਼  
[![ਜਨਰੇਟਿਵ AI ਸ਼ੁਰੂਆਤ ਲਈ](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)  
[![ਜਨਰੇਟਿਵ AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)  
[![ਜਨਰੇਟਿਵ AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)  
[![ਜਨਰੇਟਿਵ AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)  

---

### ਮੁੱਖ ਸਿੱਖਿਆ  
[![ML ਸ਼ੁਰੂਆਤ ਲਈ](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)  
[![ਡਾਟਾ ਸਾਇੰਸ ਸ਼ੁਰੂਆਤ ਲਈ](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)  
[![AI ਸ਼ੁਰੂਆਤ ਲਈ](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)  
[![ਸਾਈਬਰਸੁਰੱਖਿਆ ਸ਼ੁਰੂਆਤ ਲਈ](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)  
[![ਵੈੱਬ ਡਿਵੈਲਪਮੈਂਟ ਸ਼ੁਰੂਆਤ ਲਈ](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)  
[![IoT ਸ਼ੁਰੂਆਤ ਲਈ](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)  
[![XR ਵਿਕਾਸ ਸ਼ੁਰੂਆਤ ਲਈ](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)  

---

### ਕੋਪਾਇਲਟ ਸੀਰੀਜ਼  
[![AI ਜੋੜੇ ਪ੍ਰੋਗਰਾਮਿੰਗ ਲਈ ਕੋਪਾਇਲਟ](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)  
[![C#/.NET ਲਈ ਕੋਪਾਇਲਟ](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)  
[![ਕੋਪਾਇਲਟ ਐਡਵੈਂਚਰ](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)  
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## ਜ਼ਿੰਮੇਵਾਰ AI

ਮਾਈਕ੍ਰੋਸਾਫਟ ਇਸ ਗੱਲ ਦਾ ਵਚਨਬੱਧ ਹੈ ਕਿ ਸਾਡੇ ਗਾਹਕ ਸਾਡੇ AI ਉਤਪਾਦਾਂ ਨੂੰ ਜ਼ਿੰਮੇਵਾਰੀ ਨਾਲ ਵਰਤਣ ਵਿੱਚ ਸਹਾਇਤਾ ਪ੍ਰਦਾਨ ਕਰੇ, ਆਪਣੇ ਅਨੁਭਵ ਸਾਂਝੇ ਕਰੇ, ਅਤੇ ਟਰਾਂਸਪਰੈਂਸੀ ਨੋਟਸ ਅਤੇ ਇੰਪੈਕਟ ਐਸੈਸਮੈਂਟ ਵਰਗੇ ਉਪਕਰਣਾਂ ਰਾਹੀਂ ਭਰੋਸੇਮੰਦ ਭਾਈਚਾਰਿਆਂ ਦੀ ਰਚਨਾ ਕਰੇ। ਇਹਨਾਂ ਵਿੱਚੋਂ ਬਹੁਤ ਸਾਰੇ ਸਰੋਤ [https://aka.ms/RAI](https://aka.ms/RAI) 'ਤੇ ਲੱਭੇ ਜਾ ਸਕਦੇ ਹਨ।  
ਮਾਈਕ੍ਰੋਸਾਫਟ ਦਾ ਜ਼ਿੰਮੇਵਾਰ AI ਲਈ ਰਵੱਈਆ ਸਾਡੀਆਂ ਨਿਆਇਕਤਾ, ਭਰੋਸੇਯੋਗਤਾ ਅਤੇ ਸੁਰੱਖਿਆ, ਗੋਪनीयਤਾ ਅਤੇ ਸੁਰੱਖਿਆ, ਸਮਾਵੇਸ਼ਤਾ, ਪਾਰਦਰਸ਼ਤਾ, ਅਤੇ ਜ਼ਿੰਮੇਵਾਰੀ ਵਾਲੀਆਂ AI ਸਿਧਾਂਤਾਂ 'ਤੇ ਆਧਾਰਤ ਹੈ।

ਵੱਡੇ ਪੱਧਰ ਦੇ ਕੁਦਰਤੀ ਭਾਸ਼ਾ, ਚਿੱਤਰ ਅਤੇ ਬੋਲੀ ਮਾਡਲ - ਜਿਵੇਂ ਕਿ ਇਸ ਨਮੂਨੇ ਵਿੱਚ ਵਰਤੇ ਗਏ ਹਨ - ਸੰਭਾਵਤ ਤੌਰ 'ਤੇ ਅਨਿਆਇਕ, ਅਭਰੋਸੇਯੋਗ, ਜਾਂ ਅਪਮਾਨਜਨਕ ਵਿਹਾਰ ਕਰ ਸਕਦੇ ਹਨ, ਜਿਸ ਨਾਲ ਨੁਕਸਾਨ ਹੋ ਸਕਦਾ ਹੈ। ਕਿਰਪਾ ਕਰਕੇ [Azure OpenAI ਸੇਵਾ ਟਰਾਂਸਪਰੈਂਸੀ ਨੋਟ](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) ਨੂੰ ਦੇਖੋ ਤਾਂ ਜੋ ਖਤਰਿਆਂ ਅਤੇ ਸੀਮਾਵਾਂ ਬਾਰੇ ਜਾਣਕਾਰੀ ਮਿਲ ਸਕੇ।

ਇਨ੍ਹਾਂ ਖਤਰਿਆਂ ਨੂੰ ਘਟਾਉਣ ਦਾ ਸੁਪਾਰਸ਼ੀਤ ਤਰੀਕਾ ਹੈ ਆਪਣੇ ਆਰਕੀਟੈਕਚਰ ਵਿੱਚ ਇੱਕ ਸੁਰੱਖਿਆ ਪ੍ਰਣਾਲੀ ਸ਼ਾਮਲ ਕਰਨਾ ਜੋ ਨੁਕਸਾਨਦਾਇਕ ਵਿਹਾਰ ਦੀ ਪਛਾਣ ਅਤੇ ਰੋਕਥਾਮ ਕਰ ਸਕੇ। [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) ਇੱਕ ਖੁਦਮੁਖਤਾਰ ਸੁਰੱਖਿਆ ਪਰਤ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ, ਜੋ ਦਰਖ਼ਤੀਆਂ ਅਤੇ AI-ਨਿਰਮਿਤ ਸਮੱਗਰੀ ਦੀ ਪਛਾਣ ਅਤੇ ਰੋਕਣ ਯੋਗ ਹੈ। Azure AI Content Safety ਵਿੱਚ ਟੈਕਸਟ ਅਤੇ ਚਿੱਤਰ APIs ਸ਼ਾਮਲ ਹਨ ਜੋ ਨੁਕਸਾਨਦਾਇਕ ਸਮੱਗਰੀ ਦੀ ਪਛਾਣ ਕਰਦੇ ਹਨ। Azure AI Foundry ਵਿਚ, Content Safety ਸੇਵਾ ਤੁਹਾਨੂੰ ਵੱਖ-ਵੱਖ ਮਾਡਾਲਿਟੀਜ਼ ਵਿੱਚ ਨੁਕਸਾਨਦਾਇਕ ਸਮੱਗਰੀ ਦੀ ਪਛਾਣ ਲਈ ਨਮੂਨਾ ਕੋਡ ਵੇਖਣ, ਖੰਗਾਲਣ ਅਤੇ ਕੋਸ਼ਿਸ਼ ਕਰਨ ਦੀ ਆਗਿਆ ਦਿੰਦੀ ਹੈ। ਹੇਠਾਂ ਦਿੱਤੀ [ਕੁਇਕਸਟਾਰਟ ਡੌਕੁਮੇੰਟੇਸ਼ਨ](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) ਤੁਹਾਨੂੰ ਸੇਵਾ ਨੂੰ ਵਿੰਨਤੀਆਂ ਕਰਨ ਦੇ ਲਈ ਮਾਰਗਦਰਸ਼ਨ ਕਰਦੀ ਹੈ।
ਹੋਰ ਇੱਕ ਪੱਖ ਜੋ ਧਿਆਨ ਵਿੱਚ ਲੈਣਾ ਜਰੂਰੀ ਹੈ ਉਹ ਹੈ ਕੁੱਲ ਐਪਲੀਕੇਸ਼ਨ ਪ੍ਰਦਰਸ਼ਨ। ਬਹੁ-ਮੋਡਲ ਅਤੇ ਬਹੁ-ਮਾਡਲ ਐਪਲੀਕੇਸ਼ਨਾਂ ਵਿੱਚ, ਅਸੀਂ ਪ੍ਰਦਰਸ਼ਨ ਦੇ ਅਰਥ ਵਜੋਂ ਇਹ ਮੰਨਦੇ ਹਾਂ ਕਿ ਸਿਸਟਮ ਉਹੀ ਕਰਦਾ ਹੈ ਜੋ ਤੁਸੀਂ ਅਤੇ ਤੁਹਾਡੇ ਉਪਭੋਗਤਾ ਉਮੀਦ ਕਰਦੇ ਹੋ, ਜਿਸ ਵਿੱਚ ਨੁਕਸਾਨ ਪਹੁੰਚਾਉਣ ਵਾਲੇ ਨਤੀਜੇ ਨਹੀਂ ਬਣਾਉਣਾ ਸ਼ਾਮਲ ਹੈ। ਤੁਹਾਡੇ ਕੁੱਲ ਐਪਲੀਕੇਸ਼ਨ ਦੇ ਪ੍ਰਦਰਸ਼ਨ ਦੀ ਮਾਪ ਕਰਨ ਲਈ [Performance and Quality and Risk and Safety evaluators](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) ਦਾ ਇਸਤੇਮਾਲ ਕਰਨਾ ਮਹੱਤਵਪੂਰਣ ਹੈ। ਤੁਹਾਡੇ ਕੋਲ [custom evaluators](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators) ਬਣਾਉਣ ਅਤੇ ਮਾਪਣ ਦੀ ਵੀ ਸਮਰੱਥਾ ਹੈ।

ਤੁਸੀਂ ਆਪਣੇ ਵਿਕਾਸ ਦੇ ਵਾਤਾਵਰਣ ਵਿੱਚ [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਆਪਣੇ AI ਐਪਲੀਕੇਸ਼ਨ ਦਾ ਮੁਲਾਂਕਣ ਕਰ ਸਕਦੇ ਹੋ। ਚਾਹੇ ਇੱਕ ਟੈਸਟ ਡੇਟਾ ਸੈੱਟ ਹੋਵੇ ਜਾਂ ਇੱਕ ਟਾਰਗੇਟ, ਤੁਹਾਡੇ ਜਨਰੇਟਿਭ AI ਐਪਲੀਕੇਸ਼ਨ ਦੀਆਂ ਜਨਰੇਸ਼ਨਾਂ ਨੂੰ ਤੁਹਾਡੇ ਚੋਣ ਦੇ ਬਿਲਟ-ਇਨ ਜਾਂ ਕਸਟਮ ਮੁਲਾਂਕਣਕਾਰਾਂ ਨਾਲ ਮਾਤਰਾਤਮਕ ਤੌਰ 'ਤੇ ਮਾਪਿਆ ਜਾਂਦਾ ਹੈ। ਆਪਣੇ ਸਿਸਟਮ ਦਾ ਮੁਲਾਂਕਣ ਕਰਨ ਲਈ Azure AI Evaluation SDK ਦੇ ਨਾਲ ਸ਼ੁਰੂ ਕਰਨ ਲਈ, ਤੁਸੀਂ [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) ਦੀ ਪਾਲਣਾ ਕਰ ਸਕਦੇ ਹੋ। ਇੱਕ ਵਾਰੀ ਤੁਸੀਂ ਮੁਲਾਂਕਣ ਨੂੰ ਚਲਾ ਲੈਂਦੇ ਹੋ, ਤਾਂ ਤੁਸੀਂ ਨਤੀਜੇ [Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results) ਵਿੱਚ ਵੀਖ ਸਕਦੇ ਹੋ।

## ਟ੍ਰੇਡਮਾਰਕਸ

ਇਸ ਪਰੋਜੈਕਟ ਵਿੱਚ ਪ੍ਰੋਜੈਕਟਾਂ, ਉਤਪਾਦਾਂ ਜਾਂ ਸੇਵਾਵਾਂ ਲਈ ਟ੍ਰੇਡਮਾਰਕ ਜਾਂ ਲੋਗੋ ਸ਼ਾਮਲ ਹੋ ਸਕਦੇ ਹਨ। ਮਾਇਕਰੋਸੌਫਟ ਦੇ ਟ੍ਰੇਡਮਾਰਕ ਜਾਂ ਲੋਗੋਜ਼ ਦੀ ਅਧਿਕ੍ਰਿਤ ਵਰਤੋਂ [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) ਦੇ ਅਧੀਨ ਹੈ ਅਤੇ ਉਹਨਾਂ ਦੀ ਪਾਲਣਾ ਕਰਨੀ ਜਰੂਰੀ ਹੈ। ਇਸ ਪਰੋਜੈਕਟ ਦੇ ਬਦਲੇ ਹੋਏ ਸੰਸਕਰਣਾਂ ਵਿੱਚ ਮਾਇਕਰੋਸੌਫਟ ਦੇ ਟ੍ਰੇਡਮਾਰਕ ਜਾਂ ਲੋਗੋਜ਼ ਦੀ ਵਰਤੋਂ ਨਾਲ ਗਲਤਫਹਿਮੀ ਜਾਂ ਮਾਇਕਰੋਸੌਫਟ ਦੇ ਸਪਾਂਸਰਸ਼ਿਪ ਦਾ ਭਰਮ ਨਹੀਂ ਪੈਦਾ ਹੋਣਾ ਚਾਹੀਦਾ। ਕਿਸੇ ਵੀ ਤੀਜੇ ਪੱਖ ਦੇ ਟ੍ਰੇਡਮਾਰਕ ਜਾਂ ਲੋਗੋਜ਼ ਦੀ ਵਰਤੋਂ ਉਹਨਾਂ ਤੀਜਿਆਂ ਦੀਆਂ ਨੀਤੀਆਂ ਮੂਲ ਹੈ।

## ਮਦਦ ਪ੍ਰਾਪਤ ਕਰਨਾ

ਜੇਕਰ ਤੁਸੀਂ ਫਸ ਜਾਂਦੇ ਹੋ ਜਾਂ AI ਐਪ ਬਣਾਉਣ ਬਾਰੇ ਕੋਈ ਸਵਾਲ ਹੈ, ਤਾਂ ਸ਼ਾਮਿਲ ਹੋਵੋ:

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

ਜੇਕਰ ਤੁਹਾਡੇ ਕੋਲ ਪ੍ਰੋਡਕਟ ਫੀਡਬੈਕ ਹੈ ਜਾਂ ਬਣਾਉਂਦੇ ਸਮੇਂ ਕੋਈ ਫ਼ਰਕੁਲਤੀਆਂ ਹਨ ਤਾਂ ਜਾਓ:

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਤਸਦੀਕਈ ਰੱਦ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਨਾਲ ਅਨੁਵਾਦਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਟ੍ਰਿਵ ਕਰਦੇ ਹਾਂ ਕਿ ਅਨੁਵਾਦ ਸਹੀ ਹੋਵੇ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਆਟੋਮੈਟਿਕ ਅਨੁਵਾਦ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਤਰੁੱਟੀਆਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਇਸਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ ਪ੍ਰੋਫੈਸ਼ਨਲ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਿਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਭੁੱਲ-ਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਵਖਿਆ ਲਈ ਜਵਾਬਦੇਹ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->