**Phi-3:n hienosäätö QLoRA:lla**

Microsoftin Phi-3 Mini -kielimallin hienosäätö käyttäen [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora).

QLoRA auttaa parantamaan keskustelun ymmärrystä ja vastausten generointia.

Mallien lataamiseksi 4bitin tarkkuudella transformers- ja bitsandbytes-kirjastoilla, sinun täytyy asentaa accelerate ja transformers lähdekoodista sekä varmistaa, että sinulla on uusin versio bitsandbytes-kirjastosta.

**Esimerkit**
- [Lisätietoja tästä esimerkkimuistikirjasta](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python-hienosäätöesimerkin koodi](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Hugging Face Hubin hienosäätöesimerkki LORA:lla](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Hugging Face Hubin hienosäätöesimerkki QLORA:lla](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.