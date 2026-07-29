# **Kvantifisering av Phi-familien ved bruk av Generative AI-utvidelser for onnxruntime**

## **Hva er Generative AI-utvidelser for onnxruntime**

Disse utvidelsene hjelper deg med å kjøre generativ AI med ONNX Runtime ([https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)). De tilbyr den generative AI-løkken for ONNX-modeller, inkludert inferens med ONNX Runtime, logitsbehandling, søk og sampling, og KV cache-administrasjon. Utviklere kan kalle en høynivå generate() metode, eller kjøre hver iterasjon av modellen i en løkke, som genererer ett token om gangen, og valgfritt oppdatere generasjonsparametere inne i løkken. Den støtter greedy/beam search og TopP, TopK sampling for å generere tokensekvenser og innebygd logitsbehandling som repeteringsstraffer. Du kan også enkelt legge til egendefinert poengsetting.

På applikasjonsnivå kan du bruke Generative AI-utvidelser for onnxruntime til å bygge applikasjoner ved hjelp av C++/ C# / Python. På modellenivå kan du bruke det til å slå sammen finjusterte modeller og utføre relatert kvantitativ distribusjonsarbeid.


## **Kvantifisering av Phi-3.5 med Generative AI-utvidelser for onnxruntime**

### **Støttede modeller**

Generative AI-utvidelser for onnxruntime støtter kvantiseringskonvertering av Microsoft Phi, Google Gemma, Mistral, Meta LLaMA.


### **Modellbygger i Generative AI-utvidelser for onnxruntime**

Modellbyggeren akselererer i stor grad opprettelsen av optimaliserte og kvantiserte ONNX-modeller som kjører med ONNX Runtime generate() API.

Gjennom Modellbygger kan du kvantisere modellen til INT4, INT8, FP16, FP32, og kombinere forskjellige maskinvareakselerasjonsmetoder som CPU, CUDA, DirectML, Mobile, osv.

For å bruke Modellbygger må du installere

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

Etter installasjon kan du kjøre Modellbygger-skriptet fra terminalen for å utføre modellformat- og kvantiseringskonvertering.


```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

Forstå relevante parametere

1. **model_name** Dette er modellen på Hugging Face, som microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct, osv. Det kan også være banen der du lagrer modellen

2. **path_to_output_folder** Lagreplass for kvantisert konvertering

3. **execution_provider** Støtte for ulik maskinvareakselerasjon, som cpu, cuda, DirectML

4. **cache_dir_to_save_hf_files** Vi laster ned modellen fra Hugging Face og cacher den lokalt




***Merk:*** <ul>Selv om Generative AI-utvidelser for onnxruntime er i forhåndsvisning, er de inkorporert i Microsoft Olive, og du kan også kalle Generative AI-utvidelser for onnxruntime Modellbygger-funksjoner gjennom Microsoft Olive.</ul>

## **Hvordan bruke Modellbygger for å kvantisere Phi-3.5**

Modellbygger støtter nå ONNX-modellkvantisering for Phi-3.5 Instruct og Phi-3.5-Vision

### **Phi-3.5-Instruct**


**CPU-akselerert konvertering av kvantisert INT 4**


```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**CUDA-akselerert konvertering av kvantisert INT 4**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```



```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```


### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. Sett opp miljøet i terminalen

```bash

mkdir models

cd models 

```

2. Last ned microsoft/Phi-3.5-vision-instruct i models-mappen
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. Vennligst last ned disse filene til din Phi-3.5-vision-instruct-mappe

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)


4. Last ned denne filen til models-mappen
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. Gå til terminal

    Konverter ONNX-støtte med FP32


```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```


### **Merk:**

1. Modellbygger støtter for øyeblikket konvertering for Phi-3.5-Instruct og Phi-3.5-Vision, men ikke Phi-3.5-MoE

2. For å bruke ONNX sin kvantiserte modell, kan du bruke den gjennom Generative AI-utvidelser for onnxruntime SDK

3. Vi må ta mer ansvarlig AI i betraktning, så etter modellkvantiseringskonverteringen anbefales det å utføre mer effektive resultatstester

4. Ved å kvantisere CPU INT4-modellen kan vi distribuere den til Edge-enheter, som har bedre bruksområder, så vi har fullført Phi-3.5-Instruct rundt INT 4


## **Ressurser**

1. Lær mer om Generative AI-utvidelser for onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Generative AI-utvidelser for onnxruntime GitHub Repo [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->