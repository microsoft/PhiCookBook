<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e0a07fd2a30fe2af30b1373df207a5bf",
  "translation_date": "2025-03-27T15:01:48+00:00",
  "source_file": "md\\03.FineTuning\\FineTuning_Phi-3-visionWandB.md",
  "language_code": "de"
}
-->
# Phi-3-Vision-128K-Instruct Projektübersicht

## Das Modell

Das Phi-3-Vision-128K-Instruct ist ein leichtgewichtiges, hochmodernes multimodales Modell und steht im Mittelpunkt dieses Projekts. Es gehört zur Phi-3-Modellfamilie und unterstützt eine Kontextlänge von bis zu 128.000 Tokens. Das Modell wurde auf einem vielfältigen Datensatz trainiert, der sowohl synthetische Daten als auch sorgfältig gefilterte, öffentlich zugängliche Websites umfasst. Der Schwerpunkt lag dabei auf qualitativ hochwertigen, anspruchsvollen Inhalten, die intensives logisches Denken erfordern. Der Trainingsprozess umfasste überwachte Feinabstimmung und direkte Präferenzoptimierung, um eine präzise Befolgung von Anweisungen sowie robuste Sicherheitsmaßnahmen sicherzustellen.

## Warum die Erstellung von Beispieldaten entscheidend ist:

1. **Testen**: Beispieldaten ermöglichen es, Ihre Anwendung unter verschiedenen Szenarien zu testen, ohne reale Daten zu beeinträchtigen. Dies ist besonders in der Entwicklungs- und Staging-Phase wichtig.

2. **Leistungsoptimierung**: Mit Beispieldaten, die Umfang und Komplexität echter Daten nachahmen, können Sie Leistungsengpässe identifizieren und Ihre Anwendung entsprechend optimieren.

3. **Prototyping**: Beispieldaten können verwendet werden, um Prototypen und Mockups zu erstellen. Diese helfen, Benutzeranforderungen zu verstehen und Feedback zu erhalten.

4. **Datenanalyse**: In der Datenwissenschaft werden Beispieldaten häufig für explorative Datenanalysen, Modelltraining und Algorithmustests verwendet.

5. **Sicherheit**: Der Einsatz von Beispieldaten in Entwicklungs- und Testumgebungen kann helfen, versehentliche Datenlecks sensibler realer Daten zu verhindern.

6. **Lernen**: Wenn Sie eine neue Technologie oder ein neues Tool erlernen, können Beispieldaten eine praktische Möglichkeit bieten, das Gelernte anzuwenden.

Denken Sie daran, dass die Qualität Ihrer Beispieldaten diese Aktivitäten erheblich beeinflussen kann. Sie sollten in Struktur und Variabilität so nah wie möglich an den echten Daten sein.

### Erstellung von Beispieldaten
[Generate DataSet Script](./CreatingSampleData.md)

## Datensatz

Ein gutes Beispiel für einen Beispieldatensatz ist der [DBQ/Burberry.Product.prices.United.States Datensatz](https://huggingface.co/datasets/DBQ/Burberry.Product.prices.United.States) (verfügbar auf Huggingface).  
Der Beispieldatensatz enthält Burberry-Produkte zusammen mit Metadaten zu Produktkategorie, Preis und Titel. Insgesamt umfasst er 3.040 Zeilen, wobei jede Zeile ein einzigartiges Produkt repräsentiert. Dieser Datensatz ermöglicht es, die Fähigkeit des Modells zu testen, visuelle Daten zu verstehen und zu interpretieren, indem es beschreibende Texte generiert, die komplexe visuelle Details und markenspezifische Merkmale erfassen.

**Hinweis:** Sie können jeden Datensatz verwenden, der Bilder enthält.

## Komplexes logisches Denken

Das Modell muss Preise und Bezeichnungen nur anhand des Bildes ableiten. Dies erfordert, dass das Modell nicht nur visuelle Merkmale erkennt, sondern auch deren Bedeutung in Bezug auf den Produktwert und das Branding versteht. Durch die Synthese präziser Textbeschreibungen aus Bildern zeigt das Projekt das Potenzial auf, visuelle Daten zu integrieren, um die Leistung und Vielseitigkeit von Modellen in realen Anwendungen zu verbessern.

## Phi-3 Vision Architektur

Die Modellarchitektur ist eine multimodale Version eines Phi-3. Sie verarbeitet sowohl Text- als auch Bilddaten und integriert diese Eingaben in eine einheitliche Sequenz für umfassende Verständnis- und Generierungsaufgaben. Das Modell verwendet separate Einbettungsschichten für Text und Bilder. Text-Tokens werden in dichte Vektoren umgewandelt, während Bilder durch ein CLIP-Vision-Modell verarbeitet werden, um Feature-Einbettungen zu extrahieren. Diese Bildeinbettungen werden dann so projiziert, dass sie die Dimensionen der Texteinbettungen entsprechen, um eine nahtlose Integration zu gewährleisten.

## Integration von Text- und Bildeinbettungen

Spezielle Tokens innerhalb der Textsequenz geben an, wo die Bildeinbettungen eingefügt werden sollen. Während der Verarbeitung werden diese speziellen Tokens durch die entsprechenden Bildeinbettungen ersetzt, sodass das Modell Text und Bilder als eine einzige Sequenz behandeln kann. Das Prompt-Format für unseren Datensatz verwendet das spezielle <|image|>-Token wie folgt:

```python
text = f"<|user|>\n<|image_1|>What is shown in this image?<|end|><|assistant|>\nProduct: {row['title']}, Category: {row['category3_code']}, Full Price: {row['full_price']}<|end|>"
```

## Beispielcode
- [Phi-3-Vision Trainingsskript](../../../../code/03.Finetuning/Phi-3-vision-Trainingscript.py)
- [Weights and Bias Beispielanleitung](https://wandb.ai/byyoung3/mlnews3/reports/How-to-fine-tune-Phi-3-vision-on-a-custom-dataset--Vmlldzo4MTEzMTg3)

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, weisen wir darauf hin, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.