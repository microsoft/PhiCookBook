<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e4e010400c2918557b36bb932a14004c",
  "translation_date": "2025-05-09T22:16:09+00:00",
  "source_file": "md/03.FineTuning/FineTuning_vs_RAG.md",
  "language_code": "fi"
}
-->
## Finetuning vs RAG

## Retrieval Augmented Generation

RAG yhdistää tiedonhakemisen ja tekstin generoinnin. Yrityksen rakenteellinen ja rakenteeton data tallennetaan vektoritietokantaan. Kun haetaan relevanttia sisältöä, löydetään asiaankuuluva tiivistelmä ja sisältö muodostamaan kontekstin, ja LLM/SLM:n tekstin täydentämiskyky yhdistetään sisällön luomiseksi.

## RAG-prosessi
![FinetuningvsRAG](../../../../translated_images/rag.36e7cb856f120334d577fde60c6a5d7c5eecae255dac387669303d30b4b3efa4.fi.png)

## Fine-tuning
Fine-tuning perustuu tietyn mallin parantamiseen. Sen ei tarvitse alkaa mallialgoritmista, mutta dataa täytyy kerätä jatkuvasti. Jos haluat tarkempaa terminologiaa ja kielen ilmaisua teollisuussovelluksissa, fine-tuning on parempi valinta. Mutta jos datasi muuttuu usein, fine-tuning voi käydä monimutkaiseksi.

## Miten valita
Jos vastauksemme vaatii ulkoisen datan käyttöä, RAG on paras valinta.

Jos tarvitset vakaata ja tarkkaa teollisuusosaamista, fine-tuning on hyvä vaihtoehto. RAG painottaa relevantin sisällön hakemista, mutta ei välttämättä aina tavoita erikoistuneita vivahteita.

Fine-tuning vaatii laadukkaan aineiston, ja jos data on vain pieneltä alueelta, sillä ei ole suurta vaikutusta. RAG on joustavampi.
Fine-tuning on musta laatikko, eräänlainen metafysiikka, ja sen sisäistä toimintaa on vaikea ymmärtää. Mutta RAG helpottaa datan lähteen löytämistä, jolloin harhaluuloja tai sisältövirheitä voidaan tehokkaasti korjata ja tarjota parempi läpinäkyvyys.

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Pyrimme tarkkuuteen, mutta huomioithan, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulee pitää virallisena lähteenä. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.