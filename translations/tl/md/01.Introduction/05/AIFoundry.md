<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7b4235159486df4000e16b7b46ddfec3",
  "translation_date": "2025-07-16T22:32:55+00:00",
  "source_file": "md/01.Introduction/05/AIFoundry.md",
  "language_code": "tl"
}
-->
# **Paggamit ng Azure AI Foundry para sa pagsusuri**

![aistudo](../../../../../translated_images/tl/AIFoundry.9e0b513e999a1c5a.webp)

Paano suriin ang iyong generative AI application gamit ang [Azure AI Foundry](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo). Kung sinusuri mo man ang single-turn o multi-turn na mga pag-uusap, nagbibigay ang Azure AI Foundry ng mga kasangkapan para sa pagsusuri ng performance at kaligtasan ng modelo.

![aistudo](../../../../../translated_images/tl/AIPortfolio.69da59a8e1eaa70f.webp)

## Paano suriin ang mga generative AI app gamit ang Azure AI Foundry  
Para sa mas detalyadong gabay, tingnan ang [Azure AI Foundry Documentation](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-generative-ai-app?WT.mc_id=aiml-138114-kinfeylo)

Narito ang mga hakbang para makapagsimula:

## Pagsusuri ng Generative AI Models sa Azure AI Foundry

**Mga Kinakailangan**

- Isang test dataset na nasa CSV o JSON na format.  
- Isang deployed na generative AI model (tulad ng Phi-3, GPT 3.5, GPT 4, o Davinci models).  
- Isang runtime na may compute instance para patakbuhin ang pagsusuri.

## Mga Built-in na Evaluation Metrics

Pinapayagan ka ng Azure AI Foundry na suriin ang parehong single-turn at mas kumplikadong multi-turn na mga pag-uusap.  
Para sa Retrieval Augmented Generation (RAG) na mga senaryo, kung saan ang modelo ay naka-base sa partikular na datos, maaari mong tasahin ang performance gamit ang mga built-in na evaluation metrics.  
Bukod dito, maaari mo ring suriin ang pangkalahatang single-turn question answering na mga senaryo (hindi RAG).

## Paglikha ng Evaluation Run

Mula sa Azure AI Foundry UI, pumunta sa Evaluate page o sa Prompt Flow page.  
Sundin ang evaluation creation wizard para ma-set up ang evaluation run. Magbigay ng opsyonal na pangalan para sa iyong pagsusuri.  
Piliin ang senaryong tumutugma sa layunin ng iyong aplikasyon.  
Pumili ng isa o higit pang evaluation metrics para tasahin ang output ng modelo.

## Custom Evaluation Flow (Opsyonal)

Para sa mas malawak na kakayahan, maaari kang gumawa ng custom evaluation flow. I-customize ang proseso ng pagsusuri ayon sa iyong partikular na pangangailangan.

## Pagtingin sa Resulta

Pagkatapos patakbuhin ang pagsusuri, i-log, tingnan, at suriin ang detalyadong evaluation metrics sa Azure AI Foundry. Makakuha ng mga insight tungkol sa kakayahan at limitasyon ng iyong aplikasyon.

**Note** Azure AI Foundry ay kasalukuyang nasa public preview pa lamang, kaya gamitin ito para sa eksperimento at pag-develop. Para sa production workloads, isaalang-alang ang ibang mga opsyon. Tuklasin ang opisyal na [AI Foundry documentation](https://learn.microsoft.com/azure/ai-studio/?WT.mc_id=aiml-138114-kinfeylo) para sa karagdagang detalye at step-by-step na mga tagubilin.

**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.