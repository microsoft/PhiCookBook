# Phi-3-Vision-128K-Instruct Pangkalahatang-ideya ng Proyekto

## Ang Modelo

Ang Phi-3-Vision-128K-Instruct, isang magaan at makabagong multimodal na modelo, ang sentro ng proyektong ito. Bahagi ito ng pamilya ng Phi-3 na modelo at sumusuporta sa haba ng konteksto na hanggang 128,000 token. Ang modelo ay sinanay gamit ang isang malawak na dataset na kinabibilangan ng synthetic na datos at maingat na piniling mga pampublikong website, na nagbibigay-diin sa mataas na kalidad at reasoning-intensive na nilalaman. Kasama sa proseso ng pagsasanay ang supervised fine-tuning at direktang preference optimization upang matiyak ang tumpak na pagsunod sa mga tagubilin, pati na rin ang matibay na mga hakbang sa kaligtasan.

## Mahalaga ang paggawa ng sample data para sa ilang mga dahilan:

1. **Pagsubok**: Pinapayagan ka ng sample data na subukan ang iyong aplikasyon sa iba't ibang mga sitwasyon nang hindi naaapektuhan ang totoong datos. Mahalaga ito lalo na sa mga yugto ng pag-develop at staging.

2. **Pag-tune ng Performance**: Sa sample data na kahawig ng laki at kumplikasyon ng totoong datos, maaari mong matukoy ang mga bottleneck sa performance at i-optimize ang iyong aplikasyon nang naaayon.

3. **Prototyping**: Maaaring gamitin ang sample data upang gumawa ng mga prototype at mockup, na makakatulong sa pag-unawa sa mga pangangailangan ng gumagamit at pagkuha ng feedback.

4. **Pagsusuri ng Datos**: Sa data science, madalas gamitin ang sample data para sa exploratory data analysis, pagsasanay ng modelo, at pagsusuri ng mga algorithm.

5. **Seguridad**: Ang paggamit ng sample data sa mga development at testing environment ay makakatulong upang maiwasan ang aksidenteng pag-leak ng sensitibong totoong datos.

6. **Pagkatuto**: Kung nag-aaral ka ng bagong teknolohiya o tool, ang paggamit ng sample data ay nagbibigay ng praktikal na paraan upang mailapat ang iyong mga natutunan.

Tandaan, ang kalidad ng iyong sample data ay malaki ang epekto sa mga aktibidad na ito. Dapat itong maging kasing lapit ng totoong datos sa estruktura at pagkakaiba-iba.

### Paggawa ng Sample Data
[Generate DataSet Script](./CreatingSampleData.md)

## Dataset

Isang magandang halimbawa ng sample dataset ay ang [DBQ/Burberry.Product.prices.United.States dataset](https://huggingface.co/datasets/DBQ/Burberry.Product.prices.United.States) (makukuha sa Huggingface).  
Ang sample dataset ng mga produkto ng Burberry kasama ang metadata tungkol sa kategorya ng produkto, presyo, at pamagat ay may kabuuang 3,040 na hilera, bawat isa ay kumakatawan sa isang natatanging produkto. Pinapayagan tayo ng dataset na ito na subukan ang kakayahan ng modelo na maunawaan at bigyang-kahulugan ang visual na datos, na bumubuo ng mga deskriptibong teksto na sumasalamin sa masalimuot na detalye ng imahe at mga katangiang partikular sa tatak.

**Note:** Maaari kang gumamit ng anumang dataset na may kasamang mga larawan.

## Masalimuot na Pangangatwiran

Kailangang mag-analisa ang modelo tungkol sa mga presyo at pangalan batay lamang sa larawan. Nangangailangan ito na hindi lang makilala ng modelo ang mga visual na katangian kundi maunawaan din ang mga implikasyon nito sa halaga ng produkto at branding. Sa pamamagitan ng pagsasama-sama ng tumpak na mga tekstuwal na paglalarawan mula sa mga larawan, ipinapakita ng proyekto ang potensyal ng pagsasama ng visual na datos upang mapabuti ang performance at kakayahan ng mga modelo sa mga totoong aplikasyon.

## Arkitektura ng Phi-3 Vision

Ang arkitektura ng modelo ay isang multimodal na bersyon ng Phi-3. Pinoproseso nito ang parehong teksto at larawan, pinagsasama ang mga input na ito sa isang pinag-isang sekwensya para sa mas malawak na pag-unawa at mga gawain sa pagbuo. Gumagamit ang modelo ng magkahiwalay na embedding layers para sa teksto at mga larawan. Ang mga text token ay kinokonvert sa dense vectors, habang ang mga larawan ay pinoproseso gamit ang CLIP vision model upang makuha ang mga feature embeddings. Ang mga image embeddings na ito ay ipinro-project upang tumugma sa dimensyon ng text embeddings, na tinitiyak na maaari silang pagsamahin nang maayos.

## Pagsasama ng Text at Image Embeddings

May mga espesyal na token sa loob ng text sequence na nagsasaad kung saan ipapasok ang image embeddings. Sa panahon ng pagproseso, ang mga espesyal na token na ito ay pinapalitan ng kaukulang image embeddings, na nagpapahintulot sa modelo na hawakan ang teksto at mga larawan bilang isang solong sekwensya. Ang prompt para sa aming dataset ay naka-format gamit ang espesyal na <|image|> token tulad ng sumusunod:

```python
text = f"<|user|>\n<|image_1|>What is shown in this image?<|end|><|assistant|>\nProduct: {row['title']}, Category: {row['category3_code']}, Full Price: {row['full_price']}<|end|>"
```

## Halimbawang Code
- [Phi-3-Vision Training Script](../../../../code/03.Finetuning/Phi-3-vision-Trainingscript.py)
- [Weights and Bias Example walkthrough](https://wandb.ai/byyoung3/mlnews3/reports/How-to-fine-tune-Phi-3-vision-on-a-custom-dataset--Vmlldzo4MTEzMTg3)

**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.