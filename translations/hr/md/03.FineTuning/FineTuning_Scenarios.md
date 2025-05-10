<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cb5648935f63edc17e95ce38f23adc32",
  "translation_date": "2025-05-09T21:58:17+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Scenarios.md",
  "language_code": "hr"
}
-->
## Scenariji fino podešavanja

![FineTuning with MS Services](../../../../translated_images/FinetuningwithMS.25759a0154a97ad90e43a6cace37d6bea87f0ac0236ada3ad5d4a1fbacc3bdf7.hr.png)

**Platforma** Obuhvaća razne tehnologije kao što su Azure AI Foundry, Azure Machine Learning, AI alati, Kaito i ONNX Runtime.

**Infrastruktura** Obuhvaća CPU i FPGA, koji su ključni za proces fino podešavanja. Dopustite da vam pokažem ikone za svaku od ovih tehnologija.

**Alati i okviri** Obuhvaćaju ONNX Runtime i ONNX Runtime. Dopustite da vam pokažem ikone za svaku od ovih tehnologija.  
[Umetnite ikone za ONNX Runtime i ONNX Runtime]

Proces fino podešavanja s Microsoft tehnologijama uključuje različite komponente i alate. Razumijevanjem i korištenjem ovih tehnologija možemo učinkovito fino podesiti naše aplikacije i stvoriti bolje rješenja.

## Model kao usluga

Fino podesite model koristeći hostano fino podešavanje, bez potrebe za kreiranjem i upravljanjem računalnim resursima.

![MaaS Fine Tuning](../../../../translated_images/MaaSfinetune.6184d80a336ea9d7bb67a581e9e5d0b021cafdffff7ba257c2012e2123e0d77e.hr.png)

Serverless fino podešavanje dostupno je za modele Phi-3-mini i Phi-3-medium, što omogućuje programerima brzo i jednostavno prilagođavanje modela za cloud i edge scenarije bez potrebe za organizacijom računalnih resursa. Također smo najavili da je Phi-3-small sada dostupan kroz našu ponudu Models-as-a-Service, pa programeri mogu brzo i jednostavno započeti s razvojem AI bez upravljanja osnovnom infrastrukturom.

## Model kao platforma

Korisnici upravljaju vlastitim računalnim resursima kako bi fino podesili svoje modele.

![Maap Fine Tuning](../../../../translated_images/MaaPFinetune.cf8b08ef05bf57f362da90834be87562502f4370de4a7325a9fb03b8c008e5e7.hr.png)

[Primjer fino podešavanja](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/system/finetune/chat-completion/chat-completion.ipynb)

## Scenariji fino podešavanja

| | | | | | | |
|-|-|-|-|-|-|-|
|Scenarij|LoRA|QLoRA|PEFT|DeepSpeed|ZeRO|DORA|
|Prilagodba unaprijed treniranih LLM-ova za specifične zadatke ili domene|Da|Da|Da|Da|Da|Da|
|Fino podešavanje za NLP zadatke poput klasifikacije teksta, prepoznavanja imenovanih entiteta i strojno prevođenje|Da|Da|Da|Da|Da|Da|
|Fino podešavanje za QA zadatke|Da|Da|Da|Da|Da|Da|
|Fino podešavanje za generiranje odgovora nalik ljudskim u chatbotovima|Da|Da|Da|Da|Da|Da|
|Fino podešavanje za generiranje glazbe, umjetnosti ili drugih oblika kreativnosti|Da|Da|Da|Da|Da|Da|
|Smanjenje računalnih i financijskih troškova|Da|Da|Ne|Da|Da|Ne|
|Smanjenje potrošnje memorije|Ne|Da|Ne|Da|Da|Da|
|Korištenje manjeg broja parametara za učinkovito fino podešavanje|Ne|Da|Da|Ne|Ne|Da|
|Memorijski učinkoviti oblik paralelizma podataka koji omogućuje pristup ukupnoj GPU memoriji svih dostupnih GPU uređaja|Ne|Ne|Ne|Da|Da|Da|

## Primjeri performansi fino podešavanja

![Finetuning Performance](../../../../translated_images/Finetuningexamples.9dbf84557eef43e011eb7cadf51f51686f9245f7953e2712a27095ab7d18a6d1.hr.png)

**Odricanje od odgovornosti**:  
Ovaj dokument preveden je pomoću AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati službenim i autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazuma ili pogrešna tumačenja proizašla iz korištenja ovog prijevoda.