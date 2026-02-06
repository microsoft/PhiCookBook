# Phi-3-Vision-128K-Instruct Projektübersicht

## Das Modell

Das Phi-3-Vision-128K-Instruct, ein leichtgewichtiges, hochmodernes multimodales Modell, steht im Mittelpunkt dieses Projekts. Es gehört zur Phi-3 Modellfamilie und unterstützt eine Kontextlänge von bis zu 128.000 Tokens. Das Modell wurde auf einem vielfältigen Datensatz trainiert, der synthetische Daten und sorgfältig gefilterte öffentlich zugängliche Webseiten umfasst, mit Schwerpunkt auf qualitativ hochwertigen, reasoning-intensiven Inhalten. Der Trainingsprozess beinhaltete überwachte Feinabstimmung und direkte Präferenzoptimierung, um eine präzise Befolgung der Anweisungen sowie robuste Sicherheitsmaßnahmen zu gewährleisten.

## Die Erstellung von Beispieldaten ist aus mehreren Gründen entscheidend:

1. **Testen**: Beispieldaten ermöglichen es, Ihre Anwendung unter verschiedenen Szenarien zu testen, ohne echte Daten zu beeinträchtigen. Dies ist besonders wichtig in der Entwicklungs- und Staging-Phase.

2. **Leistungsoptimierung**: Mit Beispieldaten, die Umfang und Komplexität echter Daten nachahmen, können Sie Leistungsengpässe identifizieren und Ihre Anwendung entsprechend optimieren.

3. **Prototyping**: Beispieldaten können verwendet werden, um Prototypen und Mockups zu erstellen, die dabei helfen, Benutzeranforderungen zu verstehen und Feedback einzuholen.

4. **Datenanalyse**: In der Datenwissenschaft werden Beispieldaten häufig für explorative Datenanalysen, Modelltraining und Algorithmustests genutzt.

5. **Sicherheit**: Die Verwendung von Beispieldaten in Entwicklungs- und Testumgebungen kann helfen, versehentliche Datenlecks sensibler Echt-Daten zu verhindern.

6. **Lernen**: Wenn Sie eine neue Technologie oder ein neues Tool erlernen, bietet die Arbeit mit Beispieldaten eine praktische Möglichkeit, das Gelernte anzuwenden.

Denken Sie daran, dass die Qualität Ihrer Beispieldaten diese Aktivitäten maßgeblich beeinflussen kann. Sie sollten der realen Datenstruktur und -vielfalt so nahe wie möglich kommen.

### Erstellung von Beispieldaten
[Generate DataSet Script](./CreatingSampleData.md)

## Datensatz

Ein gutes Beispiel für einen Beispieldatensatz ist der [DBQ/Burberry.Product.prices.United.States Datensatz](https://huggingface.co/datasets/DBQ/Burberry.Product.prices.United.States) (verfügbar auf Huggingface).  
Der Beispieldatensatz enthält Burberry-Produkte zusammen mit Metadaten zur Produktkategorie, zum Preis und Titel mit insgesamt 3.040 Zeilen, von denen jede ein einzigartiges Produkt repräsentiert. Dieser Datensatz ermöglicht es uns, die Fähigkeit des Modells zu testen, visuelle Daten zu verstehen und zu interpretieren, indem es beschreibende Texte generiert, die feine visuelle Details und markenspezifische Merkmale erfassen.

**Note:** Sie können jeden Datensatz verwenden, der Bilder enthält.

## Komplexes Reasoning

Das Modell muss Preise und Bezeichnungen allein anhand des Bildes ableiten. Dies erfordert, dass das Modell nicht nur visuelle Merkmale erkennt, sondern auch deren Bedeutung in Bezug auf Produktwert und Markenbildung versteht. Durch die Synthese präziser Textbeschreibungen aus Bildern zeigt das Projekt das Potenzial, visuelle Daten zu integrieren, um die Leistung und Vielseitigkeit von Modellen in realen Anwendungen zu verbessern.

## Phi-3 Vision Architektur

Die Modellarchitektur ist eine multimodale Version eines Phi-3. Sie verarbeitet sowohl Text- als auch Bilddaten und integriert diese Eingaben in eine einheitliche Sequenz für umfassendes Verständnis und Generierungsaufgaben. Das Modell verwendet separate Embedding-Schichten für Text und Bilder. Texttokens werden in dichte Vektoren umgewandelt, während Bilder durch ein CLIP-Vision-Modell verarbeitet werden, um Feature-Embeddings zu extrahieren. Diese Bild-Embeddings werden anschließend so projiziert, dass sie den Dimensionen der Text-Embeddings entsprechen, um eine nahtlose Integration zu gewährleisten.

## Integration von Text- und Bild-Embeddings

Spezielle Tokens innerhalb der Textsequenz zeigen an, wo die Bild-Embeddings eingefügt werden sollen. Während der Verarbeitung werden diese speziellen Tokens durch die entsprechenden Bild-Embeddings ersetzt, sodass das Modell Text und Bilder als eine einzige Sequenz verarbeiten kann. Der Prompt für unseren Datensatz ist mit dem speziellen <|image|>-Token wie folgt formatiert:

```python
text = f"<|user|>\n<|image_1|>What is shown in this image?<|end|><|assistant|>\nProduct: {row['title']}, Category: {row['category3_code']}, Full Price: {row['full_price']}<|end|>"
```

## Beispielcode
- [Phi-3-Vision Trainingsskript](../../../../code/03.Finetuning/Phi-3-vision-Trainingscript.py)
- [Weights and Bias Beispiel-Durchgang](https://wandb.ai/byyoung3/mlnews3/reports/How-to-fine-tune-Phi-3-vision-on-a-custom-dataset--Vmlldzo4MTEzMTg3)

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir auf Genauigkeit achten, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache ist als maßgebliche Quelle zu betrachten. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.