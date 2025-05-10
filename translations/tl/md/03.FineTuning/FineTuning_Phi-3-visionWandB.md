<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e0a07fd2a30fe2af30b1373df207a5bf",
  "translation_date": "2025-05-09T21:49:31+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Phi-3-visionWandB.md",
  "language_code": "tl"
}
-->
# Phi-3-Vision-128K-Instruct Project Overview

## The Model

Ang Phi-3-Vision-128K-Instruct, isang magaan at makabagong multimodal na modelo, ang sentro ng proyektong ito. Bahagi ito ng pamilya ng Phi-3 model at kayang suportahan ang context length na hanggang 128,000 tokens. Ang modelo ay sinanay gamit ang iba't ibang dataset na kinabibilangan ng synthetic data at maingat na piniling mga pampublikong website, na nakatuon sa mataas na kalidad at reasoning-intensive na nilalaman. Kasama sa proseso ng pagsasanay ang supervised fine-tuning at direct preference optimization upang matiyak ang tumpak na pagsunod sa mga tagubilin, pati na rin ang matibay na mga safety measures.

## Mahalaga ang paggawa ng sample data para sa ilang dahilan:

1. **Testing**: Pinapayagan ka ng sample data na subukan ang iyong aplikasyon sa iba't ibang sitwasyon nang hindi naaapektuhan ang totoong data. Mahalaga ito lalo na sa development at staging phases.

2. **Performance Tuning**: Sa sample data na kahawig ng laki at komplikasyon ng totoong data, maaari mong matukoy ang mga bottleneck sa performance at i-optimize ang iyong aplikasyon nang naaayon.

3. **Prototyping**: Magagamit ang sample data para gumawa ng mga prototype at mockups, na makakatulong sa pag-unawa sa mga pangangailangan ng user at pagkuha ng feedback.

4. **Data Analysis**: Sa data science, madalas gamitin ang sample data para sa exploratory data analysis, pagsasanay ng modelo, at pagsubok ng algorithm.

5. **Security**: Ang paggamit ng sample data sa development at testing environments ay nakakatulong maiwasan ang hindi sinasadyang pag-leak ng sensitibong totoong data.

6. **Learning**: Kapag nag-aaral ng bagong teknolohiya o tool, ang paggamit ng sample data ay nagbibigay ng praktikal na paraan upang mailapat ang mga natutunan.

Tandaan, ang kalidad ng iyong sample data ay malaki ang epekto sa mga aktibidad na ito. Dapat ito ay kasing lapit ng totoong data sa istruktura at pagkakaiba-iba.

### Sample Data Creation
[Generate DataSet Script](./CreatingSampleData.md)

## Dataset

Isang magandang halimbawa ng sample dataset ay ang [DBQ/Burberry.Product.prices.United.States dataset](https://huggingface.co/datasets/DBQ/Burberry.Product.prices.United.States) (makikita sa Huggingface). 
Ang sample dataset ng Burberry products kasama ang metadata tungkol sa kategorya ng produkto, presyo, at pamagat na may kabuuang 3,040 na hanay, bawat isa ay kumakatawan sa isang natatanging produkto. Pinapayagan tayo ng dataset na ito na subukan ang kakayahan ng modelo na intindihin at bigyang-kahulugan ang visual data, na bumubuo ng mga deskriptibong teksto na naglalarawan ng masalimuot na detalye ng imahe at mga katangiang partikular sa brand.

**Note:** Maaari kang gumamit ng anumang dataset na may kasamang mga imahe.

## Complex Reasoning

Kailangang mag-reason ang modelo tungkol sa mga presyo at pangalan batay lamang sa imahe. Nangangailangan ito na hindi lang makilala ng modelo ang mga visual na katangian kundi maunawaan din ang kahulugan nito kaugnay ng halaga ng produkto at branding. Sa pamamagitan ng pagbuo ng tumpak na mga tekstuwal na paglalarawan mula sa mga imahe, ipinapakita ng proyekto ang potensyal ng pagsasama ng visual data upang mapahusay ang performance at kakayahan ng mga modelo sa totoong aplikasyon.

## Phi-3 Vision Architecture

Ang arkitektura ng modelo ay isang multimodal na bersyon ng Phi-3. Pinoproseso nito ang parehong text at image data, pinagsasama ang mga input na ito sa isang pinag-isang sequence para sa malawakang pag-unawa at mga gawain sa pagbuo. Gumagamit ang modelo ng magkahiwalay na embedding layers para sa text at mga imahe. Ang mga text tokens ay kinokonvert sa dense vectors, habang ang mga imahe ay pinoproseso gamit ang CLIP vision model upang makuha ang feature embeddings. Ang mga image embeddings ay ipro-proyekto upang tumugma sa dimensyon ng text embeddings, upang masigurong maayos silang maisasama.

## Integration of Text and Image Embeddings

May mga espesyal na token sa loob ng text sequence na nagsasaad kung saan ipapasok ang mga image embeddings. Sa proseso, pinapalitan ang mga espesyal na token ng katumbas na image embeddings, na nagpapahintulot sa modelo na hawakan ang text at mga imahe bilang isang sequence. Ang prompt para sa dataset namin ay naka-format gamit ang espesyal na <|image|> token gaya ng sumusunod:

```python
text = f"<|user|>\n<|image_1|>What is shown in this image?<|end|><|assistant|>\nProduct: {row['title']}, Category: {row['category3_code']}, Full Price: {row['full_price']}<|end|>"
```

## Sample Code
- [Phi-3-Vision Training Script](../../../../code/03.Finetuning/Phi-3-vision-Trainingscript.py)
- [Weights and Bias Example walkthrough](https://wandb.ai/byyoung3/mlnews3/reports/How-to-fine-tune-Phi-3-vision-on-a-custom-dataset--Vmlldzo4MTEzMTg3)

**Pagsasabi ng Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.