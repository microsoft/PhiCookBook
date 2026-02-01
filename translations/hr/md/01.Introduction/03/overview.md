U kontekstu Phi-3-mini, inferencija se odnosi na proces korištenja modela za donošenje predviđanja ili generiranje izlaza na temelju ulaznih podataka. Dopustite mi da vam pružim više detalja o Phi-3-mini i njegovim mogućnostima inferencije.

Phi-3-mini je dio Phi-3 serije modela koje je izdala Microsoft. Ovi modeli su dizajnirani da redefiniraju što je moguće s malim jezičnim modelima (SLM).

Evo nekoliko ključnih točaka o Phi-3-mini i njegovim mogućnostima inferencije:

## **Pregled Phi-3-mini:**
- Phi-3-mini ima veličinu parametara od 3,8 milijardi.
- Može se pokretati ne samo na tradicionalnim računalnim uređajima, već i na edge uređajima poput mobilnih uređaja i IoT uređaja.
- Izdanje Phi-3-mini omogućuje pojedincima i tvrtkama da implementiraju SLM-ove na različitim hardverskim uređajima, posebno u okruženjima s ograničenim resursima.
- Podržava različite formate modela, uključujući tradicionalni PyTorch format, kvantiziranu verziju gguf formata i ONNX baziranu kvantiziranu verziju.

## **Pristup Phi-3-mini:**
Za pristup Phi-3-mini možete koristiti [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) u Copilot aplikaciji. Semantic Kernel je općenito kompatibilan s Azure OpenAI Service, open-source modelima na Hugging Faceu i lokalnim modelima.  
Također možete koristiti [Ollama](https://ollama.com) ili [LlamaEdge](https://llamaedge.com) za pozivanje kvantiziranih modela. Ollama omogućuje pojedinačnim korisnicima pozivanje različitih kvantiziranih modela, dok LlamaEdge pruža dostupnost GGUF modela na više platformi.

## **Kvantizirani modeli:**
Mnogi korisnici preferiraju korištenje kvantiziranih modela za lokalnu inferenciju. Na primjer, možete izravno pokrenuti Ollama za Phi-3 ili ga konfigurirati offline pomoću Modelfile datoteke. Modelfile specificira putanju do GGUF datoteke i format prompta.

## **Mogućnosti generativne umjetne inteligencije:**
Kombinacija SLM-ova poput Phi-3-mini otvara nove mogućnosti za generativnu umjetnu inteligenciju. Inferencija je samo prvi korak; ovi modeli se mogu koristiti za različite zadatke u okruženjima s ograničenim resursima, niskom latencijom i ograničenim troškovima.

## **Otključavanje generativne AI s Phi-3-mini: vodič za inferenciju i implementaciju**  
Naučite kako koristiti Semantic Kernel, Ollama/LlamaEdge i ONNX Runtime za pristup i inferenciju Phi-3-mini modela te istražite mogućnosti generativne AI u različitim scenarijima primjene.

**Značajke**  
Inferencija phi3-mini modela u:

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)  
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)  
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)  
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)  
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)  

Ukratko, Phi-3-mini omogućuje programerima da istraže različite formate modela i iskoriste generativnu AI u raznim scenarijima primjene.

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.