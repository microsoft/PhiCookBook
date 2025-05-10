<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1ff728038c4f554b660a36b76cbdd6e",
  "translation_date": "2025-05-09T12:33:44+00:00",
  "source_file": "md/01.Introduction/03/overview.md",
  "language_code": "sr"
}
-->
U kontekstu Phi-3-mini, inferencija se odnosi na proces korišćenja modela za pravljenje predviđanja ili generisanje izlaza na osnovu ulaznih podataka. Dozvolite mi da vam pružim više detalja o Phi-3-mini i njegovim mogućnostima inferencije.

Phi-3-mini je deo Phi-3 serije modela koje je izdao Microsoft. Ovi modeli su dizajnirani da redefinišu šta je moguće sa malim jezičkim modelima (SLM).

Evo nekoliko ključnih tačaka o Phi-3-mini i njegovim mogućnostima inferencije:

## **Pregled Phi-3-mini:**
- Phi-3-mini ima veličinu od 3,8 milijardi parametara.
- Može da radi ne samo na tradicionalnim računarima, već i na edge uređajima kao što su mobilni telefoni i IoT uređaji.
- Objavljivanje Phi-3-mini omogućava pojedincima i preduzećima da implementiraju SLM-ove na različitim hardverskim uređajima, naročito u uslovima sa ograničenim resursima.
- Podržava različite formate modela, uključujući tradicionalni PyTorch format, kvantizovanu verziju gguf formata i ONNX baziranu kvantizovanu verziju.

## **Pristup Phi-3-mini:**
Da biste pristupili Phi-3-mini, možete koristiti [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) u Copilot aplikaciji. Semantic Kernel je uglavnom kompatibilan sa Azure OpenAI servisom, open-source modelima sa Hugging Face i lokalnim modelima.
Takođe možete koristiti [Ollama](https://ollama.com) ili [LlamaEdge](https://llamaedge.com) za pozivanje kvantizovanih modela. Ollama omogućava pojedinačnim korisnicima da pozivaju različite kvantizovane modele, dok LlamaEdge pruža multiplatformsku dostupnost za GGUF modele.

## **Kvantizovani modeli:**
Mnogi korisnici preferiraju korišćenje kvantizovanih modela za lokalnu inferenciju. Na primer, možete direktno pokrenuti Ollama za Phi-3 ili ga konfigurisati offline koristeći Modelfile. Modelfile specificira putanju do GGUF fajla i format prompta.

## **Mogućnosti generativne AI:**
Kombinovanjem SLM-ova poput Phi-3-mini otvaraju se nove mogućnosti za generativnu AI. Inferencija je samo prvi korak; ovi modeli mogu se koristiti za razne zadatke u okruženjima sa ograničenim resursima, gde je važna latencija i kontrola troškova.

## **Otključavanje generativne AI sa Phi-3-mini: Vodič za inferenciju i implementaciju**
Naučite kako da koristite Semantic Kernel, Ollama/LlamaEdge i ONNX Runtime za pristup i inferenciju Phi-3-mini modela, i istražite mogućnosti generativne AI u različitim scenarijima primene.

**Karakteristike**
Inferencija phi3-mini modela u:

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)

Ukratko, Phi-3-mini omogućava programerima da istraže različite formate modela i iskoriste generativnu AI u raznim scenarijima primene.

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI сервиса за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да превод буде тачан, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.