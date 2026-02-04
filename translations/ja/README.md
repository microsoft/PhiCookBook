# Phi クックブック: マイクロソフトの Phi モデルを使った実践例

[![GitHub Codespaces でサンプルを開いて使う](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Dev Containers で開く](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub コントリビューター](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub イシュー](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub プルリクエスト](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PR歓迎](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub ウォッチャー数](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub フォーク数](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub スター数](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi はマイクロソフトによって開発されたオープンソースの AI モデル群です。

Phi は現在、最も強力でコスト効率に優れた小規模言語モデル（SLM）であり、多言語、推論、テキスト／チャット生成、コーディング、画像、音声、その他のシナリオで非常に良好なベンチマークを誇ります。

Phi はクラウドやエッジデバイスに展開可能で、限られた計算能力でも生成AIアプリケーションを簡単に構築できます。

これらのリソースを使い始めるには、次の手順に従ってください：
1. **リポジトリをフォークする**: クリック [![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **リポジトリをクローンする**:   `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Microsoft AI Discord コミュニティに参加して、専門家や開発者仲間と交流**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/ja/cover.eb18d1b9605d754b.webp)

### 🌐 多言語サポート

#### GitHub Action による対応（自動化かつ常に最新）

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[アラビア語](../ar/README.md) | [ベンガル語](../bn/README.md) | [ブルガリア語](../bg/README.md) | [ビルマ語（ミャンマー）](../my/README.md) | [中国語（簡体字）](../zh-CN/README.md) | [中国語（繁体字、香港）](../zh-HK/README.md) | [中国語（繁体字、マカオ）](../zh-MO/README.md) | [中国語（繁体字、台湾）](../zh-TW/README.md) | [クロアチア語](../hr/README.md) | [チェコ語](../cs/README.md) | [デンマーク語](../da/README.md) | [オランダ語](../nl/README.md) | [エストニア語](../et/README.md) | [フィンランド語](../fi/README.md) | [フランス語](../fr/README.md) | [ドイツ語](../de/README.md) | [ギリシャ語](../el/README.md) | [ヘブライ語](../he/README.md) | [ヒンディー語](../hi/README.md) | [ハンガリー語](../hu/README.md) | [インドネシア語](../id/README.md) | [イタリア語](../it/README.md) | [日本語](./README.md) | [カンナダ語](../kn/README.md) | [韓国語](../ko/README.md) | [リトアニア語](../lt/README.md) | [マレー語](../ms/README.md) | [マラヤーラム語](../ml/README.md) | [マラーティー語](../mr/README.md) | [ネパール語](../ne/README.md) | [ナイジェリア・ピジン語](../pcm/README.md) | [ノルウェー語](../no/README.md) | [ペルシャ語（ファルシ）](../fa/README.md) | [ポーランド語](../pl/README.md) | [ポルトガル語（ブラジル）](../pt-BR/README.md) | [ポルトガル語（ポルトガル）](../pt-PT/README.md) | [パンジャブ語（グルムキー）](../pa/README.md) | [ルーマニア語](../ro/README.md) | [ロシア語](../ru/README.md) | [セルビア語（キリル文字）](../sr/README.md) | [スロバキア語](../sk/README.md) | [スロベニア語](../sl/README.md) | [スペイン語](../es/README.md) | [スワヒリ語](../sw/README.md) | [スウェーデン語](../sv/README.md) | [タガログ語（フィリピン）](../tl/README.md) | [タミル語](../ta/README.md) | [テルグ語](../te/README.md) | [タイ語](../th/README.md) | [トルコ語](../tr/README.md) | [ウクライナ語](../uk/README.md) | [ウルドゥー語](../ur/README.md) | [ベトナム語](../vi/README.md)

> **ローカルにクローンしたいですか？**

> このリポジトリには50以上の言語翻訳が含まれており、ダウンロードサイズが大幅に増加します。翻訳なしでクローンするには sparse checkout を使用してください：
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/PhiCookBook.git
> cd PhiCookBook
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> これにより、コースを完了するのに必要なすべてのものがはるかに高速にダウンロードできます。
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## 目次

- はじめに
  - [Phi ファミリーへようこそ](./md/01.Introduction/01/01.PhiFamily.md)
  - [環境のセットアップ](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [主要技術の理解](./md/01.Introduction/01/01.Understandingtech.md)
  - [Phi モデルの AI セーフティ](./md/01.Introduction/01/01.AISafety.md)
  - [Phi ハードウェアサポート](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Phi モデルとプラットフォーム別対応状況](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Guidance-ai と Phi の使用方法](./md/01.Introduction/01/01.Guidance.md)
  - [GitHub Marketplace モデル](https://github.com/marketplace/models)
  - [Azure AI モデルカタログ](https://ai.azure.com)

- さまざまな環境での Phi 推論
    -  [Hugging face](./md/01.Introduction/02/01.HF.md)
    -  [GitHub モデル](./md/01.Introduction/02/02.GitHubModel.md)
    -  [Azure AI Foundry モデルカタログ](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    -  [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md)

- Phi ファミリーの推論
    - [iOS での Phi 推論](./md/01.Introduction/03/iOS_Inference.md)
    - [Android での Phi 推論](./md/01.Introduction/03/Android_Inference.md)
    - [Jetson での Phi 推論](./md/01.Introduction/03/Jetson_Inference.md)
    - [AI PC での Phi 推論](./md/01.Introduction/03/AIPC_Inference.md)
    - [Apple MLX フレームワークでの Phi 推論](./md/01.Introduction/03/MLX_Inference.md)
    - [ローカルサーバーでの Phi 推論](./md/01.Introduction/03/Local_Server_Inference.md)
    - [AI Toolkit を使ったリモートサーバーでの Phi 推論](./md/01.Introduction/03/Remote_Interence.md)
    - [Rust での Phi 推論](./md/01.Introduction/03/Rust_Inference.md)
    - [ローカルでの Phi Vision 推論](./md/01.Introduction/03/Vision_Inference.md)
    - [Kaito AKS、Azure Containers を使った Phi 推論（公式サポート）](./md/01.Introduction/03/Kaito_Inference.md)
-  [Phi ファミリーの量子化](./md/01.Introduction/04/QuantifyingPhi.md)
    - [llama.cpp を使った Phi-3.5 / 4 の量子化](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [onnxruntime 用の生成 AI 拡張を使った Phi-3.5 / 4 の量子化](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Intel OpenVINO を使った Phi-3.5 / 4 の量子化](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Apple MLX フレームワークを使った Phi-3.5 / 4 の量子化](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

-  Phi の評価
    - [責任ある AI](./md/01.Introduction/05/ResponsibleAI.md)
    - [Azure AI Foundry を使った評価](./md/01.Introduction/05/AIFoundry.md)
    - [Promptflow を使った評価](./md/01.Introduction/05/Promptflow.md)
 
- Azure AI Search を使った RAG
    - [Azure AI Search で Phi-4-mini と Phi-4-multimodal（RAG）を使う方法](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Phi アプリケーション開発サンプル
  - テキスト＆チャットアプリケーション
    - Phi-4 サンプル 🆕
      - [📓] [Phi-4-mini ONNX モデルとチャット](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Phi-4 ローカル ONNX モデルでチャット .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [セマンティックカーネルを使った Phi-4 ONNX の .NET コンソールアプリチャット](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Phi-3 / 3.5 サンプル
      - [Phi3 と ONNX Runtime Web、WebGPU を用いたブラウザ内ローカルチャットボット](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVino チャット](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [マルチモデル - インタラクティブ Phi-3-mini と OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - ラッパーの構築と MLFlow と Phi-3 の使用](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [モデル最適化 - Olive を使った ONNX Runtime Web 用 Phi-3-min モデルの最適化方法](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [WinUI3 アプリでの Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      -[WinUI3 マルチモデル AI パワードノートアプリ サンプル](https://github.com/microsoft/ai-powered-notes-winui3-sample)
      - [カスタム Phi-3 モデルの微調整と Prompt flow との統合](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
      - [Azure AI Foundry でカスタム Phi-3 モデルを微調整し Prompt flow と統合](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
      - [Microsoft の責任ある AI 原則に焦点を当てた Azure AI Foundry での微調整 Phi-3 / Phi-3.5 モデルの評価](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
      - [📓] [Phi-3.5-mini-instruct 言語予測サンプル（中国語/英語）](./md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
      - [Phi-3.5-Instruct WebGPU RAG チャットボット](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
      - [Windows GPU を使用して Phi-3.5-Instruct ONNX の Prompt flow ソリューションを作成](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
      - [Microsoft Phi-3.5 tflite を利用して Android アプリを作成](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
      - [Microsoft.ML.OnnxRuntime を使ったローカル ONNX Phi-3 モデルの Q&A .NET サンプル](../../md/04.HOL/dotnet/src/LabsPhi301)
      - [Semantic Kernel と Phi-3 を使ったコンソールチャット .NET アプリ](../../md/04.HOL/dotnet/src/LabsPhi302)

  - Azure AI 推論 SDK コードベース サンプル
    - Phi-4 サンプル 🆕
      - [📓] [Phi-4-multimodal を使ったプロジェクトコード生成](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
    - Phi-3 / 3.5 サンプル
      - [Microsoft Phi-3 ファミリーを使ったオリジナルの Visual Studio Code GitHub Copilot チャット作成](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
      - [GitHub モデルを使い Phi-3.5 で自作 Visual Studio Code チャット Copilot エージェント作成](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

  - 高度な推論サンプル
    - Phi-4 サンプル 🆕
      - [📓] [Phi-4-mini-reasoning または Phi-4-reasoning サンプル](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
      - [📓] [Microsoft Olive を使った Phi-4-mini-reasoning のファインチューニング](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Apple MLX を使った Phi-4-mini-reasoning のファインチューニング](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [GitHub モデルでの Phi-4-mini-reasoning](./md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
      - [📓] [Azure AI Foundry モデルでの Phi-4-mini-reasoning](./md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
  - デモ
      - [Hugging Face Spaces でホストされている Phi-4-mini デモ](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
      - [Hugging Face Spaces でホストされている Phi-4-multimodal デモ](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
  - ビジョンサンプル
    - Phi-4 サンプル 🆕
      - [📓] [Phi-4-multimodal を使って画像を読み込みコード生成](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md)
    - Phi-3 / 3.5 サンプル
      -  [📓][Phi-3-vision-画像テキストからテキスト](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
      - [📓][Phi-3-vision CLIP 埋め込み](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [デモ: Phi-3 リサイクリング](https://github.com/jennifermarsman/PhiRecycling/)
      - [Phi-3-vision - Phi3-Vision と OpenVINO を使ったビジュアル言語アシスタント](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
      - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
      - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
      - [📓][Phi-3.5 Vision マルチフレームまたはマルチイメージサンプル](./md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
      - [Microsoft.ML.OnnxRuntime .NET を使ったローカル Phi-3 Vision ONNX モデル](../../md/04.HOL/dotnet/src/LabsPhi303)
      - [メニュー形式の Phi-3 Vision ローカル ONNX モデル Microsoft.ML.OnnxRuntime .NET 使用](../../md/04.HOL/dotnet/src/LabsPhi304)

  - 数学サンプル
    - Phi-4-Mini-Flash-Reasoning-Instruct サンプル 🆕 [Phi-4-Mini-Flash-Reasoning-Instruct での数学デモ](./md/02.Application/09.Math/MathDemo.ipynb)

  - オーディオサンプル
    - Phi-4 サンプル 🆕
      - [📓] [Phi-4-multimodal を使ったオーディオ文字起こし抽出](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
      - [📓] [Phi-4-multimodal オーディオサンプル](./md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
      - [📓] [Phi-4-multimodal 音声翻訳サンプル](./md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
      - [Phi-4-multimodal オーディオを使った .NET コンソールアプリケーションで音声ファイル解析と文字起こし生成](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

  - MoE サンプル
    - Phi-3 / 3.5 サンプル
      - [📓] [Phi-3.5 Mixture of Experts モデル (MoEs) ソーシャルメディアサンプル](./md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
      - [📓] [NVIDIA NIM Phi-3 MOE、Azure AI Search、LlamaIndex を使った検索拡張生成 (RAG) パイプライン構築](./md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)
      - 
  - 関数呼び出しサンプル
    - Phi-4 サンプル 🆕
      -  [📓] [Phi-4-mini での関数呼び出しの使用](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
      -  [📓] [Phi-4-mini で関数呼び出しを使いマルチエージェント作成](./md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
      -  [📓] [Ollama での関数呼び出しの使用](./md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
      -  [📓] [ONNX での関数呼び出しの使用](./md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)
  - マルチモーダルミキシングサンプル
    - Phi-4 サンプル 🆕
      -  [📓] [Phi-4-multimodal をテクノロジージャーナリストとして使用](./md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
      - [Phi-4-multimodal を使った画像解析の .NET コンソールアプリケーション](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Phi 微調整サンプル
  - [微調整シナリオ](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [微調整と RAG の比較](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [Phi-3 を業界専門家にする微調整](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [VS Code 用 AI Toolkit での Phi-3 微調整](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Azure Machine Learning Service を使った Phi-3 微調整](./md/03.FineTuning/Introduce_AzureML.md)
  - [Lora を使った Phi-3 微調整](./md/03.FineTuning/FineTuning_Lora.md)
  - [QLora を使った Phi-3 微調整](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Azure AI Foundry を使った Phi-3 微調整](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Azure ML CLI/SDK を使った Phi-3 微調整](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Microsoft Olive を使った微調整](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Microsoft Olive ハンズオンラボによる微調整](./md/03.FineTuning/olive-lab/readme.md)
  - [Weights and Biases を使った Phi-3-vision 微調整](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [Apple MLX フレームワークを使った Phi-3 微調整](./md/03.FineTuning/FineTuning_MLX.md)
  - [Phi-3-vision の公式対応による微調整](./md/03.FineTuning/FineTuning_Vision.md)
  - [Kaito AKS、Azure コンテナを使った Phi-3 の公式サポートによる微調整](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Phi-3 と 3.5 Vision の微調整](https://github.com/2U1/Phi3-Vision-Finetune)

- ハンズオンラボ
  - [最新モデルの探求: LLM、SLM、ローカル開発など](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [NLP の可能性を開く: Microsoft Olive によるファインチューニング](https://github.com/azure/Ignite_FineTuning_workshop)

- 学術研究論文と出版物
  - [Textbooks Are All You Need II: phi-1.5 技術レポート](https://arxiv.org/abs/2309.05463)
  - [Phi-3 技術レポート: あなたの携帯電話上で高性能の言語モデルをローカルに](https://arxiv.org/abs/2404.14219)
  - [Phi-4 技術レポート](https://arxiv.org/abs/2412.08905)
  - [Phi-4-Mini 技術レポート: Mixture-of-LoRAs を用いたコンパクトかつ強力なマルチモーダル言語モデル](https://arxiv.org/abs/2503.01743)
  - [車載機能呼び出し向け小規模言語モデルの最適化](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) PHI-3 を用いた多肢選択式質問応答のファインチューニング: 方法論、結果、および課題](https://arxiv.org/abs/2501.01588)
  - [Phi-4-reasoning 技術レポート](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Phi-4-mini-reasoning 技術レポート](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Phi モデルの使用

### Azure AI Foundry 上の Phi

Microsoft Phi の使い方や、さまざまなハードウェアデバイスでエンドツーエンドのソリューションを構築する方法を学べます。Phiを自分で体験するには、モデルを操作したり、シナリオに合わせて Phi をカスタマイズしたりしてみてください。詳しくは [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai) を参照し、[Azure AI Foundryのクイックスタート](/md/02.QuickStart/AzureAIFoundry_QuickStart.md)でさらに理解を深められます。

**プレイグラウンド**  
各モデルには専用のプレイグラウンドがあり、モデルのテストが可能です。[Azure AI Playground](https://aka.ms/try-phi3)をご利用ください。

### GitHub Models 上の Phi

Microsoft Phi の使い方や、各種ハードウェアデバイスでエンドツーエンドのソリューションを構築する方法を学べます。Phi を体験するには、モデルを操作し、シナリオに合わせてカスタマイズしてみてください。[GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo)を利用し、[GitHub Model Catalogのクイックスタート](/md/02.QuickStart/GitHubModel_QuickStart.md)で詳細を学べます。

**プレイグラウンド**  
各モデルに専用の[モデルテストプレイグラウンド](/md/02.QuickStart/GitHubModel_QuickStart.md)があります。

### Hugging Face 上の Phi

モデルは [Hugging Face](https://huggingface.co/microsoft) でも見つけられます。

**プレイグラウンド**  
[Hugging Chat プレイグラウンド](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## 🎒 その他のコース

当チームは他のコースも提供しています！ぜひご覧ください：

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![初心者向け LangChain4j](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![初心者向け LangChain.js](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

---

### Azure / Edge / MCP / エージェント
[![初心者向け AZD](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![初心者向け Edge AI](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![初心者向け MCP](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![初心者向け AI エージェント](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### 生成AIシリーズ
[![初心者向け 生成AI](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![生成AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![生成AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![生成AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### コア学習
[![初心者向け ML](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![初心者向け データサイエンス](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![初心者向け AI](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![初心者向け サイバーセキュリティ](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![初心者向け Web 開発](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![初心者向け IoT](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![初心者向け XR 開発](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot シリーズ
[![AIペアプログラミング用 Copilot](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![C#/.NET用 Copilot](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot アドベンチャー](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Responsible AI

Microsoft は、お客様が当社の AI 製品を責任を持って使用できるよう支援し、学びを共有し、Transparency Notes や Impact Assessments などのツールを通じて信頼に基づくパートナーシップを構築することに取り組んでいます。これらのリソースの多くは [https://aka.ms/RAI](https://aka.ms/RAI) でご覧いただけます。  
Microsoft の責任ある AI へのアプローチは、公平性、信頼性と安全性、プライバシーとセキュリティ、包摂性、透明性、説明責任という AI 原則に基づいています。

このサンプルで使用されるような、大規模な自然言語、画像、および音声モデルは、不公平、不信頼、または攻撃的な振る舞いをする可能性があり、その結果として害を及ぼすことがあります。リスクと制限については、[Azure OpenAI サービス Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text)をご参照ください。

これらのリスクを緩和する推奨方法は、有害な動作を検出・防止できる安全システムをアーキテクチャに組み込むことです。[Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) は、アプリケーションやサービス内で有害なユーザー生成コンテンツや AI 生成コンテンツを検出できる独立した保護層を提供します。Azure AI Content Safety には、有害な内容を検出可能なテキストおよび画像の API が含まれています。Azure AI Foundry 内では、Content Safety サービスを通じて、様々なモダリティにわたる有害コンテンツの検出サンプルコードの閲覧、探索、試用が可能です。以下の[クイックスタートドキュメント](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest)では、サービスへのリクエスト方法を案内しています。

もう一つの考慮すべき点は、全体的なアプリケーションのパフォーマンスです。マルチモーダルおよびマルチモデルのアプリケーションにおいて、パフォーマンスとは、システムがユーザーの期待通りに動作し、有害な出力を生成しないことを意味します。アプリケーション全体のパフォーマンスを評価するには、[Performance and Quality and Risk and Safety evaluators](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) を使用することが重要です。また、[カスタム評価器](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators)を作成し評価することも可能です。
開発環境でAIアプリケーションを評価するには、[Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html) を使用できます。テストデータセットまたはターゲットのいずれかを指定すると、生成されたAIアプリケーションの出力が組み込みの評価者や選択したカスタム評価者によって定量的に測定されます。azure ai evaluation sdkを使ってシステムの評価を始めるには、[クイックスタートガイド](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk)に従ってください。評価実行を完了すると、[Azure AI Foundryで結果を可視化](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results)できます。

## トレードマーク

このプロジェクトには、プロジェクト、製品、サービスの商標やロゴが含まれている場合があります。Microsoftの商標やロゴの正当な使用は、[Microsoftの商標およびブランドガイドライン](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general)に従う必要があります。
Microsoftの商標やロゴを変更版のプロジェクトで使用する場合は、混乱を招いたりMicrosoftのスポンサーシップを示唆してはなりません。第三者の商標やロゴの使用は、それら第三者のポリシーに従います。

## サポートを受ける

AIアプリの構築で困ったり質問がある場合は、以下に参加してください。

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

製品のフィードバックや構築中のエラーについては、こちらを参照してください。

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類はAI翻訳サービス「Co-op Translator」（https://github.com/Azure/co-op-translator）を利用して翻訳されています。正確性には努めておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語版が正式な情報源としてご利用ください。重要な情報については、専門の翻訳者による翻訳を推奨いたします。本翻訳の利用により生じたいかなる誤解や誤訳についても、当方は責任を負いかねますのでご了承ください。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
