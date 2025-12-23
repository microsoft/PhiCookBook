<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3bb9f5c926673593287eddc3741226cb",
  "translation_date": "2025-12-22T02:11:22+00:00",
  "source_file": "md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md",
  "language_code": "kn"
}
-->
# **onnxruntime‌ಗಳಿಗಾಗಿ Generative AI ವಿಸ್ತರಣೆಗಳನ್ನು ಬಳಸಿಕೊಂಡು Phi ಕುಟುಂಬವನ್ನು ಕ್ವಾಂಟೈಸ್ ಮಾಡುವುದು**

## **onnxruntime‌ಗಾಗಿ Generative AI ವಿಸ್ತರಣೆಗಳು ಎಂದರೇನು**

ಈ ವಿಸ್ತರಣೆಗಳು ONNX Runtime ( [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)) ಮೂಲಕ ಜನರೇಟಿವ್ AI ಅನ್ನು ಚಾಲನೆ ಮಾಡಲು ಸಹಾಯ ಮಾಡುತ್ತವೆ. ಇದು ONNX ಮಾದರಿಗಳಿಗಾಗಿ ಜನರೇಟಿವ್ AI ಲೂಪ್ ಅನ್ನು ಒದಗಿಸುತ್ತದೆ, ಇದರಲ್ಲಿ ONNX Runtime ನಲ್ಲಿ ಇನ್ಫರೆನ್ಸ್, logits ಪ್ರೊಸೆಸಿಂಗ್, ಶೋಧನೆ ಮತ್ತು ಸ್ಯಾಂಪಲಿಂಗ್, ಮತ್ತು KV ಕೆಚ್ ನಿರ್ವಹಣೆ ಸೇರಿದಂತೆ ಸಾಧನಗಳು ಸೇರಿವೆ. ಡೆವಲಪರ್‌ಗಳು ಉನ್ನತ ಮಟ್ಟದ generate() ವಿಧಾನವನ್ನು ಕರೆಮಾಡಬಹುದು, ಅಥವಾ ಮಾದರಿಯ ಪ್ರತಿಯೊಂದು ಇಟರೇಶನ್ ಅನ್ನು ಲೂಪ್‌ನಲ್ಲಿ ನಡೆಸಿ, ಒಂದೊಂದು ಟೋಕನ್ ಅನ್ನು ಸಮಯಕ್ಕೆ ತಯಾರಿಸಿ, ಮತ್ತು ಆಯ್ಕೆಯಾಗಿ ಲೂಪಿನ ಒಳಗೆ ಜನರೇಷನ್ ಪರಾಮೀಟರ್‌ಗಳನ್ನು ಅಪ್ಡೇಟ್ ಮಾಡಬಹುದು.ಲೂಪ್.It greedy/beam ಶೋಧನೆ ಮತ್ತು TopP, TopK ಸ್ಯಾಂಪಲಿಂಗ್ ಮೂಲಕ ಟೋಕನ್ ಸರಣಿಗಳನ್ನು生成ಗೊಳಿಸಲು ಮತ್ತು ಪುನರಾವೃತ್ತಿ ದಂಡನೆಗಳಂಥ ನಿರ್ಮಿತ logits ಪ್ರೊಸೆಸಿಂಗ್ ಅನ್ನು ಬೆಂಬಲಿಸುತ್ತದೆ. ನೀವು ಸುಲಭವಾಗಿ ಕಸ್ಟಮ್ ಸ್ಕೋರಿಂಗ್ ಅನ್ನು ಕೂಡ ಸೇರಿಸಬಹುದು.

ಅಪ್ಲಿಕೇಶನ್ ಮಟ್ಟದಲ್ಲಿ, ನೀವು C++/ C# / Python ಬಳಸಿ Generative AI extensions for onnxruntime ಅನ್ನು ಬಳಸಿ ಆಪ್ಲಿಕೇಶನ್‌ಗಳನ್ನು ನಿರ್ಮಿಸಬಹುದು. ಮಾದರಿ ಮಟ್ಟದಲ್ಲಿ, ನೀವು ಅದನ್ನು ಫೈನ್‑ಟ್ಯೂನ್ಡ್ ಮಾದರಿಗಳನ್ನು ಮರ್ಜ್ ಮಾಡಲು ಮತ್ತು ಸಂಬಂಧಿತ ಪ್ರಮಾಣಾತ್ಮಕ ಡಿಪ್ಲಾಯ್‌ಮೆಂಟ್ ಕೆಲಸಗಳನ್ನು ಮಾಡಲು ಬಳಸಬಹುದು.

## **Generative AI extensions for onnxruntime ಮೂಲಕ Phi-3.5 ಅನ್ನು ಕ್ವಾಂಟೈಸಿಂಗ್ ಮಾಡುವುದು**

### **ಬೆಂಬಲಿತ ಮಾದರಿಗಳು**

Generative AI extensions for onnxruntime Microsoft Phi , Google Gemma, Mistral, Meta LLaMA ರ ಕ್ವಾಂಟೈಜೇಷನ್ ಪರಿವರ್ತನೆಗೆ ಬೆಂಬಲ ನೀಡುತ್ತವೆ。

### **Generative AI extensions for onnxruntime ನಲ್ಲಿ Model Builder**

Model Builder ONNX Runtime generate() API ಜೊತೆ ಕಾರ್ಯನಿರ್ವಹಿಸುವ ಆಪ್ಟಿಮೈಸ್ ಮಾಡಿದ ಮತ್ತು ಕ್ವಾಂಟೈಸ್ ಮಾಡಲಾದ ONNX ಮಾದರಿಗಳನ್ನು ಸೃಷ್ಟಿಸುವ ಕಾರ್ಯವನ್ನು ವೇಗಗೊಳಿಸುತ್ತದೆ.

Model Builder ಮೂಲಕ, ನೀವು ಮಾದರಿಯನ್ನು INT4, INT8, FP16, FP32 ಗೆ ಕ್ವಾಂಟೈಸು ಮಾಡಬಹುದು, ಮತ್ತು CPU, CUDA, DirectML, Mobile ಮುಂತಾದ ವಿಭಿನ್ನ ಹಾರ್ಡ್‌ವೇರ್ ಆಕ್ಸಲರೇಶನ್ ವಿಧಾನಗಳನ್ನು ಸಂಯೋಜಿಸಬಹುದು.

Model Builder ಬಳಸಲು, ನೀವು ಇನ್ಸ್‌ಟಾಲ್ ಮಾಡುವ ಅಗತ್ಯವಿದೆ

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

ಇನ್ಸ್ಟಾಲೇಶನ್ ನಂತರ, ನೀವು ಟರ್ಮಿನಲ್‌ನಿಂದ Model Builder ಸ್ಕ್ರಿಪ್ಟ್ ಅನ್ನು ರನ್ ಮಾಡಿ ಮಾದರಿ ಫಾರ್ಮ್ಯಾಟ್ ಮತ್ತು ಕ್ವಾಂಟೈಜೇಷನ್ ಪರಿವರ್ತನೆಯನ್ನು ನಡೆಸಬಹುದು.


```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

ಸಂಬಂಧಿತ ಪರಾಮೀಟರ್ಗಳನ್ನು ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳಿ

1. **model_name** ಇದು Hugging face上的 ಮಾದರಿ, ಉದಾಹರಣೆಗೆ microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct ಇತ್ಯಾದಿ. ಅದು ನೀವು ಮಾದರಿಯನ್ನು ಸಂಗ್ರಹಿಸಿರುವ ಪಾಥ್ ಆಗಿರಬಹುದಾಗಿದೆ

2. **path_to_output_folder** ಕ್ವಾಂಟೈಜ್ಡ್ ಪರಿವರ್ತನೆಯನ್ನು ಉಳಿಸುವ ಪಥ

3. **execution_provider** ವಿವಿಧ ಹಾರ್ಡ್‌ವೇರ್ ಆಕ್ಸಲರೇಶನ್ ಬೆಂಬಲ, ಉದಾಹರಣೆಗೆ cpu, cuda, DirectML

4. **cache_dir_to_save_hf_files** ನಾವು Hugging face ನಿಂದ ಮಾದರಿಯನ್ನು ಡೌನ್‌ಲೋಡ್ ಮಾಡಿ ಸ್ಥಳೀಯವಾಗಿ ಕ್ಯಾಶೆ ಮಾಡುತ್ತೇವೆ




***Note：*** <ul>ಯಾವುದೋ Generative AI extensions for onnxruntime ಪ್ರಿವ್ಯೂದಲ್ಲಿ ಇದ್ದರೂ, ಅವುಗಳನ್ನು Microsoft Olive ಗೆ ಸೇರಿಸಲಾಗಿದೆ, ಮತ್ತು ನೀವು Generative AI extensions for onnxruntime Model Builder ಫಂಕ್ಷನ್‌ಗಳನ್ನು Microsoft Olive ಮೂಲಕವೂ ಕರೆಮಾಡಬಹುದು.</ul>

## **Model Builder ಅನ್ನು ಬಳಸಿಕೊಂಡು Phi-3.5 ಅನ್ನು ಕ್ವಾಂಟೈಸಿಂಗ್ ಹೇಗೆ ಮಾಡುವುದು**

Model Builder ಈಗ Phi-3.5 Instruct ಮತ್ತು Phi-3.5-Vision ಗಾಗಿ ONNX ಮಾದರಿ ಕ್ವಾಂಟೈಜೇಷನ್ ಅನ್ನು ಬೆಂಬಲಿಸುತ್ತದೆ

### **Phi-3.5-Instruct**


**CPU ಆಕ್ಸಲರೇಟೆಡ್ ಕ್ವಾಂಟೈಸ್ ಮಾಡಿದ INT 4 ಪರಿವರ್ತನೆ**


```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**CUDA ಆಕ್ಸಲರೇಟೆಡ್ ಕ್ವಾಂಟೈಸ್ ಮಾಡಿದ INT 4 ಪರಿವರ್ತನೆ**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```



```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```


### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. ಟರ್ಮಿನಲ್‌ನಲ್ಲಿ ಪರಿಸರವನ್ನು ಸೆಟ್ ಮಾಡಿ

```bash

mkdir models

cd models 

```

2. models ಫೋಲ್ಡರ್‌ನಲ್ಲಿ microsoft/Phi-3.5-vision-instruct ಅನ್ನು ಡೌನ್‌ಲೋಡ್ ಮಾಡಿ
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. ದಯವಿಟ್ಟು ಈ ಫೈಲ್‌ಗಳನ್ನು ನಿಮ್ಮ Phi-3.5-vision-instruct ಫೋಲ್ಡರ್‌ಗೆ ಡೌನ್‌ಲೋಡ್ ಮಾಡಿ

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)


4. ಈ ಫೈಲ್ ಅನ್ನು models ಫೋಲ್ಡರ್‌ಗೆ ಡೌನ್‌ಲೋಡ್ ಮಾಡಿ
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. ಟರ್ಮಿನಲ್‌ಗೆ ಹೋಗಿ

    Convert ONNX support with FP32


```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```


### **Note：**

1. Model Builder ಪ್ರಸ್ತುತ Phi-3.5-Instruct ಮತ್ತು Phi-3.5-Vision ರ ಪರಿವರ್ತನೆಯನ್ನು ಬೆಂಬಲಿಸುತ್ತದೆ, ಆದರೆ Phi-3.5-MoE ಅನ್ನು ಬೆಂಬಲಿಸುವುದಿಲ್ಲ

2. ONNX ನ ಕ್ವಾಂಟೈಸ್ ಮಾಡಿದ ಮಾದರಿಯನ್ನು ಬಳಸಲು, ನೀವು ಅದನ್ನು Generative AI extensions for onnxruntime SDK ಮುಖಾಂತರ ಬಳಸಬಹುದು

3. ನಮಗೆ ಹೆಚ್ಚಿನ ಜವಾಬ್ದಾರಿ ಯುಕ್ತ AI ಬಗ್ಗೆ ಪರಿಗಣನೆ ಅಗತ್ಯವಿದೆ, ಆದ್ದರಿಂದ ಮಾದರಿ ಕ್ವಾಂಟೈಜೇಷನ್ ಪರಿವರ್ತನೆಯ ನಂತರ ಹೆಚ್ಚಿನ ಪ್ರಯೋಜನಕಾರಿ ಫಲಿತಾಂಶ ಟೆಸ್ಟಿಂಗ್ ನಡೆಸುವದನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ

4. CPU INT4 ಮಾದರಿಯನ್ನು ಕ್ವಾಂಟೈಸ್ ಮಾಡುವ ಮೂಲಕ, ನಾವು ಅದನ್ನು ಎಜ್ ಡಿವೈಸ್‌ಗಳಿಗೆ ಡಿಪ್ಲಾಯ್ ಮಾಡಬಹುದು, ಇದು ಉತ್ತಮ ಅಪ್ಲಿಕೇಶನ್ سينಾರಿಓಗಳನ್ನು ನೀಡುತ್ತದೆ, ಆದ್ದರಿಂದ ನಾವು Phi-3.5-Instruct ಅನ್ನು INT 4 ಸುತ್ತಲೂ ಪೂರ್ಣಗೊಳಿಸಿದ್ದೇವೆ


## **Resources**

1. onnxruntimeಗಾಗಿ Generative AI ವಿಸ್ತರಣೆಗಳನ್ನು ಕುರಿತು ಇನ್ನಷ್ಟು ತಿಳಿಯಿರಿ [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Generative AI extensions for onnxruntime GitHub Repo [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
ಅಸ್ವೀಕಾರ:
ಈ ದಸ್ತಾವೇಜನ್ನು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಮೂಲಕ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯೆಂದು ಬಯಸುತ್ತಿದ್ದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ತಪ್ಪುಗಳು ಅಥವಾ ಅಶುದ್ಧತೆಗಳು ಇರಬಹುದೆಂದನ್ನು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ದಸ್ತಾವೇಜನ್ನು ಅದರ ಮೂಲ ಭಾಷೆಯಲ್ಲಿ ಅಧಿಕೃತ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಮಹತ್ವದ ಮಾಹಿತಿಗಾಗಿ ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಗೊಳ್ಳುವಿಕೆಗಳಿಗಾಗೋ ಅಥವಾ ಅಯೋಗ್ಯವಾದ ವಿವರಣೆಗೆಗಾಗೋ ನಾವು ಹೊಣೆಗಾರರಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->