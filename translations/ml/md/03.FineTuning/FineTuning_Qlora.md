<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "54b6b824568d4decb574b9e117c4f5f7",
  "translation_date": "2025-12-21T17:19:17+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Qlora.md",
  "language_code": "ml"
}
-->
**QLoRA ഉപയോഗിച്ച് Phi-3 ഫൈൻ-ട്യൂണിംഗ്**

Microsoft-ന്റെ Phi-3 Mini ভাষാ മോഡൽ [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora) ഉപയോഗിച്ച് ഫൈൻ-ട്യൂൺ ചെയ്യൽ. 

QLoRA സംഭാഷണപരമായ മനസ്സിലാക്കലും പ്രതികരണങ്ങളുടെ സൃഷ്ടിയും മെച്ചപ്പെടുത്താൻ സഹായിക്കും. 

transformersനും bitsandbytesനും ഉപയോഗിച്ച് 4bits-ൽ മോഡലുകൾ ലോഡ് ചെയ്യാൻ, നിങ്ങൾക്ക് accelerateയും transformersയും സോഴ്സിൽ നിന്നുതന്നെ ഇൻസ്റ്റാൾ ചെയ്യേണ്ടിവരും, കൂടാതെ bitsandbytes ലൈബ്രറിയുടെ ഏറ്റവും പുതിയ പതിപ്പ് ഉണ്ടായിരിക്കണമെന്ന് ഉറപ്പ് വരുത്തുക.

**സാമ്പിളുകൾ**
- [ഈ സാമ്പിൾ നോട്ട്ബുക്കിലൂടെ കൂടുതൽ വിവരങ്ങൾ നേടുക](../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python ഫൈൻ-ട്യൂണിംഗ് സാമ്പിളിന്റെ ഉദാഹരണം](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Hugging Face Hub-ൽ LORA ഉപയോഗിച്ച് ഫൈൻ-ട്യൂണിംഗിന്റെ ഉദാഹരണം](../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Hugging Face Hub-ൽ QLORA ഉപയോഗിച്ച് ഫൈൻ-ട്യൂണിംഗിന്റെ ഉദാഹരണം](../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
ഡിസ്ക്ലെയിമർ:
ഈ രേഖ AI പരിഭാഷാ സേവനമായ Co-op Translator (https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്കായി ശ്രമിക്കുന്നതായിരുന്നാലും, ഓട്ടോമാറ്റഡ് പരിഭാഷകളിൽ തെറ്റുകളും അശുദ്ധതകളും ഉണ്ടായേക്കാമെന്ന് ദയവായി ശ്രദ്ധിക്കുക. സ്വഭാവഭാഷയിലുള്ള പ്രാഥമിക രേഖയെ അധികാരപരമായ ഉറവിടമായി കാണണം. അത്യാവശ്യ വിവരങ്ങൾക്ക് പ്രൊഫഷണൽ മനുഷ്യപരിഭാഷ ശുപാർശ ചെയ്യപ്പെടുന്നു. ഈ പരിഭാഷ ഉപയോഗിക്കുന്നതിലൂടെ ഉളവാകുന്ന ഏതെങ്കിലും തെറ്റിദ്ധാരണകളുടെയും തെറ്റായ വ്യാഖ്യാനങ്ങളുടെയും ഉത്തരവാദിത്വം ഞങ്ങൾക്ക് ഉണ്ടായിരിക്കില്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->