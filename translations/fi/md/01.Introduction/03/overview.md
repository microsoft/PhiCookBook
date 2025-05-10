<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1ff728038c4f554b660a36b76cbdd6e",
  "translation_date": "2025-05-09T12:27:24+00:00",
  "source_file": "md/01.Introduction/03/overview.md",
  "language_code": "fi"
}
-->
Phi-3-miniin yhteydessä inferenssi tarkoittaa prosessia, jossa mallia käytetään ennusteiden tekemiseen tai tulosten tuottamiseen syötetyn datan perusteella. Kerron sinulle lisää Phi-3-ministä ja sen inferenssikyvyistä.

Phi-3-mini on osa Microsoftin julkaisemaa Phi-3-mallisarjaa. Nämä mallit on suunniteltu uudelleenmäärittelemään, mitä pienillä kielimalleilla (SLM) on mahdollista saavuttaa.

Tässä muutamia keskeisiä kohtia Phi-3-ministä ja sen inferenssikyvyistä:

## **Phi-3-mini Yleiskatsaus:**
- Phi-3-minin parametrikoko on 3,8 miljardia.
- Se voi toimia paitsi perinteisillä tietokoneilla myös reunalaitteissa, kuten mobiililaitteissa ja IoT-laitteissa.
- Phi-3-minin julkaisu mahdollistaa yksityishenkilöiden ja yritysten ottaa SLM-malleja käyttöön erilaisilla laitteistoilla, erityisesti resurssirajoitetuissa ympäristöissä.
- Se tukee erilaisia malliformaatteja, mukaan lukien perinteinen PyTorch-muoto, gguf-muodon kvantisoitu versio sekä ONNX-pohjainen kvantisoitu versio.

## **Phi-3-minin Käyttö:**
Phi-3-miniin pääsee käsiksi käyttämällä [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) -kirjastoa Copilot-sovelluksessa. Semantic Kernel on yleisesti yhteensopiva Azure OpenAI Service -palvelun, Hugging Facen avoimen lähdekoodin mallien ja paikallisten mallien kanssa.
Voit myös käyttää [Ollamaa](https://ollama.com) tai [LlamaEdgeä](https://llamaedge.com) kvantisoitujen mallien kutsumiseen. Ollama mahdollistaa yksittäisten käyttäjien kutsua erilaisia kvantisoituja malleja, kun taas LlamaEdge tarjoaa GGUF-mallien monialustaisen käytettävyyden.

## **Kvantisoidut Mallit:**
Monet käyttäjät suosivat kvantisoituja malleja paikalliseen inferenssiin. Esimerkiksi voit suoraan ajaa Ollamalla Phi-3-mallia tai määrittää sen offline-tilassa Modelfile-tiedoston avulla. Modelfile määrittelee GGUF-tiedoston polun ja kehotemuodon.

## **Generatiivisen AI:n Mahdollisuudet:**
SLM-mallien, kuten Phi-3-minin, yhdistäminen avaa uusia mahdollisuuksia generatiivisessa tekoälyssä. Inferenssi on vasta ensimmäinen askel; näitä malleja voidaan käyttää monenlaisissa tehtävissä, joissa resurssit, viiveet ja kustannukset ovat rajoitettuja.

## **Generatiivisen AI:n Avaaminen Phi-3-minillä: Opas Inferenssiin ja Käyttöönottoon**  
Opi käyttämään Semantic Kernelia, Ollamaa/LlamaEdgeä ja ONNX Runtimea Phi-3-mini-mallien käyttämiseen ja inferenssiin, ja tutustu generatiivisen AI:n mahdollisuuksiin erilaisissa sovellustilanteissa.

**Ominaisuudet**  
Inferenssi phi3-mini -mallilla seuraavissa ympäristöissä:

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)

Yhteenvetona Phi-3-mini antaa kehittäjille mahdollisuuden tutkia erilaisia malliformaatteja ja hyödyntää generatiivista tekoälyä monissa sovellustilanteissa.

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattikäännöksissä voi esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulee pitää virallisena lähteenä. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai virhetulkinnoista.