<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cb5648935f63edc17e95ce38f23adc32",
  "translation_date": "2025-07-17T08:29:15+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Scenarios.md",
  "language_code": "tl"
}
-->
## Mga Senaryo ng Fine Tuning

![FineTuning with MS Services](../../../../translated_images/tl/FinetuningwithMS.3d0cec8ae693e094.png)

**Platform** Kasama dito ang iba't ibang teknolohiya tulad ng Azure AI Foundry, Azure Machine Learning, AI Tools, Kaito, at ONNX Runtime.

**Infrastructure** Kasama dito ang CPU at FPGA, na mahalaga para sa proseso ng fine-tuning. Ipapakita ko sa iyo ang mga icon para sa bawat isa sa mga teknolohiyang ito.

**Tools & Framework** Kasama dito ang ONNX Runtime at ONNX Runtime. Ipapakita ko sa iyo ang mga icon para sa bawat isa sa mga teknolohiyang ito.  
[Insert icons for ONNX Runtime and ONNX Runtime]

Ang proseso ng fine-tuning gamit ang mga teknolohiyang Microsoft ay binubuo ng iba't ibang bahagi at kasangkapan. Sa pamamagitan ng pag-unawa at paggamit ng mga teknolohiyang ito, maaari nating epektibong i-fine-tune ang ating mga aplikasyon at makalikha ng mas mahusay na mga solusyon.

## Model as Service

I-fine-tune ang modelo gamit ang hosted fine-tuning, nang hindi na kailangang gumawa at mag-manage ng compute.

![MaaS Fine Tuning](../../../../translated_images/tl/MaaSfinetune.3eee4630607aff0d.png)

Available ang serverless fine-tuning para sa Phi-3-mini at Phi-3-medium na mga modelo, na nagbibigay-daan sa mga developer na mabilis at madaliang i-customize ang mga modelo para sa cloud at edge na mga senaryo nang hindi na kailangang mag-ayos ng compute. Inanunsyo rin namin na ang Phi-3-small ay ngayon ay available na sa pamamagitan ng aming Models-as-a-Service na alok, kaya't mabilis at madali nang makapagsimula ang mga developer sa AI development nang hindi na kailangang mag-manage ng underlying infrastructure.

## Model as a Platform

Ang mga user ang nagma-manage ng kanilang sariling compute upang i-fine-tune ang kanilang mga modelo.

![Maap Fine Tuning](../../../../translated_images/tl/MaaPFinetune.fd3829c1122f5d1c.png)

[Fine Tuning Sample](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/system/finetune/chat-completion/chat-completion.ipynb)

## Mga Senaryo ng Fine Tuning

| | | | | | | |
|-|-|-|-|-|-|-|
|Senaryo|LoRA|QLoRA|PEFT|DeepSpeed|ZeRO|DORA|
|Pag-aangkop ng pre-trained LLMs sa mga partikular na gawain o domain|Oo|Oo|Oo|Oo|Oo|Oo|
|Fine-tuning para sa mga NLP na gawain tulad ng text classification, named entity recognition, at machine translation|Oo|Oo|Oo|Oo|Oo|Oo|
|Fine-tuning para sa mga QA na gawain|Oo|Oo|Oo|Oo|Oo|Oo|
|Fine-tuning para sa pagbuo ng mga tugon na parang tao sa mga chatbot|Oo|Oo|Oo|Oo|Oo|Oo|
|Fine-tuning para sa paglikha ng musika, sining, o iba pang anyo ng pagkamalikhain|Oo|Oo|Oo|Oo|Oo|Oo|
|Pagbawas ng computational at pinansyal na gastos|Oo|Oo|Hindi|Oo|Oo|Hindi|
|Pagbawas ng paggamit ng memorya|Hindi|Oo|Hindi|Oo|Oo|Oo|
|Paggamit ng mas kaunting parameters para sa mas epektibong fine-tuning|Hindi|Oo|Oo|Hindi|Hindi|Oo|
|Memory-efficient na anyo ng data parallelism na nagbibigay access sa pinagsamang GPU memory ng lahat ng available na GPU devices|Hindi|Hindi|Hindi|Oo|Oo|Oo|

## Mga Halimbawa ng Performance ng Fine Tuning

![Finetuning Performance](../../../../translated_images/tl/Finetuningexamples.a9a41214f8f5afc1.png)

**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa kanyang sariling wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.