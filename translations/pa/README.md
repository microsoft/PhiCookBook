<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a73c59eecd7ad4ec494fd4333a29e208",
  "translation_date": "2025-10-11T10:50:10+00:00",
  "source_file": "README.md",
  "language_code": "pa"
}
-->
# ਫਾਈ ਕੂਕਬੁੱਕ: ਮਾਈਕਰੋਸਾਫਟ ਦੇ ਫਾਈ ਮਾਡਲਾਂ ਨਾਲ ਹੱਥ-ਵਰਤੋਂ ਉਦਾਹਰਨ

[![GitHub ਕੋਡਸਪੇਸ ਵਿੱਚ ਉਦਾਹਰਨਾਂ ਖੋਲ੍ਹੋ ਅਤੇ ਵਰਤੋ](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![ਡੈਵ ਕੰਟੇਨਰ ਵਿੱਚ ਖੋਲ੍ਹੋ](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub ਯੋਗਦਾਨਕਰਤਾ](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub ਮੁੱਦੇ](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub ਪੁਲ-ਰਿਕਵੇਸਟ](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PRs ਸਵਾਗਤ ਹੈ](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub ਵੇਖਣ ਵਾਲੇ](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub ਫੋਰਕ](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub ਸਟਾਰ](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

ਫਾਈ ਮਾਈਕਰੋਸਾਫਟ ਦੁਆਰਾ ਵਿਕਸਿਤ ਖੁੱਲ੍ਹੇ ਸਰੋਤ AI ਮਾਡਲਾਂ ਦੀ ਇੱਕ ਲੜੀ ਹੈ।

ਫਾਈ ਇਸ ਸਮੇਂ ਸਭ ਤੋਂ ਸ਼ਕਤੀਸ਼ਾਲੀ ਅਤੇ ਲਾਗਤ-ਪ੍ਰਭਾਵੀ ਛੋਟਾ ਭਾਸ਼ਾ ਮਾਡਲ (SLM) ਹੈ, ਜੋ ਬਹੁ-ਭਾਸ਼ਾ, ਤਰਕ, ਟੈਕਸਟ/ਚੈਟ ਜਨਰੇਸ਼ਨ, ਕੋਡਿੰਗ, ਚਿੱਤਰ, ਆਡੀਓ ਅਤੇ ਹੋਰ ਸਥਿਤੀਆਂ ਵਿੱਚ ਬਹੁਤ ਵਧੀਆ ਬੈਂਚਮਾਰਕ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ।

ਤੁਸੀਂ ਫਾਈ ਨੂੰ ਕਲਾਉਡ ਜਾਂ ਐਜ ਡਿਵਾਈਸਾਂ 'ਤੇ ਤੈਨਾਤ ਕਰ ਸਕਦੇ ਹੋ, ਅਤੇ ਤੁਸੀਂ ਸੀਮਤ ਕੰਪਿਊਟਿੰਗ ਸ਼ਕਤੀ ਨਾਲ ਆਸਾਨੀ ਨਾਲ ਜਨਰੇਟਿਵ AI ਐਪਲੀਕੇਸ਼ਨ ਬਣਾਉਣ ਲਈ ਇਸਦਾ ਵਰਤੋਂ ਕਰ ਸਕਦੇ ਹੋ।

ਇਹ ਸਰੋਤਾਂ ਦੀ ਵਰਤੋਂ ਸ਼ੁਰੂ ਕਰਨ ਲਈ ਹੇਠਾਂ ਦਿੱਤੇ ਕਦਮਾਂ ਦੀ ਪਾਲਣਾ ਕਰੋ:
1. **ਰੀਪੋਜ਼ਟਰੀ ਨੂੰ ਫੋਰਕ ਕਰੋ**: ਕਲਿੱਕ ਕਰੋ [![GitHub ਫੋਰਕ](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **ਰੀਪੋਜ਼ਟਰੀ ਕਲੋਨ ਕਰੋ**: `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Microsoft AI Discord Community ਵਿੱਚ ਸ਼ਾਮਲ ਹੋਵੋ ਅਤੇ ਮਾਹਰਾਂ ਅਤੇ ਹੋਰ ਡਿਵੈਲਪਰਾਂ ਨਾਲ ਮਿਲੋ**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![ਕਵਰ](../../imgs/cover.png)

### 🌐 ਬਹੁ-ਭਾਸ਼ਾ ਸਹਾਇਤਾ

#### GitHub Action ਰਾਹੀਂ ਸਹਾਇਤ (ਆਟੋਮੈਟਿਕ ਅਤੇ ਹਮੇਸ਼ਾ ਅਪ-ਟੂ-ਡੇਟ)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[ਅਰਬੀ](../ar/README.md) | [ਬੰਗਾਲੀ](../bn/README.md) | [ਬੁਲਗਾਰੀਆਈ](../bg/README.md) | [ਬਰਮੀ (ਮਿਆਂਮਾਰ)](../my/README.md) | [ਚੀਨੀ (ਸਰਲ)](../zh/README.md) | [ਚੀਨੀ (ਪ੍ਰੰਪਰਾਗਤ, ਹਾਂਗਕਾਂਗ)](../hk/README.md) | [ਚੀਨੀ (ਪ੍ਰੰਪਰਾਗਤ, ਮਕਾਉ)](../mo/README.md) | [ਚੀਨੀ (ਪ੍ਰੰਪਰਾਗਤ, ਤਾਈਵਾਨ)](../tw/README.md) | [ਕਰੋਏਸ਼ੀਆਈ](../hr/README.md) | [ਚੈਕ](../cs/README.md) | [ਡੈਨਿਸ਼](../da/README.md) | [ਡੱਚ](../nl/README.md) | [ਇਸਟੋਨੀਆਈ](../et/README.md) | [ਫਿਨਿਸ਼](../fi/README.md) | [ਫਰਾਂਸੀਸੀ](../fr/README.md) | [ਜਰਮਨ](../de/README.md) | [ਗ੍ਰੀਕ](../el/README.md) | [ਹਿਬਰੂ](../he/README.md) | [ਹਿੰਦੀ](../hi/README.md) | [ਹੰਗਰੀਆਈ](../hu/README.md) | [ਇੰਡੋਨੇਸ਼ੀਆਈ](../id/README.md) | [ਇਟਾਲੀਅਨ](../it/README.md) | [ਜਾਪਾਨੀ](../ja/README.md) | [ਕੋਰੀਆਈ](../ko/README.md) | [ਲਿਥੂਆਨੀਅਨ](../lt/README.md) | [ਮਲੇ](../ms/README.md) | [ਮਰਾਠੀ](../mr/README.md) | [ਨੇਪਾਲੀ](../ne/README.md) | [ਨਾਰਵੇਜੀਅਨ](../no/README.md) | [ਫਾਰਸੀ (ਫਾਰਸੀ)](../fa/README.md) | [ਪੋਲਿਸ਼](../pl/README.md) | [ਪੁਰਤਗਾਲੀ (ਬ੍ਰਾਜ਼ੀਲ)](../br/README.md) | [ਪੁਰਤਗਾਲੀ (ਪੁਰਤਗਾਲ)](../pt/README.md) | [ਪੰਜਾਬੀ (ਗੁਰਮੁਖੀ)](./README.md) | [ਰੋਮਾਨੀਆਈ](../ro/README.md) | [ਰੂਸੀ](../ru/README.md) | [ਸਰਬੀਆਈ (ਸਿਰਿਲਿਕ)](../sr/README.md) | [ਸਲੋਵਾਕ](../sk/README.md) | [ਸਲੋਵੇਨੀਆਈ](../sl/README.md) | [ਸਪੇਨੀ](../es/README.md) | [ਸਵਾਹਿਲੀ](../sw/README.md) | [ਸਵੀਡਿਸ਼](../sv/README.md) | [ਟੈਗਾਲੋਗ (ਫਿਲੀਪੀਨੋ)](../tl/README.md) | [ਤਮਿਲ](../ta/README.md) | [ਥਾਈ](../th/README.md) | [ਤੁਰਕੀ](../tr/README.md) | [ਯੂਕਰੇਨੀ](../uk/README.md) | [ਉਰਦੂ](../ur/README.md) | [ਵਿਯਤਨਾਮੀ](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## ਸਮੱਗਰੀ ਦੀ ਸੂਚੀ

- ਪਰਿਚਯ
  - [ਫਾਈ ਪਰਿਵਾਰ ਵਿੱਚ ਤੁਹਾਡਾ ਸਵਾਗਤ ਹੈ](./md/01.Introduction/01/01.PhiFamily.md)
  - [ਆਪਣੇ ਵਾਤਾਵਰਣ ਨੂੰ ਸੈਟਅੱਪ ਕਰਨਾ](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [ਮੁੱਖ ਤਕਨਾਲੋਜੀਆਂ ਨੂੰ ਸਮਝਣਾ](./md/01.Introduction/01/01.Understandingtech.md)
  - [ਫਾਈ ਮਾਡਲਾਂ ਲਈ AI ਸੁਰੱਖਿਆ](./md/01.Introduction/01/01.AISafety.md)
  - [ਫਾਈ ਹਾਰਡਵੇਅਰ ਸਹਾਇਤਾ](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [ਫਾਈ ਮਾਡਲਾਂ ਅਤੇ ਪਲੇਟਫਾਰਮਾਂ 'ਤੇ ਉਪਲਬਧਤਾ](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Guidance-ai ਅਤੇ ਫਾਈ ਦੀ ਵਰਤੋਂ](./md/01.Introduction/01/01.Guidance.md)
  - [GitHub Marketplace ਮਾਡਲ](https://github.com/marketplace/models)
  - [Azure AI Model Catalog](https://ai.azure.com)

- ਵੱਖ-ਵੱਖ ਵਾਤਾਵਰਣਾਂ ਵਿੱਚ ਫਾਈ ਇੰਫਰੈਂਸ
    - [Hugging face](./md/01.Introduction/02/01.HF.md)
    - [GitHub ਮਾਡਲ](./md/01.Introduction/02/02.GitHubModel.md)
    - [Azure AI Foundry Model Catalog](./md/01.Introduction/02/03.AzureAIFoundry.md)
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
    - [onnxruntime ਲਈ Generative AI extensions ਦੀ ਵਰਤੋਂ ਕਰਕੇ Phi-3.5 / 4 ਨੂੰ ਮਾਤਰਾ](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Intel OpenVINO ਦੀ ਵਰਤੋਂ ਕਰਕੇ Phi-3.5 / 4 ਨੂੰ ਮਾਤਰਾ](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Apple MLX Framework ਦੀ ਵਰਤੋਂ ਕਰਕੇ Phi-3.5 / 4 ਨੂੰ ਮਾਤਰਾ](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

- ਫਾਈ ਦਾ ਮੁਲਾਂਕਨ
    - [ਜਵਾਬਦੇਹ AI](./md/01.Introduction/05/ResponsibleAI.md)
    - [ਮੁਲਾਂਕਨ ਲਈ Azure AI Foundry](./md/01.Introduction/05/AIFoundry.md)
    - [ਮੁਲਾਂਕਨ ਲਈ Promptflow ਦੀ ਵਰਤੋਂ](./md/01.Introduction/05/Promptflow.md)

- Azure AI Search ਨਾਲ RAG
    - [Azure AI Search ਨਾਲ Phi-4-mini ਅਤੇ Phi-4-multimodal (RAG) ਦੀ ਵਰਤੋਂ ਕਰਨ ਦਾ ਤਰੀਕਾ](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- ਫਾਈ ਐਪਲੀਕੇਸ਼ਨ ਵਿਕਾਸ ਉਦਾਹਰਨ
  - ਟੈਕਸਟ ਅਤੇ ਚੈਟ ਐਪਲੀਕੇਸ਼ਨ
    - Phi-4 ਉਦਾਹਰਨ 🆕
      - [📓] [Phi-4-mini ONNX Model ਨਾਲ ਚੈਟ ਕਰੋ](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Phi-4 local ONNX Model .NET ਨਾਲ ਚੈਟ ਕਰੋ](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Sementic Kernel ਦੀ ਵਰਤੋਂ ਕਰਕੇ Phi-4 ONNX ਨਾਲ .NET Console ਐਪ ਵਿੱਚ ਚੈਟ ਕਰੋ](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Phi-3 / 3.5 ਉਦਾਹਰਨ
      - [ਬ੍ਰਾਊਜ਼ਰ ਵਿੱਚ Phi3, ONNX Runtime Web ਅਤੇ WebGPU ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਲੋਕਲ ਚੈਟਬੋਟ](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVino Chat](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [ਮਲਟੀ ਮਾਡਲ - ਇੰਟਰਐਕਟਿਵ Phi-3-mini ਅਤੇ OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - ਇੱਕ ਰੈਪਰ ਬਣਾਉਣਾ ਅਤੇ MLFlow ਨਾਲ Phi-3 ਦੀ ਵਰਤੋਂ](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [ਮਾਡਲ ਅਪਟਿਮਾਈਜ਼ੇਸ਼ਨ - ONNX Runtime Web ਲਈ Phi-3-min ਮਾਡਲ ਨੂੰ Olive ਨਾਲ ਕਿਵੇਂ ਅਪਟਿਮਾਈਜ਼ ਕਰਨਾ ਹੈ](https://github.com/microsoft/Olive/tree/main/examples/phi3)
- [WinUI3 ਐਪ ਫਾਈ-3 ਮਿਨੀ-4k-ਇੰਸਟ੍ਰਕਟ-onnx ਨਾਲ](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
- [WinUI3 ਮਲਟੀ ਮਾਡਲ AI ਪਾਵਰਡ ਨੋਟਸ ਐਪ ਸੈਂਪਲ](https://github.com/microsoft/ai-powered-notes-winui3-sample)
- [ਕਸਟਮ ਫਾਈ-3 ਮਾਡਲਾਂ ਨੂੰ ਪ੍ਰੋਮਪਟ ਫਲੋ ਨਾਲ ਫਾਈਨ-ਟਿਊਨ ਅਤੇ ਇੰਟੀਗ੍ਰੇਟ ਕਰੋ](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
- [Azure AI Foundry ਵਿੱਚ ਪ੍ਰੋਮਪਟ ਫਲੋ ਨਾਲ ਕਸਟਮ ਫਾਈ-3 ਮਾਡਲਾਂ ਨੂੰ ਫਾਈਨ-ਟਿਊਨ ਅਤੇ ਇੰਟੀਗ੍ਰੇਟ ਕਰੋ](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
- [Microsoft ਦੇ ਜ਼ਿੰਮੇਵਾਰ AI ਸਿਧਾਂਤਾਂ 'ਤੇ ਧਿਆਨ ਦੇਣ ਵਾਲੇ Azure AI Foundry ਵਿੱਚ ਫਾਈਨ-ਟਿਊਨ ਕੀਤੇ ਫਾਈ-3 / ਫਾਈ-3.5 ਮਾਡਲ ਦਾ ਮੁਲਾਂਕਨ ਕਰੋ](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
- [📓] [ਫਾਈ-3.5-ਮਿਨੀ-ਇੰਸਟ੍ਰਕਟ ਭਾਸ਼ਾ ਅਨੁਮਾਨ ਸੈਂਪਲ (ਚੀਨੀ/ਅੰਗਰੇਜ਼ੀ)](../../md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
- [ਫਾਈ-3.5-ਇੰਸਟ੍ਰਕਟ WebGPU RAG ਚੈਟਬੋਟ](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
- [Windows GPU ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਫਾਈ-3.5-ਇੰਸਟ੍ਰਕਟ ONNX ਨਾਲ ਪ੍ਰੋਮਪਟ ਫਲੋ ਹੱਲ ਬਣਾਉਣਾ](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
- [Microsoft ਫਾਈ-3.5 tflite ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਐਂਡਰਾਇਡ ਐਪ ਬਣਾਉਣਾ](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
- [Microsoft.ML.OnnxRuntime ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਸਥਾਨਕ ONNX ਫਾਈ-3 ਮਾਡਲ ਨਾਲ Q&A .NET ਉਦਾਹਰਨ](../../md/04.HOL/dotnet/src/LabsPhi301)
- [ਸੈਮੈਂਟਿਕ ਕਰਨਲ ਅਤੇ ਫਾਈ-3 ਨਾਲ ਕਨਸੋਲ ਚੈਟ .NET ਐਪ](../../md/04.HOL/dotnet/src/LabsPhi302)

- Azure AI ਇੰਫਰੈਂਸ SDK ਕੋਡ ਅਧਾਰਿਤ ਸੈਂਪਲ
  - ਫਾਈ-4 ਸੈਂਪਲ 🆕
    - [📓] [ਫਾਈ-4-ਮਲਟੀਮੋਡਲ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਪ੍ਰੋਜੈਕਟ ਕੋਡ ਜਨਰੇਟ ਕਰੋ](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
  - ਫਾਈ-3 / 3.5 ਸੈਂਪਲ
    - [Microsoft ਫਾਈ-3 ਪਰਿਵਾਰ ਨਾਲ ਆਪਣਾ Visual Studio Code GitHub Copilot Chat ਬਣਾਓ](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
    - [GitHub ਮਾਡਲਾਂ ਦੁਆਰਾ ਫਾਈ-3.5 ਨਾਲ ਆਪਣਾ Visual Studio Code Chat Copilot Agent ਬਣਾਓ](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

- ਐਡਵਾਂਸਡ ਰੀਜ਼ਨਿੰਗ ਸੈਂਪਲ
  - ਫਾਈ-4 ਸੈਂਪਲ 🆕
    - [📓] [ਫਾਈ-4-ਮਿਨੀ-ਰੀਜ਼ਨਿੰਗ ਜਾਂ ਫਾਈ-4-ਰੀਜ਼ਨਿੰਗ ਸੈਂਪਲ](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
    - [📓] [Microsoft Olive ਨਾਲ ਫਾਈ-4-ਮਿਨੀ-ਰੀਜ਼ਨਿੰਗ ਨੂੰ ਫਾਈਨ-ਟਿਊਨ ਕਰਨਾ](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
    - [📓] [Apple MLX ਨਾਲ ਫਾਈ-4-ਮਿਨੀ-ਰੀਜ਼ਨਿੰਗ ਨੂੰ ਫਾਈਨ-ਟਿਊਨ ਕਰਨਾ](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
    - [📓] [GitHub ਮਾਡਲਾਂ ਨਾਲ ਫਾਈ-4-ਮਿਨੀ-ਰੀਜ਼ਨਿੰਗ](../../md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
    - [📓] [Azure AI Foundry ਮਾਡਲਾਂ ਨਾਲ ਫਾਈ-4-ਮਿਨੀ-ਰੀਜ਼ਨਿੰਗ](../../md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
- ਡੈਮੋ
    - [Hugging Face Spaces 'ਤੇ ਫਾਈ-4-ਮਿਨੀ ਡੈਮੋ](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
    - [Hugging Face Spaces 'ਤੇ ਫਾਈ-4-ਮਲਟੀਮੋਡਲ ਡੈਮੋ](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
- ਵਿਜ਼ਨ ਸੈਂਪਲ
  - ਫਾਈ-4 ਸੈਂਪਲ 🆕
    - [📓] [ਫਾਈ-4-ਮਲਟੀਮੋਡਲ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਚਿੱਤਰਾਂ ਨੂੰ ਪੜ੍ਹੋ ਅਤੇ ਕੋਡ ਜਨਰੇਟ ਕਰੋ](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md)
  - ਫਾਈ-3 / 3.5 ਸੈਂਪਲ
    - [📓][ਫਾਈ-3-ਵਿਜ਼ਨ-ਚਿੱਤਰ ਟੈਕਸਟ ਤੋਂ ਟੈਕਸਟ](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
    - [ਫਾਈ-3-ਵਿਜ਼ਨ-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
    - [📓][ਫਾਈ-3-ਵਿਜ਼ਨ CLIP ਐਮਬੈਡਿੰਗ](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
    - [ਡੈਮੋ: ਫਾਈ-3 ਰੀਸਾਈਕਲਿੰਗ](https://github.com/jennifermarsman/PhiRecycling/)
    - [ਫਾਈ-3-ਵਿਜ਼ਨ - ਵਿਜ਼ੁਅਲ ਭਾਸ਼ਾ ਸਹਾਇਕ - ਫਾਈ3-ਵਿਜ਼ਨ ਅਤੇ OpenVINO ਨਾਲ](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
    - [ਫਾਈ-3 ਵਿਜ਼ਨ Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
    - [ਫਾਈ-3 ਵਿਜ਼ਨ OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
    - [📓][ਫਾਈ-3.5 ਵਿਜ਼ਨ ਮਲਟੀ-ਫਰੇਮ ਜਾਂ ਮਲਟੀ-ਚਿੱਤਰ ਸੈਂਪਲ](../../md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
    - [Microsoft.ML.OnnxRuntime .NET ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਸਥਾਨਕ ONNX ਮਾਡਲ ਨਾਲ ਫਾਈ-3 ਵਿਜ਼ਨ](../../md/04.HOL/dotnet/src/LabsPhi303)
    - [Microsoft.ML.OnnxRuntime .NET ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਮੀਨੂ ਅਧਾਰਿਤ ਸਥਾਨਕ ONNX ਮਾਡਲ ਨਾਲ ਫਾਈ-3 ਵਿਜ਼ਨ](../../md/04.HOL/dotnet/src/LabsPhi304)

- ਗਣਿਤ ਸੈਂਪਲ
  - ਫਾਈ-4-ਮਿਨੀ-ਫਲੈਸ਼-ਰੀਜ਼ਨਿੰਗ-ਇੰਸਟ੍ਰਕਟ ਸੈਂਪਲ 🆕 [ਫਾਈ-4-ਮਿਨੀ-ਫਲੈਸ਼-ਰੀਜ਼ਨਿੰਗ-ਇੰਸਟ੍ਰਕਟ ਨਾਲ ਗਣਿਤ ਡੈਮੋ](../../md/02.Application/09.Math/MathDemo.ipynb)

- ਆਡੀਓ ਸੈਂਪਲ
  - ਫਾਈ-4 ਸੈਂਪਲ 🆕
    - [📓] [ਫਾਈ-4-ਮਲਟੀਮੋਡਲ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਆਡੀਓ ਟ੍ਰਾਂਸਕ੍ਰਿਪਟਸ ਕੱਢਣਾ](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
    - [📓] [ਫਾਈ-4-ਮਲਟੀਮੋਡਲ ਆਡੀਓ ਸੈਂਪਲ](../../md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
    - [📓] [ਫਾਈ-4-ਮਲਟੀਮੋਡਲ ਸਪੀਚ ਟ੍ਰਾਂਸਲੇਸ਼ਨ ਸੈਂਪਲ](../../md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
    - [.NET ਕਨਸੋਲ ਐਪਲੀਕੇਸ਼ਨ ਫਾਈ-4-ਮਲਟੀਮੋਡਲ ਆਡੀਓ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਆਡੀਓ ਫਾਈਲ ਦਾ ਵਿਸ਼ਲੇਸ਼ਣ ਕਰਨ ਅਤੇ ਟ੍ਰਾਂਸਕ੍ਰਿਪਟ ਜਨਰੇਟ ਕਰਨ ਲਈ](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

- MOE ਸੈਂਪਲ
  - ਫਾਈ-3 / 3.5 ਸੈਂਪਲ
    - [📓] [ਫਾਈ-3.5 ਮਿਕਸਚਰ ਆਫ ਐਕਸਪਰਟਸ ਮਾਡਲ (MoEs) ਸੋਸ਼ਲ ਮੀਡੀਆ ਸੈਂਪਲ](../../md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
    - [📓] [NVIDIA NIM Phi-3 MOE, Azure AI Search, ਅਤੇ LlamaIndex ਨਾਲ Retrieval-Augmented Generation (RAG) ਪਾਈਪਲਾਈਨ ਬਣਾਉਣਾ](../../md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)

- ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਸੈਂਪਲ
  - ਫਾਈ-4 ਸੈਂਪਲ 🆕
    - [📓] [ਫਾਈ-4-ਮਿਨੀ ਨਾਲ ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਦੀ ਵਰਤੋਂ](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
    - [📓] [ਫਾਈ-4-ਮਿਨੀ ਨਾਲ ਮਲਟੀ-ਏਜੰਟਸ ਬਣਾਉਣ ਲਈ ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਦੀ ਵਰਤੋਂ](../../md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
    - [📓] [Ollama ਨਾਲ ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਦੀ ਵਰਤੋਂ](../../md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
    - [📓] [ONNX ਨਾਲ ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਦੀ ਵਰਤੋਂ](../../md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)

- ਮਲਟੀਮੋਡਲ ਮਿਕਸਿੰਗ ਸੈਂਪਲ
  - ਫਾਈ-4 ਸੈਂਪਲ 🆕
    - [📓] [ਫਾਈ-4-ਮਲਟੀਮੋਡਲ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਤਕਨਾਲੋਜੀ ਜਰਨਲਿਸਟ ਬਣੋ](../../md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
    - [.NET ਕਨਸੋਲ ਐਪਲੀਕੇਸ਼ਨ ਫਾਈ-4-ਮਲਟੀਮੋਡਲ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਚਿੱਤਰਾਂ ਦਾ ਵਿਸ਼ਲੇਸ਼ਣ ਕਰਨ ਲਈ](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- ਫਾਈਨ-ਟਿਊਨਿੰਗ ਫਾਈ ਸੈਂਪਲ
  - [ਫਾਈਨ-ਟਿਊਨਿੰਗ ਸਥਿਤੀਆਂ](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [ਫਾਈਨ-ਟਿਊਨਿੰਗ ਵਿਰੁੱਧ RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [ਫਾਈਨ-ਟਿਊਨਿੰਗ ਫਾਈ-3 ਨੂੰ ਉਦਯੋਗ ਵਿਸ਼ੇਸ਼ਗਿਆ ਬਣਾਉਣ ਦਿਓ](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [VS Code ਲਈ AI ਟੂਲਕਿਟ ਨਾਲ ਫਾਈ-3 ਨੂੰ ਫਾਈਨ-ਟਿਊਨ ਕਰਨਾ](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Azure Machine Learning Service ਨਾਲ ਫਾਈ-3 ਨੂੰ ਫਾਈਨ-ਟਿਊਨ ਕਰਨਾ](./md/03.FineTuning/Introduce_AzureML.md)
  - [Lora ਨਾਲ ਫਾਈ-3 ਨੂੰ ਫਾਈਨ-ਟਿਊਨ ਕਰਨਾ](./md/03.FineTuning/FineTuning_Lora.md)
  - [QLora ਨਾਲ ਫਾਈ-3 ਨੂੰ ਫਾਈਨ-ਟਿਊਨ ਕਰਨਾ](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Azure AI Foundry ਨਾਲ ਫਾਈ-3 ਨੂੰ ਫਾਈਨ-ਟਿਊਨ ਕਰਨਾ](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Azure ML CLI/SDK ਨਾਲ ਫਾਈ-3 ਨੂੰ ਫਾਈਨ-ਟਿਊਨ ਕਰਨਾ](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Microsoft Olive ਨਾਲ ਫਾਈਨ-ਟਿਊਨਿੰਗ](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Microsoft Olive Hands-On Lab ਨਾਲ ਫਾਈਨ-ਟਿਊਨਿੰਗ](./md/03.FineTuning/olive-lab/readme.md)
  - [Weights and Bias ਨਾਲ ਫਾਈ-3-ਵਿਜ਼ਨ ਨੂੰ ਫਾਈਨ-ਟਿਊਨ ਕਰਨਾ](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [Apple MLX Framework ਨਾਲ ਫਾਈ-3 ਨੂੰ ਫਾਈਨ-ਟਿਊਨ ਕਰਨਾ](./md/03.FineTuning/FineTuning_MLX.md)
  - [ਫਾਈ-3-ਵਿਜ਼ਨ ਨੂੰ ਫਾਈਨ-ਟਿਊਨ ਕਰਨਾ (ਆਧਿਕਾਰਿਕ ਸਹਾਇਤਾ)](./md/03.FineTuning/FineTuning_Vision.md)
  - [Kaito AKS, Azure Containers ਨਾਲ ਫਾਈ-3 ਨੂੰ ਫਾਈਨ-ਟਿਊਨ ਕਰਨਾ (ਆਧਿਕਾਰਿਕ ਸਹਾਇਤਾ)](./md/03.FineTuning/FineTuning_Kaito.md)
  - [ਫਾਈ-3 ਅਤੇ 3.5 ਵਿਜ਼ਨ ਨੂੰ ਫਾਈਨ-ਟਿਊਨ ਕਰਨਾ](https://github.com/2U1/Phi3-Vision-Finetune)

- ਹੈਂਡਸ-ਆਨ ਲੈਬ
  - [ਅਗਲੇ ਪੱਧਰ ਦੇ ਮਾਡਲਾਂ ਦੀ ਖੋਜ: LLMs, SLMs, ਸਥਾਨਕ ਵਿਕਾਸ ਅਤੇ ਹੋਰ](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [NLP ਦੀ ਸੰਭਾਵਨਾ ਨੂੰ ਖੋਲ੍ਹਣਾ: Microsoft Olive ਨਾਲ ਫਾਈਨ-ਟਿਊਨਿੰਗ](https://github.com/azure/Ignite_FineTuning_workshop)

- ਅਕਾਦਮਿਕ ਰਿਸਰਚ ਪੇਪਰ ਅਤੇ ਪ੍ਰਕਾਸ਼ਨ
  - [Textbooks Are All You Need II: phi-1.5 ਤਕਨੀਕੀ ਰਿਪੋਰਟ](https://arxiv.org/abs/2309.05463)
  - [Phi-3 ਤਕਨੀਕੀ ਰਿਪੋਰਟ: ਇੱਕ ਬਹੁਤ ਯੋਗ ਭਾਸ਼ਾ ਮਾਡਲ ਜੋ ਤੁਹਾਡੇ ਫੋਨ 'ਤੇ ਸਥਾਨਕ ਤੌਰ 'ਤੇ ਚੱਲਦਾ ਹੈ](https://arxiv.org/abs/2404.14219)
  - [Phi-4 ਤਕਨੀਕੀ ਰਿਪੋਰਟ](https://arxiv.org/abs/2412.08905)
  - [Phi-4-Mini ਤਕਨੀਕੀ ਰਿਪੋਰਟ: Mixture-of-LoRAs ਦੁਆਰਾ ਸੰਕੁਚਿਤ ਪਰ ਸ਼ਕਤੀਸ਼ਾਲੀ ਮਲਟੀਮੋਡਲ ਭਾਸ਼ਾ ਮਾਡਲ](https://arxiv.org/abs/2503.01743)
  - [ਵਾਹਨ ਵਿੱਚ ਫੰਕਸ਼ਨ-ਕਾਲਿੰਗ ਲਈ ਛੋਟੇ ਭਾਸ਼ਾ ਮਾਡਲਾਂ ਦਾ ਅਪਟਾਈਮਾਈਜ਼ੇਸ਼ਨ](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) ਬਹੁ-ਚੋਣ ਪ੍ਰਸ਼ਨ ਉੱਤਰ ਦੇਣ ਲਈ PHI-3 ਨੂੰ ਫਾਈਨ-ਟਿਊਨ ਕਰਨਾ: ਵਿਧੀ, ਨਤੀਜੇ, ਅਤੇ ਚੁਣੌਤੀਆਂ](https://arxiv.org/abs/2501.01588)
  - [Phi-4-ਤਰਕ ਤਕਨੀਕੀ ਰਿਪੋਰਟ](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Phi-4-mini-ਤਰਕ ਤਕਨੀਕੀ ਰਿਪੋਰਟ](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Phi ਮਾਡਲਾਂ ਦੀ ਵਰਤੋਂ

### Azure AI Foundry 'ਤੇ Phi

ਤੁਹਾਨੂੰ Microsoft Phi ਦੀ ਵਰਤੋਂ ਕਰਨ ਅਤੇ ਵੱਖ-ਵੱਖ ਹਾਰਡਵੇਅਰ ਡਿਵਾਈਸਾਂ ਵਿੱਚ E2E ਹੱਲ ਬਣਾਉਣ ਬਾਰੇ ਸਿੱਖਣ ਦਾ ਮੌਕਾ ਮਿਲੇਗਾ। ਆਪਣੇ ਲਈ Phi ਦਾ ਅਨੁਭਵ ਕਰਨ ਲਈ, ਮਾਡਲਾਂ ਨਾਲ ਖੇਡਣਾ ਸ਼ੁਰੂ ਕਰੋ ਅਤੇ ਆਪਣੇ ਸਥਿਤੀਆਂ ਲਈ Phi ਨੂੰ ਕਸਟਮਾਈਜ਼ ਕਰੋ। [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai) 'ਤੇ ਜਾ ਕੇ ਹੋਰ ਜਾਣਕਾਰੀ ਪ੍ਰਾਪਤ ਕਰੋ। [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md) ਨਾਲ ਸ਼ੁਰੂਆਤ ਕਰਨ ਲਈ ਸਿੱਖੋ।

**ਪਲੇਗਰਾਊਂਡ**
ਹਰ ਮਾਡਲ ਲਈ ਇੱਕ ਸਮਰਪਿਤ ਪਲੇਗਰਾਊਂਡ ਹੈ ਜਿਸ ਵਿੱਚ ਮਾਡਲ ਦੀ ਜਾਂਚ ਕੀਤੀ ਜਾ ਸਕਦੀ ਹੈ। [Azure AI Playground](https://aka.ms/try-phi3).

### GitHub ਮਾਡਲਾਂ 'ਤੇ Phi

ਤੁਹਾਨੂੰ Microsoft Phi ਦੀ ਵਰਤੋਂ ਕਰਨ ਅਤੇ ਵੱਖ-ਵੱਖ ਹਾਰਡਵੇਅਰ ਡਿਵਾਈਸਾਂ ਵਿੱਚ E2E ਹੱਲ ਬਣਾਉਣ ਬਾਰੇ ਸਿੱਖਣ ਦਾ ਮੌਕਾ ਮਿਲੇਗਾ। ਆਪਣੇ ਲਈ Phi ਦਾ ਅਨੁਭਵ ਕਰਨ ਲਈ, ਮਾਡਲ ਨਾਲ ਖੇਡਣਾ ਸ਼ੁਰੂ ਕਰੋ ਅਤੇ ਆਪਣੇ ਸਥਿਤੀਆਂ ਲਈ Phi ਨੂੰ ਕਸਟਮਾਈਜ਼ ਕਰੋ। [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) 'ਤੇ ਜਾ ਕੇ ਹੋਰ ਜਾਣਕਾਰੀ ਪ੍ਰਾਪਤ ਕਰੋ। [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md) ਨਾਲ ਸ਼ੁਰੂਆਤ ਕਰਨ ਲਈ ਸਿੱਖੋ।

**ਪਲੇਗਰਾਊਂਡ**
ਹਰ ਮਾਡਲ ਲਈ ਇੱਕ [ਪਲੇਗਰਾਊਂਡ](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) ਹੈ ਜਿਸ ਵਿੱਚ ਮਾਡਲ ਦੀ ਜਾਂਚ ਕੀਤੀ ਜਾ ਸਕਦੀ ਹੈ।

### Hugging Face 'ਤੇ Phi

ਤੁਸੀਂ ਮਾਡਲ ਨੂੰ [Hugging Face](https://huggingface.co/microsoft) 'ਤੇ ਵੀ ਲੱਭ ਸਕਦੇ ਹੋ।

**ਪਲੇਗਰਾਊਂਡ**
 [Hugging Chat ਪਲੇਗਰਾਊਂਡ](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## ਜ਼ਿੰਮੇਵਾਰ AI 

Microsoft ਆਪਣੇ ਗਾਹਕਾਂ ਨੂੰ ਜ਼ਿੰਮੇਵਾਰੀ ਨਾਲ AI ਉਤਪਾਦਾਂ ਦੀ ਵਰਤੋਂ ਕਰਨ ਵਿੱਚ ਮਦਦ ਕਰਨ, ਸਾਡੇ ਸਿੱਖਣਾਂ ਨੂੰ ਸਾਂਝਾ ਕਰਨ, ਅਤੇ ਭਰੋਸੇ-ਅਧਾਰਿਤ ਸਾਂਝੇਦਾਰੀਆਂ ਬਣਾਉਣ ਲਈ ਵਚਨਬੱਧ ਹੈ। Transparency Notes ਅਤੇ Impact Assessments ਵਰਗੇ ਟੂਲਾਂ ਰਾਹੀਂ ਸਾਡੇ ਬਹੁਤ ਸਾਰੇ ਸਰੋਤ [https://aka.ms/RAI](https://aka.ms/RAI) 'ਤੇ ਮਿਲ ਸਕਦੇ ਹਨ। Microsoft ਦਾ ਜ਼ਿੰਮੇਵਾਰ AI ਲਈ ਦ੍ਰਿਸ਼ਕੋਣ ਸਾਡੇ AI ਨਿਯਮਾਂ 'ਤੇ ਅਧਾਰਿਤ ਹੈ: ਨਿਰਪੱਖਤਾ, ਭਰੋਸੇਯੋਗਤਾ ਅਤੇ ਸੁਰੱਖਿਆ, ਗੋਪਨੀਯਤਾ ਅਤੇ ਸੁਰੱਖਿਆ, ਸ਼ਾਮਿਲਤਾ, ਪਾਰਦਰਸ਼ਤਾ, ਅਤੇ ਜਵਾਬਦੇਹੀ।

ਵੱਡੇ ਪੱਧਰ ਦੇ ਕੁਦਰਤੀ ਭਾਸ਼ਾ, ਚਿੱਤਰ, ਅਤੇ ਬੋਲ ਮਾਡਲ - ਜਿਵੇਂ ਕਿ ਇਸ ਨਮੂਨੇ ਵਿੱਚ ਵਰਤੇ ਗਏ ਹਨ - ਅਨੁਚਿਤ, ਅਵਿਸ਼ਵਾਸ਼ਯੋਗ, ਜਾਂ ਅਪਮਾਨਜਨਕ ਤਰੀਕੇ ਨਾਲ ਵਿਹਾਰ ਕਰ ਸਕਦੇ ਹਨ, ਜਿਸ ਨਾਲ ਨੁਕਸਾਨ ਹੋ ਸਕਦਾ ਹੈ। ਕਿਰਪਾ ਕਰਕੇ [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) ਨੂੰ ਪੜ੍ਹੋ ਤਾਂ ਜੋ ਖਤਰੇ ਅਤੇ ਸੀਮਾਵਾਂ ਬਾਰੇ ਜਾਣਕਾਰੀ ਪ੍ਰਾਪਤ ਕੀਤੀ ਜਾ ਸਕੇ।

ਇਹ ਖਤਰੇ ਘਟਾਉਣ ਲਈ ਸਿਫਾਰਸ਼ੀ ਤਰੀਕਾ ਇਹ ਹੈ ਕਿ ਆਪਣੇ ਆਰਕੀਟੈਕਚਰ ਵਿੱਚ ਇੱਕ ਸੁਰੱਖਿਆ ਪ੍ਰਣਾਲੀ ਸ਼ਾਮਿਲ ਕਰੋ ਜੋ ਹਾਨਿਕਾਰਕ ਵਿਹਾਰ ਦੀ ਪਛਾਣ ਅਤੇ ਰੋਕਥਾਮ ਕਰ ਸਕੇ। [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) ਇੱਕ ਸਵਤੰਤਰ ਸੁਰੱਖਿਆ ਪਰਤ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ, ਜੋ ਐਪਲੀਕੇਸ਼ਨ ਅਤੇ ਸੇਵਾਵਾਂ ਵਿੱਚ ਹਾਨਿਕਾਰਕ ਯੂਜ਼ਰ-ਜਨਰੇਟਡ ਅਤੇ AI-ਜਨਰੇਟਡ ਸਮੱਗਰੀ ਦੀ ਪਛਾਣ ਕਰਨ ਦੇ ਯੋਗ ਹੈ। Azure AI Content Safety ਵਿੱਚ ਟੈਕਸਟ ਅਤੇ ਚਿੱਤਰ APIs ਸ਼ਾਮਿਲ ਹਨ ਜੋ ਤੁਹਾਨੂੰ ਹਾਨਿਕਾਰਕ ਸਮੱਗਰੀ ਦੀ ਪਛਾਣ ਕਰਨ ਦੀ ਆਗਿਆ ਦਿੰਦੇ ਹਨ। Azure AI Foundry ਵਿੱਚ, Content Safety ਸੇਵਾ ਤੁਹਾਨੂੰ ਵੱਖ-ਵੱਖ ਮੋਡੈਲਿਟੀਜ਼ ਵਿੱਚ ਹਾਨਿਕਾਰਕ ਸਮੱਗਰੀ ਦੀ ਪਛਾਣ ਕਰਨ ਲਈ ਨਮੂਨਾ ਕੋਡ ਦੇਖਣ, ਖੋਜਣ ਅਤੇ ਅਜ਼ਮਾਉਣ ਦੀ ਆਗਿਆ ਦਿੰਦੀ ਹੈ। ਹੇਠਾਂ ਦਿੱਤੀ [quickstart documentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) ਤੁਹਾਨੂੰ ਸੇਵਾ ਲਈ ਬੇਨਤੀ ਕਰਨ ਦੇ ਰਾਹਦਰੀ ਦਿਖਾਉਂਦੀ ਹੈ।

ਇੱਕ ਹੋਰ ਪੱਖ ਜਿਸ ਨੂੰ ਧਿਆਨ ਵਿੱਚ ਰੱਖਣ ਦੀ ਲੋੜ ਹੈ ਉਹ ਹੈ ਸਮੁੱਚੇ ਐਪਲੀਕੇਸ਼ਨ ਦੀ ਕਾਰਗੁਜ਼ਾਰੀ। ਬਹੁ-ਮੋਡਲ ਅਤੇ ਬਹੁ-ਮਾਡਲ ਐਪਲੀਕੇਸ਼ਨਾਂ ਨਾਲ, ਅਸੀਂ ਕਾਰਗੁਜ਼ਾਰੀ ਨੂੰ ਇਸ ਤਰੀਕੇ ਨਾਲ ਪਰਿਭਾਸ਼ਿਤ ਕਰਦੇ ਹਾਂ ਕਿ ਪ੍ਰਣਾਲੀ ਤੁਹਾਡੇ ਅਤੇ ਤੁਹਾਡੇ ਯੂਜ਼ਰਾਂ ਦੀ ਉਮੀਦਾਂ ਅਨੁਸਾਰ ਕੰਮ ਕਰਦੀ ਹੈ, ਜਿਸ ਵਿੱਚ ਹਾਨਿਕਾਰਕ ਆਉਟਪੁੱਟ ਜਨਰੇਟ ਨਾ ਕਰਨਾ ਸ਼ਾਮਿਲ ਹੈ। ਇਹ ਮਹੱਤਵਪੂਰਨ ਹੈ ਕਿ [Performance and Quality and Risk and Safety evaluators](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਆਪਣੇ ਸਮੁੱਚੇ ਐਪਲੀਕੇਸ਼ਨ ਦੀ ਕਾਰਗੁਜ਼ਾਰੀ ਦਾ ਮੁਲਾਂਕਨ ਕੀਤਾ ਜਾਵੇ। ਤੁਹਾਡੇ ਕੋਲ [custom evaluators](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators) ਬਣਾਉਣ ਅਤੇ ਮੁਲਾਂਕਨ ਕਰਨ ਦੀ ਯੋਗਤਾ ਵੀ ਹੈ।

ਤੁਸੀਂ ਆਪਣੇ ਵਿਕਾਸ ਵਾਤਾਵਰਣ ਵਿੱਚ [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਆਪਣੀ AI ਐਪਲੀਕੇਸ਼ਨ ਦਾ ਮੁਲਾਂਕਨ ਕਰ ਸਕਦੇ ਹੋ। ਦਿੱਤੇ ਗਏ ਟੈਸਟ ਡਾਟਾਸੈਟ ਜਾਂ ਟਾਰਗਟ ਦੇ ਅਧਾਰ 'ਤੇ, ਤੁਹਾਡੇ ਜਨਰੇਟਿਵ AI ਐਪਲੀਕੇਸ਼ਨ ਜਨਰੇਸ਼ਨ ਨੂੰ ਤੁਹਾਡੇ ਚੋਣ ਦੇ ਬਿਲਟ-ਇਨ ਮੁਲਾਂਕਨਕਰਤਾ ਜਾਂ ਕਸਟਮ ਮੁਲਾਂਕਨਕਰਤਾ ਨਾਲ ਮਾਤਰਕ ਤੌਰ 'ਤੇ ਮਾਪਿਆ ਜਾਂਦਾ ਹੈ। ਆਪਣੇ ਪ੍ਰਣਾਲੀ ਦਾ ਮੁਲਾਂਕਨ ਕਰਨ ਲਈ Azure AI Evaluation SDK ਨਾਲ ਸ਼ੁਰੂਆਤ ਕਰਨ ਲਈ, ਤੁਸੀਂ [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) ਦੀ ਪਾਲਣਾ ਕਰ ਸਕਦੇ ਹੋ। ਜਦੋਂ ਤੁਸੀਂ ਇੱਕ ਮੁਲਾਂਕਨ ਚਲਾਉਂਦੇ ਹੋ, ਤਾਂ ਤੁਸੀਂ [Azure AI Foundry ਵਿੱਚ ਨਤੀਜੇ ਨੂੰ ਵਿਜੁਅਲਾਈਜ਼ ਕਰ ਸਕਦੇ ਹੋ](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results)। 

## ਟ੍ਰੇਡਮਾਰਕ

ਇਸ ਪ੍ਰੋਜੈਕਟ ਵਿੱਚ ਪ੍ਰੋਜੈਕਟਾਂ, ਉਤਪਾਦਾਂ, ਜਾਂ ਸੇਵਾਵਾਂ ਲਈ ਟ੍ਰੇਡਮਾਰਕ ਜਾਂ ਲੋਗੋ ਸ਼ਾਮਿਲ ਹੋ ਸਕਦੇ ਹਨ। Microsoft ਟ੍ਰੇਡਮਾਰਕ ਜਾਂ ਲੋਗੋ ਦੀ ਅਧਿਕ੍ਰਿਤ ਵਰਤੋਂ [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) ਦੀ ਪਾਲਣਾ ਕਰਨੀ ਚਾਹੀਦੀ ਹੈ। ਇਸ ਪ੍ਰੋਜੈਕਟ ਦੇ ਸੰਸ਼ੋਧਿਤ ਸੰਸਕਰਣਾਂ ਵਿੱਚ Microsoft ਟ੍ਰੇਡਮਾਰਕ ਜਾਂ ਲੋਗੋ ਦੀ ਵਰਤੋਂ ਗੁੰਝਲਦਾਰ ਨਹੀਂ ਹੋਣੀ ਚਾਹੀਦੀ ਅਤੇ ਨਾ ਹੀ Microsoft ਦੇ ਪ੍ਰਾਯੋਜਨ ਦਾ ਸੰਕੇਤ ਦੇਣਾ ਚਾਹੀਦਾ ਹੈ। ਕਿਸੇ ਵੀ ਤੀਜੀ ਪੱਖੀ ਟ੍ਰੇਡਮਾਰਕ ਜਾਂ ਲੋਗੋ ਦੀ ਵਰਤੋਂ ਉਹਨਾਂ ਤੀਜੀ ਪੱਖੀ ਦੀਆਂ ਨੀਤੀਆਂ ਦੇ ਅਧੀਨ ਹੈ।

---

**ਅਸਵੀਕਰਤੀ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀ ਹੋਣ ਦਾ ਯਤਨ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁਚਨਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਇਸ ਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਮੌਜੂਦ ਮੂਲ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਿਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।