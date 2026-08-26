# **Kvantizacija Phi družine z uporabo Generative AI razširitev za onnxruntime**

## **Kaj so Generative AI razširitve za onnxruntime**

Te razširitve vam pomagajo zagnati generativno AI z ONNX Runtime ([https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)). Zagotavljajo generativno AI zanko za ONNX modele, vključno z inferenco z ONNX Runtime, obdelavo logistk, iskanjem in vzorčenjem ter upravljanjem KV predpomnilnika. Razvijalci lahko pokličejo visokonivojsko metodo generate(), ali pa izvajajo vsako iteracijo modela v zanki, generirajoč en žeton naenkrat in po želji posodabljajo parametre generacije znotraj zanke. Podpirajo pohlepno/beam iskanje in TopP, TopK vzorčenje za generiranje sekvenc žetonov ter vgrajeno obdelavo logistk, kot so kazni za ponavljanje. Prav tako lahko enostavno dodate uporabniško ocenjevanje.

Na ravni aplikacije lahko Generative AI razširitve za onnxruntime uporabite za izdelavo aplikacij v C++/ C# / Python. Na ravni modela jih lahko uporabite za združevanje vnaprej natreniranih modelov in opravljanje sorodnih količinskih nalog uvajanja.


## **Kvantizacija Phi-3.5 z Generative AI razširitvami za onnxruntime**

### **Podprti modeli**

Generative AI razširitve za onnxruntime podpirajo konverzijo kvantizacije Microsoft Phi, Google Gemma, Mistral, Meta LLaMA.


### **Graditelj modelov v Generative AI razširitvah za onnxruntime**

Graditelj modelov močno pospeši ustvarjanje optimiziranih in kvantiziranih ONNX modelov, ki tečejo z ONNX Runtime generate() API-jem.

Preko Graditelja modelov lahko model kvantizirate v INT4, INT8, FP16, FP32 ter kombinirate različne metode strojno pospešene izvedbe, kot so CPU, CUDA, DirectML, Mobile itd.

Za uporabo Graditelja modelov morate namestiti

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

Po namestitvi lahko Graditelj modelov zaženete preko terminala za izvedbo konverzije formata modela in kvantizacije.


```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

Razumevanje relevantnih parametrov

1. **model_name** To je model na Hugging Face, kot na primer microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct itd. Lahko je tudi pot, kjer hranite model.

2. **path_to_output_folder** Pot za shranjevanje kvantizirane konverzije.

3. **execution_provider** Podpora za različne strojne pospešitve, kot so cpu, cuda, DirectML.

4. **cache_dir_to_save_hf_files** Prenesemo model s Hugging Face in ga lokalno predpomnimo.




***Opomba:*** <ul>Čeprav so Generative AI razširitve za onnxruntime v predogledu, so bile vključene v Microsoft Olive, in lahko tudi pokličete funkcije Graditelja modelov Generative AI razširitev za onnxruntime preko Microsoft Olive.</ul>

## **Kako uporabiti Graditelj modelov za kvantizacijo Phi-3.5**

Graditelj modelov sedaj podpira ONNX kvantizacijo modelov za Phi-3.5 Instruct in Phi-3.5-Vision

### **Phi-3.5-Instruct**


**CPU pospešena konverzija kvantiziranega INT 4**


```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**CUDA pospešena konverzija kvantiziranega INT 4**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```



```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```


### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. Nastavite okolje v terminalu

```bash

mkdir models

cd models 

```

2. Prenesite microsoft/Phi-3.5-vision-instruct v mapo models
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. Prosimo prenesite te datoteke v vašo mapo Phi-3.5-vision-instruct

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)


4. Prenesite to datoteko v mapo models
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. Pojdite v terminal

    Pretvorite ONNX z podporo za FP32


```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```


### **Opomba:**

1. Graditelj modelov trenutno podpira konverzijo Phi-3.5-Instruct in Phi-3.5-Vision, ne pa Phi-3.5-MoE

2. Za uporabo ONNX kvantiziranega modela ga lahko uporabite preko Generative AI rozširitev za onnxruntime SDK

3. Potrebno je upoštevati bolj odgovorno AI, zato po konverziji kvantizacije modela priporočamo učinkovitejše testiranje rezultatov

4. S kvantizacijo CPU INT4 modela ga lahko uvedemo na Edge naprave, ki imajo boljše scenarije uporabe, tako smo zaključili Phi-3.5-Instruct okoli INT 4


## **Viri**

1. Izvedite več o Generative AI razširitvah za onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Generative AI razširitve za onnxruntime GitHub repozitorij [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->