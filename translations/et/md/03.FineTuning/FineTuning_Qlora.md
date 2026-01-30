**Phi-3 peenhäälestamine QLoRA-ga**

Microsofti keelemudeli Phi-3 Mini peenhäälestamine, kasutades [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora).

QLoRA aitab parandada vestluste mõistmist ja vastuste genereerimist.

Mudelite laadimiseks 4-bitises formaadis, kasutades transformers ja bitsandbytes, tuleb paigaldada accelerate ja transformers lähtekoodist ning veenduda, et bitsandbytes'i raamatukogu viimane versioon on olemas.

**Näited**
- [Lisateave selle näidisnotebooki abil](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Näide Pythonis peenhäälestamise skriptist](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Näide Hugging Face Hubi peenhäälestamisest LORA-ga](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Näide Hugging Face Hubi peenhäälestamisest QLORA-ga](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.