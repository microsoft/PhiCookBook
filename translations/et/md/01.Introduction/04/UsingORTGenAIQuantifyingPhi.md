# **Phi perekonna kvantiseerimine Generative AI laienduste abil onnxruntime jaoks**

## **Mis on Generative AI laiendused onnxruntime jaoks**

Need laiendused aitavad teil käivitada generatiivset tehisintellekti ONNX Runtime'iga ([https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)). Need pakuvad generatiivse tehisintellekti tsüklit ONNX mudelite jaoks, sealhulgas järeldamist ONNX Runtime'iga, logitite töötlemist, otsingut ja valimist ning KV vahemälu haldamist. Arendajad saavad kasutada kõrgetasemelist generate() meetodit või käivitada mudeli iga iteratsiooni tsüklis, genereerides ühe tokeni korraga ja vajadusel värskendades genereerimise parameetreid tsükli sees. Toetatud on ahne/kiire otsing ja TopP, TopK valimine tokenite järjestuste genereerimiseks ning sisseehitatud logitite töötlemine, nagu korduste karistused. Samuti saate hõlpsasti lisada kohandatud hindamismeetodeid.

Rakenduse tasemel saate kasutada Generative AI laiendusi onnxruntime jaoks, et luua rakendusi C++/C#/Python keeles. Mudeli tasemel saate neid kasutada peenhäälestatud mudelite ühendamiseks ja seotud kvantitatiivse juurutamise tööde tegemiseks.

## **Phi-3.5 kvantiseerimine Generative AI laienduste abil onnxruntime jaoks**

### **Toetatud mudelid**

Generative AI laiendused onnxruntime jaoks toetavad Microsoft Phi, Google Gemma, Mistral, Meta LLaMA kvantiseerimise konversiooni.

### **Mudeli ehitaja Generative AI laiendustes onnxruntime jaoks**

Mudeli ehitaja kiirendab oluliselt optimeeritud ja kvantiseeritud ONNX mudelite loomist, mis töötavad ONNX Runtime generate() API-ga.

Mudeli ehitaja abil saate mudeli kvantiseerida INT4, INT8, FP16, FP32 formaati ja kombineerida erinevaid riistvarakiirenduse meetodeid, nagu CPU, CUDA, DirectML, Mobile jne.

Mudeli ehitaja kasutamiseks peate installima

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```
  
Pärast installimist saate terminalist käivitada Mudeli ehitaja skripti, et teostada mudeli formaadi ja kvantiseerimise konversiooni.

```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```
  
Mõistke asjakohaseid parameetreid:

1. **model_name** See on mudel Hugging Face'is, näiteks microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct jne. See võib olla ka tee, kus mudelit hoiate.

2. **path_to_output_folder** Kvantiseeritud konversiooni salvestamise tee.

3. **execution_provider** Erinevad riistvarakiirenduse toetused, nagu CPU, CUDA, DirectML.

4. **cache_dir_to_save_hf_files** Me laadime mudeli Hugging Face'ist alla ja salvestame selle lokaalselt vahemällu.

***Märkus:*** <ul>Kuigi Generative AI laiendused onnxruntime jaoks on eelvaates, on need integreeritud Microsoft Olive'i, ja saate ka Microsoft Olive'i kaudu kutsuda Generative AI laienduste Mudeli ehitaja funktsioone.</ul>

## **Kuidas kasutada Mudeli ehitajat Phi-3.5 kvantiseerimiseks**

Mudeli ehitaja toetab nüüd ONNX mudeli kvantiseerimist Phi-3.5 Instruct ja Phi-3.5-Vision jaoks.

### **Phi-3.5-Instruct**

**CPU kiirendatud kvantiseeritud INT4 konversioon**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```
  
**CUDA kiirendatud kvantiseeritud INT4 konversioon**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```
  

```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```
  

### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. Seadistage terminalis keskkond

```bash

mkdir models

cd models 

```
  
2. Laadige alla microsoft/Phi-3.5-vision-instruct mudelite kausta  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. Palun laadige need failid oma Phi-3.5-vision-instruct kausta:

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. Laadige see fail mudelite kausta:  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. Minge terminali

    Konverteerige ONNX tugi FP32-ga

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```
  

### **Märkus:**

1. Mudeli ehitaja toetab praegu Phi-3.5-Instruct ja Phi-3.5-Vision konversiooni, kuid mitte Phi-3.5-MoE.

2. ONNX kvantiseeritud mudeli kasutamiseks saate seda kasutada Generative AI laienduste SDK kaudu onnxruntime jaoks.

3. Peame arvestama vastutustundlikuma tehisintellektiga, seega pärast mudeli kvantiseerimise konversiooni on soovitatav läbi viia tõhusamaid tulemuste teste.

4. Kvantiseerides CPU INT4 mudeli, saame selle juurutada servaseadmetele, millel on paremad rakendussenaariumid, seega oleme lõpetanud Phi-3.5-Instruct INT4 ümber.

## **Ressursid**

1. Lisateave Generative AI laienduste kohta onnxruntime jaoks [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Generative AI laienduste GitHubi repo onnxruntime jaoks [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.