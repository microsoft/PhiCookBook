<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9481b07dda8f9715a5d1ff43fb27568b",
  "translation_date": "2025-05-09T10:47:10+00:00",
  "source_file": "md/01.Introduction/03/Android_Inference.md",
  "language_code": "fi"
}
-->
# **Phi-3-päätelmät Androidilla**

Tutustutaan, miten voit tehdä päätelmiä Phi-3-minillä Android-laitteilla. Phi-3-mini on Microsoftin uusi mallisarja, joka mahdollistaa suurten kielimallien (LLM) käyttöönoton reunalaitteissa ja IoT-laitteissa.

## Semantic Kernel ja päätelmät

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) on sovelluskehys, jonka avulla voit luoda sovelluksia, jotka toimivat Azure OpenAI -palvelun, OpenAI-mallien ja jopa paikallisten mallien kanssa. Jos Semantic Kernel on sinulle uusi, suosittelemme tutustumaan [Semantic Kernel Cookbookiin](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo).

### Phi-3-minin käyttö Semantic Kernelin kautta

Voit yhdistää sen Semantic Kernelin Hugging Face Connectoriin. Katso tämä [esimerkkikoodi](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo).

Oletuksena se vastaa mallin tunnistetta Hugging Facessa. Voit kuitenkin myös yhdistää paikallisesti rakennettuun Phi-3-mini -mallipalvelimeen.

### Kvantisoitujen mallien kutsuminen Ollamalla tai LlamaEdgellä

Monet käyttäjät suosivat kvantisoituja malleja, jotta mallit voi ajaa paikallisesti. [Ollama](https://ollama.com/) ja [LlamaEdge](https://llamaedge.com) mahdollistavat yksittäisten käyttäjien kutsua eri kvantisoituja malleja:

#### Ollama

Voit ajaa suoraan `ollama run Phi-3` tai määrittää sen offline-tilassa luomalla `Modelfile`, jossa on polku `.gguf` -tiedostoosi.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Esimerkkikoodi](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

Jos haluat käyttää `.gguf` -tiedostoja pilvessä ja reunalaitteissa samanaikaisesti, LlamaEdge on erinomainen valinta. Voit aloittaa tutustumalla tähän [esimerkkikoodiin](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo).

### Asenna ja käytä Android-puhelimilla

1. **Lataa MLC Chat -sovellus** (ilmainen) Android-puhelimille.
2. Lataa APK-tiedosto (148MB) ja asenna se laitteellesi.
3. Käynnistä MLC Chat -sovellus. Näet listan tekoälymalleista, mukaan lukien Phi-3-mini.

Yhteenvetona Phi-3-mini avaa jännittäviä mahdollisuuksia generatiiviselle tekoälylle reunalaitteissa, ja voit alkaa tutkia sen ominaisuuksia Androidilla.

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, ole hyvä ja huomioi, että automaattikäännöksissä voi esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulee pitää auktoritatiivisena lähteenä. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai virhetulkintatilanteista.