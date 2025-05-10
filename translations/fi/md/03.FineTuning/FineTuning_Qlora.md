<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "54b6b824568d4decb574b9e117c4f5f7",
  "translation_date": "2025-05-09T21:52:40+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Qlora.md",
  "language_code": "fi"
}
-->
**Fine-tuning Phi-3 QLoRAn avulla**

Microsoftin Phi-3 Mini -kielimallin hienosäätö [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora) -menetelmällä.

QLoRA auttaa parantamaan keskustelun ymmärtämistä ja vastausten tuottamista.

Mallien lataamiseksi 4bitin tarkkuudella transformers- ja bitsandbytes-kirjastoilla, sinun täytyy asentaa accelerate ja transformers lähdekoodista ja varmistaa, että sinulla on uusin versio bitsandbytes-kirjastosta.

**Esimerkit**
- [Lisätietoja tästä esimerkkimuistiosta](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python-hienosäätöesimerkin koodi](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Hugging Face Hubin hienosäätöesimerkki LORAlla](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Hugging Face Hubin hienosäätöesimerkki QLORAlla](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty tekoälypohjaisella käännöspalvelulla [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tästä käännöksestä aiheutuvista väärinymmärryksistä tai virhetulkinnoista.