<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3a1e48b628022485aac989c9f733e792",
  "translation_date": "2025-07-17T05:26:34+00:00",
  "source_file": "md/02.QuickStart/AzureAIFoundry_QuickStart.md",
  "language_code": "tl"
}
-->
# **Paggamit ng Phi-3 sa Azure AI Foundry**

Sa pag-unlad ng Generative AI, layunin naming gamitin ang isang pinag-isang platform upang pamahalaan ang iba't ibang LLM at SLM, integrasyon ng datos ng enterprise, fine-tuning/RAG na operasyon, at pagsusuri ng iba't ibang negosyo ng enterprise pagkatapos ng integrasyon ng LLM at SLM, atbp., upang mas mahusay na maipatupad ang mga smart application gamit ang generative AI. Ang [Azure AI Foundry](https://ai.azure.com) ay isang enterprise-level na platform para sa generative AI na aplikasyon.

![aistudo](../../../../translated_images/aifoundry_home.f28a8127c96c7d93.tl.png)

Sa Azure AI Foundry, maaari mong suriin ang mga tugon ng large language model (LLM) at i-orchestrate ang mga bahagi ng prompt application gamit ang prompt flow para sa mas mahusay na performance. Pinapadali ng platform ang scalability para sa pag-transform ng proof of concepts patungo sa ganap na produksyon nang madali. Ang tuloy-tuloy na pagmamanman at pag-refine ay sumusuporta sa pangmatagalang tagumpay.

Mabilis nating maideploy ang Phi-3 model sa Azure AI Foundry sa pamamagitan ng simpleng mga hakbang, at pagkatapos ay magagamit ang Azure AI Foundry para tapusin ang mga kaugnay na gawain tulad ng Playground/Chat, Fine-tuning, pagsusuri, at iba pa.

## **1. Paghahanda**

Kung naka-install na ang [Azure Developer CLI](https://learn.microsoft.com/azure/developer/azure-developer-cli/overview?WT.mc_id=aiml-138114-kinfeylo) sa iyong makina, madali lang gamitin ang template na ito sa pamamagitan ng pagpapatakbo ng command na ito sa isang bagong direktoryo.

## Manwal na Paglikha

Ang paggawa ng Microsoft Azure AI Foundry project at hub ay isang mahusay na paraan upang ayusin at pamahalaan ang iyong AI na mga gawain. Narito ang step-by-step na gabay para makapagsimula ka:

### Paglikha ng Project sa Azure AI Foundry

1. **Pumunta sa Azure AI Foundry**: Mag-sign in sa Azure AI Foundry portal.
2. **Gumawa ng Project**:
   - Kung nasa loob ka ng isang project, piliin ang "Azure AI Foundry" sa itaas kaliwa ng pahina para pumunta sa Home page.
   - Piliin ang "+ Create project".
   - Ilagay ang pangalan ng project.
   - Kung mayroon kang hub, ito ay awtomatikong mapipili. Kung may access ka sa higit sa isang hub, maaari kang pumili ng iba mula sa dropdown. Kung gusto mong gumawa ng bagong hub, piliin ang "Create new hub" at magbigay ng pangalan.
   - Piliin ang "Create".

### Paglikha ng Hub sa Azure AI Foundry

1. **Pumunta sa Azure AI Foundry**: Mag-sign in gamit ang iyong Azure account.
2. **Gumawa ng Hub**:
   - Piliin ang Management center mula sa kaliwang menu.
   - Piliin ang "All resources", pagkatapos ang pababang arrow sa tabi ng "+ New project" at piliin ang "+ New hub".
   - Sa dialog na "Create a new hub", ilagay ang pangalan ng iyong hub (halimbawa, contoso-hub) at baguhin ang iba pang mga field ayon sa nais.
   - Piliin ang "Next", suriin ang impormasyon, at pagkatapos ay piliin ang "Create".

Para sa mas detalyadong mga tagubilin, maaari kang tumingin sa opisyal na [Microsoft documentation](https://learn.microsoft.com/azure/ai-studio/how-to/create-projects).

Pagkatapos ng matagumpay na paglikha, maaari mong ma-access ang studio na ginawa mo sa pamamagitan ng [ai.azure.com](https://ai.azure.com/)

Maaaring magkaroon ng maraming proyekto sa isang AI Foundry. Gumawa ng proyekto sa AI Foundry bilang paghahanda.

Gumawa ng Azure AI Foundry [QuickStarts](https://learn.microsoft.com/azure/ai-studio/quickstarts/get-started-code)

## **2. I-deploy ang Phi model sa Azure AI Foundry**

I-click ang Explore option ng proyekto para pumasok sa Model Catalog at piliin ang Phi-3

Piliin ang Phi-3-mini-4k-instruct

I-click ang 'Deploy' para i-deploy ang Phi-3-mini-4k-instruct model

> [!NOTE]
>
> Maaari kang pumili ng computing power kapag nagde-deploy

## **3. Playground Chat Phi sa Azure AI Foundry**

Pumunta sa deployment page, piliin ang Playground, at makipag-chat sa Phi-3 ng Azure AI Foundry

## **4. Pag-deploy ng Model mula sa Azure AI Foundry**

Para mag-deploy ng model mula sa Azure Model Catalog, sundin ang mga hakbang na ito:

- Mag-sign in sa Azure AI Foundry.
- Piliin ang model na gusto mong i-deploy mula sa Azure AI Foundry model catalog.
- Sa Details page ng model, piliin ang Deploy at pagkatapos ay piliin ang Serverless API na may Azure AI Content Safety.
- Piliin ang proyekto kung saan mo gustong i-deploy ang iyong mga modelo. Para magamit ang Serverless API offering, ang iyong workspace ay dapat kabilang sa East US 2 o Sweden Central na rehiyon. Maaari mong i-customize ang Deployment name.
- Sa deployment wizard, piliin ang Pricing and terms para malaman ang tungkol sa presyo at mga tuntunin ng paggamit.
- Piliin ang Deploy. Maghintay hanggang maging handa ang deployment at ikaw ay ire-redirect sa Deployments page.
- Piliin ang Open in playground para simulan ang pakikipag-interact sa model.
- Maaari kang bumalik sa Deployments page, piliin ang deployment, at tandaan ang endpoint's Target URL at ang Secret Key, na magagamit mo para tawagan ang deployment at gumawa ng mga completion.
- Palaging makikita ang mga detalye ng endpoint, URL, at access keys sa pamamagitan ng pagpunta sa Build tab at pagpili sa Deployments mula sa Components section.

> [!NOTE]
> Tandaan na ang iyong account ay dapat may Azure AI Developer role permissions sa Resource Group para magawa ang mga hakbang na ito.

## **5. Paggamit ng Phi API sa Azure AI Foundry**

Maaari mong ma-access ang https://{Your project name}.region.inference.ml.azure.com/swagger.json gamit ang Postman GET at pagsamahin ito sa Key para malaman ang mga ibinigay na interface

Madali mong makukuha ang mga request parameters, pati na rin ang mga response parameters.

**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.