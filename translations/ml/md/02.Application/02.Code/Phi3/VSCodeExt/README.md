# **നിങ്ങളുടെ സ്വന്തം Visual Studio Code GitHub Copilot Chat Microsoft Phi-3 ഫാമിലിയുമായി നിർമ്മിക്കൂ**

GitHub Copilot Chat-ൽ workspace ഏജന്റ് ഉപയോഗിച്ചിട്ടുണ്ടോ? നിങ്ങളുടെ ടീമിന്റെ കോഡ് ഏജന്റ് നിർമ്മിക്കാന്നാ താൽപര്യമുള്ളോ? ഈ ഹാൻഡ്‌സ്-ഓൺ ലാബ് ഓപ്പൺ സോഴ്സ് മോഡൽ സംയോജിപ്പിച്ച് എന്റർപ്രൈസ്-തലമുറ കോഡ് ബിസിനസ് ഏജന്റ് നിർമ്മിക്കാനുള്ള ശ്രമമാണ്.

## **അടിസ്ഥാനങ്ങൾ**

### **Microsoft Phi-3 തിരഞ്ഞെടുക്കുന്നതെന്തുകൊണ്ട്**

Phi-3 ഒരു ഫാമിലി സീരീസ് ആണ്, അതിൽ phi-3-mini, phi-3-small, phi-3-medium എന്നിങ്ങനെ വിവിധ പരിശീലന പതിനങ്ങൾ അടിസ്ഥാനമാക്കി ടെക്സ്റ്റ് ജനറേഷൻ, സംഭാഷണം പൂർത്തീകരിക്കൽ, കോഡ് നിർമ്മാണം എന്നിവയ്ക്കായി വർഗ്ഗീകരിച്ചിരിക്കുന്നു. Vision അടിസ്ഥാനമാക്കിയ phi-3-vision-ഉം ഉണ്ട്. എന്റർപ്രൈസുകൾക്കും വിവിധ ടീമുകൾക്കും ഓഫ്‌ലൈൻ ജനറേറ്റീവ് AI സൊല്യൂഷനുകൾ സൃഷ്ടിക്കാൻ ഇത് അനുയോജ്യമാണ്.

ഈ ലിങ്ക് വായിക്കാൻ ശുപാർശ ചെയ്യുന്നു [https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md](https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md)

### **Microsoft GitHub Copilot Chat**

GitHub Copilot Chat എക്സ്റ്റൻഷൻ ഒരു ചാറ്റ് ഇന്റർഫേസ് നൽകുന്നു, ഇതിലൂടെ GitHub Copilot-നുമായി സംവദിച്ച് കോഡിങ്ങുമായി ബന്ധപ്പെട്ട ചോദ്യങ്ങൾക്കെതിരെ മറുപടികൾ നേരിട്ട് VS Code-ൽ ലഭിക്കും, ഡോക്യുമെന്റേഷൻ തിരയേണ്ടതില്ല, ഓൺലൈൻ ഫോറങ്ങൾ തിരയേണ്ടതില്ല.

Copilot Chat മൊത്തത്തിലുള്ള മറുപടിയിൽ സ്പഷ്ടത കൂട്ടാൻ സിനടാക്സ് ഹൈലൈറ്റിംഗ്, ഇൻഡെൻറേഷൻ, മറ്റ് ഫോർമാറ്റിങ്ങ് സവിശേഷതകൾ ഉപയോഗിക്കാം. ഉപയോക്താവിന്റെ ചോദ്യ തരം അടിസ്ഥാനമാക്കി, ഫലത്തിൽ Copilot മറുപടി സൃഷ്ടിക്കാൻ ഉപയോഗിച്ച സ്രോതസ്സ് കോഡ് ഫയലുകൾ, ഡോക്യുമെന്റേഷൻ എന്നിവയിലേക്കുള്ള ലിങ്കുകളും VS Code ഫംഗ്ഷണാലിറ്റി ആക്സസ് ചെയ്യാനുള്ള ബട്ടണുകളും ഉൾപ്പെടാം.

- Copilot Chat നിങ്ങളുടെ ഡിവലപ്രർ പ്രവাহത്തിൽ ഇന്റഗ്രേറ്റ് ചെയ്ത്, നിങ്ങള്ക്ക് സഹായം ആവശ്യമായിടത്ത് സഹായം നൽകുന്നു:

- എഡിറ്റർ അല്ലെങ്കിൽ ടെർമിനൽ മുതൽ നേരിട്ടുള്ള ഇൻലൈന‍‍‍‍‍‍‍‍‍‍‍‍ ചാറ്റ് സംവദനം ആരംഭിക്കുക, കോഡിങ്ങിനിടയിൽ സഹായം ലഭിക്കാൻ

- ഏതെങ്കിലും സമയത്ത് സഹായം ലഭിക്കേണ്ടത് താൽപര്യമുള്ളപ്പോൾ AI അസിസ്റ്റന്റ് ആയി ചാറ്റ് വ്യൂ ഉപയോഗിക്കുക

- ക്വിക്ക് ചാറ്റ് ആരംഭിച്ച് സംശയം ചോദിച്ച് തുടർന്നുള്ള കാര്യത്തിൽ മടങ്ങുക

GitHub Copilot Chat വിവിധ സാഹചര്യങ്ങളിൽ ഉപയോഗിക്കാം, ഉദാഹരണത്തിന്:

- പ്രശ്നം എങ്ങനെ മികച്ച രീതിയിൽ പരിഹരിക്കാമെന്ന് കോഡിങ്ങ് ചോദ്യങ്ങൾക്ക് മറുപടി നൽകൽ

- മറ്റാരുടെയോ കോഡ് വിശദീകരിച്ച് മെച്ചപ്പെടുത്തലുകൾ നിർദ്ദേശിക്കൽ

- കോഡ് പരിഹാരങ്ങൾ നിർദ്ദേശിക്കൽ

- യൂണിറ്റ് ടെസ്റ്റ് കേസുകൾ നിർമ്മിക്കൽ

- കോഡ് ഡോക്യുമെന്റേഷൻ നിർമ്മിക്കൽ

ഈ ലിങ്ക് വായിക്കാൻ ശുപാർശ ചെയ്യുന്നു [https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/copilot-chat?WT.mc_id=aiml-137032-kinfeylo)

###  **Microsoft GitHub Copilot Chat @workspace**

Copilot Chat-ൽ **@workspace** സാങ്കേതികമാക്കി നിങ്ങളുടെ മുഴുവൻ കോഡ്ബേസ് സംബന്ധിച്ച ചോദ്യങ്ങൾ ചോദിക്കാം. ചോദിച്ച ചോദ്യത്തിന്റെ അടിസ്ഥാനത്തിൽ, Copilot സാദ്ധ്യമായ ഫയലുകളും സിംബോളുകളും വിവേകബുദ്ധിയോടെ തിരയുന്നു, പിന്നീട് അവയെ ലിങ്കുകളും കോഡ് ഉദാഹരണങ്ങളുമായി മറുപടിയിൽ ഉൾപ്പെടുത്തുന്നു.

നിങ്ങളുടെ ചോദ്യത്തിന് മറുപടി നൽകാൻ, **@workspace** VS Code-ൽ ഡിവലപ്പർ കോഡ്ബേസ് നാവിഗേറ്റ് ചെയ്യുമ്പോൾ ഉപയോഗിക്കുന്ന സ്രോതസ്സുകൾ പോലെ തിരയുന്നു:

- .gitignore ഫയൽ അവഗണിക്കുന്ന ഫയലുകൾ ഒഴികെയുള്ള എല്ലാ വർക്‌സ്പേസ് ഫയലുകളും

- നെസ്റ്റുചെയ്ത ഫോൾഡറുകളോടെയുള്ള ഡയറക്ടറി ഘടനയും ഫയലിന്റെ നാമങ്ങളും

- വർക്‌സ്പേസ് GitHub റീഷ്പോസിറ്ററിയായിരുന്നാൽ GitHub-യുടെ കോഡ് സർച്ച് ഇൻഡക്സ്

- വർക്‌സ്പെയ്സിലെ സിംബോളുകളും നിർവചണങ്ങളും

- നിലവിൽ തിരഞ്ഞെടുക്കപ്പെട്ട ടെക്സ്റ്റും സജീവ എഡിറ്ററിൽ ദൃശ്യമായ ടെക്സ്റ്റും

കുറിപ്പ്: .gitignore അവഗണിക്കപ്പെടുന്നു, നിങ്ങൾ ഒരു ഫയൽ തുറന്നിരിക്കുകയാണെങ്കിൽ അല്ലെങ്കിൽ അവഗണിക്കപ്പെട്ട ഫയലിനുള്ളിൽ ടെക്സ്റ്റ് തിരഞ്ഞെടുക്കുകയാണെങ്കിൽ.

ഈ ലിങ്ക് വായിക്കാൻ ശുപാർശ ചെയ്യുന്നു [[https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/workspace-context?WT.mc_id=aiml-137032-kinfeylo)]

## **ഈ ലാബിനെ കുറിച്ച് കൂടുതൽ അറിയുക**

GitHub Copilot എന്റർപ്രൈസുകളുടെ പ്രോഗ്രാമിംഗ് കാര്യക്ഷമത വളരെ വളർത്തുകയും, ഓരോ എന്റർപ്രൈസും GitHub Copilot-ന്റെ അനുയോജ്യമായ സവിശേഷതകൾ കസ്റ്റമൈസ് ചെയ്യാൻ ആഗ്രഹിക്കുന്നു. നിരവധി എന്റർപ്രൈസുകൾ സ്വയം തിരഞ്ഞെടുത്ത ബിസിനസ് സാഹചര്യങ്ങളിലും ഓപ്പൺ സോഴ്സ് മോഡലുകളിലും അടിസ്ഥാനമാക്കി GitHub Copilot പോലുള്ള കസ്റ്റമൈസ് ചെയ്ത എക്സ്റ്റൻഷനുകൾ സൃഷ്ടിച്ചിട്ടുണ്ട്. എന്റർപ്രൈസുകൾക്ക് കസ്റ്റമൈസ് ചെയ്ത എക്സ്റ്റൻഷനുകൾ നിയന്ത്രിക്കാൻ എളുപ്പമാണ്, പക്ഷേ ഇത് ഉപയോക്തൃ അനുഭവത്തെയും ബാധിക്കുന്നു. GitHub Copilot പൊതു സാഹചര്യങ്ങളിലും പ്രൊഫഷണലിസത്തിലും ശക്തമായ സവിശേഷതകൾ ഉള്ളതിനാൽ, അനുഭവം സ്ഥിരതയുള്ളതായും ഉണ്ടായിരുന്നെങ്കിൽ, എന്റർപ്രൈസിന്റെ സ്വന്തം കസ്റ്റമൈസ് ചെയ്ത എക്‌സ്റ്റൻഷൻ ഉപയോഗിക്കുന്നത് മെച്ചമാണ്. GitHub Copilot Chat എന്റർപ്രൈസുകൾക്ക് ചാറ്റ് അനുഭവം വ്യാപിപ്പിക്കാൻ അനുയോജ്യമായ API-കൾ നൽകുന്നു. സ്ഥിരതയുള്ള അനുഭവവും കസ്റ്റമൈസ് ചെയ്ത സവിശേഷതകളും ഉള്ളതിനാൽ നല്ല ഉപയോക്തൃ അനുഭവം ലഭിക്കും.

ഈ ലാബിന് പ്രധാനം Phi-3 മോഡൽ ഉപയോഗിച്ച് ലൊക്കൽ NPUയും Azure ഹൈബ്രിഡും സംയോജിപ്പിച്ച് GitHub Copilot Chat-ൽ ***@PHI3*** എന്ന കസ്റ്റം ഏജന്റ് നിർമ്മിച്ച് എന്റർപ്രൈസ് ഡിവലപ്പർമാർക്ക് കോഡ് ജനറേഷൻ ***(@PHI3 /gen)*** പൂർത്തിയാക്കാനും ചിത്രങ്ങളെ അടിസ്ഥാനമാക്കി കോഡ് നിർമ്മിക്കാൻ ***(@PHI3 /img)*** സഹായിക്കുന്നതാണ്.

![PHI3](../../../../../../../translated_images/ml/cover.1017ebc9a7c46d09.webp)

### ***കുറിപ്പ്:*** 

ഇന്ത്യയിലെ Intel CPU AIPC-നും Apple Silicon-വുമാണ് ഇപ്പോൾ ഈ ലാബ് നടപ്പിലാക്കിയത്. നാം Qualcomm NPU പതിപ്പും തുടർന്നും അപ്ഡേറ്റ് ചെയ്യുന്നതാണ്.


## **ലാബ്**


| പേര് | വിവരണം | AIPC | Apple |
| ------------ | ----------- | -------- |-------- |
| Lab0 - ഇൻസ്റ്റലേഷനുകൾ(✅) | ബന്ധപ്പെട്ട പരിസ്ഥിതികളും ഇൻസ്റ്റലേഷൻ ഉപകരണങ്ങളും ക്രമീകരിക്കുകയും ഇൻസ്റ്റാൾ ചെയ്യുകയും ചെയ്യുക | [Go](./HOL/AIPC/01.Installations.md) |[Go](./HOL/Apple/01.Installations.md) |
| Lab1 - Phi-3-mini ഉപയോഗിച്ച് പ്രംപ്റ്റ് ഫ്ലോ ഓടിക്കുക(✅) | AIPC / Apple Silicon-നൊപ്പം ലൊക്കൽ NPU ഉപയോഗിച്ച് Phi-3-mini മുഖേന കോഡ് ജനറേഷൻ സൃഷ്ടിക്കുക | [Go](./HOL/AIPC/02.PromptflowWithNPU.md) |  [Go](./HOL/Apple/02.PromptflowWithMLX.md) |
| Lab2 - Azure Machine Learning Service-ൽ Phi-3-vision ഡിപ്ലോയ് ചെയ്യുക(✅) | Azure Machine Learning Serviceയുടെ മോഡൽ കാറ്റലോഗ് - Phi-3-vision ഇമേജ് ഡिप്ലോയിൽ കോഡ് സൃഷ്ടിക്കുക | [Go](./HOL/AIPC/03.DeployPhi3VisionOnAzure.md) |[Go](./HOL/Apple/03.DeployPhi3VisionOnAzure.md) |
| Lab3 - GitHub Copilot Chat-ൽ @phi-3 ഏജന്റ് സൃഷ്ടിക്കുക(✅)  | GitHub Copilot Chat-ൽ കസ്റ്റം Phi-3 ഏജന്റ് സൃഷ്ടിച്ച് കോഡ് ജനറേഷൻ, ഗ്രാഫ് ജനറേഷൻ കോഡ്, RAG മുതലായവ പൂർത്തിയാക്കുക | [Go](./HOL/AIPC/04.CreatePhi3AgentInVSCode.md) | [Go](./HOL/Apple/04.CreatePhi3AgentInVSCode.md) |
| സാമ്പിൾ കോഡ് (✅)  | സാമ്പിൾ കോഡ് ഡൗൺലോഡ് ചെയ്യുക | [Go](../../../../../../../code/07.Lab/01/AIPC) | [Go](../../../../../../../code/07.Lab/01/Apple) |


## **അന്വേഷണങ്ങൾ**

1. Phi-3 Cookbook [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook)

2. GitHub Copilot കൂടുതൽ പഠിക്കുക [https://learn.microsoft.com/training/paths/copilot/](https://learn.microsoft.com/training/paths/copilot/?WT.mc_id=aiml-137032-kinfeylo)

3. GitHub Copilot Chat കൂടുതൽ പഠിക്കുക [https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/](https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/?WT.mc_id=aiml-137032-kinfeylo)

4. GitHub Copilot Chat API കൂടുതൽ പഠിക്കുക [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat?WT.mc_id=aiml-137032-kinfeylo)

5. Microsoft Foundry കൂടുതൽ പഠിക്കുക [https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/](https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/?WT.mc_id=aiml-137032-kinfeylo)

6. Microsoft Foundry മോഡൽ കാറ്റലോഗ് കൂടുതൽ പഠിക്കുക [https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അസമ്മതിപ്പ്**:  
ഈ documento AI വിവർത്തന സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്കായി പരിശ്രമിക്കുമ്പോഴും, സ്വയംഭരണ വിവർത്തനങ്ങളിൽ പിശകുകളോ അശുദ്ധികളോ ഉണ്ടാകാം എന്നതിന് ദയവായി ശ്രദ്ധിക്കുക. സാങ്കേതികമായ വിവരംക്കായി, പ്രൊഫഷണൽ മനുഷ്യ വിവർത്തനം ശുപാർശ ചെയ്യുന്നു. ഇത് ഉപയോഗിക്കുന്നതിനാൽ ഉണ്ടാകാൻ സാധ്യതയുള്ള തെറ്റിദ്ധാരണകൾക്കും ദുരവബോധനങ്ങൾക്കും ഞങ്ങൾ ഉത്തരവാദിത്തം ഉയർത്താറില്ല.  
മൂല documento അതിന്റെ തനതായ ഭാഷയിൽ തന്നെ ആധികാരികമായ ഉറവിടമെന്ന് കാണണം.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->