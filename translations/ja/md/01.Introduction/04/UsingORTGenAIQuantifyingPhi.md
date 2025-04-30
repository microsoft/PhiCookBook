<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b96f9dc2389500e24a2c2c4debf30908",
  "translation_date": "2025-04-04T12:16:26+00:00",
  "source_file": "md\\01.Introduction\\04\\UsingORTGenAIQuantifyingPhi.md",
  "language_code": "ja"
}
-->
# **onnxruntime用のGenerative AI拡張機能を使用したPhiファミリーの量子化**

## **onnxruntime用のGenerative AI拡張機能とは**

この拡張機能は、ONNX Runtime（[https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)）を使用して生成型AIを実行するのを支援します。ONNXモデルのための生成型AIループを提供し、ONNX Runtimeによる推論、ロジット処理、検索とサンプリング、KVキャッシュ管理を含みます。開発者は高レベルの`generate()`メソッドを呼び出すか、ループ内でモデルの各イテレーションを実行して1トークンずつ生成し、ループ内で生成パラメーターをオプションで更新することができます。貪欲探索、ビーム探索、TopP、TopKサンプリングをサポートしており、トークンシーケンスを生成し、繰り返しペナルティなどの組み込みロジット処理を行います。また、カスタムスコアリングを簡単に追加することも可能です。

アプリケーションレベルでは、C++/C#/Pythonを使用してonnxruntime用のGenerative AI拡張機能を利用してアプリケーションを構築できます。モデルレベルでは、微調整済みモデルの統合や関連する量子的なデプロイ作業を行うことができます。

## **onnxruntime用のGenerative AI拡張機能を使用したPhi-3.5の量子化**

### **サポートされているモデル**

onnxruntime用のGenerative AI拡張機能は、Microsoft Phi、Google Gemma、Mistral、Meta LLaMAの量子化変換をサポートしています。

### **onnxruntime用のGenerative AI拡張機能におけるモデルビルダー**

モデルビルダーは、ONNX Runtimeの`generate()` APIで動作する最適化および量子化されたONNXモデルの作成を大幅に加速します。

モデルビルダーを使用すると、モデルをINT4、INT8、FP16、FP32に量子化し、CPU、CUDA、DirectML、モバイルなど、さまざまなハードウェアアクセラレーション方法を組み合わせることができます。

モデルビルダーを使用するには、以下をインストールする必要があります。

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

インストール後、ターミナルからモデルビルダースクリプトを実行して、モデル形式および量子化変換を行うことができます。

```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

関連するパラメーターについて理解しましょう：

1. **model_name** Hugging Face上のモデル名（例：microsoft/Phi-3.5-mini-instruct、microsoft/Phi-3.5-vision-instructなど）。または、モデルを保存しているパス。
2. **path_to_output_folder** 量子化変換後の保存パス。
3. **execution_provider** CPU、CUDA、DirectMLなどの異なるハードウェアアクセラレーションのサポート。
4. **cache_dir_to_save_hf_files** Hugging Faceからモデルをダウンロードしてローカルにキャッシュする場所。

***注：***

## **モデルビルダーを使用してPhi-3.5を量子化する方法**

モデルビルダーは現在、Phi-3.5 InstructおよびPhi-3.5-VisionのONNXモデル量子化をサポートしています。

### **Phi-3.5-Instruct**

**CPUでのINT4量子化変換**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**CUDAでのINT4量子化変換**

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

2. modelsフォルダーにmicrosoft/Phi-3.5-vision-instructをダウンロード  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. 以下のファイルをPhi-3.5-vision-instructフォルダーにダウンロードしてください：

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. 以下のファイルをmodelsフォルダーにダウンロードしてください：  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. ターミナルで以下を実行：

    FP32対応のONNX変換

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **注：**

1. モデルビルダーは現在、Phi-3.5-InstructおよびPhi-3.5-Visionの変換をサポートしていますが、Phi-3.5-MoEはサポートしていません。
2. ONNXの量子化モデルを使用するには、onnxruntime用のGenerative AI拡張機能SDKを通じて利用できます。
3. より責任あるAIを考慮するため、モデル量子化変換後には、より効果的な結果テストを行うことを推奨します。
4. CPU INT4モデルを量子化することで、エッジデバイスにデプロイでき、より良いアプリケーションシナリオが実現します。そのため、Phi-3.5-InstructをINT4を中心に完成させました。

## **リソース**

1. onnxruntime用のGenerative AI拡張機能についてもっと学ぶ  
[https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. onnxruntime用のGenerative AI拡張機能 GitHubリポジトリ  
[https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**免責事項**:  
この文書はAI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確さが含まれる可能性があることにご注意ください。原文（元の言語で書かれた文書）を信頼できる情報源としてお考えください。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤った解釈について、当方は責任を負いません。