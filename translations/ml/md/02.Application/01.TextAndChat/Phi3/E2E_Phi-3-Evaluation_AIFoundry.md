# Microsoft-ന്‍റെ ഉത്തരവാദിത്വ AI സിദ്ധാന്തങ്ങളോട് ശ്രദ്ധ കേന്ദ്രീകരിച്ച് Microsoft Foundry ലെ Fine-tuned Phi-3 / Phi-3.5 മോഡൽ വിലയിരുത്തുക

Microsoft Tech Community-യിലെ "[Evaluate Fine-tuned Phi-3 / 3.5 Models in Microsoft Foundry Focusing on Microsoft's Responsible AI](https://techcommunity.microsoft.com/blog/educatordeveloperblog/evaluate-fine-tuned-phi-3--3-5-models-in-azure-ai-studio-focusing-on-microsofts-/4227850?WT.mc_id=aiml-137032-kinfeylo)" എന്ന മാർഗ്ഗനിർദ്ദേശത്തെ അടിസ്ഥാനമാക്കിയുള്ള ഈ End-to-End (E2E) സാമ്പിൾ ആണ്.

## അവലോകനം

### Microsoft Foundry-യിൽ fine-tuned Phi-3 / Phi-3.5 മോഡൽ എങ്ങനെ സുരക്ഷിതത്വവും പ്രകടനവും വിലയിരുത്താം?

ഒരു മോഡൽ ഫൈൻ-ട്യൂൺ ചെയ്യുമ്പോൾ ചിലപ്പോൾ ആഗ്രഹിക്കാത്ത അല്ലെങ്കിൽ ഇഷ്‌ടമല്ലാത്ത പ്രതികരണങ്ങൾ വരാം. മോഡൽ സുരക്ഷിതവും ഫലപ്രദവുമായിരിക്കാൻ ഉറപ്പാക്കാൻ, മോഡലിന് ദുരുപയോഗം സൃഷ്ടിക്കാനുള്ള സാധ്യതയും കൃത്യമായ, പ്രസക്തമായ, സ്വയംഗതമായ പ്രതികരണങ്ങൾ സൃഷ്ടിക്കുന്ന കഴിവും വിലയിരുത്തുന്നത് അത്യന്താപേക്ഷിതമാണ്. ഈ ട്യൂട്ടോറിയലിൽ, Microsoft Foundry-യിലെ Prompt flow-യുമായി ഇന്റഗ്രേറ്റ് ചെയ്ത fine-tuned Phi-3 / Phi-3.5 മോഡലിന്റെ സുരക്ഷിതത്വവും പ്രകടനവും എങ്ങനെ വിലയിരുത്താമെന്ന് പഠിക്കാം.

ഇത് Microsoft Foundry-യുടെ ഒരു വിലയിരുത്തൽ പ്രക്രിയയാണ്.

![Architecture of tutorial.](../../../../../../translated_images/ml/architecture.10bec55250f5d6a4.webp)

*ചിത്ര സ്രോതസ്: [ജനന AI ആപ്ലിക്കേഷനുകളുടെ വിലയിരുത്തൽ](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> Phi-3 / Phi-3.5 സംബന്ധിച്ച കൂടുതൽ വിവരങ്ങൾക്കും കൂട്ട-produced മാർഗ്ഗങ്ങൾക്കുമായി [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723) സന്ദർശിക്കുക.

### മുൻകൂർ ആവശ്യങ്ങൾ

- [Python](https://www.python.org/downloads)
- [Azure subscription](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- Fine-tuned Phi-3 / Phi-3.5 മോഡൽ

### ഉള്ളടക്ക सारणी

1. [**സംഭവം 1: Microsoft Foundry-യുടെ Prompt flow വിലയിരുത്തലിന്റെ പരിചയം**](#scenario-1-introduction-to-azure-ai-studios-prompt-flow-evaluation)

    - [സുരക്ഷിതത്വ വിലയിരുത്തലിന്റെ പരിചയം](#സുരക്ഷിതത്വ-വിലയിരുത്തലിന്‍റെ-പരിചയം)
    - [പ്രകടന വിലയിരുത്തലിന്റെ പരിചയം](#പ്രകടന-വിലയിരുത്തലിന്‍റെ-പരിചയം)

1. [**സംഭവം 2: Microsoft Foundry-യിൽ Phi-3 / Phi-3.5 മോഡൽ വിലയിരുത്തൽ**](#scenario-2-evaluating-the-phi-3--phi-35-model-in-azure-ai-studio)

    - [തുടങ്ങുന്നതിനു മുമ്പ്](#തുടങ്ങുന്നതിനു-മുമ്പ്)
    - [Phi-3 / Phi-3.5 മോഡൽ വിലയിരുത്താൻ Azure OpenAI വിനിയോഗിക്കുക](#deploy-azure-openai-to-evaluate-the-phi-3--phi-35-model)
    - [Microsoft Foundry-യുടെ Prompt flow വിലയിരുത്തൽ ഉപയോഗിച്ച് fine-tuned Phi-3 / Phi-3.5 മോഡൽ വിലയിരുത്തുക](#evaluate-the-fine-tuned-phi-3--phi-35-model-using-azure-ai-studios-prompt-flow-evaluation)

1. [അഭിനന്ദനങ്ങൾ!](#അഭിനന്ദനങ്ങൾ)

## **സംഭവം 1: Microsoft Foundry-യുടെ Prompt flow വിലയിരുത്തലിന്റെ പരിചയം**

### സുരക്ഷിതത്വ വിലയിരുത്തലിന്‍റെ പരിചയം

നിങ്ങളുടെ AI മോഡൽ നൈതികവും സുരക്ഷിതവുമായിരിക്കണമെന്ന് ഉറപ്പാക്കാൻ, അത് Microsoft ന്റെ ഉത്തരവാദിത്വ AI സിദ്ധാന്തങ്ങളോട് പൊരുത്തപ്പെടുന്നതാണോ എന്ന് വിലയിരുത്തേണ്ടത് അനിവാര്യമാണ്. Microsoft Foundry-യിൽ, സുരക്ഷിതത്വ വിലയിരുത്തലുകൾ മോഡലിന് jailbreak ആക്രമണങ്ങൾക്കുള്ള ദുർബലതയും, ഹാനികരമായ ഉള്ളടക്കം സൃഷ്ടിക്കാനുള്ള കഴിവും വിലയിരുത്താൻ സഹായിക്കുന്നു, ഇത് നേരിട്ട് ഈ സിദ്ധാന്തങ്ങളോട് പൊരുത്തപ്പെടുന്നു.

![Safaty evaluation.](../../../../../../translated_images/ml/safety-evaluation.083586ec88dfa950.webp)

*ചിത്ര സ്രോതസ്: [ജനന AI ആപ്ലിക്കേഷനുകളുടെ വിലയിരുത്തൽ](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Microsoft-ന്റെ ഉത്തരവാദിത്വ AI സിദ്ധാന്തങ്ങൾ

സാങ്കേതിക നടപടികൾ ആരംഭിക്കുന്നതിന് മുമ്പ്, Microsoft-ന്റെ ഉത്തരവാദിത്വ AI സിദ്ധാന്തങ്ങളെ മനസ്സിലാക്കുന്നത് അത്യന്താപേക്ഷിതമാണ്. ഈ സിദ്ധാന്തങ്ങൾ, AI സിസ്റ്റങ്ങൾ ഉത്തരവാദിത്വത്തോടെ വികസിപ്പിക്കുകയും വിനിയോഗിക്കുകയും നടത്തുകയും ചെയ്യുന്നതിനുള്ള ഒരു നൈതിക ചട്ടക്കുഴപ്പമാണ്. AI സാങ്കേതികവിദ്യകൾ നീതി, പാഴ്വാതരണത്വം, ഉൾക്കാഴ്ച എന്നിവയെ അടിസ്ഥാനമാക്കിയുള്ളവിധം നിർമ്മിക്കപ്പെടുന്നുവെന്ന് ഉറപ്പാക്കാൻ ഈ സിദ്ധാന്തങ്ങൾ സഹായിക്കുന്നു. AI മോഡലുകളുടെ സുരക്ഷിതത്വം വിലയിരുത്തുന്നതിന് ഇവ അടിസ്ഥാനം ആണ്.

Microsoft-ന്റെ ഉത്തരവാദിത്വ AI സിദ്ധാന്തങ്ങൾ:

- **നീതിപരവും ഉൾക്കാഴ്ചയുള്ളതുമായവ**: AI സിസ്റ്റങ്ങൾ എല്ലാവരോടും നീതിപൂർവ്വം പെരുമാറണം, സമാന സാഹചര്യത്തിലുള്ള ഗ്രൂപ്പുകളെ വ്യത്യസ്തമായി നിയന്ത്രിക്കാൻ കഴിയരുത്. ഉദാഹരണത്തിന്, AI സിസ്റ്റങ്ങൾ ചികിത്സ, വായ്പ അപേക്ഷകൾ, തൊഴിൽ വാഗ്ദാനങ്ങൾ എന്നിവയിൽ മാർഗനിർദേശങ്ങൾ നൽകുമ്പോൾ, സമാന ലക്ഷണങ്ങൾ, സാമ്പത്തിക സാഹചര്യങ്ങൾ, മുതലായവ ഉള്ള എല്ലാവർക്കും ഒരുപോലെ നിർദ്ദേശങ്ങൾ നൽകണം.

- **നിരന്തരതയും സുരക്ഷിതത്വവും**: വിശ്വാസ്യത ഉണ്ടാക്കാൻ AI സിസ്റ്റങ്ങൾ വിശ്വാസയോഗ്യവും, സുരക്ഷിതവുമായും, സ്ഥിരതയുള്ളവയായും പ്രവർത്തിക്കണം. അവ സമഗ്രമായി രൂപകൽപ്പന ചെയ്ത പ്രകാരം പ്രവർത്തിക്കുകയും, പ്രതീക്ഷിക്കാതിരുന്ന സാഹചര്യങ്ങളിൽ സുരക്ഷിതമായി പ്രതികരിക്കുകയും, ദുഷ്പ്രവർത്തനം തടയുകയും ചെയ്യണം. അവ എങ്ങനെ പെരുമാറുന്നു, എത്രവിധമുള്ള സാഹചര്യങ്ങളിൽ പകരം വെയ്ക്കാനാകും എന്നത് രൂപകൽപ്പനയ്ക്കും പരിശോധനയ്ക്കും സമയത്ത് വിഭിന്നമായ സാഹചര്യങ്ങൾ പരിഗണിച്ചാണ്.

- **പാഴ്വാതരണത്വം**: ജനങ്ങളുടെ ജീവിതത്തിൽ വലിയ പ്രഭാവം ചെലുത്തുന്ന തീരുമാനങ്ങളിൽ AI സിസ്റ്റങ്ങൾ സഹായിക്കുമ്പോൾ, ആ തീരുമാനങ്ങൾ എങ്ങനെ വന്നതാണെന്ന് വ്യക്തികൾ മനസ്സിലാക്കണം. ഒരു ബാങ്ക് ക്രെഡിറ്റ് യോഗ്യതയുള്ള ആളെ തീരുമാനിക്കാൻ AI ഉപയോഗിച്ചേക്കാം. ഒരു കമ്പനി ഏറ്റവും യോഗ്യരായ ഉദ്യോഗാർത്ഥികളെ തിരഞ്ഞെടുക്കാൻ AI ഉപയോഗിക്കാം.

- **സ്വകാര്യതയും സുരക്ഷിതത്വവും**: AI വ്യാപകമാകുന്നതോടെ, സ്വകാര്യതയെ സംരക്ഷിക്കാനും വ്യക്തിഗതവും ബിസിനസ് വിവരങ്ങളും സുരക്ഷിതമാക്കാനുമുള്ള ആവശ്യകതയും സങ്കീർണതയും വർദ്ധിക്കുന്നു. AI-യിൽ, ഡാറ്റ പ്രവേശനം മിടുക്കായ പ്രവചനങ്ങൾക്കും തീർച്ചയായും ആവശ്യമാണ്, അതിനാൽ സ്വകാര്യതയിലും ഡാറ്റ സുരക്ഷിതത്വത്തിലും അടുത്ത ശ്രദ്ധ നൽകണം.

- **ഉത്തരവാദിത്തം**: AI സിസ്റ്റങ്ങൾ രൂപകൽപ്പന ചെയ്‌തു വിനിയോഗിക്കുന്നവരുടെ നടപടി ഏറ്റവും ഉത്തരവാദിത്തപ്പെട്ടതായിരിക്കണം. സംഘടനകൾ വ്യവസായ മാനദണ്ഡങ്ങൾ അടിസ്ഥാനം കെട്ടിയ ഉപാധികൾ രൂപപ്പെടുത്തണം. ഇതിലൂടെ, AI സിസ്റ്റങ്ങൾ ആയുധം പോലെ രാജ്യത്തിന്‍റെ അവസാന തീരുമാനകർത്താവാകുന്നില്ല. മനുഷ്യർക്ക് അർഥപൂർണ നിയന്ത്രണം നിലനിർത്താൻ കഴിയണം, പ്രത്യേകിച്ച് സ്വയംകണ്ടുപിടിക്കുന്ന AI-കളിൽ.

![Fill hub.](../../../../../../translated_images/ml/responsibleai2.c07ef430113fad8c.webp)

*ചിത്ര സ്രോതസ്: [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> Microsoft-ന്റെ ഉത്തരവാദിത്വ AI സിദ്ധാന്തങ്ങൾക്കുറിച്ച് കൂടുതൽ പഠിക്കാൻ, [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723) സന്ദർശിക്കുക.

#### സുരക്ഷിതത്വ മെട്രിക്കുകൾ

ഈ ട്യൂട്ടോറിയലിൽ, Microsoft Foundry-യുടെ സുരക്ഷിതത്വ മെട്രിക്കുകൾ ഉപയോഗിച്ച് fine-tuned Phi-3 മോഡലിന്റെ സുരക്ഷിതത്വം വിലയിരുത്തും. ഈ മെട്രിക്കുകൾ മോഡലിന് ഹാനികരമായ ഉള്ളടക്കം സൃഷ്ടിക്കാനുള്ള സാധ്യതയും jailbreak ആക്രമണങ്ങൾക്കുള്ള ദുർബലതയും പരിശോധിക്കാൻ സഹായിക്കുന്നു. സുരക്ഷിതത്വ മെട്രിക്കുകൾ ഉൾക്കൊള്ളുന്നു:

- **സ്വയംഹാനി സംബന്ധമായ ഉള്ളടക്കം**: മോഡൽ സ്വയംഹാനി സംബന്ധമായ ഉള്ളടക്കം സൃഷ്ടിക്കാൻ സാധ്യതയുമുണ്ടോ എന്ന് വിലയിരുത്തുന്നു.
- **വിവേചനപരവും അനീതിപൂർണ്ണവുമായ ഉള്ളടക്കം**: മോഡൽ ബാധ്യമായ അല്ലെങ്കിൽ അനീതിപൂർണ്ണ ഉള്ളടക്കം സൃഷ്ടിക്കാൻ സാധ്യതയുമുണ്ടോ എന്ന് വിലയിരുത്തുന്നു.
- **ഹിംസാത്മക ഉള്ളടക്കം**: മോഡൽ ഹിംസാത്മക ഉള്ളടക്കം സൃഷ്ടിക്കാൻ സാധ്യതയുമുണ്ടോ എന്ന് വിലയിരുത്തുന്നു.
- **ലിംഗബന്ധമായ ഉള്ളടക്കം**: മോഡൽ അസഭ്യമായ ലിംഗബന്ധമായ ഉള്ളടക്കം സൃഷ്ടിക്കാൻ സാധ്യതയുമുണ്ടോ എന്ന് വിലയിരുത്തുന്നു.

ഈ വശങ്ങൾ വിലയിരുത്തുന്നതിലൂടെ, AI മോഡൽ ഹാനികരമോ അപമാനകരമോ ഉള്ളടക്കം സൃഷ്ടിക്കാതെ സാമൂഹിക മൂല്യങ്ങൾക്കും നിയമോപദേശം സേവനങ്ങൾക്കും പൊരിաժամ്മിക്കാൻ സഹായിക്കുന്നു.

![Evaluate based on safety.](../../../../../../translated_images/ml/evaluate-based-on-safety.c5df819f5b0bfc07.webp)

### പ്രകടന വിലയിരുത്തലിന്‍റെ പരിചയം

നിങ്ങളുടെ AI മോഡൽ പ്രതീക്ഷപ്രകാരം പ്രവർത്തിക്കുന്നുണ്ടോയെന്ന് ഉറപ്പാക്കാൻ, പ്രകടന മെട്രിക്കുകൾ പ്രതിപാദിച്ചും പരീക്ഷിക്കേണ്ടതാണ്. Microsoft Foundry-യിൽ, പ്രകടന വിലയിരുത്തലുകൾ മോഡലിന്റെ കൃത്യവും പ്രസക്തവുമായവും സ്വയംഗതവുമായ പ്രതികരണങ്ങൾ സൃഷ്ടിക്കുന്ന ശേഷി വിലയിരുത്താൻ സഹായിക്കുന്നു.

![Safaty evaluation.](../../../../../../translated_images/ml/performance-evaluation.48b3e7e01a098740.webp)

*ചിത്ര സ്രോതസ്: [ജനന AI ആപ്ലിക്കേഷനുകളുടെ വിലയിരുത്തൽ](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### പ്രകടന മെട്രിക്കുകൾ

ഈ ട്യൂട്ടോറിയലിൽ, Microsoft Foundry-യുടെ പ്രകടന മെട്രിക്കുകൾ ഉപയോഗിച്ച് fine-tuned Phi-3 / Phi-3.5 മോഡലിന്റെ പ്രകടനം വിലയിരുത്തും. അനുസരിച്ചുള്ള മെട്രിക്കുകൾ മോഡലിന്റെ കൃത്യവും പ്രസക്തവുമായും സ്വയംഗതവുമായ പ്രതികരണങ്ങൾ സൃഷ്ടിക്കുന്ന ശേഷി വിലയിരുത്തുന്നു. പ്രകടന മെട്രിക്കുകൾ ഉൾക്കൊള്ളുന്നു:

- **ഗ്രൗണ്ടഡ്‌നെസ്**: ഉൽപ്പന്നമാക്കിയ ഉത്തരങ്ങൾ ഇൻപുട്ട് സ്രോതസ്സിൽ നിന്നുള്ള വിവരങ്ങളുമായി എത്രത്തോളം പൊരുത്തപ്പെടുന്നു എന്ന് വിലയിരുത്തും.
- **പ്രസക്തത**: നൽകിയ ചോദ്യങ്ങളുമായി ഉൽപ്പന്നമാക്കിയ പ്രതികരണങ്ങളുടെ അനുയോജ്യത വിലയിരുത്തുന്നു.
- **സ്വയംഗത്വം**: ഉൽപ്പന്നമാക്കിയ വാചകം എത്രത്തോളം സൗമ്യമായി പ്രവഹിക്കുന്നു, സ്വാഭാവികം വായിക്കുന്നു, മനുഷ്യ പോലെയുള്ള ഭാഷയ്ക്ക് സമാനമാണ് എന്ന് വിലയിരുത്തും.
- **വാചകസമർഥ്യത**: ഉൽപ്പന്നമാക്കിയ വാചകത്തിന്റെ ഭാഷാ പ്രാവീണ്യം വിലയിരുത്തും.
- **GPT സമാനത**: ഉൽപ്പന്നപ്പെട്ട പ്രതികരണം ഗ്രൗണ്ട് ട്രൂത്ത് (അസൽ ഡാറ്റ) കൂടെ താരതമ്യം ചെയ്യുന്നു.
- **F1 സ്കോർ**: ഉൽപ്പന്ന ant പ്രതികരണവും സ്രോതസ് ഡാറ്റയും തമ്മിലുള്ള പങ്കുവെച്ച വാക്കുകളുടെ അനുപാതം കണക്കാക്കുന്നു.

ഈ മെട്രിക്കുകൾ മോഡൽ കൃത്യതയുള്ള, പ്രസക്തമായ, സ്വയംഗതമായ പ്രതികരണങ്ങൾ സൃഷ്ടിക്കുന്ന കഴിവ് വിലയിരുത്താൻ സഹായിക്കുന്നു.

![Evaluate based on performance.](../../../../../../translated_images/ml/evaluate-based-on-performance.3e801c647c7554e8.webp)

## **സംഭവം 2: Microsoft Foundry-ൽ Phi-3 / Phi-3.5 മോഡൽ വിലയിരുത്തൽ**

### തുടങ്ങുന്നതിനു മുമ്പ്

ഈ ട്യൂട്ടോറിയൽ മുൻപ് പങ്കുവെച്ച ബ്ലോഗ് പോസ്റ്റുകൾ ആയ "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" ആയും "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)" ആയും അനുബന്ധമാണ്. ഈ പോസ്റ്റുകളിൽ Microsoft Foundry-യിൽ Phi-3 / Phi-3.5 മോഡൽ fine-tune ചെയ്ത് Prompt flow-യുമായി ഇൻറഗ്രേറ്റ് ചെയ്ത നടപടിക്രമങ്ങൾ വിശദീകരിച്ചിട്ടുണ്ട്.

ഈ ട്യൂട്ടോറിയലിൽ, Azure OpenAI മോഡൽ വിലയിരുത്തുക എന്ന നിലയിൽ Microsoft Foundry-യിൽ വിനിയോഗിക്കുകയും fine-tuned Phi-3 / Phi-3.5 മോഡൽ അതുപയോഗിച്ച് വിലയിരുത്തുന്നതിനായി ഉപയോഗിക്കുകയും ചെയ്യും.

ഈ ട്യൂട്ടോറിയൽ തുടങ്ങുന്നതിന് മുമ്പ്, മുൻപ് പറഞ്ഞ ട്യൂട്ടോറിയലുകളിൽ വിശദീകരിച്ചപ്രകാരമുള്ള മുൻകൂർ ആവശ്യങ്ങൾക്കൊപ്പമുള്ളവ നിർബന്ധമാണ്:

1. fine-tuned Phi-3 / Phi-3.5 മോഡൽ വിലയിരുത്താനുള്ള തയ്യാറാക്കിയ ഡാറ്റാസെറ്റ്.
1. Azure Machine Learning-ൽ ഫൈൻ-ട്യൂൺ ചെയ്ത് വിനിയോഗിച്ച Phi-3 / Phi-3.5 മോഡൽ.
1. Microsoft Foundry-യിൽ fine-tuned Phi-3 / Phi-3.5 മോഡൽ ഇൻറഗ്രേറ്റ് ചെയ്ത Prompt flow.

> [!NOTE]
> മുൻപ് ഡൗൺലോഡ് ചെയ്ത **ULTRACHAT_200k** ഡാറ്റാസെറ്റിലെ data ഫോൾഡറിൽ ഉള്ള *test_data.jsonl* ഫയൽ fine-tuned Phi-3 / Phi-3.5 മോഡൽ വിലയിരുത്താനുള്ള ഡാറ്റാസെറ്റായി ഉപയോഗിക്കും.

#### Microsoft Foundry-യിൽ Custom Phi-3 / Phi-3.5 മോഡലിനെ Prompt flow-യുമായി ഇന്റഗ്രേറ്റ് ചെയ്യുക (കോഡ് ഫസ്റ്റ് സമീപനം)

> [!NOTE]
> "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)" ലെ low-code സമീപനം പിന്തുടർത്തി വന്നവർക്ക് ഈ മാർഗ്ഗം ഒഴിവാക്കി അടുത്ത പ്രയാസത്തിലേക്ക് പോകാം.
> പക്ഷേ, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" ലെ കോഡ്-ഫസ്റ്റ് സമീപനം പാലിച്ച് Phi-3 / Phi-3.5 മോഡൽ fine-tune ചെയ്ത് വിനിയോഗിച്ചതാണെങ്കിൽ, മോഡൽ Prompt flow-യുമായി കണക്ട് ചെയ്യുന്നതിനുള്ള പ്രക്രിയ ഇത് നിന്നും വ്യത്യസ്തമാണ്. ഈ പ്രക്രിയ ഈ പ്രയാസത്തിൽ പഠിപ്പിക്കും.

തുടരാനായി, Microsoft Foundry-യിലെ Prompt flow-യിൽ fine-tuned Phi-3 / Phi-3.5 മോഡൽ ഇന്റഗ്രേറ്റ് ചെയ്യണം.

#### Microsoft Foundry Hub സൃഷ്ടിക്കുക

Project സൃഷ്ടിക്കാനുമុន്, Hub സൃഷ്ടിക്കണം. Hub ഒരു Resource Group പോലെയാണ് പ്രവർത്തിക്കുന്നത്, ഇതിലൂടെ Microsoft Foundry-ൽ പല Projects-കളും ക്രമീകരിച്ച് කළമാക്കാൻ കഴിയും.
1. സൈൻ ഇൻ ചെയ്യുക [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. എഡത്ത് യുടം ടാബിൽ നിന്നു **എല്ലാ ഹബ്സും** തിരഞ്ഞെടുത്തു.

1. നാവിഗേഷൻ മെനുവിൽ നിന്നു **+ പുതിയ ഹബ്** തിരഞ്ഞെടുത്തു.

    ![Create hub.](../../../../../../translated_images/ml/create-hub.5be78fb1e21ffbf1.webp)

1. താഴെ പറയുന്ന പ്രവർത്തനങ്ങൾ ചെയ്യുക:

    - **ഹബ് പേര്** രേഖപ്പെടുത്തുക. ഇത് ഒറ്റപ്പെട്ട മൂല്യം ആയിരിക്കണം.
    - നിങ്ങളുടെ Azure **സബ്‌സ്ക്രിപ്ഷൻ** തിരഞ്ഞെടുത്ത്.
    - ഉപയോഗിക്കാനുദ്ദേശിക്കുന്ന **റിസോഴ്‌സ് ഗ്രൂപ്പ്** തിരഞ്ഞെടുത്ത് (ആവശ്യമായി വന്നാൽ പുതിയതായി സൃഷ്ടിക്കുക).
    - നിങ്ങൾ ഉപയോഗിക്കാൻ ആഗ്രഹിക്കുന്ന **സ്ഥാനത്ത്** തിരഞ്ഞെടുക്കുക.
    - ഉപയോഗിക്കാൻ ആഗ്രഹിക്കുന്ന **Azure AI സേവനങ്ങൾ കണക്റ്റ് ചെയ്യുക** തിരഞ്ഞെടുത്ത് (ആവശ്യമായി വന്നാൽ പുതിയതായി സൃഷ്ടിക്കുക).
    - **Azure AI Search-ൽ കണക്റ്റ് ചെയ്യുന്നത്** **കണക്റ്റ് ചെയ്യാതിരിക്കാൻ** തിരഞ്ഞെടുക്കുക.

    ![Fill hub.](../../../../../../translated_images/ml/fill-hub.baaa108495c71e34.webp)

1. **അടുത്തത്** തിരഞ്ഞെടുത്ത്.

#### Microsoft Foundry പ്രോജക്ട് സൃഷ്ടിക്കുക

1. നിങ്ങൾ സൃഷ്ടിച്ച ഹബിൽ നിന്ന് എഡത്ത് യുടം ടാബിൽ നിന്നു **എല്ലാ പ്രോജക്ടുകളും** തിരഞ്ഞെടുത്ത്.

1. നാവിഗേഷൻ മെനുവിൽ നിന്നു **+ പുതിയ പ്രോജക്ട്** തിരഞ്ഞെടുത്ത്.

    ![Select new project.](../../../../../../translated_images/ml/select-new-project.cd31c0404088d7a3.webp)

1. **പ്രോജക്ട് പേര്** രേഖപ്പെടുത്തുക. ഇത് ഒറ്റപ്പെട്ട മൂല്യം ആയിരിക്കണം.

    ![Create project.](../../../../../../translated_images/ml/create-project.ca3b71298b90e420.webp)

1. **ഒരു പ്രോജക്ട് സൃഷ്ടിക്കുക** തിരഞ്ഞെടുക്കുക.

#### ഫൈൻ-ട്യൂൺ ചെയ്ത Phi-3 / Phi-3.5 മോഡലിന് സ്വന്തം കണക്ഷൻ ചേർക്കുക

നിങ്ങളുടെ കസ്റ്റം Phi-3 / Phi-3.5 മോഡലിനെ Prompt flow-യുമായി സംയോജിപ്പിക്കാൻ, മോഡലിന്റെ എന്റ്പോയിന്റും കീയും ഒരു കസ്റ്റം കണക്ഷനിൽ സംരക്ഷിക്കേണ്ടതുണ്ട്. ഇതിലൂടെ Prompt flow-യിൽ നിങ്ങളുടെ കസ്റ്റം Phi-3 / Phi-3.5 മോഡലിലേക്ക് ആക്‌സസ് ഉണ്ടാകും.

#### ഫൈൻ-ട്യൂൺ ചെയ്ത Phi-3 / Phi-3.5 മോഡലിന്റെ API കീയും എന്റ്പോയിന്റ് URIയും സെറ്റ് ചെയ്യുക

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) സന്ദർശിക്കുക.

1. നിങ്ങൾ സൃഷ്ടിച്ച Azure Machine learning വർക്ക്സ്പേസിലേക്ക് നാവിഗേറ്റ് ചെയ്യുക.

1. എഡത്ത് യുടം ടാബിൽ നിന്നു **Endpoints** തിരഞ്ഞെടുത്ത്.

    ![Select endpoints.](../../../../../../translated_images/ml/select-endpoints.ee7387ecd68bd18d.webp)

1. നിങ്ങൾ സൃഷ്ടിച്ച എന്റ്പോയിന്റ് തിരഞ്ഞെടുത്ത്.

    ![Select endpoints.](../../../../../../translated_images/ml/select-endpoint-created.9f63af5e4cf98b2e.webp)

1. നാവിഗേഷൻ മെനുവിൽ നിന്നു **Consume** തിരഞ്ഞെടുത്ത്.

1. നിങ്ങളുടെ **REST endpoint** ഉം **പ്രൈമറി കീ** ഉം കോപ്പി ചെയ്യുക.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/ml/copy-endpoint-key.0650c3786bd646ab.webp)

#### കസ്റ്റം കണക്ഷൻ ചേർക്കുക

1. [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) സന്ദർശിക്കുക.

1. നിങ്ങൾ സൃഷ്ടിച്ച Microsoft Foundry പ്രോജക്ടിലേക്ക് നാവിഗേറ്റ് ചെയ്യുക.

1. നിങ്ങൾ സൃഷ്ടിച്ച പ്രോജക്ടിൽ എഡത്ത് യുടം ടാബിൽ നിന്നു **Settings** തിരഞ്ഞെടുത്ത്.

1. **+ New connection** തിരഞ്ഞെടുത്ത്.

    ![Select new connection.](../../../../../../translated_images/ml/select-new-connection.fa0f35743758a74b.webp)

1. നാവിഗേഷൻ മെനുവിൽ നിന്നും **Custom keys** തിരഞ്ഞെടുത്ത്.

    ![Select custom keys.](../../../../../../translated_images/ml/select-custom-keys.5a3c6b25580a9b67.webp)

1. താഴെ കൊടുത്തിരിക്കുന്ന പ്രവർത്തനങ്ങൾ ചെയ്യുക:

    - **+ Add key value pairs** തിരഞ്ഞെടുത്ത്.
    - കീ നാമമായി **endpoint** നൽകുക, Azure ML Studio-യിൽ നിന്നു കോപ്പി ചെയ്ത എന്റ്പോയിന്റ് മൂല്യം പെയ്‌സ്റ്റ് ചെയ്യുക.
    - വീണ്ടും **+ Add key value pairs** തിരഞ്ഞെടുത്ത്.
    - കീ നാമമായി **key** നൽകുക, Azure ML Studio-യിൽ നിന്നു കോപ്പി ചെയ്ത കീ മൂല്യം പെയ്‌സ്റ്റ് ചെയ്യുക.
    - കീകൾ ചേർത്ത ശേഷം, കീ പുറത്ത് പുറത്തുവന്നുപോകാതെ **is secret** ഓപ്ഷൻ തിരഞ്ഞെടുക്കുക.

    ![Add connection.](../../../../../../translated_images/ml/add-connection.ac7f5faf8b10b0df.webp)

1. **Add connection** തിരഞ്ഞെടുത്ത്.

#### Prompt flow സൃഷ്ടിക്കുക

നിങ്ങൾ Microsoft Foundry-യിൽ ഒരു കസ്റ്റം കണക്ഷൻ ചേർത്തു. ഇനി ചുവടെയുള്ള പ്രവർത്തനങ്ങൾ ഉപയോഗിച്ച് Prompt flow സൃഷ്ടിക്കാം. തുടർന്ന് ഈ Prompt flow കസ്റ്റം കണക്ഷനുമായി ബന്ധിപ്പിച്ച് ഫൈൻ-ട്യൂൺ ചെയ്ത മോഡൽ Prompt flow-യിലേയ്ക്ക് ഉപയോഗിക്കാം.

1. നിങ്ങൾ സൃഷ്ടിച്ച Microsoft Foundry പ്രോജക്ടിലേക്ക് നാവിഗേറ്റ് ചെയ്യുക.

1. എഡത്ത് യുടം ടാബിൽ നിന്ന് **Prompt flow** തിരഞ്ഞെടുത്ത്.

1. നാവിഗേഷൻ മെനുവിൽ നിന്നു **+ Create** തിരഞ്ഞെടുത്ത്.

    ![Select Promptflow.](../../../../../../translated_images/ml/select-promptflow.18ff2e61ab9173eb.webp)

1. നാവിഗേഷൻ മെനുവിൽ നിന്ന് **Chat flow** തിരഞ്ഞെടുത്ത്.

    ![Select chat flow.](../../../../../../translated_images/ml/select-flow-type.28375125ec9996d3.webp)

1. ഉപയോഗിക്കാൻ **ഫോൾഡർ പേര്** രേഖപ്പെടുത്തുക.

    ![Select chat flow.](../../../../../../translated_images/ml/enter-name.02ddf8fb840ad430.webp)

1. **Create** തിരഞ്ഞെടുത്ത്.

#### നിങ്ങളുടെ കസ്റ്റം Phi-3 / Phi-3.5 മോഡലിൽ ചാറ്റ് നടത്താൻ Prompt flow ക്രമീകരിക്കുക

ഫൈൻ-ട്യൂൺ ചെയ്ത Phi-3 / Phi-3.5 മോഡൽ Prompt flow-യിലേക്ക് സംയോജിപ്പിക്കാൻ നിങ്ങൾക്ക് വേണ്ടിയുള്ള പ്രവർത്തനം. നിലവിലുള്ള Prompt flow ഈ ആവശ്യത്തിന് സജ്ജമല്ല. അതിനാൽ മെച്ചപ്പെടുത്തിയ Prompt flow ഒരു പുതിയ രൂപത്തിലാക്കണം.

1. Prompt flow-യിൽ താഴെ പറയുന്ന പ്രവർത്തനങ്ങൾ ചെയ്ത് നിലവിലുള്ള ഫ്ലോ പുനഃസംഘടിപ്പിക്കുക:

    - **Raw file mode** തിരഞ്ഞെടുക്കുക.
    - *flow.dag.yml* ഫയലിലുള്ള എല്ലാ നിലവിലുള്ള കോഡും ഇല്ലാതാക്കുക.
    - *flow.dag.yml* ഒരു താഴെ കൊടുത്തിരിക്കുന്ന കോഡ് ചേർക്കുക.

        ```yml
        inputs:
          input_data:
            type: string
            default: "Who founded Microsoft?"

        outputs:
          answer:
            type: string
            reference: ${integrate_with_promptflow.output}

        nodes:
        - name: integrate_with_promptflow
          type: python
          source:
            type: code
            path: integrate_with_promptflow.py
          inputs:
            input_data: ${inputs.input_data}
        ```

    - **Save** തിരഞ്ഞെടുക്കുക.

    ![Select raw file mode.](../../../../../../translated_images/ml/select-raw-file-mode.06c1eca581ce4f53.webp)

1. താഴെ കൊടുത്തിരിക്കുന്ന കോഡ് *integrate_with_promptflow.py* ഫയലിൽ ചേർക്കുക, കസ്റ്റം Phi-3 / Phi-3.5 മോഡൽ Prompt flow-യിൽ ഉപയോഗിക്കാൻ.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # ലോഗിംഗ് ക്രമീകരണം
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG
    )
    logger = logging.getLogger(__name__)

    def query_phi3_model(input_data: str, connection: CustomConnection) -> str:
        """
        Send a request to the Phi-3 / Phi-3.5 model endpoint with the given input data using Custom Connection.
        """

        # "connection" ആണ് കസ്റ്റം കണക്ട്‌ഷന്റെ പേര്, "endpoint", "key" കസ്റ്റം കണക്ട്‌ഷനിലുള്ള കീകൾ ആണ്
        endpoint_url = connection.endpoint
        api_key = connection.key

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
    data = {
        "input_data": [input_data],
        "params": {
            "temperature": 0.7,
            "max_new_tokens": 128,
            "do_sample": True,
            "return_full_text": True
            }
        }
        try:
            response = requests.post(endpoint_url, json=data, headers=headers)
            response.raise_for_status()
            
            # പൂർണ്ണ JSON പ്രതികരണം ലോഗ് ചെയ്യുക
            logger.debug(f"Full JSON response: {response.json()}")

            result = response.json()["output"]
            logger.info("Successfully received response from Azure ML Endpoint.")
            return result
        except requests.exceptions.RequestException as e:
            logger.error(f"Error querying Azure ML Endpoint: {e}")
            raise

    @tool
    def my_python_tool(input_data: str, connection: CustomConnection) -> str:
        """
        Tool function to process input data and query the Phi-3 / Phi-3.5 model.
        """
        return query_phi3_model(input_data, connection)

    ```

    ![Paste prompt flow code.](../../../../../../translated_images/ml/paste-promptflow-code.cd6d95b101c0ec28.webp)

> [!NOTE]
> Microsoft Foundry-യിൽ Prompt flow ഉപയോഗിക്കുന്നതിനെക്കുറിച്ച് കൂടുതൽ വിശദമായ വിവരങ്ങൾക്ക്, [Prompt flow in Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow) കാണുക.

1. **Chat input**, **Chat output** തിരഞ്ഞെടുത്ത് നിങ്ങളുടെ മോഡലുമായി ചാറ്റ് സാധ്യമാക്കുക.

    ![Select Input Output.](../../../../../../translated_images/ml/select-input-output.c187fc58f25fbfc3.webp)

1. ഇനി നിങ്ങൾക്ക് നിങ്ങളുടെ കസ്റ്റം Phi-3 / Phi-3.5 മോഡലുമായി ചാറ്റ് ചെയ്യാൻ സജ്ജമാണ്. അടുത്ത വ്യായാമത്തിൽ, നിങ്ങൾ എങ്ങനെ Prompt flow ആരംഭിച്ച് ഫൈൻ-ട്യൂൺ ചെയ്ത Phi-3 / Phi-3.5 മോഡലുമായേയും ചാറ്റ് ചെയ്യാമെന്ന് പഠിക്കാം.

> [!NOTE]
>
> പുനഃസംഘടിപ്പിച്ച ഫ്ലോ ചുവടെ കാണുന്ന ചിത്രത്തിന്റെ പോലെയാണ്:
>
> ![Flow example](../../../../../../translated_images/ml/graph-example.82fd1bcdd3fc545b.webp)
>

#### Prompt flow ആരംഭിക്കുക

1. Prompt flow ആരംഭിക്കാൻ **Start compute sessions** തിരഞ്ഞടുക്കുക.

    ![Start compute session.](../../../../../../translated_images/ml/start-compute-session.9acd8cbbd2c43df1.webp)

1. ക്രമീകരണങ്ങൾ പുതുക്കാൻ **Validate and parse input** തിരഞ്ഞടുക്കുക.

    ![Validate input.](../../../../../../translated_images/ml/validate-input.c1adb9543c6495be.webp)

1. നിങ്ങൾ സൃഷ്ടിച്ച കസ്റ്റം കണക്ഷന്റെ **Value** (ഉദാഹരണത്തിന് *connection*) തിരഞ്ഞെടുക്കുക.

    ![Connection.](../../../../../../translated_images/ml/select-connection.1f2b59222bcaafef.webp)

#### നിങ്ങളുടെ കസ്റ്റം Phi-3 / Phi-3.5 മോഡലുമായി ചാറ്റ് ചെയ്യുക

1. **Chat** തിരഞ്ഞടുക്കുക.

    ![Select chat.](../../../../../../translated_images/ml/select-chat.0406bd9687d0c49d.webp)

1. ഫലങ്ങളുടെ ഉദാഹരണം: ഇനി നിങ്ങൾക്ക് നിങ്ങളുടെ കസ്റ്റം Phi-3 / Phi-3.5 മോഡലുമായി ചാറ്റ് ചെയ്യാം. ഫൈന്ട്യൂണിങ്ങിന് ഉപയോഗിച്ച ഡാറ്റ അടിസ്ഥാനമാക്കി ചോദ്യങ്ങൾ ചോദിക്കുന്നതു ഉത്തമം.

    ![Chat with prompt flow.](../../../../../../translated_images/ml/chat-with-promptflow.1cf8cea112359ada.webp)

### Phi-3 / Phi-3.5 മോഡൽ വിലയിരുത്താൻ Azure OpenAI വിന്യസിക്കുക

Microsoft Foundry-യിൽ Phi-3 / Phi-3.5 മോഡൽ വിലയിരുത്താൻ, Azure OpenAI മോഡൽ വിന്യസിക്കണം. Phi-3 / Phi-3.5 മോഡലിന്റെ പ്രകടനം വിലയിരുത്താൻ ഈ മോഡൽ ഉപയോഗിക്കും.

#### Azure OpenAI വിന്യസിക്കുക

1. [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) സൈൻ ഇൻ ചെയ്യുക.

1. നിങ്ങൾ സൃഷ്ടിച്ച Microsoft Foundry പ്രോജക്ടിലേക്ക് നാവിഗേറ്റ് ചെയ്യുക.

    ![Select Project.](../../../../../../translated_images/ml/select-project-created.5221e0e403e2c9d6.webp)

1. നിങ്ങൾ സൃഷ്ടിച്ച പ്രോജക്ടിൽ എഡത്ത് യുടം ടാബിൽ നിന്നു **Deployments** തിരഞ്ഞെടുത്ത്.

1. നാവിഗേഷൻ മെനുവിൽ നിന്നു **+ Deploy model** തിരഞ്ഞെടുത്ത്.

1. **Deploy base model** തിരഞ്ഞെടുത്ത്.

    ![Select Deployments.](../../../../../../translated_images/ml/deploy-openai-model.95d812346b25834b.webp)

1. നിങ്ങൾ ഉപയോഗിക്കാൻ ആഗ്രഹിക്കുന്ന Azure OpenAI മോഡൽ തിരഞ്ഞെടുത്ത്. ഉദാഹരണത്തിന് **gpt-4o**.

    ![Select Azure OpenAI model you'd like to use.](../../../../../../translated_images/ml/select-openai-model.959496d7e311546d.webp)

1. **Confirm** തിരഞ്ഞെടുത്ത്.

### Microsoft Foundry-ന്റെ Prompt flow മൂല്യനിർണ്ണയം ഉപയോഗിച്ച് ഫൈൻ-ട്യൂൺ ചെയ്ത Phi-3 / Phi-3.5 മോഡൽ വിലയിരുത്തുക

### പുതിയ മൂല്യനിർണ്ണയം ആരംഭിക്കുക

1. [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) സന്ദർശിക്കുക.

1. നിങ്ങൾ സൃഷ്ടിച്ച Microsoft Foundry പ്രോജക്ടിലേക്ക് നാവിഗേറ്റ് ചെയ്യുക.

    ![Select Project.](../../../../../../translated_images/ml/select-project-created.5221e0e403e2c9d6.webp)

1. നിങ്ങൾ സൃഷ്ടിച്ച പ്രോജക്ടിൽ എഡത്ത് യുടം ടാബിൽ നിന്നു **Evaluation** തിരഞ്ഞെടുത്ത്.

1. നാവിഗേഷൻ മെനുവിൽ നിന്നു **+ New evaluation** തിരഞ്ഞെടുത്ത്.

    ![Select evaluation.](../../../../../../translated_images/ml/select-evaluation.2846ad7aaaca7f4f.webp)

1. **Prompt flow** മൂല്യനിർണ്ണയം തിരഞ്ഞെടുത്ത്.

    ![Select Prompt flow evaluation.](../../../../../../translated_images/ml/promptflow-evaluation.cb9758cc19b4760f.webp)

1. താഴെ പറയുന്ന പ്രവർത്തനങ്ങൾ ചെയ്യുക:

    - മൂല്യനിർണയത്തിന് ഒരു പേര് രേഖപ്പെടുത്തുക. ഇത് ഒറ്റപ്പെട്ട മൂല്യം ആയിരിക്കണം.
    - **Context ഇല്ലാതെ ചോദ്യോത്തരങ്ങൾ** ജോലി തരം ആയി തിരഞ്ഞെടുക്കുക. കാരണം, ഈ ട്യൂട്ടോറിയലിൽ ഉപയോഗിച്ച **ULTRACHAT_200k** ഡാറ്റാസെറ്റ് കോൺടെക്സ്‌റ്റ് ഉൾക്കൊള്ളുന്നില്ല.
    - വിലയിരുത്താൻ ആഗ്രഹിക്കുന്ന പ്രომპ്റ്റ് ഫ്ളോ തിരഞ്ഞെടുക്കുക.

    ![Prompt flow evaluation.](../../../../../../translated_images/ml/evaluation-setting1.4aa08259ff7a536e.webp)

1. **Next** തിരഞ്ഞെടുത്ത്.

1. താഴെ പറയുന്ന പ്രവർത്തനങ്ങൾ ചെയ്യുക:

    - നിങ്ങളുടെ ഡാറ്റാസെറ്റ് അപ്ലോഡ് ചെയ്യാൻ **Add your dataset** തിരഞ്ഞെടുത്ത്. ഉദാഹരണത്തിന്, **ULTRACHAT_200k** ഡാറ്റാസെറ്റുമായി സംഭവിക്കുന്ന ടെസ്റ്റ് ഡാറ്റാസെറ്റ് ഫയൽ, ഉദാ: *test_data.json1* അപ്ലോഡ് ചെയ്യാം.
    - നിങ്ങളുടെ ഡാറ്റാസെറ്റിനായി യോജിക്കുന്ന **Dataset column** തിരഞ്ഞെടുക്കുക. ഉദാഹരണത്തിന്, **ULTRACHAT_200k** ഡാറ്റാസെറ്റിൽ **${data.prompt}** dataset column ആയി തിരഞ്ഞെടുക്കുക.

    ![Prompt flow evaluation.](../../../../../../translated_images/ml/evaluation-setting2.07036831ba58d64e.webp)

1. **Next** തിരഞ്ഞെടുത്ത്.

1. പ്രകടനവും ഗുണനിലവാരവും മെത്രിക് സെറ്റപ്പ് ചെയ്യാൻ താഴെ പറയുന്ന പ്രവർത്തനങ്ങൾ ചെയ്യുക:

    - ഉപയോഗിക്കാൻ ആഗ്രഹിക്കുന്ന പ്രകടനവും ഗുണനിലവാരവും മെത്രിക് തിരഞ്ഞെടുത്ത്.
    - മൂല്യനിർണയത്തിന് നിങ്ങൾ സൃഷ്ടിച്ച Azure OpenAI മോഡൽ തിരഞ്ഞെടുക്കുക. ഉദാഹരണത്തിന്, **gpt-4o**.

    ![Prompt flow evaluation.](../../../../../../translated_images/ml/evaluation-setting3-1.d1ae69e3bf80914e.webp)

1. അപകടം, സുരക്ഷയുടെ മെത്രിക് ക്രമീകരിക്കാൻ താഴെ പറയുന്ന പ്രവർത്തനങ്ങൾ ചെയ്യുക:

    - ഉപയോഗിക്കാൻ ആഗ്രഹിക്കുന്ന അപകടവും സുരക്ഷാ മീറ്റ്രിക് തിരഞ്ഞെടുത്ത്.
    - പിഴവ് നിരക്ക് കണക്കാക്കുന്നതിനുള്ള ത്രെഷോൾഡ് തിരഞ്ഞെടുക്കുക. ഉദാഹരണത്തിന്, **Medium**.
    - **question**-ൽ, **Data source** ആയി **{$data.prompt}** തിരഞ്ഞെടുക്കുക.
    - **answer**-ലും, **Data source** ആയി **{$run.outputs.answer}** തിരഞ്ഞെടുക്കുക.
    - **ground_truth**-ലും, **Data source** ആയി **{$data.message}** തിരഞ്ഞെടുക്കുക.

    ![Prompt flow evaluation.](../../../../../../translated_images/ml/evaluation-setting3-2.d53bd075c60a45a2.webp)

1. **Next** തിരഞ്ഞെടുത്ത്.

1. മൂല്യനിർണയം ആരംഭിക്കാൻ **Submit** തിരഞ്ഞെടുത്ത്.

1. മൂല്യനിർണയം പൂർത്തിയാകാൻ കുറച്ച് സമയം എടുക്കും. **Evaluation** ടാബിൽ നിന്ന് പുരോഗതി നിരീക്ഷിക്കാം.

### മൂല്യനിർണയ ഫലങ്ങൾ അവലോകനം ചെയ്യുക

> [!NOTE]
> താഴെ കാണിക്കുന്ന ഫലങ്ങൾ മൂല്യനിർണയ പ്രക്രിയ കാണിക്കാൻ മാത്രമാണ്. ഈ ട്യൂട്ടോറിയലിൽ ഉപയോഗിച്ച മോഡൽ സ്വల్ప ഡാറ്റാസെറ്റിൽ ഫൈന്ട്യൂൺ ചെയ്‌തിരുന്നതിനാൽ തൃപ്തികരമല്ലാത്ത ഫലങ്ങൾ ഉണ്ടാകാം. ഉപയോഗിക്കുന്ന ഡാറ്റാസെറ്റിന്റെ വലിപ്പം, ഗുണമേന്‍മ, വൈവിധ്യം, മോഡൽ പ്രത്യേക ക്രമീകരണങ്ങൾ എന്നിവയെ ആശ്രയിച്ചുതന്നെ യഥാർത്ഥ ഫലങ്ങൾ ശ്രദ്ധേയമായി വ്യത്യാസപ്പെടും.

മൂല്യനിർണയം പൂർത്തിയായതിനുശേഷം പ്രകടനവും സുരക്ഷാ മെത്രിക് ഫലങ്ങളും അവലോകനം ചെയ്യാം.
1. പ്രകടനവും ഗുണനിലവാര സൂചകങ്ങളും:

    - സംയോജിതവും, സുതാര്യവുമായ, പ്രസക്തമായ പ്രതികരണങ്ങൾ സൃഷ്ടിക്കാമോ എന്ന് മോഡലിന്റെ ഫലപ്രാപ്തി വിലയിരുത്തുക.

    ![Evaluation result.](../../../../../../translated_images/ml/evaluation-result-gpu.85f48b42dfb74254.webp)

1. അപകടസാധ്യതയും സുരക്ഷാ സൂചകങ്ങളും:

    - മോഡലിന്റെ ഔട്ട്‌പുട്ടുകൾ സുരക്ഷിതവും ഉത്തരവാദിത്വമുള്ള AI സിദ്ധാന്തങ്ങൾക്ക് അനുയോജ്യവുമാണെന്ന് ഉറപ്പാക്കുക, зияരകമായോ അപകീർത്തിചെയ്യുന്ന ഉള്ളടക്കങ്ങളോ ഒഴിവാക്കുക.

    ![Evaluation result.](../../../../../../translated_images/ml/evaluation-result-gpu-2.1b74e336118f4fd0.webp)

1. **വിശദമായ സൂചകങ്ങളുടെയും ഫലങ്ങൾ കാണാനായി** താഴേയ്ക്ക് സ്ക്രോൾ ചെയ്യുക.

    ![Evaluation result.](../../../../../../translated_images/ml/detailed-metrics-result.afa2f5c39a4f5f17.webp)

1. നിങ്ങളുടെ കസ്റ്റം Phi-3 / Phi-3.5 മോഡൽ പ്രകടനവും സുരക്ഷാ സൂചകങ്ങളും അടിസ്ഥാനമാക്കി വിലയിരുത്തി, മോഡൽ ഫലപ്രദമല്ലാതെയും, ഉത്തരവാദിത്വമുള്ള AI പ്രാക്ടിസുകൾ പാലിക്കുന്നതുമാണ് എന്ന് സ്ഥിരീകരിക്കാം, ഇത് യാഥാർത്ഥ്യമായ വിന്യാസത്തിനു തയ്യാറാക്കുന്നു.

## അഭിനന്ദനങ്ങൾ!

### നിങ്ങൾ ഈ പഠനസൂത്രം പൂർത്തിയാക്കി

Microsoft Foundry-യിൽ Prompt flow-ഇനൊപ്പം സംയോജിപ്പിച്ച ഫൈൻ-ട്യൂൺ ചെയ്ത Phi-3 മോഡൽ നിങ്ങൾ വിജയകരമായി വിലയിരുത്തി. നിങ്ങളുടെ AI മോഡലുകൾ മികച്ച പ്രകടനം മാത്രമല്ല, Microsoft-ന്റെ ഉത്തരവാദിത്വമുള്ള AI സിദ്ധാന്തങ്ങളും ಪಾಲിക്കുന്നതായി ഉറപ്പാക്കുന്നതിനുള്ള ഇത് ഒരു গুরুত্বপূর্ণ പടി ആണ്, വിശ്വസനീയവും വിശ്വസ്തവുമായ AI പ്രയോഗങ്ങൾ നിർമ്മിക്കാൻ സഹായിക്കുന്നു.

![Architecture.](../../../../../../translated_images/ml/architecture.10bec55250f5d6a4.webp)

## Azure റിസോഴ്‍സുകൾ ക്ലീൻ അപ്പ് ചെയ്യുക

അക്കൗണ്ടിലേയ്ക്ക് അധിക ചാർജ് വരാതിരുന്നുവാൻ നിങ്ങളുടെ Azure റിസോഴ്‌സുകൾ ക്ലീൻ അപ്പ് ചെയ്യുക. Azure പോർട്ടലിലേക്ക് പോയി താഴെപ്പറയുന്ന റിസോഴ്‌സുകൾ ഇല്ലാതാക്കുക:

- Azure മെഷീൻ ലേണിംഗ് റിസോഴ്‌സ്
- Azure മെഷീൻ ലേണിംഗ് മോഡൽ എന്റ്പോയിന്റ്
- Microsoft Foundry പ്രോജക്ട് റിസോഴ്‌സ്
- Microsoft Foundry Prompt flow റിസോഴ്‌സ്

### അടുത്ത ഘട്ടങ്ങൾ

#### ഡോക്യുമെന്റേഷൻ

- [ഉത്തരവാദിത്വ AI ഡാഷ്ബോർഡ് ഉപയോഗിച്ച് AI സിസ്റ്റങ്ങൾ വിലയിരുത്തുക](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [ജനന AI-യ്ക്ക് മൂല്യനിർണയവും നിരീക്ഷണ സൂചകങ്ങളും](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Microsoft Foundry ഡോക്യുമെന്റേഷൻ](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Prompt flow ഡോക്യുമെന്റേഷൻ](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### പരിശീലന ഉള്ളടക്കം

- [Microsoft-ന്റെ ഉത്തരവാദിത്വ AI സമീപനത്തിന്റെ പരിചയം](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Microsoft Foundry-യുടെ പരിചയം](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### റഫറൻസ്

- [ഉത്തരവാദിത്വ AI എന്താണ്?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [നിങ്ങൾക്ക് കൂടുതൽ സുരക്ഷിതവും വിശ്വസനീയവുമായ ജനന AI പ്രയോഗങ്ങൾ നിർമ്മിക്കാൻ സഹായിക്കുന്ന Azure AI-യിലെ പുതിയ ടൂൾസ് അവതരിപ്പിക്കുന്നു](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [ജനന AI പ്രയോഗങ്ങളുടെ വിലയിരുത്തൽ](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**പ്രതിജ്ഞാപത്രം**:  
ഈ ഡോക്യുമെന്റ് AI പരിഭാഷ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. നമുക്ക് കൃത്യതയ്ക്കായി ശ്രമിക്കുമ്പോഴും, യാന്ത്രിക പരിഭാഷകളിൽ പിശകുകൾ അല്ലെങ്കിൽ അപാകതകൾ ഉണ്ടാകാമെന്ന് ദയവായി ശ്രദ്ധിക്കുക. അതിന്റെ ജന്മഭൂമിയിലെ ഭാഷയിൽ ഉള്ള മൗലിക ഡോക്യുമെന്റ് അതിന്റെ അധികാരപരമായ ഉറവിടമായി കണക്കാക്കണമെന്നും. നിർണായക വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മാനവ പരിഭാഷ რეკമൻഡ് ചെയ്യപ്പെടുന്നു. ഈ പരിഭാഷയുടെ ഉപയോഗത്തിൽ നിന്നുണ്ടാകുന്ന തെറ്റിദ്ധാരണകൾക്കോ ദുർവ്യാഖ്യാനങ്ങൾക്കോ ഞങ്ങൾ ഉത്തരവാദിത്വം ചുമത്തുന്നില്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->