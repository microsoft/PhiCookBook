# **Kuongeza Ukubwa wa Familia ya Phi kwa kutumia nyongeza za AI Zinazozalisha kwa onnxruntime**

## **Nini ni nyongeza za AI Zinazozalisha kwa onnxruntime**

Nyongeza hizi zinakusaidia kuendesha AI zinazozalisha kwa ONNX Runtime( [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)). Zinatoa mzunguko wa AI zinazozalisha kwa modeli za ONNX, ikijumuisha utambuzi kwa ONNX Runtime, usindikaji wa logits, utafutaji na sampuli, na usimamizi wa cache ya KV. Waendelezaji wanaweza kuita mbinu ya juu generate(), au kuendesha kila mzunguko wa modeli katika mzunguko, wakizalisha token moja kwa wakati, na hiari kusasisha vigezo vya kizazi ndani ya mzunguko. Ina msaada wa utafutaji wa wivu/beam na sampuli za TopP, TopK kuzalisha mfululizo wa tokeni na usindikaji wa logits uliojengwa kama adhabu za marudio. Unaweza pia kuongeza alama za kitaalamu kwa urahisi.

Kiwango cha programu, unaweza kutumia nyongeza za AI Zinazozalisha kwa onnxruntime kujenga programu kwa kutumia C++/ C# / Python. Kiwango cha modeli, unaweza kuitumia kuunganisha modeli zilizofanyiwa mazoezi maalum na kufanya kazi zinazohusiana na usambazaji wa kiasi.


## **Kuweka Ukubwa wa Phi-3.5 kwa kutumia nyongeza za AI Zinazozalisha kwa onnxruntime**

### **Modeli Zinazounga Mkono**

Nyongeza za AI Zinazozalisha kwa onnxruntime zinaunga mkono uongofu wa kuwekeza wa Microsoft Phi, Google Gemma, Mistral, Meta LLaMA。


### **Mtengenezaji wa Modeli katika nyongeza za AI Zinazozalisha kwa onnxruntime**

Mtengenezaji wa modeli huongeza kasi sana katika kuunda modeli za ONNX zilizoboreshwa na kuwekewa ukubwa zinazoendesha kwa API ya generate() ya ONNX Runtime.

Kupitia Mtengenezaji wa Modeli, unaweza kuwekeza ukubwa wa modeli kuwa INT4, INT8, FP16, FP32, na kuunganisha mbinu tofauti za kuongeza kasi ya vifaa kama CPU, CUDA, DirectML, Simu, n.k.

Ili kutumia Mtengenezaji wa Modeli unahitaji kufunga

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

Baada ya ufungaji, unaweza kuendesha script ya Mtengenezaji wa Modeli kutoka kwa terminal kufanya mabadiliko ya muundo wa modeli na uongofu wa kuwekeza ukubwa.


```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

Elewa vigezo vinavyohusiana

1. **model_name** Hii ni modeli kwenye Hugging face, kama microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct, n.k. Pia inaweza kuwa njia ambayo unahifadhi modeli

2. **path_to_output_folder** Njia ya kuhifadhi uongofu wa kuweka ukubwa

3. **execution_provider** Msaada wa vifaa vya kuongeza kasi tofauti, kama cpu, cuda, DirectML

4. **cache_dir_to_save_hf_files** Tunapakua modeli kutoka Hugging face na kuihifadhi kwa mda mfupi eneo la mahali




***Kumbuka：*** <ul>Ingawa nyongeza za AI Zinazozalisha kwa onnxruntime bado ziko katika awamu ya majaribio, zimejumuishwa katika Microsoft Olive, na pia unaweza kuita kazi za Mtengenezaji wa Modeli wa nyongeza za AI Zinazozalisha kwa onnxruntime kupitia Microsoft Olive.</ul>

## **Jinsi ya kutumia Mtengenezaji wa Modeli kuwekeza ukubwa wa Phi-3.5**

Mtengenezaji wa Modeli sasa unaunga mkono kuweka ukubwa wa modeli za ONNX kwa Phi-3.5 Instruct na Phi-3.5-Vision

### **Phi-3.5-Instruct**


**Uongofu ulioboreshwa na CPU wa kuwekeza ukubwa INT 4**


```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**Uongofu ulioboreshwa na CUDA wa kuwekeza ukubwa INT 4**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```



```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```


### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. Weka mazingira kwenye terminal

```bash

mkdir models

cd models 

```

2. Pakua microsoft/Phi-3.5-vision-instruct kwenye folda ya modeli
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. Tafadhali pakua faili hizi kwenye folda yako ya Phi-3.5-vision-instruct

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)


4. Pakua faili hii kwenye folda ya modeli
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. Nenda kwenye terminal

    Geuza msaada wa ONNX kwa FP32


```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```


### **Kumbuka：**

1. Mtengenezaji wa Modeli kwa sasa unaunga mkono uongofu wa Phi-3.5-Instruct na Phi-3.5-Vision, lakini si Phi-3.5-MoE

2. Ili kutumia modeli iliyowekwa ukubwa wa ONNX, unaweza kuitumia kupitia SDK ya nyongeza za AI Zinazozalisha kwa onnxruntime

3. Tunahitaji kuzingatia AI yenye uwajibikaji zaidi, hivyo baada ya uongofu wa kuwekeza ukubwa wa modeli, inapendekezwa kufanya majaribio ya matokeo yenye ufanisi zaidi

4. Kwa kuwekeza ukubwa wa modeli ya CPU INT4, tunaweza kuisambaza kwenye Kifaa cha Edge, ambacho kina matukio bora ya matumizi, hivyo tumemaliza Phi-3.5-Instruct kuhusu INT 4


## **Rasilimali**

1. Jifunze zaidi kuhusu nyongeza za AI Zinazozalisha kwa onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Hazina ya GitHub ya nyongeza za AI Zinazozalisha kwa onnxruntime [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->