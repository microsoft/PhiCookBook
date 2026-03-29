# **Bumuo ng sarili mong Visual Studio Code GitHub Copilot Chat gamit ang Pamilya ng Microsoft Phi-3**

Gumamit ka na ba ng workspace agent sa GitHub Copilot Chat? Nais mo bang bumuo ng sariling code agent para sa iyong koponan? Ang hands-on na lab na ito ay umaasang pagsamahin ang open source na modelo upang bumuo ng enterprise-level na business agent para sa code.

## **Pundasyon**

### **Bakit piliin ang Microsoft Phi-3**

Ang Phi-3 ay isang family series, kabilang ang phi-3-mini, phi-3-small, at phi-3-medium batay sa iba't ibang training parameters para sa text generation, dialogue completion, at code generation. Mayroon ding phi-3-vision na nakabase sa Vision. Ito ay angkop para sa mga enterprise o iba't ibang koponan upang lumikha ng offline generative AI solutions.

Inirerekomendang basahin ang link na ito [https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md](https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md)

### **Microsoft GitHub Copilot Chat**

Ang GitHub Copilot Chat extension ay nagbibigay sa iyo ng chat interface na nagpapahintulot sa iyo na makipag-ugnayan sa GitHub Copilot at makatanggap ng mga sagot sa mga tanong na may kaugnayan sa coding nang direkta sa loob ng VS Code, nang hindi kailangan mag-navigate sa dokumentasyon o maghanap sa mga online forum.

Maaaring gumamit ang Copilot Chat ng syntax highlighting, indentation, at iba pang mga formatting feature upang magdagdag ng kalinawan sa mga generated na sagot. Depende sa uri ng tanong mula sa user, ang resulta ay maaaring maglaman ng mga link sa konteksto na ginamit ng Copilot para bumuo ng sagot, tulad ng mga source code file o dokumentasyon, o mga button para sa pag-access ng functionality ng VS Code.

- Ang Copilot Chat ay nag-iintegrate sa iyong developer flow at nagbibigay ng tulong kung saan mo ito kailangan:

- Magsimula ng inline chat conversation nang direkta mula sa editor o terminal para sa tulong habang nagka-code

- Gamitin ang Chat view upang magkaroon ng AI assistant sa gilid na tutulong sa iyo anumang oras

- I-launch ang Quick Chat upang magtanong ng mabilis na tanong at bumalik agad sa iyong ginagawa

Maaari mong gamitin ang GitHub Copilot Chat sa iba't ibang senaryo, gaya ng:

- Pagsagot sa mga tanong sa coding kung paano pinakamahusay na lutasin ang isang problema

- Paliwanag sa code ng iba at pagbibigay ng mga suhestiyon para sa pagpapabuti

- Pagsumite ng mga ayos sa code

- Pag-generate ng mga unit test case

- Pag-generate ng dokumentasyon ng code

Inirerekomendang basahin ang link na ito [https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/copilot-chat?WT.mc_id=aiml-137032-kinfeylo)


###  **Microsoft GitHub Copilot Chat @workspace**

Ang pag-refer sa **@workspace** sa Copilot Chat ay nagbibigay-daan sa iyong magtanong tungkol sa buong codebase mo. Batay sa tanong, matalino nitong kinukuha ang mga kaugnay na file at simbolo na pagkatapos ay nirereferensya sa sagot bilang mga link at code example.

Para sagutin ang iyong tanong, ang **@workspace** ay naghahanap sa parehong mga pinanggagalingan na ginagamit ng developer kapag nagba-browse ng isang codebase sa VS Code:

- Lahat ng file sa workspace, maliban sa mga file na iniiwasan ng .gitignore na file

- Directory structure na may mga nested folder at pangalan ng mga file

- GitHub code search index, kung ang workspace ay isang GitHub repository at na-index ng code search

- Mga simbolo at definisyon sa workspace

- Kasalukuyang napiling teksto o nakikitang teksto sa aktibong editor

Tandaan: Pinapalampas ang .gitignore kung may bukas kang file o may napiling teksto sa loob ng isang ignored file.

Inirerekomendang basahin ang link na ito [[https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/workspace-context?WT.mc_id=aiml-137032-kinfeylo)]


## **Alamin pa tungkol sa Lab na ito**

Malaki ang naitulong ng GitHub Copilot sa pagpapabuti ng kahusayan sa programming ng mga enterprise, at inaasahan ng bawat enterprise na i-customize ang mga kaugnay na function ng GitHub Copilot. Maraming mga enterprise ang nag-customize ng mga Extension na katulad ng GitHub Copilot base sa kanilang sariling business scenario at open source model. Para sa mga enterprise, mas madaling kontrolin ang mga customized Extension, ngunit nakakaapekto ito sa karanasan ng user. Pagkatapos ng lahat, mas malakas ang mga function ng GitHub Copilot sa pagharap sa mga pangkalahatang scenario at propesyonalismo. Kung mapananatili ang consistent na karanasan, mas maganda ang mag-customize ng sariling enterprise na Extension. Nagbibigay ang GitHub Copilot Chat ng mga kaugnay na API para sa mga enterprise upang mapalawak ang karanasan sa Chat. Ang pagpapanatili ng consistent na karanasan at pagkakaroon ng mga customized na function ay mas magandang karanasan para sa user.

Ang lab na ito ay pangunahing gumagamit ng Phi-3 model na pinagsama sa lokal na NPU at Azure hybrid upang bumuo ng custom Agent sa GitHub Copilot Chat ***@PHI3*** upang tulungan ang mga enterprise developer sa pagkumpleto ng code generation***(@PHI3 /gen)*** at pag-generate ng code batay sa mga larawan ***(@PHI3 /img)***.

![PHI3](../../../../../../../translated_images/tl/cover.1017ebc9a7c46d09.webp)

### ***Tandaan:*** 

Ang lab na ito ay kasalukuyang ipinatupad sa AIPC ng Intel CPU at Apple Silicon. Patuloy naming ia-update ang Qualcomm na bersyon ng NPU.


## **Lab**


| Pangalan | Paglalarawan | AIPC | Apple |
| ------------ | ----------- | -------- |-------- |
| Lab0 - Installations(✅) | I-configure at i-install ang mga kaugnay na environment at mga installation tool | [Go](./HOL/AIPC/01.Installations.md) |[Go](./HOL/Apple/01.Installations.md) |
| Lab1 - Run Prompt flow with Phi-3-mini (✅) | Pinagsama sa AIPC / Apple Silicon, gamit ang lokal na NPU upang gumawa ng code generation gamit ang Phi-3-mini | [Go](./HOL/AIPC/02.PromptflowWithNPU.md) |  [Go](./HOL/Apple/02.PromptflowWithMLX.md) |
| Lab2 - Deploy Phi-3-vision on Azure Machine Learning Service(✅) | Gumawa ng code sa pamamagitan ng pag-deploy ng Azure Machine Learning Service's Model Catalog - Phi-3-vision image | [Go](./HOL/AIPC/03.DeployPhi3VisionOnAzure.md) |[Go](./HOL/Apple/03.DeployPhi3VisionOnAzure.md) |
| Lab3 - Create a @phi-3 agent in GitHub Copilot Chat(✅)  | Lumikha ng custom Phi-3 agent sa GitHub Copilot Chat upang kumpletuhin ang code generation, graph generation code, RAG, atbp. | [Go](./HOL/AIPC/04.CreatePhi3AgentInVSCode.md) | [Go](./HOL/Apple/04.CreatePhi3AgentInVSCode.md) |
| Sample Code (✅)  | I-download ang sample code | [Go](../../../../../../../code/07.Lab/01/AIPC) | [Go](../../../../../../../code/07.Lab/01/Apple) |


## **Mga Resources**

1. Phi-3 Cookbook [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook)

2. Alamin pa ang tungkol sa GitHub Copilot [https://learn.microsoft.com/training/paths/copilot/](https://learn.microsoft.com/training/paths/copilot/?WT.mc_id=aiml-137032-kinfeylo)

3. Alamin pa ang tungkol sa GitHub Copilot Chat [https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/](https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/?WT.mc_id=aiml-137032-kinfeylo)

4. Alamin pa ang tungkol sa GitHub Copilot Chat API [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat?WT.mc_id=aiml-137032-kinfeylo)

5. Alamin pa ang tungkol sa Microsoft Foundry [https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/](https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/?WT.mc_id=aiml-137032-kinfeylo)

6. Alamin pa ang tungkol sa Model Catalog ng Microsoft Foundry [https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI na pagsasalin na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga error o kamalian. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na opisyal na sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot para sa anumang hindi pagkakaintindihan o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->