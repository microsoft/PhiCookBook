<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1ff728038c4f554b660a36b76cbdd6e",
  "translation_date": "2025-07-16T21:11:08+00:00",
  "source_file": "md/01.Introduction/03/overview.md",
  "language_code": "fi"
}
-->
Phi-3-mini -kontekstissa inferenssi tarkoittaa prosessia, jossa mallia käytetään tekemään ennusteita tai tuottamaan tuloksia syötteen perusteella. Kerron sinulle lisää Phi-3-ministä ja sen inferenssikyvyistä.

Phi-3-mini kuuluu Microsoftin julkaisemaan Phi-3-mallisarjaan. Nämä mallit on suunniteltu uudelleenmäärittelemään, mitä pienillä kielimalleilla (SLM) on mahdollista saavuttaa.

Tässä muutamia keskeisiä seikkoja Phi-3-ministä ja sen inferenssikyvyistä:

## **Phi-3-mini Yleiskatsaus:**
- Phi-3-minin parametrikoko on 3,8 miljardia.
- Se voi toimia paitsi perinteisillä tietokoneilla myös reunalaitteilla, kuten mobiililaitteilla ja IoT-laitteilla.
- Phi-3-minin julkaisu mahdollistaa yksityishenkilöiden ja yritysten ottaa SLM-mallit käyttöön erilaisilla laitteilla, erityisesti resurssirajoitetuissa ympäristöissä.
- Se tukee useita malliformaatteja, mukaan lukien perinteinen PyTorch-muoto, gguf-muodon kvantisoitu versio sekä ONNX-pohjainen kvantisoitu versio.

## **Phi-3-minin Käyttö:**
Phi-3-miniin pääsee käsiksi käyttämällä [Semantic Kernelia](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) Copilot-sovelluksessa. Semantic Kernel on yleisesti yhteensopiva Azure OpenAI -palvelun, Hugging Facen avoimen lähdekoodin mallien sekä paikallisten mallien kanssa.
Voit myös käyttää [Ollamaa](https://ollama.com) tai [LlamaEdgeä](https://llamaedge.com) kvantisoitujen mallien kutsumiseen. Ollama mahdollistaa yksittäisten käyttäjien kutsua erilaisia kvantisoituja malleja, kun taas LlamaEdge tarjoaa GGUF-mallien monialustaisen saatavuuden.

## **Kvantisoidut Mallit:**
Monet käyttäjät suosivat kvantisoitujen mallien käyttöä paikalliseen inferenssiin. Esimerkiksi voit suorittaa Ollamalla Phi-3:n suoraan tai määrittää sen offline-tilassa Modelfile-tiedoston avulla. Modelfile määrittelee GGUF-tiedostopolun ja kehotemuodon.

## **Generatiivisen AI:n Mahdollisuudet:**
SLM-mallien, kuten Phi-3-minin, yhdistäminen avaa uusia mahdollisuuksia generatiiviselle tekoälylle. Inferenssi on vasta ensimmäinen askel; näitä malleja voidaan käyttää monenlaisiin tehtäviin resurssirajoitetuissa, viiveherkissä ja kustannusrajoitteisissa tilanteissa.

## **Generatiivisen AI:n Avaaminen Phi-3-minillä: Opas Inferenssiin ja Käyttöönottoon**  
Opi käyttämään Semantic Kernelia, Ollamaa/LlamaEdgeä ja ONNX Runtimea Phi-3-mini-mallien käyttöön ja inferenssiin sekä tutustu generatiivisen AI:n mahdollisuuksiin erilaisissa sovellusympäristöissä.

**Ominaisuudet**  
Inferenssi phi3-mini -mallilla seuraavissa ympäristöissä:

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)  
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)  
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)  
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)  
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)  

Yhteenvetona Phi-3-mini antaa kehittäjille mahdollisuuden tutkia erilaisia malliformaatteja ja hyödyntää generatiivista tekoälyä monenlaisissa sovellusympäristöissä.

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.