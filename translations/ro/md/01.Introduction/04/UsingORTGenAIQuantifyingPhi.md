# **Cuantificarea Familiei Phi folosind extensii Generative AI pentru onnxruntime**

## **Ce sunt extensiile Generative AI pentru onnxruntime**

Aceste extensii vă ajută să rulați AI generativ cu ONNX Runtime ( [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)). Ele oferă bucla AI generativă pentru modelele ONNX, inclusiv inferența cu ONNX Runtime, procesarea logits, căutarea și eșantionarea, și gestionarea cache-ului KV. Dezvoltatorii pot apela metoda de nivel înalt generate(), sau pot rula fiecare iterație a modelului într-o buclă, generând câte un token pe rând, și opțional actualizând parametrii de generare în interiorul buclei. Are suport pentru căutare greedy/beam și eșantionare TopP, TopK pentru a genera secvențe de tokeni, precum și procesare încorporată a logits precum penalizări pentru repetiție. De asemenea, puteți adăuga cu ușurință scorare personalizată.

La nivelul aplicației, puteți folosi extensiile Generative AI pentru onnxruntime pentru a construi aplicații folosind C++/ C# / Python. La nivelul modelului, le puteți folosi pentru a combina modele ajustate fin și pentru a realiza lucrări conexe de implementare cantitativă.


## **Cuantificarea Phi-3.5 cu extensiile Generative AI pentru onnxruntime**

### **Modele suportate**

Extensiile Generative AI pentru onnxruntime suportă conversia cu cuantificare a Microsoft Phi, Google Gemma, Mistral, Meta LLaMA.


### **Constructorul de modele în extensiile Generative AI pentru onnxruntime**

Constructorul de modele accelerează considerabil crearea modelelor ONNX optimizate și cuantificate care rulează cu API-ul generate() al ONNX Runtime.

Prin Constructorul de modele, puteți cuantifica modelul la INT4, INT8, FP16, FP32 și combina diferite metode de accelerare hardware precum CPU, CUDA, DirectML, Mobile, etc.

Pentru a folosi Constructorul de modele trebuie să instalați

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

După instalare, puteți rula scriptul Constructor de modele din terminal pentru a efectua conversia formatului modelului și cuantificarea.


```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

Înțelegeți parametrii relevanți

1. **model_name** Acesta este modelul de pe Hugging face, cum ar fi microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct, etc. Poate fi de asemenea calea unde stocați modelul.

2. **path_to_output_folder** Calea de salvare a conversiei cuantificate

3. **execution_provider** Suport pentru diferite accelerări hardware, cum ar fi cpu, cuda, DirectML

4. **cache_dir_to_save_hf_files** Descărcăm modelul de pe Hugging face și îl stocăm în cache local




***Notă：*** <ul>Deși extensiile Generative AI pentru onnxruntime sunt în previzualizare, ele au fost incorporate în Microsoft Olive, iar funcțiile Constructorului de modele din extensiile Generative AI pentru onnxruntime pot fi apelate și prin Microsoft Olive.</ul>

## **Cum să folosiți Constructorul de modele pentru cuantificarea Phi-3.5**

Constructorul de modele suportă acum cuantificarea modelelor ONNX pentru Phi-3.5 Instruct și Phi-3.5-Vision

### **Phi-3.5-Instruct**


**Conversie accelerată CPU a cuantificării INT 4**


```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**Conversie accelerată CUDA a cuantificării INT 4**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```



```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```


### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. Setați mediul în terminal

```bash

mkdir models

cd models 

```

2. Descărcați microsoft/Phi-3.5-vision-instruct în folderul models
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. Vă rugăm să descărcați aceste fișiere în folderul Phi-3.5-vision-instruct

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)


4. Descărcați acest fișier în folderul models
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. Mergeți la terminal

Convertiți suportul ONNX cu FP32


```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```


### **Notă：**

1. Constructorul de modele suportă în prezent conversia Phi-3.5-Instruct și Phi-3.5-Vision, dar nu și Phi-3.5-MoE

2. Pentru a folosi modelul cuantificat ONNX, îl puteți utiliza prin SDK-ul extensiilor Generative AI pentru onnxruntime

3. Trebuie să avem o responsabilitate crescută față de AI, deci după conversia prin cuantificare a modelului, este recomandat să efectuați teste mai eficiente ale rezultatelor

4. Prin cuantificarea modelului CPU INT4, îl putem implementa pe dispozitive Edge, care au scenarii de aplicare mai bune, astfel am finalizat Phi-3.5-Instruct în jurul INT 4


## **Resurse**

1. Aflați mai multe despre extensiile Generative AI pentru onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Repozitoriu GitHub pentru extensiile Generative AI pentru onnxruntime [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->