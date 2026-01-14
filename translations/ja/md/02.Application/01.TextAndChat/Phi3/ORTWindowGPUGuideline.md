<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b066fc29c1b2129df84e027cb75119ce",
  "translation_date": "2025-07-17T02:40:38+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/ORTWindowGPUGuideline.md",
  "language_code": "ja"
}
-->
# **OnnxRuntime GenAI Windows GPU ガイドライン**

このガイドラインは、Windows上でGPUを使用してONNX Runtime (ORT) をセットアップおよび利用する手順を提供します。GPUアクセラレーションを活用してモデルのパフォーマンスと効率を向上させることを目的としています。

本書では以下について説明します：

- 環境構築：CUDA、cuDNN、ONNX Runtimeなど必要な依存関係のインストール手順
- 設定：GPUリソースを効果的に利用するための環境およびONNX Runtimeの設定方法
- 最適化のヒント：GPU設定を微調整して最適なパフォーマンスを引き出すためのアドバイス

### **1. Python 3.10.x /3.11.8**

   ***注記*** Python環境には[Miniforge](https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Windows-x86_64.exe)の使用を推奨します

   ```bash

   conda create -n pydev python==3.11.8

   conda activate pydev

   ```

   ***Reminder*** もしPythonのONNXライブラリをインストールしている場合は、アンインストールしてください

### **2. wingetでCMakeをインストール**

   ```bash

   winget install -e --id Kitware.CMake

   ```

### **3. Visual Studio 2022 - C++によるデスクトップ開発をインストール**

   ***注記*** コンパイルしない場合はこのステップをスキップできます

![CPP](../../../../../../translated_images/ja/01.42f52a2b2aedff02.png)

### **4. NVIDIAドライバーのインストール**

1. **NVIDIA GPUドライバー**  [https://www.nvidia.com/en-us/drivers/](https://www.nvidia.com/en-us/drivers/)

2. **NVIDIA CUDA 12.4** [https://developer.nvidia.com/cuda-12-4-0-download-archive](https://developer.nvidia.com/cuda-12-4-0-download-archive)

3. **NVIDIA CUDNN 9.4**  [https://developer.nvidia.com/cudnn-downloads](https://developer.nvidia.com/cudnn-downloads)

***Reminder*** インストール時はデフォルト設定を使用してください

### **5. NVIDIA環境の設定**

NVIDIA CUDNN 9.4のlib、bin、includeフォルダの内容をNVIDIA CUDA 12.4の対応するフォルダにコピーします

- *'C:\Program Files\NVIDIA\CUDNN\v9.4\bin\12.6'* のファイルを *'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\bin'* にコピー

- *'C:\Program Files\NVIDIA\CUDNN\v9.4\include\12.6'* のファイルを *'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\include'* にコピー

- *'C:\Program Files\NVIDIA\CUDNN\v9.4\lib\12.6'* のファイルを *'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\lib\x64'* にコピー

### **6. Phi-3.5-mini-instruct-onnxのダウンロード**

   ```bash

   winget install -e --id Git.Git

   winget install -e --id GitHub.GitLFS

   git lfs install

   git clone https://huggingface.co/microsoft/Phi-3.5-mini-instruct-onnx

   ```

### **7. InferencePhi35Instruct.ipynbの実行**

   [Notebook](../../../../../../code/09.UpdateSamples/Aug/ortgpu-phi35-instruct.ipynb)を開いて実行してください

![RESULT](../../../../../../translated_images/ja/02.b9b06996cf7255d5.png)

### **8. ORT GenAI GPUのコンパイル**

   ***注記*** 
   
   1. まず、onnx、onnxruntime、onnxruntime-genaiに関するすべてをアンインストールしてください

   
   ```bash

   pip list 
   
   ```

   その後、すべてのonnxruntimeライブラリをアンインストールします。例：


   ```bash

   pip uninstall onnxruntime

   pip uninstall onnxruntime-genai

   pip uninstall onnxruntume-genai-cuda
   
   ```

   2. Visual Studio拡張機能のサポートを確認

   C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\extras にアクセスし、C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\extras\visual_studio_integration が存在するか確認してください。
   
   見つからない場合は、他のCudaツールキットのドライバーフォルダを確認し、visual_studio_integrationフォルダとその内容をC:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\extras\visual_studio_integrationにコピーしてください

   - コンパイルしない場合はこのステップをスキップできます

   ```bash

   git clone https://github.com/microsoft/onnxruntime-genai

   ```

   - [https://github.com/microsoft/onnxruntime/releases/download/v1.19.2/onnxruntime-win-x64-gpu-1.19.2.zip](https://github.com/microsoft/onnxruntime/releases/download/v1.19.2/onnxruntime-win-x64-gpu-1.19.2.zip) をダウンロード

   - onnxruntime-win-x64-gpu-1.19.2.zipを解凍し、フォルダ名を**ort**に変更してonnxruntime-genaiにコピー

   - Windows TerminalでVS 2022のDeveloper Command Promptを開き、onnxruntime-genaiに移動

![RESULT](../../../../../../translated_images/ja/03.b83ce473d5ff9b9b.png)

   - Python環境でコンパイルを実行

   
   ```bash

   cd onnxruntime-genai

   python build.py --use_cuda  --cuda_home "C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4" --config Release
 

   cd build/Windows/Release/Wheel

   pip install .whl

   ```

**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されました。正確性を期しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語によるオリジナル文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や誤訳についても、当方は一切の責任を負いかねます。
