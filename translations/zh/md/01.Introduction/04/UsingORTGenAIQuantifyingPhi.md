<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b96f9dc2389500e24a2c2c4debf30908",
  "translation_date": "2025-04-03T07:06:04+00:00",
  "source_file": "md\\01.Introduction\\04\\UsingORTGenAIQuantifyingPhi.md",
  "language_code": "zh"
}
-->
# **使用 Generative AI extensions for onnxruntime 对 Phi 系列进行量化**

## **什么是 Generative AI extensions for onnxruntime**

此扩展帮助您通过 ONNX Runtime 运行生成式 AI（[https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)）。它为 ONNX 模型提供了生成式 AI 循环，包括使用 ONNX Runtime 推理、logits 处理、搜索和采样以及 KV 缓存管理。开发者可以调用高级的 generate() 方法，或者在循环中运行模型的每次迭代，一次生成一个 token，并可以在循环中动态更新生成参数。它支持贪婪搜索、束搜索以及 TopP、TopK 采样来生成 token 序列，并内置 logits 处理功能，如重复惩罚。此外，您还可以轻松添加自定义评分。

在应用层面，您可以使用 Generative AI extensions for onnxruntime 构建基于 C++/C#/Python 的应用程序。在模型层面，您可以用于合并微调模型并进行相关量化部署工作。

## **使用 Generative AI extensions for onnxruntime 对 Phi-3.5 进行量化**

### **支持的模型**

Generative AI extensions for onnxruntime 支持对以下模型进行量化转换：Microsoft Phi、Google Gemma、Mistral、Meta LLaMA。

### **Generative AI extensions for onnxruntime 的模型构建器**

模型构建器显著加速了创建优化和量化的 ONNX 模型，这些模型可以通过 ONNX Runtime 的 generate() API 运行。

通过模型构建器，您可以将模型量化为 INT4、INT8、FP16、FP32，并结合不同的硬件加速方式，如 CPU、CUDA、DirectML、移动设备等。

使用模型构建器需要安装以下内容：

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

安装完成后，您可以通过终端运行模型构建器脚本来进行模型格式和量化转换。

```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

了解相关参数：

1. **model_name** Hugging Face 上的模型名称，例如 microsoft/Phi-3.5-mini-instruct、microsoft/Phi-3.5-vision-instruct 等，也可以是您存储模型的路径。

2. **path_to_output_folder** 量化转换的保存路径。

3. **execution_provider** 不同的硬件加速支持，例如 cpu、cuda、DirectML。

4. **cache_dir_to_save_hf_files** 我们从 Hugging Face 下载模型并将其本地缓存。

***注意：***

## **如何使用模型构建器量化 Phi-3.5**

模型构建器现在支持对 Phi-3.5 Instruct 和 Phi-3.5 Vision 的 ONNX 模型进行量化。

### **Phi-3.5-Instruct**

**使用 CPU 加速进行量化 INT4 转换**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**使用 CUDA 加速进行量化 INT4 转换**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. 在终端中设置环境

```bash

mkdir models

cd models 

```

2. 在 models 文件夹中下载 microsoft/Phi-3.5-vision-instruct  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. 请将以下文件下载到您的 Phi-3.5-vision-instruct 文件夹：

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. 将以下文件下载到 models 文件夹：  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. 打开终端

    转换为支持 FP32 的 ONNX

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **注意：**

1. 模型构建器目前支持对 Phi-3.5-Instruct 和 Phi-3.5-Vision 的转换，但不支持 Phi-3.5-MoE。

2. 要使用 ONNX 的量化模型，可以通过 Generative AI extensions for onnxruntime SDK 实现。

3. 我们需要更多地考虑负责任的 AI，因此在完成模型量化转换后，建议进行更有效的结果测试。

4. 通过量化 CPU INT4 模型，我们可以将其部署到边缘设备，从而获得更好的应用场景，因此我们围绕 INT4 完成了对 Phi-3.5-Instruct 的优化。

## **资源**

1. 了解更多关于 Generative AI extensions for onnxruntime 的信息：[https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Generative AI extensions for onnxruntime 的 GitHub 仓库：[https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**免责声明**：  
本文档使用AI翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们努力确保翻译的准确性，但请注意，自动翻译可能会包含错误或不准确之处。原始语言版本的文档应被视为权威来源。对于关键信息，建议使用专业人工翻译。对于因使用此翻译而产生的任何误解或错误解释，我们不承担任何责任。