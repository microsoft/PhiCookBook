<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bcf5dd7031db0031abdb9dd0c05ba118",
  "translation_date": "2025-07-16T20:57:57+00:00",
  "source_file": "md/01.Introduction/03/Local_Server_Inference.md",
  "language_code": "fi"
}
-->
# **Phi-3:n päättely paikallisella palvelimella**

Voimme ottaa Phi-3:n käyttöön paikallisella palvelimella. Käyttäjät voivat valita [Ollama](https://ollama.com) tai [LM Studio](https://llamaedge.com) -ratkaisuista, tai he voivat kirjoittaa oman koodinsa. Phi-3:n paikallisiin palveluihin voi yhdistää [Semantic Kernelin](https://github.com/microsoft/semantic-kernel?WT.mc_id=aiml-138114-kinfeylo) tai [Langchainin](https://www.langchain.com/) kautta Copilot-sovellusten rakentamiseksi.

## **Semantic Kernelin käyttö Phi-3-miniin pääsyyn**

Copilot-sovelluksessa luomme sovelluksia Semantic Kernelin / LangChainin avulla. Tämän tyyppinen sovelluskehys on yleisesti yhteensopiva Azure OpenAI Service- / OpenAI-mallien kanssa, ja se tukee myös avoimen lähdekoodin malleja Hugging Facessa sekä paikallisia malleja. Mitä meidän tulisi tehdä, jos haluamme käyttää Semantic Kernelia Phi-3-miniin pääsyyn? Käytetään esimerkkinä .NET:iä, jonka voi yhdistää Semantic Kernelin Hugging Face Connectoriin. Oletuksena se vastaa Hugging Facen mallin tunnistetta (ensimmäisellä käyttökerralla malli ladataan Hugging Facesta, mikä vie aikaa). Voit myös yhdistää itse rakennettuun paikalliseen palveluun. Näistä kahdesta suosittelemme jälkimmäistä, koska se tarjoaa enemmän itsenäisyyttä, erityisesti yrityssovelluksissa.

![sk](../../../../../translated_images/sk.d03785c25edc6d44.fi.png)

Kuvasta nähdään, että paikallisiin palveluihin pääsy Semantic Kernelin kautta yhdistää helposti itse rakennettuun Phi-3-mini-mallipalvelimeen. Tässä on ajon tulos:

![skrun](../../../../../translated_images/skrun.5aafc1e7197dca20.fi.png)

***Esimerkkikoodi*** https://github.com/kinfey/Phi3MiniSamples/tree/main/semantickernel

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.