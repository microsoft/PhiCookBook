# **Quantizing Phi Family wit Generative AI extensions for onnxruntime**

## **Wetin be Generative AI extensions for onnxruntime**

These extensions dey help you run generative AI with ONNX Runtime( [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)). E dey provide the generative AI loop for ONNX models, including inference with ONNX Runtime, logits processing, search and sampling, and KV cache management. Developers fit call one high level generate() method, or run each iteration of the model in a loop, dey generate one token at a time, and optionally update generation parameters inside the loop. E get support for greedy/beam search and TopP, TopK sampling to generate token sequences and built-in logits processing like repetition penalties. You fit also easily add custom scoring.

For application level, you fit use Generative AI extensions for onnxruntime to build applications using C++/ C# / Python. For model level, you fit use am to merge fine-tuned models and do related quantitative deployment work.


## **Quantizing Phi-3.5 wit Generative AI extensions for onnxruntime**

### **Support Models**

Generative AI extensions for onnxruntime dey support quantization conversion for Microsoft Phi, Google Gemma, Mistral, Meta LLaMA。

### **Model Builder in Generative AI extensions for onnxruntime**

Model Builder dey greatly accelerate the creation of optimized and quantized ONNX models wey go run with the ONNX Runtime generate() API.

Through Model Builder, you fit quantize the model to INT4, INT8, FP16, FP32, and combine different hardware acceleration methods such as CPU, CUDA, DirectML, Mobile, etc.

To use Model Builder you need to install

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

After installation, you fit run the Model Builder script from the terminal to perform model format and quantization conversion.


```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

Make you sabi the relevant parameters

1. **model_name** Na the model for Hugging Face, such as microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct, etc. E fit also be the path wey you store the model

2. **path_to_output_folder** Path wey dem go save the quantized conversion

3. **execution_provider** Different hardware acceleration wey e support, such as cpu, cuda, DirectML

4. **cache_dir_to_save_hf_files** We download the model from Hugging Face and cache am locally




***Note：*** <ul>Even though Generative AI extensions for onnxruntime dey for preview, dem don incorporate am into Microsoft Olive, and you fit also call Generative AI extensions for onnxruntime Model Builder functions through Microsoft Olive.</ul>

## **How to use Model Builder to quantize Phi-3.5**

Model Builder now dey support ONNX model quantization for Phi-3.5 Instruct and Phi-3.5-Vision

### **Phi-3.5-Instruct**


**CPU accelerated conversion of quantized INT 4**


```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**CUDA accelerated conversion of quantized INT 4**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```



```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```


### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. Set environment in terminal

```bash

mkdir models

cd models 

```

2. Download microsoft/Phi-3.5-vision-instruct in models folder
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. Abeg download these files to your Phi-3.5-vision-instruct folder

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)


4. Download this file to models folder
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. Go to terminal

    Convert ONNX to support FP32


```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```


### **Note：**

1. Model Builder right now dey support the conversion of Phi-3.5-Instruct and Phi-3.5-Vision, but e no support Phi-3.5-MoE

2. To use ONNX quantized model, you fit use am through Generative AI extensions for onnxruntime SDK

3. We need to consider responsible AI more, so after the model quantization conversion, e dey recommended make you do more effective result testing

4. By quantizing the CPU INT4 model, we fit deploy am to Edge Device, wey get better application scenarios, so we don complete Phi-3.5-Instruct around INT 4


## **Resources**

1. Find out more about Generative AI extensions for onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Generative AI extensions for onnxruntime GitHub Repo [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Disclaimer:
Dis document don translate with AI translation service wey name na Co-op Translator (https://github.com/Azure/co-op-translator). Even though we dey try make am correct, abeg note say automated translations fit get errors or no too accurate. The original document for im native language na di main authoritative source. If na important mata, e better make professional human translator check am. We no go responsible for any misunderstanding or wrong interpretation wey fit come from this translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->