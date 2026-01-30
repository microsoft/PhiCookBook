## **如何使用 Model Builder 对 Phi-3.5 进行量化**

Model Builder 现已支持 Phi-3.5 Instruct 和 Phi-3.5-Vision 的 ONNX 模型量化。

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

2. 在 models 文件夹中下载 microsoft/Phi-3.5-vision-instruct  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. 请将以下文件下载到你的 Phi-3.5-vision-instruct 文件夹中

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. 将此文件下载到 models 文件夹  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. 进入终端

    使用 FP32 转换 ONNX 支持

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **注意：**

1. Model Builder 目前支持 Phi-3.5-Instruct 和 Phi-3.5-Vision 的转换，但不支持 Phi-3.5-MoE

2. 要使用 ONNX 的量化模型，可以通过 Generative AI extensions for onnxruntime SDK 来使用

3. 我们需要更多地考虑负责任的 AI，因此模型量化转换后，建议进行更有效的结果测试

4. 通过量化 CPU INT4 模型，我们可以将其部署到边缘设备，拥有更好的应用场景，因此我们已完成 Phi-3.5-Instruct 的 INT4 量化

## **资源**

1. 了解更多关于 Generative AI extensions for onnxruntime 的信息  
[https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Generative AI extensions for onnxruntime GitHub 仓库  
[https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**免责声明**：  
本文件使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始文件的母语版本应被视为权威来源。对于重要信息，建议使用专业人工翻译。我们不对因使用本翻译而产生的任何误解或误释承担责任。