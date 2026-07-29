# **Kvadratizace rodiny Phi pomocí rozšíření Generative AI pro onnxruntime**

## **Co jsou rozšíření Generative AI pro onnxruntime**

Tato rozšíření vám pomáhají spouštět generativní AI s ONNX Runtime ([https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)). Poskytují generativní AI smyčku pro ONNX modely, včetně inference s ONNX Runtime, zpracování logits, vyhledávání a vzorkování a správy KV cache. Vývojáři mohou volat metodu generate() na vysoké úrovni, nebo spouštět každou iteraci modelu v cyklu, generovat jeden token za čas a volitelně aktualizovat parametry generování uvnitř smyčky. Podporuje greedy/beam search a TopP, TopK vzorkování pro generování posloupností tokenů a vestavěné zpracování logits, jako jsou penalizace opakování. Můžete také snadno přidat vlastní skórování.

Na aplikační úrovni můžete použít rozšíření Generative AI pro onnxruntime k vytváření aplikací v C++/ C# / Python. Na úrovni modelu je můžete použít k sloučení doladěných modelů a provádění související kvantitativní nasazovací práce.


## **Kvadratizace Phi-3.5 pomocí rozšíření Generative AI pro onnxruntime**

### **Podporované modely**

Rozšíření Generative AI pro onnxruntime podporují kvantovací konverzi Microsoft Phi, Google Gemma, Mistral, Meta LLaMA.


### **Model Builder v rozšířeních Generative AI pro onnxruntime**

Model Builder výrazně urychluje vytváření optimalizovaných a kvantovaných ONNX modelů, které běží s ONNX Runtime generate() API.

Pomocí Model Builderu můžete kvantizovat model na INT4, INT8, FP16, FP32 a kombinovat různé metody hardwarové akcelerace jako CPU, CUDA, DirectML, Mobile atd.

Pro použití Model Builderu musíte nainstalovat

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

Po instalaci můžete spustit skript Model Builder z terminálu pro provedení konverze formátu modelu a kvantizace.


```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

Pochopení souvisejících parametrů

1. **model_name** Toto je model na Hugging face, například microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct atd. Může to být také cesta, kde model uchováváte

2. **path_to_output_folder** Cesta pro uložení kvantované konverze

3. **execution_provider** Podpora různých hardwarových akcelerací, například cpu, cuda, DirectML

4. **cache_dir_to_save_hf_files** Stahujeme model z Hugging face a ukládáme ho do lokální cache




***Poznámka：*** <ul>Ačkoli jsou rozšíření Generative AI pro onnxruntime ve verzi preview, byla začleněna do Microsoft Olive a také můžete volat funkce Model Builder rozšíření Generative AI pro onnxruntime přes Microsoft Olive.</ul>

## **Jak používat Model Builder pro kvantizaci Phi-3.5**

Model Builder nyní podporuje kvantizaci ONNX modelů pro Phi-3.5 Instruct a Phi-3.5-Vision

### **Phi-3.5-Instruct**


**CPU akcelerovaná konverze kvantovaných INT 4**


```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**CUDA akcelerovaná konverze kvantovaných INT 4**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```



```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```


### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. Nastavte prostředí v terminálu

```bash

mkdir models

cd models 

```

2. Stáhněte microsoft/Phi-3.5-vision-instruct do složky models
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. Stáhněte tyto soubory do vaší složky Phi-3.5-vision-instruct

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)


4. Stáhněte tento soubor do složky models
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. Přejděte do terminálu

    Proveďte konverzi ONNX s podporou FP32


```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```


### **Poznámka：**

1. Model Builder momentálně podporuje konverzi Phi-3.5-Instruct a Phi-3.5-Vision, ale ne Phi-3.5-MoE

2. Pro použití kvantizovaného ONNX modelu ho můžete použít přes Generative AI extensions for onnxruntime SDK

3. Musíme se více zaměřit na odpovědnou AI, proto se doporučuje po konverzi modelu kvantizace provést efektivnější testování výsledků

4. Kvantizací CPU INT4 modelu ho můžeme nasadit na Edge zařízení, což má lepší aplikační scénáře, takže jsme dokončili Phi-3.5-Instruct kolem INT 4


## **Zdroje**

1. Naučte se více o rozšířeních Generative AI pro onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. GitHub repozitář Generative AI extensions for onnxruntime [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->