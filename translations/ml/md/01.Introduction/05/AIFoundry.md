<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7b4235159486df4000e16b7b46ddfec3",
  "translation_date": "2025-12-21T22:45:46+00:00",
  "source_file": "md/01.Introduction/05/AIFoundry.md",
  "language_code": "ml"
}
-->
# **Using Azure AI Foundry to evaluation**

![aistudo](../../../../../translated_images/AIFoundry.9e0b513e999a1c5a.ml.png)

How to evaluate your generative AI application using [Azure AI Foundry](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo). Whether you're assessing single-turn or multi-turn conversations, Azure AI Foundry provides tools for evaluating model performance and safety. 

![aistudo](../../../../../translated_images/AIPortfolio.69da59a8e1eaa70f.ml.png)

## How to evaluate generative AI apps with Azure AI Foundry
For more details instruction see the [Azure AI Foundry Documentation](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-generative-ai-app?WT.mc_id=aiml-138114-kinfeylo)

Here are the steps to get started:

## Evaluating Generative AI Models in Azure AI Foundry

**ആവശ്യങ്ങൾ**

- CSV അല്ലെങ്കിൽ JSON ഫോർമാറ്റിലുള്ള ഒരു ടെസ്റ്റ് ഡാറ്റാസെറ്റ്.
- വിന്യസിച്ചിരിക്കുന്ന ഒരു ജനനാത്മക AI മോഡൽ (ഉദാഹരണത്തിന് Phi-3, GPT 3.5, GPT 4, അല്ലെങ്കിൽ Davinci മോഡലുകൾ).
- മൂല്യനിർണയം നടത്താൻ compute instance ഉള്ളൊരു runtime.

## Built-in Evaluation Metrics

Azure AI Foundry നിങ്ങളെ single-turn കൂടാതെ സങ്കീർണ്ണമായ multi-turn സംഭാഷണങ്ങളിലെയും മൂല്യനിർണയം നടത്താനാവുന്നതാണ്. Retrieval Augmented Generation (RAG) സാഹചര്യങ്ങളിൽ, മോഡൽ പ്രത്യേക ഡാറ്റയിൽ ഉറപ്പിച്ചിരിക്കുന്നപ്പോൾ, നിര്‍മിച്ചിട്ടുള്ള എവല്യൂവേഷൻ മെട്രിക്‌സ് ഉപയോഗിച്ച് പ്രകടനം വിലയിരുത്താവുന്നതാണ്. പൊതു single-turn ചോദ്യോത്തരങ്ങളായ (non-RAG) senarios-കൾക്കും നിങ്ങൾ മൂല്യനിർണയം നടത്താം.

## Creating an Evaluation Run

Azure AI Foundry UI-യിൽ നിന്ന് Evaluate പേജ് അല്ലെങ്കിൽ Prompt Flow പേജിലേക്കു നാവിഗേറ്റ് ചെയ്യുക. എവല്യൂഷൻ റൺ സജ്ജമാക്കാൻ evaluation creation വിസാർഡ് പിന്തുടരുക. നിങ്ങളുടെ മൂല്യനിർണയത്തിന് ഐച്ഛികമായൊരു പേര് നൽകുക. നിങ്ങളുടെ ആപ്ലിക്കേഷന്റെ ലക്ഷ്യങ്ങളെ അനുയോജ്യമായ സീനാര്യോ തിരഞ്ഞെടുക്കുക. മോഡലിന്റെ ഔട്ട്പുട്ട് വിലയിരുത്തുന്നതിനായി ഒരു അല്ലെങ്കിൽ കൂടുതല്‍ എവല്യൂവേഷൻ മെട്രിക്‌സ് തിരഞ്ഞെടുക്കുക.

## Custom Evaluation Flow (Optional)

കൂടുതൽ ഫ്ലക്സിബിലിറ്റിക്ക്, നിങ്ങൾക്കു ഒരു കസ്റ്റം എവല്യൂവേഷൻ ഫ്ലോ സജ്ജീകരിക്കാവുന്നതാണ്. നിങ്ങളുടെ പ്രത്യേക ആവശ്യങ്ങളെ അടിസ്ഥാനമാക്കി എവല്യൂവേഷൻ പ്രക്രിയാ ക്രമീകരിക്കുക.

## Viewing Results

എവല്യൂവേഷൻ 실행ിച്ചതിനു ശേഷം, Azure AI Foundry-യിൽ വിശദമായ എവല്യൂവേഷൻ മെട്രിക്സുകൾ ലോഗ് ചെയ്യുകയും കാണിക്കുകയും വിശകലനം ചെയ്യുകയും ചെയ്യുക. നിങ്ങളുടെ ആപ്ലിക്കേഷന്റെ ശേഷികളും പരിധികളും കുറിച്ചുള്ള洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞洞

**കുറിപ്പ്** Azure AI Foundry ഇപ്പോൾ public preview-ൽ ആണ്, അതിനാൽ പരീക്ഷണത്തിനും വികസനത്തിനും ഉപയോഗിക്കുക. പ്രൊഡക്ഷൻ വർക്‌ലോഡുകൾക്കായി മറ്റ് انتخابങ്ങൾ പരിഗണിക്കുക. കൂടുതൽ വിശദാംശങ്ങൾക്കും ഘട്ടം-ഘട്ട നിർദേശങ്ങൾക്കുമായി ഔദ്യോഗിക [AI Foundry documentation](https://learn.microsoft.com/azure/ai-studio/?WT.mc_id=aiml-138114-kinfeylo) കാണുക.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അസ്വീകാരം**:
ഈ പ്രമാണം AI വിവർത്തനസേവനമായ [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്യപ്പെട്ടതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്ക് പരിശ്രമിച്ചിരുന്നുവെങ്കിലും, ഓട്ടോമേറ്റഡ് വിവർത്തനങ്ങളിൽ പിശകുകൾ അല്ലെങ്കിൽ അസത്യതകൾ ഉണ്ടാകാവുന്നതാണ് എന്ന് ദയവായി ശ്രദ്ധിക്കുക. യഥാർത്ഥ ഭാഷയിൽ ഉള്ള രേഖയാണ് ഔപചാരിക സ്രോതസ്സായി കാണപ്പെടേണ്ടത്. നിർണായകമായ വിവരങ്ങൾക്ക് പ്രൊഫഷണൽ മാനവ വിവർത്തനം ശുപാർശ ചെയ്യുന്നു. ഈ വിവർത്തനത്തിന്റെ ഉപയോഗം മൂലം ഉണ്ടാകുന്ന ഏതെങ്കിലും തെറ്റിദ്ധാരണങ്ങളോ തെറ്റ് വ്യാഖ്യാനങ്ങളോ ഞങ്ങൾക്ക് ഉത്തരവാദിത്വം ഉണ്ടായിരിക്കില്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->