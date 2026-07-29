# **onnxruntimeのGenerative AI拡張機能を使用したPhiファミリーの量子化**

## **onnxruntimeのGenerative AI拡張機能とは**

この拡張機能はONNX Runtime（[https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)）で生成AIを実行するのに役立ちます。ONNXモデル向けの生成AIループを提供し、ONNX Runtimeによる推論、ロジット処理、探索とサンプリング、KVキャッシュ管理などを含みます。開発者は高レベルなgenerate()メソッドを呼び出すことも、ループ内でモデルの各イテレーションを実行して一度に1トークンを生成し、生成パラメータをオプションでループ内で更新することも可能です。貪欲法やビームサーチ、TopPやTopKサンプリングによるトークン列の生成をサポートし、繰り返しペナルティなどの組み込みのロジット処理も備えています。カスタムスコアリングも簡単に追加できます。

アプリケーションレベルでは、onnxruntimeのGenerative AI拡張機能を使ってC++/ C# / Pythonでアプリケーションを構築できます。モデルレベルでは、微調整済みモデルをマージし、関連する量子化デプロイメント作業を行うのに役立ちます。


## **onnxruntimeのGenerative AI拡張機能を使ったPhi-3.5の量子化**

### <strong>サポートモデル</strong>

onnxruntimeのGenerative AI拡張機能は、Microsoft Phi、Google Gemma、Mistral、Meta LLaMAの量子化変換をサポートします。


### **onnxruntimeのGenerative AI拡張機能のModel Builder**

Model Builderは、ONNX Runtime generate() APIで動作する最適化および量子化されたONNXモデルの作成を大幅に加速します。

Model Builderを使うと、モデルをINT4、INT8、FP16、FP32に量子化し、CPU、CUDA、DirectML、Mobileなどのさまざまなハードウェアアクセラレーション手法を組み合わせることができます。

Model Builderを使用するには以下をインストールする必要があります

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

インストール後、ターミナルからModel Builderスクリプトを実行してモデル形式および量子化変換を行うことができます。


```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

関連パラメータの理解

1. **model_name** Hugging face上のモデル名。例：microsoft/Phi-3.5-mini-instruct、microsoft/Phi-3.5-vision-instructなど。モデルを保存しているパスも指定可能

2. **path_to_output_folder** 量子化後の保存先パス

3. **execution_provider** CPU、CUDA、DirectMLなどの異なるハードウェアアクセラレーションのサポート指定

4. **cache_dir_to_save_hf_files** Hugging faceからモデルをダウンロードしローカルにキャッシュするディレクトリ




***注意：*** <ul>onnxruntimeのGenerative AI拡張機能はプレビュー中ですが、Microsoft Oliveに統合されており、Microsoft Olive経由でGenerative AI拡張機能のModel Builder機能を呼び出すことも可能です。</ul>

## **Model Builderを使ったPhi-3.5の量子化方法**

Model Builderは現在、Phi-3.5 InstructとPhi-3.5 VisionのONNXモデルの量子化をサポートしています

### **Phi-3.5-Instruct**


**CPUアクセラレーションによる量子化INT 4変換**


```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**CUDAアクセラレーションによる量子化INT 4変換**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```



```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```


### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. ターミナルで環境を設定

```bash

mkdir models

cd models 

```

2. modelsフォルダにmicrosoft/Phi-3.5-vision-instructをダウンロード
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. 以下のファイルをYour Phi-3.5-vision-instructフォルダにダウンロードしてください

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)


4. このファイルをmodelsフォルダにダウンロード
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. ターミナルへ移動

    FP32でONNXサポートの変換を行う


```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```


### **注意：**

1. Model Builderは現在Phi-3.5-InstructとPhi-3.5-Visionの変換をサポートしていますが、Phi-3.5-MoEはサポートしていません

2. ONNXの量子化モデルを使用するには、Generative AI拡張機能のonnxruntime SDKを通じて利用できます

3. より責任あるAIを考慮する必要があるため、モデルの量子化変換後はより効果的な結果テストを推奨します

4. CPUのINT4モデルを量子化することでEdgeデバイスへの展開が可能となり、より良い適用シナリオが広がります。そのため、Phi-3.5-InstructのINT 4周りの作業は完了しています


## <strong>リソース</strong>

1. onnxruntimeのGenerative AI拡張機能の詳細はこちら [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. onnxruntimeのGenerative AI拡張機能GitHubリポジトリ [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->