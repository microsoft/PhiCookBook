<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3bb9f5c926673593287eddc3741226cb",
  "translation_date": "2025-07-16T22:25:54+00:00",
  "source_file": "md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md",
  "language_code": "ro"
}
-->
## **Cum să folosești Model Builder pentru cuantizarea Phi-3.5**

Model Builder suportă acum cuantizarea modelelor ONNX pentru Phi-3.5 Instruct și Phi-3.5-Vision

### **Phi-3.5-Instruct**

**Conversie accelerată pe CPU pentru cuantizarea INT4**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**Conversie accelerată pe CUDA pentru cuantizarea INT4**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. Configurează mediul în terminal

```bash

mkdir models

cd models 

```

2. Descarcă microsoft/Phi-3.5-vision-instruct în folderul models  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. Te rugăm să descarci aceste fișiere în folderul tău Phi-3.5-vision-instruct

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. Descarcă acest fișier în folderul models  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. Accesează terminalul

    Convertește suportul ONNX cu FP32

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **Notă:**

1. Model Builder suportă în prezent conversia pentru Phi-3.5-Instruct și Phi-3.5-Vision, dar nu și pentru Phi-3.5-MoE

2. Pentru a folosi modelul cuantizat ONNX, îl poți utiliza prin SDK-ul Generative AI extensions for onnxruntime

3. Trebuie să avem în vedere un AI mai responsabil, așa că după conversia modelului prin cuantizare, este recomandat să se efectueze teste mai eficiente ale rezultatelor

4. Prin cuantizarea modelului CPU INT4, îl putem implementa pe dispozitive Edge, care oferă scenarii de aplicare mai bune, astfel am finalizat Phi-3.5-Instruct în jurul INT4

## **Resurse**

1. Află mai multe despre Generative AI extensions for onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Repozitoriu GitHub Generative AI extensions for onnxruntime [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.