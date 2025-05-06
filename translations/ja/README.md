<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "469e2c58e8d576f8bfdf9e4ca2218897",
  "translation_date": "2025-05-06T11:08:03+00:00",
  "source_file": "README.md",
  "language_code": "ja"
}
-->
# Phi Cookbook: MicrosoftのPhiモデルを使った実践例

[![GitHub Codespacesでサンプルを開いて使う](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)  
[![Dev Containersで開く](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHubのコントリビューター](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)  
[![GitHubのイシュー](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)  
[![GitHubのプルリクエスト](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)  
[![PR歓迎](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHubのウォッチャー](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)  
[![GitHubのフォーク](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)  
[![GitHubのスター](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Azure AI Community Discord](https://dcbadge.vercel.app/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

PhiはMicrosoftが開発したオープンソースのAIモデルシリーズです。

Phiは現在、最も強力かつコスト効率の高い小型言語モデル（SLM）であり、多言語対応、推論、テキスト／チャット生成、コーディング、画像、音声など様々なシナリオで優れたベンチマークを誇ります。

Phiはクラウドやエッジデバイスに展開でき、限られた計算リソースでも簡単に生成AIアプリケーションを構築できます。

これらのリソースを使い始めるには、以下の手順に従ってください：  
1. **リポジトリをフォークする**: クリック [![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)  
2. **リポジトリをクローンする**: `git clone https://github.com/microsoft/PhiCookBook.git`  
3. [**Microsoft AI Discordコミュニティに参加して、専門家や他の開発者と交流する**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/cover.2595d43b382944c601aebf88583314636768eece3d94e8e4448e03a4e5bedef4.ja.png)

## 🌐 多言語対応

### GitHub Actionで対応（自動化＆常に最新）

[フランス語](../fr/README.md) | [スペイン語](../es/README.md) | [ドイツ語](../de/README.md) | [ロシア語](../ru/README.md) | [アラビア語](../ar/README.md) | [ペルシア語（ファルシ）](../fa/README.md) | [ウルドゥー語](../ur/README.md) | [中国語（簡体字）](../zh/README.md) | [中国語（繁体字、マカオ）](../mo/README.md) | [中国語（繁体字、香港）](../hk/README.md) | [中国語（繁体字、台湾）](../tw/README.md) | [日本語](./README.md) | [韓国語](../ko/README.md) | [ヒンディー語](../hi/README.md)

### CLIで対応予定 - 現在進行中
[Bengali](../bn/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Portuguese (Brazil)](../br/README.md) | [Italian](../it/README.md) | [Polish](../pl/README.md) | [Turkish](../tr/README.md) | [Greek](../el/README.md) | [Thai](../th/README.md) | [Swedish](../sv/README.md) | [Danish](../da/README.md) | [Norwegian](../no/README.md) | [Finnish](../fi/README.md) | [Dutch](../nl/README.md) | [Hebrew](../he/README.md) | [Vietnamese](../vi/README.md) | [Indonesian](../id/README.md) | [Malay](../ms/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Swahili](../sw/README.md) | [Hungarian](../hu/README.md) | [Czech](../cs/README.md) | [Slovak](../sk/README.md) | [Romanian](../ro/README.md) | [Bulgarian](../bg/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Croatian](../hr/README.md) | [Slovenian](../sl/README.md)


## 目次

- はじめに
- [Phiファミリーへようこそ](./md/01.Introduction/01/01.PhiFamily.md)
  - [環境のセットアップ](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [主要技術の理解](./md/01.Introduction/01/01.Understandingtech.md)
  - [PhiモデルのAIセーフティ](./md/01.Introduction/01/01.AISafety.md)
  - [Phiハードウェアサポート](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Phiモデルとプラットフォーム間の利用可能性](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Guidance-aiとPhiの活用](./md/01.Introduction/01/01.Guidance.md)
  - [GitHubマーケットプレイスモデル](https://github.com/marketplace/models)
  - [Azure AIモデルカタログ](https://ai.azure.com)

- さまざまな環境でのPhi推論
    -  [Hugging face](./md/01.Introduction/02/01.HF.md)
    -  [GitHubモデル](./md/01.Introduction/02/02.GitHubModel.md)
    -  [Azure AI Foundryモデルカタログ](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)

- Phiファミリーでの推論
    - [iOSでのPhi推論](./md/01.Introduction/03/iOS_Inference.md)
    - [AndroidでのPhi推論](./md/01.Introduction/03/Android_Inference.md)
    - [JetsonでのPhi推論](./md/01.Introduction/03/Jetson_Inference.md)
    - [AI PCでのPhi推論](./md/01.Introduction/03/AIPC_Inference.md)
    - [Apple MLXフレームワークでのPhi推論](./md/01.Introduction/03/MLX_Inference.md)
    - [ローカルサーバーでのPhi推論](./md/01.Introduction/03/Local_Server_Inference.md)
    - [AI Toolkitを使ったリモートサーバーでのPhi推論](./md/01.Introduction/03/Remote_Interence.md)
    - [RustでのPhi推論](./md/01.Introduction/03/Rust_Inference.md)
    - [ローカルでのPhi--Vision推論](./md/01.Introduction/03/Vision_Inference.md)
    - [Kaito AKS、Azureコンテナ（公式サポート）でのPhi推論](./md/01.Introduction/03/Kaito_Inference.md)
-  [Phiファミリーの量子化](./md/01.Introduction/04/QuantifyingPhi.md)
    - [llama.cppを使ったPhi-3.5 / 4の量子化](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [onnxruntime用のGenerative AI拡張機能を使ったPhi-3.5 / 4の量子化](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Intel OpenVINOを使ったPhi-3.5 / 4の量子化](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Apple MLXフレームワークを使ったPhi-3.5 / 4の量子化](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

- Phiの評価
- [Response AI](./md/01.Introduction/05/ResponsibleAI.md)
    - [Azure AI Foundry for Evaluation](./md/01.Introduction/05/AIFoundry.md)
    - [Using Promptflow for Evaluation](./md/01.Introduction/05/Promptflow.md)
 
- Azure AI Searchを使ったRAG
    - [Phi-4-miniとPhi-4-multimodal(RAG)をAzure AI Searchで使う方法](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Phiアプリケーション開発サンプル
  - テキスト＆チャットアプリケーション
    - Phi-4サンプル 🆕
      - [📓] [Phi-4-mini ONNXモデルでチャット](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Phi-4ローカルONNXモデルでチャット .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Semantic Kernelを使ったPhi-4 ONNXの.NETコンソールチャットアプリ](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Phi-3 / 3.5サンプル
      - [Phi3、ONNX Runtime Web、WebGPUを使ったブラウザ内ローカルチャットボット](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVinoチャット](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [マルチモデル - Phi-3-miniとOpenAI Whisperのインタラクティブ](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - ラッパー作成とPhi-3のMLFlow利用](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [モデル最適化 - Oliveを使ったPhi-3-miniモデルのONNX Runtime Web最適化方法](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [Phi-3 mini-4k-instruct-onnxを使ったWinUI3アプリ](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      - [WinUI3マルチモデルAI搭載ノートアプリサンプル](https://github.com/microsoft/ai-powered-notes-winui3-sample)
      - [カスタムPhi-3モデルのファインチューニングとPrompt flow統合](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
      - [Azure AI FoundryでのカスタムPhi-3モデルのファインチューニングとPrompt flow統合](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
      - [MicrosoftのResponsible AI原則に注目したAzure AI Foundryでのファインチューニング済みPhi-3 / Phi-3.5モデル評価](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
      - [📓] [Phi-3.5-mini-instruct言語予測サンプル（中国語/英語）](../../md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
      - [Phi-3.5-Instruct WebGPU RAGチャットボット](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
      - [Windows GPUを使ったPhi-3.5-Instruct ONNXのPrompt flowソリューション作成](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
      - [Microsoft Phi-3.5 tfliteを使ったAndroidアプリ作成](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
      - [Microsoft.ML.OnnxRuntimeを使ったローカルONNX Phi-3モデルのQ&A .NET例](../../md/04.HOL/dotnet/src/LabsPhi301)
      - [Semantic KernelとPhi-3を使ったコンソールチャット.NETアプリ](../../md/04.HOL/dotnet/src/LabsPhi302)

  - Azure AI Inference SDKコードベースサンプル 
    - Phi-4サンプル 🆕
      - [📓] [Phi-4-multimodalを使ったプロジェクトコード生成](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
    - Phi-3 / 3.5サンプル
      - [Microsoft Phi-3ファミリーを使ったVisual Studio Code GitHub Copilotチャットの作成](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
      - [GitHubモデルを使ったPhi-3.5によるVisual Studio Codeチャットコパイロットエージェントの作成](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

  - 高度な推論サンプル
    - Phi-4サンプル 🆕
      - [📓] [Phi-4-mini-reasoningまたはPhi-4-reasoningサンプル](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
      - [📓] [Microsoft Oliveを使ったPhi-4-mini-reasoningのファインチューニング](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Apple MLXを使ったPhi-4-mini-reasoningのファインチューニング](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [GitHubモデルを使ったPhi-4-mini-reasoning](../../md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
- [📓] [Azure AI Foundry Modelsを使ったPhi-4-miniの推論](../../md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
  - デモ
      - [Hugging Face SpacesでホストされているPhi-4-miniデモ](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
      - [Hugging Face SpacesでホストされているPhi-4-multimodalデモ](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
  - ビジョンサンプル
    - Phi-4サンプル 🆕
      - [📓] [Phi-4-multimodalを使って画像を読み取りコードを生成する](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
    - Phi-3 / 3.5サンプル
      -  [📓][Phi-3-vision-画像テキストからテキストへ](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
      - [📓][Phi-3-vision CLIP埋め込み](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [DEMO: Phi-3 Recycling](https://github.com/jennifermarsman/PhiRecycling/)
      - [Phi-3-vision - Phi3-VisionとOpenVINOによるビジュアル言語アシスタント](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
      - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
      - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
      - [📓][Phi-3.5 Vision マルチフレームまたはマルチ画像サンプル](../../md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
      - [Microsoft.ML.OnnxRuntime .NETを使ったPhi-3 VisionローカルONNXモデル](../../md/04.HOL/dotnet/src/LabsPhi303)
      - [メニュー形式のPhi-3 VisionローカルONNXモデル（Microsoft.ML.OnnxRuntime .NET使用）](../../md/04.HOL/dotnet/src/LabsPhi304)

  - オーディオサンプル
    - Phi-4サンプル 🆕
      - [📓] [Phi-4-multimodalを使った音声文字起こし](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
      - [📓] [Phi-4-multimodalオーディオサンプル](../../md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
      - [📓] [Phi-4-multimodal音声翻訳サンプル](../../md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
      - [.NETコンソールアプリケーションでPhi-4-multimodalを使い、音声ファイルを解析して文字起こしを生成](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

  - MOEサンプル
    - Phi-3 / 3.5サンプル
      - [📓] [Phi-3.5 Mixture of Experts Models (MoEs) ソーシャルメディアサンプル](../../md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
      - [📓] [NVIDIA NIM Phi-3 MOE、Azure AI Search、LlamaIndexを使ったRetrieval-Augmented Generation (RAG)パイプラインの構築](../../md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)
  - 関数呼び出しサンプル
    - Phi-4サンプル 🆕
      -  [📓] [Phi-4-miniでのFunction Callingの使い方](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
      -  [📓] [Function Callingを使ってPhi-4-miniでマルチエージェントを作成する](../../md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
      -  [📓] [OllamaでFunction Callingを使う](../../md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
  - マルチモーダルミキシングサンプル
    - Phi-4サンプル 🆕
      -  [📓] [Phi-4-multimodalをテクノロジージャーナリストとして使う](../../md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
      - [.NETコンソールアプリケーションでPhi-4-multimodalを使い画像を解析](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Phiファインチューニングサンプル
  - [ファインチューニングシナリオ](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [ファインチューニングとRAGの違い](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [Phi-3を業界の専門家に育てるファインチューニング](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [VS Code用AI Toolkitを使ったPhi-3のファインチューニング](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Azure Machine Learning Serviceを使ったPhi-3のファインチューニング](./md/03.FineTuning/Introduce_AzureML.md)
- [LoraによるPhi-3のファインチューニング](./md/03.FineTuning/FineTuning_Lora.md)
  - [QLoraによるPhi-3のファインチューニング](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Azure AI FoundryによるPhi-3のファインチューニング](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Azure ML CLI/SDKによるPhi-3のファインチューニング](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Microsoft Oliveによるファインチューニング](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Microsoft Oliveハンズオンラボによるファインチューニング](./md/03.FineTuning/olive-lab/readme.md)
  - [Weights and Biasを使ったPhi-3-visionのファインチューニング](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [Apple MLX FrameworkによるPhi-3のファインチューニング](./md/03.FineTuning/FineTuning_MLX.md)
  - [Phi-3-visionのファインチューニング（公式サポート）](./md/03.FineTuning/FineTuning_Vision.md)
  - [Kaito AKS、Azure Containersを使ったPhi-3のファインチューニング（公式サポート）](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Phi-3および3.5 Visionのファインチューニング](https://github.com/2U1/Phi3-Vision-Finetune)

- ハンズオンラボ
  - [最先端モデルの探求：LLM、SLM、ローカル開発など](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [NLPの可能性を引き出す：Microsoft Oliveによるファインチューニング](https://github.com/azure/Ignite_FineTuning_workshop)

- 学術研究論文および出版物
  - [Textbooks Are All You Need II: phi-1.5 技術報告](https://arxiv.org/abs/2309.05463)
  - [Phi-3 技術報告：あなたの携帯電話で動作する高性能言語モデル](https://arxiv.org/abs/2404.14219)
  - [Phi-4 技術報告](https://arxiv.org/abs/2412.08905)
  - [Phi-4-Mini 技術報告：LoRAの混合によるコンパクトで強力なマルチモーダル言語モデル](https://arxiv.org/abs/2503.01743)
  - [車載機能呼び出し向け小型言語モデルの最適化](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) 複数選択問題回答のためのPHI-3ファインチューニング：方法論、結果、課題](https://arxiv.org/abs/2501.01588)
  - [Phi-4-推論技術報告](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Phi-4-mini-推論技術報告](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Phiモデルの利用方法

### Azure AI FoundryでのPhi

Microsoft Phiの使い方や、さまざまなハードウェアデバイスでのE2Eソリューション構築方法を学べます。Phiを実際に体験するには、モデルを試し、自分のシナリオに合わせてPhiをカスタマイズしてみてください。詳細は[Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai)で確認できます。[Azure AI Foundryのはじめ方](/md/02.QuickStart/AzureAIFoundry_QuickStart.md)もご覧ください。

**Playground**  
各モデルには専用のプレイグラウンドがあり、モデルを試せます。[Azure AI Playground](https://aka.ms/try-phi3)をご利用ください。

### GitHub ModelsでのPhi

Microsoft Phiの使い方や、さまざまなハードウェアデバイスでのE2Eソリューション構築方法を学べます。Phiを実際に体験するには、モデルを試し、自分のシナリオに合わせてPhiをカスタマイズしてみてください。[GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo)で詳細を確認できます。[GitHub Model Catalogのはじめ方](/md/02.QuickStart/GitHubModel_QuickStart.md)もご覧ください。

**Playground**  
各モデルには専用の[プレイグラウンド](/md/02.QuickStart/GitHubModel_QuickStart.md)が用意されています。

### Hugging FaceでのPhi

モデルは[Hugging Face](https://huggingface.co/microsoft)でも見つけることができます。

**Playground**  
[Hugging Chat playground](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## Responsible AI

Microsoftは、お客様が当社のAI製品を責任を持って利用できるよう支援し、学びを共有し、Transparency NotesやImpact Assessmentsなどのツールを通じて信頼に基づくパートナーシップを築くことにコミットしています。これらのリソースは多くが[https://aka.ms/RAI](https://aka.ms/RAI)で提供されています。  
Microsoftの責任あるAIへの取り組みは、公平性、信頼性と安全性、プライバシーとセキュリティ、包摂性、透明性、説明責任というAI原則に基づいています。
大規模な自然言語、画像、音声モデル（このサンプルで使用されているもののような）は、不公平、不確実、または攻撃的な振る舞いをする可能性があり、その結果として害を引き起こすことがあります。リスクや制限については、[Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text)をご確認ください。

これらのリスクを軽減する推奨される方法は、有害な振る舞いを検出し防止できる安全システムをアーキテクチャに組み込むことです。[Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview)は独立した保護層を提供し、アプリケーションやサービス内のユーザー生成およびAI生成の有害なコンテンツを検出できます。Azure AI Content Safetyには、有害な素材を検出できるテキストおよび画像APIが含まれています。Azure AI Foundry内のContent Safetyサービスでは、異なるモダリティの有害コンテンツ検出用のサンプルコードを表示、探索、試すことができます。以下の[クイックスタートドキュメント](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest)では、サービスへのリクエスト方法を案内しています。

もう一つ考慮すべき点は、全体的なアプリケーションのパフォーマンスです。マルチモーダルかつマルチモデルのアプリケーションでは、パフォーマンスとは、システムがあなたやユーザーの期待通りに動作し、有害な出力を生成しないことを意味します。全体のアプリケーションパフォーマンスを評価するには、[Performance and Quality and Risk and Safety evaluators](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in)を使用することが重要です。また、[カスタム評価器](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators)を作成・評価することも可能です。

[Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html)を使えば、開発環境でAIアプリケーションを評価できます。テストデータセットまたはターゲットを用いて、生成AIアプリケーションの生成物を組み込み評価器や任意のカスタム評価器で定量的に測定します。azure ai evaluation sdkを使ったシステム評価の開始には、[クイックスタートガイド](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk)をご参照ください。評価を実行した後は、[Azure AI Foundryで結果を可視化](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results)できます。

## 商標

このプロジェクトには、プロジェクト、製品、またはサービスの商標やロゴが含まれている場合があります。Microsoftの商標またはロゴの正当な使用は、[Microsoftの商標およびブランドガイドライン](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general)に従う必要があります。  
このプロジェクトの修正版でMicrosoftの商標やロゴを使用する場合、混乱を招いたりMicrosoftの後援を示唆したりしてはなりません。  
第三者の商標やロゴの使用は、該当する第三者のポリシーに従います。

**免責事項**:  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されています。正確性を期しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語で記載された文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じた誤解や解釈の相違について、当方は一切の責任を負いかねます。