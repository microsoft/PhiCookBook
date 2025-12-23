<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1ff728038c4f554b660a36b76cbdd6e",
  "translation_date": "2025-12-22T00:41:40+00:00",
  "source_file": "md/01.Introduction/03/overview.md",
  "language_code": "ml"
}
-->
Phi-3-mini എന്ന സാഹചര്യത്തില്‍, ഇൻഫെരെൻസ് എന്നത് മോഡൽ ഉപയോഗിച്ച് ഇൻപുട്ട് ഡേറ്റയുടെ അടിസ്ഥാനത്തിൽ പ്രവചനങ്ങൾ നടത്തുകയോ ഔട്ട്പുട്ടുകൾ സൃഷ്‌ടിക്കുകയോ ചെയ്യുന്നതിനുള്ള പ്രക്രിയയെ സൂചിപ്പിക്കുന്നു. Phi-3-mini-യും അതിന്റെ ഇൻഫെരെൻസ് ശേഷികളുമായുള്ള കൂടുതൽ വിശദാംശങ്ങൾ ഞാൻ ഇവിടെ നൽകുന്നു.

Phi-3-mini Microsoft പുറത്തിറക്കിയ Phi-3 ശ്രേണിയിലെ മോഡലുകളുടെ ഭാഗമാണ്. ഈ മോഡലുകൾ Small Language Models (SLMs) ഉപയോഗിക്കുമ്പോൾ സാധ്യമാകുന്ന കാര്യങ്ങളെ പുതുതായി നിർവചിക്കാൻ രൂപകൽപ്പന ചെയ്തതാണ്. 

ഇവിടെ Phi-3-mini-യും അതിന്റെ ഇൻഫെറെൻസ് ശേഷികളുമിലെ ചില പ്രധാന നൊക്കുകൾ കൊടുത്തിരിക്കുന്നു:

## **Phi-3-mini Overview:**
- Phi-3-mini-യ്ക്ക് 3.8 ബില്യൺ പാരാമീറ്ററുകൾ ഉണ്ട്.
- ഇത് പരമ്പരാഗത കംപ്യൂട്ടിംഗ് ഉപകരണങ്ങളിലെയും മൊബൈൽ ഉപകരണങ്ങളും IoT ഉപകരണങ്ങൾ പോലെയുള്ള എജ് ഡിവൈസുകളിലെയും പ്രവർത്തിക്കാനുള്ള ശേഷിയുണ്ട്.
- Phi-3-mini റിലീസ് ചെയ്തことで വ്യക്തികൾക്കും ഏർപ്രൈസുകൾക്കും വിവിധ ഹാർഡ്‌വെയർ ഡിവൈസുകളിലേക്ക്, പ്രത്യേകിച്ച് ശ്രമസാധ്യവും നിഷ്ടമായ പരിതസ്ഥിതികളിൽ SLM-കൾ ഡിപ്ലോയ് ചെയ്യാൻ സാധിക്കും.
- ഇത് പരമ്പരാഗത PyTorch ഫോർമാറ്റും gguf ഫോർമാറ്റിന്റെ ക്വാണ്ടൈസ്ഡ് പതിപ്പും ONNX ആധാരമാക്കിയ ക്വാണ്ടൈസ്ഡ് പതിപ്പും ഉൾപ്പെടെ വിവിധ മോഡൽ ഫോർമാറ്റുകൾ കവർ ചെയ്യുന്നു.

## **Accessing Phi-3-mini:**
Phi-3-mini ആക്‌സസ് ചെയ്യാൻ Copilot ആപ്ലിക്കേഷനിൽ [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) ഉപയോഗിക്കാം. Semantic Kernel സാധാരണയായി Azure OpenAI Service, Hugging Face-യിലെ open-source മോഡലുകൾ, കൂടാതെ ലോക്കൽ മോഡലുകളുമായും പൊരുത്തപ്പെടുന്നു.
ക്വാണ്ടൈസ്ഡ് മോഡലുകൾ കോൾ ചെയ്യാൻ [Ollama](https://ollama.com) അല്ലെങ്കിൽ [LlamaEdge](https://llamaedge.com) ഉപയോഗിക്കാം. Ollama വ്യക്തിഗത ഉപഭോക്താക്കൾക്ക് വ്യത്യസ്ത ക്വാണ്ടൈസ്ഡ് മോഡലുകൾ കോൾ ചെയ്യാൻ അനുവദിക്കുന്നു, അതേസമയം LlamaEdge GGUF മോഡലുകൾക്ക് کراസ്-പ്ലാറ്റ്ഫോം ലഭ്യത നൽകുന്നു.

## **Quantized Models:**
பல ഉപയോക്താക്കളും ലോക്കൽ ഇൻഫെറൻസിനായി ക്വാണ്റൈസ്ഡ് മോഡലുകൾ ഉപയോഗിക്കുന്നത് ഇഷ്ടപ്പെടുന്നു. ഉദാഹരണമായി, നിങ്ങൾ നേരടியாக Ollama run Phi-3 ഓടിക്കാമോ അല്ലെങ്കിൽ Modelfile ഉപയോഗിച്ച് അത് ഓഫ്‌ലൈനിൽ കോൺഫിഗർ ചെയ്യാവുന്നതാണ്. Modelfile GGUF ഫയൽ പാതയും പ്രോമ്പ്റ്റ് ഫോർമാറ്റും വ്യക്തമാക്കുന്നു.

## **Generative AI Possibilities:**
Phi-3-mini പോലുള്ള SLM-കൾ സംയോജിപ്പിച്ചാൽ ജനറേറ്റീവ് AI-യ്ക്ക് പുതിയ സാധ്യതകൾ തുറക്കപ്പെടുന്നു. ഇൻഫെറെൻസ് വെറും ആദ്യ പോയിന്റ് മാത്രമാണ്; ഈ മോഡലുകൾ വിഭിന്ന ടാസ്കുകൾക്ക്، ശ്രോത്-പരിമിതമായ, ലേറ്റൻസി-ബൗണ്ട്, ചെലവ്-പരിമിതമായ പശ്ചാത്തലങ്ങളിൽ ഉപയോഗിക്കാവുന്നതാണ്.

## **Unlocking Generative AI with Phi-3-mini: A Guide to Inference and Deployment** 
Semantic Kernel, Ollama/LlamaEdge, आणि ONNX Runtime ഉപയോഗിച്ച് Phi-3-mini മോഡലുകൾ ആക്‌സസ് ചെയ്ത് ഇൻഫെർ ചെയ്യുന്നതെങ്ങനെ എന്നതും വ്യത്യസ്ത ആപ്ലിക്കേഷൻ സീനാരികളിൽ ജനറേറ്റീവ് AI-യുടെ സാധ്യതകൾ എങ്ങനെ കണ്ടെത്താമെന്നതും പഠിക്കുക.

**Features**
Inference phi3-mini model in:

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)

സംഗ്രഹമായി, Phi-3-mini ഡെവലപ്പർമാർക്ക് വ്യത്യസ്ത മോഡൽ ഫോർമാറ്റുകൾ പരീക്ഷിക്കുകയും വിവിധ ആപ്ലിക്കേഷൻ സീനാരികളിൽ ജനറേറ്റീവ് AI പ്രയോജനപ്പെടുത്തുകയും ചെയ്യാൻ അവസരം നൽകുന്നു.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
ഡിസ്ക്ലെയിമർ:
ഈ രേഖ AI വിവർത്തനസേവനമായ [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. നാം കൃത്യതയ്ക്ക് ശ്രമിച്ചെങ്കിലും, ഓട്ടോമേറ്റഡ് വിവർത്തനങ്ങളിൽ പിശകുകൾ അല്ലെങ്കിൽ തെറ്റായ വ്യാഖ്യാനങ്ങൾ ഉണ്ടായേക്കാവുന്നതാണ്. മറ്റുഭാഷയിലുണ്ടായ মূলരൂപം ആണ് ഔദ്യോഗികമായ ഉറവിടം എന്ന് കരുതണം. നിർണായകമായ വിവരങ്ങൾക്ക് പ്രൊഫഷണൽ മനുഷ്യ പരിഭാഷ ശുപാർശ ചെയ്യപ്പെടുന്നു. ഈ വിവർത്തനത്തിന്റെ ഉപയോഗത്തിൽ നിന്നുണ്ടാകുന്ന ഏതെങ്കിലും തെറ്റിദ്ധാരണങ്ങളിലോ തെറ്റുകളിലോ അതിന്റെ ഒരു ഭാഗമായോ ഞങ്ങൾ ഉത്തരവാദിത്വം ഏറ്റെടുക്കുന്നില്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->