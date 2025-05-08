<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "743d7e9cb9c4e8ea642d77bee657a7fa",
  "translation_date": "2025-05-08T05:19:39+00:00",
  "source_file": "md/03.FineTuning/LetPhi3gotoIndustriy.md",
  "language_code": "ja"
}
-->
# **Phi-3を業界の専門家に育てる**

Phi-3モデルを業界に導入するには、業界のビジネスデータをPhi-3モデルに追加する必要があります。選択肢は2つあり、1つはRAG（Retrieval Augmented Generation）、もう1つはFine Tuningです。

## **RAGとFine-Tuningの比較**

### **Retrieval Augmented Generation**

RAGはデータ検索＋テキスト生成の組み合わせです。企業の構造化データや非構造化データはベクターデータベースに保存されます。関連するコンテンツを検索すると、関連する要約や内容が見つかり、それがコンテキストとして形成され、LLM/SLMのテキスト補完機能と組み合わせてコンテンツを生成します。

### **Fine-tuning**

Fine-tuningは特定のモデルの改善を目的としています。モデルのアルゴリズムから始める必要はなく、データを継続的に蓄積する必要があります。業界アプリケーションでより正確な専門用語や言語表現が求められる場合、Fine-tuningが適しています。ただし、データが頻繁に変わる場合は、Fine-tuningが複雑になることがあります。

### **選び方**

1. 外部データの導入が必要な場合は、RAGが最適です。

2. 安定した正確な業界知識を出力したい場合は、Fine-tuningが良い選択です。RAGは関連コンテンツを引き出すことを優先しますが、専門的なニュアンスを常に捉えられるとは限りません。

3. Fine-tuningには高品質なデータセットが必要で、データ範囲が狭い場合はあまり効果が出ません。RAGの方が柔軟です。

4. Fine-tuningはブラックボックス的で内部メカニズムが理解しにくいですが、RAGはデータの出典を追いやすく、誤生成や内容の誤りを効果的に調整でき、透明性が高いです。

### **利用シナリオ**

1. 特定の専門用語や表現が必要な垂直業界では、***Fine-tuning***が最適です。

2. 複数の知識ポイントを統合するQAシステムには、***RAG***が最適です。

3. 自動化された業務フローの組み合わせには、***RAG + Fine-tuning***が最適です。

## **RAGの使い方**

![rag](../../../../translated_images/rag.2014adc59e6f6007bafac13e800a6cbc3e297fbb9903efe20a93129bd13987e9.ja.png)

ベクターデータベースは数学的な形式でデータを保存するコレクションです。ベクターデータベースにより、機械学習モデルは過去の入力を記憶しやすくなり、検索、推薦、テキスト生成などのユースケースをサポートできます。データは厳密な一致ではなく類似度指標に基づいて識別されるため、コンピュータモデルがデータの文脈を理解しやすくなります。

ベクターデータベースはRAG実現の鍵です。text-embedding-3やjina-ai-embeddingなどのベクターモデルを使ってデータをベクター形式に変換できます。

RAGアプリケーションの作成について詳しくは[https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?WT.mc_id=aiml-138114-kinfeylo)をご覧ください。

## **Fine-tuningの使い方**

Fine-tuningでよく使われるアルゴリズムはLoraとQLoraです。どちらを選ぶべきか？
- [このサンプルノートブックで詳しく学ぶ](../../../../code/04.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python FineTuningサンプルの例](../../../../code/04.Finetuning/FineTrainingScript.py)

### **LoraとQLora**

![lora](../../../../translated_images/qlora.e6446c988ee04ca08807488bb7d9e2c0ea7ef4af9d000fc6d13032b4ac2de18d.ja.png)

LoRA（Low-Rank Adaptation）とQLoRA（Quantized Low-Rank Adaptation）は、Parameter Efficient Fine Tuning（PEFT）を用いて大規模言語モデル（LLM）を効率的にファインチューニングする技術です。PEFTは従来の方法より効率的にモデルを訓練するために設計されています。

LoRAは単独のファインチューニング技術で、重みの更新行列に低ランク近似を適用することでメモリ使用量を削減します。高速な訓練時間を提供し、従来のファインチューニングに近い性能を維持します。

QLoRAはLoRAの拡張版で、量子化技術を取り入れてメモリ使用量をさらに削減します。QLoRAは事前学習済みLLMの重みパラメータを4ビット精度に量子化し、LoRAよりもメモリ効率が高いです。ただし、量子化と逆量子化のステップが追加されるため、QLoRAの訓練はLoRAより約30％遅くなります。

QLoRAは量子化による誤差を修正するためにLoRAを補助的に使用します。QLoRAは数十億パラメータの大規模モデルを、比較的小規模で入手しやすいGPUでファインチューニング可能にします。例えば、QLoRAは36台のGPUを必要とする70Bパラメータモデルを、わずか2台のGPUでファインチューニングできます。

**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されました。正確性の向上に努めておりますが、自動翻訳には誤りや不正確な箇所が含まれる可能性があることをご了承ください。原文の言語によるオリジナル文書が正式な情報源とみなされます。重要な情報については、専門の人間翻訳をご利用いただくことを推奨します。本翻訳の利用により生じた誤解や解釈の相違について、当方は一切の責任を負いかねます。