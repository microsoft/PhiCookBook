<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e08ce816e23ad813244a09ca34ebb8ac",
  "translation_date": "2025-07-16T19:56:49+00:00",
  "source_file": "md/01.Introduction/03/AIPC_Inference.md",
  "language_code": "ja"
}
-->
# **AI PCでのPhi-3推論**

生成AIの進化とエッジデバイスのハードウェア性能向上により、ユーザーのBYOD（Bring Your Own Device）デバイスに多くの生成AIモデルが組み込まれるようになってきました。AI PCもその一例です。2024年から、Intel、AMD、QualcommはPCメーカーと協力し、ハードウェアの改良を通じてローカルで生成AIモデルを展開できるAI PCを導入しています。本稿ではIntelのAI PCに焦点を当て、Intel AI PC上でのPhi-3の展開方法を解説します。

### NPUとは何か

NPU（Neural Processing Unit）は、より大きなSoC上に統合された専用プロセッサで、ニューラルネットワークの演算やAIタスクの高速化に特化しています。汎用CPUやGPUとは異なり、NPUはデータ駆動型の並列計算に最適化されており、動画や画像などの大量のマルチメディアデータ処理やニューラルネットワークの演算に非常に効率的です。音声認識、ビデオ通話の背景ぼかし、物体検出などの写真や動画編集処理など、AI関連のタスクに特に強みを持っています。

## NPUとGPUの違い

多くのAIや機械学習の処理はGPUで行われますが、GPUとNPUには重要な違いがあります。  
GPUは並列計算能力で知られていますが、すべてのGPUがグラフィックス以外の処理に同じ効率を持つわけではありません。一方、NPUはニューラルネットワークの複雑な計算に特化して設計されており、AIタスクに非常に効果的です。

まとめると、NPUはAI計算を加速する数学の達人であり、AI PC時代の重要な役割を担っています！

***本例はIntelの最新Intel Core Ultraプロセッサをベースにしています***

## **1. NPUを使ってPhi-3モデルを実行する**

Intel® NPUデバイスは、Intel® Core™ Ultra世代（旧Meteor Lake）以降のIntelクライアントCPUに統合されたAI推論アクセラレータです。人工ニューラルネットワークのタスクを省電力で実行可能にします。

![Latency](../../../../../translated_images/aipcphitokenlatency.2be14f04f30a3bf7.ja.png)

![Latency770](../../../../../translated_images/aipcphitokenlatency770.e923609a57c5d394.ja.png)

**Intel NPU Acceleration Library**

Intel NPU Acceleration Library [https://github.com/intel/intel-npu-acceleration-library](https://github.com/intel/intel-npu-acceleration-library) は、Intel Neural Processing Unit (NPU)の力を活用し、対応ハードウェア上で高速計算を実現するPythonライブラリです。アプリケーションの効率を向上させます。

Intel® Core™ Ultraプロセッサ搭載AI PCでのPhi-3-miniの例。

![DemoPhiIntelAIPC](../../../../../imgs/01/03/AIPC/aipcphi3-mini.gif)

pipでPythonライブラリをインストール

```bash

   pip install intel-npu-acceleration-library

```

***注意*** プロジェクトはまだ開発中ですが、参照モデルはすでに非常に完成度が高いです。

### **Intel NPU Acceleration LibraryでPhi-3を実行する**

Intel NPUアクセラレーションを使う場合、このライブラリは従来のエンコード処理に影響を与えません。元のPhi-3モデルをFP16、INT8、INT4などに量子化するためにこのライブラリを使うだけです。

```python
from transformers import AutoTokenizer, pipeline,TextStreamer
from intel_npu_acceleration_library import NPUModelForCausalLM, int4
from intel_npu_acceleration_library.compiler import CompilerConfig
import warnings

model_id = "microsoft/Phi-3-mini-4k-instruct"

compiler_conf = CompilerConfig(dtype=int4)
model = NPUModelForCausalLM.from_pretrained(
    model_id, use_cache=True, config=compiler_conf, attn_implementation="sdpa"
).eval()

tokenizer = AutoTokenizer.from_pretrained(model_id)

text_streamer = TextStreamer(tokenizer, skip_prompt=True)
```

量子化が成功したら、続けてNPUを呼び出してPhi-3モデルを実行します。

```python
generation_args = {
   "max_new_tokens": 1024,
   "return_full_text": False,
   "temperature": 0.3,
   "do_sample": False,
   "streamer": text_streamer,
}

pipe = pipeline(
   "text-generation",
   model=model,
   tokenizer=tokenizer,
)

query = "<|system|>You are a helpful AI assistant.<|end|><|user|>Can you introduce yourself?<|end|><|assistant|>"

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    pipe(query, **generation_args)
```

コード実行中は、タスクマネージャーでNPUの稼働状況を確認できます。

![NPU](../../../../../translated_images/aipc_NPU.7a3cb6db47b377e1.ja.png)

***サンプル*** : [AIPC_NPU_DEMO.ipynb](../../../../../code/03.Inference/AIPC/AIPC_NPU_DEMO.ipynb)

## **2. DirectML + ONNX RuntimeでPhi-3モデルを実行する**

### **DirectMLとは**

[DirectML](https://github.com/microsoft/DirectML) は、機械学習向けの高性能でハードウェアアクセラレーション対応のDirectX 12ライブラリです。AMD、Intel、NVIDIA、QualcommなどのDirectX 12対応GPUで共通の機械学習タスクをGPUアクセラレーションします。

単体で使う場合、DirectML APIは低レベルのDirectX 12ライブラリであり、フレームワークやゲーム、リアルタイムアプリケーションなどの高性能・低遅延用途に適しています。Direct3D 12とのシームレスな連携、低オーバーヘッド、ハードウェア間の互換性により、高性能かつ信頼性の高い機械学習加速が可能です。

***注意*** : 最新のDirectMLはすでにNPUをサポートしています(https://devblogs.microsoft.com/directx/introducing-neural-processor-unit-npu-support-in-directml-developer-preview/)

### DirectMLとCUDAの性能・機能比較

**DirectML** はMicrosoftが開発した機械学習ライブラリで、Windowsデバイス（デスクトップ、ノートPC、エッジデバイス）上の機械学習処理を加速します。  
- DX12ベース：DirectX 12上に構築されており、NVIDIAやAMDを含む幅広いGPUをサポート。  
- 幅広い対応：DX12対応GPUなら統合GPUも含めて利用可能。  
- 画像処理：ニューラルネットワークを使った画像認識や物体検出などに適している。  
- 簡単セットアップ：GPUメーカーの特定SDK不要で導入が容易。  
- 性能：特定のワークロードではCUDAより高速な場合もある。  
- 制限：float16の大規模バッチ処理では遅くなることもある。

**CUDA** はNVIDIAの並列計算プラットフォームで、NVIDIA GPUの性能を最大限に引き出すためのプログラミングモデル。  
- NVIDIA専用：NVIDIA GPUに特化。  
- 高度に最適化：NVIDIA GPUでのGPUアクセラレーション処理に優れる。  
- 広く利用：TensorFlowやPyTorchなど多くの機械学習フレームワークが対応。  
- カスタマイズ可能：特定タスク向けに細かく調整可能。  
- 制限：NVIDIAハードウェアに依存し、他GPUとの互換性は限定的。

### DirectMLとCUDAの選択

用途やハードウェア環境、好みによって選択が変わります。  
幅広い互換性と導入の容易さを重視するならDirectMLが適しています。  
NVIDIA GPUを持ち、高度な最適化性能が必要ならCUDAが有力です。  
両者にはそれぞれ長所短所があるため、要件と環境に応じて選んでください。

### **ONNX Runtimeでの生成AI**

AI時代において、AIモデルの移植性は非常に重要です。ONNX Runtimeは学習済みモデルを異なるデバイスに簡単に展開でき、開発者は推論フレームワークを意識せず統一APIで推論を行えます。生成AIの時代においてもONNX Runtimeはコード最適化を行い(https://onnxruntime.ai/docs/genai/)、量子化された生成AIモデルを様々な端末で推論可能にしています。ONNX Runtimeを使った生成AIでは、Python、C#、C/C++でAIモデルAPIを呼び出せます。iPhoneでの展開もC++のONNX Runtime APIを活用できます。

[サンプルコード](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx)

***ONNX Runtimeライブラリのビルド***

```bash

winget install --id=Kitware.CMake  -e

git clone https://github.com/microsoft/onnxruntime.git

cd .\onnxruntime\

./build.bat --build_shared_lib --skip_tests --parallel --use_dml --config Release

cd ../

git clone https://github.com/microsoft/onnxruntime-genai.git

cd .\onnxruntime-genai\

mkdir ort

cd ort

mkdir include

mkdir lib

copy ..\onnxruntime\include\onnxruntime\core\providers\dml\dml_provider_factory.h ort\include

copy ..\onnxruntime\include\onnxruntime\core\session\onnxruntime_c_api.h ort\include

copy ..\onnxruntime\build\Windows\Release\Release\*.dll ort\lib

copy ..\onnxruntime\build\Windows\Release\Release\onnxruntime.lib ort\lib

python build.py --use_dml


```

**ライブラリのインストール**

```bash

pip install .\onnxruntime_genai_directml-0.3.0.dev0-cp310-cp310-win_amd64.whl

```

実行結果はこちら

![DML](../../../../../translated_images/aipc_DML.52a44180393ab491.ja.png)

***サンプル*** : [AIPC_DirectML_DEMO.ipynb](../../../../../code/03.Inference/AIPC/AIPC_DirectML_DEMO.ipynb)

## **3. Intel OpenVinoでPhi-3モデルを実行する**

### **OpenVINOとは**

[OpenVINO](https://github.com/openvinotoolkit/openvino) は、深層学習モデルの最適化と展開のためのオープンソースツールキットです。TensorFlowやPyTorchなどの人気フレームワークの視覚、音声、言語モデルの性能を向上させます。OpenVINOはCPUやGPUと組み合わせてPhi-3モデルの実行にも利用可能です。

***注意*** : 現時点でOpenVINOはNPUをサポートしていません。

### **OpenVINOライブラリのインストール**

```bash

 pip install git+https://github.com/huggingface/optimum-intel.git

 pip install git+https://github.com/openvinotoolkit/nncf.git

 pip install openvino-nightly

```

### **OpenVINOでPhi-3を実行する**

NPUと同様に、OpenVINOも量子化モデルを実行して生成AIモデルを呼び出します。まずPhi-3モデルを量子化し、optimum-cliでコマンドラインから量子化を完了させます。

**INT4**

```bash

optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code ./openvinomodel/phi3/int4

```

**FP16**

```bash

optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format fp16 --trust-remote-code ./openvinomodel/phi3/fp16

```

変換後のフォーマットはこのようになります。

![openvino_convert](../../../../../translated_images/aipc_OpenVINO_convert.9e6360b65331ffca.ja.png)

モデルパス(model_dir)、関連設定(ov_config = {"PERFORMANCE_HINT": "LATENCY", "NUM_STREAMS": "1", "CACHE_DIR": ""})、ハードウェアアクセラレートデバイス(GPU.0)をOVModelForCausalLMで読み込みます。

```python

ov_model = OVModelForCausalLM.from_pretrained(
     model_dir,
     device='GPU.0',
     ov_config=ov_config,
     config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
     trust_remote_code=True,
)

```

コード実行中はタスクマネージャーでGPUの稼働状況を確認できます。

![openvino_gpu](../../../../../translated_images/aipc_OpenVINO_GPU.20180edfffd91e55.ja.png)

***サンプル*** : [AIPC_OpenVino_Demo.ipynb](../../../../../code/03.Inference/AIPC/AIPC_OpenVino_Demo.ipynb)

### ***注意*** : 上記3つの方法にはそれぞれ利点がありますが、AI PCでの推論にはNPUアクセラレーションの利用を推奨します。

**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されました。正確性を期しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語によるオリジナル文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じた誤解や誤訳について、当方は一切の責任を負いかねます。