<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3bb9f5c926673593287eddc3741226cb",
  "translation_date": "2025-05-09T14:51:45+00:00",
  "source_file": "md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md",
  "language_code": "hr"
}
-->
## **Kako koristiti Model Builder za kvantizaciju Phi-3.5**

Model Builder sada podržava kvantizaciju ONNX modela za Phi-3.5 Instruct i Phi-3.5-Vision

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

### **Napomena:**

1. Model Builder trenutno podržava konverziju Phi-3.5-Instruct i Phi-3.5-Vision, ali ne i Phi-3.5-MoE

2. Da biste koristili ONNX kvantizirani model, možete ga koristiti preko Generative AI extensions for onnxruntime SDK-a

3. Potrebno je razmotriti odgovorniji pristup AI-u, pa se nakon kvantizacije modela preporučuje provesti detaljnije testiranje rezultata

4. Kvantizacijom CPU INT4 modela možemo ga implementirati na Edge uređaje, što pruža bolje scenarije primjene, stoga smo završili Phi-3.5-Instruct u INT 4 verziji

## **Resursi**

1. Saznajte više o Generative AI extensions for onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Generative AI extensions for onnxruntime GitHub repozitorij [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**Odricanje od odgovornosti**:  
Ovaj dokument preveden je korištenjem AI usluge za prijevod [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo postići točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati službenim i autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakve nesporazume ili kriva tumačenja koja proizlaze iz korištenja ovog prijevoda.