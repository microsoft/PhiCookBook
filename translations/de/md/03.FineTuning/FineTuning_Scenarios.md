## Fine-Tuning-Szenarien

![FineTuning with MS Services](../../../../translated_images/de/FinetuningwithMS.3d0cec8ae693e094.webp)

Dieser Abschnitt bietet einen Überblick über Fine-Tuning-Szenarien in Microsoft Foundry- und Azure-Umgebungen, einschließlich Bereitstellungsmodelle, Infrastrukturebenen und häufig verwendeter Optimierungstechniken.

**Plattform**  
Dazu gehören verwaltete Dienste wie Microsoft Foundry (früher Microsoft Foundry) und Azure Machine Learning, die Modellverwaltung, Orchestrierung, Experimentverfolgung und Bereitstellungs-Workflows bereitstellen.

**Infrastruktur**  
Fine-Tuning erfordert skalierbare Rechenressourcen. In Azure-Umgebungen umfasst dies typischerweise GPU-basierte virtuelle Maschinen und CPU-Ressourcen für leichte Workloads sowie skalierbaren Speicher für Datensätze und Checkpoints.

**Werkzeuge & Framework**  
Fine-Tuning-Workflows stützen sich häufig auf Frameworks und Optimierungsbibliotheken wie Hugging Face Transformers, DeepSpeed und PEFT (Parameter-Efficient Fine-Tuning).

Der Fine-Tuning-Prozess mit Microsoft-Technologien umfasst Plattformdienste, Recheninfrastruktur und Trainingsframeworks. Durch das Verständnis, wie diese Komponenten zusammenarbeiten, können Entwickler Foundation-Modelle effizient an spezifische Aufgaben und Produktionsszenarien anpassen.

## Modell als Dienst

Feinabstimmung des Modells mittels gehostetem Fine-Tuning, ohne die Notwendigkeit, Compute zu erstellen und zu verwalten.

![MaaS Fine Tuning](../../../../translated_images/de/MaaSfinetune.3eee4630607aff0d.webp)

Serverloses Fine-Tuning ist jetzt für Modellfamilien Phi-3, Phi-3.5 und Phi-4 verfügbar und ermöglicht es Entwicklern, die Modelle schnell und einfach für Cloud- und Edge-Szenarien anzupassen, ohne Compute bereitstellen zu müssen.

## Modell als Plattform

Benutzer verwalten ihre eigene Compute-Infrastruktur, um ihre Modelle fein abzustimmen.

![Maap Fine Tuning](../../../../translated_images/de/MaaPFinetune.fd3829c1122f5d1c.webp)

[Fine Tuning Sample](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/system/finetune/chat-completion/chat-completion.ipynb)

## Vergleich der Fine-Tuning-Techniken

|Szenario|LoRA|QLoRA|PEFT|DeepSpeed|ZeRO|DoRA|
|---|---|---|---|---|---|---|
|Anpassung vortrainierter LLMs an spezifische Aufgaben oder Domänen|Ja|Ja|Ja|Ja|Ja|Ja|
|Fine-Tuning für NLP-Aufgaben wie Textklassifizierung, Named Entity Recognition und maschinelle Übersetzung|Ja|Ja|Ja|Ja|Ja|Ja|
|Fine-Tuning für QA-Aufgaben|Ja|Ja|Ja|Ja|Ja|Ja|
|Fine-Tuning zur Erzeugung menschenähnlicher Antworten in Chatbots|Ja|Ja|Ja|Ja|Ja|Ja|
|Fine-Tuning zur Erzeugung von Musik, Kunst oder anderen Kreativitätsformen|Ja|Ja|Ja|Ja|Ja|Ja|
|Reduzierung von Rechen- und Kostenaufwand|Ja|Ja|Ja|Ja|Ja|Ja|
|Reduzierung des Speicherverbrauchs|Ja|Ja|Ja|Ja|Ja|Ja|
|Verwendung weniger Parameter für effizientes Fine-Tuning|Ja|Ja|Ja|Nein|Nein|Ja|
|Speichereffiziente Form der Datenparallelität, die Zugriff auf den aggregierten GPU-Speicher aller verfügbaren GPU-Geräte ermöglicht|Nein|Nein|Nein|Ja|Ja|Nein|

> [!NOTE]
> LoRA, QLoRA, PEFT und DoRA sind parameter-effiziente Fine-Tuning-Methoden, während DeepSpeed und ZeRO sich auf verteiltes Training und Speicheroptimierung konzentrieren.

## Beispiele für Fine-Tuning-Leistung

![Finetuning Performance](../../../../translated_images/de/Finetuningexamples.a9a41214f8f5afc1.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir Genauigkeit anstreben, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das ursprüngliche Dokument in seiner Originalsprache ist als maßgebliche Quelle zu betrachten. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die durch die Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->