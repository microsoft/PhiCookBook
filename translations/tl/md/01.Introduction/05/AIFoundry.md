# **Paggamit ng Microsoft Foundry para sa Pagsusuri**

![aistudo](../../../../../translated_images/tl/AIFoundry.9e0b513e999a1c5a.webp)

Paano suriin ang iyong generative AI application gamit ang [Microsoft Foundry](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo). Kung ikaw ay nagsusuri ng single-turn o multi-turn na mga pag-uusap, nagbibigay ang Microsoft Foundry ng mga kasangkapan para sa pagsusuri ng performance at kaligtasan ng modelo.

![aistudo](../../../../../translated_images/tl/AIPortfolio.69da59a8e1eaa70f.webp)

## Paano suriin ang mga generative AI apps gamit ang Microsoft Foundry
Para sa mas detalyadong instruksyon, tingnan ang [Microsoft Foundry Documentation](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-generative-ai-app?WT.mc_id=aiml-138114-kinfeylo)

Narito ang mga hakbang upang makapagsimula:

## Pagsusuri ng mga Generative AI Models sa Microsoft Foundry

**Mga Kinakailangan**

- Isang test dataset na nasa CSV o JSON na format.
- Isang deployed na generative AI model (tulad ng Phi-3, GPT 3.5, GPT 4, o Davinci models).
- Isang runtime na may compute instance upang patakbuhin ang pagsusuri.

## Mga Built-in na Evaluation Metrics

Pinapayagan ng Microsoft Foundry na suriin ang parehong single-turn at complex, multi-turn na mga pag-uusap.
Para sa Retrieval Augmented Generation (RAG) scenarios, kung saan ang modelo ay naka-base sa partikular na datos, maaari mong suriin ang performance gamit ang mga built-in na evaluation metrics.
Bukod dito, maaari mo ring suriin ang general single-turn question answering scenarios (hindi RAG).

## Paglikha ng Evaluation Run

Mula sa Microsoft Foundry UI, pumunta sa Evaluate page o sa Prompt Flow page.
Sundin ang evaluation creation wizard upang mag-setup ng evaluation run. Magbigay ng optional na pangalan para sa iyong pagsusuri.
Piliin ang scenario na naaayon sa layunin ng iyong aplikasyon.
Pumili ng isa o higit pang evaluation metrics upang suriin ang output ng modelo.

## Custom Evaluation Flow (Opsyonal)

Para sa mas mataas na kakayahang mag-ayos, maaari kang magtayo ng custom evaluation flow. I-customize ang proseso ng pagsusuri base sa iyong mga partikular na pangangailangan.

## Pagsilip sa Resulta

Pagkatapos patakbuhin ang pagsusuri, i-log, tingnan, at suriin ang detalyadong evaluation metrics sa Microsoft Foundry. Makakuha ng mga pananaw tungkol sa kakayahan at limitasyon ng iyong aplikasyon.



**Note** Kasalukuyang nasa public preview pa ang Microsoft Foundry, kaya gamitin ito para sa eksperimento at mga layunin sa pag-develop. Para sa production workloads, isaalang-alang ang ibang mga opsyon. Tuklasin ang opisyal na [AI Foundry documentation](https://learn.microsoft.com/azure/ai-studio/?WT.mc_id=aiml-138114-kinfeylo) para sa higit pang detalye at step-by-step na mga instruksyon.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagaman nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga error o pagkakamali. Ang orihinal na dokumento sa kanyang orihinal na wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang mga maling pagkaunawa o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->