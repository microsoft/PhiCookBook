# **使用 onnxruntime 的生成式 AI 扩展进行 Phi 系列量化**

## **什么是 onnxruntime 的生成式 AI 扩展**

该扩展帮助您使用 ONNX Runtime 运行生成式 AI（[https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)）。它为 ONNX 模型提供生成式 AI 循环，包括使用 ONNX Runtime 进行推理、logits 处理、搜索和采样，以及 KV 缓存管理。开发者可以调用高级的 generate() 方法，或者在循环中每次生成一个 token，选择性地在循环内更新生成参数。它支持贪婪/光束搜索和 TopP、TopK 采样来生成 token 序列，同时内置了重复惩罚等 logits 处理。您也可以轻松添加自定义评分。

在应用层，您可以使用 onnxruntime 的生成式 AI 扩展用 C++/C#/Python 构建应用程序；在模型层，可用于合并微调后的模型及其相关的量化部署工作。


## **使用 onnxruntime 的生成式 AI 扩展量化 Phi-3.5**

### <strong>支持的模型</strong>

onnxruntime 的生成式 AI 扩展支持 Microsoft Phi、Google Gemma、Mistral、Meta LLaMA 的量化转换。


### **onnxruntime 生成式 AI 扩展中的模型构建器**

模型构建器大幅加速了优化和量化 ONNX 模型的创建，这些模型可通过 ONNX Runtime 的 generate() API 运行。

利用模型构建器，您可以将模型量化为 INT4、INT8、FP16、FP32，并结合 CPU、CUDA、DirectML、Mobile 等不同硬件加速方式。

使用模型构建器需要安装

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

安装完成后，您可以通过终端运行模型构建器脚本，执行模型格式和量化转换。


```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

了解相关参数

1. **model_name** 这是 Hugging Face 上的模型名称，如 microsoft/Phi-3.5-mini-instruct、microsoft/Phi-3.5-vision-instruct 等，也可以是您存储模型的路径

2. **path_to_output_folder** 量化转换后的保存路径

3. **execution_provider** 不同硬件加速支持，如 cpu、cuda、DirectML

4. **cache_dir_to_save_hf_files** 我们从 Hugging Face 下载模型并本地缓存的位置




***注意：*** <ul>虽然 onnxruntime 的生成式 AI 扩展处于预览状态，但已经集成到 Microsoft Olive，您也可以通过 Microsoft Olive 调用生成式 AI 扩展的模型构建器功能。</ul>

## **如何使用模型构建器量化 Phi-3.5**

模型构建器现支持 Phi-3.5 Instruct 和 Phi-3.5-Vision 的 ONNX 模型量化

### **Phi-3.5-Instruct**


**CPU 加速的 INT4 量化转换**


```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**CUDA 加速的 INT4 量化转换**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```



```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```


### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. 在终端设置环境

```bash

mkdir models

cd models 

```

2. 下载 microsoft/Phi-3.5-vision-instruct 至 models 文件夹
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. 请下载这些文件到您的 Phi-3.5-vision-instruct 文件夹

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)


4. 下载该文件到 models 文件夹
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. 进入终端

    支持 FP32 的 ONNX 转换


```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```


### **注意：**

1. 模型构建器目前支持 Phi-3.5-Instruct 和 Phi-3.5-Vision 的转换，但不支持 Phi-3.5-MoE

2. 想使用 ONNX 量化模型，可以通过 onnxruntime 的生成式 AI 扩展 SDK 使用

3. 我们需要更负责任的 AI，因此在模型量化转换后建议进行更有效的结果测试

4. 通过量化 CPU INT4 模型，我们可以将其部署到边缘设备，这有更好的应用场景，因此我们已完成了 Phi-3.5-Instruct 的 INT4 量化工作


## <strong>资源</strong>

1. 了解更多关于 onnxruntime 的生成式 AI 扩展 [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. onnxruntime 生成式 AI 扩展 GitHub 仓库 [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->