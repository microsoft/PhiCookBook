<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e0a07fd2a30fe2af30b1373df207a5bf",
  "translation_date": "2025-07-17T08:11:27+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Phi-3-visionWandB.md",
  "language_code": "fi"
}
-->
# Phi-3-Vision-128K-Instruct Projektin Yleiskatsaus

## Malli

Phi-3-Vision-128K-Instruct, kevyt ja huippuluokan multimodaalinen malli, on tämän projektin ytimessä. Se kuuluu Phi-3-malliperheeseen ja tukee jopa 128 000 tokenin kontekstipituutta. Malli on koulutettu monipuolisella aineistolla, joka sisältää synteettistä dataa sekä huolellisesti suodatettuja julkisesti saatavilla olevia verkkosivuja, painottaen korkealaatuista ja päättelyä vaativaa sisältöä. Koulutusprosessiin kuului valvottu hienosäätö ja suora preferenssien optimointi, jotta ohjeiden noudattaminen olisi tarkkaa, sekä vahvat turvallisuustoimenpiteet.

## Esimerkkidatan luominen on tärkeää monesta syystä:

1. **Testaus**: Esimerkkidata mahdollistaa sovelluksen testaamisen erilaisissa tilanteissa ilman, että oikea data kärsii. Tämä on erityisen tärkeää kehitys- ja testausvaiheissa.

2. **Suorituskyvyn optimointi**: Esimerkkidatan avulla, joka jäljittelee oikean datan mittakaavaa ja monimutkaisuutta, voit tunnistaa suorituskykyyn vaikuttavat pullonkaulat ja optimoida sovellustasi niiden mukaan.

3. **Prototyyppien tekeminen**: Esimerkkidataa voi käyttää prototyyppien ja mallien luomiseen, mikä auttaa ymmärtämään käyttäjien tarpeita ja saamaan palautetta.

4. **Datan analysointi**: Data-analytiikassa esimerkkidataa käytetään usein tutkimusaineistona, mallien koulutukseen ja algoritmien testaamiseen.

5. **Turvallisuus**: Kehitys- ja testausympäristöissä esimerkkidatan käyttö auttaa estämään vahingossa tapahtuvat oikean, arkaluontoisen datan vuodot.

6. **Oppiminen**: Uutta teknologiaa tai työkalua opiskellessa esimerkkidatan kanssa työskentely tarjoaa käytännön tavan soveltaa opittua.

Muista, että esimerkkidatan laatu vaikuttaa merkittävästi näihin toimintoihin. Sen tulisi olla mahdollisimman lähellä oikeaa dataa rakenteeltaan ja vaihtelultaan.

### Esimerkkidatan luominen
[Generate DataSet Script](./CreatingSampleData.md)

## Aineisto

Hyvä esimerkkiaineisto on esimerkiksi [DBQ/Burberry.Product.prices.United.States dataset](https://huggingface.co/datasets/DBQ/Burberry.Product.prices.United.States) (saatavilla Huggingfacessa).  
Burberry-tuotteiden esimerkkiaineisto sisältää tuotetiedot, kuten kategorian, hinnan ja nimen, yhteensä 3 040 riviä, joista kukin edustaa ainutlaatuista tuotetta. Tämä aineisto antaa meille mahdollisuuden testata mallin kykyä ymmärtää ja tulkita visuaalista dataa, tuottaen kuvailevaa tekstiä, joka vangitsee yksityiskohtaiset visuaaliset piirteet ja brändikohtaiset ominaisuudet.

**Note:** Voit käyttää mitä tahansa aineistoa, joka sisältää kuvia.

## Monimutkainen päättely

Mallin tulee pystyä päättelyyn hinnoista ja nimistä pelkän kuvan perusteella. Tämä edellyttää, että malli ei ainoastaan tunnista visuaalisia piirteitä, vaan myös ymmärtää niiden merkityksen tuotteen arvon ja brändäyksen kannalta. Tuottamalla tarkkoja tekstikuvauksia kuvista projekti korostaa visuaalisen datan integroinnin potentiaalia mallien suorituskyvyn ja monipuolisuuden parantamisessa käytännön sovelluksissa.

## Phi-3 Vision Arkkitehtuuri

Mallin arkkitehtuuri on multimodaalinen versio Phi-3:sta. Se käsittelee sekä teksti- että kuvadataa, yhdistäen nämä syötteet yhtenäiseksi sekvenssiksi kattavaa ymmärrystä ja generointitehtäviä varten. Malli käyttää erillisiä upotustasoja tekstille ja kuville. Tekstisymbolit muunnetaan tiheiksi vektoreiksi, kun taas kuvat käsitellään CLIP-vision-mallin kautta piirreupotusten erottamiseksi. Nämä kuva-upotukset projisoidaan vastaamaan tekstin upotusten mittoja, jotta ne voidaan saumattomasti yhdistää.

## Teksti- ja kuva-upotusten yhdistäminen

Tekstisekvenssissä erikoissymbolit osoittavat, mihin kuva-upotukset tulee sijoittaa. Käsittelyn aikana nämä erikoissymbolit korvataan vastaavilla kuva-upotuksilla, jolloin malli voi käsitellä tekstiä ja kuvia yhtenä sekvenssinä. Datasetimme kehotteen muotoilu käyttää erikoissymbolia <|image|> seuraavasti:

```python
text = f"<|user|>\n<|image_1|>What is shown in this image?<|end|><|assistant|>\nProduct: {row['title']}, Category: {row['category3_code']}, Full Price: {row['full_price']}<|end|>"
```

## Esimerkkikoodi
- [Phi-3-Vision Training Script](../../../../code/03.Finetuning/Phi-3-vision-Trainingscript.py)
- [Weights and Bias Example walkthrough](https://wandb.ai/byyoung3/mlnews3/reports/How-to-fine-tune-Phi-3-vision-on-a-custom-dataset--Vmlldzo4MTEzMTg3)

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.