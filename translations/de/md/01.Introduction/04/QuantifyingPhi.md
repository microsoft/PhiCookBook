<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d658062de70b131ef4c0bff69b5fc70e",
  "translation_date": "2025-03-27T08:18:47+00:00",
  "source_file": "md\\01.Introduction\\04\\QuantifyingPhi.md",
  "language_code": "de"
}
-->
# **Quantifizierung der Phi-Familie**

Die Modellquantisierung bezieht sich auf den Prozess, bei dem die Parameter (wie Gewichte und Aktivierungswerte) eines neuronalen Netzwerks von einem großen Wertebereich (normalerweise ein kontinuierlicher Wertebereich) auf einen kleineren, endlichen Wertebereich abgebildet werden. Diese Technologie kann die Größe und die rechnerische Komplexität des Modells reduzieren und die Betriebseffizienz des Modells in ressourcenbeschränkten Umgebungen wie Mobilgeräten oder eingebetteten Systemen verbessern. Die Modellquantisierung erreicht die Kompression durch die Reduzierung der Parameterpräzision, führt jedoch auch zu einem gewissen Präzisionsverlust. Daher ist es während des Quantisierungsprozesses notwendig, die Modellgröße, die rechnerische Komplexität und die Präzision in Balance zu halten. Häufige Quantisierungsmethoden umfassen Festpunktquantisierung, Gleitpunktquantisierung usw. Je nach spezifischem Szenario und Bedarf kann die geeignete Quantisierungsstrategie gewählt werden.

Wir möchten das GenAI-Modell auf Edge-Geräten bereitstellen und mehr Geräte in GenAI-Szenarien einbinden, wie Mobilgeräte, AI-PCs/Copilot+PCs und traditionelle IoT-Geräte. Durch den quantisierten Modellansatz können wir es auf verschiedene Edge-Geräte basierend auf deren spezifischen Eigenschaften bereitstellen. In Kombination mit den von Hardwareherstellern bereitgestellten Beschleunigungs- und Quantisierungsmodellen können wir bessere SLM-Anwendungsszenarien entwickeln.

Im Quantisierungskontext stehen uns unterschiedliche Präzisionen zur Verfügung (INT4, INT8, FP16, FP32). Im Folgenden werden die gängigsten Quantisierungspräzisionen erklärt.

### **INT4**

Die INT4-Quantisierung ist eine radikale Methode, bei der die Gewichte und Aktivierungswerte des Modells in 4-Bit-Ganzzahlen quantisiert werden. Aufgrund des kleineren Darstellungsbereichs und der geringeren Präzision führt die INT4-Quantisierung in der Regel zu einem größeren Präzisionsverlust. Im Vergleich zur INT8-Quantisierung kann die INT4-Quantisierung jedoch die Speicheranforderungen und die rechnerische Komplexität des Modells weiter reduzieren. Es ist jedoch zu beachten, dass die INT4-Quantisierung in der Praxis relativ selten verwendet wird, da die extrem niedrige Genauigkeit zu erheblichen Leistungseinbußen des Modells führen kann. Außerdem unterstützen nicht alle Hardwareplattformen INT4-Operationen, daher muss die Hardwarekompatibilität bei der Wahl der Quantisierungsmethode berücksichtigt werden.

### **INT8**

Die INT8-Quantisierung beschreibt den Prozess, bei dem die Gewichte und Aktivierungen eines Modells von Gleitkommazahlen in 8-Bit-Ganzzahlen umgewandelt werden. Obwohl der durch INT8-Ganzzahlen dargestellte Wertebereich kleiner und weniger präzise ist, können dadurch die Speicher- und Rechenanforderungen erheblich reduziert werden. Bei der INT8-Quantisierung durchlaufen die Gewichte und Aktivierungswerte des Modells einen Quantisierungsprozess, der Skalierung und Offset umfasst, um die ursprünglichen Gleitkommainformationen so weit wie möglich zu bewahren. Während der Inferenz werden diese quantisierten Werte zurück in Gleitkommazahlen dequantisiert, berechnet und anschließend wieder in INT8 quantisiert, um den nächsten Schritt durchzuführen. Diese Methode bietet in den meisten Anwendungen ausreichend Genauigkeit bei gleichzeitig hoher Recheneffizienz.

### **FP16**

Das FP16-Format, also 16-Bit-Gleitkommazahlen (float16), reduziert den Speicherbedarf im Vergleich zu 32-Bit-Gleitkommazahlen (float32) um die Hälfte, was in groß angelegten Deep-Learning-Anwendungen erhebliche Vorteile bietet. Das FP16-Format ermöglicht das Laden größerer Modelle oder die Verarbeitung größerer Datenmengen innerhalb der gleichen GPU-Speichergrenzen. Da moderne GPU-Hardware zunehmend FP16-Operationen unterstützt, kann die Verwendung des FP16-Formats auch zu einer Verbesserung der Rechengeschwindigkeit führen. Allerdings hat das FP16-Format auch seine Nachteile, insbesondere die geringere Präzision, die in einigen Fällen zu numerischer Instabilität oder Präzisionsverlust führen kann.

### **FP32**

Das FP32-Format bietet eine höhere Präzision und kann einen breiten Wertebereich genau darstellen. In Szenarien, in denen komplexe mathematische Operationen durchgeführt werden oder hochpräzise Ergebnisse erforderlich sind, wird das FP32-Format bevorzugt. Höhere Präzision bedeutet jedoch auch einen höheren Speicherbedarf und längere Berechnungszeiten. Für groß angelegte Deep-Learning-Modelle, insbesondere wenn viele Modellparameter und eine große Datenmenge vorliegen, kann das FP32-Format zu unzureichendem GPU-Speicher oder einer verringerten Inferenzgeschwindigkeit führen.

Auf Mobilgeräten oder IoT-Geräten können wir Phi-3.x-Modelle in INT4 konvertieren, während AI-PCs/Copilot-PCs eine höhere Präzision wie INT8, FP16 oder FP32 verwenden können.

Derzeit bieten verschiedene Hardwarehersteller unterschiedliche Frameworks zur Unterstützung generativer Modelle an, wie Intels OpenVINO, Qualcomms QNN, Apples MLX und Nvidias CUDA. In Kombination mit Modellquantisierung können diese Frameworks für lokale Bereitstellungen genutzt werden.

Technisch gesehen haben wir nach der Quantisierung unterschiedliche Formatunterstützungen, wie PyTorch-/Tensorflow-Format, GGUF und ONNX. Ich habe einen Vergleich zwischen GGUF und ONNX sowie deren Anwendungsszenarien durchgeführt. Hier empfehle ich das ONNX-Quantisierungsformat, das von Modellframeworks bis hin zur Hardware gut unterstützt wird. In diesem Kapitel konzentrieren wir uns auf die Modellquantisierung mit ONNX Runtime für GenAI, OpenVINO und Apple MLX (wenn ihr eine bessere Methode habt, könnt ihr sie uns gerne per PR vorschlagen).

**Dieses Kapitel beinhaltet**

1. [Quantisierung von Phi-3.5/4 mit llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Quantisierung von Phi-3.5/4 mit Generative AI Extensions für onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Quantisierung von Phi-3.5/4 mit Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Quantisierung von Phi-3.5/4 mit dem Apple MLX Framework](./UsingAppleMLXQuantifyingPhi.md)

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.