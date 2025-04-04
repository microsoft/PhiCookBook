<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8f2577190cbe70305b9de13df37e1c9a",
  "translation_date": "2025-04-04T11:20:08+00:00",
  "source_file": "README.md",
  "language_code": "ja"
}
-->
# Phi Cookbook: MicrosoftのPhiモデルを使った実践例

[![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub issues](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub watchers](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub stars](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Azure AI Community Discord](https://dcbadge.vercel.app/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

PhiはMicrosoftが開発したオープンソースのAIモデルシリーズです。

Phiは現在、最も強力かつコストパフォーマンスの高い小型言語モデル（SLM）であり、多言語対応、推論、テキスト/チャット生成、コーディング、画像、音声などのシナリオで非常に優れたベンチマークを持っています。

Phiはクラウドやエッジデバイスにデプロイ可能で、限られたコンピューティングリソースでも簡単に生成AIアプリケーションを構築できます。

これらのリソースを使い始めるためのステップは以下の通りです：
1. **リポジトリをフォークする**: [![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo) をクリックしてください。
2. **リポジトリをクローンする**: `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Microsoft AI Discordコミュニティに参加し、専門家や他の開発者と交流する**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/cover.2595d43b382944c601aebf88583314636768eece3d94e8e4448e03a4e5bedef4.ja.png)

## 🌐 多言語対応
[フランス語](../fr/README.md) | [スペイン語](../es/README.md) | [ドイツ語](../de/README.md) | [ロシア語](../ru/README.md) | [アラビア語](../ar/README.md) | [ペルシア語 (ファルシ)](../fa/README.md) | [ウルドゥー語](../ur/README.md) | [中国語 (簡体字)](../zh/README.md) | [中国語 (繁体字, マカオ)](../mo/README.md) | [中国語 (繁体字, 香港)](../hk/README.md) | [中国語 (繁体字, 台湾)](../tw/README.md) | [日本語](./README.md) | [韓国語](../ko/README.md) | [ヒンディー語](../hi/README.md) | [ベンガル語](../bn/README.md) | [マラーティー語](../mr/README.md) | [ネパール語](../ne/README.md) | [パンジャーブ語 (グルムキー)](../pa/README.md) | [ポルトガル語 (ポルトガル)](../pt/README.md) | [ポルトガル語 (ブラジル)](../br/README.md) | [イタリア語](../it/README.md) | [ポーランド語](../pl/README.md) | [トルコ語](../tr/README.md) | [ギリシャ語](../el/README.md) | [タイ語](../th/README.md) | [スウェーデン語](../sv/README.md) | [デンマーク語](../da/README.md) | [ノルウェー語](../no/README.md) | [フィンランド語](../fi/README.md) | [オランダ語](../nl/README.md) | [ヘブライ語](../he/README.md) | [ベトナム語](../vi/README.md) | [インドネシア語](../id/README.md) | [マレー語](../ms/README.md) | [タガログ語 (フィリピン語)](../tl/README.md) | [スワヒリ語](../sw/README.md) | [ハンガリー語](../hu/README.md) | [チェコ語](../cs/README.md) | [スロバキア語](../sk/README.md) | [ルーマニア語](../ro/README.md) | [ブルガリア語](../bg/README.md) | [セルビア語 (キリル文字)](../sr/README.md) | [クロアチア語](../hr/README.md) | [スロベニア語](../sl/README.md)
## 目次

- はじめに
  - [Phiファミリーへようこそ](./md/01.Introduction/01/01.PhiFamily.md)
  - [環境のセットアップ](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [主要技術の理解](./md/01.Introduction/01/01.Understandingtech.md)
  - [PhiモデルのAI安全性](./md/01.Introduction/01/01.AISafety.md)
  - [Phiハードウェアのサポート](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Phiモデルとプラットフォーム間の利用可能性](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Guidance-aiとPhiの利用](./md/01.Introduction/01/01.Guidance.md)
  - [GitHubマーケットプレイスモデル](https://github.com/marketplace/models)
  - [Azure AIモデルカタログ](https://ai.azure.com)

- 異なる環境でのPhi推論
    -  [Hugging face](./md/01.Introduction/02/01.HF.md)
    -  [GitHubモデル](./md/01.Introduction/02/02.GitHubModel.md)
    -  [Azure AI Foundryモデルカタログ](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)

- Phiファミリーの推論
    - [iOSでのPhi推論](./md/01.Introduction/03/iOS_Inference.md)
    - [AndroidでのPhi推論](./md/01.Introduction/03/Android_Inference.md)
    - [JetsonでのPhi推論](./md/01.Introduction/03/Jetson_Inference.md)
    - [AI PCでのPhi推論](./md/01.Introduction/03/AIPC_Inference.md)
    - [Apple MLXフレームワークを使用したPhi推論](./md/01.Introduction/03/MLX_Inference.md)
    - [ローカルサーバーでのPhi推論](./md/01.Introduction/03/Local_Server_Inference.md)
    - [AI Toolkitを使用したリモートサーバーでのPhi推論](./md/01.Introduction/03/Remote_Interence.md)
    - [Rustを使用したPhi推論](./md/01.Introduction/03/Rust_Inference.md)
    - [ローカル環境でのPhi-Vision推論](./md/01.Introduction/03/Vision_Inference.md)
    - [Kaito AKS、Azure Containers（公式サポート）を使用したPhi推論](./md/01.Introduction/03/Kaito_Inference.md)
-  [Phiファミリーの量子化](./md/01.Introduction/04/QuantifyingPhi.md)
    - [llama.cppを使用したPhi-3.5 / 4の量子化](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [onnxruntime用生成AI拡張機能を使用したPhi-3.5 / 4の量子化](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Intel OpenVINOを使用したPhi-3.5 / 4の量子化](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Apple MLXフレームワークを使用したPhi-3.5 / 4の量子化](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

-  Phiの評価
- [Response AI](./md/01.Introduction/05/ResponsibleAI.md)  
    - [Azure AI Foundryによる評価](./md/01.Introduction/05/AIFoundry.md)  
    - [Promptflowを使用した評価](./md/01.Introduction/05/Promptflow.md)  

- Azure AI Searchを使用したRAG  
    - [Phi-4-miniとPhi-4-multimodal(RAG)をAzure AI Searchで使用する方法](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)  

- Phiアプリケーション開発サンプル  
  - テキスト＆チャットアプリケーション  
    - Phi-4 サンプル 🆕  
      - [📓] [Phi-4-mini ONNXモデルでチャット](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)  
      - [Phi-4ローカルONNXモデル.NETでチャット](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)  
      - [Semantic Kernelを使用したPhi-4 ONNXによる.NETコンソールチャットアプリ](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)  
    - Phi-3 / 3.5 サンプル  
      - [Phi3、ONNX Runtime Web、WebGPUを使用したブラウザ内ローカルチャットボット](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)  
      - [OpenVino Chat](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)  
      - [複数モデル - Phi-3-miniとOpenAI Whisperのインタラクティブサンプル](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)  
      - [MLFlow - ラッパーの構築とPhi-3をMLFlowで使用する方法](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)  
      - [モデル最適化 - Oliveを使用してPhi-3-minモデルをONNX Runtime Web用に最適化する方法](https://github.com/microsoft/Olive/tree/main/examples/phi3)  
      - [Phi-3 mini-4k-instruct-onnxを使用したWinUI3アプリ](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)  
      - [WinUI3複数モデルAI対応ノートアプリサンプル](https://github.com/microsoft/ai-powered-notes-winui3-sample)  
      - [カスタムPhi-3モデルを微調整しPromptflowと統合する方法](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)  
      - [Azure AI FoundryでカスタムPhi-3モデルを微調整しPromptflowと統合する方法](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)  
      - [Microsoftの責任あるAI原則に基づいて微調整されたPhi-3 / Phi-3.5モデルをAzure AI Foundryで評価する方法](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)  
      - [📓] [Phi-3.5-mini-instruct 言語予測サンプル（中国語/英語）](../../md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)  
      - [Phi-3.5-Instruct WebGPU RAG チャットボット](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)  
      - [Windows GPUを使用してPhi-3.5-Instruct ONNXでPromptflowソリューションを作成する方法](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)  
      - [Microsoft Phi-3.5 tfliteを使用してAndroidアプリを作成する方法](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)  
      - [Microsoft.ML.OnnxRuntimeを使用してローカルONNX Phi-3モデルでQ&A .NETサンプルを作成する方法](../../md/04.HOL/dotnet/src/LabsPhi301)  
      - [Semantic KernelとPhi-3を使用した.NETコンソールチャットアプリ](../../md/04.HOL/dotnet/src/LabsPhi302)  

  - Azure AI推論SDKコードベースサンプル  
    - Phi-4 サンプル 🆕  
      - [📓] [Phi-4-multimodalを使用したプロジェクトコード生成](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)  
    - Phi-3 / 3.5 サンプル  
      - [Microsoft Phi-3ファミリーを使用して独自のVisual Studio Code GitHub Copilot Chatを構築する方法](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)  
      - [Phi-3.5を使用してGitHubモデルで独自のVisual Studio Code Chat Copilot Agentを作成する方法](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)  

  - 高度な推論サンプル  
    - Phi-4 サンプル 🆕  
      - [📓] [Phi-4-mini 推論サンプル](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)  

  - デモ  
      - [Hugging Face SpacesでホストされているPhi-4-miniデモ](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)  
      - [Hugging Face SpacesでホストされているPhi-4-multimodalデモ](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)  
  - ビジョンサンプル  
    - Phi-4 サンプル 🆕  
      - [📓] [Phi-4-multimodalを使用して画像を読み取りコードを生成する](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md)  
    - Phi-3 / 3.5 サンプル  
- [📓][Phi-3-vision-Image text to text](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
  - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
  - [📓][Phi-3-vision CLIP Embedding](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
  - [DEMO: Phi-3 Recycling](https://github.com/jennifermarsman/PhiRecycling/)
  - [Phi-3-vision - 視覚言語アシスタント - Phi3-VisionとOpenVINOを使用](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
  - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
  - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
  - [📓][Phi-3.5 Vision 複数フレームまたは複数画像サンプル](../../md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
  - [Phi-3 Vision Local ONNX Model using the Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi303)
  - [メニュー方式 Phi-3 Vision Local ONNX Model using the Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi304)

- 音声サンプル
  - Phi-4 サンプル 🆕
    - [📓] [Phi-4-multimodalを使用した音声トランスクリプトの抽出](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
    - [📓] [Phi-4-multimodal 音声サンプル](../../md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
    - [📓] [Phi-4-multimodal 音声翻訳サンプル](../../md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
    - [.NETコンソールアプリケーションを使用してPhi-4-multimodal Audioで音声ファイルを分析し、トランスクリプトを生成](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

- MOEサンプル
  - Phi-3 / 3.5 サンプル
    - [📓] [Phi-3.5 Mixture of Experts Models (MoEs) ソーシャルメディアサンプル](../../md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
    - [📓] [NVIDIA NIM Phi-3 MOE、Azure AI Search、LlamaIndexを使用したRetrieval-Augmented Generation (RAG) パイプラインの構築](../../md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)

- 関数呼び出しサンプル
  - Phi-4 サンプル 🆕
    - [📓] [Phi-4-miniを使用した関数呼び出し](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
    - [📓] [Phi-4-miniを使用してマルチエージェントを作成する関数呼び出し](../../md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
    - [📓] [Ollamaを使用した関数呼び出し](../../md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)

- マルチモーダルミキシングサンプル
  - Phi-4 サンプル 🆕
    - [📓] [Phi-4-multimodalを技術ジャーナリストとして使用](../../md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
    - [.NETコンソールアプリケーションを使用してPhi-4-multimodalで画像を分析](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Phiのファインチューニングサンプル
  - [ファインチューニングシナリオ](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [ファインチューニング vs RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [Phi-3を業界の専門家にするファインチューニング](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [AI Toolkit for VS Codeを使用したPhi-3のファインチューニング](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Azure Machine Learning Serviceを使用したPhi-3のファインチューニング](./md/03.FineTuning/Introduce_AzureML.md)
  - [Loraを使用したPhi-3のファインチューニング](./md/03.FineTuning/FineTuning_Lora.md)
  - [QLoraを使用したPhi-3のファインチューニング](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Azure AI Foundryを使用したPhi-3のファインチューニング](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Azure ML CLI/SDKを使用したPhi-3のファインチューニング](./md/03.FineTuning/FineTuning_MLSDK.md)
- [Microsoft Oliveでの微調整](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Microsoft Olive Hands-On Labでの微調整](./md/03.FineTuning/olive-lab/readme.md)
  - [Phi-3-visionのWeights and Biasを使用した微調整](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [Apple MLX Frameworkを使用したPhi-3の微調整](./md/03.FineTuning/FineTuning_MLX.md)
  - [Phi-3-visionの微調整（公式サポート）](./md/03.FineTuning/FineTuning_Vision.md)
  - [Kaito AKSおよびAzure Containersを使用したPhi-3の微調整（公式サポート）](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Phi-3および3.5 Visionの微調整](https://github.com/2U1/Phi3-Vision-Finetune)

- Hands-on Lab
  - [最先端モデルの探索: LLMs、SLMs、ローカル開発など](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [NLPの可能性を解き放つ: Microsoft Oliveでの微調整](https://github.com/azure/Ignite_FineTuning_workshop)

- 学術研究論文と出版物
  - [Textbooks Are All You Need II: phi-1.5技術レポート](https://arxiv.org/abs/2309.05463)
  - [Phi-3技術レポート: あなたのスマートフォン上で動作する高性能な言語モデル](https://arxiv.org/abs/2404.14219)
  - [Phi-4技術レポート](https://arxiv.org/abs/2412.08905)
  - [Phi-4-Mini技術レポート: Mixture-of-LoRAsを活用したコンパクトかつ強力なマルチモーダル言語モデル](https://arxiv.org/abs/2503.01743)
  - [車載機能呼び出しのための小型言語モデルの最適化](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) PHI-3を選択式質問回答に微調整する: 方法論、結果、および課題](https://arxiv.org/abs/2501.01588)

## Phiモデルの使用方法

### Azure AI FoundryでのPhi

Microsoft Phiを使用し、さまざまなハードウェアデバイスでE2Eソリューションを構築する方法を学ぶことができます。Phiを体験するには、モデルを試してみたり、シナリオに合わせてPhiをカスタマイズすることから始めましょう。 [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai)を使用してさらに学べます。[Azure AI Foundryの入門ガイド](/md/02.QuickStart/AzureAIFoundry_QuickStart.md)もご覧ください。

**プレイグラウンド**
各モデルには専用のプレイグラウンドがあります。[Azure AI Playground](https://aka.ms/try-phi3)でモデルを試してみてください。

### GitHubモデルでのPhi

Microsoft Phiを使用し、さまざまなハードウェアデバイスでE2Eソリューションを構築する方法を学ぶことができます。Phiを体験するには、モデルを試してみたり、シナリオに合わせてPhiをカスタマイズすることから始めましょう。 [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo)を使用してさらに学べます。[GitHub Model Catalogの入門ガイド](/md/02.QuickStart/GitHubModel_QuickStart.md)もご覧ください。

**プレイグラウンド**
各モデルには専用の[プレイグラウンドがあります](/md/02.QuickStart/GitHubModel_QuickStart.md)。

### Hugging FaceでのPhi

モデルは[Hugging Face](https://huggingface.co/microsoft)でも利用可能です。

**プレイグラウンド**
[Hugging Chatプレイグラウンド](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## 責任あるAI 

Microsoftは、お客様がAI製品を責任を持って使用できるよう支援し、学びを共有し、透明性のあるパートナーシップを構築することにコミットしています。これには、Transparency NotesやImpact Assessmentsといったツールが含まれます。これらのリソースの多くは[https://aka.ms/RAI](https://aka.ms/RAI)で見つけることができます。
Microsoftの責任あるAIへの取り組みは、公平性、信頼性と安全性、プライバシーとセキュリティ、包括性、透明性、説明責任といったAI原則に基づいています。

このサンプルで使用されているような大規模な自然言語、画像、音声モデルは、不公平、不信頼、または攻撃的な振る舞いをする可能性があり、結果として害を引き起こすことがあります。[Azure OpenAIサービスのTransparency Note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text)を参照し、リスクや制限について理解してください。

これらのリスクを軽減する推奨アプローチは、有害な振る舞いを検出し防止する安全システムをアーキテクチャに組み込むことです。[Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview)は、アプリケーションやサービス内で生成された有害なコンテンツを検出できる独立した保護層を提供します。Azure AI Content Safetyには、有害なテキストや画像を検出するAPIが含まれています。Azure AI Foundry内では、Content Safetyサービスを使用して、有害なコンテンツを検出するサンプルコードを閲覧、探索、試用することができます。[クイックスタートドキュメント](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest)では、サービスへのリクエストを行う方法について説明しています。

もう1つ考慮すべき点は、全体的なアプリケーションのパフォーマンスです。マルチモーダルおよびマルチモデルのアプリケーションにおいて、パフォーマンスとはシステムが期待通りの動作をし、ユーザーに有害な出力を生成しないことを意味します。アプリケーション全体のパフォーマンスを評価するには、[Performance and Quality and Risk and Safety evaluators](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in)を使用することが重要です。[カスタム評価機能](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators)を作成し評価することも可能です。
Azure AI Evaluation SDK を使用して、開発環境で AI アプリケーションを評価することができます。[Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html) を使用すると、テストデータセットやターゲットを基に生成型 AI アプリケーションの生成物を、組み込みの評価ツールや任意のカスタム評価ツールで定量的に測定できます。Azure AI Evaluation SDK を使ってシステムを評価するには、[クイックスタートガイド](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk)に従ってください。評価を実行した後は、[Azure AI Foundry で結果を可視化](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results)することができます。

## 商標

このプロジェクトには、プロジェクト、製品、サービスの商標やロゴが含まれる場合があります。Microsoft の商標やロゴの正規の使用は、[Microsoft の商標およびブランドガイドライン](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general)に従う必要があります。このプロジェクトの改変版における Microsoft の商標やロゴの使用は、混乱を招いたり Microsoft の後援を暗示したりしないようにしてください。第三者の商標やロゴの使用については、その第三者のポリシーに従う必要があります。

**免責事項**:  
この文書はAI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を追求していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。元の言語で記載された原文が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤解釈について、当方は一切の責任を負いません。