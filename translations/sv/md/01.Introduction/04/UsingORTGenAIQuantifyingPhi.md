# **Kvantisering av Phi-familjen med Generative AI-tillägg för onnxruntime**

## **Vad är Generative AI-tillägg för onnxruntime**

Dessa tillägg hjälper dig att köra generativ AI med ONNX Runtime( [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)). De tillhandahåller den generativa AI-loopen för ONNX-modeller, inklusive inferens med ONNX Runtime, logit-processning, sökning och sampling samt hantering av KV-cache. Utvecklare kan anropa en metod på hög nivå generate(), eller köra varje iteration av modellen i en loop, generera en token i taget och valfritt uppdatera generationsparametrar inom loopen. Det finns stöd för greedy/beam-sökning och TopP, TopK-sampling för att generera tokensekvenser samt inbyggd logit-processning som repetitionsstraff. Du kan också enkelt lägga till egna poängsättningar.

På applikationsnivå kan du använda Generative AI-tillägg för onnxruntime för att bygga applikationer med C++/C#/Python. På modelnivå kan du använda det för att slå ihop finjusterade modeller och utföra relaterat kvantitativt distributionsarbete.


## **Kvantisering av Phi-3.5 med Generative AI-tillägg för onnxruntime**

### **Stödda modeller**

Generative AI-tillägg för onnxruntime stödjer kvantiseringskonvertering av Microsoft Phi, Google Gemma, Mistral, Meta LLaMA.


### **Model Builder i Generative AI-tillägg för onnxruntime**

Model Builder påskyndar avsevärt skapandet av optimerade och kvantiserade ONNX-modeller som körs med ONNX Runtime generate() API.

Via Model Builder kan du kvantisera modellen till INT4, INT8, FP16, FP32, och kombinera olika hårdvaruaccelerationstekniker som CPU, CUDA, DirectML, Mobile, etc.

För att använda Model Builder behöver du installera

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

Efter installation kan du köra Model Builder-skriptet från terminalen för att utföra modellformat- och kvantiseringskonvertering.


```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

Förstå relevanta parametrar

1. **model_name** Detta är modellen på Hugging Face, som microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct, etc. Det kan också vara sökvägen där du lagrar modellen

2. **path_to_output_folder** Sökväg för sparande av kvantiserad konvertering

3. **execution_provider** Stöd för olika hårdvaruaccelerationer, som cpu, cuda, DirectML

4. **cache_dir_to_save_hf_files** Vi laddar ner modellen från Hugging Face och cachar den lokalt




***Notera：*** <ul>Även om Generative AI-tillägg för onnxruntime är i preview, har de integrerats i Microsoft Olive, och du kan också anropa Generative AI-tillägg för onnxruntime Model Builder-funktioner via Microsoft Olive.</ul>

## **Hur man använder Model Builder för kvantisering av Phi-3.5**

Model Builder stödjer nu kvantisering av ONNX-modeller för Phi-3.5 Instruct och Phi-3.5-Vision

### **Phi-3.5-Instruct**


**CPU-accelererad konvertering av kvantiserad INT 4**


```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**CUDA-accelererad konvertering av kvantiserad INT 4**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```



```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```


### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. Sätt miljön i terminalen

```bash

mkdir models

cd models 

```

2. Ladda ner microsoft/Phi-3.5-vision-instruct i mapp för modeller
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. Ladda ner dessa filer till din Phi-3.5-vision-instruct-mapp

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)


4. Ladda ner denna fil till modellmappen
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. Gå till terminalen

    Konvertera ONNX-stöd med FP32


```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```


### **Notera:**

1. Model Builder stödjer för närvarande konvertering av Phi-3.5-Instruct och Phi-3.5-Vision, men inte Phi-3.5-MoE

2. För att använda ONNXs kvantiserade modell kan du göra det via Generative AI-tillägg för onnxruntime SDK

3. Vi behöver tänka mer på ansvarsfull AI, så efter kvantiseringskonverteringen av modellen rekommenderas det att genomföra mer effektiv resultatutvärdering

4. Genom att kvantisera CPU INT4-modellen kan vi distribuera den till Edge-enheter, som har bättre användningsscenarier, så vi har färdigställt Phi-3.5-Instruct kring INT 4


## **Resurser**

1. Lär dig mer om Generative AI-tillägg för onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Generative AI-tillägg för onnxruntime GitHub Repo [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->