# **Quantifizierung der Phi-Familie**

Modellquantisierung bezieht sich auf den Prozess, die Parameter (wie Gewichte und Aktivierungswerte) in einem neuronalen Netzmodell von einem großen Wertebereich (in der Regel ein kontinuierlicher Wertebereich) auf einen kleineren endlichen Wertebereich abzubilden. Diese Technologie kann die Größe und die Rechenkomplexität des Modells reduzieren und die Betriebseffizienz des Modells in ressourcenbeschränkten Umgebungen wie Mobilgeräten oder eingebetteten Systemen verbessern. Die Modellquantisierung erreicht Kompression, indem die Präzision der Parameter verringert wird, führt aber auch zu einem gewissen Genauigkeitsverlust. Daher ist es im Quantisierungsprozess notwendig, Größe, Rechenkomplexität und Präzision des Modells auszubalancieren. Übliche Quantisierungsmethoden sind Festkommquantisierung, Fließkommquantisierung usw. Je nach Szenario und Bedarf kann die passende Quantisierungsstrategie ausgewählt werden.

Wir wollen GenAI-Modelle auf Edge-Geräten einsetzen und mehr Geräte in GenAI-Szenarien einbinden, wie Mobilgeräte, AI-PC/Copilot+PC und traditionelle IoT-Geräte. Durch das quantisierte Modell können wir dieses je nach Gerätetyp auf verschiedene Edge-Geräte ausrollen. In Kombination mit dem von Hardwareherstellern bereitgestellten Modellbeschleunigungs-Framework und dem quantisierten Modell können wir bessere SLM-Anwendungsszenarien aufbauen.

Im Quantisierungsszenario gibt es verschiedene Genauigkeiten (INT4, INT8, FP16, FP32). Nachfolgend eine Erklärung der häufig verwendeten Quantisierungspräzisionen.

### **INT4**

INT4-Quantisierung ist eine radikale Quantisierungsmethode, die die Gewichte und Aktivierungswerte des Modells in 4-Bit-Ganzzahlen quantisiert. INT4-Quantisierung führt aufgrund des kleineren Darstellungsbereichs und der niedrigeren Präzision meist zu einem größeren Genauigkeitsverlust. Allerdings reduziert INT4-Quantisierung im Vergleich zu INT8 die Speicheranforderungen und die Rechenkomplexität des Modells weiter. Es sei jedoch darauf hingewiesen, dass INT4-Quantisierung in der Praxis relativ selten ist, da die zu geringe Genauigkeit die Modellleistung wesentlich verschlechtern kann. Zudem unterstützen nicht alle Hardware INT4-Operationen, weshalb die Hardwarekompatibilität bei der Wahl der Quantisierungsmethode berücksichtigt werden muss.

### **INT8**

INT8-Quantisierung ist der Prozess, die Gewichte und Aktivierungen eines Modells von Fließkommazahlen auf 8-Bit-Ganzzahlen zu konvertieren. Obwohl der durch INT8-Ganzzahlen repräsentierte Wertebereich kleiner und weniger präzise ist, lässt sich der Speicher- und Rechenbedarf erheblich reduzieren. Bei der INT8-Quantisierung durchlaufen die Gewichte und Aktivierungswerte des Modells einen Quantisierungsprozess, der Skalierung und Offset umfasst, um die ursprünglichen Fließkommainformationen so gut wie möglich zu erhalten. Während der Inferenz werden diese quantisierten Werte zurück in Fließkommazahlen dequantisiert, um Berechnungen durchzuführen, und dann für den nächsten Schritt wieder in INT8 quantisiert. Diese Methode bietet in den meisten Anwendungen ausreichend Genauigkeit bei gleichzeitig hoher Recheneffizienz.

### **FP16**

Das FP16-Format, also 16-Bit-Fließkommazahlen (float16), reduziert den Speicherbedarf im Vergleich zu 32-Bit-Fließkommazahlen (float32) um die Hälfte, was große Vorteile bei groß angelegten Deep-Learning-Anwendungen hat. Das FP16-Format ermöglicht es, größere Modelle zu laden oder mehr Daten innerhalb derselben GPU-Speicherbegrenzungen zu verarbeiten. Da moderne GPU-Hardware FP16-Operationen zunehmend unterstützt, kann die Verwendung des FP16-Formats zudem Verbesserungen bei der Rechengeschwindigkeit bringen. Allerdings besitzt das FP16-Format auch inhärente Nachteile, nämlich eine geringere Präzision, die in manchen Fällen zu numerischer Instabilität oder Genauigkeitsverlust führen kann.

### **FP32**

Das FP32-Format bietet höhere Präzision und kann einen breiten Wertebereich genau darstellen. In Szenarien mit komplexen mathematischen Operationen oder wenn hochpräzise Ergebnisse erforderlich sind, wird das FP32-Format bevorzugt. Hohe Genauigkeit bedeutet jedoch auch höheren Speicherverbrauch und längere Rechenzeit. Für groß angelegte Deep-Learning-Modelle, insbesondere mit vielen Modellparametern und großen Datenmengen, kann das FP32-Format zu unzureichendem GPU-Speicher oder einer Verlangsamung der Inferenzgeschwindigkeit führen.

Auf Mobilgeräten oder IoT-Geräten können wir Phi-3.x-Modelle auf INT4 umwandeln, während AI-PCs/Copilot-PCs höhere Genauigkeiten wie INT8, FP16 oder FP32 verwenden können.

Derzeit bieten verschiedene Hardwarehersteller verschiedene Frameworks zur Unterstützung generativer Modelle an, wie Intels OpenVINO, Qualcomms QNN, Apples MLX sowie Nvidias CUDA, kombiniert mit Modellquantisierung für die lokale Bereitstellung.

Technisch bieten wir nach der Quantisierung verschiedene Formatunterstützungen an, etwa PyTorch / TensorFlow-Format, GGUF und ONNX. Ich habe einen Formatvergleich und Anwendungsszenarien zwischen GGUF und ONNX durchgeführt. Hier empfehle ich das ONNX-Quantisierungsformat, das eine gute Unterstützung vom Modellframework bis zur Hardware bietet. In diesem Kapitel konzentrieren wir uns auf ONNX Runtime für GenAI, OpenVINO und Apple MLX zur Modellquantisierung (wenn Sie einen besseren Weg haben, können Sie uns gern mit einer PR unterstützen).

**Dieses Kapitel beinhaltet**

1. [Quantifizierung von Phi-3.5 / 4 mit llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Quantifizierung von Phi-3.5 / 4 mit Generative AI-Erweiterungen für onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Quantifizierung von Phi-3.5 / 4 mit Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Quantifizierung von Phi-3.5 / 4 mit Apple MLX Framework](./UsingAppleMLXQuantifyingPhi.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:  
Dieses Dokument wurde mithilfe des KI-Übersetzungsdienstes [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir um Genauigkeit bemüht sind, kann es bei automatisierten Übersetzungen zu Fehlern oder Ungenauigkeiten kommen. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die durch die Nutzung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->