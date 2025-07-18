<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "92e7dac1e5af0dd7c94170fdaf6860fe",
  "translation_date": "2025-07-17T02:56:42+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md",
  "language_code": "de"
}
-->
# Verwendung der Windows-GPU zur Erstellung einer PromptFlow-Lösung mit Phi-3.5-Instruct ONNX

Das folgende Dokument zeigt ein Beispiel, wie man PromptFlow mit ONNX (Open Neural Network Exchange) verwendet, um KI-Anwendungen auf Basis von Phi-3-Modellen zu entwickeln.

PromptFlow ist eine Sammlung von Entwicklungstools, die den gesamten Entwicklungszyklus von KI-Anwendungen auf Basis von LLMs (Large Language Models) vereinfachen – von der Ideenfindung und Prototypenerstellung bis hin zu Tests und Evaluation.

Durch die Integration von PromptFlow mit ONNX können Entwickler:

- Modellleistung optimieren: ONNX für effiziente Modellausführung und Bereitstellung nutzen.
- Entwicklung vereinfachen: PromptFlow verwenden, um den Workflow zu steuern und wiederkehrende Aufgaben zu automatisieren.
- Zusammenarbeit verbessern: Bessere Teamarbeit durch eine einheitliche Entwicklungsumgebung ermöglichen.

**PromptFlow** ist eine Sammlung von Entwicklungstools, die den gesamten Entwicklungszyklus von LLM-basierten KI-Anwendungen vereinfachen – von der Ideenfindung, Prototypenerstellung, Tests und Evaluation bis hin zur produktiven Bereitstellung und Überwachung. Es macht Prompt Engineering deutlich einfacher und ermöglicht es, LLM-Anwendungen in Produktionsqualität zu erstellen.

PromptFlow kann sich mit OpenAI, Azure OpenAI Service und anpassbaren Modellen (Huggingface, lokale LLM/SLM) verbinden. Wir planen, das quantisierte ONNX-Modell von Phi-3.5 in lokalen Anwendungen einzusetzen. PromptFlow hilft uns dabei, unser Geschäft besser zu planen und lokale Lösungen auf Basis von Phi-3.5 zu realisieren. In diesem Beispiel kombinieren wir die ONNX Runtime GenAI Library, um die PromptFlow-Lösung auf einer Windows-GPU umzusetzen.

## **Installation**

### **ONNX Runtime GenAI für Windows GPU**

Lies diese Anleitung, um ONNX Runtime GenAI für Windows GPU einzurichten: [hier klicken](./ORTWindowGPUGuideline.md)

### **PromptFlow in VSCode einrichten**

1. Installiere die PromptFlow VS Code Erweiterung

![pfvscode](../../../../../../translated_images/pfvscode.eff93dfc66a42cbef699fc16fa48f3ed3a23361875a3362037d026896395a00d.de.png)

2. Nach der Installation der PromptFlow VS Code Erweiterung, klicke auf die Erweiterung und wähle **Installation dependencies**. Folge dieser Anleitung, um das PromptFlow SDK in deiner Umgebung zu installieren.

![pfsetup](../../../../../../translated_images/pfsetup.b46e93096f5a254f74e8b74ce2be7047ce963ef573d755ec897eb1b78cb9c954.de.png)

3. Lade den [Beispielcode](../../../../../../code/09.UpdateSamples/Aug/pf/onnx_inference_pf) herunter und öffne das Beispiel mit VS Code

![pfsample](../../../../../../translated_images/pfsample.8d89e70584ffe7c4dba182513e3148a989e552c3b8e4948567a6b806b5ae1845.de.png)

4. Öffne **flow.dag.yaml**, um deine Python-Umgebung auszuwählen

![pfdag](../../../../../../translated_images/pfdag.264a77f7366458ff850a76ae949226391ea382856d543ef9da4b92096aff7e4b.de.png)

   Öffne **chat_phi3_ort.py**, um den Speicherort deines Phi-3.5-instruct ONNX-Modells anzupassen

![pfphi](../../../../../../translated_images/pfphi.72da81d74244b45fc78cdfeeb8c7fbd9e7cd610bf2f96814dbade6a4a2dfad7e.de.png)

5. Starte deinen PromptFlow-Testlauf

Öffne **flow.dag.yaml** und klicke auf den visuellen Editor

![pfv](../../../../../../translated_images/pfv.ba8a81f34b20f603cccee3fe91e94113792ed6f5af28f76ab08e1a0b3e77b33b.de.png)

Klicke darauf und führe den Testlauf aus

![pfflow](../../../../../../translated_images/pfflow.4e1135a089b1ce1b6348b59edefdb6333e5729b54c8e57f9039b7f9463e68fbd.de.png)

1. Du kannst auch im Terminal Batch-Läufe starten, um weitere Ergebnisse zu prüfen


```bash

pf run create --file batch_run.yaml --stream --name 'Your eval qa name'    

```

Die Ergebnisse kannst du in deinem Standardbrowser ansehen


![pfresult](../../../../../../translated_images/pfresult.c22c826f8062d7cbe871cff35db4a013dcfefc13fafe5da6710a8549a96a4ceb.de.png)

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.