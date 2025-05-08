<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "462bddc47427d8785f3c9fd817b346fe",
  "translation_date": "2025-05-08T06:11:05+00:00",
  "source_file": "md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md",
  "language_code": "ja"
}
-->
# **llama.cppを使ったPhiファミリーの量子化**

## **llama.cppとは**

llama.cppは主にC++で書かれたオープンソースのソフトウェアライブラリで、Llamaなどのさまざまな大規模言語モデル（LLM）の推論を行います。主な目的は、幅広いハードウェアで最小限のセットアップで最先端のLLM推論性能を提供することです。さらに、このライブラリにはPythonバインディングもあり、テキスト補完のための高レベルAPIやOpenAI互換のウェブサーバーを提供しています。

llama.cppの主な目標は、ローカルやクラウド上の多様なハードウェアで、最小限のセットアップで最先端のLLM推論を可能にすることです。

- 依存関係なしの純粋なC/C++実装
- Appleシリコンを優先サポートし、ARM NEON、Accelerate、Metalフレームワークで最適化
- x86アーキテクチャ向けにAVX、AVX2、AVX512をサポート
- 1.5ビット、2ビット、3ビット、4ビット、5ビット、6ビット、8ビットの整数量子化による高速推論とメモリ使用量削減
- NVIDIA GPUでのLLM実行のためのカスタムCUDAカーネル（AMD GPUはHIP経由でサポート）
- VulkanおよびSYCLバックエンドのサポート
- 総VRAM容量を超える大規模モデルの部分的高速化のためのCPU+GPUハイブリッド推論

## **llama.cppによるPhi-3.5の量子化**

Phi-3.5-Instructモデルはllama.cppで量子化可能ですが、Phi-3.5-VisionやPhi-3.5-MoEはまだサポートされていません。llama.cppが変換するフォーマットはggufで、これが最も広く使われている量子化フォーマットでもあります。

Hugging Faceには多くの量子化済みGGUFフォーマットモデルがあります。AI Foundry、Ollama、LlamaEdgeはllama.cppに依存しているため、GGUFモデルもよく使われています。

### **GGUFとは**

GGUFはモデルの高速な読み込みと保存に最適化されたバイナリフォーマットで、推論用途に非常に効率的です。GGUFはGGMLや他の実行エンジン向けに設計されています。GGUFはllama.cppの開発者である@ggerganovによって開発されました。PyTorchなどのフレームワークで開発されたモデルは、これらのエンジンで使うためにGGUFフォーマットに変換可能です。

### **ONNXとGGUFの比較**

ONNXは従来の機械学習・深層学習フォーマットで、多様なAIフレームワークで広くサポートされており、エッジデバイスでの利用に適しています。一方、GGUFはllama.cppをベースにしており、生成AI時代に生まれたフォーマットと言えます。用途は似ていますが、組み込みハードウェアやアプリケーション層でより良い性能を求めるならONNXが適しているかもしれません。llama.cppの派生フレームワークや技術を利用するなら、GGUFの方が向いています。

### **llama.cppを使ったPhi-3.5-Instructの量子化**

**1. 環境設定**


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```


**2. 量子化**

llama.cppを使ってPhi-3.5-InstructをFP16 GGUFに変換


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

***Note*** 

Apple Siliconを使う場合は、llama-cpp-pythonを以下のようにインストールしてください


```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

テスト実行


```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```



## **参考資料**

1. llama.cppについて詳しくはこちら [https://github.com/ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)
2. onnxruntimeについて詳しくはこちら [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)
3. GGUFについて詳しくはこちら [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

**免責事項**:  
本書類はAI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されました。正確性を期しておりますが、自動翻訳には誤りや不正確な箇所が含まれる可能性があります。正式な情報源としては、原文（原言語）の文書を参照してください。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の使用により生じた誤解や誤訳について、一切の責任を負いかねますのでご了承ください。