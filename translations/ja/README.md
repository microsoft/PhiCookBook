<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c2e4b490f4bd424b095f21e38c6af33b",
  "translation_date": "2026-01-05T01:08:24+00:00",
  "source_file": "README.md",
  "language_code": "ja"
}
-->
# Phi Cookbook: Hands-On Examples with Microsoft's Phi Models

[![GitHub Codespacesでサンプルを開いて使用する](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Dev Containersで開く](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHubのコントリビューター](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHubの課題](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHubのプルリクエスト](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PR歓迎](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Azure AI FoundryのDiscord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

PhiはMicrosoftが開発したオープンソースのAIモデルのシリーズです。 

Phiは現在、マルチランゲージ、推論、テキスト/チャット生成、コーディング、画像、オーディオなどのシナリオで非常に優れたベンチマークを持つ、最も強力で費用対効果の高い小規模言語モデル（SLM）です。 

Phiはクラウドやエッジデバイスにデプロイでき、限られた計算リソースでも簡単に生成型AIアプリケーションを構築できます。

これらのリソースを使用して始めるには、次の手順に従ってください：
1. **リポジトリをフォークする**：クリック [![GitHubのフォーク](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **リポジトリをクローンする**：   `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Microsoft AI Discord コミュニティに参加して、専門家や開発者仲間と交流しましょう**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![カバー画像](../../translated_images/cover.eb18d1b9605d754b.ja.png)

### 🌐 多言語サポート

#### GitHub Actionでサポート（自動化＆常に最新）

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[アラビア語](../ar/README.md) | [ベンガル語](../bn/README.md) | [ブルガリア語](../bg/README.md) | [ビルマ語（ミャンマー）](../my/README.md) | [中国語（簡体字）](../zh/README.md) | [中国語（繁体字、香港）](../hk/README.md) | [中国語（繁体字、マカオ）](../mo/README.md) | [中国語（繁体字、台湾）](../tw/README.md) | [クロアチア語](../hr/README.md) | [チェコ語](../cs/README.md) | [デンマーク語](../da/README.md) | [オランダ語](../nl/README.md) | [エストニア語](../et/README.md) | [フィンランド語](../fi/README.md) | [フランス語](../fr/README.md) | [ドイツ語](../de/README.md) | [ギリシャ語](../el/README.md) | [ヘブライ語](../he/README.md) | [ヒンディー語](../hi/README.md) | [ハンガリー語](../hu/README.md) | [インドネシア語](../id/README.md) | [イタリア語](../it/README.md) | [日本語](./README.md) | [カンナダ語](../kn/README.md) | [韓国語](../ko/README.md) | [リトアニア語](../lt/README.md) | [マレー語](../ms/README.md) | [マラヤーラム語](../ml/README.md) | [マラーティー語](../mr/README.md) | [ネパール語](../ne/README.md) | [ナイジェリア・ピジン語](../pcm/README.md) | [ノルウェー語](../no/README.md) | [ペルシア語（ファルシ）](../fa/README.md) | [ポーランド語](../pl/README.md) | [ポルトガル語（ブラジル）](../br/README.md) | [ポルトガル語（ポルトガル）](../pt/README.md) | [パンジャブ語（グルムキー）](../pa/README.md) | [ルーマニア語](../ro/README.md) | [ロシア語](../ru/README.md) | [セルビア語（キリル）](../sr/README.md) | [スロバキア語](../sk/README.md) | [スロベニア語](../sl/README.md) | [スペイン語](../es/README.md) | [スワヒリ語](../sw/README.md) | [スウェーデン語](../sv/README.md) | [タガログ語（フィリピン）](../tl/README.md) | [タミル語](../ta/README.md) | [テルグ語](../te/README.md) | [タイ語](../th/README.md) | [トルコ語](../tr/README.md) | [ウクライナ語](../uk/README.md) | [ウルドゥー語](../ur/README.md) | [ベトナム語](../vi/README.md)

> **ローカルにクローンしますか？**

> このリポジトリには50以上の言語翻訳が含まれており、ダウンロードサイズが大幅に増加します。翻訳なしでクローンするには、スパースチェックアウトを使用してください：
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/PhiCookBook.git
> cd PhiCookBook
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> これにより、コースを完了するために必要なすべてが、より高速なダウンロードで入手できます。
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## 目次

- はじめに
  - [Phiファミリーへようこそ](./md/01.Introduction/01/01.PhiFamily.md)
  - [環境の設定](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [主要技術の理解](./md/01.Introduction/01/01.Understandingtech.md)
  - [PhiモデルのAI安全性](./md/01.Introduction/01/01.AISafety.md)
  - [Phiハードウェアサポート](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Phiモデルとプラットフォーム別の提供状況](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Guidance-aiとPhiの使用](./md/01.Introduction/01/01.Guidance.md)
  - [GitHub Marketplaceのモデル](https://github.com/marketplace/models)
  - [Azure AIモデルカタログ](https://ai.azure.com)

- さまざまな環境でのPhi推論
    -  [Hugging face](./md/01.Introduction/02/01.HF.md)
    -  [GitHub Models](./md/01.Introduction/02/02.GitHubModel.md)
    -  [Azure AI Foundry Model Catalog](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    -  [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md)

- Phiファミリーの推論
    - [iOSでのPhi推論](./md/01.Introduction/03/iOS_Inference.md)
    - [AndroidでのPhi推論](./md/01.Introduction/03/Android_Inference.md)
    - [JetsonでのPhi推論](./md/01.Introduction/03/Jetson_Inference.md)
    - [AI PCでのPhi推論](./md/01.Introduction/03/AIPC_Inference.md)
    - [Apple MLXフレームワークでのPhi推論](./md/01.Introduction/03/MLX_Inference.md)
    - [ローカルサーバーでのPhi推論](./md/01.Introduction/03/Local_Server_Inference.md)
    - [AI Toolkitを使用したリモートサーバーでのPhi推論](./md/01.Introduction/03/Remote_Interence.md)
    - [RustでのPhi推論](./md/01.Introduction/03/Rust_Inference.md)
    - [ローカルでのPhiビジョン推論](./md/01.Introduction/03/Vision_Inference.md)
    - [Kaito AKS、Azure Containers（公式サポート）でのPhi推論](./md/01.Introduction/03/Kaito_Inference.md)
-  [Phiファミリーの量子化](./md/01.Introduction/04/QuantifyingPhi.md)
    - [llama.cppを使用したPhi-3.5 / 4の量子化](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [onnxruntime用Generative AI拡張を使用したPhi-3.5 / 4の量子化](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Intel OpenVINOを使用したPhi-3.5 / 4の量子化](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Apple MLXフレームワークを使用したPhi-3.5 / 4の量子化](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

-  Phiの評価
    - [責任あるAI](./md/01.Introduction/05/ResponsibleAI.md)
    - [評価のためのAzure AI Foundry](./md/01.Introduction/05/AIFoundry.md)
    - [評価のためのPromptflowの使用](./md/01.Introduction/05/Promptflow.md)
 
- Azure AI SearchによるRAG
    - [Azure AI SearchでPhi-4-miniとPhi-4-multimodal(RAG)を使用する方法](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Phiアプリケーション開発サンプル
  - テキスト＆チャットアプリケーション
    - Phi-4 サンプル 🆕
      - [📓] [Phi-4-mini ONNXモデルとのチャット](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [.NETでPhi-4ローカルONNXモデルとチャット](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Sementic Kernelを使用したPhi-4 ONNXによる.NETコンソールアプリのチャット](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Phi-3 / 3.5 サンプル
      - [Phi3、ONNX Runtime Web、WebGPUを使用したブラウザ内ローカルチャットボット](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVino チャット](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [マルチモデル - インタラクティブ Phi-3-mini と OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - ラッパーを構築し MLFlow で Phi-3 を使用する](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [モデル最適化 - Olive を使用して Phi-3-min モデルを ONNX Runtime Web 用に最適化する方法](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [Phi-3 mini-4k-instruct-onnx を使用した WinUI3 アプリ](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      -[WinUI3 マルチモデル AI 搭載ノートアプリ サンプル](https://github.com/microsoft/ai-powered-notes-winui3-sample)
      - [Prompt flow を使ってカスタム Phi-3 モデルをファインチューニングして統合する](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
      - [Azure AI Foundry で Prompt flow を使ってカスタム Phi-3 モデルをファインチューニングして統合する](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
      - [Azure AI Foundry で Microsoft の責任ある AI 原則に焦点を当てたファインチューニング済み Phi-3 / Phi-3.5 モデルの評価](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
      - [📓] [Phi-3.5-mini-instruct 言語予測サンプル（中国語/英語）](./md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
      - [Phi-3.5-Instruct WebGPU RAG チャットボット](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
      - [Windows GPU を使用して Phi-3.5-Instruct ONNX で Prompt flow ソリューションを作成する](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
      - [Microsoft Phi-3.5 tflite を使用して Android アプリを作成する](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
      - [Microsoft.ML.OnnxRuntime を使用してローカル ONNX Phi-3 モデルを使う Q&A .NET サンプル](../../md/04.HOL/dotnet/src/LabsPhi301)
      - [Semantic Kernel と Phi-3 を使ったコンソールチャット .NET アプリ](../../md/04.HOL/dotnet/src/LabsPhi302)

  - Azure AI Inference SDK コードベースのサンプル 
    - Phi-4 サンプル 🆕
      - [📓] [Phi-4-multimodal を使用してプロジェクトコードを生成する](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
    - Phi-3 / 3.5 サンプル
      - [Microsoft Phi-3 ファミリーで独自の Visual Studio Code GitHub Copilot Chat を構築する](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
      - [GitHub Models の Phi-3.5 で独自の Visual Studio Code Chat Copilot エージェントを作成する](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

  - 高度な推論サンプル
    - Phi-4 サンプル 🆕
      - [📓] [Phi-4-mini-reasoning または Phi-4-reasoning サンプル](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
      - [📓] [Microsoft Olive で Phi-4-mini-reasoning をファインチューニングする](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Apple MLX で Phi-4-mini-reasoning をファインチューニングする](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [GitHub Models での Phi-4-mini-reasoning](./md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
      - [📓] [Azure AI Foundry Models での Phi-4-mini-reasoning](./md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
  - デモ
      - [Hugging Face Spaces でホストされている Phi-4-mini デモ](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
      - [Hugginge Face Spaces でホストされている Phi-4-multimodal デモ](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
  - ビジョンサンプル
    - Phi-4 サンプル 🆕
      - [📓] [Phi-4-multimodal を使用して画像を読み取りコードを生成する](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
    - Phi-3 / 3.5 サンプル
      -  [📓][Phi-3-vision-Image 画像のテキストからテキストへ](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
      - [📓][Phi-3-vision CLIP 埋め込み](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [DEMO: Phi-3 リサイクリング](https://github.com/jennifermarsman/PhiRecycling/)
      - [Phi-3-vision - ビジュアル言語アシスタント - Phi3-Vision と OpenVINO を使用](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
      - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
      - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
      - [📓][Phi-3.5 Vision マルチフレームまたはマルチイメージ サンプル](./md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
      - [Microsoft.ML.OnnxRuntime .NET を使用した Phi-3 Vision ローカル ONNX モデル](../../md/04.HOL/dotnet/src/LabsPhi303)
      - [メニュー ベースの Phi-3 Vision ローカル ONNX モデル Microsoft.ML.OnnxRuntime .NET を使用](../../md/04.HOL/dotnet/src/LabsPhi304)

  - 数学サンプル
    -  Phi-4-Mini-Flash-Reasoning-Instruct サンプル 🆕 [Phi-4-Mini-Flash-Reasoning-Instruct を使った数学デモ](./md/02.Application/09.Math/MathDemo.ipynb)

  - オーディオサンプル
    - Phi-4 サンプル 🆕
      - [📓] [Phi-4-multimodal を使用した音声トランスクリプトの抽出](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
      - [📓] [Phi-4-multimodal オーディオサンプル](./md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
      - [📓] [Phi-4-multimodal 音声翻訳サンプル](./md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
      - [.NET コンソールアプリケーション - Phi-4-multimodal オーディオを使用してオーディオファイルを分析しトランスクリプトを生成](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

  - MOE サンプル
    - Phi-3 / 3.5 サンプル
      - [📓] [Phi-3.5 Mixture of Experts モデル (MoEs) ソーシャルメディアサンプル](./md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
      - [📓] [NVIDIA NIM Phi-3 MOE、Azure AI Search、LlamaIndex を使った Retrieval-Augmented Generation (RAG) パイプラインの構築](./md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)
      - 
  - 関数呼び出しサンプル
    - Phi-4 サンプル 🆕
      -  [📓] [Phi-4-mini での関数呼び出しの使用](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
      -  [📓] [Phi-4-mini でマルチエージェントを作成するための関数呼び出しの使用](./md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
      -  [📓] [Ollama での関数呼び出しの使用](./md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
      -  [📓] [ONNX での関数呼び出しの使用](./md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)
  - マルチモーダルミキシングサンプル
    - Phi-4 サンプル 🆕
      -  [📓] [Phi-4-multimodal をテクノロジージャーナリストとして使用する](./md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
      - [.NET コンソールアプリケーション - Phi-4-multimodal を使用して画像を分析](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Phi のファインチューニング サンプル
  - [ファインチューニング シナリオ](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [ファインチューニングと RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [ファインチューニング - Phi-3 を業界の専門家にする](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [AI Toolkit for VS Code を使用した Phi-3 のファインチューニング](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Azure Machine Learning Service を使用した Phi-3 のファインチューニング](./md/03.FineTuning/Introduce_AzureML.md)
  - [Lora を使用した Phi-3 のファインチューニング](./md/03.FineTuning/FineTuning_Lora.md)
  - [QLora を使用した Phi-3 のファインチューニング](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Azure AI Foundry を使用した Phi-3 のファインチューニング](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Azure ML CLI/SDK を使用した Phi-3 のファインチューニング](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Microsoft Olive を使用したファインチューニング](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Microsoft Olive ハンズオンラボでのファインチューニング](./md/03.FineTuning/olive-lab/readme.md)
  - [Weights and Bias を使用した Phi-3-vision のファインチューニング](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [Apple MLX Framework を使用した Phi-3 のファインチューニング](./md/03.FineTuning/FineTuning_MLX.md)
  - [Phi-3-vision のファインチューニング（公式サポート）](./md/03.FineTuning/FineTuning_Vision.md)
  - [Kaito AKS , Azure Containers(公式サポート) を使用した Phi-3 のファインチューニング](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Phi-3 および 3.5 Vision のファインチューニング](https://github.com/2U1/Phi3-Vision-Finetune)

- ハンズオンラボ
  - [最先端モデルの探索: LLM、SLM、ローカル開発など](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [NLP の可能性を引き出す: Microsoft Olive でのファインチューニング](https://github.com/azure/Ignite_FineTuning_workshop)

- 学術研究論文と出版物
  - [Textbooks Are All You Need II: phi-1.5 技術報告](https://arxiv.org/abs/2309.05463)
  - [Phi-3 技術報告: 携帯電話上でローカルに動作する高性能言語モデル](https://arxiv.org/abs/2404.14219)
  - [Phi-4 技術報告](https://arxiv.org/abs/2412.08905)
  - [Phi-4-Mini 技術報告: Mixture-of-LoRAs によるコンパクトだが強力なマルチモーダル言語モデル](https://arxiv.org/abs/2503.01743)
  - [車載機能呼び出し向け小型言語モデルの最適化](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) PHI-3 の多肢選択問題解答へのファインチューニング: 方法論、結果、および課題](https://arxiv.org/abs/2501.01588)
  - [Phi-4-reasoning 技術報告](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Phi-4-mini-reasoning 技術報告](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Using Phi Models

### Azure AI Foundry 上の Phi

You can learn how to use Microsoft Phi and how to build E2E solutions in your different hardware devices. To experience Phi for yourself, start by playing with the models and customizing Phi for your scenarios using the [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai) you can learn more at Getting Started with [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md)

**Playground**
各モデルにはモデルをテストする専用のプレイグラウンドがあります [Azure AI Playground](https://aka.ms/try-phi3).

### GitHub Models 上の Phi

You can learn how to use Microsoft Phi and how to build E2E solutions in your different hardware devices. To experience Phi for yourself, start by playing with the model and customizing Phi for your scenarios using the [GitHub モデル カタログ](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) you can learn more at Getting Started with [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md)

**Playground**
各モデルにはモデルをテストする専用の[プレイグラウンド](/md/02.QuickStart/GitHubModel_QuickStart.md)があります。

### Hugging Face 上の Phi

You can also find the model on the [Hugging Face](https://huggingface.co/microsoft)

**Playground**
 [Hugging Chat プレイグラウンド](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

 ## 🎒 その他のコース

Our team produces other courses! Check out:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j（初心者向け）](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js（初心者向け）](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

---

### Azure / Edge / MCP / エージェント
[![AZD（初心者向け）](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI（初心者向け）](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP（初心者向け）](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Agents（初心者向け）](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Generative AI Series
[![生成AI（初心者向け）](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![生成AI（.NET）](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![生成AI（Java）](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![生成AI（JavaScript）](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### コア学習
[![ML（初心者向け）](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![データサイエンス（初心者向け）](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI（初心者向け）](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![サイバーセキュリティ（初心者向け）](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Web 開発（初心者向け）](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT（初心者向け）](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR 開発（初心者向け）](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot シリーズ
[![Copilot（AI ペアプログラミング向け）](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot（C#/.NET 向け）](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot アドベンチャー](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## 責任ある AI 

Microsoft is committed to helping our customers use our AI products responsibly, sharing our learnings, and building trust-based partnerships through tools like Transparency Notes and Impact Assessments. Many of these resources can be found at [https://aka.ms/RAI](https://aka.ms/RAI).
Microsoft’s approach to responsible AI is grounded in our AI principles of fairness, reliability and safety, privacy and security, inclusiveness, transparency, and accountability.

Large-scale natural language, image, and speech models - like the ones used in this sample - can potentially behave in ways that are unfair, unreliable, or offensive, in turn causing harms. Please consult the [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) to be informed about risks and limitations.

The recommended approach to mitigating these risks is to include a safety system in your architecture that can detect and prevent harmful behavior. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) provides an independent layer of protection, able to detect harmful user-generated and AI-generated content in applications and services. Azure AI Content Safety includes text and image APIs that allow you to detect material that is harmful. Within Azure AI Foundry, the Content Safety service allows you to view, explore and try out sample code for detecting harmful content across different modalities. The following [quickstart documentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) guides you through making requests to the service.

Another aspect to take into account is the overall application performance. With multi-modal and multi-models applications, we consider performance to mean that the system performs as you and your users expect, including not generating harmful outputs. It's important to assess the performance of your overall application using [パフォーマンスと品質およびリスクと安全性の評価器](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in). You also have the ability to create and evaluate with [カスタム評価器](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators).
開発環境で [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html) を使用して AI アプリケーションを評価できます。テスト用データセットまたはターゲットのいずれかを指定すると、生成型 AI アプリケーションの出力は、組み込みの評価器や選択したカスタム評価器によって定量的に測定されます。システムを評価するために Azure AI Evaluation SDK を使い始めるには、[クイックスタート ガイド](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) に従ってください。評価の実行後、[Azure AI Foundry で結果を視覚化できます](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results)。

## 商標

このプロジェクトには、プロジェクト、製品、またはサービスの商標やロゴが含まれている場合があります。Microsoft の商標やロゴの使用は許可されている場合でも、[Microsoft の商標・ブランド ガイドライン](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) に従う必要があります。本プロジェクトの修正版で Microsoft の商標やロゴを使用する場合、混乱を招いたり Microsoft の後援を示唆したりしてはいけません。サードパーティの商標やロゴの使用は、それらサードパーティのポリシーに従う必要があります。

## ヘルプ

AI アプリの構築で行き詰まったり質問がある場合は、参加してください:

[![Azure AI Foundry Discord コミュニティ](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

製品に関するフィードバックや構築中のエラーがある場合は、次を参照してください:

[![Azure AI Foundry 開発者フォーラム](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
免責事項：
本書はAI翻訳サービス「Co‑op Translator」（https://github.com/Azure/co-op-translator）を用いて翻訳されました。正確性の確保に努めておりますが、自動翻訳には誤りや不正確な箇所が含まれる場合があります。原文（原言語）の文書を正本として扱ってください。重要な情報については、専門の人による翻訳をお勧めします。本翻訳の利用により生じたいかなる誤解や解釈の相違についても、当方は責任を負いません。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->