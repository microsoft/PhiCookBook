<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "00b7a699de8ac405fa821f4c0f7fc0ab",
  "translation_date": "2025-05-09T19:15:58+00:00",
  "source_file": "md/02.Application/02.Code/Phi3/VSCodeExt/README.md",
  "language_code": "tl"
}
-->
# **Bumuo ng sarili mong Visual Studio Code GitHub Copilot Chat gamit ang Microsoft Phi-3 Family**

Nagamit mo na ba ang workspace agent sa GitHub Copilot Chat? Gusto mo bang gumawa ng sariling code agent para sa iyong team? Layunin ng hands-on lab na ito na pagsamahin ang open source model para makabuo ng enterprise-level na code business agent.

## **Pundasyon**

### **Bakit piliin ang Microsoft Phi-3**

Ang Phi-3 ay isang family series, kabilang ang phi-3-mini, phi-3-small, at phi-3-medium na nakabase sa iba't ibang training parameters para sa text generation, dialogue completion, at code generation. Meron ding phi-3-vision na nakabase sa Vision. Angkop ito para sa mga enterprise o iba't ibang team na gustong gumawa ng offline generative AI solutions.

Inirerekomendang basahin ang link na ito [https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md](https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md)

### **Microsoft GitHub Copilot Chat**

Ang GitHub Copilot Chat extension ay nagbibigay ng chat interface na nagpapahintulot sa iyo na makipag-ugnayan sa GitHub Copilot at makatanggap ng mga sagot sa mga tanong na may kinalaman sa coding diretso sa loob ng VS Code, nang hindi na kailangang mag-browse sa dokumentasyon o maghanap sa online forums.

Maaaring gamitin ng Copilot Chat ang syntax highlighting, indentation, at iba pang formatting features para mas maging malinaw ang sagot na nalikha. Depende sa uri ng tanong mula sa user, maaaring maglaman ang resulta ng mga link sa context na ginamit ng Copilot para gumawa ng sagot, tulad ng mga source code files o dokumentasyon, o mga button para ma-access ang functionality ng VS Code.

- Nakakabit ang Copilot Chat sa workflow ng developer at nagbibigay ng tulong kung saan mo ito kailangan:

- Magsimula ng inline chat conversation diretso mula sa editor o terminal para sa tulong habang nagko-code ka

- Gamitin ang Chat view para magkaroon ng AI assistant sa gilid na handang tumulong anumang oras

- Ilunsad ang Quick Chat para magtanong ng mabilis at makabalik agad sa iyong ginagawa

Maaaring gamitin ang GitHub Copilot Chat sa iba't ibang sitwasyon, tulad ng:

- Pagsagot sa mga tanong tungkol sa coding kung paano pinakamahusay na lutasin ang isang problema

- Pagpapaliwanag ng code ng iba at pagbibigay ng suhestiyon para sa pagpapabuti

- Pagsusulong ng mga code fixes

- Pagbuo ng unit test cases

- Pagbuo ng code documentation

Inirerekomendang basahin ang link na ito [https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/copilot-chat?WT.mc_id=aiml-137032-kinfeylo)


###  **Microsoft GitHub Copilot Chat @workspace**

Ang pagbanggit sa **@workspace** sa Copilot Chat ay nagpapahintulot sa iyo na magtanong tungkol sa buong codebase mo. Batay sa tanong, matalino nitong kinukuha ang mga kaugnay na files at symbols, na pagkatapos ay nirereferensiya sa sagot bilang mga link at code examples.

Para sagutin ang tanong mo, naghahanap ang **@workspace** sa mga parehong pinanggagalingan na ginagamit ng developer kapag nagna-navigate sa codebase sa VS Code:

- Lahat ng files sa workspace, maliban sa mga files na naka-ignore ng .gitignore file

- Directory structure kasama ang mga nested folder at pangalan ng mga file

- GitHub's code search index, kung ang workspace ay isang GitHub repository at naka-index ng code search

- Mga symbols at definitions sa workspace

- Kasalukuyang napiling teksto o nakikitang teksto sa aktibong editor

Tandaan: Binabalewala ang .gitignore kung may bukas kang file o may napiling teksto sa loob ng isang ignored file.

Inirerekomendang basahin ang link na ito [[https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/workspace-context?WT.mc_id=aiml-137032-kinfeylo)]


## **Alamin pa tungkol sa Lab na ito**

Malaki ang naitulong ng GitHub Copilot sa pagpapabilis ng programming sa mga enterprise, at bawat enterprise ay nais i-customize ang mga kaugnay na functionality ng GitHub Copilot. Maraming enterprise ang gumawa ng customized Extensions na kahawig ng GitHub Copilot base sa kanilang sariling business scenarios at open source models. Para sa mga enterprise, mas madali kontrolin ang customized Extensions, ngunit nakakaapekto rin ito sa user experience. Pagkatapos ng lahat, mas malakas ang GitHub Copilot sa pag-handle ng mga general na sitwasyon at pagiging propesyonal. Kung mapapanatili ang consistent na karanasan, mas mainam na i-customize ang sariling Extension ng enterprise. Nagbibigay ang GitHub Copilot Chat ng kaugnay na APIs para sa mga enterprise upang mapalawak ang Chat experience. Ang pagpapanatili ng consistent na karanasan at pagkakaroon ng customized na mga function ay mas magandang user experience.

Gumagamit ang lab na ito ng Phi-3 model na pinagsama sa local NPU at Azure hybrid para bumuo ng custom Agent sa GitHub Copilot Chat ***@PHI3*** upang tulungan ang mga enterprise developers sa pagkompleto ng code generation***(@PHI3 /gen)*** at pagbuo ng code base sa mga imahe ***(@PHI3 /img)***.

![PHI3](../../../../../../../translated_images/cover.410a18b85555fad4ca8bfb8f0b1776a96ae7f8eae1132b8f0c09d4b92b8e3365.tl.png)

### ***Note:*** 

Ang lab na ito ay kasalukuyang ipinatutupad sa AIPC ng Intel CPU at Apple Silicon. Patuloy naming ia-update ang Qualcomm version ng NPU.


## **Lab**


| Pangalan | Deskripsyon | AIPC | Apple |
| ------------ | ----------- | -------- |-------- |
| Lab0 - Installations(✅) | I-configure at i-install ang mga kaugnay na environment at installation tools | [Go](./HOL/AIPC/01.Installations.md) |[Go](./HOL/Apple/01.Installations.md) |
| Lab1 - Run Prompt flow with Phi-3-mini (✅) | Pinagsama sa AIPC / Apple Silicon, gamit ang local NPU para gumawa ng code generation gamit ang Phi-3-mini | [Go](./HOL/AIPC/02.PromptflowWithNPU.md) |  [Go](./HOL/Apple/02.PromptflowWithMLX.md) |
| Lab2 - Deploy Phi-3-vision on Azure Machine Learning Service(✅) | Gumawa ng code sa pamamagitan ng pag-deploy ng Azure Machine Learning Service's Model Catalog - Phi-3-vision image | [Go](./HOL/AIPC/03.DeployPhi3VisionOnAzure.md) |[Go](./HOL/Apple/03.DeployPhi3VisionOnAzure.md) |
| Lab3 - Create a @phi-3 agent in GitHub Copilot Chat(✅)  | Gumawa ng custom Phi-3 agent sa GitHub Copilot Chat para tapusin ang code generation, graph generation code, RAG, atbp. | [Go](./HOL/AIPC/04.CreatePhi3AgentInVSCode.md) | [Go](./HOL/Apple/04.CreatePhi3AgentInVSCode.md) |
| Sample Code (✅)  | I-download ang sample code | [Go](../../../../../../../code/07.Lab/01/AIPC) | [Go](../../../../../../../code/07.Lab/01/Apple) |


## **Mga Resources**

1. Phi-3 Cookbook [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook)

2. Alamin pa tungkol sa GitHub Copilot [https://learn.microsoft.com/training/paths/copilot/](https://learn.microsoft.com/training/paths/copilot/?WT.mc_id=aiml-137032-kinfeylo)

3. Alamin pa tungkol sa GitHub Copilot Chat [https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/](https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/?WT.mc_id=aiml-137032-kinfeylo)

4. Alamin pa tungkol sa GitHub Copilot Chat API [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat?WT.mc_id=aiml-137032-kinfeylo)

5. Alamin pa tungkol sa Azure AI Foundry [https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/](https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/?WT.mc_id=aiml-137032-kinfeylo)

6. Alamin pa tungkol sa Azure AI Foundry's Model Catalog [https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview)

**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o kamalian. Ang orihinal na dokumento sa kanyang likas na wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.