<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e4e010400c2918557b36bb932a14004c",
  "translation_date": "2025-07-17T09:29:59+00:00",
  "source_file": "md/03.FineTuning/FineTuning_vs_RAG.md",
  "language_code": "fi"
}
-->
## Finetuning vs RAG

## Retrieval Augmented Generation

RAG on tiedonhaku + tekstin generointi. Yrityksen rakenteellinen ja rakenteeton data tallennetaan vektoritietokantaan. Kun haetaan relevanttia sisältöä, löydetään siihen liittyvä tiivistelmä ja sisältö muodostamaan kontekstin, ja yhdistetään LLM/SLM:n tekstin täydentämiskyky sisällön luomiseksi.

## RAG-prosessi
![FinetuningvsRAG](../../../../translated_images/rag.2014adc59e6f6007.fi.png)

## Fine-tuning
Fine-tuning perustuu tietyn mallin parantamiseen. Sen ei tarvitse alkaa mallin algoritmista, mutta dataa täytyy kerätä jatkuvasti. Jos haluat tarkempaa terminologiaa ja kielen ilmaisua teollisuussovelluksissa, fine-tuning on parempi valinta. Mutta jos datasi muuttuu usein, fine-tuning voi käydä monimutkaiseksi.

## Miten valita
Jos vastauksemme vaatii ulkopuolisen datan käyttöä, RAG on paras valinta.

Jos tarvitset vakaata ja tarkkaa teollisuusalan tietoa, fine-tuning on hyvä vaihtoehto. RAG painottaa relevantin sisällön hakemista, mutta ei välttämättä aina tavoita erikoistuneita vivahteita.

Fine-tuning vaatii laadukkaan datan, ja jos data on vain pienen alueen kattavaa, sillä ei ole suurta vaikutusta. RAG on joustavampi.  
Fine-tuning on musta laatikko, metafysiikkaa, ja sen sisäistä mekanismia on vaikea ymmärtää. Mutta RAG helpottaa datan lähteen löytämistä, jolloin harhojen tai sisältövirheiden korjaaminen on tehokkaampaa ja läpinäkyvyys parempi.

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.