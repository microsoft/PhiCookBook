# Phi ਕੂਕਬੁੱਕ: Microsoft ਦੇ Phi ਮਾਡਲਾਂ ਨਾਲ ਹੱਥ-ਅਨੁਭਵ ਉਦਾਹਰਨਾਂ

[![GitHub Codespaces ਵਿੱਚ ਸੈਂਪਲ ਖੋਲ੍ਹੋ ਅਤੇ ਵਰਤੋਂ ਕਰੋ](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![ਡੈਵ ਕੰਟੇਨਰਾਂ ਵਿੱਚ ਖੋਲ੍ਹੋ](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub ਯੋਗਦਾਨਕਾਰ](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub ਸਮੱਸਿਆਵਾਂ](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub ਪੁੱਲ-ਰਿਕਵੈਸਟ](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PRs ਦਾ ਸਵਾਗਤ ਹੈ](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub ਦੇਖਣ ਵਾਲੇ](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub ਫੋਰਕ](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub ਸਿਤਾਰੇ](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi ਮਾਇਕਰੋਸਾਫਟ ਵੱਲੋਂ ਵਿਕਸਤ ਖੁੱਲ੍ਹਾ ਸਰੋਤ ਏਆਈ ਮਾਡਲਾਂ ਦੀ ਇੱਕ ਸੀਰੀਜ਼ ਹੈ।

ਫਿਲਹਾਲ Phi ਸਭ ਤੋਂ ਸ਼ਕਤੀਸ਼ਾਲੀ ਅਤੇ ਲਾਭਕਾਰੀ ਛੋਟਾ ਭਾਸ਼ਾ ਮਾਡਲ (SLM) ਹੈ, ਜਿਸ ਦੇ ਬਹੁ-ਭਾਸ਼ਾ, ਤਰਕ, ਲਿਖਤ/ਚੈਟ ਜਨਰੇਸ਼ਨ, ਕੋਡਿੰਗ, ਚਿੱਤਰ, ਆਡੀਓ ਅਤੇ ਹੋਰ ਸੰਦਰਭਾਂ ਵਿੱਚ ਬਹੁਤ ਚੰਗੇ ਬੈਨਚਮਾਰਕ ਹਨ।

ਤੁਸੀਂ Phi ਨੂੰ ਕਲਾਉਡ ਜਾਂ ਏਜ ਡਿਵਾਈਸਾਂ 'ਤੇ ਡਿਪਲੌਇ ਕਰ ਸਕਦੇ ਹੋ, ਅਤੇ ਤੁਸੀਂ ਸੀਮਿਤ ਕੰਪਿਊਟਿੰਗ ਸ਼ਕਤੀ ਨਾਲ ਪੈਦਾ ਕਰਨ ਵਾਲੀਆਂ ਏਆਈ ਐਪਲੀਕੇਸ਼ਨਾਂ ਨੂੰ ਆਸਾਨੀ ਨਾਲ ਬਣਾਅ ਸਕਦੇ ਹੋ।

ਇਹ ਸਰੋਤ ਵਰਤਣਾ ਸ਼ੁਰੂ ਕਰਨ ਲਈ ਇਹ ਕਦਮ ਅਪਣਾਓ:
1. **ਰੇਪੋਜ਼ੀਟਰੀ ਨੂੰ ਫੋਰਕ ਕਰੋ**: Click [![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **ਰੇਪੋਜ਼ੀਟਰੀ ਨੂੰ ਕਲੋਨ ਕਰੋ**: `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**ਮਾਇਕਰੋਸਾਫਟ AI Discord ਕਮਿਉਨਿਟੀ ਵਿੱਚ ਸ਼ਾਮਲ ਹੋਵੋ ਅਤੇ ਮਾਹਿਰਾਂ ਅਤੇ ਹੋਰ ਵਿਕਾਸਕਾਰਾਂ ਨਾਲ ਮਿਲੋ**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/pa/cover.eb18d1b9605d754b.webp)

### 🌐 ਬਹੁ-ਭਾਸ਼ਾਈ ਸਹਾਇਤਾ

#### GitHub ਇੱਕਸ਼ਨ ਰਾਹੀਂ ਸਹਾਇਤਾਪ੍ਰਾਪਤ (ਆਟੋਮੈਟਿਕ ਅਤੇ ਸਦਾ ਤਾਜ਼ਾ)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](./README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **ਕਲੋਨ ਸਥਾਨਕ ਤੌਰ 'ਤੇ ਪ੍ਰਭਾਵਸ਼ਾਲੀ ਮੰਨਦੇ ਹੋ?**

> ਇਸ ਰੇਪੋ ਵਿੱਚ 50+ ਭਾਸ਼ਾ ਅਨੁਵਾਦ ਸ਼ਾਮਿਲ ਹਨ ਜੋ ਡਾਊਨਲੋਡ ਸਾਈਜ਼ ਨੂੰ ਕਾਫੀ ਵਧਾ ਦਿੰਦੇ ਹਨ। ਅਨੁਵਾਦਾਂ ਦੇ ਬਿਨਾਂ ਕਲੋਨ ਕਰਨ ਲਈ, sparse checkout ਵਰਤੋਂ ਕਰੋ:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/PhiCookBook.git
> cd PhiCookBook
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> ਇਹ ਤੁਹਾਨੂੰ ਕੋਰਸ ਪੂਰਾ ਕਰਨ ਲਈ ਸਾਰੀ ਲੋੜੀਂਦੀ ਚੀਜ਼਼ ਤੇਜ਼ ਡਾਊਨਲੋਡ ਨਾਲ ਦੇਂਦਾ ਹੈ।
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## ਸੂਚੀ ਸਿਰਲੇਖ

- ਪਰਿਚਯ
  - [Phi ਪਰਿਵਾਰ ਵਿੱਚ ਤੁਹਾਡੇ ਦਾ ਸਵਾਗਤ ਹੈ](./md/01.Introduction/01/01.PhiFamily.md)
  - [ਆਪਣੇ ਵਾਤਾਵਰਣ ਦੀ ਸੈਟਿੰਗ ਕਰਨਾ](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [ਮੁੱਖ ਟੈਕਨਾਲੋਜੀਆਂ ਨੂੰ ਸਮਝਣਾ](./md/01.Introduction/01/01.Understandingtech.md)
  - [Phi ਮਾਡਲਾਂ ਲਈ ਏਆਈ ਸੁਰੱਖਿਆ](./md/01.Introduction/01/01.AISafety.md)
  - [Phi ਹਾਰਡਵੇਅਰ ਸਹਾਇਤਾ](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [ਵਿਭਿੰਨ ਪਲੇਟਫਾਰਮਾਂ ’ਤੇ Phi ਮਾਡਲ ਅਤੇ ਉਪਲਬਧਤਾ](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Guidance-ai ਅਤੇ Phi ਦੀ ਵਰਤੋਂ](./md/01.Introduction/01/01.Guidance.md)
  - [GitHub ਮਾਰਕੀਟਪਲੇਸ ਮਾਡਲ](https://github.com/marketplace/models)
  - [Azure AI ਮਾਡਲ ਕੈਟਾਲੌਗ](https://ai.azure.com)

- ਵੱਖਰੇ ਵਾਤਾਵਰਣ ਵਿੱਚ Phi ਇੰਫਰਨਸ
    -  [Hugging face](./md/01.Introduction/02/01.HF.md)
    -  [GitHub ਮਾਡਲ](./md/01.Introduction/02/02.GitHubModel.md)
    -  [Azure AI Foundry ਮਾਡਲ ਕੈਟਾਲੌਗ](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [AI ਟੂਲਕਿਟ VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    -  [Foundry ਸਥਾਨਕ](./md/01.Introduction/02/07.FoundryLocal.md)

- Phi ਪਰਿਵਾਰ ਦਾ ਇੰਫਰਨਸ
    - [iOS ਵਿੱਚ Phi ਇੰਫਰਨਸ](./md/01.Introduction/03/iOS_Inference.md)
    - [Android ਵਿੱਚ Phi ਇੰਫਰਨਸ](./md/01.Introduction/03/Android_Inference.md)
    - [Jetson ਵਿੱਚ Phi ਇੰਫਰਨਸ](./md/01.Introduction/03/Jetson_Inference.md)
    - [ਏਆਈ ਪੀਸੀ ਵਿੱਚ Phi ਇੰਫਰਨਸ](./md/01.Introduction/03/AIPC_Inference.md)
    - [Apple MLX ਫਰੇਮਵਰਕ ਨਾਲ Phi ਇੰਫਰਨਸ](./md/01.Introduction/03/MLX_Inference.md)
    - [ਸਥਾਨਕ ਸਰਵਰ ਵਿੱਚ Phi ਇੰਫਰਨਸ](./md/01.Introduction/03/Local_Server_Inference.md)
    - [ਏਆਈ ਟੂਲਕਿਟ ਦੀ ਵਰਤੋਂ ਨਾਲ ਰਿਮੋਟ ਸਰਵਰ ਵਿੱਚ Phi ਇੰਫਰਨਸ](./md/01.Introduction/03/Remote_Interence.md)
    - [Rust ਨਾਲ Phi ਇੰਫਰਨਸ](./md/01.Introduction/03/Rust_Inference.md)
    - [ਸਥਾਨਕ ਵਿੱਚ Phi--Vision ਇੰਫਰਨਸ](./md/01.Introduction/03/Vision_Inference.md)
    - [Kaito AKS, Azure Containers ਨਾਲ Phi ਇੰਫਰਨਸ(ਅਧਿਕਾਰਿਕ ਸਹਾਇਤਾ)](./md/01.Introduction/03/Kaito_Inference.md)
-  [Phi ਪਰਿਵਾਰ ਦੀ ਕੁਆੰਟਿਫਾਈੰਗ](./md/01.Introduction/04/QuantifyingPhi.md)
    - [llama.cpp ਦੀ ਵਰਤੋਂ ਨਾਲ Phi-3.5 / 4 ਨੂੰ ਕੁਆੰਟਾਈਜ਼ ਕਰਨਾ](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [onnxruntime ਲਈ ਜਨਰੇਟਿਵ ਏਆਈ ਐਕਸਟੈਂਸ਼ਨ ਦੀ ਵਰਤੋਂ ਨਾਲ Phi-3.5 / 4 ਨੂੰ ਕੁਆੰਟਾਈਜ਼ ਕਰਨਾ](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Intel OpenVINO ਦੀ ਵਰਤੋਂ ਨਾਲ Phi-3.5 / 4 ਨੂੰ ਕੁਆੰਟਾਈਜ਼ ਕਰਨਾ](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Apple MLX ਫਰੇਮਵਰਕ ਦੀ ਵਰਤੋਂ ਨਾਲ Phi-3.5 / 4 ਨੂੰ ਕੁਆੰਟਾਈਜ਼ ਕਰਨਾ](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

-  Phi ਦਾ ਮੂਲਾਂਕਣ
    - [ਜਵਾਬਦੇਹ ਏਆਈ](./md/01.Introduction/05/ResponsibleAI.md)
    - [ਮੂਲਾਂਕਣ ਲਈ Azure AI Foundry](./md/01.Introduction/05/AIFoundry.md)
    - [ਮੂਲਾਂਕਣ ਲਈ Promptflow ਦੀ ਵਰਤੋਂ](./md/01.Introduction/05/Promptflow.md)
 
- Azure AI ਸੇਅਰਚ ਨਾਲ RAG
    - [Azure AI ਸੇਅਰਚ ਨਾਲ Phi-4-mini ਅਤੇ Phi-4-multimodal(RAG) ਦੀ ਵਰਤੋਂ ਕਿਵੇਂ ਕਰੀਏ](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Phi ਐਪਲੀਕੇਸ਼ਨ ਵਿਕਾਸ ਸੈਂਪਲ
  - ਲਿਖਤ ਅਤੇ ਚੈਟ ਐਪਲੀਕੇਸ਼ਨ
    - Phi-4 ਸੈਂਪਲ 🆕
      - [📓] [Phi-4-mini ONNX ਮਾਡਲ ਨਾਲ ਗੱਲਬਾਤ](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [ਲੋਕਲ ONNX ਮਾਡਲ .NET ਨਾਲ Phi-4 ਚੈਟ](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [ਸਮੈਂਟਿਕ ਕਰਨਲ ਦੀ ਵਰਤੋਂ ਕਰਦਿਆਂ Phi-4 ONNX ਨਾਲ .NET ਕਨਸੋਲ ਐਪ ਚੈਟ](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Phi-3 / 3.5 ਸੈਂਪਲ
      - [ਫ਼ਿਰੋਜ਼ਾ ਬਰਾਊਜ਼ਰ ਵਿੱਚ Phi3, ONNX ਰਨਟਾਈਮ ਵੈਬ ਅਤੇ WebGPU ਦੀ ਵਰਤੋਂ ਨਾਲ ਲੋਕਲ ਚੈਟਬੋਟ](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVino ਚੈਟ](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [ਮਲਟੀ ਮਾਡਲ - ਇੰਟਰਐਕਟਿਵ ਫਾਈ-3-ਮੀਨੀ ਅਤੇ ਓਪਨਏਆਈ ਵਿਸਪਰ](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [ਐਮਐਲਫਲੋ - ਐਮਐਲਫਲੋ ਨਾਲ ਫਾਈ-3 ਦੀ ਵਰਤੋਂ ਅਤੇ ਰੈਪਰ ਬਣਾਉਣਾ](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [ਮਾਡਲ ਅਪਟੀਮਾਈਜੇਸ਼ਨ - ਓਐਨਐਨਐਕਸ ਰਨਟਾਈਮ ਵੈੱਬ ਲਈ ਫਾਈ-3-ਮੀਨੀ ਮਾਡਲ ਨੂੰ ਓਲਿਵ ਨਾਲ ਕਿਵੇਂ ਅਪਟੀਮਾਈਜ਼ ਕਰਨਾ ਹੈ](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [ਫਾਈ-3 ਮੀਨੀ-4k-ਇੰਸਟ੍ਰਕਟ-ਓਐਨਐਨਐਕਸ ਨਾਲ WinUI3 ਐਪ](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      -[WinUI3 ਮਲਟੀ ਮਾਡਲ AI ਪਾਵਰਡ ਨੋਟਸ ਐਪ ਸਮਪਲ](https://github.com/microsoft/ai-powered-notes-winui3-sample)
      - [ਕਸਟਮ ਫਾਈ-3 ਮਾਡਲਾਂ ਨੂੰ ਪ੍ਰੌਂਪਟ ਫਲੋ ਨਾਲ ਫਾਈਨ-ਟਿਊਨ ਅਤੇ ਇੰਟੀਗ੍ਰੇਟ ਕਰੋ](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
      - [ਆਜ਼ੂਰ ਏਆਈ ਫਾਊਂਡਰੀ ਵਿੱਚ ਪ੍ਰੌਂਪਟ ਫਲੋ ਨਾਲ ਕਸਟਮ ਫਾਈ-3 ਮਾਡਲਾਂ ਨੂੰ ਫਾਈਨ-ਟਿਊਨ ਅਤੇ ਇੰਟੀਗ੍ਰੇਟ ਕਰੋ](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
      - [ਆਜ਼ੂਰ ਏਆਈ ਫਾਊਂਡਰੀ ਵਿੱਚ ਫਾਈਨ-ਟਿਊਨ ਕੀਤੇ ਫਾਈ-3 / ਫਾਈ-3.5 ਮਾਡਲ ਨੂੰ ਮਾਈਕ੍ਰੋਸਾਫਟ ਦੇ ਜ਼ਿੰਮੇਵਾਰ AI ਸਿਧਾਂਤਾਂ 'ਤੇ ਕੇਂਦਰਿਤ ਕਰਕੇ ਮੁਲਾਂਕਣ ਕਰੋ](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
      - [📓] [ਫਾਈ-3.5-ਮੀਨੀ-ਇੰਸਟ੍ਰਕਟ ਭਾਸ਼ਾ ਅਨੁਮਾਨ ਸਮਪਲ (ਚੀਨੀ/ਅੰਗਰੇਜ਼ੀ)](./md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
      - [ਫਾਈ-3.5-ਇੰਸਟ੍ਰਕਟ WebGPU RAG ਚੈਟਬੋਟ](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
      - [ਵਿੰਡੋਜ਼ GPU ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਫਾਈ-3.5-ਇੰਸਟ੍ਰਕਟ ONNX ਨਾਲ ਪ੍ਰੌਂਪਟ ਫਲੋ ਹੱਲ ਤਿਆਰ ਕਰਨਾ](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
      - [ਮਾਈਕ੍ਰੋਸਾਫਟ ਫਾਈ-3.5 ਟੀਐਫਲਾਈਟ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਐਂਡਰਾਇਡ ਐਪ ਬਣਾਉਣਾ](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
      - [ਸਥਾਨਕ ONNX ਫਾਈ-3 ਮਾਡਲ ਦੀ ਵਰਤੋਂ ਕਰਕੇ Q&A .NET ਉਦਾਹਰਨ Microsoft.ML.OnnxRuntime ਨਾਲ](../../md/04.HOL/dotnet/src/LabsPhi301)
      - [ਸੀਮਾਂਟਿਕ ਕਰਨਲ ਅਤੇ ਫਾਈ-3 ਨਾਲ ਕਨਸੋਲ ਚੈਟ .NET ਐਪ](../../md/04.HOL/dotnet/src/LabsPhi302)

  - ਆਜ਼ੂਰ ਏਆਈ ਇੰਫਰੈਂਸ SDK ਕੋਡ ਬੇਸਡ ਸਮਪਲ
    - ਫਾਈ-4 ਸਮਪਲ 🆕
      - [📓] [ਫਾਈ-4-ਮਲਟੀਮੋਡਲ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਪ੍ਰੋਜੈਕਟ ਕੋਡ ਬਣਾਓ](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
    - ਫਾਈ-3 / 3.5 ਸਮਪਲ
      - [ਮਾਈਕ੍ਰੋਸਾਫਟ ਫਾਈ-3 ਫੈਮਿਲੀ ਨਾਲ ਆਪਣਾ ਵਿਜੁਅਲ ਸਟੂਡੀਓ ਕੋਡ GitHub ਕੋਪਾਇਲਟ ਚੈਟ ਬਣਾਓ](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
      - [GitHub ਮਾਡਲਾਂ ਨਾਲ ਫਾਈ-3.5 ਵਰਤ ਕੇ ਆਪਣਾ ਵਿਜੁਅਲ ਸਟੂਡੀਓ ਕੋਡ ਚੈਟ ਕੋਪਾਇਲਟ ਏਜੰਟ ਬਣਾਓ](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

  - ਅੱਡਵਾਂਸਡ ਰੀਜਨਿੰਗ ਸਮਪਲ
    - ਫਾਈ-4 ਸਮਪਲ 🆕
      - [📓] [ਫਾਈ-4-ਮੀਨੀ-ਰੀਜਨਿੰਗ ਜਾਂ ਫਾਈ-4-ਰੀਜਨਿੰਗ ਸਮਪਲ](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
      - [📓] [ਮਾਈਕ੍ਰੋਸਾਫਟ ਓਲਿਵ ਨਾਲ ਫਾਈ-4-ਮੀਨੀ-ਰੀਜਨਿੰਗ ਦਾ ਫਾਈਨ-ਟਿਊਨਿੰਗ](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [ਐਪਲ MLX ਨਾਲ ਫਾਈਨ-ਟਿਊਨਿੰਗ ਫਾਈ-4-ਮੀਨੀ-ਰੀਜਨਿੰਗ](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [GitHub ਮਾਡਲਾਂ ਨਾਲ ਫਾਈ-4-ਮੀਨੀ-ਰੀਜਨਿੰਗ](./md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
      - [📓] [ਆਜ਼ੂਰ ਏਆਈ ਫਾਊਂਡਰੀ ਮਾਡਲਾਂ ਨਾਲ ਫਾਈ-4-ਮੀਨੀ-ਰੀਜਨਿੰਗ](./md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
  - ਡੈਮੋ
      - [ਫਾਈ-4-ਮੀਨੀ ਡੈਮੋ ਹੱਗਿੰਗ ਫੇਸ ਸਪੇਸز 'ਤੇ ਹੋਸਟ ਕੀਤੇ ਗਏ](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
      - [ਫਾਈ-4-ਮਲਟੀਮੋਡਲ ਡੈਮੋ ਹੱਗਿੰਗ ਫੇਸ ਸਪੇਸਜ਼ 'ਤੇ ਹੋਸਟ ਕੀਤੇ ਗਏ](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
  - ਵਿਜ਼ਨ ਸਮਪਲ
    - ਫਾਈ-4 ਸਮਪਲ 🆕
      - [📓] [ਫਾਈ-4-ਮਲਟੀਮੋਡਲ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਚਿੱਤਰ ਪੜ੍ਹੋ ਅਤੇ ਕੋਡ ਜੈਨਰੇਟ ਕਰੋ](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
    - ਫਾਈ-3 / 3.5 ਸਮਪਲ
      -  [📓][ਫਾਈ-3-ਵਿਜ਼ਨ-ਚਿੱਤਰ ਟੈਕਸਟ ਤੋਂ ਟੈਕਸਟ](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [ਫਾਈ-3-ਵਿਜ਼ਨ-ਓਐਨਐਨਐਕਸ](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
      - [📓][ਫਾਈ-3-ਵਿਜ਼ਨ ਸੀਐਲਆਈਪੀ ਐਂਬੈਡਿੰਗ](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [ਡੈਮੋ: ਫਾਈ-3 ਰੀਸਾਈਕਲਿੰਗ](https://github.com/jennifermarsman/PhiRecycling/)
      - [ਫਾਈ-3-ਵਿਜ਼ਨ - ਦ੍ਰਿਸ਼ਟੀ ਭਾਸ਼ਾ ਸਹਾਇਕ - ਫਾਈ3-ਵਿਜ਼ਨ ਅਤੇ ਓਪਨਵਾਈਨੋ ਨਾਲ](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
      - [ਫਾਈ-3 ਵਿਜ਼ਨ ਨਵਿਡੀਆ NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
      - [ਫਾਈ-3 ਵਿਜ਼ਨ ਓਪਨਵਾਈਨੋ](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
      - [📓][ਫਾਈ-3.5 ਵਿਜ਼ਨ ਮਲਟੀ-ਫਰੇਮ ਜਾਂ ਮਲਟੀ-ਚਿੱਤਰ ਸਮਪਲ](./md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
      - [ਮਾਈਕ੍ਰੋਸਾਫਟ.ML.OnnxRuntime .NET ਵਰਤ ਕੇ ਫਾਈ-3 ਵਿਜ਼ਨ ਸਥਾਨਕ ONNX ਮਾਡਲ](../../md/04.HOL/dotnet/src/LabsPhi303)
      - [ਮੈਨੂ ਆਧਾਰਿਤ ਫਾਈ-3 ਵਿਜ਼ਨ ਸਥਾਨਕ ONNX ਮਾਡਲ Microsoft.ML.OnnxRuntime .NET ਨਾਲ](../../md/04.HOL/dotnet/src/LabsPhi304)

  - ਗਣਿਤ ਸਮਪਲ
    -  ਫਾਈ-4-ਮੀਨੀ-ਫਲੈਸ਼-ਰੀਜਨਿੰਗ-ਇੰਸਟ੍ਰਕਟ ਸਮਪਲ 🆕 [ਫਾਈ-4-ਮੀਨੀ-ਫਲੈਸ਼-ਰੀਜਨਿੰਗ-ਇੰਸਟ੍ਰਕਟ ਨਾਲ ਗਣਿਤ ਡੈਮੋ](./md/02.Application/09.Math/MathDemo.ipynb)

  - ਆਡੀਓ ਸਮਪਲ
    - ਫਾਈ-4 ਸਮਪਲ 🆕
      - [📓] [ਫਾਈ-4-ਮਲਟੀਮੋਡਲ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਆਡੀਓ ਟ੍ਰਾਂਸਕ੍ਰਿਪਟਸ ਨਿਕਾਲਣਾ](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
      - [📓] [ਫਾਈ-4-ਮਲਟੀਮੋਡਲ ਆਡੀਓ ਸਮਪਲ](./md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
      - [📓] [ਫਾਈ-4-ਮਲਟੀਮੋਡਲ ਸਪੀਚ ਟ੍ਰਾਂਸਲੇਸ਼ਨ ਸਮਪਲ](./md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
      - [.NET ਕਨਸੋਲ ਐਪਲੀਕੇਸ਼ਨ ਜੋ ਫਾਈ-4-ਮਲਟੀਮੋਡਲ ਆਡੀਓ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਆਡੀਓ ਫਾਇਲ ਦਾ ਵਿਸ਼ਲੇਸ਼ਣ ਕਰਦਾ ਹੈ ਅਤੇ ਟ੍ਰਾਂਸਕ੍ਰਿਪਟ ਬਣਾਉਂਦਾ ਹੈ](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

  - MOE ਸਮਪਲ
    - ਫਾਈ-3 / 3.5 ਸਮਪਲ
      - [📓] [ਫਾਈ-3.5 ਮਿਕਸਚਰ ਆਫ ਐਕਸਪੋਰਟਸ ਮਾਡਲ (MoEs) ਸੋਸ਼ਲ ਮੀਡੀਆ ਸਮਪਲ](./md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
      - [📓] [NVIDIA NIM ਫਾਈ-3 MOE, ਆਜ਼ੂਰ ਏਆਈ ਸਰਚ ਅਤੇ ਲਾਮਾ ਇੰਡੈਕਸ ਨਾਲ ਰੀਟਰੀਵਲ-ਆਗਮੇਂਟਡ ਜੇਨੇਰੇਸ਼ਨ (RAG) ਪਾਈਪਲਾਈਨ ਬਣਾਉਣਾ](./md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)
      - 
  - ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਸਮਪਲ
    - ਫਾਈ-4 ਸਮਪਲ 🆕
      -  [📓] [ਫਾਈ-4-ਮੀਨੀ ਨਾਲ ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਦੀ ਵਰਤੋਂ](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
      -  [📓] [ਫਾਈ-4-ਮੀਨੀ ਨਾਲ ਮਲਟੀ-ਏਜੰਟ ਬਣਾਉਣ ਲਈ ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਦੀ ਵਰਤੋਂ](./md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
      -  [📓] [ਓਲਾਮਾ ਨਾਲ ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਦੀ ਵਰਤੋਂ](./md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
      -  [📓] [ONNX ਨਾਲ ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਦੀ ਵਰਤੋਂ](./md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)
  - ਮਲਟੀਮੋਡਲ ਮਿਕਸਿੰਗ ਸਮਪਲ
    - ਫਾਈ-4 ਸਮਪਲ 🆕
      -  [📓] [ਫਾਈ-4-ਮਲਟੀਮੋਡਲ ਨੂੰ ਟੈਕਨੋਲੋਜੀ ਪੱਤਰਕਾਰ ਵਜੋਂ ਵਰਤਣਾ](./md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
      - [.NET ਕਨਸੋਲ ਐਪਲੀਕੇਸ਼ਨ ਜੋ ਫਾਈ-4-ਮਲਟੀਮੋਡਲ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਚਿੱਤਰਾਂ ਦਾ ਵਿਸ਼ਲੇਸ਼ਣ ਕਰਦਾ ਹੈ](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- ਫਾਈਨ-ਟਿਊਨਿੰਗ ਫਾਈ ਸਮਪਲ
  - [ਫਾਈਨ-ਟਿਊਨਿੰਗ ਸਨੇਰੀਓਜ਼](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [ਫਾਈਨ-ਟਿਊਨਿੰਗ ਬਨਾਮ RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [ਫਾਈਨ-ਟਿਊਨਿੰਗ ਨਾਲ ਫਾਈ-3 ਨੂੰ ਉਦਯੋਗਕ ਮਹਿਰ ਬਣਾਓ](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [VS ਕੋਡ ਲਈ AI ਟੂਲਕਿਟ ਨਾਲ ਫਾਈ-3 ਦੀ ਫਾਈਨ-ਟਿਊਨਿੰਗ](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [ਆਜ਼ੂਰ ਮਸ਼ੀਨ ਲਰਨਿੰਗ ਸਰਵਿਸ ਨਾਲ ਫਾਈ-3 ਦੀ ਫਾਈਨ-ਟਿਊਨਿੰਗ](./md/03.FineTuning/Introduce_AzureML.md)
  - [ਲੋਰਾ ਨਾਲ ਫਾਈ-3 ਦੀ ਫਾਈਨ-ਟਿਊਨਿੰਗ](./md/03.FineTuning/FineTuning_Lora.md)
  - [ਕਿਊਲੋਰਾ ਨਾਲ ਫਾਈ-3 ਦੀ ਫਾਈਨ-ਟਿਊਨਿੰਗ](./md/03.FineTuning/FineTuning_Qlora.md)
  - [ਆਜ਼ੂਰ ਏਆਈ ਫਾਊਂਡਰੀ ਨਾਲ ਫਾਈ-3 ਦੀ ਫਾਈਨ-ਟਿਊਨਿੰਗ](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [ਆਜ਼ੂਰ ML CLI/SDK ਨਾਲ ਫਾਈ-3 ਦੀ ਫਾਈਨ-ਟਿਊਨਿੰਗ](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [ਮਾਈਕ੍ਰੋਸਾਫਟ ਓਲਿਵ ਨਾਲ ਫਾਈਨ-ਟਿਊਨਿੰਗ](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [ਮਾਈਕ੍ਰੋਸਾਫਟ ਓਲਿਵ ਹੈਂਡਸ-ਆਨ ਲੈਬ ਨਾਲ ਫਾਈਨ-ਟਿਊਨਿੰਗ](./md/03.FineTuning/olive-lab/readme.md)
  - [ਫਾਈ-3-ਵਿਜ਼ਨ ਨੂੰ ਵੇਟਸ ਐਂਡ ਬਾਈਅਸ ਨਾਲ ਫਾਈਨ-ਟਿਊਨਿੰਗ](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [ਐਪਲ MLX ਫ੍ਰੇਮਵਰਕ ਨਾਲ ਫਾਈ-3 ਦੀ ਫਾਈਨ-ਟਿਊਨਿੰਗ](./md/03.FineTuning/FineTuning_MLX.md)
  - [ਫਾਈ-3-ਵਿਜ਼ਨ (ਆਧਿਕਾਰਿਕ ਸਮਰਥਨ)](./md/03.FineTuning/FineTuning_Vision.md)
  - [ਕੇਇਟੋ AKS, ਆਜ਼ੂਰ ਕੰਟੇਨਰਾਂ ਨਾਲ ਫਾਈ-3 ਦੀ ਫਾਈਨ-ਟਿਊਨਿੰਗ (ਆਧਿਕਾਰਿਕ ਸਮਰਥਨ)](./md/03.FineTuning/FineTuning_Kaito.md)
  - [ਫਾਈ-3 ਅਤੇ 3.5 ਵਿਜ਼ਨ ਦੀ ਫਾਈਨ-ਟਿਊਨਿੰਗ](https://github.com/2U1/Phi3-Vision-Finetune)

- ਹੈਂਡਸ ਆਨ ਲੈਬ
  - [ਕੱਟਿੰਗ-ਏਜ ਮਾਡਲਾਂ ਦੀ ਖੋਜ: LLMs, SLMs, ਸਥਾਨਕ ਵਿਕਾਸ ਅਤੇ ਹੋਰ](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [NLP ਸਮਰੱਥਾ ਖੋਲ੍ਹਣਾ: ਮਾਈਕ੍ਰੋਸਾਫਟ ਓਲਿਵ ਨਾਲ ਫਾਈਨ-ਟਿਊਨਿੰਗ](https://github.com/azure/Ignite_FineTuning_workshop)

- ਅਕਾਦਮਿਕ ਅਨੁਸੰਧਾਨ ਕਾਗਜ਼ ਅਤੇ ਪ੍ਰਕਾਸ਼ਨ
  - [ਪਾਠਪੁਸਤਕ ਤੁਹਾਨੂੰ ਸਾਰਾ ਕੁਝ ਦਿੰਦੇ ਹਨ II: phi-1.5 ਤਕਨੀਕੀ ਰਿਪੋਰਟ](https://arxiv.org/abs/2309.05463)
  - [Phi-3 ਤਕਨੀਕੀ ਰਿਪੋਰਟ: ਤੁਹਾਡੇ ਫੋਨ 'ਤੇ ਸਥਾਨਕ ਤੌਰ 'ਤੇ ਬਹੁਤ ਯੋਗ ਭਾਸ਼ਾ ਮਾਡਲ](https://arxiv.org/abs/2404.14219)
  - [Phi-4 ਤਕਨੀਕੀ ਰਿਪੋਰਟ](https://arxiv.org/abs/2412.08905)
  - [Phi-4-Mini ਤਕਨੀਕੀ ਰਿਪੋਰਟ: ਮਿਸ਼ਰਨ-ਆਫ-ਲੋਰਾਸ ਰਾਹੀਂ ਕੰਪੈਕਟ ਪਰ ਤਾਕਤਵਰ ਬਹੁ-ਮਾਡਲ ਭਾਸ਼ਾ ਮਾਡਲ](https://arxiv.org/abs/2503.01743)
  - [ਵਾਹਨ-ਅੰਦਰ ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਲਈ ਛੋਟੇ ਭਾਸ਼ਾ ਮਾਡਲਾਂ ਦੀ ਅਪਟੀਮਾਈਜ਼ੇਸ਼ਨ](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) ਬਹੁ-ਚੋਣ ਪ੍ਰਸ਼ਨ ਉੱਤਰਣ ਲਈ PHI-3 ਦੀ ਫਾਈਨ-ਟਿਊਨਿੰਗ: ਵਿਧੀ, ਨਤੀਜੇ, ਅਤੇ ਚੁਣੌਤੀਆਂ](https://arxiv.org/abs/2501.01588)
  - [Phi-4-ਰਿਜਨਿੰਗ ਤਕਨੀਕੀ ਰਿਪੋਰਟ](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Phi-4-ਮਿਨੀ-ਰਿਜਨਿੰਗ ਤਕਨੀਕੀ ਰਿਪੋਰਟ](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## ਫਾਈ ਮਾਡਲਾਂ ਦੀ ਵਰਤੋਂ

### Azure AI Foundry 'ਤੇ ਫਾਈ

ਤੁਸੀਂ ਸਿੱਖ ਸਕਦੇ ਹੋ ਕਿ Microsoft Phi ਨੂੰ ਕਿਵੇਂ ਵਰਤਣਾ ਹੈ ਅਤੇ ਤੁਹਾਡੇ ਵੱਖ-ਵੱਖ ਹਾਰਡਵੇਅਰ ਡਿਵਾਈਸਾਂ ਵਿੱਚ E2E ਸੋਲੂਸ਼ਨ ਕਿਵੇਂ ਬਣਾਉਣੇ ਹਨ। ਖੁਦ ਫਾਈ ਦਾ ਅਨੁਭਵ ਕਰਨ ਲਈ, ਮਾਡਲਾਂ ਨਾਲ ਖੇਡਣਾ ਸ਼ੁਰੂ ਕਰੋ ਅਤੇ ਆਪਣੇ ਸਿਨਾਰਿਆਂ ਲਈ ਫਾਈ ਨੂੰ ਕਸਟਮਾਈਜ਼ ਕਰੋ [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai) ਦਾ ਉਪਯੋਗ ਕਰਦੇ ਹੋਏ। ਤੁਸੀਂ ਹੋਰ ਜਾਣਕਾਰੀ ਹਾਸਲ ਕਰ ਸਕਦੇ ਹੋ Getting Started with [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md)

**ਪਲੇਆਗ੍ਰਾਊਂਡ**
ਹਰ ਮਾਡਲ ਲਈ ਇੱਕ ਸਮਰਪਿਤ ਪਲੇਆਗ੍ਰਾਊਂਡ ਹੈ ਮਾਡਲ ਨੂੰ ਟੈਸਟ ਕਰਨ ਲਈ [Azure AI Playground](https://aka.ms/try-phi3)।

### GitHub ਮਾਡਲਾਂ 'ਤੇ ਫਾਈ

ਤੁਸੀਂ ਸਿੱਖ ਸਕਦੇ ਹੋ ਕਿ Microsoft Phi ਨੂੰ ਕਿਵੇਂ ਵਰਤਣਾ ਹੈ ਅਤੇ ਤੁਹਾਡੇ ਵੱਖ-ਵੱਖ ਹਾਰਡਵੇਅਰ ਡਿਵਾਈਸਾਂ ਵਿੱਚ E2E ਸੋਲੂਸ਼ਨ ਕਿਵੇਂ ਬਣਾਉਣੇ ਹਨ। ਖੁਦ ਫਾਈ ਦਾ ਅਨੁਭਵ ਕਰਨ ਲਈ, ਮਾਡਲ ਨਾਲ ਖੇਡਣਾ ਸ਼ੁਰੂ ਕਰੋ ਅਤੇ ਆਪਣੇ ਸਿਨਾਰਿਆਂ ਲਈ ਫਾਈ ਨੂੰ ਕਸਟਮਾਈਜ਼ ਕਰੋ [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) ਦਾ ਉਪਯੋਗ ਕਰਦੇ ਹੋਏ। ਤੁਸੀਂ ਹੋਰ ਜਾਣਕਾਰੀ ਹਾਸਲ ਕਰ ਸਕਦੇ ਹੋ Getting Started with [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md)

**ਪਲੇਆਗ੍ਰਾਊਂਡ**
ਹਰ ਮਾਡਲ ਲਈ ਇੱਕ ਸਮਰਪਿਤ [ਮਾਡਲ ਨੂੰ ਟੈਸਟ ਕਰਨ ਲਈ ਪਲੇਆਗ੍ਰਾਊਂਡ](/md/02.QuickStart/GitHubModel_QuickStart.md) ਹੈ।

### Hugging Face 'ਤੇ ਫਾਈ

ਤੁਸੀਂ ਮਾਡਲ ਨੂੰ [Hugging Face](https://huggingface.co/microsoft) 'ਤੇ ਵੀ ਲੱਭ ਸਕਦੇ ਹੋ।

**ਪਲੇਆਗ੍ਰਾਊਂਡ**
 [Hugging Chat ਪਲੇਆਗ੍ਰਾਊਂਡ](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

 ## 🎒 ਹੋਰ ਕੋਰਸز

ਸਾਡੀ ਟੀਮ ਹੋਰ ਕੋਰਸਜ਼ ਤਿਆਰ ਕਰਦੀ ਹੈ! ਦੇਖੋ:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### ਲੈੰਗਚੇਨ
[![LangChain4j for Beginners](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js for Beginners](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![LangChain for Beginners](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### Azure / Edge / MCP / Agents
[![AZD for Beginners](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI for Beginners](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP for Beginners](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Agents for Beginners](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### ਜਨੇਰੇਟਿਵ AI ਸੀਰੀਜ਼
[![Generative AI for Beginners](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generative AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generative AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generative AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### ਕੋਰ ਸਿਖਲਾਈ
[![ML for Beginners](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science for Beginners](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI for Beginners](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Cybersecurity for Beginners](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Web Dev for Beginners](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT for Beginners](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR Development for Beginners](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### ਕੋਪਾਇਲਟ ਸਿਰੀਜ਼
[![Copilot for AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## ਜ਼ਿੰਮੇਵਾਰ AI

Microsoft ਸਾਡੇ ਗ੍ਰਾਹਕਾਂ ਨੂੰ ਸਾਡੇ AI ਉਤਪਾਦਾਂ ਨੂੰ ਜ਼ਿੰਮੇਵਾਰੀ ਨਾਲ ਵਰਤਣ ਵਿੱਚ ਮਦਦ ਕਰਨ ਲਈ ਵਚਨਬੱਧ ਹੈ, ਆਪਣੇ ਸਿੱਖਿਆਂ ਨੂੰ ਸਾਂਝਾ ਕਰਨਾ, ਅਤੇ ਟਰਾਂਸਪੈਰੈਂਸੀ ਨੋਟਸ ਅਤੇ ਪ੍ਰਭਾਵ ਮੁਲਾਂਕਣ ਜਿਹੇ ਉਪਕਰਨਾਂ ਰਾਹੀਂ ਭਰੋਸੇ ਅਧਾਰਿਤ ਭਾਈਚਾਰੇ ਬਣਾਉਣਾ। ਇਹਨਾਂ ਵਿੱਚੋਂ ਬਹੁਤ ਸਾਰੇ ਸਰੋਤ [https://aka.ms/RAI](https://aka.ms/RAI) 'ਤੇ ਮਿਲ ਸਕਦੇ ਹਨ।
Microsoft ਦਾ ਜ਼ਿੰਮੇਵਾਰ AI ਲਈ ਦਰਿਸ਼ਟੀਕੋਣ ਸਾਡੇ  ਨਿਆਂ, ਭਰੋਸੇਯੋਗਤਾ ਅਤੇ ਸੁਰੱਖਿਆ, ਪਰਦੇਦਾਰੀ ਅਤੇ ਸੁਰੱਖਿਆ, ਸ਼ਾਮਿਲੀਅਤ, ਪਾਰਦਰਸ਼ੀਤਾ ਅਤੇ ਜ਼ਿੰਮੇਵਾਰੀ ਦੇ AI ਸਿਧਾਂਤਾਂ 'ਤੇ ਆਧਾਰਿਤ ਹੈ।

ਵੱਡੇ ਪੱਧਰ ਦੇ ਕੁਦਰਤੀ ਭਾਸ਼ਾ, ਚਿੱਤਰ ਅਤੇ ਭਾਸ਼ਣ ਮਾਡਲ - ਜਿਵੇਂ ਕਿ ਇਸ ਨਮੂਨੇ ਵਿੱਚ ਵਰਤੇ ਗਏ ਹਨ - ਸੰਭਵ ਤੌਰ 'ਤੇ ਅਨਿਆਂਸਪਦ, ਭਰੋਸੇਯੋਗ ਨਾ ਹੋਣਗੇ ਜਾਂ ਅਪਮਾਨਜਨਕ ਤਰੀਕੇ ਨਾਲ ਵਿਹਾਰ ਕਰ ਸਕਦੇ ਹਨ, ਜਿਸ ਨਾਲ ਨੁਕਸਾਨ ਹੋ ਸਕਦਾ ਹੈ। ਕਿਰਪਾ ਕਰਕੇ ਖਤਰੇ ਅਤੇ ਸੀਮਾਵਾਂ ਬਾਰੇ ਜਾਣਕਾਰੀ ਲਈ [Azure OpenAI ਸੇਵਾ ਟਰਾਂਸਪੈਰੈਂਸੀ ਨੋਟ](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) ਨੂੰ ਦੇਖੋ।

ਇਨ੍ਹਾਂ ਖਤਰਿਆਂ ਨੂੰ ਘਟਾਉਣ ਲਈ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਗਈ ਪદ્ધਤੀ ਹੈ ਕਿ ਆਪਣੀ ਆਰਕੀਟੈਕਚਰ ਵਿੱਚ ਇਕ ਸੁਰੱਖਿਆ ਪ੍ਰਣਾਲੀ ਸ਼ਾਮਿਲ ਕਰੋ ਜੋ ਹਾਨਿਕਾਰਕ ਵਿਹਾਰ ਦਾ ਪਤਾ ਲਗਾ ਸਕੇ ਅਤੇ ਰੋਕ ਸਕੇ। [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) ਇੱਕ ਸੁਤੰਤਰ ਸੁਰੱਖਿਆ ਪਰਤ ਮੁਹੱਈਆ ਕਰਦਾ ਹੈ, ਜੋ ਐਪਲੀਕੇਸ਼ਨਾਂ ਅਤੇ ਸੇਵਾਵਾਂ ਵਿੱਚ ਹਾਨਿਕਾਰਕ ਉਪਭੋਗਤਾ-ਜਨਰੇਟਡ ਅਤੇ AI-ਜਨਰੇਟਡ ਸਮੱਗਰੀ ਦਾ ਪਤਾ ਲਗਾਉਣ ਦੇ ਯੋਗ ਹੈ। Azure AI Content Safety ਵਿੱਚ ਲੇਖ ਅਤੇ ਚਿੱਤਰ ਏਪੀਆਈਜ਼ ਸ਼ਾਮਿਲ ਹਨ ਜਿਹੜੇ ਤੁਹਾਨੂੰ ਹਾਨਿਕਾਰਕ ਸਮੱਗਰੀ ਨੂੰ ਖੋਜਣ ਦੀ ਆਗਿਆ ਦਿੰਦੇ ਹਨ। Azure AI Foundry ਦੇ ਅੰਦਰ, Content Safety ਸੇਵਾ ਤੁਹਾਨੂੰ ਵੱਖ-ਵੱਖ ਮੋਡੈਲਿਟੀਆਂ ਵਿੱਚੋਂ ਹਾਨਿਕਾਰਕ ਸਮੱਗਰੀ ਦਾ ਪਤਾ ਲਗਾਉਣ ਲਈ ਨਮੂਨਾ ਕੋਡ ਦੇਖਣ, ਖੋਜਣ ਅਤੇ ਅਜ਼ਮਾਉਣ ਦੀ ਆਗਿਆ ਦਿੰਦੀ ਹੈ। ਹੇਠਾਂ ਦਿੱਤੀ [ਤੁਰੰਤ-ਸ਼ੁਰੂਆਤ ਡੌਕਯੂਮੈਂਟੇਸ਼ਨ](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) ਤੁਹਾਨੂੰ ਸੇਵਾ ਨੂੰ ਬੇਨਤੀ ਕਰਨ ਲਿਆਂ ਮਦਦ ਕਰਦੀ ਹੈ।
ਹੋਰ ਇੱਕ ਪਹਿਲੂ ਜਿਸ ਨੂੰ ਧਿਆਨ ਵਿੱਚ ਰੱਖਣਾ ਜਰੂਰੀ ਹੈ ਉਹ ਹੈ ਕੁੱਲ ਮਿਲਾ ਕੇ ਐਪਲੀਕੇਸ਼ਨ ਦੀ ਪ੍ਰਦਰਸ਼ਨਸ਼ੀਲਤਾ। ਮਲਟੀ-ਮੋਡਲ ਅਤੇ ਮਲਟੀ-ਮਾਡਲ ਐਪਲੀਕੇਸ਼ਨਾਂ ਦੇ ਨਾਲ, ਅਸੀਂ ਪ੍ਰਦਰਸ਼ਨ ਨੂੰ ਇਸ ਤਰ੍ਹਾਂ ਸਮਝਦੇ ਹਾਂ ਕਿ ਸਿਸਟਮ ਤੁਹਾਡੇ ਅਤੇ ਤੁਹਾਡੇ ਉਪਭੋਗਤਾਵਾਂ ਦੀ ਉਮੀਦਾਂ ਮੁਤਾਬਕ ਕੰਮ ਕਰਦਾ ਹੈ, ਜਿਸ ਵਿੱਚ ਨੁਕਸਾਨਦਾਇਕ ਨਤੀਜੇ ਨਾਹ ਬਣਾਉਣਾ ਵੀ ਸ਼ਾਮਲ ਹੈ। ਇਹ ਜਰੂਰੀ ਹੈ ਕਿ ਤੁਸੀਂ ਆਪਣੀ ਕੁੱਲ ਐਪਲੀਕੇਸ਼ਨ ਦੀ ਪ੍ਰਦਰਸ਼ਨਸ਼ੀਲਤਾ ਨੂੰ [Performance and Quality and Risk and Safety evaluators](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) ਨਾਲ ਮਾਪੋ। ਤੁਹਾਡੇ ਕੋਲ ਇਹ ਵੀ ਸਖਤ ਹੈ ਕਿ ਤੁਸੀਂ [custom evaluators](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators) ਨਾਲ ਬਣਾਉਣ ਅਤੇ ਮਾਪਣ ਕਰ ਸਕਦੇ ਹੋ।

ਤੁਸੀਂ [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਆਪਣੇ ਵਿਕਾਸ ਪ੍ਰਦਰਸ਼ਨ ਵਿੱਚ ਆਪਣੀ AI ਐਪਲੀਕੇਸ਼ਨ ਦਾ ਮੁਲਾਂਕਣ ਕਰ ਸਕਦੇ ਹੋ। ਚਾਹੇ ਤੁਸੀਂ ਕਿਸੇ ਟੈਸਟ ਡੇਟਾਸੇਟ ਜਾਂ ਟਾਰਗੇਟ ਨੂੰ ਧਿਆਨ ਵਿੱਚ ਰੱਖੋ, ਤੁਹਾਡੀ ਜਨਰੇਟਿਵ AI ਐਪਲੀਕੇਸ਼ਨ ਦੀ ਸਿਰਜਣਾ ਮਾਤਰਾਤਮਕ ਤੌਰ 'ਤੇ ਬਿਲਟ-ਇਨ ਇਵੈਲੂਏਟਰ ਜਾਂ ਤੁਹਾਡੇ ਚੋਣ ਵਾਲੇ ਕਸਟਮ ਇਵੈਲੂਏਟਰ ਨਾਲ ਮਾਪੀ ਜਾਂਦੀ ਹੈ। ਅਜ਼ੂਰ AI ਇਵੈਲੂਏਸ਼ਨ SDK ਨਾਲ ਆਪਣੀ ਸਿਸਟਮ ਦਾ ਮੁਲਾਂਕਣ ਸ਼ੁਰੂ ਕਰਨ ਲਈ, ਤੁਸੀਂ [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) ਦੀ ਪਾਲਣਾ ਕਰ ਸਕਦੇ ਹੋ। ਜਦੋਂ ਤੁਸੀਂ ਮੁਲਾਂਕਣ ਚਲਾਉਂਦੇ ਹੋ, ਤਾਂ ਤੁਸੀਂ [Azure AI Foundry ਵਿੱਚ ਨਤੀਜੇ ਵੇਖ ਸਕਦੇ ਹੋ](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results)। 

## ਟ੍ਰੇਡਮਾਰਕਸ

ਇਹ ਪ੍ਰੋਜੈਕਟ ਪ੍ਰੋਜੈਕਟਾਂ, ਉਤਪਾਦਾਂ ਜਾਂ ਸੇਵਾਵਾਂ ਲਈ ਟ੍ਰੇਡਮਾਰਕਸ ਜਾਂ ਲੋਗੋ ਸਮੇਤ ਹੋ ਸਕਦਾ ਹੈ। ਮਾਈਕ੍ਰੋਸੌਫਟ ਦੇ ਟ੍ਰੇਡਮਾਰਕਸ ਜਾਂ ਲੋਗੋ ਦੀ ਮੰਨੀ ਹੋਈ ਵਰਤੋਂ [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) ਦੇ ਅਧੀਨ ਹੋਵੇਗੀ ਅਤੇ ਇਸ ਦਾ ਪਾਲਣ ਕਰਨਾ ਜਰੂਰੀ ਹੈ। ਇਸ ਪ੍ਰੋਜੈਕਟ ਦੀ ਸੋਧੀ ਹੋਈ ਸੰਸਕਰਨਾਂ ਵਿੱਚ ਮਾਈਕ੍ਰੋਸੌਫਟ ਦੇ ਟ੍ਰੇਡਮਾਰਕਸ ਜਾਂ ਲੋਗੋ ਦੀ ਵਰਤੋਂ ਭ੍ਰਮ ਪੈਦਾ ਨਹੀਂ ਕਰਨੀ ਚਾਹੀਦੀ ਜਾਂ ਮਾਈਕ੍ਰੋਸੌਫਟ ਦੀ ਸਪਾਂਸਰਸ਼ਿਪ ਦਰਸਾਉਣੀ ਨਹੀਂ ਚਾਹੀਦੀ। ਤੀਜੀ ਪੱਖ ਦੇ ਟ੍ਰੇਡਮਾਰਕਸ ਜਾਂ ਲੋਗੋ ਦੀ ਕੋਈ ਵੀ ਵਰਤੋਂ ਉਸ ਤੀਜੀ ਪੱਖ ਦੀਆਂ ਨੀਤੀਆਂ ਦੇ ਅਧੀਨ ਹੈ।

## ਸਹਾਇਤਾ ਪ੍ਰਾਪਤ ਕਰੋ

ਜੇ ਤੁਸੀਂ ਅਟਕੇ ਹੋ ਜਾਂ AI ਐਪਸ ਬਣਾਉਣ ਬਾਰੇ ਕੋਈ ਸਵਾਲ ਹੈ, ਤਾਂ ਜੁੜੋ:

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

ਜੇ ਤੁਹਾਡੇ ਕੋਲ ਉਤਪਾਦ ਫੀਡਬੈਕ ਜਾਂ ਬਣਾਉਣ ਦੌਰਾਨ ਕੋਈ ਗਲਤੀ ਹੈ, ਤਾਂ ਜਾ ਕੇ ਵੇਖੋ:

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਰਦੇਸ਼**:  
ਇਹ ਦਸਤਾਵੇਜ਼ [Co-op Translator](https://github.com/Azure/co-op-translator) ਏਆਈ ਅਨੁਵਾਦ ਸੇਵਾ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਵਿੱਚ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮਰਥਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੇ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਹੀ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਪ੍ਰੋਫੈਸ਼ਨਲ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਦੁਭਾਵਾਂ ਲਈ ਜਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->