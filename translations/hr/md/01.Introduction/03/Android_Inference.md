<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9481b07dda8f9715a5d1ff43fb27568b",
  "translation_date": "2025-05-09T10:52:47+00:00",
  "source_file": "md/01.Introduction/03/Android_Inference.md",
  "language_code": "hr"
}
-->
# **Inference Phi-3 na Androidu**

Pogledajmo kako možete izvesti inferencu s Phi-3-mini na Android uređajima. Phi-3-mini je nova serija modela iz Microsofta koja omogućava implementaciju velikih jezičnih modela (LLM) na edge i IoT uređajima.

## Semantic Kernel i Inference

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) je aplikacijski okvir koji vam omogućuje stvaranje aplikacija kompatibilnih s Azure OpenAI servisom, OpenAI modelima, pa čak i lokalnim modelima. Ako ste novi u Semantic Kernelu, preporučujemo da pogledate [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo).

### Kako pristupiti Phi-3-mini koristeći Semantic Kernel

Možete ga kombinirati s Hugging Face Connectorom u Semantic Kernelu. Pogledajte ovaj [primjer koda](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo).

Po defaultu, koristi model ID na Hugging Faceu, no također se možete povezati s lokalno izgrađenim Phi-3-mini model serverom.

### Pozivanje kvantiziranih modela s Ollama ili LlamaEdge

Mnogi korisnici preferiraju korištenje kvantiziranih modela za lokalno pokretanje modela. [Ollama](https://ollama.com/) i [LlamaEdge](https://llamaedge.com) omogućuju pojedinačnim korisnicima pozivanje različitih kvantiziranih modela:

#### Ollama

Možete direktno pokrenuti `ollama run Phi-3` ili ga konfigurirati offline stvaranjem `Modelfile` s putanjom do vašeg `.gguf` fajla.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Primjer koda](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

Ako želite koristiti `.gguf` fajlove u oblaku i na edge uređajima istovremeno, LlamaEdge je odličan izbor. Za početak pogledajte ovaj [primjer koda](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo).

### Instalacija i pokretanje na Android telefonima

1. **Preuzmite MLC Chat aplikaciju** (besplatno) za Android telefone.  
2. Preuzmite APK datoteku (148MB) i instalirajte je na svoj uređaj.  
3. Pokrenite MLC Chat aplikaciju. Vidjet ćete popis AI modela, uključujući Phi-3-mini.

Ukratko, Phi-3-mini otvara uzbudljive mogućnosti za generativnu AI na edge uređajima, a možete početi istraživati njegove mogućnosti na Androidu.

**Odricanje od odgovornosti**:  
Ovaj je dokument preveden korištenjem AI usluge za prijevod [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo postići točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazumevanja ili pogrešna tumačenja proizašla iz korištenja ovog prijevoda.