<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5c07bb4c3c89a36c9be332a065a9a33c",
  "translation_date": "2025-07-16T15:00:16+00:00",
  "source_file": "README.md",
  "language_code": "ja"
}
-->
# Phi クックブック：Microsoft の Phi モデルを使った実践例

[![GitHub Codespaces でサンプルを開いて使う](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)  
[![Dev Containers で開く](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub コントリビューター](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)  
[![GitHub イシュー](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)  
[![GitHub プルリクエスト](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)  
[![PR歓迎](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub ウォッチャー](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)  
[![GitHub フォーク](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)  
[![GitHub スター](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Azure AI Community Discord](https://dcbadge.vercel.app/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

Phi は Microsoft が開発したオープンソースの AI モデル群です。

Phi は現在、最も強力でコスト効率の高い小型言語モデル（SLM）であり、多言語対応、推論、テキスト／チャット生成、コーディング、画像、音声など様々なシナリオで優れたベンチマークを誇ります。

Phi はクラウドやエッジデバイスに展開可能で、限られた計算リソースでも簡単に生成系 AI アプリケーションを構築できます。

これらのリソースを使い始めるには、以下の手順に従ってください：  
1. **リポジトリをフォークする**：クリック [![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)  
2. **リポジトリをクローンする**： `git clone https://github.com/microsoft/PhiCookBook.git`  
3. [**Microsoft AI Discord コミュニティに参加して、専門家や開発者仲間と交流する**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/cover.eb18d1b9605d754b30973f4e17c6e11ea4f8473d9686ee378d6e7b44e3c70ac7.ja.png)

### 🌐 多言語対応

#### GitHub Actions によるサポート（自動化＆常に最新）

[フランス語](../fr/README.md) | [スペイン語](../es/README.md) | [ドイツ語](../de/README.md) | [ロシア語](../ru/README.md) | [アラビア語](../ar/README.md) | [ペルシャ語（ファルシ）](../fa/README.md) | [ウルドゥー語](../ur/README.md) | [中国語（簡体字）](../zh/README.md) | [中国語（繁体字、マカオ）](../mo/README.md) | [中国語（繁体字、香港）](../hk/README.md) | [中国語（繁体字、台湾）](../tw/README.md) | [日本語](./README.md) | [韓国語](../ko/README.md) | [ヒンディー語](../hi/README.md)  
[ベンガル語](../bn/README.md) | [マラーティー語](../mr/README.md) | [ネパール語](../ne/README.md) | [パンジャブ語（グルムキー）](../pa/README.md) | [ポルトガル語（ポルトガル）](../pt/README.md) | [ポルトガル語（ブラジル）](../br/README.md) | [イタリア語](../it/README.md) | [ポーランド語](../pl/README.md) | [トルコ語](../tr/README.md) | [ギリシャ語](../el/README.md) | [タイ語](../th/README.md) | [スウェーデン語](../sv/README.md) | [デンマーク語](../da/README.md) | [ノルウェー語](../no/README.md) | [フィンランド語](../fi/README.md) | [オランダ語](../nl/README.md) | [ヘブライ語](../he/README.md) | [ベトナム語](../vi/README.md) | [インドネシア語](../id/README.md) | [マレー語](../ms/README.md) | [タガログ語（フィリピン）](../tl/README.md) | [スワヒリ語](../sw/README.md) | [ハンガリー語](../hu/README.md) | [チェコ語](../cs/README.md) | [スロバキア語](../sk/README.md) | [ルーマニア語](../ro/README.md) | [ブルガリア語](../bg/README.md) | [セルビア語（キリル）](../sr/README.md) | [クロアチア語](../hr/README.md) | [スロベニア語](../sl/README.md)

## 目次

- はじめに  
  - [Phi ファミリーへようこそ](./md/01.Introduction/01/01.PhiFamily.md)  
  - [環境設定](./md/01.Introduction/01/01.EnvironmentSetup.md)  
  - [主要技術の理解](./md/01.Introduction/01/01.Understandingtech.md)  
  - [Phi モデルの AI セーフティ](./md/01.Introduction/01/01.AISafety.md)  
  - [Phi ハードウェアサポート](./md/01.Introduction/01/01.Hardwaresupport.md)  
  - [Phi モデルとプラットフォーム別の利用可能性](./md/01.Introduction/01/01.Edgeandcloud.md)  
  - [Guidance-ai と Phi の活用](./md/01.Introduction/01/01.Guidance.md)  
  - [GitHub Marketplace Models](https://github.com/marketplace/models)  
  - [Azure AI Model Catalog](https://ai.azure.com)

- さまざまな環境での Phi 推論  
  - [Hugging face](./md/01.Introduction/02/01.HF.md)  
  - [GitHub Models](./md/01.Introduction/02/02.GitHubModel.md)  
  - [Azure AI Foundry Model Catalog](./md/01.Introduction/02/03.AzureAIFoundry.md)  
  - [Ollama](./md/01.Introduction/02/04.Ollama.md)  
  - [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)  
  - [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)  
  - [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md)

- Phi ファミリーの推論  
  - [iOS での Phi 推論](./md/01.Introduction/03/iOS_Inference.md)  
  - [Android での Phi 推論](./md/01.Introduction/03/Android_Inference.md)  
  - [Jetson での Phi 推論](./md/01.Introduction/03/Jetson_Inference.md)  
  - [AI PC での Phi 推論](./md/01.Introduction/03/AIPC_Inference.md)  
  - [Apple MLX フレームワークでの Phi 推論](./md/01.Introduction/03/MLX_Inference.md)  
  - [ローカルサーバーでの Phi 推論](./md/01.Introduction/03/Local_Server_Inference.md)  
  - [AI Toolkit を使ったリモートサーバーでの Phi 推論](./md/01.Introduction/03/Remote_Interence.md)  
  - [Rust での Phi 推論](./md/01.Introduction/03/Rust_Inference.md)  
  - [ローカルでの Phi--Vision 推論](./md/01.Introduction/03/Vision_Inference.md)  
  - [Kaito AKS、Azure Containers（公式サポート）での Phi 推論](./md/01.Introduction/03/Kaito_Inference.md)

- Phi ファミリーの量子化  
  - [llama.cpp を使った Phi-3.5 / 4 の量子化](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)  
  - [onnxruntime の Generative AI 拡張を使った Phi-3.5 / 4 の量子化](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)  
  - [Intel OpenVINO を使った Phi-3.5 / 4 の量子化](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)  
  - [Apple MLX フレームワークを使った Phi-3.5 / 4 の量子化](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

- Phi の評価  
  - [Responsible AI](./md/01.Introduction/05/ResponsibleAI.md)  
  - [Azure AI Foundry を使った評価](./md/01.Introduction/05/AIFoundry.md)  
  - [Promptflow を使った評価](./md/01.Introduction/05/Promptflow.md)

- Azure AI Search を使った RAG  
  - [Phi-4-mini と Phi-4-multimodal(RAG) を Azure AI Search で使う方法](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Phi アプリケーション開発サンプル  
  - テキスト＆チャットアプリケーション  
    - Phi-4 サンプル 🆕  
      - [📓] [Phi-4-mini ONNX モデルでチャット](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)  
      - [Phi-4 ローカル ONNX モデルでチャット (.NET)](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)  
      - [Semantic Kernel を使った Phi-4 ONNX の .NET コンソールチャットアプリ](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)  
    - Phi-3 / 3.5 サンプル  
      - [ブラウザで動く Phi3、ONNX Runtime Web、WebGPU を使ったローカルチャットボット](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)  
      - [OpenVino チャット](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)  
      - [マルチモデル - Phi-3-mini と OpenAI Whisper のインタラクティブ連携](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)  
      - [MLFlow - Phi-3 を使ったラッパー作成と MLFlow 利用](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)  
      - [モデル最適化 - Olive を使った Phi-3-mini モデルの ONNX Runtime Web 向け最適化](https://github.com/microsoft/Olive/tree/main/examples/phi3)  
      - [WinUI3 アプリで Phi-3 mini-4k-instruct-onnx を使う](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)  
      - [WinUI3 マルチモデル AI パワードノートアプリサンプル](https://github.com/microsoft/ai-powered-notes-winui3-sample)
- [カスタムPhi-3モデルのファインチューニングとPrompt flowとの統合](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
- [Azure AI FoundryでのカスタムPhi-3モデルのファインチューニングとPrompt flowとの統合](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
- [Microsoftの責任あるAI原則に焦点を当てたAzure AI Foundryでのファインチューニング済みPhi-3 / Phi-3.5モデルの評価](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
- [📓] [Phi-3.5-mini-instruct 言語予測サンプル（中国語/英語）](../../md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
- [Phi-3.5-Instruct WebGPU RAGチャットボット](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
- [Windows GPUを使ったPhi-3.5-Instruct ONNXによるPrompt flowソリューションの作成](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
- [Microsoft Phi-3.5 tfliteを使ったAndroidアプリの作成](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
- [Microsoft.ML.OnnxRuntimeを使ったローカルONNX Phi-3モデルのQ&A .NETサンプル](../../md/04.HOL/dotnet/src/LabsPhi301)
- [Semantic KernelとPhi-3を使ったコンソールチャット.NETアプリ](../../md/04.HOL/dotnet/src/LabsPhi302)

- Azure AI Inference SDK コードベースサンプル
  - Phi-4 サンプル 🆕
    - [📓] [Phi-4-multimodalを使ったプロジェクトコード生成](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
  - Phi-3 / 3.5 サンプル
    - [Microsoft Phi-3ファミリーで独自のVisual Studio Code GitHub Copilot Chatを構築](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
    - [GitHubモデルを使ったPhi-3.5によるVisual Studio Codeチャットコパイロットエージェントの作成](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

- 高度な推論サンプル
  - Phi-4 サンプル 🆕
    - [📓] [Phi-4-mini-reasoning または Phi-4-reasoning サンプル](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
    - [📓] [Microsoft Oliveを使ったPhi-4-mini-reasoningのファインチューニング](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
    - [📓] [Apple MLXを使ったPhi-4-mini-reasoningのファインチューニング](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
    - [📓] [GitHubモデルを使ったPhi-4-mini-reasoning](../../md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
    - [📓] [Azure AI Foundryモデルを使ったPhi-4-mini-reasoning](../../md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
- デモ
    - [Hugging Face SpacesでホストされているPhi-4-miniデモ](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
    - [Hugging Face SpacesでホストされているPhi-4-multimodalデモ](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
- ビジョンサンプル
  - Phi-4 サンプル 🆕
    - [📓] [Phi-4-multimodalを使って画像を読み込みコードを生成](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md)
  - Phi-3 / 3.5 サンプル
    - [📓][Phi-3-vision-画像テキストからテキストへの変換](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
    - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
    - [📓][Phi-3-vision CLIP埋め込み](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
    - [デモ: Phi-3 Recycling](https://github.com/jennifermarsman/PhiRecycling/)
    - [Phi-3-vision - Phi3-VisionとOpenVINOを使ったビジュアル言語アシスタント](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
    - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
    - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
    - [📓][Phi-3.5 Vision マルチフレームまたはマルチイメージサンプル](../../md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
    - [Microsoft.ML.OnnxRuntime .NETを使ったPhi-3 VisionローカルONNXモデル](../../md/04.HOL/dotnet/src/LabsPhi303)
    - [メニュー形式のPhi-3 VisionローカルONNXモデル Microsoft.ML.OnnxRuntime .NET使用](../../md/04.HOL/dotnet/src/LabsPhi304)

- 数学サンプル
  - Phi-4-Mini-Flash-Reasoning-Instruct サンプル 🆕 [Phi-4-Mini-Flash-Reasoning-Instructによる数学デモ](../../md/02.Application/09.Math/MathDemo.ipynb)

- オーディオサンプル
  - Phi-4 サンプル 🆕
    - [📓] [Phi-4-multimodalを使った音声文字起こしの抽出](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
    - [📓] [Phi-4-multimodalオーディオサンプル](../../md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
    - [📓] [Phi-4-multimodal音声翻訳サンプル](../../md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
    - [Phi-4-multimodalを使った音声ファイル解析と文字起こし生成の.NETコンソールアプリケーション](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

- MOEサンプル
  - Phi-3 / 3.5 サンプル
    - [📓] [Phi-3.5 Mixture of Experts Models (MoEs) ソーシャルメディアサンプル](../../md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
    - [📓] [NVIDIA NIM Phi-3 MOE、Azure AI Search、LlamaIndexを使ったRetrieval-Augmented Generation (RAG)パイプライン構築](../../md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)

- 関数呼び出しサンプル
  - Phi-4 サンプル 🆕
    - [📓] [Phi-4-miniでの関数呼び出しの使用](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
    - [📓] [Phi-4-miniでの関数呼び出しを使ったマルチエージェント作成](../../md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
    - [📓] [Ollamaでの関数呼び出しの使用](../../md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
    - [📓] [ONNXでの関数呼び出しの使用](../../md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)

- マルチモーダルミキシングサンプル
  - Phi-4 サンプル 🆕
    - [📓] [Phi-4-multimodalをテクノロジージャーナリストとして使う](../../md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
    - [Phi-4-multimodalを使った画像解析の.NETコンソールアプリケーション](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Phiファインチューニング
  - [ファインチューニングシナリオ](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [ファインチューニングとRAGの比較](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [Phi-3を業界の専門家に育てるファインチューニング](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [VS Code用AIツールキットでのPhi-3ファインチューニング](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Azure Machine Learning ServiceでのPhi-3ファインチューニング](./md/03.FineTuning/Introduce_AzureML.md)
  - [Loraを使ったPhi-3ファインチューニング](./md/03.FineTuning/FineTuning_Lora.md)
  - [QLoraを使ったPhi-3ファインチューニング](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Azure AI FoundryでのPhi-3ファインチューニング](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Azure ML CLI/SDKでのPhi-3ファインチューニング](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Microsoft Oliveを使ったファインチューニング](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Microsoft Oliveハンズオンラボでのファインチューニング](./md/03.FineTuning/olive-lab/readme.md)
  - [Weights and Biasを使ったPhi-3-visionのファインチューニング](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [Apple MLXフレームワークを使ったPhi-3ファインチューニング](./md/03.FineTuning/FineTuning_MLX.md)
  - [Phi-3-visionのファインチューニング（公式サポート）](./md/03.FineTuning/FineTuning_Vision.md)
  - [Kaito AKS、Azure Containersを使ったPhi-3ファインチューニング（公式サポート）](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Phi-3および3.5 Visionのファインチューニング](https://github.com/2U1/Phi3-Vision-Finetune)

- ハンズオンラボ
  - [最先端モデルの探求：LLM、SLM、ローカル開発など](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [NLPの可能性を引き出す：Microsoft Oliveによるファインチューニング](https://github.com/azure/Ignite_FineTuning_workshop)

- 学術研究論文および出版物
  - [Textbooks Are All You Need II: phi-1.5 技術報告](https://arxiv.org/abs/2309.05463)
  - [Phi-3 技術報告：スマホ上で動作する高性能言語モデル](https://arxiv.org/abs/2404.14219)
  - [Phi-4 技術報告](https://arxiv.org/abs/2412.08905)
  - [Phi-4-Mini 技術報告：Mixture-of-LoRAsによるコンパクトで強力なマルチモーダル言語モデル](https://arxiv.org/abs/2503.01743)
  - [車載向け関数呼び出しに最適化された小型言語モデル](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) PHI-3の多肢選択式質問応答向けファインチューニング：方法論、結果、課題](https://arxiv.org/abs/2501.01588)
- [Phi-4-reasoning 技術レポート](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
- [Phi-4-mini-reasoning 技術レポート](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Phiモデルの利用方法

### Azure AI FoundryでのPhi

Microsoft Phiの使い方や、さまざまなハードウェアデバイスでのエンドツーエンドソリューションの構築方法を学べます。Phiを実際に体験するには、モデルを操作し、ご自身のシナリオに合わせてPhiをカスタマイズしてみてください。詳しくは[Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai)をご覧ください。[Azure AI Foundryのはじめ方](/md/02.QuickStart/AzureAIFoundry_QuickStart.md)も参考にしてください。

**Playground**  
各モデルには専用のプレイグラウンドがあり、モデルのテストが可能です。[Azure AI Playground](https://aka.ms/try-phi3)をご利用ください。

### GitHubモデルでのPhi

Microsoft Phiの使い方や、さまざまなハードウェアデバイスでのエンドツーエンドソリューションの構築方法を学べます。Phiを実際に体験するには、モデルを操作し、ご自身のシナリオに合わせてPhiをカスタマイズしてみてください。詳しくは[GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo)をご覧ください。[GitHub Model Catalogのはじめ方](/md/02.QuickStart/GitHubModel_QuickStart.md)も参考にしてください。

**Playground**  
各モデルには専用の[プレイグラウンドがあり、モデルのテストが可能です](/md/02.QuickStart/GitHubModel_QuickStart.md)。

### Hugging FaceでのPhi

モデルは[Hugging Face](https://huggingface.co/microsoft)でも見つけることができます。

**Playground**  
[Hugging Chat playground](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## Responsible AI（責任あるAI）

Microsoftは、お客様が当社のAI製品を責任を持って利用できるよう支援し、学びを共有し、Transparency NotesやImpact Assessmentsなどのツールを通じて信頼に基づくパートナーシップを築くことに取り組んでいます。これらのリソースの多くは[https://aka.ms/RAI](https://aka.ms/RAI)でご覧いただけます。  
Microsoftの責任あるAIへのアプローチは、公平性、信頼性と安全性、プライバシーとセキュリティ、包括性、透明性、説明責任というAI原則に基づいています。

このサンプルで使用されているような大規模な自然言語、画像、音声モデルは、不公平、不信頼、攻撃的な振る舞いをする可能性があり、その結果として害を及ぼすことがあります。リスクや制限については、[Azure OpenAIサービスのTransparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text)をご参照ください。

これらのリスクを軽減する推奨される方法は、有害な行動を検出し防止できる安全システムをアーキテクチャに組み込むことです。[Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview)は、アプリケーションやサービス内のユーザー生成コンテンツやAI生成コンテンツの有害な内容を検出できる独立した保護レイヤーを提供します。Azure AI Content Safetyには、有害なテキストや画像を検出するAPIが含まれています。Azure AI Foundry内のContent Safetyサービスでは、異なるモダリティにわたる有害コンテンツの検出用サンプルコードを閲覧、試用できます。以下の[クイックスタートドキュメント](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest)では、サービスへのリクエスト方法を案内しています。

もう一つ考慮すべき点は、アプリケーション全体のパフォーマンスです。マルチモーダルかつマルチモデルのアプリケーションでは、パフォーマンスとは、システムがユーザーの期待通りに動作し、有害な出力を生成しないことを意味します。全体のアプリケーションパフォーマンスは、[Performance and Quality and Risk and Safety evaluators](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in)を使って評価することが重要です。また、[カスタム評価器](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators)を作成して評価することも可能です。

開発環境でAIアプリケーションを評価するには、[Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html)を利用できます。テストデータセットやターゲットを用いて、生成AIアプリケーションの出力を組み込み評価器やカスタム評価器で定量的に測定します。Azure AI Evaluation SDKの使い方は、[クイックスタートガイド](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk)をご覧ください。評価実行後は、[Azure AI Foundryで結果を可視化](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results)できます。

## 商標について

このプロジェクトには、プロジェクト、製品、サービスの商標やロゴが含まれている場合があります。Microsoftの商標やロゴの使用は、[Microsoftの商標およびブランドガイドライン](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general)に従う必要があります。  
Microsoftの商標やロゴを改変したバージョンで使用する場合、混乱を招いたりMicrosoftの後援を示唆したりしてはなりません。第三者の商標やロゴの使用は、それぞれの第三者のポリシーに従います。

**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されました。正確性の向上に努めておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語によるオリジナル文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や誤訳についても、当方は責任を負いかねます。