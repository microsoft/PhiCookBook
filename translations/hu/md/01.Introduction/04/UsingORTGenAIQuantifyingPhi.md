# **Phi család kvantálása a generatív AI bővítményekkel az onnxruntime-hoz**

## **Mi az a generatív AI bővítmény az onnxruntime-hoz**

Ezek a bővítmények segítenek generatív AI futtatásában az ONNX Runtime-tal ([https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)). Biztosítják a generatív AI ciklust ONNX modellekhez, beleértve az ONNX Runtime inferenciát, a logit feldolgozást, keresést és mintavételezést, valamint a KV cache kezelését. A fejlesztők hívhatják a magas szintű generate() metódust, vagy minden iterációt külön is futtathatnak, egy token generálásával egyszerre, és opcionálisan frissíthetik a generálási paramétereket a cikluson belül. Támogatja a greedy/beam keresést és a TopP, TopK mintavételezést token sorozatok generálásához, valamint beépített logit feldolgozást, mint az ismétlési büntetések. Egyedi pontozás is könnyen hozzáadható.

Alkalmazási szinten C++/C#/Python nyelven építhetsz alkalmazásokat a generatív AI bővítmények segítségével az onnxruntime-hoz. Modell szinten finomhangolt modellek összevonására és kapcsolódó kvantitatív telepítési munkák elvégzésére használható.


## **Phi-3.5 kvantálása a generatív AI bővítményekkel az onnxruntime-hoz**

### **Támogatott modellek**

A generatív AI bővítmények támogatják a Microsoft Phi, Google Gemma, Mistral, Meta LLaMA modellek kvantálási átalakítását.


### **Model Builder a generatív AI bővítményekben az onnxruntime-hoz**

A Model Builder nagyban felgyorsítja az optimalizált és kvantált ONNX modellek létrehozását, melyek az ONNX Runtime generate() API-val futnak.

A Model Builder segítségével a modellt INT4, INT8, FP16, FP32 formátumba kvantálhatod, és kombinálhatod különféle hardveres gyorsítási módszerekkel, például CPU, CUDA, DirectML, Mobile stb.

A Model Builder használatához telepítened kell

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

Telepítés után a terminálból futtathatod a Model Builder szkriptet a modell formátumának és kvantálásának konvertálásához.


```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

Az érintett paraméterek megértése

1. **model_name** Ez a modell Hugging Face-en, például microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct stb. Lehet a modell elérési útja is.

2. **path_to_output_folder** Kvantált konverzió mentési útvonala

3. **execution_provider** Különböző hardveres gyorsítás támogatása, mint cpu, cuda, DirectML

4. **cache_dir_to_save_hf_files** A modellt a Hugging Face-ről töltjük le és helyileg cache-eljük




***Megjegyzés:*** <ul>Bár a generatív AI bővítmények az onnxruntime-hoz előzetes verzióban vannak, be lettek építve a Microsoft Olive-ba, és a Generative AI extensions for onnxruntime Model Builder funkciókat a Microsoft Olive-on keresztül is hívhatod.</ul>

## **Hogyan használd a Model Buildert a Phi-3.5 kvantálásához**

A Model Builder jelenleg támogatja az ONNX modell kvantálását Phi-3.5 Instruct és Phi-3.5-Vision modellekhez

### **Phi-3.5-Instruct**


**CPU gyorsított kvantált INT 4 konverzió**


```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**CUDA gyorsított kvantált INT 4 konverzió**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```



```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```


### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. Környezet beállítása a terminálban

```bash

mkdir models

cd models 

```

2. Töltsd le a microsoft/Phi-3.5-vision-instruct modellt a models mappába
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. Kérjük, töltsd le ezeket a fájlokat a Phi-3.5-vision-instruct mappádba

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)


4. Töltsd le ezt a fájlt a models mappába
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. Menj a terminálba

    ONNX támogatás FP32-vel konvertálva


```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```


### **Megjegyzés:**

1. A Model Builder jelenleg támogatja a Phi-3.5-Instruct és Phi-3.5-Vision átalakítását, de nem a Phi-3.5-MoE-t

2. Az ONNX kvantált modellt a Generative AI extensions for onnxruntime SDK-n keresztül használhatod

3. Felelős AI-t is figyelembe kell vennünk, ezért a modell kvantálási átalakítása után javasolt hatékonyabb eredményteszteket végezni

4. A CPU INT4 modell kvantálásával elérhető az Edge Deviceokra történő telepítés, amely jobb alkalmazási forgatókönyveket kínál, így a Phi-3.5-Instruct INT4 körüli kvantálása befejeződött


## **Források**

1. Tudj meg többet a Generative AI extensions for onnxruntime-ról [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Generative AI extensions for onnxruntime GitHub tárhely [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->