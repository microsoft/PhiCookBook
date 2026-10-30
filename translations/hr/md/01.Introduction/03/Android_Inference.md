# **Inferencija Phi-3 na Androidu**

Istražimo kako možete izvesti inferenciju s Phi-3-mini na Android uređajima. Phi-3-mini je nova serija modela iz Microsofta koja omogućuje implementaciju Velikih jezičnih modela (LLM) na edge uređajima i IoT uređajima.

## Semantic Kernel i Inferencija

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) je aplikacijski okvir koji vam omogućuje kreiranje aplikacija kompatibilnih s Azure OpenAI Service, OpenAI modelima, pa čak i lokalnim modelima. Ako ste novi u Semantic Kernelu, predlažemo da pogledate [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo).

### Pristup Phi-3-mini koristeći Semantic Kernel

Možete ga kombinirati s Hugging Face Connectorom u Semantic Kernelu. Pogledajte ovaj [primjer koda](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo).

Po zadanim postavkama, to odgovara ID-u modela na Hugging Faceu. Međutim, također se možete povezati s lokalno izgrađenim poslužiteljem modela Phi-3-mini.

### Pozivanje kvantiziranih modela s Ollama ili LlamaEdge

Mnogi korisnici preferiraju korištenje kvantiziranih modela za lokalno pokretanje modela. [Ollama](https://ollama.com/) i [LlamaEdge](https://llamaedge.com) omogućuju pojedinačnim korisnicima pozivanje različitih kvantiziranih modela:

#### Ollama

Možete ga izravno pokrenuti `ollama run Phi-3` ili ga konfigurirati offline tako da kreirate `Modelfile` s putanjom do vaše `.gguf` datoteke.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Primjer koda](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

Ako želite koristiti `.gguf` datoteke u oblaku i na edge uređajima istovremeno, LlamaEdge je izvrstan izbor. Možete se poslužiti ovim [primjerom koda](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) za početak.

### Instalirajte i pokrenite na Android telefonima

1. **Preuzmite MLC Chat aplikaciju** (Besplatno) za Android telefone.
2. Preuzmite APK datoteku (148MB) i instalirajte je na svoj uređaj.
3. Pokrenite MLC Chat aplikaciju. Vidjet ćete popis AI modela, uključujući Phi-3-mini.

### Pokrenite Phi-4-mini-reasoning s LiteRT-LM

[Phi-4-mini-reasoning](https://huggingface.co/litert-community/Phi-4-mini-reasoning) dostupan je kao zajednički konvertirani int4 `.litertlm` paket za Googleov [LiteRT-LM](https://github.com/google-ai-edge/LiteRT-LM) runtime na uređaju. Na Androidu radi na CPU-u ili GPU-u putem [Google AI Edge Gallery](https://github.com/google-ai-edge/gallery) aplikacije (uvoz paketa s Hugging Facea unutar aplikacije) ili putem LiteRT-LM Kotlin API-ja; isti paket radi i na iOS-u, macOS-u, Linuxu i Windowsu. Kartica modela navodi izmjerene brzine i naredbe za pokretanje.

Ukratko, Phi-3-mini otvara uzbudljive mogućnosti za generativnu AI na edge uređajima, i možete započeti istraživati njegove mogućnosti na Androidu.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->