<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dcb656f3d206fc4968e236deec5d4384",
  "translation_date": "2025-12-22T01:28:20+00:00",
  "source_file": "md/01.Introduction/03/MLX_Inference.md",
  "language_code": "ml"
}
-->
# **Apple MLX ഫ്രെയിംവർക്കിൽ Phi-3 ഉപയോഗിച്ച് ഇന്‍ഫെറൻസ്**

## **MLX ഫ്രെയിംവർക്കാണ് എന്ത്**

MLX Apple സിലിക്കണിൽ മെഷീൻ ലേണിംഗ് ഗവേഷണത്തിനുള്ള ഒരു അരേ ഫ്രെയിംവർക്കാണ്, ഇത് Apple machine learning research അവതരിപ്പിക്കുന്നു.

MLX മെഷീൻ ലേണിംഗ് ഗവേഷകരால் മെഷീൻ ലേണിംഗ് ഗവേഷകര്ക്ക് രൂപകൽപ്പന ചെയ്തതാണ്. ഫ്രെയിംവർക്കിന്റെ ഉദ്ദേശം ഉപയോക്തൃ സുഹൃദായകമായിട്ടാണ്, എന്നിരിക്കിലും മോഡലുകൾ ട്രെയിൻ ചെയ്യാനും ഡിപ്പ്ലോയ് ചെയ്യാനും കാര്യക്ഷമമാക്കാൻ დიზൈനിംഗ് ചെയ്തിരിക്കുന്നു. ഫ്രെയിംവർക്കിന്റെ രൂപകൽപ്പനയും ആശയപരമായി സിമ്പിൾ ആണ്. പുതിയ ആശയങ്ങൾ വേഗത്തിൽ പരീക്ഷിക്കാൻ ഗവേഷകർ MLX എളുപ്പത്തിൽ വികസിപ്പിച്ച് മെച്ചപ്പെടുത്താൻ ഞങ്ങൾ ഉദ്ദേശിക്കുന്നു.

MLX മുഖേന Apple Silicon ഉപകരണങ്ങളിൽ LLMകൾ വേഗത്തിലാക്കാൻ കഴിയും, കൂടാതെ മോഡലുകൾ ലോക്കലായും വളരെ സൗകര്യപ്രദമായ രീതിയിൽ ഓടിക്കരണം ചെയ്യാവുന്നതാണ്.

## **MLX ഉപയോഗിച്ച് Phi-3-mini നെ ഇൻഫെറൻസ് ചെയ്യൽ**

### **1. Set up you MLX env**

1. Python 3.11.x
2. Install MLX Library


```bash

pip install mlx-lm

```

### **2. Running Phi-3-mini in Terminal with MLX**


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

ഫലം (എന്റെ പരിസ്ഥിതി Apple M1 Max,64GB ആണ്) ഇങ്ങനെ ആണ്

![ടർമിനൽ](../../../../../translated_images/01.5cf57df8f7407cf9.ml.png)

### **3. Quantizing Phi-3-mini with MLX in Terminal**


```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3-mini-4k-instruct

```

***കുറിപ്പ്：*** മോഡൽ mlx_lm.convert ഉപയോഗിച്ച് ക്വാണ്ടൈസുചെയ്യാവുന്നതാണ്, ഡീഫോൾട്ട് ക്വാണ്ടൈസേഷൻ INT4 ആണ്. ഈ ഉദാഹരണം Phi-3-mini നെ INT4 ആക്കെയാണ്.

മോഡൽ mlx_lm.convert ഉപയോഗിച്ച് ക്വാണ്ടൈസുചെയ്യാവുന്നതാണ്, ഡീഫോൾട്ട് ക്വാണ്ടൈസേഷൻ INT4 ആണ്. ഈ ഉദാഹരണം Phi-3-mini നെ INT4 ആയി ക്വാണ്ടൈസ് ചെയ്യാനുള്ളതാണ്. ക്വാണ്ടൈസേഷൻ കഴിഞ്ഞ് ഇത് ഡീഫോൾട്ട് ഡയറക്ടറിയായ ./mlx_modelൽ സൂക്ഷിക്കപ്പെടും

ഞങ്ങൾ ടർമിനലിൽ നിന്ന് MLX ഉപയോഗിച്ച് ക്വാണ്ടൈസ് ചെയ്ത മോഡൽ പരിശോധിക്കാവുന്നതാണ്


```bash

python -m mlx_lm.generate --model ./mlx_model/ --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

ഫലം ഈർപ്പം ആണ്

![INT4](../../../../../translated_images/02.7b188681a8eadbc1.ml.png)


### **4. Running Phi-3-mini with MLX in Jupyter Notebook**


![നോട്ട്ബുക്ക്](../../../../../translated_images/03.b9705a3a5aaa89f9.ml.png)

***കുറിപ്പ്:*** ദയവായി ഈ സാമ്പിൾ [ഈ ലിങ്കിൽ ക്ലിക്ക് ചെയ്യുക](../../../code/03.Inference/MLX/MLX_DEMO.ipynb)


## **Resources**

1. Apple MLX ഫ്രെയിംവർക്കിനെക്കുറിച്ച് അറിയുക [https://ml-explore.github.io](https://ml-explore.github.io/mlx/build/html/index.html)

2. Apple MLX GitHub റിപ്പൊസിറ്ററി [https://github.com/ml-explore](https://github.com/ml-explore)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
ഡിസ്ക്ലെയിമർ:
ഈ രേഖ [Co-op Translator](https://github.com/Azure/co-op-translator) എന്ന AI വിവർത്തന സേവനം ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്ക് ശ്രമിച്ചെങ്കിലും, യാന്ത്രിക വിവർത്തനങ്ങളിൽ പിഴവുകൾ അല്ലെങ്കിൽ തെറ്റുകൾ ഉണ്ടായിരിക്കാമെന്ന് ദയവായി ശ്രദ്ധിക്കുക. മാതൃഭാഷയിലുള്ള ഒറിജിനൽ രേഖ ശക്തമായ ഔദ്യോഗിക സ്രോതസായി കരുതപ്പെടണം. നിർണായകമായ വിവരങ്ങൾക്ക് പ്രൊഫഷണൽ മനുഷ്യ വിവർത്തനം നിർദ്ദേശിക്കുന്നു. ഈ വിവർത്തനത്തിന്റെ ഉപയോഗത്തെ തുടർന്ന് ഉണ്ടാകുന്ന ഏതെങ്കിലും തെറ്റിദ്ധാരണങ്ങൾക്കോ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കോ ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->