## **Sådan bruger du Model Builder til at kvantisere Phi-3.5**

Model Builder understøtter nu ONNX-modelkvantisering for Phi-3.5 Instruct og Phi-3.5-Vision

### **Phi-3.5-Instruct**

**CPU-accelereret konvertering til kvantiseret INT4**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**CUDA-accelereret konvertering til kvantiseret INT4**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. Sæt miljøet op i terminalen

```bash

mkdir models

cd models 

```

2. Download microsoft/Phi-3.5-vision-instruct i models-mappen  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. Download venligst disse filer til din Phi-3.5-vision-instruct-mappe

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. Download denne fil til models-mappen  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. Gå til terminalen

    Konverter ONNX med FP32-understøttelse

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **Bemærk:**

1. Model Builder understøtter i øjeblikket konvertering af Phi-3.5-Instruct og Phi-3.5-Vision, men ikke Phi-3.5-MoE

2. For at bruge ONNX’s kvantiserede model kan du anvende den via Generative AI extensions for onnxruntime SDK

3. Vi skal tage mere ansvarlig AI i betragtning, så efter modelkvantiseringen anbefales det at udføre mere effektiv test af resultaterne

4. Ved at kvantisere CPU INT4-modellen kan vi implementere den på Edge-enheder, hvilket giver bedre anvendelsesscenarier, så vi har fuldført Phi-3.5-Instruct omkring INT4

## **Ressourcer**

1. Lær mere om Generative AI extensions for onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Generative AI extensions for onnxruntime GitHub Repo [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.