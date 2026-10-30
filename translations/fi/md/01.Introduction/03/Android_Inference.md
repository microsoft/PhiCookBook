# **Inference Phi-3 Androidissa**

Tutkitaan, miten voit suorittaa inferenssiä Phi-3-minillä Android-laitteilla. Phi-3-mini on Microsoftin uusi mallisarja, joka mahdollistaa suurten kielimallien (LLM) käyttöönoton reunalaitteissa ja IoT-laitteissa.

## Semantic Kernel ja Inferenssi

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) on sovelluskehys, jonka avulla voit luoda sovelluksia, jotka toimivat Azure OpenAI -palvelun, OpenAI-mallien ja paikallisten mallien kanssa. Jos olet uusi Semantic Kernelin käyttäjä, suosittelemme tutustumaan [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) -oppaaseen.

### Phi-3-minin käyttöönotto Semantic Kernelin kautta

Voit yhdistää sen Semantic Kernelin Hugging Face Connectoriin. Katso tämä [esimerkkikoodi](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo).

Oletuksena se vastaa mallin tunnistetta Hugging Facessa. Voit kuitenkin myös yhdistää paikallisesti rakennettuun Phi-3-mini -mallipalvelimeen.

### Kvantisoitujen mallien kutsuminen Ollamalla tai LlamaEdgellä

Monet käyttäjät suosivat kvantisoituja malleja ajettaessa malleja paikallisesti. [Ollama](https://ollama.com/) ja [LlamaEdge](https://llamaedge.com) antavat yksittäisten käyttäjien kutsua erilaisia kvantisoituja malleja:

#### Ollama

Voit ajaa `ollama run Phi-3` suoraan tai määrittää sen offline-tilassa luomalla `Modelfile` tiedoston, jossa on polku `.gguf` tiedostoosi.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Esimerkkikoodi](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

Jos haluat käyttää `.gguf` tiedostoja sekä pilvessä että reunalaitteilla samanaikaisesti, LlamaEdge on loistava valinta. Voit aloittaa tämän [esimerkkikoodin](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) avulla.

### Asenna ja suorita Android-puhelimissa

1. **Lataa MLC Chat -sovellus** (ilmainen) Android-puhelimille.
2. Lataa APK-tiedosto (148 Mt) ja asenna se laitteellesi.
3. Käynnistä MLC Chat -sovellus. Näet listan tekoälymalleista, mukaan lukien Phi-3-mini.

### Käynnistä Phi-4-mini-reasoning LiteRT-LM:llä

[Phi-4-mini-reasoning](https://huggingface.co/litert-community/Phi-4-mini-reasoning) on saatavilla yhteisön muuntamana int4 `.litertlm` pakettina Googlen [LiteRT-LM](https://github.com/google-ai-edge/LiteRT-LM) laiteajona. Androidilla se toimii CPU:lla tai GPU:lla [Google AI Edge Gallery](https://github.com/google-ai-edge/gallery) -sovelluksen kautta (tuo paketti Hugging Facesta sovelluksen sisällä) tai LiteRT-LM Kotlin API:n kautta; sama paketti toimii myös iOS:lla, macOS:llä, Linuxilla ja Windowsilla. Mallikortissa on listattu mitatut nopeudet ja ajokomennot.

Yhteenvetona Phi-3-mini tarjoaa jännittäviä mahdollisuuksia generatiiviselle tekoälylle reunalaitteissa, ja voit aloittaa sen ominaisuuksien tutkimisen Androidilla.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->