<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c2e4b490f4bd424b095f21e38c6af33b",
  "translation_date": "2026-01-05T02:29:26+00:00",
  "source_file": "README.md",
  "language_code": "pa"
}
-->
# Phi ਕੁੱਕਬੁੱਕ: ਮਾਇਕ੍ਰੋਸਾਫਟ ਦੇ Phi ਮਾਡਲਾਂ ਨਾਲ ਹੱਥ-ਅਨੁਭਵੀ ਉਦਾਹਰਣਾਂ

[![GitHub Codespaces ਵਿੱਚ ਨਮੂਨੇ ਖੋਲ੍ਹੋ ਅਤੇ ਵਰਤੋ](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Dev Containers ਵਿੱਚ ਖੋਲ੍ਹੋ](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub ਯੋਗਦਾਨਕਰਤਾ](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub ਮੁੱਦੇ](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub ਪੁਲ-ਰਿਕਵੇਸਟ](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PRs ਸਵਾਗਤ ਹਨ](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub ਵੇਖਣ ਵਾਲੇ](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub ਫੋਰਕ](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub ਸਟਾਰਾਂ](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi ਮਾਇਕ੍ਰੋਸਾਫਟ ਵੱਲੋਂ ਵਿਕਸਿਤ ਖੁੱਲ੍ਹੇ ਸਰੋਤ ਵਾਲੇ AI ਮਾਡਲਾਂ ਦੀ ਇੱਕ ਲੜੀ ਹੈ। 

Phi ਵਰਤਮਾਨ ਵਿੱਚ ਸਭ ਤੋਂ ਤਾਕਤਵਰ ਅਤੇ ਲਾਗਤ-ਪੱਖੋਂ ਪ੍ਰਭਾਵਸ਼ালী ਛੋਟਾ ਭਾਸ਼ਾ ਮਾਡਲ (SLM) ਹੈ, ਜਿਸ ਦੇ ਮਲਟੀ-ਭਾਸ਼ਾ, ਤਰਕ, ਟੈਕਸਟ/ਚੈਟ ਜਨਰੇਸ਼ਨ, ਕੋਡਿੰਗ, ਚਿੱਤਰ, ਆਡੀਓ ਅਤੇ ਹੋਰ ਪ੍ਰਸੰਗਾਂ ਵਿੱਚ ਬਹੁਤ ਚੰਗੇ ਬੈਂਚਮਾਰਕ ਹਨ। 

ਤੁਸੀਂ Phi ਨੂੰ ਕਲਾਉਡ ਜਾਂ ਏਜ ਡਿਵਾਈਸਾਂ 'ਤੇ ਡਿਪਲੌਏ ਕਰ ਸਕਦੇ ਹੋ, ਅਤੇ ਸੀਮਿਤ ਕੰਪਿਊਟਿੰਗ ਸ਼ਕਤੀ ਨਾਲ ਆਸਾਨੀ ਨਾਲ ਜੈਨਰੇਟਿਵ AI ਐਪਲੀਕੇਸ਼ਨ ਬਣਾ ਸਕਦੇ ਹੋ।

ਇਨ੍ਹਾਂ ਸਰੋਤਾਂ ਨੂੰ ਵਰਤਣਾ ਸ਼ੁਰੂ ਕਰਨ ਲਈ ਇਹ ਕਦਮ ਫੋਲੋ ਕਰੋ :
1. **ਰਿਪੋਜ਼ਟਰੀ ਨੂੰ Fork ਕਰੋ**: ਕਲਿੱਕ ਕਰੋ [![GitHub ਫੋਰਕ](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **ਰਿਪੋਜ਼ਟਰੀ ਨੂੰ ਕਲੋਨ ਕਰੋ**:   `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Microsoft AI Discord Community ਵਿੱਚ ਸ਼ਾਮਲ ਹੋਵੋ ਅਤੇ ਮਾਹਿਰਾਂ ਅਤੇ ਹੋਰ ਡਿਵੈਲਪਰਾਂ ਨਾਲ ਮਿਲੋ**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![ਕਵਰ](../../translated_images/cover.eb18d1b9605d754b.pa.png)

### 🌐 ਬਹੁ-ਭਾਸ਼ਾਈ ਸਹਾਇਤਾ

#### GitHub Action ਰਾਹੀਂ ਸਮਰਥਿਤ (ਆਟੋਮੇਟਿਕ ਅਤੇ ਹਮੇਸ਼ਾਂ ਅੱਪ-ਟੂ-ਡੇਟ)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[ਅਰਬੀ](../ar/README.md) | [ਬੰਗਾਲੀ](../bn/README.md) | [ਬੁਲਗੇਰੀ](../bg/README.md) | [ਬੁਰਮੇਜ਼ (ਮਿਆਨਮਾਰ)](../my/README.md) | [ਚੀਨੀ (ਸਰਲੀਕਰਨ)](../zh/README.md) | [ਚੀਨੀ (ਰਵਾਇਤੀ, ਹੌਂਗ ਕੌਂਗ)](../hk/README.md) | [ਚੀਨੀ (ਰਵਾਇਤੀ, ਮਕਾਓ)](../mo/README.md) | [ਚੀਨੀ (ਰਵਾਇਤੀ, ਤਾਈਵਾਨ)](../tw/README.md) | [ਕ੍ਰੋਏਸ਼ੀਆਈ](../hr/README.md) | [ਚੈੱਕ](../cs/README.md) | [ਡੈਨਿਸ਼](../da/README.md) | [ਡੱਚ](../nl/README.md) | [ਐਸਟੋਨੀਅਨ](../et/README.md) | [ਫਿਨਿਸ਼](../fi/README.md) | [ਫਰੈਂਚ](../fr/README.md) | [ਜਰਮਨ](../de/README.md) | [ਗ੍ਰੀਕ](../el/README.md) | [ਹੀਬਰੂ](../he/README.md) | [ਹਿੰਦੀ](../hi/README.md) | [ਹੰਗੇਰੀਅਨ](../hu/README.md) | [ਇੰਡੋਨੇਸ਼ੀਆਈ](../id/README.md) | [ਇਤਾਲਵੀ](../it/README.md) | [ਜਾਪਾਨੀ](../ja/README.md) | [ਕੰਨੜ](../kn/README.md) | [ਕੋਰੀਆਈ](../ko/README.md) | [ਲਿਥੁਆਨੀਅਨ](../lt/README.md) | [ਮਲਏ](../ms/README.md) | [മലയാളം](../ml/README.md) | [ਮਰਾਠੀ](../mr/README.md) | [ਨੇਪਾਲੀ](../ne/README.md) | [ਨਾਈਜੀਰੀਆਈ ਪਿਡਗਿਨ](../pcm/README.md) | [ਨਾਰਵੇਜੀਅਨ](../no/README.md) | [ਫਾਰਸੀ (ਫਾਰਸੀ)](../fa/README.md) | [ਪੋਲਿਸ਼](../pl/README.md) | [ਪੁਰਤਗਾਲੀ (ਬ੍ਰਾਜ਼ੀਲ)](../br/README.md) | [ਪੁਰਤਗਾਲੀ (ਪੋਰਤੂਗਾਲ)](../pt/README.md) | [ਪੰਜਾਬੀ (ਗੁਰਮੁਖੀ)](./README.md) | [ਰੋਮੈਨੀਆਈ](../ro/README.md) | [ਰੂਸੀ](../ru/README.md) | [ਸਰਬੀਆਈ (ਸਿਰਿਲਿਕ)](../sr/README.md) | [ਸਲੋਵੈਕ](../sk/README.md) | [ਸਲੋਵੇਨੀਆਈ](../sl/README.md) | [ਸਪੇਨੀ](../es/README.md) | [ਸੁਾਹਿਲੀ](../sw/README.md) | [ਸਵੀਡਿਸ਼](../sv/README.md) | [ਟੈਗਾਲੋਗ (ਫਿਲੀਪੀਨੋ)](../tl/README.md) | [ਤਮਿਲ](../ta/README.md) | [ਤੇਲੁਗੂ](../te/README.md) | [ਥਾਈ](../th/README.md) | [ਤੁਰਕੀ](../tr/README.md) | [ਯੂਕਰੇਨੀਅਨ](../uk/README.md) | [ਉਰਦੂ](../ur/README.md) | [ਵਿਯਤਨਾਮੀ](../vi/README.md)

> **ਕੀ ਤੁਸੀਂ ਲੋਕਲ ਤੌਰ 'ਤੇ ਕਲੋਨ ਕਰਨਾ ਪਸੰਦ ਕਰਦੇ ਹੋ?**

> This repository includes 50+ language translations which significantly increases the download size. To clone without translations, use sparse checkout:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/PhiCookBook.git
> cd PhiCookBook
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> ਇਸ ਨਾਲ ਤੁਹਾਨੂੰ ਕੋਰਸ ਨੂੰ ਪੂਰਾ ਕਰਨ ਲਈ ਜਰੂਰੀ ਸਭ ਕੁਝ ਮਿਲਦਾ ਹੈ ਅਤੇ ਡਾਊਨਲੋਡ ਕਾਫੀ ਤੇਜ਼ ਹੁੰਦਾ ਹੈ।
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## ਸਮੱਗਰੀ ਦੀ ਸੂਚੀ

- ਪਰਿਚਯ
  - [Phi ਪਰਿਵਾਰ ਵਿੱਚ ਤੁਹਾਡਾ ਸਵਾਗਤ ਹੈ](./md/01.Introduction/01/01.PhiFamily.md)
  - [ਆਪਣਾ ਵਾਤਾਵਰਣ ਸੈਟਅਪ ਕਰਨਾ](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [ਮੁੱਖ ਟੈਕਨੋਲੋਜੀਆਂ ਨੂੰ ਸਮਝਣਾ](./md/01.Introduction/01/01.Understandingtech.md)
  - [Phi ਮਾਡਲਾਂ ਲਈ AI ਸੁਰੱਖਿਆ](./md/01.Introduction/01/01.AISafety.md)
  - [Phi ਹਾਰਡਵੇਅਰ ਸਹਾਇਤਾ](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Phi ਮਾਡਲ ਅਤੇ ਪਲੇਟਫਾਰਮਾਂ 'ਤੇ ਉਪਲਬਧਤਾ](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Guidance-ai ਅਤੇ Phi ਦੀ ਵਰਤੋਂ](./md/01.Introduction/01/01.Guidance.md)
  - [GitHub Marketplace ਮਾਡਲ](https://github.com/marketplace/models)
  - [Azure AI ਮਾਡਲ ਕੈਟਾਲੌਗ](https://ai.azure.com)

- ਵੱਖ-ਵੱਖ ਵਾਤਾਵਰਣਾਂ ਵਿੱਚ Phi ਦਾ ਇਨਫਰੈਂਸ
    -  [Hugging Face](./md/01.Introduction/02/01.HF.md)
    -  [GitHub ਮਾਡਲ](./md/01.Introduction/02/02.GitHubModel.md)
    -  [Azure AI Foundry ਮਾਡਲ ਕੈਟਾਲੌਗ](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    -  [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md)

- Phi ਪਰਿਵਾਰ ਵਿੱਚ ਇਨਫਰੈਂਸ
    - [iOS ਵਿੱਚ Phi ਇਨਫਰੈਂਸ](./md/01.Introduction/03/iOS_Inference.md)
    - [Android ਵਿੱਚ Phi ਇਨਫਰੈਂਸ](./md/01.Introduction/03/Android_Inference.md)
    - [Jetson ਵਿੱਚ Phi ਇਨਫਰੈਂਸ](./md/01.Introduction/03/Jetson_Inference.md)
    - [AI PC ਵਿੱਚ Phi ਇਨਫਰੈਂਸ](./md/01.Introduction/03/AIPC_Inference.md)
    - [Apple MLX ਫ੍ਰੇਮਵਰਕ ਨਾਲ Phi ਇਨਫਰੈਂਸ](./md/01.Introduction/03/MLX_Inference.md)
    - [ਲੋਕਲ ਸਰਵਰ ਵਿੱਚ Phi ਇਨਫਰੈਂਸ](./md/01.Introduction/03/Local_Server_Inference.md)
    - [AI Toolkit ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਰਿਮੋਟ ਸਰਵਰ ਵਿੱਚ Phi ਇਨਫਰੈਂਸ](./md/01.Introduction/03/Remote_Interence.md)
    - [Rust ਨਾਲ Phi ਇਨਫਰੈਂਸ](./md/01.Introduction/03/Rust_Inference.md)
    - [ਲੋਕਲ ਵਿੱਚ Phi--ਵਿਜ਼ਨ ਇਨਫਰੈਂਸ](./md/01.Introduction/03/Vision_Inference.md)
    - [Kaito AKS, Azure Containers ਨਾਲ Phi ਇਨਫਰੈਂਸ (ਅਧਿਕਾਰਕ ਸਮਰਥਨ)](./md/01.Introduction/03/Kaito_Inference.md)
-  [Phi ਪਰਿਵਾਰ ਦੀ ਮਾਤਰਾ-ਨਿਰਧਾਰਨ](./md/01.Introduction/04/QuantifyingPhi.md)
    - [llama.cpp ਦੀ ਵਰਤੋਂ ਕਰਕੇ Phi-3.5 / 4 ਨੂੰ Quantize ਕਰਨਾ](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [onnxruntime ਲਈ Generative AI ਐਕਸਟੈਂਸ਼ਨ ਦੀ ਵਰਤੋਂ ਕਰਕੇ Phi-3.5 / 4 ਨੂੰ ਕੁਆਂਟੀਫਾਈ ਕਰਨਾ](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Intel OpenVINO ਦੀ ਵਰਤੋਂ ਕਰਕੇ Phi-3.5 / 4 ਨੂੰ ਕੁਆਂਟੀਫਾਈ ਕਰਨਾ](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Apple MLX ਫ੍ਰੇਮਵਰਕ ਦੀ ਵਰਤੋਂ ਕਰਕੇ Phi-3.5 / 4 ਨੂੰ ਕੁਆਂਟੀਫਾਈ ਕਰਨਾ](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

-  Phi ਦੀ ਮੁਲਾਂਕਣ
    - [Response AI](./md/01.Introduction/05/ResponsibleAI.md)
    - [ਮੁਲਾਂਕਣ ਲਈ Azure AI Foundry](./md/01.Introduction/05/AIFoundry.md)
    - [ਮੁਲਾਂਕਣ ਲਈ Promptflow ਦੀ ਵਰਤੋਂ](./md/01.Introduction/05/Promptflow.md)
 
- Azure AI Search ਨਾਲ RAG
    - [Azure AI Search ਨਾਲ Phi-4-mini ਅਤੇ Phi-4-multimodal(RAG) ਨੂੰ ਕਿਵੇਂ ਵਰਤਣਾ](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Phi ਐਪਲੀਕੇਸ਼ਨ ਵਿਕਾਸ ਨਮੂਨੇ
  - ਟੈਕਸਟ ਅਤੇ ਚੈਟ ਐਪਲੀਕੇਸ਼ਨ
    - Phi-4 ਸੈਂਪਲ 🆕
      - [📓] [Phi-4-mini ONNX ਮਾਡਲ ਨਾਲ ਚੈਟ](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Phi-4 ਲੋਕਲ ONNX ਮਾਡਲ ਨਾਲ ਚੈਟ .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Sementic Kernel ਦੀ ਵਰਤੋਂ ਕਰਕੇ Phi-4 ONNX ਨਾਲ Chat .NET ਕਨਸੋਲ ਐਪ](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Phi-3 / 3.5 ਸੈਂਪਲ
      - [Phi3, ONNX Runtime Web ਅਤੇ WebGPU ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਬ੍ਰਾਊਜ਼ਰ ਵਿੱਚ ਲੋਕਲ ਚੈਟਬੋਟ](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVino ਚੈਟ](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [ਮਲਟੀ ਮਾਡਲ - ਇੰਟਰਐਕਟਿਵ Phi-3-mini ਅਤੇ OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - ਇੱਕ ਰੈਪਰ ਬਣਾਉਣ ਅਤੇ MLFlow ਨਾਲ Phi-3 ਦੀ ਵਰਤੋਂ](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [ਮਾਡਲ ਅਪਟੀਮਾਈਜ਼ੇਸ਼ਨ - Olive ਨਾਲ ONNX Runtime Web ਲਈ Phi-3-min ਮਾਡਲ ਨੂੰ ਕਿਵੇਂ ਅਪਟੀਮਾਈਜ਼ ਕੀਤਾ ਜਾਵੇ](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [WinUI3 ਐਪ ਨਾਲ Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      -[WinUI3 ਮਲਟੀ ਮਾਡਲ AI ਸੰਚਾਲਿਤ ਨੋਟਸ ਐਪ ਨਮੂਨਾ](https://github.com/microsoft/ai-powered-notes-winui3-sample)
      - [Prompt flow ਨਾਲ ਕਸਟਮ Phi-3 ਮਾਡਲਾਂ ਨੂੰ ਫਾਈਨ-ਟਿਊਨ ਅਤੇ ਇੰਟੀਗ੍ਰੇਟ ਕਰੋ](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
      - [Azure AI Foundry ਵਿੱਚ Prompt flow ਨਾਲ ਕਸਟਮ Phi-3 ਮਾਡਲਾਂ ਨੂੰ ਫਾਈਨ-ਟਿਊਨ ਅਤੇ ਇੰਟੀਗ੍ਰੇਟ ਕਰੋ](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
      - [Microsoft ਦੇ ਜ਼ਿੰਮੇਵਾਰ AI ਨੀਤੀਆਂ 'ਤੇ ਧਿਆਨ ਕੇਂਦ੍ਰਿਤ ਕਰਦੇ ਹੋਏ Azure AI Foundry ਵਿੱਚ ਫਾਈਨ-ਟਿਊਨ ਕੀਤੇ Phi-3 / Phi-3.5 ਮਾਡਲ ਦਾ ਮੁੱਲਾਂਕਣ ਕਰੋ](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
      - [📓] [Phi-3.5-mini-instruct ਭਾਸ਼ਾ ਅਨੁਮਾਨ ਨਮੂਨਾ (ਚੀਨੀ/ਅੰਗਰੇਜ਼ੀ)](./md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
      - [Phi-3.5-Instruct WebGPU RAG ਚੈਟਬੋਟ](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
      - [Phi-3.5-Instruct ONNX ਨਾਲ Prompt flow ਸ_solution ਬਣਾਉਣ ਲਈ Windows GPU ਦੀ ਵਰਤੋਂ](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
      - [Android ਐਪ ਬਣਾਉਣ ਲਈ Microsoft Phi-3.5 tflite ਦੀ ਵਰਤੋਂ](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
      - [Q&A .NET ਉਦਾਹਰਨ — Microsoft.ML.OnnxRuntime ਦੀ ਵਰਤੋਂ ਨਾਲ ਲੋਕਲ ONNX Phi-3 ਮਾਡਲ](../../md/04.HOL/dotnet/src/LabsPhi301)
      - [ਕੰਸੋਲ ਚੈਟ .NET ਐਪ Semantic Kernel ਅਤੇ Phi-3 ਨਾਲ](../../md/04.HOL/dotnet/src/LabsPhi302)

  - Azure AI Inference SDK Code Based Samples 
    - Phi-4 ਨਮੂਨੇ 🆕
      - [📓] [Phi-4-multimodal ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਪ੍ਰੋਜੈਕਟ ਕੋਡ ਬਣਾਓ](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
    - Phi-3 / 3.5 ਨਮੂਨੇ
      - [ਆਪਣਾ Visual Studio Code GitHub Copilot Chat Microsoft Phi-3 Family ਨਾਲ ਬਣਾਉ](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
      - [GitHub Models ਦੁਆਰਾ Phi-3.5 ਨਾਲ ਆਪਣਾ Visual Studio Code Chat Copilot Agent ਬਣਾਓ](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

  - ਐਡਵਾਂਸਡ ਰੀਜ਼ਨਿੰਗ ਨਮੂਨੇ
    - Phi-4 ਨਮੂਨੇ 🆕
      - [📓] [Phi-4-mini-reasoning ਜਾਂ Phi-4-reasoning ਨਮੂਨੇ](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
      - [📓] [Microsoft Olive ਨਾਲ Phi-4-mini-reasoning ਨੂੰ ਫਾਈਨ-ਟਿਊਨ ਕਰਨਾ](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Apple MLX ਨਾਲ Phi-4-mini-reasoning ਨੂੰ ਫਾਈਨ-ਟਿਊਨ ਕਰਨਾ](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [GitHub Models ਨਾਲ Phi-4-mini-reasoning](./md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
      - [📓] [Azure AI Foundry Models ਨਾਲ Phi-4-mini-reasoning](./md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
  - ਡੈਮੋਜ਼
      - [Hugging Face Spaces 'ਤੇ ਹੋਸਟ ਕੀਤੇ ਗਏ Phi-4-mini ਡੈਮੋਜ਼](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
      - [Hugginge Face Spaces 'ਤੇ ਹੋਸਟ ਕੀਤੇ ਗਏ Phi-4-multimodal ਡੈਮੋਜ਼](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
  - ਵਿਜ਼ਨ ਨਮੂਨੇ
    - Phi-4 ਨਮੂਨੇ 🆕
      - [📓] [ਚਿੱਤਰ ਪੜ੍ਹਨ ਅਤੇ ਕੋਡ ਬਣਾਉਣ ਲਈ Phi-4-multimodal ਦੀ ਵਰਤੋਂ ਕਰੋ](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
    - Phi-3 / 3.5 ਨਮੂਨੇ
      -  [📓][Phi-3-vision-ਇਮੇਜ ਟੈਕਸਟ ਤੋਂ ਟੈਕਸਟ](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
      - [📓][Phi-3-vision CLIP ਐਮਬੈੱਡਿੰਗ](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [ਡੀਮੋ: Phi-3 ਰੀਸਾਈਕਲਿੰਗ](https://github.com/jennifermarsman/PhiRecycling/)
      - [Phi-3-vision - ਵਿਜ਼ੂਅਲ ਭਾਸ਼ਾ ਸਹਾਇਕ - Phi3-Vision ਅਤੇ OpenVINO ਨਾਲ](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
      - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
      - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
      - [📓][Phi-3.5 Vision ਮਲਟੀ-ਫਰੇਮ ਜਾਂ ਮਲਟੀ-ਇਮੇਜ ਨਮੂਨਾ](./md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
      - [Microsoft.ML.OnnxRuntime .NET ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਹੋਏ Phi-3 Vision ਲੋਕਲ ONNX ਮਾਡਲ](../../md/04.HOL/dotnet/src/LabsPhi303)
      - [ਮੇਨੂ ਆਧਾਰਿਤ Phi-3 Vision ਲੋਕਲ ONNX ਮਾਡਲ Microsoft.ML.OnnxRuntime .NET ਦੀ ਵਰਤੋਂ ਨਾਲ](../../md/04.HOL/dotnet/src/LabsPhi304)

  - ਗਣਿਤ ਨਮੂਨੇ
    -  Phi-4-Mini-Flash-Reasoning-Instruct ਨਮੂਨੇ 🆕 [Phi-4-Mini-Flash-Reasoning-Instruct ਨਾਲ ਗਣਿਤ ਡੈਮੋ](./md/02.Application/09.Math/MathDemo.ipynb)

  - ਆਡੀਓ ਨਮੂਨੇ
    - Phi-4 ਨਮੂਨੇ 🆕
      - [📓] [Phi-4-multimodal ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਆਡੀਓ ਟ੍ਰਾਂਸਕ੍ਰਿਪਟ ਨਿਕਾਲਣਾ](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
      - [📓] [Phi-4-multimodal ਆਡੀਓ ਨਮੂਨਾ](./md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
      - [📓] [Phi-4-multimodal ਬੋਲ ਚਾਲ ਅਨੁਵਾਦ ਨਮੂਨਾ](./md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
      - [.NET ਕੰਸੋਲ ਐਪਲੀਕੇਸ਼ਨ ਜੋ Phi-4-multimodal ਆਡੀਓ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇੱਕ ਆਡੀਓ ਫਾਇਲ ਦਾ ਵਿਸ਼ਲੇਸ਼ਣ ਕਰਦਾ ਹੈ ਅਤੇ ਟ੍ਰਾਂਸਕ੍ਰਿਪਟ ਬਣਾਉਂਦਾ ਹੈ](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

  - MOE ਨਮੂਨੇ
    - Phi-3 / 3.5 ਨਮੂਨੇ
      - [📓] [Phi-3.5 Mixture of Experts Models (MoEs) ਸੋਸ਼ਲ ਮੀਡੀਆ ਨਮੂਨਾ](./md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
      - [📓] [NVIDIA NIM Phi-3 MOE, Azure AI Search, ਅਤੇ LlamaIndex ਨਾਲ Retrieval-Augmented Generation (RAG) ਪਾਈਪਲਾਈਨ ਬਣਾਉਣਾ](./md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)
      - 
  - Function Calling ਨਮੂਨੇ
    - Phi-4 ਨਮੂਨੇ 🆕
      -  [📓] [Phi-4-mini ਨਾਲ Function Calling ਦੀ ਵਰਤੋਂ](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
      -  [📓] [Phi-4-mini ਨਾਲ ਬਹੁ-ਏਜੰਟ ਬਣਾਉਣ ਲਈ Function Calling ਦੀ ਵਰਤੋਂ](./md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
      -  [📓] [Ollama ਨਾਲ Function Calling ਦੀ ਵਰਤੋਂ](./md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
      -  [📓] [ONNX ਨਾਲ Function Calling ਦੀ ਵਰਤੋਂ](./md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)
  - ਮਲਟੀਮੋਡਲ ਮਿਕਸਿੰਗ ਨਮੂਨੇ
    - Phi-4 ਨਮੂਨੇ 🆕
      -  [📓] [ਟੈਕਨੋਲੋਜੀ ਪੱਤਰਕਾਰ ਵਜੋਂ Phi-4-multimodal ਦੀ ਵਰਤੋਂ](./md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
      - [.NET ਕੰਸੋਲ ਐਪਲੀਕੇਸ਼ਨ ਜੋ Phi-4-multimodal ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਚਿੱਤਰਾਂ ਦਾ ਵਿਸ਼ਲੇਸ਼ਣ ਕਰਦਾ ਹੈ](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Phi ਫਾਈਨ-ਟਿਊਨਿੰਗ ਨਮੂਨੇ
  - [ਫਾਈਨ-ਟਿਊਨਿੰਗ ਸਥਿਤੀਆਂ](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [ਫਾਈਨ-ਟਿਊਨਿੰਗ ਬਨਾਮ RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [ਫਾਈਨ-ਟਿਊਨਿੰਗ: Phi-3 ਨੂੰ ਉਦਯੋਗ ਵਿਸ਼ੇਸ਼ਗਿਆ ਬਣਾਓ](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [Visual Studio Code ਲਈ AI Toolkit ਨਾਲ Phi-3 ਨੂੰ ਫਾਈਨ-ਟਿਊਨ ਕਰਨਾ](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Azure Machine Learning Service ਨਾਲ Phi-3 ਨੂੰ ਫਾਈਨ-ਟਿਊਨ ਕਰਨਾ](./md/03.FineTuning/Introduce_AzureML.md)
  - [Lora ਨਾਲ Phi-3 ਨੂੰ ਫਾਈਨ-ਟਿਊਨ ਕਰਨਾ](./md/03.FineTuning/FineTuning_Lora.md)
  - [QLora ਨਾਲ Phi-3 ਨੂੰ ਫਾਈਨ-ਟਿਊਨ ਕਰਨਾ](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Azure AI Foundry ਨਾਲ Phi-3 ਨੂੰ ਫਾਈਨ-ਟਿਊਨ ਕਰਨਾ](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Azure ML CLI/SDK ਨਾਲ Phi-3 ਨੂੰ ਫਾਈਨ-ਟਿਊਨ ਕਰਨਾ](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Microsoft Olive ਨਾਲ ਫਾਈਨ-ਟਿਊਨਿੰਗ](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Microsoft Olive Hands-On Lab ਨਾਲ ਫਾਈਨ-ਟਿਊਨਿੰਗ](./md/03.FineTuning/olive-lab/readme.md)
  - [Weights and Bias ਨਾਲ Phi-3-vision ਨੂੰ ਫਾਈਨ-ਟਿਊਨ ਕਰਨਾ](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [Apple MLX Framework ਨਾਲ Phi-3 ਨੂੰ ਫਾਈਨ-ਟਿਊਨ ਕਰਨਾ](./md/03.FineTuning/FineTuning_MLX.md)
  - [Phi-3-vision ਦੀ ਫਾਈਨ-ਟਿਊਨਿੰਗ (ਆਧਿਕਾਰਿਕ ਸਹਾਇਤਾ)](./md/03.FineTuning/FineTuning_Vision.md)
  - [Kaito AKS , Azure Containers(ਆਧਿਕਾਰਿਕ ਸਹਾਇਤਾ) ਨਾਲ Phi-3 ਦੀ ਫਾਈਨ-ਟਿਊਨਿੰਗ](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Phi-3 ਅਤੇ 3.5 Vision ਦੀ ਫਾਈਨ-ਟਿਊਨਿੰਗ](https://github.com/2U1/Phi3-Vision-Finetune)

- ਹੈਂਡਸ-ਆਨ ਲੈਬ
  - [ਕਟਿੰਗ-ਐਜ ਮਾਡਲਾਂ ਦੀ ਖੋਜ: LLMs, SLMs, ਲੋਕਲ ਡਿਵੈਲਪਮੈਂਟ ਅਤੇ ਹੋਰ](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [NLP ਦੀ ਸੰਭਾਵਨਾ ਅਨਲੌਕ ਕਰਨਾ: Microsoft Olive ਨਾਲ ਫਾਈਨ-ਟਿਊਨਿੰਗ](https://github.com/azure/Ignite_FineTuning_workshop)

- ਅਕਾਦਮਿਕ ਖੋਜ ਪੇਪਰ ਅਤੇ ਪ੍ਰਕਾਸ਼ਨ
  - [Textbooks Are All You Need II: phi-1.5 ਤਕਨੀਕੀ ਰਿਪੋਰਟ](https://arxiv.org/abs/2309.05463)
  - [Phi-3 ਤਕਨੀਕੀ ਰਿਪੋਰਟ: ਤੁਹਾਡੇ ਫੋਨ 'ਤੇ ਲੋਕਲ ਤੌਰ 'ਤੇ ਉੱਚ ਸਮਰੱਥਾ ਵਾਲਾ ਭਾਸ਼ਾ ਮਾਡਲ](https://arxiv.org/abs/2404.14219)
  - [Phi-4 ਤਕਨੀਕੀ ਰਿਪੋਰਟ](https://arxiv.org/abs/2412.08905)
  - [Phi-4-Mini ਤਕਨੀਕੀ ਰਿਪੋਰਟ: Mixture-of-LoRAs ਰਾਹੀਂ ਸੰਕੁਚਿਤ ਪਰ ਸ਼ਕਤिशਾਲੀ ਬਹੁ-ਮੋਡਲ ਭਾਸ਼ਾ ਮਾਡਲ](https://arxiv.org/abs/2503.01743)
  - [ਵਾਹਨ-ਅੰਦਰ ਫੰਕਸ਼ਨ-ਕਾਲਿੰਗ ਲਈ ਛੋਟੇ ਭਾਸ਼ਾ ਮਾਡਲਾਂ ਦਾ ਅਪਟੀਮਾਈਜ਼ੇਸ਼ਨ](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) Multiple-Choice ਸਵਾਲਾਂ ਦੇ ਜਵਾਬ ਲਈ PHI-3 ਦੀ ਫਾਈਨ-ਟਿਊਨਿੰਗ: ਵਿਧੀ, ਨਤੀਜੇ ਅਤੇ ਚੁਣੌਤੀਆਂ](https://arxiv.org/abs/2501.01588)
  - [Phi-4-reasoning ਤਕਨੀਕੀ ਰਿਪੋਰਟ](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Phi-4-mini-reasoning ਤਕਨੀਕੀ ਰਿਪੋਰਟ](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Phi ਮਾਡਲਾਂ ਦੀ ਵਰਤੋਂ

### Azure AI Foundry 'ਤੇ Phi

ਤੁਸੀਂ ਸਿੱਖ ਸਕਦੇ ਹੋ ਕਿ Microsoft Phi ਦੀ ਵਰਤੋਂ ਕਿਵੇਂ ਕਰਨੀ ਹੈ ਅਤੇ ਆਪਣੇ ਵੱਖ-ਵੱਖ ਹਾਰਡਵੇਅਰ ਡਿਵਾਈਸਾਂ 'ਤੇ E2E ਹੱਲ ਕਿਵੇਂ ਬਣਾਉਣੇ ਹਨ। Phi ਨੂੰ ਖੁਦ ਅਨੁਭਵ ਕਰਨ ਲਈ, ਮਾਡਲਾਂ ਨਾਲ ਖੇਡਣਾ ਸ਼ੁਰੂ ਕਰੋ ਅਤੇ ਆਪਣੇ ਪਰਿਪੇਖ ਲਈ Phi ਨੂੰ ਕਸਟਮਾਈਜ਼ ਕਰਨ ਲਈ [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai) ਦੀ ਵਰਤੋਂ ਕਰੋ। ਤੁਸੀਂ [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md) ਨਾਲ ਸ਼ੁਰੂ ਕਰਨ ਬਾਰੇ ਹੋਰ ਜਾਣ ਸਕਦੇ ਹੋ।

**ਪਲੇਗ੍ਰਾਊਂਡ**
ਹਰ ਮਾਡਲ ਨੂੰ ਮਾਡਲ ਦੀ ਜਾਂਚ ਕਰਨ ਲਈ ਇੱਕ ਸਮਰਪਿਤ ਪਲੇਗ੍ਰਾਊਂਡ ਮਿਲਦਾ ਹੈ [Azure AI Playground](https://aka.ms/try-phi3).

### GitHub Models 'ਤੇ Phi

ਤੁਸੀਂ ਸਿੱਖ ਸਕਦੇ ਹੋ ਕਿ Microsoft Phi ਦੀ ਵਰਤੋਂ ਕਿਵੇਂ ਕਰਨੀ ਹੈ ਅਤੇ ਆਪਣੇ ਵੱਖ-ਵੱਖ ਹਾਰਡਵੇਅਰ ਡਿਵਾਈਸਾਂ 'ਤੇ E2E ਹੱਲ ਕਿਵੇਂ ਬਣਾਉਣੇ ਹਨ। Phi ਨੂੰ ਖੁਦ ਅਨੁਭਵ ਕਰਨ ਲਈ, ਮਾਡਲ ਨਾਲ ਖੇਡਣਾ ਸ਼ੁਰੂ ਕਰੋ ਅਤੇ ਆਪਣੇ ਪਰਿਪੇਖ ਲਈ Phi ਨੂੰ ਕਸਟਮਾਈਜ਼ ਕਰਨ ਲਈ [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) ਦੀ ਵਰਤੋਂ ਕਰੋ। ਤੁਸੀਂ [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md) ਨਾਲ ਸ਼ੁਰੂ ਕਰਨ ਬਾਰੇ ਹੋਰ ਜਾਣ ਸਕਦੇ ਹੋ।

**ਪਲੇਗ੍ਰਾਊਂਡ**
ਹਰ ਮਾਡਲ ਦਾ ਇੱਕ ਸਮਰਪਿਤ [ਮਾਡਲ ਦੀ ਜਾਂਚ ਲਈ ਪਲੇਗ੍ਰਾਊਂਡ](/md/02.QuickStart/GitHubModel_QuickStart.md) ਹੁੰਦਾ ਹੈ।

### Hugging Face 'ਤੇ Phi

ਤੁਸੀਂ ਮਾਡਲ ਨੂੰ [Hugging Face](https://huggingface.co/microsoft) 'ਤੇ ਵੀ ਲੱਭ ਸਕਦੇ ਹੋ।

**ਪਲੇਗ੍ਰਾਊਂਡ**
 [Hugging Chat ਪਲੇਗ੍ਰਾਊਂਡ](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

 ## 🎒 ਹੋਰ ਕੋਰਸ

Our team produces other courses! Check out:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j ਸ਼ੁਰੂਆਤ ਕਰਨ ਵਾਲਿਆਂ ਲਈ](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js ਸ਼ੁਰੂਆਤ ਕਰਨ ਵਾਲਿਆਂ ਲਈ](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

---

### Azure / Edge / MCP / ਏਜੰਟਸ
[![AZD ਸ਼ੁਰੂਆਤ ਕਰਨ ਵਾਲਿਆਂ ਲਈ](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI ਸ਼ੁਰੂਆਤ ਕਰਨ ਵਾਲਿਆਂ ਲਈ](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP ਸ਼ੁਰੂਆਤ ਕਰਨ ਵਾਲਿਆਂ ਲਈ](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI ਏਜੰਟਸ ਸ਼ੁਰੂਆਤ ਕਰਨ ਵਾਲਿਆਂ ਲਈ](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Generative AI ਸੀਰੀਜ਼
[![Generative AI ਸ਼ੁਰੂਆਤ ਕਰਨ ਵਾਲਿਆਂ ਲਈ](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generative AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generative AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generative AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### ਮੁੱਖ ਸਿੱਖਿਆ
[![ML ਸ਼ੁਰੂਆਤ ਕਰਨ ਵਾਲਿਆਂ ਲਈ](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science ਸ਼ੁਰੂਆਤ ਕਰਨ ਵਾਲਿਆਂ ਲਈ](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI ਸ਼ੁਰੂਆਤ ਕਰਨ ਵਾਲਿਆਂ ਲਈ](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![ਸਾਇਬਰਸੁਰੱਖਿਆ ਸ਼ੁਰੂਆਤ ਕਰਨ ਵਾਲਿਆਂ ਲਈ](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Web Dev ਸ਼ੁਰੂਆਤ ਕਰਨ ਵਾਲਿਆਂ ਲਈ](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT ਸ਼ੁਰੂਆਤ ਕਰਨ ਵਾਲਿਆਂ ਲਈ](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR Development ਸ਼ੁਰੂਆਤ ਕਰਨ ਵਾਲਿਆਂ ਲਈ](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot ਸੀਰੀਜ਼
[![Copilot AI ਜੋੜੀ ਪ੍ਰੋਗ੍ਰਾਮਿੰਗ ਲਈ](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot C#/.NET ਲਈ](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## ਜ਼ਿੰਮੇਵਾਰ AI 

Microsoft ਆਪਣੇ ਗ੍ਰਾਹਕਾਂ ਨੂੰ ਸਾਡੇ AI ਉਤਪਾਦਾਂ ਦੀ ਜ਼ਿੰਮੇਵਾਰੀ ਨਾਲ ਵਰਤੋਂ ਕਰਨ ਵਿੱਚ ਮਦਦ ਕਰਨ, ਸਾਡੇ ਸਿੱਖਿਆ ਦਾ ਸਾਂਝਾ ਕਰਨ ਅਤੇ Transparency Notes ਅਤੇ Impact Assessments ਵਰਗੇ ਟੂਲਾਂ ਰਾਹੀਂ ਭਰੋਸੇ 'ਤੇ ਆਧਾਰਿਤ ਭਾਈਚਾਰੇ ਬਣਾਉਣ ਲਈ ਪ੍ਰਤਿਬੱਧ ਹੈ। ਇਹਨਾਂ ਵਿੱਚੋਂ ਕਈ ਸਰੋਤ [https://aka.ms/RAI](https://aka.ms/RAI) 'ਤੇ ਮਿਲ ਸਕਦੇ ਹਨ।
Microsoft ਦਾ ਜ਼ਿੰਮੇਵਾਰ AI ਲਈ ਰਵੱਈਆ ਸਾਡੇ AI ਸਿਧਾਂਤਾਂ 'ਤੇ ਅਧਾਰਿਤ ਹੈ: ਇਨਸਾਫ, ਭਰੋਸੇਯੋਗਤਾ ਅਤੇ ਸੁਰੱਖਿਆ, ਗੋਪਨੀਆਂਅਤਾ ਅਤੇ ਸੁਰੱਖਿਆ, ਸ਼ਾਮਿਲਤਾ, ਪਾਰਦਰਸ਼ਤਾ, ਅਤੇ ਜਵਾਬਦੇਹੀ।

ਵੱਡੇ ਪੱਧਰ ਦੇ ਕੁਦਰਤੀ ਭਾਸ਼ਾ, ਚਿੱਤਰ, ਅਤੇ ਭਾਸ਼ਣ ਮਾਡਲ — ਜਿਵੇਂ ਕਿ ਇਸ ਨਮੂਨੇ ਵਿੱਚ ਵਰਤੇ ਗਏ ਮਾਡਲ — ਸੰਭਵ ਹੈ ਕਿ ਅਨੁਚਿਤ, ਅਣਭਰੋਸੇਯੋਗ, ਜਾਂ ਉਕਸਾਉਣ ਵਾਲੇ ਢੰਗ ਨਾਲ ਵਰਤਾਵ ਕਰ ਸਕਨ, ਜਿਸ ਨਾਲ नुकਸਾਨ ਹੋ ਸਕਦਾ ਹੈ। ਜੋਖਮਾਂ ਅਤੇ ਸੀਮਾਵਾਂ ਬਾਰੇ ਜਾਣੂ ਹੋਣ ਲਈ ਕਿਰਪਾ ਕਰਕੇ [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) ਦੀ ਸਲਾਹ ਲਓ।

ਇਨ੍ਹਾਂ ਜੋਖਮਾਂ ਨੂੰ ਘਟਾਉਣ ਲਈ ਸਿਫ਼ਾਰਸ਼ੀ ਪਹੁੰਚ ਇਹ ਹੈ ਕਿ ਆਪਣੀ ਆਰਕੀਟੈਕਚਰ ਵਿੱਚ ਇੱਕ ਸੁਰੱਖਿਆ ਸਿਸਟਮ ਸ਼ਾਮਲ ਕੀਤਾ ਜਾਵੇ ਜੋ ਹਾਨਿਕਾਰਕ ਵਰਤੋਂ ਨੂੰ ਪਹਚਾਣ ਅਤੇ ਰੋਕ ਸਕੇ। [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) ਇੱਕ ਸੁਤੰਤਰ ਪਰਤ ਦੀ ਰੱਖਿਆ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ, ਜੋ ਕਿ ਐਪਲੀਕੇਸ਼ਨਾਂ ਅਤੇ ਸੇਵਾਵਾਂ ਵਿੱਚ ਹਾਨਿਕਾਰਕ ਉਪਭੋਗਤਾ-ਜਨਿਤ ਅਤੇ AI-ਜਨਿਤ ਸਮੱਗਰੀ ਨੂੰ ਪਹਚਾਣ ਸਕਦਾ ਹੈ। Azure AI Content Safety ਵਿੱਚ ਉਹ ਟੈਕਸਟ ਅਤੇ ਚਿੱਤਰ API ਸ਼ਾਮਲ ਹਨ ਜੋ ਤੁਹਾਨੂੰ ਹਾਨਿਕਾਰਕ ਸਮੱਗਰੀ ਦੀ ਪਹਿਚਾਣ ਕਰਨ ਦੀ ਆਗਿਆ ਦਿੰਦੇ ਹਨ। Azure AI Foundry ਵਿੱਚ, Content Safety ਸੇਵਾ ਤੁਹਾਨੂੰ ਵੱਖ-ਵੱਖ ਮੋਡੈਲਿਟੀਜ਼ ਵਿੱਚ ਹਾਨਿਕਾਰਕ ਸਮੱਗਰੀ ਦੀ ਪਹਚਾਣ ਲਈ ਨਮੂਨਾ ਕੋਡ ਵੇਖਣ, ਖੋਜਣ ਅਤੇ ਕੋਸ਼ਿਸ਼ ਕਰਨ ਦੀ ਆਗਿਆ ਦਿੰਦੀ ਹੈ। ਹੇਠਾਂ ਦਿੱਤਾ ਗਿਆ [quickstart documentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) ਤੁਹਾਨੂੰ ਸੇਵਾ ਲਈ ਬੇਨਤੀਆਂ ਬਣਾਉਣ ਰਾਹੀਂ ਮਦਦ ਕਰੇਗਾ।

ਇੱਕ ਹੋਰ ਪਹਲੂ ਜੋ ਧਿਆਨ ਵਿੱਚ ਰੱਖਣਯੋਗ ਹੈ ਉਹ ਹੈ ਕੁੱਲ ਐਪਲੀਕੇਸ਼ਨ ਪ੍ਰਦਰਸ਼ਨ। ਬਹੁ-ਮੋਡਲ ਅਤੇ ਬਹੁ-ਮਾਡਲ ਐਪਲੀਕੇਸ਼ਨਾਂ ਦੇ ਨਾਲ, ਅਸੀਂ ਪ੍ਰਦਰਸ਼ਨ ਨੂੰ ਇਸ ਰੂਪ ਵਿੱਚ ਵੇਖਦੇ ਹਾਂ ਕਿ ਸਿਸਟਮ ਓਸੇ ਤਰ੍ਹਾਂ ਕੰਮ ਕਰੇ ਜਿਵੇਂ ਤੁਸੀਂ ਅਤੇ ਤੁਹਾਡੇ ਉਪਭੋਗਤਾ ਉਮੀਦ ਕਰਦੇ ਹੋ, ਜਿਸ ਵਿੱਚ ਹਾਨਿਕਾਰਕ ਆਉਟਪੁੱਟ ਨਿਰਮਾਣ ਨਾ ਕਰਨਾ ਵੀ ਸ਼ਾਮਲ ਹੈ। ਆਪਣੇ ਕੁੱਲ ਐਪਲੀਕੇਸ਼ਨ ਦੇ ਪ੍ਰਦਰਸ਼ਨ ਦਾ ਮੁਲਾਂਕਣ ਕਰਨ ਲਈ ਇਹ ਜਰੂਰੀ ਹੈ ਕਿ ਤੁਸੀਂ [Performance and Quality and Risk and Safety evaluators](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) ਦੀ ਵਰਤੋਂ ਕਰੋ। ਤੁਹਾਡੇ ਕੋਲ [custom evaluators](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators) ਨਾਲ ਬਣਾਉਣ ਅਤੇ ਮੁਲਾਂਕਣ ਕਰਨ ਦੀ ਸਮਰੱਥਾ ਵੀ ਹੈ।
ਤੁਸੀਂ ਆਪਣੇ ਵਿਕਾਸ ਵਾਤਾਵਰਨ ਵਿੱਚ [Azure AI ਮੂਲਾਂਕਣ SDK](https://microsoft.github.io/promptflow/index.html) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਆਪਣੀ AI ਐਪਲੀਕੇਸ਼ਨ ਦਾ ਮੁਲਾਂਕਣ ਕਰ ਸਕਦੇ ਹੋ। ਚਾਹੇ ਇੱਕ ਟੈਸਟ ਡੇਟਾਸੈੱਟ ਦਿੱਤਾ ਗਿਆ ਹੋਵੇ ਜਾਂ ਕੋਈ ਟਾਰਗੇਟ, ਤੁਹਾਡੇ ਜਨਰੇਟਿਵ AI ਐਪਲੀਕੇਸ਼ਨ ਦੀਆਂ ਪੈਦਾਵਾਰਾਂ ਨੂੰ ਬਣੇ-ਬਣਾਏ ਇਵੈਲੂਏਟਰਾਂ ਜਾਂ ਤੁਹਾਡੇ ਚੋਣ ਵਾਲੇ ਕਸਟਮ ਇਵੈਲੂਏਟਰਾਂ ਨਾਲ ਪਰਿਮਾਣਾਤਮਕ ਤੌਰ 'ਤੇ ਮਾਪਿਆ ਜਾਂਦਾ ਹੈ। ਆਪਣੇ ਸਿਸਟਮ ਦਾ ਮੁਲਾਂਕਣ ਕਰਨ ਲਈ Azure AI ਮੂਲਾਂਕਣ SDK ਨਾਲ ਸ਼ੁਰੂ ਕਰਨ ਲਈ, ਤੁਸੀਂ [ਤੁਰੰਤ ਸ਼ੁਰੂਆਤ ਗਾਈਡ](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) ਨੂੰ ਫਾਲੋ ਕਰ ਸਕਦੇ ਹੋ। ਇੱਕ ਵਾਰੀ ਤੁਸੀਂ ਇੱਕ ਇਵੈਲੂਏਸ਼ਨ ਰਨ ਚਲਾਉਂਦੇ ਹੋ, ਤਾਂ ਤੁਸੀਂ [Azure AI Foundry ਵਿੱਚ ਨਤੀਜੇ ਵੇਖ ਸਕਦੇ ਹੋ](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results)।

## ਟਰੇਡਮਾਰਕ

ਇਸ ਪ੍ਰੋਜੈਕਟ ਵਿੱਚ ਪ੍ਰੋਜੈਕਟਾਂ, ਉਤਪਾਦਾਂ ਜਾਂ ਸੇਵਾਵਾਂ ਦੇ ਟਰੇਡਮਾਰਕ ਜਾਂ ਲੋਗੋ ਸ਼ਾਮਿਲ ਹੋ ਸਕਦੇ ਹਨ। Microsoft ਦੇ ਟਰੇਡਮਾਰਕ ਜਾਂ ਲੋਗੋ ਦੀ ਪ੍ਰਮਾਣਤ ਵਰਤੋਂ ਇਸ ਗੱਲ ਦੀ ਵਿਸ਼ੇਸ਼ਤਾ ਹੈ ਅਤੇ ਇਸਨੂੰ [Microsoft ਦੇ ਟਰੇਡਮਾਰਕ ਅਤੇ ਬ੍ਰਾਂਡ ਦਿਸ਼ਾ-ਨਿਰਦੇਸ਼](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) ਦੇ ਅਨੁਸਾਰ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ। ਇਸ ਪ੍ਰੋਜੈਕਟ ਦੇ ਸੋਧੇ ਗਏ ਸੰਸਕਰਣਾਂ ਵਿੱਚ Microsoft ਦੇ ਟਰੇਡਮਾਰਕ ਜਾਂ ਲੋਗੋ ਦੀ ਵਰਤੋਂ ਗਲਤਫਹਮੀ ਪੈਦਾ ਨਹੀਂ ਕਰਨੀ ਚਾਹੀਦੀ ਅਤੇ ਨਾ ਹੀ ਇਹ Microsoft ਦੀ ਪੈਰੋਕਾਰੀ ਦਾ ਸੰਕੇਤ ਦੇਣੀ ਚਾਹੀਦੀ ਹੈ। ਤੀਜੀਆਂ ਪੱਖਾਂ ਦੇ ਟਰੇਡਮਾਰਕ ਜਾਂ ਲੋਗੋ ਦੀ ਕੋਈ ਵੀ ਵਰਤੋਂ ਉਸ ਤੀਜੇ ਪੱਖ ਦੀਆਂ ਨੀਤੀਆਂ ਦੇ ਅਧੀਨ ਹੋਵੇਗੀ।

## ਸਹਾਇਤਾ

ਜੇ ਤੁਸੀਂ ਫਸ ਜਾਂਦੇ ਹੋ ਜਾਂ AI ਐਪਸ ਬਣਾਉਣ ਬਾਰੇ ਕੋਈ ਸਵਾਲ ਹੈ, ਤਾਂ ਸ਼ਾਮਲ ਹੋਵੋ:

[![Azure AI Foundry ਡਿਸਕੋਰਡ](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

ਜੇ ਤੁਹਾਡੇ ਕੋਲ ਪ੍ਰੋਡਕਟ ਫੀਡਬੈਕ ਹੈ ਜਾਂ ਬਣਾਉਂਦੇ ਸਮੇਂ ਕੋਈ ਤਰੁੱਟੀਆਂ ਆਉਂਦੀਆਂ ਹਨ ਤਾਂ ਵੇਖੋ:

[![Azure AI Foundry ਡਿਵੈਲਪਰ ਫੋਰਮ](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
ਇਨਕਾਰਨਾਮਾ:
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਹਾਲਾਂਕਿ ਅਸੀਂ ਸ਼ੁੱਧਤਾ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਣਸਹੀਤੀਆਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਉਸਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਅਹਿਮ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫ਼ਾਰਿਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੇ ਉਪਯੋਗ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->