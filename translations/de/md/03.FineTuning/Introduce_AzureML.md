<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7fe541373802e33568e94e13226d463c",
  "translation_date": "2025-07-17T09:33:29+00:00",
  "source_file": "md/03.FineTuning/Introduce_AzureML.md",
  "language_code": "de"
}
-->
# **Einführung in den Azure Machine Learning Service**

[Azure Machine Learning](https://ml.azure.com?WT.mc_id=aiml-138114-kinfeylo) ist ein Cloud-Dienst zur Beschleunigung und Verwaltung des gesamten Lebenszyklus von Machine-Learning-(ML)-Projekten.

ML-Experten, Data Scientists und Ingenieure können ihn in ihrem täglichen Workflow nutzen, um:

- Modelle zu trainieren und bereitzustellen.
- Machine Learning Operations (MLOps) zu verwalten.
- Sie können ein Modell in Azure Machine Learning erstellen oder ein Modell verwenden, das auf einer Open-Source-Plattform wie PyTorch, TensorFlow oder scikit-learn entwickelt wurde.
- MLOps-Tools helfen dabei, Modelle zu überwachen, neu zu trainieren und erneut bereitzustellen.

## Für wen ist Azure Machine Learning geeignet?

**Data Scientists und ML-Ingenieure**

Sie können Tools nutzen, um ihre täglichen Arbeitsabläufe zu beschleunigen und zu automatisieren.  
Azure ML bietet Funktionen für Fairness, Erklärbarkeit, Nachverfolgung und Auditierbarkeit.

**Anwendungsentwickler:**  
Sie können Modelle nahtlos in Anwendungen oder Dienste integrieren.

**Plattformentwickler**

Sie haben Zugriff auf ein robustes Set an Tools, unterstützt durch langlebige Azure Resource Manager APIs.  
Diese Tools ermöglichen den Aufbau fortschrittlicher ML-Werkzeuge.

**Unternehmen**

Im Microsoft Azure Cloud-Umfeld profitieren Unternehmen von bewährter Sicherheit und rollenbasierter Zugriffskontrolle.  
Projekte können so eingerichtet werden, dass der Zugriff auf geschützte Daten und bestimmte Operationen kontrolliert wird.

## Produktivität für das gesamte Team  
ML-Projekte erfordern oft ein Team mit unterschiedlichen Fähigkeiten, um sie zu entwickeln und zu pflegen.

Azure ML stellt Werkzeuge bereit, mit denen Sie:  
- Mit Ihrem Team über geteilte Notebooks, Rechenressourcen, serverlose Compute-Optionen, Daten und Umgebungen zusammenarbeiten können.  
- Modelle mit Fokus auf Fairness, Erklärbarkeit, Nachverfolgung und Auditierbarkeit entwickeln, um Anforderungen an Herkunft und Compliance zu erfüllen.  
- ML-Modelle schnell und einfach in großem Maßstab bereitstellen sowie effizient mit MLOps verwalten und steuern können.  
- Machine-Learning-Workloads überall ausführen, mit integrierter Governance, Sicherheit und Compliance.

## Plattformübergreifende Tools

Jeder im ML-Team kann seine bevorzugten Werkzeuge nutzen, um die Aufgaben zu erledigen.  
Egal, ob Sie schnelle Experimente durchführen, Hyperparameter abstimmen, Pipelines erstellen oder Inferenz verwalten – Sie können vertraute Schnittstellen verwenden, darunter:  
- Azure Machine Learning Studio  
- Python SDK (v2)  
- Azure CLI (v2)  
- Azure Resource Manager REST APIs

Während Sie Modelle verfeinern und im Entwicklungszyklus zusammenarbeiten, können Sie Assets, Ressourcen und Metriken innerhalb der Azure Machine Learning Studio-Benutzeroberfläche teilen und finden.

## **LLM/SLM in Azure ML**

Azure ML hat viele Funktionen im Bereich LLM/SLM hinzugefügt und kombiniert LLMOps und SLMOps, um eine unternehmensweite Plattform für generative künstliche Intelligenz zu schaffen.

### **Modellkatalog**

Unternehmensnutzer können über den Modellkatalog verschiedene Modelle je nach Geschäftsszenario bereitstellen und als Model as Service für Entwickler oder Nutzer im Unternehmen zugänglich machen.

![models](../../../../translated_images/de/models.e6c7ff50a51806fd.png)

Der Modellkatalog im Azure Machine Learning Studio ist die zentrale Anlaufstelle, um eine breite Palette von Modellen zu entdecken und zu nutzen, die den Aufbau generativer KI-Anwendungen ermöglichen. Der Modellkatalog umfasst Hunderte von Modellen verschiedener Anbieter wie Azure OpenAI Service, Mistral, Meta, Cohere, Nvidia, Hugging Face sowie von Microsoft trainierte Modelle. Modelle von Anbietern außerhalb von Microsoft gelten als Non-Microsoft Products, wie in den Microsoft-Produktbedingungen definiert, und unterliegen den jeweiligen Nutzungsbedingungen.

### **Job-Pipeline**

Der Kern einer Machine-Learning-Pipeline besteht darin, eine komplette ML-Aufgabe in einen mehrstufigen Workflow zu unterteilen. Jeder Schritt ist eine überschaubare Komponente, die einzeln entwickelt, optimiert, konfiguriert und automatisiert werden kann. Die Schritte sind über klar definierte Schnittstellen verbunden. Der Azure Machine Learning Pipeline-Dienst orchestriert automatisch alle Abhängigkeiten zwischen den einzelnen Schritten.

Beim Feintuning von SLM / LLM können wir unsere Daten-, Trainings- und Generierungsprozesse über Pipelines verwalten.

![finetuning](../../../../translated_images/de/finetuning.6559da198851fa52.png)

### **Prompt Flow**

Vorteile der Nutzung von Azure Machine Learning Prompt Flow  
Azure Machine Learning Prompt Flow bietet eine Reihe von Vorteilen, die Nutzern helfen, von der Ideenfindung über Experimente bis hin zu produktionsreifen, auf LLM basierenden Anwendungen zu gelangen:

**Agilität im Prompt Engineering**

Interaktive Erstellungserfahrung: Azure Machine Learning Prompt Flow bietet eine visuelle Darstellung der Struktur des Flows, die es Nutzern erleichtert, ihre Projekte zu verstehen und zu navigieren. Zudem gibt es eine notebookähnliche Codiererfahrung für effiziente Entwicklung und Debugging.  
Varianten für Prompt-Tuning: Nutzer können mehrere Prompt-Varianten erstellen und vergleichen, was einen iterativen Verfeinerungsprozess unterstützt.

Evaluation: Eingebaute Evaluationsflows ermöglichen es, die Qualität und Effektivität von Prompts und Flows zu bewerten.

Umfangreiche Ressourcen: Azure Machine Learning Prompt Flow enthält eine Bibliothek mit integrierten Tools, Beispielen und Vorlagen, die als Ausgangspunkt für die Entwicklung dienen, Kreativität fördern und den Prozess beschleunigen.

**Unternehmensreife für LLM-basierte Anwendungen**

Zusammenarbeit: Azure Machine Learning Prompt Flow unterstützt Teamarbeit, sodass mehrere Nutzer gemeinsam an Prompt-Engineering-Projekten arbeiten, Wissen teilen und Versionskontrolle nutzen können.

All-in-One-Plattform: Azure Machine Learning Prompt Flow vereinfacht den gesamten Prompt-Engineering-Prozess – von Entwicklung und Evaluation bis hin zu Bereitstellung und Überwachung. Nutzer können ihre Flows mühelos als Azure Machine Learning Endpunkte bereitstellen und deren Leistung in Echtzeit überwachen, um optimale Abläufe und kontinuierliche Verbesserungen sicherzustellen.

Azure Machine Learning Enterprise Readiness Solutions: Prompt Flow nutzt die robusten Enterprise-Readiness-Lösungen von Azure Machine Learning und bietet eine sichere, skalierbare und zuverlässige Basis für Entwicklung, Experimentieren und Bereitstellung von Flows.

Mit Azure Machine Learning Prompt Flow können Nutzer ihre Agilität im Prompt Engineering entfalten, effektiv zusammenarbeiten und Enterprise-Lösungen für eine erfolgreiche Entwicklung und Bereitstellung von LLM-basierten Anwendungen nutzen.

Durch die Kombination der Rechenleistung, Daten und verschiedenen Komponenten von Azure ML können Unternehmensentwickler ihre eigenen KI-Anwendungen einfach erstellen.

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache ist als maßgebliche Quelle zu betrachten. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.