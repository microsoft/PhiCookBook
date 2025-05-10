<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1ff728038c4f554b660a36b76cbdd6e",
  "translation_date": "2025-05-09T12:34:42+00:00",
  "source_file": "md/01.Introduction/03/overview.md",
  "language_code": "sl"
}
-->
Phi-3-mini sambandha me, inference ka matlab hai model ka istemal karke input data ke aadhaar par prediction karna ya output generate karna. Main aapko Phi-3-mini aur uski inference kshamtaon ke baare me adhik jankari deta hoon.

Phi-3-mini Microsoft ke dwara release ki gayi Phi-3 series ka hissa hai. Ye models Small Language Models (SLMs) ke liye naye standards set karne ke liye design kiye gaye hain.

Yahaan kuch mukhya baatein hain Phi-3-mini aur uski inference kshamtaon ke baare me:

## **Phi-3-mini Overview:**
- Phi-3-mini ke paas 3.8 billion parameters hain.
- Ye sirf paramparagat computing devices par hi nahi, balki edge devices jaise mobile aur IoT devices par bhi chal sakta hai.
- Phi-3-mini ke release se vyakti aur sansthaen alag-alag hardware devices par SLMs ko deploy kar sakti hain, khaaskar resource-sankuchit environments me.
- Ye kai model formats ko cover karta hai, jinme paramparagat PyTorch format, quantized gguf format, aur ONNX-based quantized version shamil hain.

## **Accessing Phi-3-mini:**
Phi-3-mini tak pahunchne ke liye, aap [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) ka upyog kar sakte hain Copilot application me. Semantic Kernel aam taur par Azure OpenAI Service, Hugging Face ke open-source models, aur local models ke saath compatible hai.  
Aap quantized models ko call karne ke liye [Ollama](https://ollama.com) ya [LlamaEdge](https://llamaedge.com) ka bhi istemal kar sakte hain. Ollama vyakti gat users ko alag-alag quantized models call karne ki suvidha deta hai, jabki LlamaEdge GGUF models ke liye cross-platform uplabdhata pradan karta hai.

## **Quantized Models:**
Kai users local inference ke liye quantized models ka istemal karna pasand karte hain. Udaharan ke liye, aap seedha Ollama run Phi-3 kar sakte hain ya offline Modelfile ke madhyam se ise configure kar sakte hain. Modelfile me GGUF file path aur prompt format specify kiya jata hai.

## **Generative AI Possibilities:**
Phi-3-mini jaise SLMs ke saath milkar generative AI ke naye avsar khulte hain. Inference sirf pehla kadam hai; ye models resource-sankuchit, latency-bound, aur cost-sankuchit paristhitiyon me anek karyo ke liye upyog kiye ja sakte hain.

## **Unlocking Generative AI with Phi-3-mini: A Guide to Inference and Deployment**  
Semantic Kernel, Ollama/LlamaEdge, aur ONNX Runtime ka upyog karke Phi-3-mini models ko access aur infer karna seekhein, aur alag-alag application scenarios me generative AI ke sambhavnayon ko explore karein.

**Features**  
Inference phi3-mini model me:

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)  
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)  
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)  
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)  
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)  

Saaransh ke roop me, Phi-3-mini developers ko alag-alag model formats ko explore karne aur generative AI ko vivid application scenarios me istemal karne ki suvidha pradan karta hai.

**Opozorilo**:  
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za ključne informacije priporočamo strokovni človeški prevod. Nismo odgovorni za morebitne nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.