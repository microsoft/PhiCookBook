## Fine Tuning -skenaariot

![FineTuning with MS Services](../../../../translated_images/fi/FinetuningwithMS.3d0cec8ae693e094.webp)

Tässä osiossa annetaan yleiskatsaus hienosäätöskenaarioihin Microsoft Foundry- ja Azure-ympäristöissä, mukaan lukien käyttöönotto-mallit, infrastruktuurikerrokset ja yleisesti käytetyt optimointitekniikat.

**Alusta**  
Tähän sisältyvät hallinnoidut palvelut, kuten Microsoft Foundry (entinen Azure AI Foundry) ja Azure Machine Learning, jotka tarjoavat mallien hallinnan, orkestroinnin, kokeilujen seurannan ja käyttöönottojen työnkulut.

**Infrastruktuuri**  
Hienosäätö vaatii skaalautuvia laskentaresursseja. Azure-ympäristöissä tämä sisältää tyypillisesti GPU-pohjaiset virtuaalikoneet ja CPU-resurssit kevyille työkuormille sekä skaalautuvan tallennustilan datasettejä ja checkpointteja varten.

**Työkalut & Kehykset**  
Hienosäätötyönkulut perustuvat usein kehyksiin ja optimointikirjastoihin, kuten Hugging Face Transformers, DeepSpeed ja PEFT (Parameter-Efficient Fine-Tuning).

Hienosäätöprosessi Microsoftin teknologioilla kattaa alustan palvelut, laskentainfrastruktuurin ja koulutuskehykset. Ymmärtämällä näiden komponenttien yhteistyön kehittäjät voivat tehokkaasti sovittaa perustamalleja tiettyihin tehtäviin ja tuotantoskenaarioihin.

## Malli palveluna

Hienosäädä mallia käyttämällä isännöityä hienosäätöä ilman tarvetta luoda ja hallita laskentaa.

![MaaS Fine Tuning](../../../../translated_images/fi/MaaSfinetune.3eee4630607aff0d.webp)

Serveriton hienosäätö on nyt saatavilla Phi-3, Phi-3.5 ja Phi-4 malliperheille, mikä mahdollistaa kehittäjien nopean ja helpon mallien mukauttamisen pilvi- ja reunaskenaarioihin ilman laskennan järjestämistä.

## Malli alustana

Käyttäjät hallitsevat omaa laskentaa hienosäätääkseen mallejaan.

![Maap Fine Tuning](../../../../translated_images/fi/MaaPFinetune.fd3829c1122f5d1c.webp)

[Hienosäätöesimerkki](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/system/finetune/chat-completion/chat-completion.ipynb)

## Hienosäätötekniikoiden vertailu

|Skenaario|LoRA|QLoRA|PEFT|DeepSpeed|ZeRO|DoRA|
|---|---|---|---|---|---|---|
|Ennaltakoulutettujen LLM:ien sovittaminen tiettyihin tehtäviin tai toimialoihin|Kyllä|Kyllä|Kyllä|Kyllä|Kyllä|Kyllä|
|Hienosäätö NLP-tehtäviin, kuten tekstiluokittelu, nimettyjen entiteettien tunnistus ja konekäännös|Kyllä|Kyllä|Kyllä|Kyllä|Kyllä|Kyllä|
|Hienosäätö QA-tehtäviin|Kyllä|Kyllä|Kyllä|Kyllä|Kyllä|Kyllä|
|Hienosäätö ihmismäisten vastausten tuottamiseen chatbotteihin|Kyllä|Kyllä|Kyllä|Kyllä|Kyllä|Kyllä|
|Hienosäätö musiikin, taiteen tai muiden luovien muotojen tuotantoon|Kyllä|Kyllä|Kyllä|Kyllä|Kyllä|Kyllä|
|Laskenta- ja taloudellisten kustannusten vähentäminen|Kyllä|Kyllä|Kyllä|Kyllä|Kyllä|Kyllä|
|Muistin käytön vähentäminen|Kyllä|Kyllä|Kyllä|Kyllä|Kyllä|Kyllä|
|Vähemmillä parametreilla tehokas hienosäätö|Kyllä|Kyllä|Kyllä|Ei|Ei|Kyllä|
|Muistitehokas dataparallelismin muoto, joka tarjoaa pääsyn kaikkien käytettävissä olevien GPU-laitteiden yhteenlaskettuun muistimäärään|Ei|Ei|Ei|Kyllä|Kyllä|Ei|

> [!NOTE]
> LoRA, QLoRA, PEFT ja DoRA ovat parametri-tehokkaita hienosäätömenetelmiä, kun taas DeepSpeed ja ZeRO keskittyvät hajautettuun koulutukseen ja muistin optimointiin.

## Hienosäädön suorituskyky-esimerkkejä

![Finetuning Performance](../../../../translated_images/fi/Finetuningexamples.a9a41214f8f5afc1.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty tekoälykäännöspalvelulla [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, automaattisissa käännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä tulee pitää ensisijaisena ja luotettavana lähteenä. Tärkeän tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme vastaa mahdollisista väärinymmärryksistä tai virhetulkintojen seurauksista, jotka johtuvat tämän käännöksen käytöstä.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->