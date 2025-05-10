<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e0a07fd2a30fe2af30b1373df207a5bf",
  "translation_date": "2025-05-09T21:48:31+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Phi-3-visionWandB.md",
  "language_code": "fi"
}
-->
# Phi-3-Vision-128K-Instruct Projektin yleiskatsaus

## Malli

Phi-3-Vision-128K-Instruct on kevyt, huippuluokan multimodaalinen malli, joka on tämän projektin ytimessä. Se kuuluu Phi-3-malliperheeseen ja tukee jopa 128 000 tokenin kontekstipituutta. Malli on koulutettu monipuolisella aineistolla, joka sisältää synteettistä dataa sekä huolellisesti suodatettuja julkisesti saatavilla olevia verkkosivuja, painottaen korkealaatuista ja päättelyä vaativaa sisältöä. Koulutusprosessiin sisältyi valvottu hienosäätö ja suora preferenssien optimointi, jotta ohjeiden noudattaminen olisi tarkkaa, sekä vahvat turvallisuustoimenpiteet.

## Näytedata on tärkeää monesta syystä:

1. **Testaus**: Näytedata mahdollistaa sovelluksen testaamisen erilaisissa tilanteissa ilman, että oikeaa dataa käytetään. Tämä on erityisen tärkeää kehitys- ja testausvaiheissa.

2. **Suorituskyvyn optimointi**: Näytedata, joka jäljittelee oikean datan mittakaavaa ja monimutkaisuutta, auttaa tunnistamaan suorituskykyongelmia ja optimoimaan sovellusta niiden mukaan.

3. **Prototyyppien tekeminen**: Näytedata auttaa luomaan prototyyppejä ja mallinnuksia, jotka tukevat käyttäjävaatimusten ymmärtämistä ja palautteen saamista.

4. **Data-analyysi**: Data-analytiikassa näytedata toimii usein tutkimusaineistona, mallien koulutuksessa ja algoritmien testaamisessa.

5. **Turvallisuus**: Näytedatan käyttö kehitys- ja testausympäristöissä auttaa estämään vahingossa tapahtuvat arkaluontoisen datan vuodot.

6. **Oppiminen**: Uutta teknologiaa tai työkalua opiskellessa näytedatan kanssa työskentely tarjoaa käytännön tavan soveltaa opittua.

Muista, että näytedatan laatu vaikuttaa merkittävästi näihin toimintoihin. Sen tulisi olla mahdollisimman lähellä oikeaa dataa rakenteeltaan ja vaihtelultaan.

### Näytedatan luonti
[Generate DataSet Script](./CreatingSampleData.md)

## Aineisto

Hyvä esimerkki näytedatasta on [DBQ/Burberry.Product.prices.United.States dataset](https://huggingface.co/datasets/DBQ/Burberry.Product.prices.United.States) (saatavilla Huggingfacessa).  
Burberry-tuotteiden näytedatasetti sisältää metatietoja tuotteiden kategoriasta, hinnasta ja nimestä, yhteensä 3 040 riviä, joista kukin kuvaa ainutlaatuista tuotetta. Tämä aineisto mahdollistaa mallin kyvyn testauksen ymmärtää ja tulkita visuaalista dataa sekä tuottaa kuvailevaa tekstiä, joka vangitsee yksityiskohtaiset visuaaliset piirteet ja brändikohtaiset ominaisuudet.

**Note:** Voit käyttää mitä tahansa aineistoa, joka sisältää kuvia.

## Monimutkainen päättely

Mallin tulee pystyä päättelyyn hinnoista ja nimityksistä pelkän kuvan perusteella. Tämä edellyttää, että malli tunnistaa visuaaliset ominaisuudet ja ymmärtää niiden merkityksen tuotteen arvon ja brändäyksen kannalta. Tuottamalla tarkkoja tekstikuvauksia kuvista projekti korostaa visuaalisen datan integroinnin potentiaalia mallien suorituskyvyn ja monipuolisuuden parantamisessa käytännön sovelluksissa.

## Phi-3 Vision -arkkitehtuuri

Mallin arkkitehtuuri on multimodaalinen versio Phi-3:sta. Se käsittelee sekä teksti- että kuvatietoa, yhdistäen nämä syötteet yhtenäiseksi sekvenssiksi kattavaa ymmärrystä ja generointitehtäviä varten. Malli käyttää erillisiä upotustasoja tekstille ja kuville. Tekstitokenit muunnetaan tiheiksi vektoreiksi, kun taas kuvat käsitellään CLIP-vision-mallin kautta piirreupotusten eristämiseksi. Nämä kuva-upotukset projisoidaan sitten tekstin upotusten mittoihin, jotta ne voidaan saumattomasti yhdistää.

## Teksti- ja kuva-upotusten yhdistäminen

Tekstisekvenssissä erikoistokenit ilmaisevat, mihin kuva-upotukset tulee sijoittaa. Prosessoinnin aikana nämä erikoistokenit korvataan vastaavilla kuva-upotuksilla, jolloin malli voi käsitellä tekstiä ja kuvia yhtenä sekvenssinä. Datasetimme promptti on muotoiltu käyttämällä erikoistokenia <|image|> seuraavasti:

```python
text = f"<|user|>\n<|image_1|>What is shown in this image?<|end|><|assistant|>\nProduct: {row['title']}, Category: {row['category3_code']}, Full Price: {row['full_price']}<|end|>"
```

## Esimerkkikoodi
- [Phi-3-Vision Training Script](../../../../code/03.Finetuning/Phi-3-vision-Trainingscript.py)
- [Weights and Bias Example walkthrough](https://wandb.ai/byyoung3/mlnews3/reports/How-to-fine-tune-Phi-3-vision-on-a-custom-dataset--Vmlldzo4MTEzMTg3)

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä johtuvista väärinymmärryksistä tai tulkinnoista.