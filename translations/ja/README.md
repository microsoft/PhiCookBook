<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a73c59eecd7ad4ec494fd4333a29e208",
  "translation_date": "2025-10-11T10:43:03+00:00",
  "source_file": "README.md",
  "language_code": "ja"
}
-->
# Phi Cookbook: MicrosoftのPhiモデルを使った実践例

[![GitHub Codespacesでサンプルを開いて使用する](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Dev Containersで開く](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub issues](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub watchers](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub stars](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

PhiはMicrosoftが開発したオープンソースのAIモデルシリーズです。

Phiは現在、最も強力でコストパフォーマンスに優れた小型言語モデル（SLM）であり、多言語対応、推論、テキスト/チャット生成、コーディング、画像、音声などのシナリオで非常に優れたベンチマークを達成しています。

Phiはクラウドやエッジデバイスに展開可能で、限られた計算能力で生成AIアプリケーションを簡単に構築できます。

以下の手順に従ってリソースを利用してください：
1. **リポジトリをフォークする**: [![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo) をクリック
2. **リポジトリをクローンする**: `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Microsoft AI Discordコミュニティに参加して、専門家や他の開発者と交流する**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../imgs/cover.png)

### 🌐 多言語対応

#### GitHub Actionによるサポート（自動化＆常に最新）

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[アラビア語](../ar/README.md) | [ベンガル語](../bn/README.md) | [ブルガリア語](../bg/README.md) | [ビルマ語（ミャンマー）](../my/README.md) | [中国語（簡体字）](../zh/README.md) | [中国語（繁体字、香港）](../hk/README.md) | [中国語（繁体字、マカオ）](../mo/README.md) | [中国語（繁体字、台湾）](../tw/README.md) | [クロアチア語](../hr/README.md) | [チェコ語](../cs/README.md) | [デンマーク語](../da/README.md) | [オランダ語](../nl/README.md) | [エストニア語](../et/README.md) | [フィンランド語](../fi/README.md) | [フランス語](../fr/README.md) | [ドイツ語](../de/README.md) | [ギリシャ語](../el/README.md) | [ヘブライ語](../he/README.md) | [ヒンディー語](../hi/README.md) | [ハンガリー語](../hu/README.md) | [インドネシア語](../id/README.md) | [イタリア語](../it/README.md) | [日本語](./README.md) | [韓国語](../ko/README.md) | [リトアニア語](../lt/README.md) | [マレー語](../ms/README.md) | [マラーティー語](../mr/README.md) | [ネパール語](../ne/README.md) | [ノルウェー語](../no/README.md) | [ペルシャ語（ファルシー）](../fa/README.md) | [ポーランド語](../pl/README.md) | [ポルトガル語（ブラジル）](../br/README.md) | [ポルトガル語（ポルトガル）](../pt/README.md) | [パンジャブ語（グルムキー）](../pa/README.md) | [ルーマニア語](../ro/README.md) | [ロシア語](../ru/README.md) | [セルビア語（キリル文字）](../sr/README.md) | [スロバキア語](../sk/README.md) | [スロベニア語](../sl/README.md) | [スペイン語](../es/README.md) | [スワヒリ語](../sw/README.md) | [スウェーデン語](../sv/README.md) | [タガログ語（フィリピン）](../tl/README.md) | [タミル語](../ta/README.md) | [タイ語](../th/README.md) | [トルコ語](../tr/README.md) | [ウクライナ語](../uk/README.md) | [ウルドゥー語](../ur/README.md) | [ベトナム語](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## 目次

- はじめに
  - [Phiファミリーへようこそ](./md/01.Introduction/01/01.PhiFamily.md)
  - [環境のセットアップ](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [主要技術の理解](./md/01.Introduction/01/01.Understandingtech.md)
  - [PhiモデルのAI安全性](./md/01.Introduction/01/01.AISafety.md)
  - [Phiのハードウェアサポート](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Phiモデルとプラットフォームでの利用可能性](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Guidance-aiとPhiの使用](./md/01.Introduction/01/01.Guidance.md)
  - [GitHub Marketplace Models](https://github.com/marketplace/models)
  - [Azure AI Model Catalog](https://ai.azure.com)

- 異なる環境でのPhi推論
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
    - [Apple MLX FrameworkでのPhi推論](./md/01.Introduction/03/MLX_Inference.md)
    - [ローカルサーバーでのPhi推論](./md/01.Introduction/03/Local_Server_Inference.md)
    - [AI Toolkitを使用したリモートサーバーでのPhi推論](./md/01.Introduction/03/Remote_Interence.md)
    - [Rustを使用したPhi推論](./md/01.Introduction/03/Rust_Inference.md)
    - [ローカルでのPhi--Vision推論](./md/01.Introduction/03/Vision_Inference.md)
    - [Kaito AKS、Azure Containers（公式サポート）でのPhi推論](./md/01.Introduction/03/Kaito_Inference.md)
-  [Phiファミリーの量子化](./md/01.Introduction/04/QuantifyingPhi.md)
    - [llama.cppを使用したPhi-3.5 / 4の量子化](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [onnxruntimeの生成AI拡張を使用したPhi-3.5 / 4の量子化](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Intel OpenVINOを使用したPhi-3.5 / 4の量子化](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Apple MLX Frameworkを使用したPhi-3.5 / 4の量子化](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

-  Phiの評価
    - [責任あるAI](./md/01.Introduction/05/ResponsibleAI.md)
    - [評価のためのAzure AI Foundry](./md/01.Introduction/05/AIFoundry.md)
    - [Promptflowを使用した評価](./md/01.Introduction/05/Promptflow.md)
 
- Azure AI Searchを使用したRAG
    - [Phi-4-miniとPhi-4-multimodal(RAG)をAzure AI Searchで使用する方法](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Phiアプリケーション開発サンプル
  - テキスト＆チャットアプリケーション
    - Phi-4 サンプル 🆕
      - [📓] [Phi-4-mini ONNXモデルでチャット](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Phi-4ローカルONNXモデル .NETでチャット](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Sementic Kernelを使用したPhi-4 ONNXの.NETコンソールアプリでのチャット](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Phi-3 / 3.5 サンプル
      - [ブラウザでPhi3、ONNX Runtime Web、WebGPUを使用したローカルチャットボット](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVino Chat](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [マルチモデル - Phi-3-miniとOpenAI Whisperのインタラクティブ](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - ラッパーの構築とPhi-3を使用したMLFlow](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [モデル最適化 - Oliveを使用したONNX Runtime Web向けPhi-3-minモデルの最適化方法](https://github.com/microsoft/Olive/tree/main/examples/phi3)
- [WinUI3 アプリと Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
- [WinUI3 マルチモデル AI 搭載ノートアプリのサンプル](https://github.com/microsoft/ai-powered-notes-winui3-sample)
- [カスタム Phi-3 モデルを Prompt flow と統合して微調整する](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
- [Azure AI Foundry でカスタム Phi-3 モデルを Prompt flow と統合して微調整する](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
- [Microsoft の責任ある AI 原則に焦点を当てた Azure AI Foundry での微調整された Phi-3 / Phi-3.5 モデルの評価](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
- [📓] [Phi-3.5-mini-instruct 言語予測サンプル (中国語/英語)](../../md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
- [Phi-3.5-Instruct WebGPU RAG チャットボット](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
- [Windows GPU を使用して Phi-3.5-Instruct ONNX を用いた Prompt flow ソリューションを作成する](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
- [Microsoft Phi-3.5 tflite を使用して Android アプリを作成する](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
- [Microsoft.ML.OnnxRuntime を使用したローカル ONNX Phi-3 モデルによる Q&A .NET サンプル](../../md/04.HOL/dotnet/src/LabsPhi301)
- [Semantic Kernel と Phi-3 を使用したコンソールチャット .NET アプリ](../../md/04.HOL/dotnet/src/LabsPhi302)

- Azure AI 推論 SDK コードベースのサンプル
  - Phi-4 サンプル 🆕
    - [📓] [Phi-4-multimodal を使用してプロジェクトコードを生成する](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
  - Phi-3 / 3.5 サンプル
    - [Microsoft Phi-3 ファミリーを使用して Visual Studio Code GitHub Copilot チャットを構築する](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
    - [GitHub モデルを使用して Phi-3.5 を用いた Visual Studio Code チャットエージェントを作成する](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

- 高度な推論サンプル
  - Phi-4 サンプル 🆕
    - [📓] [Phi-4-mini-reasoning または Phi-4-reasoning サンプル](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
    - [📓] [Microsoft Olive を使用した Phi-4-mini-reasoning の微調整](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
    - [📓] [Apple MLX を使用した Phi-4-mini-reasoning の微調整](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
    - [📓] [GitHub モデルを使用した Phi-4-mini-reasoning](../../md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
    - [📓] [Azure AI Foundry モデルを使用した Phi-4-mini-reasoning](../../md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
- デモ
    - [Hugging Face Spaces にホストされた Phi-4-mini デモ](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
    - [Hugging Face Spaces にホストされた Phi-4-multimodal デモ](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
- ビジョンサンプル
  - Phi-4 サンプル 🆕
    - [📓] [Phi-4-multimodal を使用して画像を読み取りコードを生成する](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
  - Phi-3 / 3.5 サンプル
    - [📓][Phi-3-vision-画像テキストからテキストへ](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
    - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
    - [📓][Phi-3-vision CLIP 埋め込み](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
    - [デモ: Phi-3 リサイクル](https://github.com/jennifermarsman/PhiRecycling/)
    - [Phi-3-vision - Phi3-Vision と OpenVINO を使用した視覚言語アシスタント](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
    - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
    - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
    - [📓][Phi-3.5 Vision マルチフレームまたはマルチ画像サンプル](../../md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
    - [Microsoft.ML.OnnxRuntime .NET を使用したローカル ONNX モデルによる Phi-3 Vision](../../md/04.HOL/dotnet/src/LabsPhi303)
    - [Microsoft.ML.OnnxRuntime .NET を使用したメニュー形式のローカル ONNX モデルによる Phi-3 Vision](../../md/04.HOL/dotnet/src/LabsPhi304)

- 数学サンプル
  - Phi-4-Mini-Flash-Reasoning-Instruct サンプル 🆕 [Phi-4-Mini-Flash-Reasoning-Instruct を使用した数学デモ](../../md/02.Application/09.Math/MathDemo.ipynb)

- オーディオサンプル
  - Phi-4 サンプル 🆕
    - [📓] [Phi-4-multimodal を使用した音声トランスクリプトの抽出](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
    - [📓] [Phi-4-multimodal オーディオサンプル](../../md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
    - [📓] [Phi-4-multimodal 音声翻訳サンプル](../../md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
    - [.NET コンソールアプリケーションを使用して Phi-4-multimodal オーディオで音声ファイルを分析しトランスクリプトを生成する](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

- MOE サンプル
  - Phi-3 / 3.5 サンプル
    - [📓] [Phi-3.5 Mixture of Experts Models (MoEs) ソーシャルメディアサンプル](../../md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
    - [📓] [NVIDIA NIM Phi-3 MOE、Azure AI Search、LlamaIndex を使用した Retrieval-Augmented Generation (RAG) パイプラインの構築](../../md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)

- 関数呼び出しサンプル
  - Phi-4 サンプル 🆕
    - [📓] [Phi-4-mini を使用した関数呼び出し](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
    - [📓] [Phi-4-mini を使用してマルチエージェントを作成する関数呼び出し](../../md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
    - [📓] [Ollama を使用した関数呼び出し](../../md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
    - [📓] [ONNX を使用した関数呼び出し](../../md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)

- マルチモーダルミキシングサンプル
  - Phi-4 サンプル 🆕
    - [📓] [Phi-4-multimodal を使用して技術ジャーナリストとして活動する](../../md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
    - [.NET コンソールアプリケーションを使用して Phi-4-multimodal で画像を分析する](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Phi の微調整サンプル
  - [微調整シナリオ](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [微調整 vs RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [Phi-3 を業界の専門家にする微調整](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [VS Code 用 AI ツールキットを使用した Phi-3 の微調整](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Azure Machine Learning Service を使用した Phi-3 の微調整](./md/03.FineTuning/Introduce_AzureML.md)
  - [Lora を使用した Phi-3 の微調整](./md/03.FineTuning/FineTuning_Lora.md)
  - [QLora を使用した Phi-3 の微調整](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Azure AI Foundry を使用した Phi-3 の微調整](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Azure ML CLI/SDK を使用した Phi-3 の微調整](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Microsoft Olive を使用した微調整](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Microsoft Olive ハンズオンラボを使用した微調整](./md/03.FineTuning/olive-lab/readme.md)
  - [Weights and Bias を使用した Phi-3-vision の微調整](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [Apple MLX Framework を使用した Phi-3 の微調整](./md/03.FineTuning/FineTuning_MLX.md)
  - [Phi-3-vision の微調整 (公式サポート)](./md/03.FineTuning/FineTuning_Vision.md)
  - [Kaito AKS、Azure Containers を使用した Phi-3 の微調整 (公式サポート)](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Phi-3 および 3.5 Vision の微調整](https://github.com/2U1/Phi3-Vision-Finetune)

- ハンズオンラボ
  - [最先端モデルの探求: LLMs、SLMs、ローカル開発など](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [NLP の可能性を解き放つ: Microsoft Olive を使用した微調整](https://github.com/azure/Ignite_FineTuning_workshop)

- 学術研究論文と出版物
  - [Textbooks Are All You Need II: phi-1.5 技術レポート](https://arxiv.org/abs/2309.05463)
  - [Phi-3 技術レポート: 高性能な言語モデルをスマートフォンでローカルに](https://arxiv.org/abs/2404.14219)
  - [Phi-4 技術レポート](https://arxiv.org/abs/2412.08905)
  - [Phi-4-Mini 技術レポート: Mixture-of-LoRAs によるコンパクトで強力なマルチモーダル言語モデル](https://arxiv.org/abs/2503.01743)
  - [車載機能呼び出しのための小型言語モデルの最適化](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) PHI-3を選択式質問応答に特化させる: 方法論、結果、課題](https://arxiv.org/abs/2501.01588)
  - [Phi-4推論技術レポート](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Phi-4-mini推論技術レポート](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Phiモデルの利用方法

### Azure AI FoundryでのPhi

Microsoft Phiの使用方法や、さまざまなハードウェアデバイスでのE2Eソリューションの構築方法を学ぶことができます。Phiを体験するには、モデルを試してみたり、シナリオに合わせてPhiをカスタマイズすることから始めてください。 [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai)で詳細を確認できます。[Azure AI Foundryの入門ガイド](/md/02.QuickStart/AzureAIFoundry_QuickStart.md)も参照してください。

**プレイグラウンド**
各モデルには専用のプレイグラウンドがあり、モデルをテストできます。[Azure AI Playground](https://aka.ms/try-phi3)。

### GitHubモデルでのPhi

Microsoft Phiの使用方法や、さまざまなハードウェアデバイスでのE2Eソリューションの構築方法を学ぶことができます。Phiを体験するには、モデルを試してみたり、シナリオに合わせてPhiをカスタマイズすることから始めてください。 [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo)で詳細を確認できます。[GitHub Model Catalogの入門ガイド](/md/02.QuickStart/GitHubModel_QuickStart.md)も参照してください。

**プレイグラウンド**
各モデルには専用の[プレイグラウンドがあります](/md/02.QuickStart/GitHubModel_QuickStart.md)。

### Hugging FaceでのPhi

モデルは[Hugging Face](https://huggingface.co/microsoft)でも見つけることができます。

**プレイグラウンド**
 [Hugging Chatプレイグラウンド](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## 責任あるAI

Microsoftは、AI製品を責任を持って使用するための支援、学びの共有、透明性ノートや影響評価などのツールを通じた信頼に基づくパートナーシップの構築に取り組んでいます。これらのリソースの多くは[https://aka.ms/RAI](https://aka.ms/RAI)で見つけることができます。
Microsoftの責任あるAIへのアプローチは、公平性、信頼性と安全性、プライバシーとセキュリティ、包括性、透明性、責任というAI原則に基づいています。

このサンプルで使用されるような大規模な自然言語、画像、音声モデルは、不公平、不信頼、または攻撃的な振る舞いをする可能性があり、それによって害を引き起こすことがあります。[Azure OpenAIサービス透明性ノート](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text)を参照し、リスクと制限について理解してください。

これらのリスクを軽減するための推奨されるアプローチは、有害な振る舞いを検出し防止する安全システムをアーキテクチャに組み込むことです。[Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview)は、独立した保護層を提供し、アプリケーションやサービス内のユーザー生成コンテンツやAI生成コンテンツの有害性を検出することができます。Azure AI Content Safetyには、有害な素材を検出するためのテキストおよび画像APIが含まれています。Azure AI Foundry内では、Content Safetyサービスを使用して、異なるモダリティで有害なコンテンツを検出するサンプルコードを表示、探索、試すことができます。[クイックスタートドキュメント](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest)では、サービスへのリクエストの作成方法を案内しています。

もう一つ考慮すべき側面は、全体的なアプリケーションのパフォーマンスです。マルチモーダルおよびマルチモデルアプリケーションでは、パフォーマンスとは、システムがユーザーの期待通りに動作し、有害な出力を生成しないことを意味します。[Performance and Quality and Risk and Safety evaluators](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in)を使用して、全体的なアプリケーションのパフォーマンスを評価することが重要です。また、[カスタム評価ツール](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators)を作成して評価することも可能です。

開発環境でAIアプリケーションを評価するには、[Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html)を使用できます。テストデータセットまたはターゲットを指定すると、生成AIアプリケーションの生成物が組み込み評価ツールや選択したカスタム評価ツールで定量的に測定されます。Azure AI Evaluation SDKを使用してシステムを評価する方法については、[クイックスタートガイド](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk)を参照してください。評価を実行した後は、[Azure AI Foundryで結果を視覚化](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results)することができます。

## 商標

このプロジェクトには、プロジェクト、製品、またはサービスの商標やロゴが含まれている場合があります。Microsoftの商標やロゴの使用は、[Microsoftの商標およびブランドガイドライン](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general)に従う必要があります。
このプロジェクトの改変版でMicrosoftの商標やロゴを使用する場合、混乱を招いたりMicrosoftの後援を示唆することがあってはなりません。第三者の商標やロゴの使用は、それぞれの第三者のポリシーに従う必要があります。

---

**免責事項**:  
この文書は、AI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知ください。元の言語で記載された文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤解について、当社は責任を負いません。