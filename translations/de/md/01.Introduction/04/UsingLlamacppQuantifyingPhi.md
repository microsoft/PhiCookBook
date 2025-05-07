<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "462bddc47427d8785f3c9fd817b346fe",
  "translation_date": "2025-05-07T10:47:16+00:00",
  "source_file": "md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md",
  "language_code": "de"
}
-->
# **Quantisierung der Phi-Familie mit llama.cpp**

## **Was ist llama.cpp**

llama.cpp ist eine Open-Source-Softwarebibliothek, die hauptsächlich in C++ geschrieben ist und Inferenz auf verschiedenen Large Language Models (LLMs) wie Llama durchführt. Das Hauptziel ist es, eine erstklassige Leistung bei der LLM-Inferenz auf einer Vielzahl von Hardware mit minimalem Aufwand zu bieten. Zusätzlich gibt es Python-Bindings für diese Bibliothek, die eine hochentwickelte API für Textvervollständigung und einen OpenAI-kompatiblen Webserver bereitstellen.

Das Hauptziel von llama.cpp ist es, LLM-Inferenz mit minimaler Einrichtung und erstklassiger Leistung auf unterschiedlichster Hardware – lokal und in der Cloud – zu ermöglichen.

- Reine C/C++-Implementierung ohne Abhängigkeiten
- Apple Silicon wird als erstklassige Plattform unterstützt – optimiert durch ARM NEON, Accelerate und Metal Frameworks
- AVX, AVX2 und AVX512 Unterstützung für x86-Architekturen
- 1,5-Bit-, 2-Bit-, 3-Bit-, 4-Bit-, 5-Bit-, 6-Bit- und 8-Bit-Ganzzahlquantisierung für schnellere Inferenz und geringeren Speicherverbrauch
- Eigene CUDA-Kernel zur Ausführung von LLMs auf NVIDIA-GPUs (Unterstützung für AMD-GPUs über HIP)
- Vulkan- und SYCL-Backend-Unterstützung
- CPU+GPU-Hybridinferenz zur teilweisen Beschleunigung von Modellen, die größer als die gesamte VRAM-Kapazität sind

## **Quantisierung von Phi-3.5 mit llama.cpp**

Das Modell Phi-3.5-Instruct kann mit llama.cpp quantisiert werden, Phi-3.5-Vision und Phi-3.5-MoE werden jedoch noch nicht unterstützt. Das von llama.cpp konvertierte Format ist gguf, welches auch das am weitesten verbreitete Quantisierungsformat ist.

Es gibt eine große Anzahl quantisierter GGUF-Modelle auf Hugging Face. AI Foundry, Ollama und LlamaEdge basieren auf llama.cpp, daher werden GGUF-Modelle häufig verwendet.

### **Was ist GGUF**

GGUF ist ein binäres Format, das für schnelles Laden und Speichern von Modellen optimiert ist und somit besonders effizient für Inferenzzwecke ist. GGUF ist für die Verwendung mit GGML und anderen Ausführungsumgebungen konzipiert. GGUF wurde von @ggerganov entwickelt, der auch Entwickler von llama.cpp ist, einem beliebten C/C++-Framework für LLM-Inferenz. Modelle, die ursprünglich in Frameworks wie PyTorch entwickelt wurden, können in das GGUF-Format konvertiert werden, um sie mit diesen Engines zu verwenden.

### **ONNX vs GGUF**

ONNX ist ein traditionelles Format für maschinelles Lernen/tiefes Lernen, das in verschiedenen KI-Frameworks gut unterstützt wird und gute Einsatzmöglichkeiten auf Edge-Geräten bietet. GGUF hingegen basiert auf llama.cpp und kann als Produkt der GenAI-Ära betrachtet werden. Beide Formate haben ähnliche Anwendungsbereiche. Wenn Sie bessere Leistung auf eingebetteter Hardware und Anwendungsebene wünschen, könnte ONNX die bessere Wahl sein. Wenn Sie das derivative Framework und die Technologie von llama.cpp nutzen, ist GGUF möglicherweise besser geeignet.

### **Quantisierung von Phi-3.5-Instruct mit llama.cpp**

**1. Umgebung konfigurieren**


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```


**2. Quantisierung**

Phi-3.5-Instruct mit llama.cpp in FP16 GGUF konvertieren


```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```

Phi-3.5 in INT4 quantisieren


```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```


**3. Testen**

llama-cpp-python installieren


```bash

pip install llama-cpp-python -U

```

***Hinweis*** 

Wenn Sie Apple Silicon verwenden, installieren Sie llama-cpp-python bitte wie folgt


```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

Testen


```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```



## **Ressourcen**

1. Mehr über llama.cpp erfahren [https://github.com/ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)  
2. Mehr über onnxruntime erfahren [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)  
3. Mehr über GGUF erfahren [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

**Haftungsausschluss**:  
Dieses Dokument wurde mithilfe des KI-Übersetzungsdienstes [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir auf Genauigkeit achten, bitten wir zu beachten, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ausgangssprache gilt als maßgebliche Quelle. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die durch die Nutzung dieser Übersetzung entstehen.