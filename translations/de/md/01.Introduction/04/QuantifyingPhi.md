<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f4cbbe7bf3e764de52d64a96d97b3c35",
  "translation_date": "2026-01-04T06:56:56+00:00",
  "source_file": "md/01.Introduction/04/QuantifyingPhi.md",
  "language_code": "de"
}
-->
# **Quantifizierung der Phi-Familie**

Modellquantisierung bezieht sich auf den Prozess, die Parameter (wie Gewichte und Aktivierungswerte) in einem neuronalen Netzwerkmodell aus einem großen Wertebereich (in der Regel ein kontinuierlicher Wertebereich) in einen kleineren, endlichen Wertebereich abzubilden. Diese Technologie kann die Größe und die rechnerische Komplexität des Modells reduzieren und die Betriebseffizienz des Modells in ressourcenbeschränkten Umgebungen wie Mobilgeräten oder eingebetteten Systemen verbessern. Modellquantisierung erreicht Kompression durch Verringerung der Präzision der Parameter, führt dabei jedoch auch zu einem gewissen Präzisionsverlust. Daher ist es im Quantisierungsprozess notwendig, Modellgröße, Rechenkomplexität und Präzision auszubalancieren. Übliche Quantisierungsmethoden umfassen Festkommaquantisierung, Gleitkommaquantisierung usw. Sie können die geeignete Quantisierungsstrategie entsprechend dem spezifischen Szenario und Bedarf auswählen.

Wir hoffen, GenAI-Modelle auf Edge-Geräte zu bringen und mehr Geräte in GenAI-Szenarien zu integrieren, wie Mobilgeräte, AI PC/Copilot+PC und traditionelle IoT-Geräte. Durch das quantisierte Modell können wir es je nach Gerät auf verschiedene Edge-Geräte bereitstellen. In Kombination mit dem von Hardwareherstellern bereitgestellten Modellbeschleunigungs-Framework und dem Quantisierungsmodell können wir bessere SLM-Anwendungsszenarien aufbauen.

Im Quantisierungsszenario stehen verschiedene Präzisionsformate zur Verfügung (INT4, INT8, FP16, FP32). Nachfolgend eine Erklärung der häufig verwendeten Quantisierungspräzisionen

### **INT4**

INT4-Quantisierung ist eine radikale Quantisierungsmethode, die die Gewichte und Aktivierungswerte des Modells in 4-Bit-Ganzzahlen quantisiert. Durch den kleineren Darstellungsbereich und die niedrigere Präzision führt INT4-Quantisierung in der Regel zu einem größeren Präzisionsverlust. Im Vergleich zur INT8-Quantisierung kann INT4-Quantisierung jedoch den Speicherbedarf und die Rechenkomplexität des Modells weiter reduzieren. Es sei darauf hingewiesen, dass INT4-Quantisierung in praktischen Anwendungen relativ selten ist, da zu geringe Genauigkeit zu einer erheblichen Verschlechterung der Modellleistung führen kann. Außerdem unterstützen nicht alle Hardware INT4-Operationen, sodass die Hardwarekompatibilität bei der Wahl einer Quantisierungsmethode berücksichtigt werden muss.

### **INT8**

INT8-Quantisierung ist der Prozess, die Gewichte und Aktivierungen eines Modells von Gleitkommazahlen in 8-Bit-Ganzzahlen umzuwandeln. Obwohl der Zahlenbereich, den INT8-Ganzzahlen darstellen, kleiner und weniger präzise ist, können Speicherung und Rechenaufwand erheblich reduziert werden. Bei der INT8-Quantisierung durchlaufen die Gewichte und Aktivierungswerte des Modells einen Quantisierungsprozess, einschließlich Skalierung und Offset, um die ursprünglichen Gleitkommainformationen so weit wie möglich zu erhalten. Während der Inferenz werden diese quantisierten Werte wieder in Gleitkommazahlen zurückkonvertiert, um Berechnungen durchzuführen, und anschließend für den nächsten Schritt wieder in INT8 quantisiert. Diese Methode kann in den meisten Anwendungen eine ausreichende Genauigkeit bei hoher Rechenleistung bieten.

### **FP16**

Das FP16-Format, also 16-Bit-Gleitkommazahlen (float16), reduziert den Speicherbedarf im Vergleich zu 32-Bit-Gleitkommazahlen (float32) um die Hälfte, was in groß angelegten Deep-Learning-Anwendungen erhebliche Vorteile bringt. Das FP16-Format ermöglicht das Laden größerer Modelle oder die Verarbeitung größerer Datenmengen innerhalb derselben GPU-Speicherbegrenzungen. Da moderne GPU-Hardware weiterhin FP16-Operationen unterstützt, kann die Verwendung des FP16-Formats auch Verbesserungen in der Rechengeschwindigkeit bringen. Allerdings hat das FP16-Format auch seine inhärenten Nachteile, nämlich eine geringere Präzision, die in einigen Fällen zu numerischer Instabilität oder Präzisionsverlust führen kann.

### **FP32**

Das FP32-Format bietet höhere Präzision und kann ein breites Spektrum an Werten genau darstellen. In Szenarien, in denen komplexe mathematische Operationen ausgeführt werden oder hochpräzise Ergebnisse erforderlich sind, wird das FP32-Format bevorzugt. Hohe Genauigkeit bedeutet jedoch auch größeren Speicherverbrauch und längere Berechnungszeiten. Für groß angelegte Deep-Learning-Modelle, insbesondere bei vielen Modellparametern und großen Datenmengen, kann das FP32-Format zu unzureichendem GPU-Speicher oder einer Verringerung der Inferenzgeschwindigkeit führen.

Auf Mobilgeräten oder IoT-Geräten können wir Phi-3.x-Modelle in INT4 konvertieren, während AI PC / Copilot PC höhere Präzisionen wie INT8, FP16, FP 32 verwenden können.

Derzeit haben verschiedene Hardwarehersteller unterschiedliche Frameworks zur Unterstützung generativer Modelle, wie Intels OpenVINO, Qualcomms QNN, Apples MLX und Nvidias CUDA, die in Kombination mit Modellquantisierung eine lokale Bereitstellung ermöglichen.

In technologischer Hinsicht haben wir nach der Quantisierung verschiedene Formatunterstützungen, wie PyTorch / TensorFlow-Format, GGUF und ONNX. Ich habe einen Formatvergleich und Anwendungsszenarien zwischen GGUF und ONNX durchgeführt. Hier empfehle ich das ONNX-Quantisierungsformat, das eine gute Unterstützung vom Modellframework bis zur Hardware bietet. In diesem Kapitel konzentrieren wir uns auf ONNX Runtime für GenAI, OpenVINO und Apple MLX, um Modellquantisierung durchzuführen (wenn Sie einen besseren Weg haben, können Sie uns diesen auch durch Einreichen eines PR mitteilen)

**Dieses Kapitel enthält**

1. [Quantisierung von Phi-3.5 / 4 mit llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Quantisierung von Phi-3.5 / 4 mit Generative AI extensions für onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Quantisierung von Phi-3.5 / 4 mit Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Quantisierung von Phi-3.5 / 4 mit dem Apple MLX Framework](./UsingAppleMLXQuantifyingPhi.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Haftungsausschluss:
Dieses Dokument wurde mithilfe des KI-Übersetzungsdienstes [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprache ist als maßgebliche Quelle zu betrachten. Bei wichtigen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Für Missverständnisse oder Fehlinterpretationen, die sich aus der Verwendung dieser Übersetzung ergeben, übernehmen wir keine Haftung.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->