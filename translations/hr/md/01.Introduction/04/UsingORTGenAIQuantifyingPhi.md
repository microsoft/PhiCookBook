# **Kvantizacija Phi obitelji pomoću Generative AI ekstenzija za onnxruntime**

## **Što su Generative AI ekstenzije za onnxruntime**

Ove ekstenzije pomažu vam u pokretanju generativne AI s ONNX Runtime ([https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)). One pružaju generativni AI ciklus za ONNX modele, uključujući izvršavanje s ONNX Runtime, obradu logita, pretraživanje i uzorkovanje, te upravljanje KV cacheom. Programeri mogu pozvati visoko razinu generate() metodu ili pokrenuti svaku iteraciju modela u petlji, generirajući jedan token u isto vrijeme i po potrebi ažurirajući parametre generiranja unutar petlje. Podržava greedy/beam pretraživanje i TopP, TopK uzorkovanje za generiranje nizova tokena, kao i ugrađenu obradu logita poput kazni za ponavljanje. Također lako možete dodati vlastito ocjenjivanje.

Na razini aplikacije možete koristiti Generative AI ekstenzije za onnxruntime za izradu aplikacija u C++/C#/Python. Na razini modela, možete ih koristiti za spajanje fino podešenih modela i obavljanje povezane kvantitativne implementacije.


## **Kvantizacija Phi-3.5 pomoću Generative AI ekstenzija za onnxruntime**

### **Podržani modeli**

Generative AI ekstenzije za onnxruntime podržavaju konverziju kvantizacije Microsoft Phi, Google Gemma, Mistral, Meta LLaMA.


### **Izrada modela u Generative AI ekstenzijama za onnxruntime**

Izrada modela znatno ubrzava stvaranje optimiziranih i kvantiziranih ONNX modela koji rade s ONNX Runtime generate() API-jem.

Putem Izrade modela možete kvantizirati model u INT4, INT8, FP16, FP32 i kombinirati različite metode hardverskog ubrzanja poput CPU, CUDA, DirectML, Mobile i dr.

Za korištenje Izrade modela potrebno je instalirati

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

Nakon instalacije, možete pokrenuti skriptu Izrade modela iz terminala da izvršite konverziju formata i kvantizacije modela.


```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

Razumijevanje relevantnih parametara

1. **model_name** Ovo je model na Hugging faceu, kao microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct itd. Također može biti putanja gdje pohranjujete model

2. **path_to_output_folder** Putanja spremanja kvantizirane konverzije

3. **execution_provider** Različite podrške za hardversko ubrzanje, poput cpu, cuda, DirectML

4. **cache_dir_to_save_hf_files** Model preuzimamo s Hugging facea i keširamo lokalno




***Napomena：*** <ul>Iako su Generative AI ekstenzije za onnxruntime u pregledu, one su uključene u Microsoft Olive, te također možete pozvati funkcije Izrade modela Generative AI ekstenzija za onnxruntime putem Microsoft Olive.</ul>

## **Kako koristiti Izradu modela za kvantizaciju Phi-3.5**

Izrada modela sada podržava kvantizaciju ONNX modela za Phi-3.5 Instruct i Phi-3.5-Vision

### **Phi-3.5-Instruct**


**CPU ubrzana konverzija kvantiziranog INT 4**


```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**CUDA ubrzana konverzija kvantiziranog INT 4**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```



```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```


### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. Postavite okruženje u terminalu

```bash

mkdir models

cd models 

```

2. Preuzmite microsoft/Phi-3.5-vision-instruct u mapu models
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. Molimo preuzmite ove datoteke u vašu Phi-3.5-vision-instruct mapu

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)


4. Preuzmite ovu datoteku u mapu models
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. Idite u terminal

    Konvertirajte ONNX podršku s FP32


```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```


### **Napomena：**

1. Izrada modela trenutno podržava konverziju Phi-3.5-Instruct i Phi-3.5-Vision, ali ne i Phi-3.5-MoE

2. Za korištenje ONNX kvantiziranog modela, možete ga koristiti kroz Generative AI ekstenzije za onnxruntime SDK

3. Moramo više razmotriti odgovornu AI, stoga se nakon konverzije kvantizacije modela preporučuje provesti učinkovitije testiranje rezultata

4. Kvantizacijom CPU INT4 modela, možemo ga implementirati na Edge uređaj, koji ima bolje scenarije primjene, tako da smo dovršili Phi-3.5-Instruct oko INT 4


## **Resursi**

1. Saznajte više o Generative AI ekstenzijama za onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Generative AI ekstenzije za onnxruntime GitHub Repo [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->