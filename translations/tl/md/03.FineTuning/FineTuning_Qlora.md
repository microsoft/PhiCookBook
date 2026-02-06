**Fine-tuning ng Phi-3 gamit ang QLoRA**

Fine-tuning ng Microsoft Phi-3 Mini language model gamit ang [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora).

Makakatulong ang QLoRA para mapabuti ang pag-unawa sa pag-uusap at paggawa ng mga tugon.

Para ma-load ang mga modelo sa 4bits gamit ang transformers at bitsandbytes, kailangan mong i-install ang accelerate at transformers mula sa source at siguraduhing meron kang pinakabagong bersyon ng bitsandbytes library.

**Mga Halimbawa**
- [Matuto Pa gamit ang sample notebook na ito](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Halimbawa ng Python FineTuning Sample](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Halimbawa ng Hugging Face Hub Fine Tuning gamit ang LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Halimbawa ng Hugging Face Hub Fine Tuning gamit ang QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.