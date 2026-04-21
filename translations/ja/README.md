# Phi クックブック：Microsoft の Phi モデルを使ったハンズオン例

[![GitHub Codespaces でサンプルを開いて使用する](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Dev Containers で開く](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub コントリビューター](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub イシュー](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub プルリクエスト](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PR歓迎](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub ウォッチャー](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub フォーク](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub スター](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi は Microsoft によって開発されたオープンソースの AI モデルのシリーズです。

Phi は現在、非常に優れた多言語・推論・テキスト/チャット生成・コーディング・画像・音声およびその他のシナリオでのベンチマークを誇る、最も強力かつコスト効率の高い小型言語モデル（SLM）です。

Phi はクラウドやエッジデバイスにデプロイ可能で、限られた計算リソースでも簡単に生成型 AI アプリケーションを構築できます。

以下のステップに従ってこれらのリソースの使用を開始してください：
1. <strong>リポジトリをフォークする</strong>: クリック [![GitHub フォーク](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. <strong>リポジトリをクローンする</strong>: `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Microsoft AI Discord コミュニティに参加し、専門家や他の開発者と交流する**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/ja/cover.eb18d1b9605d754b.webp)

### 🌐 多言語対応

#### GitHub Actions によるサポート（自動化＆常に最新）

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[アラビア語](../ar/README.md) | [ベンガル語](../bn/README.md) | [ブルガリア語](../bg/README.md) | [ビルマ語（ミャンマー）](../my/README.md) | [中国語（簡体字）](../zh-CN/README.md) | [中国語（繁体字、香港）](../zh-HK/README.md) | [中国語（繁体字、マカオ）](../zh-MO/README.md) | [中国語（繁体字、台湾）](../zh-TW/README.md) | [クロアチア語](../hr/README.md) | [チェコ語](../cs/README.md) | [デンマーク語](../da/README.md) | [オランダ語](../nl/README.md) | [エストニア語](../et/README.md) | [フィンランド語](../fi/README.md) | [フランス語](../fr/README.md) | [ドイツ語](../de/README.md) | [ギリシャ語](../el/README.md) | [ヘブライ語](../he/README.md) | [ヒンディー語](../hi/README.md) | [ハンガリー語](../hu/README.md) | [インドネシア語](../id/README.md) | [イタリア語](../it/README.md) | [日本語](./README.md) | [カンナダ語](../kn/README.md) | [クメール語](../km/README.md) | [韓国語](../ko/README.md) | [リトアニア語](../lt/README.md) | [マレー語](../ms/README.md) | [マラヤーラム語](../ml/README.md) | [マラーティー語](../mr/README.md) | [ネパール語](../ne/README.md) | [ナイジェリア・ピジン語](../pcm/README.md) | [ノルウェー語](../no/README.md) | [ペルシア語（ファルシ）](../fa/README.md) | [ポーランド語](../pl/README.md) | [ポルトガル語（ブラジル）](../pt-BR/README.md) | [ポルトガル語（ポルトガル）](../pt-PT/README.md) | [パンジャブ語（グルムキー）](../pa/README.md) | [ルーマニア語](../ro/README.md) | [ロシア語](../ru/README.md) | [セルビア語（キリル）](../sr/README.md) | [スロバキア語](../sk/README.md) | [スロベニア語](../sl/README.md) | [スペイン語](../es/README.md) | [スワヒリ語](../sw/README.md) | [スウェーデン語](../sv/README.md) | [タガログ語（フィリピン）](../tl/README.md) | [タミル語](../ta/README.md) | [テルグ語](../te/README.md) | [タイ語](../th/README.md) | [トルコ語](../tr/README.md) | [ウクライナ語](../uk/README.md) | [ウルドゥー語](../ur/README.md) | [ベトナム語](../vi/README.md)

> **ローカルクローンを希望しますか？**
>
> このリポジトリには50以上の言語の翻訳が含まれており、ダウンロードサイズが大幅に増加します。翻訳を含めずにクローンする場合は、スパースチェックアウトを使用してください：
>
> **Bash / macOS / Linux:**
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/PhiCookBook.git
> cd PhiCookBook
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
>
> **CMD（Windows）:**
> ```cmd
> git clone --filter=blob:none --sparse https://github.com/microsoft/PhiCookBook.git
> cd PhiCookBook
> git sparse-checkout set --no-cone "/*" "!translations" "!translated_images"
> ```
>
> これにより、コース完了に必要なすべてがより高速にダウンロード可能になります。
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## 目次

- はじめに
  - [Phi ファミリーへようこそ](./md/01.Introduction/01/01.PhiFamily.md)
  - [環境のセットアップ](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [主要技術の理解](./md/01.Introduction/01/01.Understandingtech.md)
  - [Phi モデルの AI セーフティ](./md/01.Introduction/01/01.AISafety.md)
  - [Phi ハードウェアサポート](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Phi モデルとプラットフォーム別の利用状況](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Guidance-ai と Phi の使用](./md/01.Introduction/01/01.Guidance.md)
  - [GitHub Marketplace Models](https://github.com/marketplace/models)
  - [Azure AI Model Catalog](https://ai.azure.com)

- 様々な環境での Phi 推論
    -  [Hugging face](./md/01.Introduction/02/01.HF.md)
    -  [GitHub Models](./md/01.Introduction/02/02.GitHubModel.md)
    -  [Microsoft Foundry Model Catalog](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    -  [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md)

- Phi ファミリーの推論
    - [iOS での Phi 推論](./md/01.Introduction/03/iOS_Inference.md)
    - [Android での Phi 推論](./md/01.Introduction/03/Android_Inference.md)
    - [Jetson での Phi 推論](./md/01.Introduction/03/Jetson_Inference.md)
    - [AI PC での Phi 推論](./md/01.Introduction/03/AIPC_Inference.md)
    - [Apple MLX フレームワークによる Phi 推論](./md/01.Introduction/03/MLX_Inference.md)
    - [ローカルサーバーでの Phi 推論](./md/01.Introduction/03/Local_Server_Inference.md)
    - [AI Toolkit を使用したリモートサーバーでの Phi 推論](./md/01.Introduction/03/Remote_Interence.md)
    - [Rust での Phi 推論](./md/01.Introduction/03/Rust_Inference.md)
    - [ローカルでの Phi ビジョン推論](./md/01.Introduction/03/Vision_Inference.md)
    - [Kaito AKS、Azure Containers による Phi 推論（公式サポート）](./md/01.Introduction/03/Kaito_Inference.md)

-  [Phi ファミリーの量子化](./md/01.Introduction/04/QuantifyingPhi.md)
    - [llama.cpp を使った Phi-3.5 / 4 の量子化](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [onnxruntime 用生成 AI 拡張を使った Phi-3.5 / 4 の量子化](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Intel OpenVINO を使った Phi-3.5 / 4 の量子化](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Apple MLX フレームワークを使った Phi-3.5 / 4 の量子化](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

-  Phi の評価
    - [Responsible AI](./md/01.Introduction/05/ResponsibleAI.md)
    - [評価のための Microsoft Foundry](./md/01.Introduction/05/AIFoundry.md)
    - [Promptflow を使った評価](./md/01.Introduction/05/Promptflow.md)

- Azure AI Search を使った RAG
    - [Azure AI Search での Phi-4-mini と Phi-4-multimodal(RAG) の使い方](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Phi アプリケーション開発サンプル
  - テキスト＆チャットアプリケーション
    - Phi-4 サンプル
      - [📓] [Phi-4-mini ONNX モデルとのチャット](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Phi-4 ローカル ONNX モデルとのチャット .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Semantic Kernel を使用した Phi-4 ONNX の .NET コンソールアプリチャット](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Phi-3 / 3.5 サンプル
      - [ブラウザで Phi3、ONNX Runtime Web と WebGPU を使ったローカルチャットボット](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVino Chat](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [マルチモデル - 対話型 Phi-3-mini と OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - ラッパーの構築と Phi-3 を MLFlow で使用する](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [モデル最適化 - Olive を使って Phi-3-mini モデルを ONNX Runtime Web 用に最適化する方法](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [Phi-3 mini-4k-instruct-onnx を使った WinUI3 アプリ](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      -[WinUI3 マルチモデル AI 搭載ノートアプリのサンプル](https://github.com/microsoft/ai-powered-notes-winui3-sample)
      - [カスタム Phi-3 モデルのファインチューニングと Prompt flow との統合](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
      - [Microsoft Foundry での Prompt flow を使ったカスタム Phi-3 モデルのファインチューニングと統合](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
      - [Microsoft の責任ある AI 原則に焦点を当てた Microsoft Foundry でのファインチューニング済み Phi-3 / Phi-3.5 モデルの評価](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
      - [📓] [Phi-3.5-mini-instruct 言語予測サンプル（中国語／英語）](./md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
      - [Phi-3.5-Instruct WebGPU RAG チャットボット](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
      - [Windows GPU を使って Phi-3.5-Instruct ONNX の Prompt flow ソリューションを作成する](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
      - [Microsoft Phi-3.5 tflite を使って Android アプリを作成する](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
      - [Microsoft.ML.OnnxRuntime を使ったローカル ONNX Phi-3 モデルによる Q&A .NET の例](../../md/04.HOL/dotnet/src/LabsPhi301)
      - [Semantic Kernel と Phi-3 を使ったコンソールチャット .NET アプリ](../../md/04.HOL/dotnet/src/LabsPhi302)

  - Azure AI Inference SDK のコードベースサンプル 
    - Phi-4 サンプル 
      - [📓] [Phi-4-multimodal を用いたプロジェクトコード生成](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
    - Phi-3 / 3.5 サンプル
      - [Microsoft Phi-3 ファミリーを使って Visual Studio Code GitHub Copilot Chat を構築する](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
      - [GitHub モデルで Phi-3.5 による独自の Visual Studio Code Chat Copilot エージェントを作成する](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

  - 高度な推論サンプル
    - Phi-4 サンプル 
      - [📓] [Phi-4-mini-reasoning または Phi-4-reasoning サンプル](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
      - [📓] [Microsoft Olive を使った Phi-4-mini-reasoning のファインチューニング](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Apple MLX を使った Phi-4-mini-reasoning のファインチューニング](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [GitHub モデルを使った Phi-4-mini-reasoning](./md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
      - [📓] [Microsoft Foundry モデルを使った Phi-4-mini-reasoning](./md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
  - デモ
      - [Hugging Face Spaces でホストされている Phi-4-mini デモ](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
      - [Hugginge Face Spaces でホストされている Phi-4-multimodal デモ](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
  - ビジョンサンプル
    - Phi-4 サンプル 
      - [📓] [Phi-4-multimodal を用いて画像を読み取りコードを生成する](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
    - Phi-3 / 3.5 サンプル
      -  [📓][Phi-3-vision-画像テキスト変換](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
      - [📓][Phi-3-vision CLIP 埋め込み](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [DEMO: Phi-3 リサイクリング](https://github.com/jennifermarsman/PhiRecycling/)
      - [Phi-3-vision - ビジュアル言語アシスタント - Phi3-Vision と OpenVINO を使って](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
      - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
      - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
      - [📓][Phi-3.5 Vision マルチフレームまたはマルチ画像サンプル](./md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
      - [Microsoft.ML.OnnxRuntime .NET を使った Phi-3 Vision ローカル ONNX モデル](../../md/04.HOL/dotnet/src/LabsPhi303)
      - [メニュー形式の Phi-3 Vision ローカル ONNX モデル Microsoft.ML.OnnxRuntime .NET を使用](../../md/04.HOL/dotnet/src/LabsPhi304)

  - Reasoning-Vision サンプル
    - Phi-4-Reasoning-Vision-15B 
      - [📓] [Phi-4-Reasoning-Vision-15B を使って歩行禁止区域違反を検出する](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_Jaywalking.ipynb)
      - [📓] [Phi-4-Reasoning-Vision-15B を使って数学問題を解く](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_Math.ipynb)
      - [📓] [Phi-4-Reasoning-Vision-15B を使って UI を検出する](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_ui.ipynb)

  - 数学サンプル
    -  Phi-4-Mini-Flash-Reasoning-Instruct サンプル  [Phi-4-Mini-Flash-Reasoning-Instruct による数学デモ](./md/02.Application/09.Math/MathDemo.ipynb)

  - オーディオサンプル
    - Phi-4 サンプル 
      - [📓] [Phi-4-multimodal を使った音声書き起こしの抽出](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
      - [📓] [Phi-4-multimodal 音声サンプル](./md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
      - [📓] [Phi-4-multimodal 音声翻訳サンプル](./md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
      - [Phi-4-multimodal を使った .NET コンソールアプリケーションで音声ファイルを分析し文字起こしを生成する](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

  - MOE サンプル
    - Phi-3 / 3.5 サンプル
      - [📓] [Phi-3.5 Mixture of Experts モデル (MoEs) ソーシャルメディアサンプル](./md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
      - [📓] [NVIDIA NIM Phi-3 MOE、Azure AI Search、LlamaIndex を使った Retrieval-Augmented Generation (RAG) パイプライン構築](./md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)
      - 
  - 関数呼び出しサンプル
    - Phi-4 サンプル 🆕
      -  [📓] [Phi-4-mini での関数呼び出しの使用](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
      -  [📓] [Phi-4-mini で関数呼び出しを使いマルチエージェントを作成する](./md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
      -  [📓] [Ollama で関数呼び出しを使用する](./md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
      -  [📓] [ONNX で関数呼び出しを使用する](./md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)
  - マルチモーダルミキシングサンプル
    - Phi-4 サンプル 🆕
      -  [📓] [Phi-4-multimodal をテクノロジージャーナリストとして使用](./md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
      - [.NET コンソールアプリケーションで Phi-4-multimodal を使用して画像を分析](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Phi ファインチューニングサンプル
  - [ファインチューニングシナリオ](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [ファインチューニングと RAG の比較](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [ファインチューニング：Phi-3 を業界専門家にする](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [VS Code 用 AI ツールキットでの Phi-3 ファインチューニング](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Azure Machine Learning サービスによる Phi-3 ファインチューニング](./md/03.FineTuning/Introduce_AzureML.md)
  - [Lora を使った Phi-3 ファインチューニング](./md/03.FineTuning/FineTuning_Lora.md)
  - [QLora を使った Phi-3 ファインチューニング](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Microsoft Foundry での Phi-3 ファインチューニング](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Azure ML CLI/SDK での Phi-3 ファインチューニング](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Microsoft Olive を使ったファインチューニング](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Microsoft Olive ハンズオンラボでのファインチューニング](./md/03.FineTuning/olive-lab/readme.md)
  - [Weights and Bias を使った Phi-3-vision のファインチューニング](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [Apple MLX フレームワークを使った Phi-3 ファインチューニング](./md/03.FineTuning/FineTuning_MLX.md)
  - [Phi-3-vision ファインチューニング（公式サポート）](./md/03.FineTuning/FineTuning_Vision.md)
  - [Kaito AKSによるPhi-3のファインチューニング、Azureコンテナ（公式サポート）](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Phi-3および3.5 Visionのファインチューニング](https://github.com/2U1/Phi3-Vision-Finetune)

- ハンズオンラボ
  - [最先端モデルの探求：LLM、SLM、ローカル開発など](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [NLPの可能性を引き出す：Microsoft Oliveによるファインチューニング](https://github.com/azure/Ignite_FineTuning_workshop)

- 学術研究論文と出版物
  - [Textbooks Are All You Need II：phi-1.5技術報告](https://arxiv.org/abs/2309.05463)
  - [Phi-3技術報告：高性能な言語モデルをローカルの携帯電話で](https://arxiv.org/abs/2404.14219)
  - [Phi-4技術報告](https://arxiv.org/abs/2412.08905)
  - [Phi-4-Mini技術報告：Mixture-of-LoRAsによるコンパクトでパワフルなマルチモーダル言語モデル](https://arxiv.org/abs/2503.01743)
  - [車載用機能呼び出しに最適化された小型言語モデル](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) PHI-3の多肢選択問題解答向けファインチューニング：方法論、結果、課題](https://arxiv.org/abs/2501.01588)
  - [Phi-4推論技術報告](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Phi-4-mini推論技術報告](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Phiモデルの使用

### Microsoft Foundry上のPhi

Microsoft Phiの使い方や、さまざまなハードウェアデバイスでのE2Eソリューションの構築方法を学べます。Phiを体験するには、モデルを操作し、シナリオに合わせてPhiをカスタマイズすることから始めてください。詳しくは[Microsoft Foundry Azure AIモデルカタログ](https://aka.ms/phi3-azure-ai) と [Microsoft Foundryの開始方法](/md/02.QuickStart/AzureAIFoundry_QuickStart.md)をご覧ください。

<strong>プレイグラウンド</strong>  
各モデルには専用のプレイグラウンドがあり、モデルのテストが可能です。[Azure AI Playground](https://aka.ms/try-phi3)

### GitHubモデル上のPhi

Microsoft Phiの使い方や、さまざまなハードウェアデバイスでのE2Eソリューション構築方法を学べます。Phiを体験するには、モデルを操作しシナリオに合わせてカスタマイズしてください。詳しくは[GitHubモデルカタログ](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo)と[GitHubモデルカタログの開始方法](/md/02.QuickStart/GitHubModel_QuickStart.md)をご覧ください。

<strong>プレイグラウンド</strong>  
各モデルには専用の[プレイグラウンドがあります](/md/02.QuickStart/GitHubModel_QuickStart.md)。

### Hugging Face上のPhi

モデルは[Hugging Face](https://huggingface.co/microsoft)でも提供されています。

<strong>プレイグラウンド</strong>  
[Hugging Chatプレイグラウンド](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## 🎒 その他のコース

私たちのチームは他にも様々なコースを作成しています！ぜひチェックしてください：

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
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
 
### ジェネレーティブAIシリーズ
[![Generative AI for Beginners](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generative AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generative AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generative AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### コアラーニング
[![ML for Beginners](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science for Beginners](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI for Beginners](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Cybersecurity for Beginners](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Web Dev for Beginners](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT for Beginners](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR Development for Beginners](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilotシリーズ
[![Copilot for AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## 責任あるAI

Microsoftは、お客様が当社のAI製品を責任を持って使用できるよう支援し、学びを共有し、透明性ノートや影響評価などのツールを通じて信頼に基づくパートナーシップを築くことにコミットしています。これらのリソースの多くは[https://aka.ms/RAI](https://aka.ms/RAI)でご覧いただけます。  
Microsoftの責任あるAIへのアプローチは、公平性、信頼性と安全性、プライバシーとセキュリティ、包括性、透明性、説明責任というAIの原則に基づいています。

このサンプルで使用されている大規模な自然言語、画像、音声モデルは、不公平、不信頼、または不快な挙動をする可能性があり、それによって被害をもたらすことがあります。リスクと制限については、[Azure OpenAIサービスの透明性ノート](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text)をご参照ください。
これらのリスクを軽減する推奨される方法は、有害な行動を検出し防止できる安全システムをアーキテクチャに組み込むことです。[Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) は独立した保護レイヤーを提供し、アプリケーションやサービス内の有害なユーザー生成コンテンツおよびAI生成コンテンツを検出できます。Azure AI Content Safetyには有害な素材を検出できるテキストおよび画像のAPIが含まれています。Microsoft Foundry内では、Content Safetyサービスを使って異なるモダリティにわたる有害コンテンツの検出用のサンプルコードを閲覧、探索、試すことができます。以下の[クイックスタートドキュメント](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest)では、サービスへのリクエストの方法を案内しています。

考慮すべきもう一つの側面は全体的なアプリケーションのパフォーマンスです。マルチモーダルかつマルチモデルのアプリケーションでは、パフォーマンスとは、ユーザーやあなたの期待通りにシステムが動作し、有害な出力を生成しないことを意味します。[Performance and Quality and Risk and Safety evaluators](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) を使用して全体のアプリケーション性能を評価することが重要です。また、[カスタム評価ツール](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators)を作成して評価することもできます。

[Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html) を使うと、開発環境でAIアプリを評価できます。テストデータセットまたはターゲットを与えると、生成型AIアプリの生成物が組み込み評価器や任意のカスタム評価器で定量的に測定されます。azure ai evaluation sdkを使ってシステム評価を始めるには、[クイックスタートガイド](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk)に従ってください。評価を実行すると、[Microsoft Foundryで結果を可視化](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results) できます。

## トレードマーク

このプロジェクトにはプロジェクト名、製品名、またはサービスのトレードマークやロゴが含まれている場合があります。Microsoftのトレードマークやロゴの許可された使用は、[Microsoftのトレードマークとブランドのガイドライン](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) に従う必要があります。 このプロジェクトの改変版でのMicrosoftのトレードマークまたはロゴの使用は混乱を招いたりMicrosoftの後援を示唆したりしてはなりません。第三者のトレードマークやロゴの使用は、それら第三者の方針に従います。

## ヘルプを得る

AIアプリの構築で行き詰まったり質問がある場合は、以下に参加してください：

[![Microsoft Foundry Discord](https://img.shields.io/badge/Discord-Microsoft_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

製品のフィードバックや構築時のエラーの報告は以下へ：

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**:  
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご理解ください。原文の母国語版が正式な情報源とみなされます。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の使用による誤解や誤訳について当方は一切責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->