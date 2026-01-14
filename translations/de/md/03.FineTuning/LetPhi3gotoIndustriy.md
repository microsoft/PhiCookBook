<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "743d7e9cb9c4e8ea642d77bee657a7fa",
  "translation_date": "2025-07-17T09:51:18+00:00",
  "source_file": "md/03.FineTuning/LetPhi3gotoIndustriy.md",
  "language_code": "de"
}
-->
# **Lassen Sie Phi-3 zum Branchenexperten werden**

Um das Phi-3-Modell in einer Branche einzusetzen, müssen branchenspezifische Geschäftsdaten in das Phi-3-Modell integriert werden. Wir haben zwei verschiedene Optionen: Die erste ist RAG (Retrieval Augmented Generation) und die zweite Fine-Tuning.

## **RAG vs Fine-Tuning**

### **Retrieval Augmented Generation**

RAG ist Datenabruf + Textgenerierung. Die strukturierten und unstrukturierten Daten des Unternehmens werden in der Vektordatenbank gespeichert. Bei der Suche nach relevantem Inhalt werden die passenden Zusammenfassungen und Inhalte gefunden, um einen Kontext zu bilden, und die Textvervollständigungsfunktion von LLM/SLM wird kombiniert, um Inhalte zu generieren.

### **Fine-Tuning**

Fine-Tuning basiert auf der Verbesserung eines bestimmten Modells. Es ist nicht notwendig, mit dem Modellalgorithmus neu zu beginnen, aber es müssen kontinuierlich Daten gesammelt werden. Wenn Sie in Branchenanwendungen präzisere Terminologie und sprachliche Ausdrucksweise wünschen, ist Fine-Tuning die bessere Wahl. Wenn sich Ihre Daten jedoch häufig ändern, kann Fine-Tuning kompliziert werden.

### **Wie man wählt**

1. Wenn unsere Antwort die Einbeziehung externer Daten erfordert, ist RAG die beste Wahl.

2. Wenn Sie stabile und präzise Branchenkenntnisse ausgeben müssen, ist Fine-Tuning eine gute Wahl. RAG priorisiert das Abrufen relevanter Inhalte, trifft aber nicht immer die spezialisierten Nuancen.

3. Fine-Tuning benötigt einen hochwertigen Datensatz, und wenn es sich nur um einen kleinen Datenbereich handelt, macht es wenig Unterschied. RAG ist flexibler.

4. Fine-Tuning ist eine Blackbox, eine Art Metaphysik, und es ist schwierig, den internen Mechanismus zu verstehen. RAG hingegen erleichtert es, die Datenquelle zu finden, wodurch Halluzinationen oder Fehler im Inhalt effektiv angepasst und eine bessere Transparenz geboten werden kann.

### **Szenarien**

1. Vertikale Branchen benötigen spezifisches Fachvokabular und Ausdrucksweisen, ***Fine-Tuning*** ist hier die beste Wahl.

2. QA-Systeme, die die Synthese verschiedener Wissenspunkte erfordern, profitieren am meisten von ***RAG***.

3. Die Kombination aus automatisierten Geschäftsabläufen ist mit ***RAG + Fine-Tuning*** am effektivsten.

## **Wie man RAG verwendet**

![rag](../../../../translated_images/de/rag.2014adc59e6f6007.png)

Eine Vektordatenbank ist eine Sammlung von Daten, die in mathematischer Form gespeichert sind. Vektordatenbanken erleichtern es Machine-Learning-Modellen, sich an vorherige Eingaben zu erinnern, wodurch Machine Learning für Anwendungsfälle wie Suche, Empfehlungen und Textgenerierung unterstützt wird. Daten können anhand von Ähnlichkeitsmetriken identifiziert werden, anstatt auf exakten Übereinstimmungen zu basieren, was es Computermodellen ermöglicht, den Kontext der Daten zu verstehen.

Die Vektordatenbank ist der Schlüssel zur Umsetzung von RAG. Wir können Daten durch Vektormodelle wie text-embedding-3, jina-ai-embedding usw. in Vektorspeicher umwandeln.

Erfahren Sie mehr über die Erstellung von RAG-Anwendungen unter [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?WT.mc_id=aiml-138114-kinfeylo)

## **Wie man Fine-Tuning verwendet**

Die häufig verwendeten Algorithmen im Fine-Tuning sind Lora und QLora. Wie wählt man aus?
- [Mehr erfahren mit diesem Beispiel-Notebook](../../../../code/04.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Beispiel für Python FineTuning Sample](../../../../code/04.Finetuning/FineTrainingScript.py)

### **Lora und QLora**

![lora](../../../../translated_images/de/qlora.e6446c988ee04ca0.png)

LoRA (Low-Rank Adaptation) und QLoRA (Quantized Low-Rank Adaptation) sind Techniken, die verwendet werden, um große Sprachmodelle (LLMs) mit Parameter Efficient Fine Tuning (PEFT) zu verfeinern. PEFT-Techniken sind darauf ausgelegt, Modelle effizienter zu trainieren als traditionelle Methoden.  
LoRA ist eine eigenständige Fine-Tuning-Technik, die den Speicherbedarf reduziert, indem sie eine Niedrigrang-Approximation auf die Gewichtsmatrix anwendet. Sie bietet schnelle Trainingszeiten und hält die Leistung nahe an traditionellen Fine-Tuning-Methoden.

QLoRA ist eine erweiterte Version von LoRA, die Quantisierungstechniken integriert, um den Speicherverbrauch weiter zu reduzieren. QLoRA quantisiert die Präzision der Gewichtungsparameter im vortrainierten LLM auf 4-Bit-Präzision, was speichereffizienter ist als LoRA. Allerdings ist das Training mit QLoRA aufgrund der zusätzlichen Quantisierungs- und Dequantisierungsschritte etwa 30 % langsamer als bei LoRA.

QLoRA verwendet LoRA als Ergänzung, um Fehler zu korrigieren, die während der Quantisierung entstehen. QLoRA ermöglicht das Fine-Tuning riesiger Modelle mit Milliarden von Parametern auf relativ kleinen, weit verbreiteten GPUs. Zum Beispiel kann QLoRA ein 70B-Parameter-Modell, das normalerweise 36 GPUs benötigt, mit nur 2 GPUs feinabstimmen.

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir auf Genauigkeit achten, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache ist als maßgebliche Quelle zu betrachten. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.