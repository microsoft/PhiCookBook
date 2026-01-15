<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "743d7e9cb9c4e8ea642d77bee657a7fa",
  "translation_date": "2025-07-17T09:59:34+00:00",
  "source_file": "md/03.FineTuning/LetPhi3gotoIndustriy.md",
  "language_code": "tl"
}
-->
# **Pahintulutan ang Phi-3 na maging eksperto sa industriya**

Para mailapat ang Phi-3 model sa isang industriya, kailangan mong idagdag ang datos ng negosyo ng industriya sa Phi-3 model. Mayroon tayong dalawang opsyon, ang una ay RAG (Retrieval Augmented Generation) at ang pangalawa ay Fine Tuning.

## **RAG vs Fine-Tuning**

### **Retrieval Augmented Generation**

Ang RAG ay kombinasyon ng pagkuha ng datos at pagbuo ng teksto. Ang nakaayos at hindi nakaayos na datos ng kumpanya ay iniimbak sa vector database. Kapag naghahanap ng kaugnay na nilalaman, hinahanap ang kaugnay na buod at nilalaman upang bumuo ng konteksto, at pinagsasama ito sa kakayahan ng LLM/SLM sa pagkompleto ng teksto upang makabuo ng nilalaman.

### **Fine-tuning**

Ang Fine-tuning ay nakabatay sa pagpapabuti ng isang partikular na modelo. Hindi kailangang simulan sa algorithm ng modelo, ngunit kailangang patuloy na mag-ipon ng datos. Kung nais mo ng mas tumpak na terminolohiya at pagpapahayag ng wika sa mga aplikasyon sa industriya, mas mainam ang fine-tuning. Ngunit kung madalas magbago ang iyong datos, maaaring maging komplikado ang fine-tuning.

### **Paano pumili**

1. Kung ang sagot ay nangangailangan ng pagdagdag ng panlabas na datos, RAG ang pinakamainam na piliin.

2. Kung kailangan mo ng matatag at tumpak na kaalaman sa industriya, magandang piliin ang fine-tuning. Pinapahalagahan ng RAG ang paghahanap ng kaugnay na nilalaman ngunit maaaring hindi palaging makuha ang mga espesyalisadong detalye.

3. Nangangailangan ang fine-tuning ng mataas na kalidad na datos, at kung maliit lang ang saklaw ng datos, hindi ito gaanong makakaapekto. Mas flexible ang RAG.

4. Ang fine-tuning ay parang black box, mahirap maintindihan ang internal na mekanismo. Ngunit mas madali sa RAG na matunton ang pinagmulan ng datos, kaya mas epektibong naiaayos ang mga hallucination o pagkakamali sa nilalaman at nagbibigay ng mas malinaw na transparency.

### **Mga senaryo**

1. Ang mga vertical na industriya na nangangailangan ng espesipikong bokabularyo at pagpapahayag, ***Fine-tuning*** ang pinakamainam.

2. Sa QA system na nangangailangan ng pagsasama-sama ng iba't ibang punto ng kaalaman, ***RAG*** ang pinakamainam.

3. Ang kombinasyon ng automated na daloy ng negosyo ***RAG + Fine-tuning*** ang pinakamainam.

## **Paano gamitin ang RAG**

![rag](../../../../translated_images/tl/rag.2014adc59e6f6007.png)

Ang vector database ay koleksyon ng datos na iniimbak sa anyong matematikal. Pinapadali ng vector databases para sa mga machine learning model na maalala ang mga naunang input, kaya nagagamit ang machine learning para suportahan ang mga kaso tulad ng paghahanap, rekomendasyon, at pagbuo ng teksto. Nakikilala ang datos base sa pagkakatulad kaysa eksaktong tugma, kaya naiintindihan ng mga computer model ang konteksto ng datos.

Ang vector database ang susi para maisakatuparan ang RAG. Maaari nating i-convert ang datos sa vector storage gamit ang mga vector model tulad ng text-embedding-3, jina-ai-embedding, atbp.

Alamin pa kung paano gumawa ng RAG application [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?WT.mc_id=aiml-138114-kinfeylo)

## **Paano gamitin ang Fine-tuning**

Ang karaniwang ginagamit na algorithm sa Fine-tuning ay Lora at QLora. Paano pumili?
- [Alamin pa gamit ang sample notebook na ito](../../../../code/04.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Halimbawa ng Python FineTuning Sample](../../../../code/04.Finetuning/FineTrainingScript.py)

### **Lora at QLora**

![lora](../../../../translated_images/tl/qlora.e6446c988ee04ca0.png)

Ang LoRA (Low-Rank Adaptation) at QLoRA (Quantized Low-Rank Adaptation) ay mga teknik na ginagamit para i-fine-tune ang malalaking language model (LLMs) gamit ang Parameter Efficient Fine Tuning (PEFT). Ang PEFT ay mga teknik na dinisenyo para mas epektibong matrain ang mga modelo kumpara sa tradisyunal na paraan.

Ang LoRA ay isang standalone na fine-tuning technique na nagpapababa ng memory footprint sa pamamagitan ng paglalapat ng low-rank approximation sa weight update matrix. Nagbibigay ito ng mabilis na training at nananatiling malapit ang performance sa tradisyunal na fine-tuning.

Ang QLoRA ay pinalawak na bersyon ng LoRA na gumagamit ng quantization techniques para lalo pang mabawasan ang paggamit ng memorya. Kinukuha ng QLoRA ang precision ng weight parameters sa pre-trained LLM sa 4-bit precision, na mas memory efficient kaysa LoRA. Ngunit ang training ng QLoRA ay mga 30% na mas mabagal kaysa LoRA dahil sa dagdag na hakbang ng quantization at dequantization.

Ginagamit ng QLoRA ang LoRA bilang accessory para itama ang mga error na dulot ng quantization. Pinapahintulutan ng QLoRA ang fine-tuning ng malalaking modelo na may bilyon-bilyong parameters gamit ang mga GPU na maliit at madaling ma-access. Halimbawa, kayang i-fine-tune ng QLoRA ang 70B parameter model na nangangailangan ng 36 GPUs gamit lamang ang 2

**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.