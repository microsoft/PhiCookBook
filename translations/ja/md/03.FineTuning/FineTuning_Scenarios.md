## ファインチューニングのシナリオ

![FineTuning with MS Services](../../../../translated_images/ja/FinetuningwithMS.3d0cec8ae693e094.webp)

このセクションでは、Microsoft FoundryおよびAzure環境におけるファインチューニングのシナリオについて、展開モデル、インフラストラクチャ層、および一般的に使用される最適化手法を含めて概要を説明します。

<strong>プラットフォーム</strong>  
これは、Microsoft Foundry（旧Microsoft Foundry）やAzure Machine Learningなどのマネージドサービスを含み、モデル管理、オーケストレーション、実験追跡、および展開ワークフローを提供します。

<strong>インフラストラクチャ</strong>  
ファインチューニングにはスケーラブルなコンピュートリソースが必要です。Azure環境では、通常、GPUベースの仮想マシンや軽量ワークロード用のCPUリソース、ならびにデータセットやチェックポイント用のスケーラブルなストレージが含まれます。

**ツール＆フレームワーク**  
ファインチューニングのワークフローは一般的に、Hugging Face Transformers、DeepSpeed、PEFT（パラメーター効率の良いファインチューニング）のようなフレームワークと最適化ライブラリに依存しています。

Microsoftの技術を用いたファインチューニングプロセスは、プラットフォームサービス、コンピュートインフラストラクチャ、およびトレーニングフレームワークにまたがります。これらのコンポーネントの連携方法を理解することで、開発者は基盤モデルを特定のタスクやプロダクションのシナリオに効率的に適応させることができます。

## モデルをサービスとして

ホステッドファインチューニングを使用してモデルをファインチューニングし、コンピュートの作成や管理は必要ありません。

![MaaS Fine Tuning](../../../../translated_images/ja/MaaSfinetune.3eee4630607aff0d.webp)

Phi-3、Phi-3.5、およびPhi-4モデルファミリー向けにサーバーレスファインチューニングが利用可能であり、開発者はコンピュートの手配なしに、クラウドおよびエッジのシナリオにモデルを迅速かつ容易にカスタマイズできます。

## モデルをプラットフォームとして

ユーザーが自身でコンピュートを管理し、モデルのファインチューニングを行います。

![Maap Fine Tuning](../../../../translated_images/ja/MaaPFinetune.fd3829c1122f5d1c.webp)

[Fine Tuning Sample](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/system/finetune/chat-completion/chat-completion.ipynb)

## ファインチューニング手法の比較

|シナリオ|LoRA|QLoRA|PEFT|DeepSpeed|ZeRO|DoRA|
|---|---|---|---|---|---|---|
|事前学習済みLLMを特定のタスクやドメインに適応|はい|はい|はい|はい|はい|はい|
|テキスト分類、固有表現抽出、機械翻訳などのNLPタスク向けファインチューニング|はい|はい|はい|はい|はい|はい|
|QAタスク向けファインチューニング|はい|はい|はい|はい|はい|はい|
|チャットボットでの人間らしい応答生成のためのファインチューニング|はい|はい|はい|はい|はい|はい|
|音楽、アート、その他創造的表現のためのファインチューニング|はい|はい|はい|はい|はい|はい|
|計算コストと財務コストの削減|はい|はい|はい|はい|はい|はい|
|メモリ使用量の削減|はい|はい|はい|はい|はい|はい|
|効率的なファインチューニングのためのパラメーター削減|はい|はい|はい|いいえ|いいえ|はい|
|利用可能なすべてのGPUデバイスの合計GPUメモリにアクセス可能なメモリ効率的なデータ並列の形式|いいえ|いいえ|いいえ|はい|はい|いいえ|

> [!NOTE]
> LoRA、QLoRA、PEFT、DoRAはパラメーター効率の良いファインチューニング手法であり、一方でDeepSpeedとZeROは分散トレーニングとメモリ最適化に重点を置いています。

## ファインチューニングのパフォーマンス例

![Finetuning Performance](../../../../translated_images/ja/Finetuningexamples.a9a41214f8f5afc1.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**:  
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な箇所が含まれる可能性があることをご承知おきください。原文は母国語の文書が正本とみなされます。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の使用に起因するいかなる誤解や誤訳についても当方は責任を負いません。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->