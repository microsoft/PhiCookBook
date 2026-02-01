# **Phi കുടുംബത്തെ Generative AI extensions for onnxruntime ഉപയോഗിച്ച് Quantizing ചെയ്യൽ**

## **Generative AI extensions for onnxruntime എന്താണെന്ന്**

ഈ എക്സ്ടൻഷൻങ്ങൾ ONNX Runtime ([https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)) ഉപയോഗിച്ച് ജനറേറ്റീവ് AI ഓടിക്കാൻ സഹായിക്കുന്നു. ഇത് ONNX മോഡलोंുമായി ജനറേറ്റീവ് AI ലൂപ്പ് പ്രദാനം ചെയ്യുന്നു, ONNX Runtime ഉപയോഗിച്ചുള്ള ഇൻഫറൻസ്, ലോജിറ്റ്സ് പ്രോസസ്സിംഗ്, sørch and sampling (മാറ്റമില്ല), and KV cache മാനേജ്മെന്റ് ഉൾപ്പെടെ. ഡവലപ്പർമാർക്ക് ഉയർന്ന നിലവാരത്തിലുള്ള generate() മെതോഡ് വിളിക്കാനോ, മോഡലിന്റെ ഓരോ ഇറ്ററേഷനും ലൂപിൽ റൺ ചെയ്ത് ഒരു ടോക്കൺ ഓരോ തവണ ജനറേറ്റ് ചെയ്യാനും, ആവശ്യമായ പക്ഷം ലൂപിനുള്ളിലാണ് ജനറേഷൻ പാരാമീറ്ററുകൾ അപ്ഡേറ്റ് ചെയ്യാനും സാധിക്കും. ഇത് greedy/beam search നും TopP, TopK സാംപ്ലിങ്ങിനും പിന്തുണ നൽകുന്നു, ടോക്കൺ സീക്വൻസുകൾ ജനറേറ്റ് ചെയ്യുന്നതിനും repetition penalties പോലെയുള്ള നിര്‍മ്മിത ലോജിറ്റ്സ് പ്രോസസ്സിംഗ് ഉൾക്കൊള്ളുന്നതിനും. നിങ്ങൾക്ക് എളുപ്പത്തിൽ കസ്റ്റം സ്കോറിംഗ് ചേർക്കാനും സാധിക്കും.

അപ്ലിക്കേഷൻ നിലയിൽ, C++/ C# / Python ഉപയോഗിച്ച് Generative AI extensions for onnxruntime ഉപയോഗിച്ച് അപ്ലിക്കേഷനുകൾ നിർമ്മിക്കാൻ കഴിയും. മോഡൽ നിലയിൽ, ഫൈൻ‑ട്യൂൺ ചെയ്യപ്പെട്ട മോഡലുകൾ മർജ് ചെയ്യാനും ബന്ധപ്പെട്ട ക്വാണ്ടിറ്റേറ്റീവ് ഡിപ്പ്ലോയ്മെന്റ് പ്രവർത്തനങ്ങൾ നടത്താനുമാണ് ഇത് ഉപയോഗിക്കാവുന്നത്.


## **Generative AI extensions for onnxruntime ഉപയോഗിച്ച് Phi-3.5 ക്വാണ്ടൈസിംഗ്**

### **ഒപ്പം പിന്തുണയുള്ള മോഡലുകൾ**

Generative AI extensions for onnxruntime Microsoft Phi, Google Gemma, Mistral, Meta LLaMA എന്നിവയുടെ ക്വാന്തൈസേഷൻ കണ്ട്വേഴ്ഷനുകൾക്ക് പിന്തുണ നൽകുന്നു。

### **Generative AI extensions for onnxruntime ഇൽ മോഡൽ ബിൽഡർ**

മോഡൽ ബിൽഡർ ONNX Runtime generate() API ഉപയോഗിച്ച് പ്രവർത്തിക്കുന്ന ഓപ്‌റ്റിമൈസ്ഡ്, ക്വാണ്ടൈസ്ഡ് ONNX മോഡലുകൾ സൃഷ്ടിക്കാൻ വളരെ വേഗം മുന്നോട്ട് നയിക്കുന്നു.

Model Builder വഴിയാണ് നിങ്ങൾ മോഡൽ INT4, INT8, FP16, FP32 എന്നിവയിലേക്ക് ക്വാണ്ടൈസുചെയ്യാനും CPU, CUDA, DirectML, Mobile തുടങ്ങിയ വിവിധ ഹാർഡ്‌വെയർ ആക്സിലറേഷൻ രീതികൾ സംയോജിപ്പിക്കാനുമുള്ള കഴിവ് ലഭിക്കുന്നത്.

Model Builder ഉപയോഗിക്കാൻ നിങ്ങൾക്ക് ഇൻസ്റ്റോൾ ചെയ്യേണ്ടതുണ്ട്

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

ഇൻസ്റ്റാൾ കഴിഞ്ഞാൽ, മോഡൽ ഫോർമാറ്റ് ಮತ್ತು ക്വാണ്ടൈസേഷൻ تبدیلی നടത്തുന്നതിന് ടർമിനലിൽ നിന്നു Model Builder സ്ക്രിപ്റ്റ് പ്രവർത്തിപ്പിക്കാം.


```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

സംബന്ധിച്ച പാരാമീറ്ററുകൾ മനസിലാക്കുക

1. **model_name** ഇത് Hugging Face上的 മോഡലാണ്, ഉദാഹരണത്തിന് microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct തുടങ്ങിയവ. അതുപോലെ നിങ്ങൾ മോഡൽ സേവ് ചെയ്തിരിക്കുന്ന പാതയേയും ഇത് ആയിരിക്കാൻ পারে

2. **path_to_output_folder** ക്വാണ്ടൈസ്ഡ് മാറ്റം സംരക്ഷിക്കേണ്ട പാത

3. **execution_provider** CPU, CUDA, DirectML പോലുള്ള വ്യത്യസ്ത ഹാർഡ്‌വെയർ ആക്സിലറേഷൻ പിന്തുണ

4. **cache_dir_to_save_hf_files** നാം Hugging Face മുതൽ മോഡൽ ഡൗൺലോഡ് ചെയ്ത് ലോക്കലായി കാഷെ ചെയ്യുന്നതിന് ഉപയോഗിക്കുന്ന ഡയറക്ടറി




***Note：*** <ul>Generative AI extensions for onnxruntime ഇപ്പോൾ പ്രിവ്യൂ ഘട്ടത്തിലാണ് എങ്കിലും, ഇവ Microsoft Olive-ലിൽ ഉൾക്കൊള്ളിച്ചിട്ടുണ്ട്, കൂടാതെ Generative AI extensions for onnxruntime Model Builder ഫങ്ഷനുകൾ Microsoft Olive വഴി വിളിക്കാനും കഴിയും.</ul>

## **Phi-3.5 ക്വാന്തൈസിംഗ് ചെയ്യുന്നതിന് Model Builder എങ്ങനെ ഉപയോഗിക്കാം**

Model Builder ഇപ്പോൾ Phi-3.5 Instruct and Phi-3.5-Vision നുള്ള ONNX മോഡൽ ക്വാന്തൈസേഷൻ പിന്തുണിക്കുന്നു

### **Phi-3.5-Instruct**


**CPU ആക്സിലറേറ്റഡ് Quantized INT 4 കൺവേഴ്ഷൻ**


```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**CUDA ആക്സിലറേറ്റഡ് Quantized INT 4 കൺവേഴ്ഷൻ**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```



```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```


### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. ടർമിനലിൽ പരിസ്ഥിതി സജ്ജമാക്കുക

```bash

mkdir models

cd models 

```

2. models ഫോൾഡറിൽ microsoft/Phi-3.5-vision-instruct ഡൗൺലോഡ് ചെയ്യുക
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. ദയവായി ഈ ഫയലുകൾ നിങ്ങളുടെ Phi-3.5-vision-instruct ഫോൾഡറിൽ ഡൗൺലോഡ് ചെയ്യുക

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)


4. ഈ ഫയൽ models ഫോൾഡറിലേക്ക് ഡൗൺലോഡ് ചെയ്യുക
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. ടെർമിനലിലേക്ക് പോകുക

    ONNX പിന്തുണ FP32 കൺവേർട്ട് ചെയ്യുക


```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```


### **നോട്ടുകൾ：**

1. Model Builder ഇപ്പോൾ Phi-3.5-Instruct మరియు Phi-3.5-Vision ന്റെ കൺവർഷനുകൾ പിന്തുണച്ചുകൊണ്ടേയുണ്ട്, Phi-3.5-MoE പിന്തുണയില്ല

2. ONNX ന്റെ ക്വാന്തൈസ്ഡ് മോഡൽ ഉപയോഗിക്കാൻ Generative AI extensions for onnxruntime SDK വഴി ഇത് ഉപയോഗിക്കാം

3. മറുപടി ഉത്തരവാദിത്വപരമായി പരിഗണിക്കാൻ കൂടുതൽ ശ്രദ്ധ വേണം, അതിനാൽ മോഡൽ ക്വാന്തൈസേഷൻ转换 കഴിഞ്ഞശേഷം കൂടുതൽ ഫലപരിശോധന നടത്താൻ ശിപാർശ ചെയ്യുന്നു

4. CPU INT4 മോഡൽ ക്വാന്തൈസ് ചെയ്ത് ഡിപ്പ്ലോയ്മെന്റ് എഡ്ജ് ഡിവൈസുകളിൽ നടത്താവുന്നതാണ്, ഇത് മികച്ച ഉപയോഗ സാഹചര്യമൊരുക്കുന്നു; അതിനാൽ ഞങ്ങൾ Phi-3.5-Instruct നുള്ള INT 4 ചുറ്റുപാട് പൂർത്തീകരിച്ചു


## **സമ്പദങ്ങൾ**

1. Generative AI extensions for onnxruntime കുറിച്ച് കൂടുതൽ അറിയാൻ [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Generative AI extensions for onnxruntime GitHub Repo [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
അസ്വീകാര്യതാ കുറിപ്പ്:
ഈ രേഖ AI വിവർത്തന സേവനമായ Co‑op Translator (https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. ഞങ്ങൾ ശരിയായ വിവർത്തനത്തിനായി ശ്രമിച്ചിട്ടുണ്ടെങ്കിലും, ഓട്ടോമേറ്റഡ് വിവർത്തനങ്ങളിൽ പിശകുകളോ തെറ്റായ വിവർത്തനങ്ങളോ ഉണ്ടായേക്കാമെന്ന് ദയവായി ശ്രദ്ധിക്കുക. മൂലഭാഷയിലെ അസൽ രേഖ പ്രാമാണികമായ ഉറവിടമായാണ് കണക്കാക്കേണ്ടത്. നിർണ്ണായകമായ വിവരങ്ങൾക്ക് പ്രൊഫഷണൽ മനുഷ്യവിവർത്തനം ശുപാർശ ചെയ്യപ്പെടുന്നു. ഈ വിവർത്തനത്തിന്റെ ഉപയോഗത്തിൽനിന്നുണ്ടാകുന്ന ഏതെങ്കിലും തെറ്റിദ്ധാരണകൾക്കും തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കും ഞങ്ങൾക്ക് ഉത്തരവാദിത്വം ബാധിക്കില്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->