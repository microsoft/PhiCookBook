# Phi ਕੂਕਬੁੱਕ: Microsoft ਦੇ Phi ਮਾਡਲਾਂ ਨਾਲ ਹੱਥ-ਅਨੁਭਵ ਉਦਾਹਰਨਾਂ

[![GitHub Codespaces ਵਿੱਚ ਨਮੂਨੇ ਖੋਲ੍ਹੋ ਅਤੇ ਵਰਤੋਂ ਕਰੋ](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Dev Containers ਵਿੱਚ ਖੋਲ੍ਹੋ](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub ਯੋਗਦਾਨਕਾਰੀਆਂ](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub ਮੁੱਦੇ](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub ਪੁੱਲ-ਰੀਕਵੇਸਟ](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PRs ਸੁਆਗਤ ਹਨ](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub ਦੇਖਣ ਵਾਲੇ](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub ਫorks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub ਸਿਤਾਰੇ](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi ਇੱਕ ਖੁੱਲ੍ਹਾ ਸਰੋਤ AI ਮਾਡਲਾਂ ਦੀ ਲੜੀ ਹੈ ਜੋ Microsoft ਵਲੋਂ ਵਿਕਸਤ ਕੀਤੀ ਗਈ ਹੈ।

Phi ਇਸ ਸਮੇਂ ਸਭ ਤੋਂ ਸ਼ਕਤੀਸ਼ਾਲੀ ਅਤੇ ਲਾਗਤ-ਪ੍ਰਭਾਵਸ਼ਾਲੀ ਛੋਟਾ ਭਾਸ਼ਾ ਮਾਡਲ (SLM) ਹੈ, ਜਿਸ ਦੇ ਬਹੁਭਾਸ਼ੀ, ਤਰਕਸ਼ੀਲ, ਪਾਠ/ਚੈਟ ਉਤਪਾਦਨ, ਕੋਡਿੰਗ, ਚਿੱਤਰ, ਆਡੀਓ ਅਤੇ ਹੋਰ ਸਥਿਤੀਆਂ ਵਿੱਚ ਬਹੁਤ ਵਧੀਆ ਬੈਂਚਮਾਰਕ ਹਨ।

ਤੁਸੀਂ Phi ਨੂੰ ਕਲਾਊਡ ਜਾਂ ਏਜ ਡਿਵਾਈਸਾਂ ਤੇ ਤैनਾਤ ਕਰ ਸਕਦੇ ਹੋ, ਅਤੇ ਤੁਸੀਂ ਸੀਮਤ ਕੰਪਿਊਟਿੰਗ ਸ਼ਕਤੀ ਨਾਲ ਆਸਾਨੀ ਨਾਲ ਜੀਨਰੇਟਿਵ AI ਐਪਲੀਕੇਸ਼ਨਾਂ ਨੂੰ ਬਣਾਉਂ ਸਕਦੇ ਹੋ।

ਇਹ ਸਰੋਤ ਵਰਤਣ ਲਈ ਇਹ ਕਦਮ ਅਪਣਾਓ:
1. **ਰਿਪੋਜੇਟਰੀ ਨੂੰ ਫੋਰਕ ਕਰੋ**: ਕਲਿੱਕ ਕਰੋ [![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **ਰਿਪੋਜੇਟਰੀ ਨੂੰ ਕਲੋਨ ਕਰੋ**:   `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Microsoft AI Discord ਕਮਿਊਨਿਟੀ ਜੁੜੋ ਅਤੇ ਮਾਹਿਰਾਂ ਅਤੇ ਹੋਰ ਵਿਕਾਸਕਾਰਾਂ ਨਾਲ ਮਿਲੋ**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/pa/cover.eb18d1b9605d754b.webp)

### 🌐 ਬਹੁ-ਭਾਸ਼ਾ ਸਹਿਯੋਗ

#### GitHub Action ਰਾਹੀਂ ਸਮਰਥਿਤ (ਆਟੋਮੈਟਿਕ ਅਤੇ ਹਮੇਸ਼ਾਂ ਅੱਪਡੇਟ ਰਹਿਣ ਵਾਲਾ)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](./README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **ਸਥਾਨਕ ਤੌਰ 'ਤੇ ਕਲੋਨ ਕਰਨਾ ਵੱਧ ਪਸੰਦ ਹੈ?**
>
> ਇਹ ਰਿਪੋਜ਼ੀਟਰੀ 50+ ਭਾਸ਼ਾਈਆਂ ਦੇ ਅਨੁਵਾਦ ਸ਼ਾਮਲ ਕਰਦੀ ਹੈ ਜਿੰਨ੍ਹਾਂ ਕਾਰਨ ਡਾਊਨਲੋਡ ਸਾਈਜ਼ ਕਾਫੀ ਵੱਧ ਜਾਦਾ ਹੈ। ਬਿਨਾਂ ਅਨੁਵਾਦਾਂ ਦੇ ਕਲੋਨ ਕਰਨ ਲਈ, ਸਪਾਰਸ ਚੈੱਕਆਉਟ ਵਰਤੋਂ:
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
> ਇਸ ਨਾਲ ਤੁਹਾਨੂੰ ਕੋਰਸ ਪੂਰਾ ਕਰਨ ਲਈ ਸਭ ਕੁਝ ਬਹੁਤ ਤੇਜ਼ ਡਾਊਨਲੋਡ ਮਿਲੇਗਾ।
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## ਮਸੌਦਾ ਸੂਚੀ
- ਪਰਿਚਯ - [Phi ਪਰਿਵਾਰ ਵਿੱਚ ਤੁਹਾਡਾ ਸਵਾਗਤ ਹੈ](./md/01.Introduction/01/01.PhiFamily.md) - [ਆਪਣੇ ਵਾਤਾਵਰਣ ਨੂੰ ਸੈਟ ਕਰਨਾ](./md/01.Introduction/01/01.EnvironmentSetup.md) - [ਮੁੱਖ ਤਕਨਾਲੋਜੀਆਂ ਨੂੰ ਸਮਝਣਾ](./md/01.Introduction/01/01.Understandingtech.md) - [Phi ਮਾਡਲਾਂ ਲਈ AI ਸੁਰੱਖਿਆ](./md/01.Introduction/01/01.AISafety.md) - [Phi ਹਾਰਡਵੇਅਰ ਸਹਾਇਤਾ](./md/01.Introduction/01/01.Hardwaresupport.md) - [ਪਲੇਟਫਾਰਮਾਂ ਤੇ Phi ਮਾਡਲ ਅਤੇ ਉਪਲਬਧਤਾ](./md/01.Introduction/01/01.Edgeandcloud.md) - [Guidance-ai ਅਤੇ Phi ਦੀ ਵਰਤੋਂ](./md/01.Introduction/01/01.Guidance.md) - [GitHub Marketplace ਮਾਡਲ](https://github.com/marketplace/models) - [Azure AI ਮਾਡਲ ਕੈਟਾਲੋਗ](https://ai.azure.com) - ਵੱਖ-ਵੱਖ ਵਾਤਾਵਰਣ ਵਿੱਚ Phi ਦਾ ਨਿਰਣਯ - [Hugging face](./md/01.Introduction/02/01.HF.md) - [GitHub ਮਾਡਲ](./md/01.Introduction/02/02.GitHubModel.md) - [Microsoft Foundry ਮਾਡਲ ਕੈਟਾਲੋਗ](./md/01.Introduction/02/03.AzureAIFoundry.md) - [Ollama](./md/01.Introduction/02/04.Ollama.md) - [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md) - [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md) - [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md) - Phi ਪਰਿਵਾਰ ਵਿੱਚ ਨਿਰਣਯ - [iOS ਵਿੱਚ ਨਿਰਣਯ Phi](./md/01.Introduction/03/iOS_Inference.md) - [Android ਵਿੱਚ ਨਿਰਣਯ Phi](./md/01.Introduction/03/Android_Inference.md) - [Jetson ਵਿੱਚ ਨਿਰਣਯ Phi](./md/01.Introduction/03/Jetson_Inference.md) - [AI PC ਵਿੱਚ ਨਿਰਣਯ Phi](./md/01.Introduction/03/AIPC_Inference.md) - [Apple MLX ਫਰੇਮਵਰਕ ਨਾਲ ਨਿਰਣਯ Phi](./md/01.Introduction/03/MLX_Inference.md) - [ਲੋਕਲ ਸਰਵਰ ਵਿੱਚ ਨਿਰਣਯ Phi](./md/01.Introduction/03/Local_Server_Inference.md) - [AI Toolkit ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਦੂਰੇ ਸਰਵਰ ਵਿੱਚ ਨਿਰਣਯ Phi](./md/01.Introduction/03/Remote_Interence.md) - [Rust ਨਾਲ ਨਿਰਣਯ Phi](./md/01.Introduction/03/Rust_Inference.md) - [ਲੋਕਲ ਵਿੱਚ ਨਿਰਣਯ Phi--Vision](./md/01.Introduction/03/Vision_Inference.md) - [Kaito AKS, Azure Containers (ਅਧਿਕਾਰਿਕ ਸਹਾਇਤਾ) ਨਾਲ ਨਿਰਣਯ Phi](./md/01.Introduction/03/Kaito_Inference.md) - [Phi ਪਰਿਵਾਰ ਦੀ ਮਾਤਰਾ ਨਾਪਣਾ](./md/01.Introduction/04/QuantifyingPhi.md) - [llama.cpp ਦੀ ਵਰਤੋਂ ਕਰਕੇ Phi-3.5 / 4 ਨੂੰ ਪਰਿਮਾਣਕਿਤ ਕਰਨਾ](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md) - [onnxruntime ਲਈ ਜੇਨੇਰੇਟਿਵ AI ਐਕਸਟੇਂਸ਼ਨਜ਼ ਦੀ ਵਰਤੋਂ ਕਰਕੇ Phi-3.5 / 4 ਨੂੰ ਪਰਿਮਾਣਕਿਤ ਕਰਨਾ](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md) - [Intel OpenVINO ਦੀ ਵਰਤੋਂ ਕਰਕੇ Phi-3.5 / 4 ਨੂੰ ਪਰਿਮਾਣਕਿਤ ਕਰਨਾ](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md) - [Apple MLX ਫਰੇਮਵਰਕ ਦੀ ਵਰਤੋਂ ਕਰਕੇ Phi-3.5 / 4 ਨੂੰ ਪਰਿਮਾਣਕਿਤ ਕਰਨਾ](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md) - ਮੁਲਾਂਕਣ Phi - [ਜਵਾਬਦੇਹ AI](./md/01.Introduction/05/ResponsibleAI.md) - [ਮਾਇਕ੍ਰੋਸਾਫਟ Foundry ਲਈ ਮੁਲਾਂਕਣ](./md/01.Introduction/05/AIFoundry.md) - [ਮੁਲਾਂਕਣ ਲਈ Promptflow ਦੀ ਵਰਤੋਂ](./md/01.Introduction/05/Promptflow.md) - Azure AI Search ਨਾਲ RAG - [Azure AI Search ਨਾਲ Phi-4-mini ਅਤੇ Phi-4-multimodal(RAG) ਨੂੰ ਕਿਵੇਂ ਵਰਤਣਾ](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb) - Phi ਐਪਲੀਕੇਸ਼ਨ ਵਿਕਾਸ ਦੇ ਨਮੂਨੇ - ਟੈਕਸਟ & ਚੈਟ ਐਪਲੀਕੇਸ਼ਨ - Phi-4 ਨਮੂਨੇ - [📓] [Phi-4-mini ONNX ਮਾਡਲ ਨਾਲ ਚੈਟ ਕਰੋ](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md) - [ਥਾਣਾ ONNX ਮਾਡਲ ਨਾਲ Phi-4 ਸਥਾਨਕ ਚੈਟ .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) - [ਸੇਮੈਂਟਿਕ ਕਰਨਲ ਦੀ ਵਰਤੋਂ ਕਰਕੇ Phi-4 ONNX ਨਾਲ ਚੈਟ .NET ਕਨਸੋਲ ਐਪ](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) - Phi-3 / 3.5 ਨਮੂਨੇ - [ਫ਼ਾਇਰਫਾਕਸ ਵਿੱਚ ਸਥਾਨਕ ਚੈਟਬੋਟ Phi3, ONNX ਰਨটাইਮ ਵੈੱਬ ਅਤੇ WebGPU ਦੀ ਵਰਤੋਂ ਕਰਕੇ](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat) - [OpenVino ਚੈਟ](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md) - [ਬਹੁ-ਮਾਡਲ - ਇੰਟਰਐਕਟਿਵ Phi-3-mini ਅਤੇ OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md) - [MLFlow - ਇੱਕ ਰੈਪਰੀ ਬਣਾਉਣਾ ਅਤੇ Phi-3 ਨਾਲ MLFlow ਦੀ ਵਰਤੋਂ ਕਰਨਾ](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md) - [ਮਾਡਲ ਅਪਟੀਮਾਈਜ਼ੇਸ਼ਨ - ONNX Runtime ਵੈੱਬ ਨਾਲ Phi-3-mini ਮਾਡਲ ਅਪਟੀਮਾਈਜ਼ ਕਰਨ ਦਾ ਤਰੀਕਾ Olive ਦੀ ਵਰਤੋਂ ਕਰਕੇ](https://github.com/microsoft/Olive/tree/main/examples/phi3) - [Phi-3 mini-4k-instruct-onnx ਨਾਲ WinUI3 ਐਪ](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/) -[WinUI3 ਬਹੁ ਮਾਡਲ AI Powered ਨੋਟਸ ਐਪ ਨਮੂਨਾ](https://github.com/microsoft/ai-powered-notes-winui3-sample) - [Prompt flow ਨਾਲ ਕਸਟਮ Phi-3 ਮਾਡਲਾਂ ਨੂੰ ਫਾਈਨ-ਟਿਊਨ ਅਤੇ ਏਕੀਕ੍ਰਿਤ ਕਰੋ](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md) - [Microsoft Foundry ਵਿੱਚ Prompt flow ਨਾਲ ਕਸਟਮ Phi-3 ਮਾਡਲਾਂ ਨੂੰ ਫਾਈਨ-ਟਿਊਨ ਅਤੇ ਏਕੀਕ੍ਰਿਤ ਕਰੋ](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md) - [Microsoft ਦੇ ਜ਼ਿੰਮੇਵਾਰ AI ਸਿਧਾਂਤਾਂ 'ਤੇ ਧਿਆਨ ਦੇਦੇ ਹੋਏ Microsoft Foundry ਵਿੱਚ ਫਾਈਨ-ਟਿਊਨ ਕੀਤੇ Phi-3 / Phi-3.5 ਮਾਡਲ ਦਾ ਮੁਲਾਂਕਣ ਕਰੋ](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md) - [📓] [Phi-3.5-mini-instruct ਭਾਸ਼ਾ ਭਵਿੱਖਬਾਣੀ ਦਾ ਨਮੂਨਾ (ਚੀਨੀ/ਅੰਗਰੇਜ਼ੀ)](./md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb) - [Phi-3.5-Instruct WebGPU RAG ਚੈਟਬੋਟ](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md) - [Windows GPU ਦੀ ਵਰਤੋਂ ਕਰਕੇ Phi-3.5-Instruct ONNX ਨਾਲ Prompt flow ਸੁਝਾਅ ਬਣਾਉਣਾ](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md) - [Microsoft Phi-3.5 tflite ਦੀ ਵਰਤੋਂ ਕਰਕੇ Android ਐਪ ਬਣਾਉਣਾ](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md) - [ਸਥਾਨਕ ONNX Phi-3 ਮਾਡਲ ਦੀ ਵਰਤੋਂ ਕਰਕੇ Q&A .NET ਉਦਾਹਰਣ Microsoft.ML.OnnxRuntime ਦੀ ਵਰਤੋਂ ਕਰਦਾ ਹੈ](../../md/04.HOL/dotnet/src/LabsPhi301) - [ਸੇਮੈਂਟਿਕ ਕਰਨਲ ਅਤੇ Phi-3 ਨਾਲ ਕਨਸੋਲ ਚੈਟ .NET ਐਪ](../../md/04.HOL/dotnet/src/LabsPhi302) - Azure AI Inference SDK ਕੋਡ ਆਧਾਰਿਤ ਨਮੂਨੇ - Phi-4 ਨਮੂਨੇ - [📓] [Phi-4-multimodal ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਪ੍ਰੋਜੈਕਟ ਕੋਡ ਜਨਰੇਟ ਕਰੋ](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md) - Phi-3 / 3.5 ਨਮੂਨੇ - [ਆਪਣੇ ਮਾਇਕ੍ਰੋਸਾਫਟ Phi-3 ਪਰਿਵਾਰ ਨਾਲ ਆਪਣੇ ਵਿਜ਼ੂਅਲ ਸਟੂਡੀਓ ਕੋਡ GitHub ਕੋਪਾਇਲਟ ਚੈਟ ਬਣਾਓ](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md) - [GitHub ਮਾਡਲਾਂ ਨਾਲ Phi-3.5 ਨਾਲ ਆਪਣਾ ਵਿਜ਼ੂਅਲ ਸਟੂਡੀਓ ਕੋਡ ਚੈਟ ਕੋਪਾਇਲਟ ਏਜੰਟ ਬਣਾਓ](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md) - ਤਕਨੀਕੀ ਵਿਚਾਰਧਾਰਾ ਨਮੂਨੇ - Phi-4 ਨਮੂਨੇ - [📓] [Phi-4-mini-reasoning ਜਾਂ Phi-4-reasoning ਨਮੂਨੇ](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md) - [📓] [Microsoft Olive ਨਾਲ Phi-4-mini-reasoning ਨੂੰ ਫਾਈਨ-ਟਿਊਨ ਕਰਨਾ](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb) - [📓] [Apple MLX ਨਾਲ Phi-4-mini-reasoning ਨੂੰ ਫਾਈਨ-ਟਿਊਨ ਕਰਨਾ](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb) - [📓] [GitHub ਮਾਡਲਾਂ ਨਾਲ Phi-4-mini-reasoning](./md/02.Application/02.Code/Phi4r/github_models_inference.ipynb) - [📓] [Microsoft Foundry ਮਾਡਲਾਂ ਨਾਲ Phi-4-mini-reasoning](./md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb) -
ਡੈਮੋਜ਼ - [ਫਾਈ-4-ਮਿਨੀ ਡੈਮੋਜ਼ ਜੋ ਕਿ ਹੱਗਿੰਗ ਫੇਸ ਸਪੇਸز ਉੱਤੇ ਹੋਸਟ ਕੀਤੇ ਗਏ ਹਨ](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo) - [ਫਾਈ-4-ਮਲਟੀਮੋਡਲ ਡੈਮੋਜ਼ ਜੋ ਕਿ ਹੱਗਿੰਗ ਫੇਸ ਸਪੇਸਜ਼ ਉੱਤੇ ਹੋਸਟ ਕੀਤੇ ਗਏ ਹਨ](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo) - ਵਿਜ਼ਨ ਸੈਂਪਲਜ਼ - ਫਾਈ-4 ਸੈਂਪਲਜ਼ - [📓] [ਫਾਈ-4-ਮਲਟੀਮੋਡਲ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਚਿੱਤਰ ਪੜ੍ਹੋ ਅਤੇ ਕੋਡ ਤਿਆਰ ਕਰੋ](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) - ਫਾਈ-3 / 3.5 ਸੈਂਪਲਜ਼ - [📓][ਫਾਈ-3-ਵਿਜ਼ਨ-ਚਿੱਤਰ-ਪਾਠ ਤੋਂ ਪਾਠ](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb) - [ਫਾਈ-3-ਵਿਜ਼ਨ-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html) - [📓][ਫਾਈ-3-ਵਿਜ਼ਨ CLIP ਇੰਬੈੱਡਿੰਗ](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb) - [ਡੈਮੋ: ਫਾਈ-3 ਰੀਸਾਇਕਲਿੰਗ](https://github.com/jennifermarsman/PhiRecycling/) - [ਫਾਈ-3-ਵਿਜ਼ਨ - ਵਿਜ਼ੂਅਲ ਭਾਸ਼ਾ ਸਹਾਇਕ - ਫਾਈ-3-ਵਿਜ਼ਨ ਅਤੇ ਓਪਨਵਿਨੋ ਨਾਲ](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html) - [ਫਾਈ-3 ਵਿਜ਼ਨ ਨਿਵੀਡੀਆ NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md) - [ਫਾਈ-3 ਵਿਜ਼ਨ ਓਪਨਵਿਨੋ](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md) - [📓][ਫਾਈ-3.5 ਵਿਜ਼ਨ ਮਲਟੀ-ਫ੍ਰੇਮ ਜਾਂ ਮਲਟੀ-ਚਿੱਤਰ ਸੈਂਪਲ](./md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb) - [ਫਾਈ-3 ਵਿਜ਼ਨ ਲੋਕਲ ONNX ਮਾਡਲ Microsoft.ML.OnnxRuntime .NET ਨਾਲ ਵਰਤੋਂ ਕਰਕੇ](../../md/04.HOL/dotnet/src/LabsPhi303) - [ਮੇਨੂ ਆਧਾਰਿਤ ਫਾਈ-3 ਵਿਜ਼ਨ ਲੋਕਲ ONNX ਮਾਡਲ Microsoft.ML.OnnxRuntime .NET ਨਾਲ ਵਰਤੋਂ ਕਰਕੇ](../../md/04.HOL/dotnet/src/LabsPhi304) - ਰੀਜ਼ਨਿੰਗ-ਵਿਜ਼ਨ ਸੈਂਪਲਜ਼ - ਫਾਈ-4-ਰੀਜ਼ਨਿੰਗ-ਵਿਜ਼ਨ-15B - [📓] [ਫਾਈ-4-ਰੀਜ਼ਨਿੰਗ-ਵਿਜ਼ਨ-15B ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਜੇਵਾਕਿੰਗ ਨੂੰ ਪਛਾਣੋ](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_Jaywalking.ipynb) - [📓] [ਫਾਈ-4-ਰੀਜ਼ਨਿੰਗ-ਵਿਜ਼ਨ-15B ਨਾਲ ਗਣਿਤ ਕਰੋ](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_Math.ipynb) - [📓] [ਫਾਈ-4-ਰੀਜ਼ਨਿੰਗ-ਵਿਜ਼ਨ-15B ਨਾਲ UI ਪਛਾਣੋ](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_ui.ipynb) - ਗਣਿਤ ਸੈਂਪਲਜ਼ - ਫਾਈ-4-ਮਿਨੀ-ਫਲੈਸ਼-ਰੀਜ਼ਨਿੰਗ-ਇੰਸਟ੍ਰਕਟ ਸੈਂਪਲਜ਼ [ਫਾਈ-4-ਮਿਨੀ-ਫਲੈਸ਼-ਰੀਜ਼ਨਿੰਗ-ਇੰਸਟ੍ਰਕਟ ਨਾਲ ਗਣਿਤ ਡੈਮੋ](./md/02.Application/09.Math/MathDemo.ipynb) - ਆਡੀਓ ਸੈਂਪਲਜ਼ - ਫਾਈ-4 ਸੈਂਪਲਜ਼ - [📓] [ਫਾਈ-4-ਮਲਟੀਮੋਡਲ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਆਡੀਓ ਟਰਾਂਸਕ੍ਰਿਪਟ ਇੱਕਸਰਟ ਕਰਨਾ](./md/02.Application/05.Audio/Phi4/Transciption/README.md) - [📓] [ਫਾਈ-4-ਮਲਟੀਮੋਡਲ ਆਡੀਓ ਸੈਂਪਲ](./md/02.Application/05.Audio/Phi4/Siri/demo.ipynb) - [📓] [ਫਾਈ-4-ਮਲਟੀਮੋਡਲ ਸਪੀਚ ਅਨੁਵਾਦ ਸੈਂਪਲ](./md/02.Application/05.Audio/Phi4/Translate/demo.ipynb) - [.NET ਕੰਸੋਲ ਐਪਲੀਕੇਸ਼ਨ ਫਾਈ-4-ਮਲਟੀਮੋਡਲ ਆਡੀਓ ਦੀ ਵਰਤੋ ਕਰਕੇ ਆਡੀਓ ਫਾਈਲ ਦਾ ਵਿਸ਼ਲੇਸ਼ਣ ਅਤੇ ਟਰਾਂਸਕ੍ਰਿਪਟ ਤਿਆਰ ਕਰਨਾ](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) - MOE ਸੈਂਪਲਜ਼ - ਫਾਈ-3 / 3.5 ਸੈਂਪਲਜ਼ - [📓] [ਫਾਈ-3.5 ਮਿਕਸਚਰ ਆਫ ਐਕਸਪਰਟਸ ਮਾਡਲਜ਼ (MoEs) ਸੋਸ਼ਲ ਮੀਡੀਆ ਸੈਂਪਲ](./md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb) - [📓] [ਨਿਵੀਡੀਆ NIM ਫਾਈ-3 MOE, ਅਜ਼ੁਰ ਏਆਈ ਖੋਜ ਅਤੇ ਲਾਮਾ ਇੰਡੈਕਸ ਨਾਲ ਰੀਟ੍ਰੀਵਲ-ਆਗਮੈਂਟਡ ਜਨਰੇਸ਼ਨ (RAG) ਪਾਈਪਲਾਈਨ ਬਣਾਉਣਾ](./md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb) - - ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਸੈਂਪਲਜ਼ - ਫਾਈ-4 ਸੈਂਪਲਜ਼ 🆕 - [📓] [ਫਾਈ-4-ਮਿਨੀ ਨਾਲ ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਦੀ ਵਰਤੋਂ](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md) - [📓] [ਫਾਈ-4-ਮਿਨੀ ਨਾਲ ਮਲਟੀ-ਏਜੰਟ ਬਣਾਉਣ ਲਈ ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਦੀ ਵਰਤੋਂ](./md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb) - [📓] [ਓਲਾਮਾ ਨਾਲ ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਦੀ ਵਰਤੋਂ](./md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb) - [📓] [ONNX ਨਾਲ ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਦੀ ਵਰਤੋਂ](./md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb) - ਮਲਟੀਮੋਡਲ ਮਿਲਾਵਟ ਸੈਂਪਲਜ਼ - ਫਾਈ-4 ਸੈਂਪਲਜ਼ 🆕 - [📓] [ਫਾਈ-4-ਮਲਟੀਮੋਡਲ ਨੂੰ ਟੈਕਨੋਲੋਜੀ ਪੱਤਰਕਾਰ ਵਜੋਂ ਵਰਤਣਾ](./md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb) - [.NET ਕੰਸੋਲ ਐਪਲੀਕੇਸ਼ਨ ਫਾਈ-4-ਮਲਟੀਮੋਡਲ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਚਿੱਤਰਾਂ ਦਾ ਵਿਸ਼ਲੇਸ਼ਣ](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) - ਫਾਈ ਸੈਂਪਲਜ਼ ਫਾਈਨ-ਟਿਊਨਿੰਗ - [ਫਾਈਨ-ਟਿਊਨਿੰਗ ਦ੍ਰਿਸ਼](./md/03.FineTuning/FineTuning_Scenarios.md) - [ਫਾਈਨ-ਟਿਊਨਿੰਗ ਬਨਾਮ RAG](./md/03.FineTuning/FineTuning_vs_RAG.md) - [ਫਾਈਨ-ਟਿਊਨਿੰਗ ਫਾਈ-3 ਨੂੰ ਉਦਯੋਗ ਮੁਹਾਰਤ ਬਣਾਓ](./md/03.FineTuning/LetPhi3gotoIndustriy.md) - [ਫਾਈਨ-ਟਿਊਨਿੰਗ ਫਾਈ-3 AI ਟੂਲਕੀਟ ਫਾਰ VS ਕੋਡ ਨਾਲ](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md) - [ਫਾਈਨ-ਟਿਊਨਿੰਗ ਫਾਈ-3 ਅਜ਼ੁਰ ਮਸ਼ੀਨ ਲਰਨਿੰਗ ਸੇਵਾ ਨਾਲ](./md/03.FineTuning/Introduce_AzureML.md) - [ਫਾਈਨ-ਟਿਊਨਿੰਗ ਫਾਈ-3 ਲੋਰਾ ਨਾਲ](./md/03.FineTuning/FineTuning_Lora.md) - [ਫਾਈਨ-ਟਿਊਨਿੰਗ ਫਾਈ-3 ਕਿਊਲੋਰਾ ਨਾਲ](./md/03.FineTuning/FineTuning_Qlora.md) - [ਫਾਈਨ-ਟਿਊਨਿੰਗ ਫਾਈ-3 ਮਾਈਕ੍ਰੋਸਾਫਟ ਫਾਊਂਡਰੀ ਨਾਲ](./md/03.FineTuning/FineTuning_AIFoundry.md) - [ਫਾਈਨ-ਟਿਊਨਿੰਗ ਫਾਈ-3 ਅਜ਼ੁਰ ML CLI/SDK ਨਾਲ](./md/03.FineTuning/FineTuning_MLSDK.md) - [ਮਾਈਕ੍ਰੋਸਾਫਟ ਓਲਿਵ ਨਾਲ ਫਾਈਨ-ਟਿਊਨਿੰਗ](./md/03.FineTuning/FineTuning_MicrosoftOlive.md) - [ਮਾਈਕ੍ਰੋਸਾਫਟ ਓਲਿਵ ਹੈਂਡਸ-ਆਨ ਲੈਬ ਨਾਲ ਫਾਈਨ-ਟਿਊਨਿੰਗ](./md/03.FineTuning/olive-lab/readme.md) - [ਫਾਈਨ-ਟਿਊਨਿੰਗ ਫਾਈ-3-ਵਿਜ਼ਨ ਵਿਕਸਿਤ ਚਰਮ ਅਤੇ ਪੱਖ](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md) - [ਫਾਈਨ-ਟਿਊਨਿੰਗ ਫਾਈ-3 ਐਪਲ MLX ਫਰੇਮਵਰਕ ਨਾਲ](./md/03.FineTuning/FineTuning_MLX.md) - [ਫਾਈਨ-ਟਿਊਨਿੰਗ ਫਾਈ-3-ਵਿਜ਼ਨ (ਸਰਕਾਰੀ ਸਹਾਇਤਾ)](./md/03.FineTuning/FineTuning_Vision.md) - [ਫਾਈਨ-ਟਿਊਨਿੰਗ ਫਾਈ-3 ਕਾਈਟੋ AKS, ਅਜ਼ੁਰ ਕੰਟੇਨਰਜ਼ (ਸਰਕਾਰੀ ਸਹਾਇਤਾ)](./md/03.FineTuning/FineTuning_Kaito.md) - [ਫਾਈਨ-ਟਿਊਨਿੰਗ ਫਾਈ-3 ਅਤੇ 3.5 ਵਿਜ਼ਨ](https://github.com/2U1/Phi3-Vision-Finetune) - ਹੈਂਡਸ-ਆਨ ਲੈਬ - [ਅਗਲੇ ਦਰਜੇ ਮਾਡਲਾਂ ਦੀ ਖੋਜ: LLMs, SLMs, స్థానਿਕ ਵਿਕਾਸ ਅਤੇ ਹੋਰ](https://github.com/microsoft/aitour-exploring-cutting-edge-models) - [NLP ਗੁਣਾਤਮਕਤਾ ਨੂੰ ਖੋਲ੍ਹਣਾ: ਮਾਈਕ੍ਰੋਸਾਫਟ ਓਲਿਵ ਨਾਲ ਫਾਈਨ-ਟਿਊਨਿੰਗ](https://github.com/azure/Ignite_FineTuning_workshop) - ਅਕਾਦਮਿਕ ਖੋਜ ਪੇਪਰ ਅਤੇ ਪ੍ਰਕਾਸ਼ਨ - [ਟੈਕਸਟਬੁਕਸ ਆਰ ਆਲ ਯੂ ਨੀਡ II: phi-1.5 ਤਕਨੀਕੀ ਰਿਪੋਰਟ](https://arxiv.org/abs/2309.05463) - [ਫਾਈ-3 ਤਕਨੀਕੀ ਰਿਪੋਰਟ: ਤੁਹਾਡੇ ਫੋਨ ਉੱਤੇ ਇੱਕ ਬਹੁਤ ਕਾਬਲ ਲੈਂਗਵੇਜ਼ ਮਾਡਲ](https://arxiv.org/abs/2404.14219) - [ਫਾਈ-4 ਤਕਨੀਕੀ ਰਿਪੋਰਟ](https://arxiv.org/abs/2412.08905) - [ਫਾਈ-4-ਮਿਨੀ ਤਕਨੀਕੀ ਰਿਪੋਰਟ: ਮਿਕਸਚਰ-ਆਫ-ਲੋਰਾ ਦੇ ਜ਼ਰੀਏ ਕੰਪੈਕਟ ਪਰ ਜ਼ਬਰਦਸਤ ਮਲਟੀਮੋਡਲ ਭਾਸ਼ਾ ਮਾਡਲਸ](https://arxiv.org/abs/2503.01743) - [ਛੋਟੇ ਭਾਸ਼ਾ ਮਾਡਲਾਂ ਨੂੰ ਗੱਡੀ ਅੰਦਰ ਫੰਕਸ਼ਨ-ਕਾਲਿੰਗ ਲਈ ਅਨੁਕੂਲਿਤ ਕਰਨਾ](https://arxiv.org/abs/2501.02342) - [(WhyPHI) ਬਹੁ-ਚੋਣ ਪ੍ਰਸ਼ਨ ਉੱਤਰ ਦੇਣ ਲਈ PHI-3 ਦੀ ਫਾਈਨ-ਟਿਊਨਿੰਗ: ਤਰੀਕਾ, ਨਤੀਜੇ ਅਤੇ ਚੁਣੌਤੀਆਂ](https://arxiv.org/abs/2501.01588) - [ਫਾਈ-4-ਰੀਜ਼ਨਿੰਗ ਤਕਨੀਕੀ ਰਿਪੋਰਟ](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
- [Phi-4-mini-reasoning ਤਕਨੀਕੀ ਰਿਪੋਰਟ](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)
# ਫਾਈ ਕੁੱਕਬੁਕ: ਮਾਈਕ੍ਰੋਸੋਫਟ ਦੇ ਫਾਈ ਮਾਡਲਾਂ ਨਾਲ ਹੱਥੋਂ-ਹੱਥ ਉਦਾਹਰਨਾਂ

[![GitHub ਕੋਡਸਪੇਸਿਜ਼ ਵਿੱਚ ਨਮੂਨੇ ਖੋਲ੍ਹੋ ਅਤੇ ਉਪਯੋਗ ਕਰੋ](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![ਡੇਵ ਕੰਟੇਨਰਾਂ ਵਿੱਚ ਖੋਲ੍ਹੋ](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub ਯੋਗਦਾਨਕਾਰ](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub ਮੁੱਦੇ](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub ਪੁਲ-ਰਿਕਵੈਸਟ](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![ਪੀਆਰ ਲਈ ਸੁਆਗਤ ਹੈ](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub ਵਾਚਰ](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub ਫੋਰਕ](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub ਸਿਤਾਰੇ](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

ਫਾਈ ਮਾਈਕ੍ਰੋਸੋਫਟ ਦੁਆਰਾ ਵਿਕਸਤ ਖੁੱਲ੍ਹੇ ਸਰੋਤ ਵਾਲੇ ਏਆਈ ਮਾਡਲਾਂ ਦੀ ਇੱਕ ਸੀਰੀਜ਼ ਹੈ।

ਫਾਈ ਵਰਤਮਾਨ ਵਿੱਚ ਸਭ ਤੋਂ ਸ਼ਕਤিশਾਲੀ ਅਤੇ ਲਾਗਤ-ਪ੍ਰਭਾਵੀ ਛੋਟਾ ਭਾਸ਼ਾ ਮਾਡਲ (ਐਸਐਲਐਮ) ਹੈ, ਜਿਸ ਵਿੱਚ ਬਹੁ-ਭਾਸ਼ਾਈ, ਤਰਕਸ਼ੀਲਤਾ, ਲਿਖਤ/ਚੈਟ ਜਨਰੇਸ਼ਨ, ਕੋਡਿੰਗ, ਚਿੱਤਰ, ਆਡੀਓ ਅਤੇ ਹੋਰ ਸਥਿਤੀਆਂ ਵਿੱਚ ਬਹੁਤ ਵਧੀਆ ਬੈਂਚਮਾਰਕ ਹਨ।

ਤੁਸੀਂ ਫਾਈ ਨੂੰ ਕਲਾਉਡ ਜਾਂ ਏਜ ਡਿਵਾਈਸਾਂ 'ਤੇ ਤਿਆਰ ਕਰ ਸਕਦੇ ਹੋ, ਅਤੇ ਅਸੀਮਤ ਕਮਪਿਊਟਿੰਗ ਸ਼ਕਤੀ ਨਾਲ ਆਸਾਨੀ ਨਾਲ ਜਨਰੇਟਿਵ ਏਆਈ ਐਪਲੀਕੇਸ਼ਨਾਂ ਬਣਾ ਸਕਦੇ ਹੋ।

ਇਹਨਾਂ ਸਾਧਨਾਂ ਨੂੰ ਵਰਤਣ ਲਈ ਇਨ੍ਹਾਂ ਕਦਮਾਂ ਦਾ ਪਾਲਣ ਕਰੋ:
1. **ਰੇਪੋਜ਼ਿਟਰੀ ਨੂੰ ਫੋਰਕ ਕਰੋ**: ਕਲਿੱਕ ਕਰੋ [![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **ਰੇਪੋਜ਼ਿਟਰੀ ਕਲੋਨ ਕਰੋ**:   `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**ਮਾਈਕ੍ਰੋਸੋਫਟ ਏਆਈ ਡਿਸਕਾਰਡ ਕਮਿਊਨਿਟੀ ਵਿੱਚ ਸ਼ਾਮਲ ਹੋਵੋ ਅਤੇ ਮਾਹਿਰਾਂ ਅਤੇ ਹੋਰ ਵਿਕਾਸਕਰਤਿਆਂ ਨਾਲ ਮਿਲੋ**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/pa/cover.eb18d1b9605d754b.webp)

### 🌐 ਬਹੁ-ਭਾਸ਼ਾਈ ਸਹਾਇਤਾ

#### GitHub ਐਕਸ਼ਨ ਰਾਹੀਂ ਸਮਰਥਿਤ (ਆਟੋਮੈਟਿਕ ਅਤੇ ਸਦਾ ਅਪ-ਟੂ-ਡੇਟ)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](./README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **ਮੁੜ ਕਲੋਨ ਬਾਹਰਲਾਇਨ ਜ਼ਿਆਦਾ ਪਸੰਦ ਕਰਦੇ ਹੋ?**
>
> ਇਸ ਰੇਪੋ ਵਿੱਚ 50+ ਭਾਸ਼ਾ ਅਨੁਵਾਦ ਸ਼ਾਮਲ ਹਨ ਜੋ ਡਾਊਨਲੋਡ ਦਾ ਆਕਾਰ ਕਾਫੀ ਵਧਾ ਦਿੰਦੇ ਹਨ। ਬਿਨਾਂ ਅਨੁਵਾਦਾਂ ਦੇ ਕਲੋਨ ਕਰਨ ਲਈ, ਸਪਾਰਸ ਚੈਕਆਉਟ ਵਰਤੋ:
>
> **Bash / macOS / Linux:**
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/PhiCookBook.git
> cd PhiCookBook
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
>
> **CMD (ਵਿੰਡੋਜ਼):**
> ```cmd
> git clone --filter=blob:none --sparse https://github.com/microsoft/PhiCookBook.git
> cd PhiCookBook
> git sparse-checkout set --no-cone "/*" "!translations" "!translated_images"
> ```
>
> ਇਹ ਤੁਹਾਨੂੰ ਤੇਜ਼ ਡਾਊਨਲੋਡ ਨਾਲ ਪਾਠ ਸਿੱਖਣ ਲਈ ਸਾਰੀ ਲੋੜੀਂਦੀ ਚੀਜ਼ ਦਿੰਦਾ ਹੈ।
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## ਸੂਚੀ

## ਫਾਈ ਮਾਡਲਾਂ ਦੀ ਵਰਤੋਂ

### ਮਾਈਕ੍ਰੋਸੋਫਟ ਫਾਉਂਡਰੀ 'ਤੇ ਫਾਈ

ਤੁਸੀਂ ਮਾਈਕ੍ਰੋਸੋਫਟ ਫਾਈ ਦੀ ਵਰਤੋਂ ਕਿਵੇਂ ਕਰਨੀ ਹੈ ਅਤੇ ਆਪਣੇ ਵੱਖ-ਵੱਖ ਹਾਰਡਵੇਅਰ ਡਿਵਾਈਸਾਂ ਵਿੱਚ E2E ਹੱਲ ਕਿਵੇਂ ਬਣਾਉਣੇ ਹਨ, ਸਿੱਖ ਸਕਦੇ ਹੋ। ਆਪਣੀ ਰੂਪਰੇखा ਲਈ ਫਾਈ ਦਾ ਅਨੁਭਵ ਕਰਨ ਲਈ, ਮਾਡਲਾਂ ਨਾਲ ਖੇਡਣਾ ਸ਼ੁਰੂ ਕਰੋ ਅਤੇ ਆਪਣੇ ਪਰਿਦ੍ਰਸ਼ਿਆਂ ਲਈ ਫਾਈ ਨੂੰ ਅਨੁਕੂਲਿਤ ਕਰੋ [Microsoft Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai) ਦੀ ਵਰਤੋਂ ਕਰਕੇ। ਤੁਸੀਂ ਵਧੇਰੇ ਜਾਣਕਾਰੀ ਪ੍ਰਾਪਤ ਕਰ ਸਕਦੇ ਹੋ Getting Started with [Microsoft Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md)

**ਪਲੇਗ੍ਰਾਊਂਡ**
ਹਰ ਮਾਡਲ ਲਈ ਤੈਅ ਮਿਸ਼ਨ ਪਲੇਗ੍ਰਾਊਂਡ ਹੈ [Azure AI Playground](https://aka.ms/try-phi3).

### GitHub ਮਾਡਲਾਂ 'ਤੇ ਫਾਈ

ਤੁਸੀਂ ਮਾਈਕ੍ਰੋਸੋਫਟ ਫਾਈ ਦੀ ਵਰਤੋਂ ਕਿਵੇਂ ਕਰਨੀ ਹੈ ਅਤੇ ਆਪਣੇ ਵੱਖ-ਵੱਖ ਹਾਰਡਵੇਅਰ ਡਿਵਾਈਸਾਂ ਵਿੱਚ E2E ਹੱਲ ਕਿਵੇਂ ਬਣਾਉਣੇ ਹਨ, ਜਾਣ ਸਕਦੇ ਹੋ। ਆਪਣੀ ਰੂਪਰੇਖਾ ਲਈ ਫਾਈ ਦਾ ਅਨੁਭਵ ਕਰਨ ਲਈ, ਮਾਡਲ ਨਾਲ ਖੇਡਣਾ ਸ਼ੁਰੂ ਕਰੋ ਅਤੇ ਆਪਣੇ ਪਰਿਦ੍ਰਸ਼ਿਆਂ ਲਈ ਫਾਈ ਨੂੰ ਅਨੁਕੂਲਿਤ ਕਰੋ [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) ਦੀ ਵਰਤੋਂ ਕਰਕੇ। ਤੁਸੀਂ ਵਧੇਰੇ ਜਾਣਕਾਰੀ ਪ੍ਰਾਪਤ ਕਰ ਸਕਦੇ ਹੋ Getting Started with [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md)

**ਪਲੇਗ੍ਰਾਊਂਡ**
ਹਰ ਮਾਡਲ ਲਈ [ਮਾਡਲ ਟੈਸਟ ਕਰਨ ਲਈ ਪਲੇਗ੍ਰਾਊਂਡ](/md/02.QuickStart/GitHubModel_QuickStart.md) ਹੈ।

### Hugging Face 'ਤੇ ਫਾਈ

ਤੁਸੀਂ ਮਾਡਲ ਨੂੰ [Hugging Face](https://huggingface.co/microsoft) 'ਤੇ ਵੀ ਲੱਭ ਸਕਦੇ ਹੋ।

**ਪਲੇਗ੍ਰਾਊਂਡ**
[Hugging Chat playground](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## 🎒 ਹੋਰ ਕੋਰਸز

ਸਾਡੀ ਟੀਮ ਹੋਰ ਕੋਰਸਜ਼ ਤਿਆਰ ਕਰਦੀ ਹੈ! ਵੇਖੋ:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### ਲੈਂਗਚੇਨ
[![ਸ਼ੁਰੂਆਤੀਆਂ ਲਈ LangChain4j](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![ਸ਼ੁਰੂਆਤੀਆਂ ਲਈ LangChain.js](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![ਸ਼ੁਰੂਆਤੀਆਂ ਲਈ LangChain](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### Azure / Edge / MCP / ਏਜੰਟਸ
[![ਸ਼ੁਰੂਆਤੀਆਂ ਲਈ AZD](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![ਸ਼ੁਰੂਆਤੀਆਂ ਲਈ Edge AI](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![ਸ਼ੁਰੂਆਤੀਆਂ ਲਈ MCP](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![ਸ਼ੁਰੂਆਤੀਆਂ ਲਈ AI ਏਜੰਟਸ](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---

### ਜਨਰੇਟਿਵ ਏਆਈ ਸੀਰੀਜ਼
[![ਸ਼ੁਰੂਆਤੀਆਂ ਲਈ ਜਨਰੇਟਿਵ ਏਆਈ](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![ਜਨਰੇਟਿਵ ਏਆਈ (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generative AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generative AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---

### ਮੁੱਖ ਸਿੱਖਿਆ
[![ML for Beginners](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science for Beginners](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI for Beginners](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Cybersecurity for Beginners](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Web Dev for Beginners](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT for Beginners](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR Development for Beginners](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---

### ਕੋਪਾਈਲਟ ਜ਼ਰੀਆ
[![Copilot for AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## ਜਿੰਮੇਵਾਰ ਏਆਈ

ਮਾਇਕ੍ਰੋਸਾਫਟ ਆਪਣੇ ਗਾਹਕਾਂ ਨੂੰ ਆਪਣੇ ਏਆਈ ਉਤਪਾਦਾਂ ਨੂੰ ਜਿੰਮੇਵਾਰੀ ਨਾਲ ਵਰਤਣ ਵਿੱਚ ਸਹਾਇਤਾ ਕਰਨ, ਸਾਡੇ ਸਿੱਖਣੀਆਂ ਸਾਂਝੀਆਂ ਕਰਨ ਅਤੇTransparency Notes ਅਤੇ Impact Assessments ਵਰਗੇ ਟੂਲਾਂ ਰਾਹੀਂ ਭਰੋਸਾ-ਆਧਾਰਿਤ ਭਾਈਚਾਰਿਆਂ ਨੂੰ ਬਣਾਉਣ ਲਈ ਵਚਨਬੱਧ ਹੈ। ਇਨ੍ਹਾਂ ਸੋਧਾਂ ਦੀਆਂ ਕਈ ਸਾਧਨਾਂ ਨੂੰ ਤੁਸੀਂ [https://aka.ms/RAI](https://aka.ms/RAI) 'ਤੇ ਲੱਭ ਸਕਦੇ ਹੋ।
ਮਾਇਕ੍ਰੋਸਾਫਟ ਦਾ ਜਿੰਮੇਵਾਰ ਏਆਈ ਵੱਲ ਰੁਝਾਨ ਸਾਡੀਆਂ ਏਆਈ ਨੀਤੀਆਂ 'ਤੇ ਅਧਾਰਿਤ ਹੈ ਜੋ ਇਨਸਾਫ਼, ਭਰੋਸੇਯੋਗਤਾ ਤੇ ਸੁਰੱਖਿਆ, ਪਰਦੇਦਾਰੀ ਅਤੇ ਸੁਰੱਖਿਆ, ਸ਼ਾਮਿਲ ਹੋਣਾ, ਪਾਰਦਰਸ਼ਤਾ ਅਤੇ ਜਵਾਬਦੇਹੀ ਹਨ।

ਵੱਡੇ ਪੈਮਾਨੇ ਦੇ ਕੁਦਰਤੀ ਭਾਸ਼ਾ, ਚਿੱਤਰ ਅਤੇ ਬੋਲਣ ਮਾਡਲ - ਜਿਵੇਂ ਇਸ ਨਮੂਨੇ ਵਿਚ ਵਰਤੇ ਗਏ ਹਨ - ਸੰਭਾਵਤ ਤੌਰ 'ਤੇ ਅਣਇਨਸਾਫ਼ੀ, ਭਰੋਸੇਯੋਗ ਨਾ ਹੋਣ ਜਾਂ ਅਪਮਾਨਜਨਕ ਤਰੀਕੇ ਨਾਲ ਵਰਤੋਂ ਕਰ ਸਕਦੇ ਹਨ, ਜਿਸ ਨਾਲ ਨੁਕਸਾਨ ਹੋ ਸਕਦਾ ਹੈ। ਕਿਰਪਾ ਕਰਕੇ [Azure OpenAI ਸੇਵਾ Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) ਨੂੰ ਦੇਖੋ ਤਾਂ ਜੋ ਖਤਰਾ ਅਤੇ ਸੀਮਾਵਾਂ ਬਾਰੇ ਜਾਣਕਾਰੀ ਮਿਲੇ।

ਇਹਨਾਂ ਖਤਰਿਆਂ ਨੂੰ ਘਟਾਉਣ ਲਈ ਦਿੱਤੀ ਗਈ ਸਿਫ਼ਾਰਸ਼ ਇਹ ਹੈ ਕਿ ਤੁਸੀਂ ਆਪਣੀ ਪ੍ਰਣਾਲੀ ਵਿਚ ਇੱਕ ਸੁਰੱਖਿਆ ਪ੍ਰਣਾਲੀ ਸ਼ਾਮਲ ਕਰੋ ਜੋ ਹਾਣਿਕਾਰਕ ਵਿਹਾਰ ਨੂੰ ਪਹਚਾਣ ਸਕਦੀ ਅਤੇ ਰੋਕ ਸਕਦੀ ਹੈ। [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) ਇੱਕ ਸੁਤੰਤਰ ਪਰਤ ਸੁਰੱਖਿਆ ਲਈ ਦਾ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ, ਜੋ ਐਪਲੀਕੇਸ਼ਨਾਂ ਅਤੇ ਸੇਵਾਵਾਂ ਵਿੱਚ ਹਾਣਿਕਾਰਕ ਉਪਭੋਗਤਾ ਨਾਲ ਬਣਾਈ ਗਈ ਅਤੇ ਏਆਈ ਨਾਲ ਬਣਾਈ ਗਈ ਸਮੱਗਰੀ ਨੂੰ ਪਹਚਾਣਦਾ ਹੈ। ਮਾਇਕ੍ਰੋਸਾਫਟ ਫਾਉਂਡ੍ਰੀ ਦੇ ਅੰਦਰ, Content Safety ਸੇਵਾ ਤੁਹਾਨੂੰ ਵੱਖ-ਵੱਖ ਮੋਡਾਲਿਟੀਆਂ ਵਿਚ ਹਾਣਿਕਾਰਕ ਸਮੱਗਰੀ ਦੀ ਪਹਚਾਣ ਲਈ ਨਮੂਣਾ ਕੋਡ ਵੇਖਣ, ਖੋਜ ਕਰਨ ਅਤੇ ਕੋਸ਼ਿਸ਼ ਕਰਨ ਦੀ ਆਗਿਆ ਦਿੰਦੀ ਹੈ। ਹੇਠਾਂ ਦਿੱਤੀ [ਤੁਰੰਤ ਸ਼ੁਰੂਆਤ ਡਾਕੂਮੈਂਟੇਸ਼ਨ](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) ਤੁਹਾਨੂੰ ਸੇਵਾ ਨੂੰ ਕਿਵੇਂ ਬੇਨਤੀ ਕਰਨ ਦੀ ਦਿੱਖ ਦਿੰਦੀ ਹੈ।

ਇੱਕ ਹੋਰ ਪਹਲੂ ਜਿਸਦਾ ਖ਼ਿਆਲ ਰੱਖਣਾ ਚਾਹੀਦਾ ਹੈ ਉਹ ਹੈ ਕੁੱਲ ਐਪਲੀਕੇਸ਼ਨ ਕਾਰਗੁਜ਼ਾਰੀ। ਬਹੁ-ਮੋਡਾਲ ਅਤੇ ਬਹੁ-ਮਾਡਲ ਐਪਲੀਕੇਸ਼ਨਾਂ ਦੇ ਸੰਦਰਭ ਵਿਚ, ਅਸੀਂ ਕਾਰਗੁਜ਼ਾਰੀ ਨੂੰ ਸਮਝਦੇ ਹਾਂ ਕਿ ਪ੍ਰਣਾਲੀ ਤੁਹਾਡੇ ਅਤੇ ਤੁਹਾਡੇ ਉਪਭੋਗਤਾਵਾਂ ਦੀ ਉਮੀਦਾਂ ਮੁਤਾਬਕ ਕੰਮ ਕਰਦੀ ਹੈ, ਜਿਸ ਵਿੱਚ ਹਾਣਿਕਾਰਕ ਨਤੀਜੇ ਨਾ ਬਣਾਉਣਾ ਸ਼ਾਮਿਲ ਹੈ। ਇਹ ਜ਼ਰੂਰੀ ਹੈ ਕਿ ਤੁਸੀਂ ਆਪਣੇ ਕੁੱਲ ਐਪਲੀਕੇਸ਼ਨ ਦੀ ਕਾਰਗੁਜ਼ਾਰੀ ਨੂੰ [Performance and Quality and Risk and Safety evaluators](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਮੂਲਾਂਕਣ ਕਰੋ। ਤੁਹਾਡੇ ਕੋਲ [custom evaluators](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators) ਬਣਾਉਣ ਅਤੇ ਮੂਲਾਂਕਣ ਕਰਨ ਦੀ ਵੀ ਸਮਰੱਥਾ ਹੈ।

ਤੁਸੀਂ ਆਪਣੀ ਵਿਕਾਸ ਪਰਿਬੇਸ਼ ਵਿਚ [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਆਪਣੀ ਏਆਈ ਐਪਲੀਕੇਸ਼ਨ ਦਾ ਮੂਲਾਂਕਣ ਕਰ ਸਕਦੇ ਹੋ। ਚਾਹੇ ਇਹ ਇੱਕ ਟੈਸਟ ਡੇਟਾਸੈੱਟ ਹੋਵੇ ਜਾਂ ਇੱਕ ਲੱਛਾ, ਤੁਹਾਡੇ ਜੇਨਰੇਟਿਵ ਏਆਈ ਐਪਲੀਕੇਸ਼ਨ ਜੇਨਰੇਸ਼ਨਾਂ ਨੂੰ ਬਿਲਟ-ਇਨ ਜਾਂ ਕਸਟਮ ਮੂਲਾਂਕਕ ਦੁਆਰਾ ਮਾਤਰਾਤਮਿਕ ਤੌਰ 'ਤੇ ਮਾਪਿਆ ਜਾਂਦਾ ਹੈ। ਆਪਣੀ ਪ੍ਰਣਾਲੀ ਦਾ ਮੂਲਾਂਕਣ ਕਰਨ ਲਈ ਅਜੁਰੂ ਏਆਈ ਈਵੈਲੁਏਸ਼ਨ SDK ਨਾਲ ਤੁਰੰਤ ਸ਼ੁਰੂਆਤ ਕਰਨ ਲਈ, ਤੁਸੀਂ [quickstart ਗਾਈਡ](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) ਨੂੰ ਫਾਲੋ ਕਰ ਸਕਦੇ ਹੋ। ਇੱਕ ਵਾਰੀ ਤੁਸੀਂ ਇਕ ਮੂਲਾਂਕਣ ਚਲਾਉਣ ਦੇ ਬਾਅਦ, ਤੁਸੀਂ [Microsoft Foundry ਵਿੱਚ ਨਤੀਜੇ ਵੇਖ ਸਕਦੇ ਹੋ](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results)। 

## ਟ੍ਰੇਡਮਾਰਕ

ਇਹ ਪ੍ਰੋਜੈਕਟ ਪ੍ਰੋਜੈਕਟਾਂ, ਉਤਪਾਦਾਂ ਜਾਂ ਸੇਵਾਵਾਂ ਲਈ ਟ੍ਰੇਡਮਾਰਕ ਜਾਂ ਲੋਗੋ ਸ਼ਾਮਲ ਕਰ ਸਕਦਾ ਹੈ। ਮਾਇਕ੍ਰੋਸਾਫਟ ਦੇ ਟ੍ਰੇਡਮਾਰਕ ਜਾਂ ਲੋਗੋ ਦੀ ਅਧਿਕਾਰਤ ਵਰਤੋਂ [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) ਦੇ ਅਧੀਨ ਹੈ ਅਤੇ ਇਸ ਨੂੰ ਪਾਲਣਾ ਕਰਨਾ ਜ਼ਰੂਰੀ ਹੈ।
ਇਸ ਪ੍ਰੋਜੈਕਟ ਦੇ ਸੋਧੇ ਹੋਏ ਵਰਜਨਾਂ ਵਿੱਚ ਮਾਇਕ੍ਰੋਸਾਫਟ ਦੇ ਟ੍ਰੇਡਮਾਰਕ ਜਾਂ ਲੋਗੋ ਦੀ ਵਰਤੋਂ ਮਾਇਕ੍ਰੋਸਾਫਟ ਦੀ ਸਹਾਇਤਾ ਧਾਰਨਾ ਜਾਂ ਗਲਤਫਹਮੀ ਪੈਦਾ ਨਹੀਂ ਕਰਨੀ ਚਾਹੀਦੀ। ਕਿਸੇ ਤੀਜੀ ਪਾਰਟੀ ਦੇ ਟ੍ਰੇਡਮਾਰਕ ਜਾਂ ਲੋਗੋ ਦੀ ਵਰਤੋਂ ਉਹਨਾਂ ਤੀਜੀ ਪਾਰਟੀ ਦੀ ਨੀਤੀਆਂ ਦੇ ਅਧੀਨ ਹੁੰਦੀ ਹੈ।

## ਸਹਾਇਤਾ ਪ੍ਰਾਪਤ ਕਰਨਾ

ਜੇ ਤੁਸੀਂ ਕੰਮ ਦੇ ਦੌਰਾਨ ਫਸ ਜਾਂਦੇ ਹੋ ਜਾਂ ਏਆਈ ਐਪ ਬਣਾਉਣ ਬਾਰੇ ਕਿਸੇ ਵੀ ਪ੍ਰਸ਼ਨ ਹੋਣ ਤਾਂ ਸ਼ਾਮਿਲ ਹੋਵੋ:

[![Microsoft Foundry Discord](https://img.shields.io/badge/Discord-Microsoft_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

ਜੇ ਤੁਹਾਡੇ ਕੋਲ ਉਤਪਾਦ ਪ੍ਰਤੀਕਿਰਿਆ ਹੈ ਜਾਂ ਬਣਾਉਂਦੇ ਸਮੇਂ ਕੋਈ ਗਲਤੀ ਆਉਂਦੀ ਹੈ ਤਾਂ ਜਾਓ:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਪਸ਼ਟੀਕਰਨ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ ਏਆਈ ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸ਼ੁੱਧਤਾ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਵਿੱਚ ਰੱਖੋ ਕਿ ਸੁਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਪਸ਼ਟਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਤ ਸ੍ਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਣ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਪੈਦਾ ਹੋਣ ਵਾਲੀ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਵਿਸ਼ਲੇਸ਼ਣ ਲਈ ਜਵਾਬਦੇਹ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->