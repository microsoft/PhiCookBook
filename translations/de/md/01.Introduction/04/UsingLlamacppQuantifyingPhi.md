<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e5bb9190ef9d149d28037a768c6b62b2",
  "translation_date": "2025-03-27T08:37:30+00:00",
  "source_file": "md\\01.Introduction\\04\\UsingLlamacppQuantifyingPhi.md",
  "language_code": "de"
}
-->
# **Quantisierung der Phi-Familie mit llama.cpp**

## **Was ist llama.cpp**

llama.cpp ist eine Open-Source-Softwarebibliothek, die hauptsächlich in C++ geschrieben ist und Inferenz auf verschiedenen großen Sprachmodellen (LLMs) wie Llama durchführt. Ihr Hauptziel ist es, eine erstklassige Leistung für LLM-Inferenz auf einer breiten Palette von Hardware mit minimaler Einrichtung zu bieten. Zusätzlich gibt es Python-Bindings für diese Bibliothek, die eine High-Level-API für Textvervollständigung und einen OpenAI-kompatiblen Webserver bieten.

Das Hauptziel von llama.cpp ist es, LLM-Inferenz mit minimaler Einrichtung und erstklassiger Leistung auf einer Vielzahl von Hardware zu ermöglichen – lokal und in der Cloud.

- Reine C/C++-Implementierung ohne Abhängigkeiten
- Apple Silicon wird als erstklassige Plattform behandelt – optimiert durch ARM NEON, Accelerate und Metal-Frameworks
- AVX-, AVX2- und AVX512-Unterstützung für x86-Architekturen
- 1,5-Bit-, 2-Bit-, 3-Bit-, 4-Bit-, 5-Bit-, 6-Bit- und 8-Bit-Integer-Quantisierung für schnellere Inferenz und reduzierten Speicherverbrauch
- Benutzerdefinierte CUDA-Kernel für die Ausführung von LLMs auf NVIDIA-GPUs (Unterstützung für AMD-GPUs über HIP)
- Vulkan- und SYCL-Backend-Unterstützung
- CPU+GPU-Hybrid-Inferenz zur teilweisen Beschleunigung von Modellen, die größer als die Gesamtkapazität des VRAM sind

## **Quantisierung von Phi-3.5 mit llama.cpp**

Das Modell Phi-3.5-Instruct kann mit llama.cpp quantisiert werden, aber Phi-3.5-Vision und Phi-3.5-MoE werden noch nicht unterstützt. Das von llama.cpp konvertierte Format ist gguf, welches auch das am weitesten verbreitete Quantisierungsformat ist.

Es gibt eine große Anzahl von quantisierten Modellen im GGUF-Format auf Hugging Face. AI Foundry, Ollama und LlamaEdge basieren auf llama.cpp, daher werden GGUF-Modelle ebenfalls häufig verwendet.

### **Was ist GGUF**

GGUF ist ein binäres Format, das für schnelles Laden und Speichern von Modellen optimiert ist, wodurch es sich hervorragend für Inferenzzwecke eignet. GGUF ist für die Verwendung mit GGML und anderen Ausführungs-Engines konzipiert. GGUF wurde von @ggerganov entwickelt, der auch der Entwickler von llama.cpp ist, einem beliebten C/C++ LLM-Inferenz-Framework. Modelle, die ursprünglich in Frameworks wie PyTorch entwickelt wurden, können in das GGUF-Format konvertiert werden, um mit diesen Engines verwendet zu werden.

### **ONNX vs GGUF**

ONNX ist ein traditionelles Format für maschinelles Lernen/Tiefes Lernen, das in verschiedenen KI-Frameworks gut unterstützt wird und gute Anwendungsszenarien auf Edge-Geräten bietet. GGUF hingegen basiert auf llama.cpp und kann als Produkt des GenAI-Zeitalters betrachtet werden. Beide Formate haben ähnliche Verwendungszwecke. Wenn Sie eine bessere Leistung auf eingebetteter Hardware und Anwendungsebenen wünschen, könnte ONNX die richtige Wahl sein. Wenn Sie das abgeleitete Framework und die Technologie von llama.cpp nutzen, könnte GGUF besser geeignet sein.

### **Quantisierung von Phi-3.5-Instruct mit llama.cpp**

**1. Konfiguration der Umgebung**

```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```

**2. Quantisierung**

Mit llama.cpp Phi-3.5-Instruct in FP16 GGUF konvertieren

```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```

Quantisierung von Phi-3.5 in INT4

```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```

**3. Testen**

Installieren Sie llama-cpp-python

```bash

pip install llama-cpp-python -U

```

***Hinweis***

Falls Sie Apple Silicon verwenden, installieren Sie llama-cpp-python folgendermaßen:

```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

Testen

```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```

## **Ressourcen**

1. Mehr über llama.cpp erfahren [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Mehr über GGUF erfahren [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

**Haftungsausschluss**:  
Dieses Dokument wurde mithilfe des KI-Übersetzungsdienstes [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.