<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9481b07dda8f9715a5d1ff43fb27568b",
  "translation_date": "2025-05-09T10:52:26+00:00",
  "source_file": "md/01.Introduction/03/Android_Inference.md",
  "language_code": "sr"
}
-->
# **Inference Phi-3 na Androidu**

Hajde da istražimo kako možete izvršiti inferencu sa Phi-3-mini na Android uređajima. Phi-3-mini je nova serija modela iz Microsofta koja omogućava implementaciju velikih jezičkih modela (LLM) na edge uređajima i IoT uređajima.

## Semantic Kernel i Inference

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) je aplikacioni okvir koji vam omogućava da kreirate aplikacije kompatibilne sa Azure OpenAI Service, OpenAI modelima, pa čak i lokalnim modelima. Ako ste novi u Semantic Kernel, preporučujemo da pogledate [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo).

### Kako pristupiti Phi-3-mini koristeći Semantic Kernel

Možete ga kombinovati sa Hugging Face Connector u Semantic Kernel-u. Pogledajte ovaj [primer koda](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo).

Podrazumevano, koristi model ID sa Hugging Face-a. Međutim, možete se povezati i na lokalno izgrađeni Phi-3-mini model server.

### Pozivanje kvantizovanih modela sa Ollama ili LlamaEdge

Mnogi korisnici preferiraju korišćenje kvantizovanih modela za lokalno pokretanje modela. [Ollama](https://ollama.com/) i [LlamaEdge](https://llamaedge.com) omogućavaju pojedinačnim korisnicima da pozivaju različite kvantizovane modele:

#### Ollama

Možete direktno pokrenuti `ollama run Phi-3` ili ga podesiti offline kreiranjem `Modelfile` sa putanjom do vašeg `.gguf` fajla.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Primer koda](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

Ako želite da koristite `.gguf` fajlove istovremeno u oblaku i na edge uređajima, LlamaEdge je odličan izbor. Možete pogledati ovaj [primer koda](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) za početak.

### Instalacija i pokretanje na Android telefonima

1. **Preuzmite MLC Chat aplikaciju** (besplatno) za Android telefone.  
2. Preuzmite APK fajl (148MB) i instalirajte ga na svoj uređaj.  
3. Pokrenite MLC Chat aplikaciju. Videćete listu AI modela, uključujući Phi-3-mini.

Ukratko, Phi-3-mini otvara uzbudljive mogućnosti za generativnu veštačku inteligenciju na edge uređajima, i možete početi da istražujete njegove mogućnosti na Androidu.

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI услуге за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако настојимо да превод буде тачан, молимо вас да имате у виду да аутоматизовани преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални превод од стране људског стручњака. Не одговарамо за било каква неспоразума или погрешне тумачења настала коришћењем овог превода.