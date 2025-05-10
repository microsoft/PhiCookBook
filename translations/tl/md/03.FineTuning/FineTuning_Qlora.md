<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "54b6b824568d4decb574b9e117c4f5f7",
  "translation_date": "2025-05-09T21:53:12+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Qlora.md",
  "language_code": "tl"
}
-->
**Fine-tuning Phi-3 gamit ang QLoRA**

Pag-fine-tune ng Phi-3 Mini language model ng Microsoft gamit ang [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora).

Makakatulong ang QLoRA para mapabuti ang pag-unawa sa usapan at paggawa ng mga sagot.

Para makapag-load ng mga modelo sa 4bits gamit ang transformers at bitsandbytes, kailangan mong i-install ang accelerate at transformers mula sa source at siguraduhing nasa pinakabagong bersyon ang bitsandbytes library.

**Mga Halimbawa**
- [Matuto Pa gamit ang sample notebook na ito](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Halimbawa ng Python FineTuning Sample](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Halimbawa ng Hugging Face Hub Fine Tuning gamit ang LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Halimbawa ng Hugging Face Hub Fine Tuning gamit ang QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pinagmulan ng katotohanan. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.