<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2a7aaeb42235207ba74581473b305581",
  "translation_date": "2025-04-04T12:15:25+00:00",
  "source_file": "md\\01.Introduction\\04\\UsingLlamacppQuantifyingPhi.md",
  "language_code": "ja"
}
-->
# **Phiファミリーの量子化をllama.cppで行う**

## **llama.cppとは**

llama.cppは主にC++で書かれたオープンソースのソフトウェアライブラリで、Llamaのような様々な大規模言語モデル（LLM）の推論を実行します。このライブラリの主な目的は、最小限のセットアップで幅広いハードウェアにおいて最先端の性能を提供することです。また、このライブラリにはPythonバインディングもあり、テキスト補完のための高レベルAPIやOpenAI互換のウェブサーバーを提供しています。

llama.cppの主な目標は、ローカルおよびクラウド環境で、最小限のセットアップで幅広いハードウェア上で最先端の性能を持つLLM推論を可能にすることです。

- 依存関係のない純粋なC/C++実装
- Appleシリコンに最適化 - ARM NEON、Accelerate、Metalフレームワークを活用
- x86アーキテクチャ向けのAVX、AVX2、AVX512サポート
- 推論を高速化しメモリ使用量を削減するための1.5ビット、2ビット、3ビット、4ビット、5ビット、6ビット、8ビット整数量子化
- NVIDIA GPUでLLMを実行するためのカスタムCUDAカーネル（AMD GPUはHIPでサポート）
- VulkanおよびSYCLバックエンドのサポート
- CPU+GPUハイブリッド推論により、VRAM容量を超える大規模モデルを部分的に高速化

## **Phi-3.5の量子化をllama.cppで行う**

Phi-3.5-Instructモデルはllama.cppを使用して量子化することができますが、Phi-3.5-VisionおよびPhi-3.5-MoEは現在サポートされていません。llama.cppによって変換される形式はggufであり、これが最も広く使用されている量子化形式です。

Hugging Faceには大量の量子化されたGGUF形式モデルがあります。AI Foundry、Ollama、LlamaEdgeはllama.cppに依存しているため、GGUFモデルが頻繁に使用されます。

### **GGUFとは**

GGUFはモデルの高速な読み込みと保存に最適化されたバイナリ形式であり、推論において非常に効率的です。GGUFはGGMLやその他の実行エンジンで使用することを目的として設計されています。GGUFは、llama.cppの開発者である@ggerganovによって開発されました。このフレームワークは人気のあるC/C++ LLM推論フレームワークです。PyTorchなどのフレームワークで開発されたモデルは、これらのエンジンで使用するためにGGUF形式に変換することができます。

### **ONNXとGGUFの比較**

ONNXは従来の機械学習/深層学習形式であり、様々なAIフレームワークで良好にサポートされており、エッジデバイスでの利用シナリオに適しています。一方、GGUFはllama.cppに基づいており、生成AI時代に生まれたものと言えます。両者は似たような用途を持っています。埋め込みハードウェアやアプリケーション層での性能を重視する場合、ONNXが選択肢となるでしょう。llama.cppの派生フレームワークや技術を使用する場合、GGUFがより適しているかもしれません。

### **Phi-3.5-Instructをllama.cppで量子化する方法**

**1. 環境設定**


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```


**2. 量子化**

llama.cppを使用してPhi-3.5-InstructをFP16 GGUFに変換


```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```

Phi-3.5をINT4に量子化


```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```


**3. テスト**

llama-cpp-pythonをインストール


```bash

pip install llama-cpp-python -U

```

***注記*** 

Apple Siliconを使用している場合は、以下のようにllama-cpp-pythonをインストールしてください


```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

テスト


```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```



## **リソース**

1. llama.cppについて詳しく学ぶ [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. GGUFについて詳しく学ぶ [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

**免責事項**:  
この文書は、AI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確さが含まれる可能性があることをご承知ください。元の言語で記載された文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の利用に起因する誤解や誤読について、当社は責任を負いません。