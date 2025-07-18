<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3bb9f5c926673593287eddc3741226cb",
  "translation_date": "2025-07-16T22:22:47+00:00",
  "source_file": "md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md",
  "language_code": "nl"
}
-->
## **Hoe Model Builder te gebruiken voor het kwantiseren van Phi-3.5**

Model Builder ondersteunt nu ONNX-modelkwantisering voor Phi-3.5 Instruct en Phi-3.5-Vision

### **Phi-3.5-Instruct**

**CPU-versnelde conversie van gekwantiseerde INT4**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**CUDA-versnelde conversie van gekwantiseerde INT4**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. Stel de omgeving in de terminal in

```bash

mkdir models

cd models 

```

2. Download microsoft/Phi-3.5-vision-instruct in de map models  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. Download deze bestanden naar jouw Phi-3.5-vision-instruct map

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. Download dit bestand naar de map models  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. Ga naar de terminal

    Converteer ONNX-ondersteuning met FP32

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **Opmerking:**

1. Model Builder ondersteunt momenteel de conversie van Phi-3.5-Instruct en Phi-3.5-Vision, maar niet Phi-3.5-MoE

2. Om het gekwantiseerde ONNX-model te gebruiken, kun je dit doen via de Generative AI extensions voor onnxruntime SDK

3. We moeten meer verantwoordelijke AI overwegen, dus na de modelkwantisering wordt aanbevolen om grondiger resultaattesten uit te voeren

4. Door het CPU INT4-model te kwantiseren, kunnen we het op Edge Devices inzetten, wat betere toepassingsscenario’s biedt. Daarom hebben we Phi-3.5-Instruct rond INT4 afgerond

## **Bronnen**

1. Leer meer over Generative AI extensions voor onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Generative AI extensions voor onnxruntime GitHub Repo [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.