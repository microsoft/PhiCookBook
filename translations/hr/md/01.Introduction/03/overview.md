<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1ff728038c4f554b660a36b76cbdd6e",
  "translation_date": "2025-05-09T12:34:13+00:00",
  "source_file": "md/01.Introduction/03/overview.md",
  "language_code": "hr"
}
-->
U kontekstu Phi-3-mini, inference se odnosi na proces korištenja modela za donošenje predviđanja ili generiranje izlaza na temelju ulaznih podataka. Dopustite mi da vam pružim više detalja o Phi-3-mini i njegovim mogućnostima inference.

Phi-3-mini je dio serije modela Phi-3 koju je izdala Microsoft. Ovi modeli su dizajnirani da redefiniraju što je moguće sa Small Language Models (SLM).

Evo nekoliko ključnih točaka o Phi-3-mini i njegovim mogućnostima inference:

## **Pregled Phi-3-mini:**
- Phi-3-mini ima veličinu parametara od 3,8 milijardi.
- Može se pokretati ne samo na tradicionalnim računalnim uređajima, već i na edge uređajima poput mobilnih i IoT uređaja.
- Izlazak Phi-3-mini omogućuje pojedincima i poduzećima da implementiraju SLM-ove na različitim hardverskim uređajima, posebno u okruženjima s ograničenim resursima.
- Podržava različite formate modela, uključujući tradicionalni PyTorch format, kvantiziranu verziju gguf formata i ONNX baziranu kvantiziranu verziju.

## **Pristup Phi-3-mini:**
Za pristup Phi-3-mini, možete koristiti [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) u Copilot aplikaciji. Semantic Kernel je općenito kompatibilan s Azure OpenAI Service, open-source modelima na Hugging Faceu i lokalnim modelima.
Također možete koristiti [Ollama](https://ollama.com) ili [LlamaEdge](https://llamaedge.com) za pozivanje kvantiziranih modela. Ollama omogućuje pojedinačnim korisnicima pozivanje različitih kvantiziranih modela, dok LlamaEdge pruža dostupnost na više platformi za GGUF modele.

## **Kvantizirani modeli:**
Mnogi korisnici preferiraju korištenje kvantiziranih modela za lokalni inference. Na primjer, možete izravno pokrenuti Ollama run Phi-3 ili ga konfigurirati offline pomoću Modelfile-a. Modelfile specificira putanju do GGUF datoteke i format prompta.

## **Mogućnosti generativne AI:**
Kombinacija SLM-ova poput Phi-3-mini otvara nove mogućnosti za generativnu AI. Inference je samo prvi korak; ovi modeli se mogu koristiti za razne zadatke u okruženjima s ograničenim resursima, ograničenjima latencije i troškovima.

## **Otključavanje generativne AI s Phi-3-mini: Vodič za inference i implementaciju**  
Naučite kako koristiti Semantic Kernel, Ollama/LlamaEdge i ONNX Runtime za pristup i inference Phi-3-mini modela, te istražite mogućnosti generativne AI u različitim scenarijima primjene.

**Značajke**  
Inference phi3-mini modela u:

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)

Ukratko, Phi-3-mini omogućuje developerima istraživanje različitih formata modela i iskorištavanje generativne AI u raznim scenarijima primjene.

**Odricanje od odgovornosti**:  
Ovaj je dokument preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo postići točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati službenim i autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakve nesporazume ili kriva tumačenja koja proizlaze iz korištenja ovog prijevoda.