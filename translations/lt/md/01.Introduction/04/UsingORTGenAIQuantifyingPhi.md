# **Kvantuojant Phi šeimą naudojant Generatyvios AI plėtinius onnxruntime**

## **Kas yra Generatyvios AI plėtiniai onnxruntime?**

Šie plėtiniai padeda vykdyti generatyviąją AI su ONNX Runtime ([https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)). Jie suteikia generatyvios AI ciklą ONNX modeliams, įskaitant išvadą su ONNX Runtime, logitų apdorojimą, paiešką ir mėginių ėmimą bei KV talpyklos valdymą. Kūrėjai gali naudoti aukšto lygio generate() metodą arba vykdyti kiekvieną modelio iteraciją cikle, generuodami po vieną žetoną ir, jei reikia, atnaujindami generavimo parametrus ciklo metu. Plėtiniai palaiko godų/šviesos spindulio paiešką, TopP, TopK mėginių ėmimą žetonų sekų generavimui ir įmontuotą logitų apdorojimą, pvz., pasikartojimo baudas. Taip pat lengvai galima pridėti individualų vertinimą.

Programų lygmenyje galite naudoti Generatyvios AI plėtinius onnxruntime, kad kurtumėte programas naudodami C++/C#/Python. Modelio lygmenyje galite juos naudoti, kad sujungtumėte pritaikytus modelius ir atliktumėte susijusius kiekybinius diegimo darbus.

## **Kvantuojant Phi-3.5 su Generatyvios AI plėtiniais onnxruntime**

### **Palaikomi modeliai**

Generatyvios AI plėtiniai onnxruntime palaiko kvantavimo konversiją Microsoft Phi, Google Gemma, Mistral, Meta LLaMA.

### **Modelio kūrėjas Generatyvios AI plėtiniuose onnxruntime**

Modelio kūrėjas labai pagreitina optimizuotų ir kvantuotų ONNX modelių kūrimą, kurie veikia su ONNX Runtime generate() API.

Naudodami Modelio kūrėją galite kvantuoti modelį į INT4, INT8, FP16, FP32 ir derinti skirtingus aparatūros pagreičio metodus, tokius kaip CPU, CUDA, DirectML, Mobile ir kt.

Norėdami naudoti Modelio kūrėją, turite įdiegti

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

Įdiegę galite paleisti Modelio kūrėjo skriptą iš terminalo, kad atliktumėte modelio formato ir kvantavimo konversiją.

```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

Supraskite susijusius parametrus:

1. **model_name** Tai yra modelis Hugging Face platformoje, pvz., microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct ir kt. Tai taip pat gali būti kelias, kuriame saugote modelį.

2. **path_to_output_folder** Kvantuotos konversijos išsaugojimo kelias.

3. **execution_provider** Skirtingų aparatūros pagreičio palaikymas, pvz., cpu, cuda, DirectML.

4. **cache_dir_to_save_hf_files** Mes atsisiunčiame modelį iš Hugging Face ir talpiname jį vietoje.

***Pastaba:***

## **Kaip naudoti Modelio kūrėją kvantuojant Phi-3.5**

Modelio kūrėjas dabar palaiko ONNX modelio kvantavimą Phi-3.5 Instruct ir Phi-3.5-Vision.

### **Phi-3.5-Instruct**

**CPU pagreitinta INT4 kvantavimo konversija**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**CUDA pagreitinta INT4 kvantavimo konversija**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. Nustatykite aplinką terminale

```bash

mkdir models

cd models 

```

2. Atsisiųskite microsoft/Phi-3.5-vision-instruct į modelių aplanką  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. Atsisiųskite šiuos failus į savo Phi-3.5-vision-instruct aplanką:

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. Atsisiųskite šį failą į modelių aplanką  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. Eikite į terminalą  

   Konvertuokite ONNX palaikymą su FP32

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **Pastaba:**

1. Modelio kūrėjas šiuo metu palaiko Phi-3.5-Instruct ir Phi-3.5-Vision konversiją, tačiau ne Phi-3.5-MoE.

2. Norėdami naudoti ONNX kvantuotą modelį, galite jį naudoti per Generatyvios AI plėtinius onnxruntime SDK.

3. Turime atsižvelgti į atsakingesnę AI, todėl po modelio kvantavimo konversijos rekomenduojama atlikti efektyvesnį rezultatų testavimą.

4. Kvantuodami CPU INT4 modelį, galime jį diegti Edge įrenginiuose, kurie turi geresnius taikymo scenarijus, todėl užbaigėme Phi-3.5-Instruct aplink INT4.

## **Ištekliai**

1. Sužinokite daugiau apie Generatyvios AI plėtinius onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Generatyvios AI plėtiniai onnxruntime GitHub Repo [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

---

**Atsakomybės atsisakymas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius naudojant šį vertimą.