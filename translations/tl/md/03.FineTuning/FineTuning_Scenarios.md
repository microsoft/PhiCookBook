## Fine Tuning Scenarios

![FineTuning with MS Services](../../../../translated_images/tl/FinetuningwithMS.3d0cec8ae693e094.webp)

Ang seksyong ito ay nagbibigay ng pangkalahatang-ideya ng mga senaryo ng fine-tuning sa Microsoft Foundry at Azure na mga kapaligiran, kabilang ang mga modelo ng deployment, mga layer ng imprastraktura, at mga karaniwang ginagamit na teknik sa optimization.

**Platform**  
Kasama dito ang mga managed services tulad ng Microsoft Foundry (dating Microsoft Foundry) at Azure Machine Learning, na nagbibigay ng pamamahala ng modelo, orchestration, pagsubaybay sa eksperimento, at mga workflow ng deployment.

**Infrastructure**  
Ang fine-tuning ay nangangailangan ng scalable na compute resources. Sa mga Azure na kapaligiran, karaniwan itong kinabibilangan ng GPU-based na mga virtual machine at mga CPU resources para sa magagaan na mga workload, kasama ang scalable na storage para sa mga dataset at checkpoints.

**Tools & Framework**  
Ang mga workflow ng fine-tuning ay karaniwang nakasalalay sa mga framework at optimization libraries tulad ng Hugging Face Transformers, DeepSpeed, at PEFT (Parameter-Efficient Fine-Tuning).

Ang proseso ng fine-tuning gamit ang mga teknolohiyang Microsoft ay sumasaklaw sa mga platform services, compute infrastructure, at mga training framework. Sa pamamagitan ng pag-unawa kung paano nagtutulungan ang mga bahaging ito, maaaring mahusay na i-adapt ng mga developer ang mga foundation model sa mga tiyak na gawain at senaryo ng produksyon.

## Model as Service

I-fine-tune ang modelo gamit ang hosted fine-tuning, nang hindi kailangan maglikha at mag-manage ng compute.

![MaaS Fine Tuning](../../../../translated_images/tl/MaaSfinetune.3eee4630607aff0d.webp)

Ngayon ay available na ang serverless fine-tuning para sa Phi-3, Phi-3.5, at Phi-4 na mga pamilya ng modelo, na nagpapahintulot sa mga developer na mabilis at madaling i-customize ang mga modelo para sa mga senaryo sa cloud at edge nang hindi na kailangang mag-ayos ng compute.

## Model as a Platform 

Pinamamahalaan ng mga user ang kanilang sariling compute upang ma-Fine-tune ang kanilang mga modelo.

![Maap Fine Tuning](../../../../translated_images/tl/MaaPFinetune.fd3829c1122f5d1c.webp)

[Fine Tuning Sample](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/system/finetune/chat-completion/chat-completion.ipynb)

## Fine-Tuning Techniques Comparison

|Scenario|LoRA|QLoRA|PEFT|DeepSpeed|ZeRO|DoRA|
|---|---|---|---|---|---|---|
|Pagsasaayos ng pre-trained na LLMs para sa mga tiyak na gawain o domain|Oo|Oo|Oo|Oo|Oo|Oo|
|Fine-tuning para sa mga NLP na gawain tulad ng text classification, named entity recognition, at machine translation|Oo|Oo|Oo|Oo|Oo|Oo|
|Fine-tuning para sa mga QA na gawain|Oo|Oo|Oo|Oo|Oo|Oo|
|Fine-tuning para sa paggawa ng mga tugon na tila tao sa mga chatbot|Oo|Oo|Oo|Oo|Oo|Oo|
|Fine-tuning para sa paglikha ng musika, sining, o iba pang anyo ng pagkamalikhain|Oo|Oo|Oo|Oo|Oo|Oo|
|Pagbawas ng mga gastusin sa kompyutasyon at pinansyal|Oo|Oo|Oo|Oo|Oo|Oo|
|Pagbawas ng paggamit ng memorya|Oo|Oo|Oo|Oo|Oo|Oo|
|Paggamit ng mas kaunting mga parameter para sa mahusay na finetuning|Oo|Oo|Oo|Hindi|Hindi|Oo|
|Memory-efficient na anyo ng data parallelism na nagbibigay ng access sa pinagsamang GPU memory ng lahat ng GPU device na available|Hindi|Hindi|Hindi|Oo|Oo|Hindi|

> [!NOTE]
> Ang LoRA, QLoRA, PEFT, at DoRA ay mga parameter-efficient na mga pamamaraan ng fine-tuning, samantalang ang DeepSpeed at ZeRO ay nakatuon sa distributed training at memory optimization.

## Fine Tuning Performance Examples

![Finetuning Performance](../../../../translated_images/tl/Finetuningexamples.a9a41214f8f5afc1.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagaman aming pinagsusumikapan ang pagiging tumpak, pakatandaan na ang mga awtomatikong salin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na opisyal na sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na salin na isinasagawa ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng salin na ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->