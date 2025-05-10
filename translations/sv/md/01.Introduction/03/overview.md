<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1ff728038c4f554b660a36b76cbdd6e",
  "translation_date": "2025-05-09T12:26:08+00:00",
  "source_file": "md/01.Introduction/03/overview.md",
  "language_code": "sv"
}
-->
I sammanhanget med Phi-3-mini syftar inferens på processen att använda modellen för att göra förutsägelser eller generera resultat baserat på indata. Låt mig ge dig mer information om Phi-3-mini och dess inferensmöjligheter.

Phi-3-mini är en del av Phi-3-serien av modeller som släppts av Microsoft. Dessa modeller är utformade för att omdefiniera vad som är möjligt med små språkmodeller (SLMs).

Här är några viktiga punkter om Phi-3-mini och dess inferensmöjligheter:

## **Översikt av Phi-3-mini:**
- Phi-3-mini har en parameterstorlek på 3,8 miljarder.
- Den kan köras inte bara på traditionella datorer utan även på edge-enheter som mobila enheter och IoT-enheter.
- Lanseringen av Phi-3-mini gör det möjligt för både privatpersoner och företag att distribuera SLMs på olika hårdvaruenheter, särskilt i miljöer med begränsade resurser.
- Den stöder flera modellformat, inklusive det traditionella PyTorch-formatet, den kvantiserade versionen av gguf-formatet och den ONNX-baserade kvantiserade versionen.

## **Åtkomst till Phi-3-mini:**
För att få åtkomst till Phi-3-mini kan du använda [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) i en Copilot-applikation. Semantic Kernel är generellt kompatibelt med Azure OpenAI Service, open-source modeller på Hugging Face och lokala modeller.
Du kan också använda [Ollama](https://ollama.com) eller [LlamaEdge](https://llamaedge.com) för att anropa kvantiserade modeller. Ollama tillåter enskilda användare att anropa olika kvantiserade modeller, medan LlamaEdge erbjuder plattformsoberoende tillgång till GGUF-modeller.

## **Kvantiserade modeller:**
Många användare föredrar att använda kvantiserade modeller för lokal inferens. Till exempel kan du direkt köra Ollama run Phi-3 eller konfigurera det offline med en Modelfile. Modelfilen specificerar sökvägen till GGUF-filen och promptformatet.

## **Möjligheter med generativ AI:**
Kombinationen av SLMs som Phi-3-mini öppnar upp nya möjligheter för generativ AI. Inferens är bara det första steget; dessa modeller kan användas för olika uppgifter i resursbegränsade, latenskrävande och kostnadsbegränsade scenarier.

## **Frigör generativ AI med Phi-3-mini: En guide till inferens och distribution**  
Lär dig hur du använder Semantic Kernel, Ollama/LlamaEdge och ONNX Runtime för att få åtkomst till och göra inferens med Phi-3-mini-modeller, och utforska möjligheterna med generativ AI i olika applikationsscenarier.

**Funktioner**  
Inferens av phi3-mini-modellen i:

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)

Sammanfattningsvis gör Phi-3-mini det möjligt för utvecklare att utforska olika modellformat och dra nytta av generativ AI i olika applikationsscenarier.

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår vid användning av denna översättning.