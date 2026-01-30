# **llama.cppを使ったPhiファミリーの量子化**

## **llama.cppとは**

llama.cppは主にC++で書かれたオープンソースのソフトウェアライブラリで、Llamaなどのさまざまな大規模言語モデル（LLM）の推論を行います。主な目的は、幅広いハードウェア上で最小限のセットアップで最先端のLLM推論性能を提供することです。さらに、このライブラリにはPythonバインディングもあり、テキスト補完のための高レベルAPIやOpenAI互換のウェブサーバーを提供しています。

llama.cppの主な目標は、ローカルおよびクラウド環境で幅広いハードウェアに対応し、最小限のセットアップで最先端のLLM推論を可能にすることです。

- 依存関係なしの純粋なC/C++実装
- Appleシリコンを第一級にサポートし、ARM NEON、Accelerate、Metalフレームワークで最適化
- x86アーキテクチャ向けにAVX、AVX2、AVX512をサポート
- 推論高速化とメモリ使用量削減のための1.5ビット、2ビット、3ビット、4ビット、5ビット、6ビット、8ビット整数量子化
- NVIDIA GPUでのLLM実行のためのカスタムCUDAカーネル（AMD GPUはHIPでサポート）
- VulkanおよびSYCLバックエンドのサポート
- VRAM容量を超える大規模モデルの部分的な高速化のためのCPU+GPUハイブリッド推論

## **llama.cppを使ったPhi-3.5の量子化**

Phi-3.5-Instructモデルはllama.cppで量子化可能ですが、Phi-3.5-VisionやPhi-3.5-MoEはまだ対応していません。llama.cppで変換されるフォーマットはggufで、これは最も広く使われている量子化フォーマットでもあります。

Hugging Faceには大量の量子化されたGGUFフォーマットモデルがあります。AI Foundry、Ollama、LlamaEdgeはllama.cppに依存しているため、GGUFモデルもよく使われています。

### **GGUFとは**

GGUFはモデルの高速な読み込みと保存に最適化されたバイナリフォーマットで、推論に非常に効率的です。GGUFはGGMLやその他の実行環境での使用を想定して設計されています。GGUFはllama.cppの開発者である@ggerganovによって開発されました。PyTorchなどのフレームワークで最初に開発されたモデルは、GGUFフォーマットに変換してこれらのエンジンで利用できます。

### **ONNXとGGUFの比較**

ONNXは従来の機械学習／深層学習フォーマットで、さまざまなAIフレームワークで広くサポートされており、エッジデバイスでの利用シナリオも豊富です。一方GGUFはllama.cppをベースにしており、GenAI時代に生まれたと言えます。両者は似た用途を持ちます。組み込みハードウェアやアプリケーション層でより良い性能を求めるならONNXが適しているかもしれません。llama.cppの派生フレームワークや技術を使うならGGUFの方が良いでしょう。

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

***注意*** 

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

**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されました。正確性の向上に努めておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語によるオリジナル文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や誤訳についても、当方は責任を負いかねます。