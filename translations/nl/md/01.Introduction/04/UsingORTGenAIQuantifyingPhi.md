# **Quantificeren van Phi-familie met Generative AI-extensies voor onnxruntime**

## **Wat zijn Generative AI-extensies voor onnxruntime**

Deze extensies helpen je generatieve AI uit te voeren met ONNX Runtime ([https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)). Het biedt de generatieve AI-lus voor ONNX-modellen, inclusief inferentie met ONNX Runtime, logitsverwerking, zoeken en sampling, en KV-cachebeheer. Ontwikkelaars kunnen een method op hoog niveau generate() aanroepen, of elke iteratie van het model in een lus uitvoeren, waarbij telkens één token wordt gegenereerd en optioneel generatieparameters binnen de lus worden bijgewerkt. Het ondersteunt greedy/beam search en TopP, TopK sampling om tokenreeksen te genereren en ingebouwde logitsverwerking zoals straf voor herhaling. Je kunt ook eenvoudig aangepaste scoring toevoegen.

Op applicatieniveau kun je Generative AI-extensies voor onnxruntime gebruiken om applicaties te bouwen met C++ / C# / Python. Op modelniveau kun je het gebruiken om fijn-afgestelde modellen samen te voegen en gerelateerd kwantitatief deploy-werk te doen.


## **Quantificeren van Phi-3.5 met Generative AI-extensies voor onnxruntime**

### **Ondersteunde Modellen**

Generative AI-extensies voor onnxruntime ondersteunen kwantisatieconversie van Microsoft Phi, Google Gemma, Mistral, Meta LLaMA.


### **Model Builder in Generative AI-extensies voor onnxruntime**

De model builder versnelt het creëren van geoptimaliseerde en gekwantiseerde ONNX-modellen die draaien met de ONNX Runtime generate() API aanzienlijk.

Via Model Builder kun je het model kwantiseren naar INT4, INT8, FP16, FP32, en verschillende hardwareversnellingsmethodes combineren zoals CPU, CUDA, DirectML, Mobile, enzovoort.

Om Model Builder te gebruiken moet je installeren

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

Na installatie kun je het Model Builder-script vanuit de terminal uitvoeren om model formaat- en kwantisatieconversies te doen.


```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

Begrijp de relevante parameters

1. **model_name** Dit is het model op Hugging Face, zoals microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct, etc. Het kan ook het pad zijn waar je het model opslaat.

2. **path_to_output_folder** Pad waar gekwantiseerde conversie wordt opgeslagen

3. **execution_provider** Verschillende hardwareversnellingsondersteuning, zoals cpu, cuda, DirectML

4. **cache_dir_to_save_hf_files** We downloaden het model van Hugging Face en cachen het lokaal




***Let op：*** <ul>Hoewel Generative AI-extensies voor onnxruntime in preview zijn, zijn ze geïntegreerd in Microsoft Olive, en je kunt ook functies van Generative AI-extensies voor onnxruntime Model Builder aanroepen via Microsoft Olive.</ul>

## **Hoe Model Builder te gebruiken voor kwantisatie van Phi-3.5**

Model Builder ondersteunt nu ONNX model kwantisatie voor Phi-3.5 Instruct en Phi-3.5-Vision

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

1. Stel de omgeving in in de terminal

```bash

mkdir models

cd models 

```

2. Download microsoft/Phi-3.5-vision-instruct naar de models-map
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. Download deze bestanden naar jouw Phi-3.5-vision-instruct map

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)


4. Download dit bestand naar de models-map
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. Ga naar de terminal

    Conversie ONNX ondersteuning met FP32


```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```


### **Let op：**

1. Model Builder ondersteunt momenteel de conversie van Phi-3.5-Instruct en Phi-3.5-Vision, maar niet Phi-3.5-MoE

2. Om het gekwantiseerde ONNX-model te gebruiken, kun je het via Generative AI-extensies voor onnxruntime SDK gebruiken

3. We moeten meer verantwoordelijk AI overwegen, dus na de kwantisatie van het model wordt aanbevolen om meer effectieve resultaat testen uit te voeren

4. Door het CPU INT4-model te kwantiseren, kunnen we het implementeren op Edge Devices, wat betere toepassingssituaties biedt, daarom hebben we Phi-3.5-Instruct rond INT4 voltooid


## **Hulpbronnen**

1. Leer meer over Generative AI-extensies voor onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Generative AI-extensies voor onnxruntime GitHub Repo [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->