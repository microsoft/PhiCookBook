# **Kvantovanie rodiny Phi pomocou Generatívnych AI rozšírení pre onnxruntime**

## **Čo sú Generatívne AI rozšírenia pre onnxruntime**

Tieto rozšírenia vám pomáhajú spúšťať generatívnu AI s ONNX Runtime ([https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)). Poskytujú generatívnu AI slučku pre ONNX modely, vrátane inferencie pomocou ONNX Runtime, spracovania logitov, vyhľadávania a vzorkovania a správy KV cache. Vývojári môžu volať vysokoúrovňovú metódu generate(), alebo spúšťať každý krok modelu v slučke, generovať jeden token naraz a voliteľne aktualizovať parametre generovania v rámci slučky. Podporuje greedy/beam search a TopP, TopK vzorkovanie na generovanie sekvencií tokenov a zabudované spracovanie logitov ako penalizácie opakovania. Tiež môžete ľahko pridať vlastné hodnotenie.

Na úrovni aplikácie môžete použiť Generatívne AI rozšírenia pre onnxruntime na tvorbu aplikácií pomocou C++/ C# / Python. Na úrovni modelu môžete použiť toto na zlúčenie doladených modelov a vykonanie súvisiacej kvantitatívnej implementácie.


## **Kvantovanie Phi-3.5 s Generatívnymi AI rozšíreniami pre onnxruntime**

### **Podporované modely**

Generatívne AI rozšírenia pre onnxruntime podporujú konverziu kvantizácie Microsoft Phi, Google Gemma, Mistral, Meta LLaMA.


### **Tvorca modelov v Generatívnych AI rozšíreniach pre onnxruntime**

Tvorca modelov výrazne urýchľuje vytváranie optimalizovaných a kvantizovaných ONNX modelov, ktoré fungujú s ONNX Runtime generate() API.

Pomocou Tvorcu modelov môžete kvantizovať model na INT4, INT8, FP16, FP32 a kombinovať rôzne metódy hardvérovej akcelerácie ako CPU, CUDA, DirectML, Mobile a pod.

Na použitie Tvorcu modelov musíte nainštalovať

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

Po inštalácii môžete spustiť skript Tvorcu modelov z terminálu na vykonanie konverzie formátu modelu a kvantizácie.


```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

Pochopte príslušné parametre

1. **model_name** Toto je model na Hugging face, ako microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct a pod. Môže to byť aj cesta, kde máte uložený model.

2. **path_to_output_folder** Cesta na uloženie konvertovaného kvantizovaného modelu

3. **execution_provider** Podpora rôznych hardvérových akcelerácií ako cpu, cuda, DirectML

4. **cache_dir_to_save_hf_files** Model sťahujeme z Hugging face a ukladajú sa do cache lokálne




***Poznámka：*** <ul>Aj keď sú Generatívne AI rozšírenia pre onnxruntime v náhľadovej verzii, boli začlenené do Microsoft Olive a môžete tiež volať funkcie Tvorcu modelov Generatívnych AI rozšírení pre onnxruntime cez Microsoft Olive.</ul>

## **Ako použiť Tvorcu modelov na kvantovanie Phi-3.5**

Tvorca modelov teraz podporuje ONNX kvantizáciu modelov Phi-3.5 Instruct a Phi-3.5-Vision

### **Phi-3.5-Instruct**


**CPU akcelerovaná konverzia kvantizovaného INT4**


```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**CUDA akcelerovaná konverzia kvantizovaného INT4**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```



```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```


### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. Nastavte prostredie v termináli

```bash

mkdir models

cd models 

```

2. Stiahnite microsoft/Phi-3.5-vision-instruct do priečinka models
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. Stiahnite si prosím tieto súbory do vášho priečinka Phi-3.5-vision-instruct

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)


4. Stiahnite tento súbor do priečinka models
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. Prejdite do terminálu

    Konvertujte ONNX podporu s FP32


```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```


### **Poznámka：**

1. Tvorca modelov momentálne podporuje konverziu Phi-3.5-Instruct a Phi-3.5-Vision, ale nie Phi-3.5-MoE

2. Pre použitie ONNX kvantizovaného modelu ho môžete využívať cez SDK Generatívnych AI rozšírení pre onnxruntime

3. Musíme viac uvažovať o zodpovednej AI, preto po konverzii kvantizácie modelu sa odporúča vykonať efektívnejšie testovanie výsledkov

4. Kvantovaním CPU INT4 modelu ho môžeme nasadiť na Edge zariadenia, ktoré majú lepšie aplikačné scenáre, takže sme dokončili Phi-3.5-Instruct okolo INT4


## **Zdroje**

1. Viac informácií o Generatívnych AI rozšíreniach pre onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. GitHub repozitár Generatívnych AI rozšírení pre onnxruntime [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->