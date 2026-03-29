# **Paggamit ng Phi-3 sa Microsoft Foundry**

Sa pag-unlad ng Generative AI, umaasa kami na gamitin ang isang pinag-isang plataporma upang pamahalaan ang iba't ibang LLM at SLM, enterprise data integration, fine-tuning/RAG operations, at ang pagsusuri ng iba't ibang enterprise business matapos isama ang LLM at SLM, atbp., upang mas mahusay na maipatupad ang mga smart application ng generative AI. Ang [Microsoft Foundry](https://ai.azure.com) ay isang enterprise-level na generative AI application platform.

![aistudo](../../../../translated_images/tl/aifoundry_home.f28a8127c96c7d93.webp)

Sa Microsoft Foundry, maaari mong suriin ang mga tugon ng large language model (LLM) at i-orchestrate ang mga prompt application components gamit ang prompt flow para sa mas mahusay na performance. Pinadadali ng plataporma ang scalability para sa pag-transform ng mga proof of concepts tungo sa ganap na produksyon nang madali. Sinusuportahan nito ang patuloy na monitoring at refinement para sa pangmatagalang tagumpay.

Mabilis nating maideploy ang Phi-3 model sa Microsoft Foundry gamit ang simpleng mga hakbang, at pagkatapos ay gamitin ang Microsoft Foundry upang kumpletuhin ang mga kaugnay na gawain tulad ng Playground/Chat, Fine-tuning, pagsusuri, at iba pa na may kaugnayan sa Phi-3.

## **1. Paghahanda**

Kung mayroon ka nang naka-install na [Azure Developer CLI](https://learn.microsoft.com/azure/developer/azure-developer-cli/overview?WT.mc_id=aiml-138114-kinfeylo) sa iyong makina, ang paggamit ng template na ito ay kasing dali ng pagpapatakbo ng command na ito sa isang bagong direktoryo.

## Manwal na Paglikha

Ang paggawa ng proyekto at hub sa Microsoft Foundry ay isang mahusay na paraan upang ayusin at pamahalaan ang iyong AI na gawain. Narito ang gabay na hakbang-hakbang upang makapagsimula ka:

### Paglikha ng Proyekto sa Microsoft Foundry

1. **Pumunta sa Microsoft Foundry**: Mag-sign in sa Microsoft Foundry portal.
2. **Gumawa ng Proyekto**:
   - Kung nasa isang proyekto ka, piliin ang "Microsoft Foundry" sa itaas kaliwa ng pahina upang pumunta sa Home page.
   - Piliin ang "+ Create project".
   - I-enter ang pangalan ng proyekto.
   - Kung mayroon kang hub, ito ay awtomatikong mapipili. Kung may access ka sa higit sa isang hub, maaari kang pumili ng iba mula sa dropdown. Kung nais mong gumawa ng bagong hub, piliin ang "Create new hub" at magbigay ng pangalan.
   - Piliin ang "Create".

### Paglikha ng Hub sa Microsoft Foundry

1. **Pumunta sa Microsoft Foundry**: Mag-sign in gamit ang iyong Azure account.
2. **Gumawa ng Hub**:
   - Piliin ang Management center mula sa kaliwang menu.
   - Piliin ang "All resources", pagkatapos ay ang down arrow sa tabi ng "+ New project" at piliin ang "+ New hub".
   - Sa dialog na "Create a new hub", ilagay ang pangalan para sa iyong hub (hal., contoso-hub) at baguhin ang iba pang mga field ayon sa nais.
   - Piliin ang "Next", suriin ang impormasyon, at pagkatapos ay piliin ang "Create".

Para sa mas detalyadong mga tagubilin, maaari kang sumangguni sa opisyal na [Microsoft documentation](https://learn.microsoft.com/azure/ai-studio/how-to/create-projects).

Pagkatapos ng matagumpay na paglikha, maaari mong ma-access ang studio na iyong ginawa sa pamamagitan ng [ai.azure.com](https://ai.azure.com/)

Maaaring magkaroon ng maraming proyekto sa isang AI Foundry. Gumawa ng proyekto sa AI Foundry bilang paghahanda.

Gumawa ng Microsoft Foundry [QuickStarts](https://learn.microsoft.com/azure/ai-studio/quickstarts/get-started-code)


## **2. I-deploy ang Phi model sa Microsoft Foundry**

I-click ang Explore option ng proyekto upang pumasok sa Model Catalog at piliin ang Phi-3

Piliin ang Phi-3-mini-4k-instruct

I-click ang 'Deploy' upang i-deploy ang modelong Phi-3-mini-4k-instruct

> [!NOTE]
>
> Maaari kang pumili ng computing power kapag nagde-deploy

## **3. Playground Chat Phi sa Microsoft Foundry**

Pumunta sa deployment page, piliin ang Playground, at makipag-chat sa Phi-3 ng Microsoft Foundry

## **4. Pagde-deploy ng Modelo mula sa Microsoft Foundry**

Upang mag-deploy ng modelo mula sa Azure Model Catalog, sundin ang mga hakbang na ito:

- Mag-sign in sa Microsoft Foundry.
- Pumili ng modelong nais mong i-deploy mula sa Microsoft Foundry model catalog.
- Sa pahina ng Detalye ng modelo, piliin ang Deploy pagkatapos ay piliin ang Serverless API with Azure AI Content Safety.
- Piliin ang proyekto kung saan nais mong i-deploy ang iyong mga modelo. Upang magamit ang Serverless API offering, kailangang kabilang ang iyong workspace sa rehiyon ng East US 2 o Sweden Central. Maaari mong i-customize ang Deployment name.
- Sa deployment wizard, piliin ang Pricing and terms upang malaman ang tungkol sa presyo at mga kondisyong gamit.
- Piliin ang Deploy. Hintayin hanggang ang deployment ay handa na at ikaw ay ire-redirect sa Deployments page.
- Piliin ang Open in playground upang simulan ang pakikipag-ugnayan sa modelo.
- Maaari kang bumalik sa Deployments page, piliin ang deployment, at tandaan ang endpoint's Target URL at ang Secret Key, na maaari mong gamitin upang tawagan ang deployment at gumawa ng mga completion.
- Palaging makikita ang mga detalye ng endpoint, URL, at access keys sa pamamagitan ng pagpunta sa Build tab at pagpili ng Deployments mula sa Components section.

> [!NOTE]
> Pakitandaan na ang iyong account ay kailangang magkaroon ng Azure AI Developer role permissions sa Resource Group upang maisagawa ang mga hakbang na ito.

## **5. Paggamit ng Phi API sa Microsoft Foundry**

Maaari kang mag-access sa https://{Your project name}.region.inference.ml.azure.com/swagger.json gamit ang Postman GET at i-combine ito sa Key upang matutunan ang tungkol sa mga ibinigay na interface

Maaari mong makuha ang mga request parameters nang napakadali, pati na rin ang response parameters.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang serbisyong AI na pagsasalin na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, mangyaring tandaan na maaaring maglaman ng mga error o kamalian ang mga awtomatikong pagsasalin. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na opisyal na sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->