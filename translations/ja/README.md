<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "698f7f3d48ebc9e25a273d7c8b7e31c5",
  "translation_date": "2025-09-12T13:27:19+00:00",
  "source_file": "README.md",
  "language_code": "ja"
}
-->
# Phi Cookbook: マイクロソフトのPhiモデルを使った実践例

Phiは、マイクロソフトが開発したオープンソースのAIモデルシリーズです。

Phiは現在、最も強力でコスト効率の高い小型言語モデル（SLM）であり、多言語対応、推論、テキスト/チャット生成、コーディング、画像、音声などのシナリオで非常に優れたベンチマークを持っています。

Phiはクラウドやエッジデバイスに展開可能で、限られた計算能力で生成型AIアプリケーションを簡単に構築することができます。

以下の手順に従って、これらのリソースを使用してみましょう：
1. **リポジトリをフォークする**: [![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo) をクリック
2. **リポジトリをクローンする**: `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Microsoft AI Discordコミュニティに参加して、専門家や他の開発者と交流する**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../imgs/cover.png)

### 🌐 多言語対応

#### GitHub Actionによるサポート（自動化＆常に最新）

[フランス語](../fr/README.md) | [スペイン語](../es/README.md) | [ドイツ語](../de/README.md) | [ロシア語](../ru/README.md) | [アラビア語](../ar/README.md) | [ペルシャ語 (ファルシ)](../fa/README.md) | [ウルドゥー語](../ur/README.md) | [中国語 (簡体字)](../zh/README.md) | [中国語 (繁体字, マカオ)](../mo/README.md) | [中国語 (繁体字, 香港)](../hk/README.md) | [中国語 (繁体字, 台湾)](../tw/README.md) | [日本語](./README.md) | [韓国語](../ko/README.md) | [ヒンディー語](../hi/README.md) 
[ベンガル語](../bn/README.md) | [マラーティー語](../mr/README.md) | [ネパール語](../ne/README.md) | [パンジャブ語 (グルムキー)](../pa/README.md) | [ポルトガル語 (ポルトガル)](../pt/README.md) | [ポルトガル語 (ブラジル)](../br/README.md) | [イタリア語](../it/README.md) | [ポーランド語](../pl/README.md) | [トルコ語](../tr/README.md) | [ギリシャ語](../el/README.md) | [タイ語](../th/README.md) | [スウェーデン語](../sv/README.md) | [デンマーク語](../da/README.md) | [ノルウェー語](../no/README.md) | [フィンランド語](../fi/README.md) | [オランダ語](../nl/README.md) | [ヘブライ語](../he/README.md) | [ベトナム語](../vi/README.md) | [インドネシア語](../id/README.md) | [マレー語](../ms/README.md) | [タガログ語 (フィリピン)](../tl/README.md) | [スワヒリ語](../sw/README.md) | [ハンガリー語](../hu/README.md) | [チェコ語](../cs/README.md) | [スロバキア語](../sk/README.md) | [ルーマニア語](../ro/README.md) | [ブルガリア語](../bg/README.md) | [セルビア語 (キリル文字)](../sr/README.md) | [クロアチア語](../hr/README.md) | [スロベニア語](../sl/README.md)

## 目次

- はじめに
  - [Phiファミリーへようこそ](./md/01.Introduction/01/01.PhiFamily.md)
  - [環境のセットアップ](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [主要技術の理解](./md/01.Introduction/01/01.Understandingtech.md)
  - [PhiモデルのAI安全性](./md/01.Introduction/01/01.AISafety.md)
  - [Phiのハードウェアサポート](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Phiモデルとプラットフォームでの利用可能性](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Guidance-aiとPhiの使用](./md/01.Introduction/01/01.Guidance.md)
  - [GitHubマーケットプレイスモデル](https://github.com/marketplace/models)
  - [Azure AIモデルカタログ](https://ai.azure.com)

- 異なる環境でのPhiの推論
    - [Hugging face](./md/01.Introduction/02/01.HF.md)
    - [GitHubモデル](./md/01.Introduction/02/02.GitHubModel.md)
    - [Azure AI Foundryモデルカタログ](./md/01.Introduction/02/03.AzureAIFoundry.md)
    - [Ollama](./md/01.Introduction/02/04.Ollama.md)
    - [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    - [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    - [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md)

- Phiファミリーの推論
    - [iOSでのPhiの推論](./md/01.Introduction/03/iOS_Inference.md)
    - [AndroidでのPhiの推論](./md/01.Introduction/03/Android_Inference.md)
    - [JetsonでのPhiの推論](./md/01.Introduction/03/Jetson_Inference.md)
    - [AI PCでのPhiの推論](./md/01.Introduction/03/AIPC_Inference.md)
    - [Apple MLX FrameworkでのPhiの推論](./md/01.Introduction/03/MLX_Inference.md)
    - [ローカルサーバーでのPhiの推論](./md/01.Introduction/03/Local_Server_Inference.md)
    - [AI Toolkitを使用したリモートサーバーでのPhiの推論](./md/01.Introduction/03/Remote_Interence.md)
    - [RustでのPhiの推論](./md/01.Introduction/03/Rust_Inference.md)
    - [ローカルでのPhi--Visionの推論](./md/01.Introduction/03/Vision_Inference.md)
    - [Kaito AKS、Azure Containers（公式サポート）でのPhiの推論](./md/01.Introduction/03/Kaito_Inference.md)

- [Phiファミリーの量子化](./md/01.Introduction/04/QuantifyingPhi.md)
    - [llama.cppを使用したPhi-3.5 / 4の量子化](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [onnxruntimeの生成型AI拡張を使用したPhi-3.5 / 4の量子化](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Intel OpenVINOを使用したPhi-3.5 / 4の量子化](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Apple MLX Frameworkを使用したPhi-3.5 / 4の量子化](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

- Phiの評価
    - [責任あるAI](./md/01.Introduction/05/ResponsibleAI.md)
    - [評価のためのAzure AI Foundry](./md/01.Introduction/05/AIFoundry.md)
    - [Promptflowを使用した評価](./md/01.Introduction/05/Promptflow.md)

- Azure AI Searchを使用したRAG
    - [Phi-4-miniとPhi-4-multimodal(RAG)をAzure AI Searchで使用する方法](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Phiアプリケーション開発サンプル
  - テキスト＆チャットアプリケーション
    - Phi-4 サンプル 🆕
      - [📓] [Phi-4-mini ONNXモデルとのチャット](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Phi-4ローカルONNXモデル.NETとのチャット](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Sementic Kernelを使用したPhi-4 ONNXとの.NETコンソールアプリチャット](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Phi-3 / 3.5 サンプル
      - [ブラウザ内でPhi3、ONNX Runtime Web、WebGPUを使用したローカルチャットボット](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVinoチャット](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [インタラクティブPhi-3-miniとOpenAI Whisperのマルチモデル](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - ラッパーを構築し、Phi-3をMLFlowで使用](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [モデル最適化 - Oliveを使用してPhi-3-minモデルをONNX Runtime Web向けに最適化する方法](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [Phi-3 mini-4k-instruct-onnxを使用したWinUI3アプリ](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      - [WinUI3マルチモデルAI対応ノートアプリサンプル](https://github.com/microsoft/ai-powered-notes-winui3-sample)
- [カスタムPhi-3モデルをPrompt flowで微調整し統合する](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
- [Azure AI FoundryでカスタムPhi-3モデルをPrompt flowで微調整し統合する](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
- [Microsoftの責任あるAI原則に焦点を当てたAzure AI Foundryでの微調整済みPhi-3 / Phi-3.5モデルの評価](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
- [📓] [Phi-3.5-mini-instruct 言語予測サンプル (中国語/英語)](../../md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
- [Phi-3.5-Instruct WebGPU RAG チャットボット](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
- [Windows GPUを使用してPhi-3.5-Instruct ONNXでPrompt flowソリューションを作成する](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
- [Microsoft Phi-3.5 tfliteを使用してAndroidアプリを作成する](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
- [Microsoft.ML.OnnxRuntimeを使用したローカルONNX Phi-3モデルによるQ&A .NETサンプル](../../md/04.HOL/dotnet/src/LabsPhi301)
- [Semantic KernelとPhi-3を使用したコンソールチャット.NETアプリ](../../md/04.HOL/dotnet/src/LabsPhi302)

- Azure AI推論SDKコードベースサンプル
  - Phi-4 サンプル 🆕
    - [📓] [Phi-4-multimodalを使用してプロジェクトコードを生成する](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
  - Phi-3 / 3.5 サンプル
    - [Microsoft Phi-3ファミリーを使用してVisual Studio Code GitHub Copilot Chatを構築する](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
    - [GitHubモデルを使用してPhi-3.5でVisual Studio Code Chat Copilot Agentを作成する](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

- 高度な推論サンプル
  - Phi-4 サンプル 🆕
    - [📓] [Phi-4-mini-reasoningまたはPhi-4-reasoningサンプル](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
    - [📓] [Microsoft Oliveを使用したPhi-4-mini-reasoningの微調整](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
    - [📓] [Apple MLXを使用したPhi-4-mini-reasoningの微調整](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
    - [📓] [GitHubモデルを使用したPhi-4-mini-reasoning](../../md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
    - [📓] [Azure AI Foundryモデルを使用したPhi-4-mini-reasoning](../../md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
- デモ
    - [Hugging Face SpacesでホストされているPhi-4-miniデモ](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
    - [Hugging Face SpacesでホストされているPhi-4-multimodalデモ](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
- ビジョンサンプル
  - Phi-4 サンプル 🆕
    - [📓] [Phi-4-multimodalを使用して画像を読み取りコードを生成する](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
  - Phi-3 / 3.5 サンプル
    - [📓][Phi-3-vision-画像テキストからテキストへ](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
    - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
    - [📓][Phi-3-vision CLIP埋め込み](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
    - [DEMO: Phi-3リサイクル](https://github.com/jennifermarsman/PhiRecycling/)
    - [Phi-3-vision - 視覚言語アシスタント - Phi3-VisionとOpenVINOを使用](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
    - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
    - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
    - [📓][Phi-3.5 Vision マルチフレームまたはマルチ画像サンプル](../../md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
    - [Microsoft.ML.OnnxRuntime .NETを使用したローカルONNXモデルによるPhi-3 Vision](../../md/04.HOL/dotnet/src/LabsPhi303)
    - [Microsoft.ML.OnnxRuntime .NETを使用したメニュー形式のローカルONNXモデルによるPhi-3 Vision](../../md/04.HOL/dotnet/src/LabsPhi304)

- 数学サンプル
  - Phi-4-Mini-Flash-Reasoning-Instruct サンプル 🆕 [Phi-4-Mini-Flash-Reasoning-Instructを使用した数学デモ](../../md/02.Application/09.Math/MathDemo.ipynb)

- オーディオサンプル
  - Phi-4 サンプル 🆕
    - [📓] [Phi-4-multimodalを使用した音声トランスクリプトの抽出](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
    - [📓] [Phi-4-multimodalオーディオサンプル](../../md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
    - [📓] [Phi-4-multimodal音声翻訳サンプル](../../md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
    - [.NETコンソールアプリケーションを使用してPhi-4-multimodalオーディオで音声ファイルを分析しトランスクリプトを生成する](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

- MOEサンプル
  - Phi-3 / 3.5 サンプル
    - [📓] [Phi-3.5 Mixture of Experts Models (MoEs) ソーシャルメディアサンプル](../../md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
    - [📓] [NVIDIA NIM Phi-3 MOE、Azure AI Search、LlamaIndexを使用した検索強化生成 (RAG) パイプラインの構築](../../md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)

- 関数呼び出しサンプル
  - Phi-4 サンプル 🆕
    - [📓] [Phi-4-miniを使用した関数呼び出し](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
    - [📓] [Phi-4-miniを使用してマルチエージェントを作成する関数呼び出し](../../md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
    - [📓] [Ollamaを使用した関数呼び出し](../../md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
    - [📓] [ONNXを使用した関数呼び出し](../../md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)

- マルチモーダルミキシングサンプル
  - Phi-4 サンプル 🆕
    - [📓] [Phi-4-multimodalを使用して技術ジャーナリストとして活動する](../../md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
    - [.NETコンソールアプリケーションを使用してPhi-4-multimodalで画像を分析する](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Phiサンプルの微調整
  - [微調整シナリオ](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [微調整 vs RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [Phi-3を業界の専門家にする微調整](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [VS Code用AIツールキットを使用したPhi-3の微調整](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Azure Machine Learning Serviceを使用したPhi-3の微調整](./md/03.FineTuning/Introduce_AzureML.md)
  - [Loraを使用したPhi-3の微調整](./md/03.FineTuning/FineTuning_Lora.md)
  - [QLoraを使用したPhi-3の微調整](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Azure AI Foundryを使用したPhi-3の微調整](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Azure ML CLI/SDKを使用したPhi-3の微調整](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Microsoft Oliveを使用した微調整](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Microsoft Olive Hands-On Labを使用した微調整](./md/03.FineTuning/olive-lab/readme.md)
  - [Weights and Biasを使用したPhi-3-visionの微調整](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [Apple MLX Frameworkを使用したPhi-3の微調整](./md/03.FineTuning/FineTuning_MLX.md)
  - [Phi-3-visionの微調整 (公式サポート)](./md/03.FineTuning/FineTuning_Vision.md)
  - [Kaito AKS、Azure Containersを使用したPhi-3の微調整 (公式サポート)](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Phi-3および3.5 Visionの微調整](https://github.com/2U1/Phi3-Vision-Finetune)

- ハンズオンラボ
  - [最先端モデルの探索: LLMs、SLMs、ローカル開発など](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [NLPの可能性を解き放つ: Microsoft Oliveを使用した微調整](https://github.com/azure/Ignite_FineTuning_workshop)

- 学術研究論文と出版物
  - [Textbooks Are All You Need II: phi-1.5技術レポート](https://arxiv.org/abs/2309.05463)
  - [Phi-3技術レポート: あなたのスマートフォンでローカルに動作する高性能言語モデル](https://arxiv.org/abs/2404.14219)
  - [Phi-4技術レポート](https://arxiv.org/abs/2412.08905)
  - [Phi-4-Mini技術レポート: Mixture-of-LoRAsによるコンパクトで強力なマルチモーダル言語モデル](https://arxiv.org/abs/2503.01743)
  - [車載機能呼び出しのための小型言語モデルの最適化](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) Phi-3を微調整して選択式質問応答を行う: 方法論、結果、課題](https://arxiv.org/abs/2501.01588)
- [Phi-4-reasoning 技術レポート](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
- [Phi-4-mini-reasoning 技術レポート](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Phiモデルの使用方法

### Azure AI FoundryでのPhi

Microsoft Phiの使用方法や、さまざまなハードウェアデバイスでのE2Eソリューションの構築方法を学ぶことができます。Phiを体験するには、モデルを試してみたり、シナリオに合わせてPhiをカスタマイズすることから始めてください。 [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai)で詳細を確認できます。[Azure AI Foundryの入門ガイド](/md/02.QuickStart/AzureAIFoundry_QuickStart.md)も参照してください。

**Playground**  
各モデルには専用のプレイグラウンドがあり、モデルをテストできます。[Azure AI Playground](https://aka.ms/try-phi3)。

### GitHubモデルでのPhi

Microsoft Phiの使用方法や、さまざまなハードウェアデバイスでのE2Eソリューションの構築方法を学ぶことができます。Phiを体験するには、モデルを試してみたり、シナリオに合わせてPhiをカスタマイズすることから始めてください。 [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo)で詳細を確認できます。[GitHub Model Catalogの入門ガイド](/md/02.QuickStart/GitHubModel_QuickStart.md)も参照してください。

**Playground**  
各モデルには専用の[プレイグラウンドがあります](/md/02.QuickStart/GitHubModel_QuickStart.md)。

### Hugging FaceでのPhi

モデルは[Hugging Face](https://huggingface.co/microsoft)でも見つけることができます。

**Playground**  
[Hugging Chat playground](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## 責任あるAI

Microsoftは、AI製品を責任を持って使用するための支援、学びの共有、透明性ノートや影響評価などのツールを通じた信頼に基づくパートナーシップの構築に取り組んでいます。これらのリソースの多くは[https://aka.ms/RAI](https://aka.ms/RAI)で見つけることができます。  
Microsoftの責任あるAIへのアプローチは、公平性、信頼性と安全性、プライバシーとセキュリティ、包括性、透明性、責任というAI原則に基づいています。

このサンプルで使用されるような大規模な自然言語、画像、音声モデルは、不公平、不信頼、または攻撃的な振る舞いをする可能性があり、それによって害を引き起こすことがあります。[Azure OpenAIサービスの透明性ノート](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text)を参照し、リスクと制限について理解してください。

これらのリスクを軽減するための推奨アプローチは、有害な振る舞いを検出し防止する安全システムをアーキテクチャに組み込むことです。[Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview)は、独立した保護層を提供し、アプリケーションやサービス内で生成された有害なコンテンツを検出することができます。Azure AI Content Safetyには、テキストと画像のAPIが含まれており、有害な素材を検出することができます。Azure AI Foundry内では、Content Safetyサービスを使用して、さまざまなモダリティで有害なコンテンツを検出するサンプルコードを表示、探索、試すことができます。[クイックスタートドキュメント](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest)では、サービスへのリクエストの作成方法を案内しています。

もう一つ考慮すべき側面は、アプリケーション全体のパフォーマンスです。マルチモーダルおよびマルチモデルのアプリケーションでは、パフォーマンスとは、システムがユーザーの期待通りに動作し、有害な出力を生成しないことを意味します。[Performance and Quality and Risk and Safety evaluators](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in)を使用して、アプリケーション全体のパフォーマンスを評価することが重要です。また、[カスタム評価ツール](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators)を作成して評価することも可能です。

開発環境でAIアプリケーションを評価するには、[Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html)を使用できます。テストデータセットまたはターゲットを使用して、生成AIアプリケーションの生成物を、組み込み評価ツールや選択したカスタム評価ツールで定量的に測定します。Azure AI Evaluation SDKを使用してシステムを評価する方法については、[クイックスタートガイド](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk)を参照してください。評価を実行した後は、[Azure AI Foundryで結果を視覚化](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results)することができます。

## 商標

このプロジェクトには、プロジェクト、製品、またはサービスの商標やロゴが含まれている場合があります。Microsoftの商標やロゴの正当な使用は、[Microsoftの商標およびブランドガイドライン](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general)に従う必要があります。  
このプロジェクトの改変版でMicrosoftの商標やロゴを使用する場合、混乱を招いたり、Microsoftの後援を暗示したりしてはなりません。第三者の商標やロゴの使用は、それぞれの第三者のポリシーに従う必要があります。

---

**免責事項**:  
この文書はAI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。元の言語で記載された文書を正式な情報源としてお考えください。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤解について、当社は責任を負いません。