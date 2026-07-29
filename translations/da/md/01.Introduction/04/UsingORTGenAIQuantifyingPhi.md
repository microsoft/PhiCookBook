# **Kvantificering af Phi-familien ved brug af Generative AI-udvidelser til onnxruntime**

## **Hvad er Generative AI-udvidelser til onnxruntime**

Disse udvidelser hjælper dig med at køre generativ AI med ONNX Runtime ([https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)). De leverer den generative AI-løkke til ONNX-modeller, inklusive inferens med ONNX Runtime, logitsbehandling, søgning og sampling, samt KV-cachehåndtering. Udviklere kan kalde en høj-niveau generate() metode, eller køre hver iteration af modellen i en løkke, der genererer et token ad gangen, og valgfrit opdatere parametre for generering inde i løkken. Den understøtter greedy/beam-søgning og TopP, TopK-sampling til at generere tokensekvenser og indbygget logitsbehandling som gentagelsesstraf. Du kan også nemt tilføje brugerdefineret scoring.

På applikationsniveau kan du bruge Generative AI-udvidelser til onnxruntime til at bygge applikationer med C++/ C# / Python. På modelniveau kan du bruge det til at sammenflette finjusterede modeller og udføre relateret kvantitativ udrulningsarbejde.


## **Kvantificering af Phi-3.5 med Generative AI-udvidelser til onnxruntime**

### **Understøttede modeller**

Generative AI-udvidelser til onnxruntime understøtter kvantificeringskonvertering af Microsoft Phi, Google Gemma, Mistral, Meta LLaMA.


### **Model Builder i Generative AI-udvidelser til onnxruntime**

Model Builder accelererer betydeligt oprettelse af optimerede og kvantificerede ONNX-modeller, som kører med ONNX Runtime generate() API.

Gennem Model Builder kan du kvantificere modellen til INT4, INT8, FP16, FP32 og kombinere forskellige hardwareaccelerationsmetoder såsom CPU, CUDA, DirectML, Mobile osv.

For at bruge Model Builder skal du installere

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

Efter installation kan du køre Model Builder-scriptet fra terminalen for at udføre modelformat- og kvantificeringskonvertering.


```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

Forstå de relevante parametre

1. **model_name** Dette er modellen på Hugging face, såsom microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct osv. Det kan også være stien, hvor du opbevarer modellen

2. **path_to_output_folder** Gemningssti for kvantificeret konvertering

3. **execution_provider** Forskellig hardwareaccelerationsunderstøttelse, såsom cpu, cuda, DirectML

4. **cache_dir_to_save_hf_files** Vi downloader modellen fra Hugging face og cacher den lokalt




***Bemærk:*** <ul>Selvom Generative AI-udvidelser til onnxruntime er i preview, er de blevet indarbejdet i Microsoft Olive, og du kan også kalde Generative AI-udvidelser til onnxruntime Model Builder funktioner gennem Microsoft Olive.</ul>

## **Sådan bruger du Model Builder til kvantificering af Phi-3.5**

Model Builder understøtter nu ONNX-modelkvantificering for Phi-3.5 Instruct og Phi-3.5-Vision

### **Phi-3.5-Instruct**


**CPU-accelereret konvertering til kvantificeret INT 4**


```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**CUDA-accelereret konvertering til kvantificeret INT 4**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```



```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```


### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. Sæt miljø i terminalen

```bash

mkdir models

cd models 

```

2. Download microsoft/Phi-3.5-vision-instruct i models folder
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. Download venligst disse filer til din Phi-3.5-vision-instruct mappe

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)


4. Download denne fil til models folder
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. Gå til terminalen

    Konverter ONNX-support med FP32


```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```


### **Bemærk:**

1. Model Builder understøtter i øjeblikket konvertering af Phi-3.5-Instruct og Phi-3.5-Vision, men ikke Phi-3.5-MoE

2. For at bruge ONNX's kvantificerede model kan du bruge den via Generative AI-udvidelser til onnxruntime SDK

3. Vi skal tage mere ansvarlig AI i betragtning, så efter modelkvantificeringskonvertering anbefales det at udføre mere effektiv resultat-test

4. Ved at kvantificere CPU INT4-modellen kan vi implementere den på Edge Device, som har bedre anvendelsesscenarier, så vi har fuldført Phi-3.5-Instruct omkring INT 4


## **Ressourcer**

1. Lær mere om Generative AI-udvidelser til onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Generative AI-udvidelser til onnxruntime GitHub Repo [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->