<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3bb9f5c926673593287eddc3741226cb",
  "translation_date": "2025-07-16T22:24:58+00:00",
  "source_file": "md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md",
  "language_code": "hu"
}
-->
## **Hogyan használjuk a Model Builder-t a Phi-3.5 kvantálásához**

A Model Builder most támogatja az ONNX modell kvantálását a Phi-3.5 Instruct és Phi-3.5-Vision modellekhez.

### **Phi-3.5-Instruct**

**CPU gyorsított kvantált INT4 konverzió**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**CUDA gyorsított kvantált INT4 konverzió**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. Állítsd be a környezetet a terminálban

```bash

mkdir models

cd models 

```

2. Töltsd le a microsoft/Phi-3.5-vision-instruct modellt a models mappába  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. Kérlek, töltsd le ezeket a fájlokat a Phi-3.5-vision-instruct mappádba

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. Töltsd le ezt a fájlt a models mappába  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. Menj a terminálba

    Konvertáld az ONNX támogatást FP32-re

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **Megjegyzés:**

1. A Model Builder jelenleg támogatja a Phi-3.5-Instruct és Phi-3.5-Vision konverzióját, de nem támogatja a Phi-3.5-MoE-t

2. Az ONNX kvantált modellt a Generative AI extensions for onnxruntime SDK-n keresztül használhatod

3. Felelősebb AI megközelítés érdekében a modell kvantálás utáni átalakítás után ajánlott alaposabb eredménytesztelést végezni

4. A CPU INT4 modell kvantálásával az Edge eszközökre is telepíthető, ami jobb alkalmazási lehetőségeket kínál, így a Phi-3.5-Instruct INT4 körüli kvantálása elkészült

## **Források**

1. Tudj meg többet a Generative AI extensions for onnxruntime-ról [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Generative AI extensions for onnxruntime GitHub tárhely [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén szakmai, emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.