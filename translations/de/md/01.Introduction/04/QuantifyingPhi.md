<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d658062de70b131ef4c0bff69b5fc70e",
  "translation_date": "2025-05-07T10:47:46+00:00",
  "source_file": "md/01.Introduction/04/QuantifyingPhi.md",
  "language_code": "de"
}
-->
# **Quantifizierung der Phi-Familie**

Modellquantisierung bezeichnet den Prozess, bei dem die Parameter (wie Gewichte und Aktivierungswerte) eines neuronalen Netzmodells von einem großen Wertebereich (meist ein kontinuierlicher Wertebereich) auf einen kleineren, endlichen Wertebereich abgebildet werden. Diese Technologie kann die Größe und die Rechenkomplexität des Modells reduzieren und die Betriebseffizienz in ressourcenbeschränkten Umgebungen wie Mobilgeräten oder eingebetteten Systemen verbessern. Modellquantisierung erreicht Kompression durch Verringerung der Genauigkeit der Parameter, führt jedoch auch zu einem gewissen Genauigkeitsverlust. Daher muss im Quantisierungsprozess ein Gleichgewicht zwischen Modellgröße, Rechenkomplexität und Genauigkeit gefunden werden. Übliche Quantisierungsmethoden sind Fixed-Point-Quantisierung, Floating-Point-Quantisierung usw. Je nach spezifischem Szenario und Bedarf kann die passende Quantisierungsstrategie gewählt werden.

Wir möchten GenAI-Modelle auf Edge-Geräte bringen und so mehr Geräte für GenAI-Szenarien zugänglich machen, wie Mobilgeräte, AI PC/Copilot+PC und traditionelle IoT-Geräte. Durch das quantisierte Modell können wir es auf verschiedenen Edge-Geräten basierend auf deren Eigenschaften bereitstellen. In Kombination mit dem von Hardwareherstellern bereitgestellten Modellbeschleunigungs-Framework und Quantisierungsmodell können wir bessere SLM-Anwendungsszenarien schaffen.

Im Quantisierungsszenario gibt es verschiedene Genauigkeiten (INT4, INT8, FP16, FP32). Im Folgenden werden die gängigen Quantisierungsgenauigkeiten erläutert.

### **INT4**

INT4-Quantisierung ist eine sehr radikale Methode, bei der die Gewichte und Aktivierungswerte eines Modells in 4-Bit-Ganzzahlen quantisiert werden. INT4-Quantisierung führt aufgrund des kleineren Darstellungsbereichs und der geringeren Genauigkeit meist zu einem größeren Genauigkeitsverlust. Im Vergleich zur INT8-Quantisierung kann INT4 jedoch den Speicherbedarf und die Rechenkomplexität des Modells weiter reduzieren. Zu beachten ist, dass INT4-Quantisierung in der Praxis eher selten verwendet wird, da die zu geringe Genauigkeit die Modellleistung deutlich verschlechtern kann. Außerdem unterstützen nicht alle Hardwareplattformen INT4-Operationen, weshalb die Hardwarekompatibilität bei der Wahl der Quantisierungsmethode berücksichtigt werden muss.

### **INT8**

INT8-Quantisierung wandelt die Gewichte und Aktivierungen eines Modells von Fließkommazahlen in 8-Bit-Ganzzahlen um. Obwohl der darstellbare Zahlenbereich bei INT8 kleiner und weniger präzise ist, können Speicher- und Rechenanforderungen deutlich reduziert werden. Bei der INT8-Quantisierung durchlaufen Gewichte und Aktivierungswerte einen Quantisierungsprozess mit Skalierung und Offset, um die ursprünglichen Fließkommadaten möglichst gut zu erhalten. Während der Inferenz werden diese quantisierten Werte wieder in Fließkommazahlen dequantisiert, berechnet und anschließend erneut in INT8 quantisiert für den nächsten Schritt. Diese Methode bietet in den meisten Anwendungen ausreichend Genauigkeit bei gleichzeitig hoher Rechenleistung.

### **FP16**

Das FP16-Format, also 16-Bit-Fließkommazahlen (float16), reduziert den Speicherbedarf im Vergleich zu 32-Bit-Fließkommazahlen (float32) um die Hälfte, was besonders bei groß angelegten Deep-Learning-Anwendungen große Vorteile bietet. Das FP16-Format ermöglicht es, größere Modelle zu laden oder mehr Daten innerhalb desselben GPU-Speichers zu verarbeiten. Da moderne GPU-Hardware zunehmend FP16-Operationen unterstützt, kann die Nutzung von FP16 auch zu einer höheren Rechengeschwindigkeit führen. Allerdings hat das FP16-Format auch seine Nachteile, vor allem die geringere Genauigkeit, die in einigen Fällen zu numerischer Instabilität oder Präzisionsverlust führen kann.

### **FP32**

Das FP32-Format bietet eine höhere Genauigkeit und kann einen weiten Wertebereich präzise darstellen. In Szenarien, in denen komplexe mathematische Operationen durchgeführt werden oder hohe Präzision erforderlich ist, wird FP32 bevorzugt. Allerdings bedeutet die hohe Genauigkeit auch einen größeren Speicherbedarf und längere Berechnungszeiten. Bei groß angelegten Deep-Learning-Modellen mit vielen Parametern und großen Datenmengen kann FP32 zu unzureichendem GPU-Speicher oder einer geringeren Inferenzgeschwindigkeit führen.

Auf mobilen Geräten oder IoT-Geräten können wir Phi-3.x-Modelle auf INT4 konvertieren, während AI PC / Copilot PC höhere Genauigkeiten wie INT8, FP16 oder FP32 nutzen können.

Derzeit bieten verschiedene Hardwarehersteller unterschiedliche Frameworks zur Unterstützung generativer Modelle an, wie Intels OpenVINO, Qualcomms QNN, Apples MLX und Nvidias CUDA, die zusammen mit Modellquantisierung die lokale Bereitstellung ermöglichen.

Technologisch gesehen unterstützen wir nach der Quantisierung verschiedene Formate wie PyTorch / Tensorflow, GGUF und ONNX. Ich habe einen Vergleich der Formate und Anwendungsszenarien zwischen GGUF und ONNX durchgeführt. Hier empfehle ich das ONNX-Quantisierungsformat, das von Modellframework bis Hardware gut unterstützt wird. In diesem Kapitel konzentrieren wir uns auf ONNX Runtime für GenAI, OpenVINO und Apple MLX zur Modellquantisierung (wenn Sie bessere Methoden haben, können Sie uns diese gerne per PR zukommen lassen).

**Dieses Kapitel enthält**

1. [Quantisierung von Phi-3.5 / 4 mit llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Quantisierung von Phi-3.5 / 4 mit Generative AI Extensions für onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Quantisierung von Phi-3.5 / 4 mit Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Quantisierung von Phi-3.5 / 4 mit Apple MLX Framework](./UsingAppleMLXQuantifyingPhi.md)

**Haftungsausschluss**:  
Dieses Dokument wurde mithilfe des KI-Übersetzungsdienstes [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache ist als maßgebliche Quelle zu betrachten. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.