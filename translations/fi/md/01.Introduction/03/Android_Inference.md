<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9481b07dda8f9715a5d1ff43fb27568b",
  "translation_date": "2025-07-16T20:14:24+00:00",
  "source_file": "md/01.Introduction/03/Android_Inference.md",
  "language_code": "fi"
}
-->
# **Phi-3-päätelmien teko Androidilla**

Tutustutaan, miten voit suorittaa päätelmiä Phi-3-minillä Android-laitteilla. Phi-3-mini on Microsoftin uusi mallisarja, joka mahdollistaa suurten kielimallien (LLM) käyttöönoton reunalaitteissa ja IoT-laitteissa.

## Semantic Kernel ja päätelmät

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) on sovelluskehys, jonka avulla voit luoda sovelluksia, jotka toimivat Azure OpenAI -palvelun, OpenAI-mallien ja jopa paikallisten mallien kanssa. Jos olet uusi Semantic Kernelin käyttäjä, suosittelemme tutustumaan [Semantic Kernel Cookbookiin](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo).

### Phi-3-minin käyttö Semantic Kernelin kautta

Voit yhdistää sen Semantic Kernelin Hugging Face Connectoriin. Katso tämä [esimerkkikoodi](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo).

Oletuksena se vastaa Hugging Facen mallin tunnistetta, mutta voit myös yhdistää paikallisesti rakennettuun Phi-3-mini -mallipalvelimeen.

### Kvantisoitujen mallien kutsuminen Ollaman tai LlamaEdgen avulla

Monet käyttäjät suosivat kvantisoituja malleja, jotta mallit voi ajaa paikallisesti. [Ollama](https://ollama.com/) ja [LlamaEdge](https://llamaedge.com) mahdollistavat yksittäisten käyttäjien kutsua erilaisia kvantisoituja malleja:

#### Ollama

Voit ajaa suoraan `ollama run Phi-3` tai määrittää sen offline-tilassa luomalla `Modelfile`-tiedoston, jossa on polku `.gguf`-tiedostoosi.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Esimerkkikoodi](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

Jos haluat käyttää `.gguf`-tiedostoja sekä pilvessä että reunalaitteissa samanaikaisesti, LlamaEdge on erinomainen valinta. Voit aloittaa tämän [esimerkkikoodin](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) avulla.

### Asennus ja käyttö Android-puhelimilla

1. **Lataa MLC Chat -sovellus** (ilmainen) Android-puhelimille.
2. Lataa APK-tiedosto (148 Mt) ja asenna se laitteellesi.
3. Käynnistä MLC Chat -sovellus. Näet listan tekoälymalleista, mukaan lukien Phi-3-mini.

Yhteenvetona Phi-3-mini avaa jännittäviä mahdollisuuksia generatiiviselle tekoälylle reunalaitteissa, ja voit alkaa tutkia sen ominaisuuksia Androidilla.

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.