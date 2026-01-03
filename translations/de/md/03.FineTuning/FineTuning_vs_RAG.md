<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e4e010400c2918557b36bb932a14004c",
  "translation_date": "2025-07-17T09:26:31+00:00",
  "source_file": "md/03.FineTuning/FineTuning_vs_RAG.md",
  "language_code": "de"
}
-->
## Finetuning vs RAG

## Retrieval Augmented Generation

RAG ist Datenabruf plus Textgenerierung. Die strukturierten und unstrukturierten Daten des Unternehmens werden in der Vektordatenbank gespeichert. Bei der Suche nach relevantem Inhalt werden die passenden Zusammenfassungen und Inhalte gefunden, um einen Kontext zu bilden, und die Textvervollständigungsfunktion von LLM/SLM wird kombiniert, um Inhalte zu generieren.

## RAG-Prozess
![FinetuningvsRAG](../../../../translated_images/rag.2014adc59e6f6007.de.png)

## Fine-tuning
Fine-tuning basiert auf der Verbesserung eines bestimmten Modells. Es ist nicht nötig, mit dem Modellalgorithmus zu beginnen, aber es müssen kontinuierlich Daten gesammelt werden. Wenn Sie in Branchenanwendungen präzisere Terminologie und sprachliche Ausdrucksweise wünschen, ist Fine-tuning die bessere Wahl. Wenn sich Ihre Daten jedoch häufig ändern, kann Fine-tuning kompliziert werden.

## Wie man wählt
Wenn unsere Antwort die Einbindung externer Daten erfordert, ist RAG die beste Wahl.

Wenn Sie stabile und präzise Branchenkenntnisse ausgeben müssen, ist Fine-tuning eine gute Option. RAG legt den Fokus darauf, relevante Inhalte zu ziehen, trifft aber nicht immer die spezialisierten Nuancen.

Fine-tuning benötigt einen hochwertigen Datensatz, und wenn es sich nur um einen kleinen Datenbereich handelt, macht es kaum einen Unterschied. RAG ist flexibler.  
Fine-tuning ist eine Blackbox, eine Art Metaphysik, und es ist schwierig, den internen Mechanismus zu verstehen. RAG hingegen erleichtert es, die Datenquelle zu finden, wodurch Halluzinationen oder Fehler im Inhalt effektiv angepasst und eine bessere Transparenz geboten werden kann.

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache ist als maßgebliche Quelle zu betrachten. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.