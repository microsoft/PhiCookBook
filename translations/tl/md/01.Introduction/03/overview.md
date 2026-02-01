Sa konteksto ng Phi-3-mini, ang inference ay tumutukoy sa proseso ng paggamit ng modelo upang gumawa ng mga prediksyon o lumikha ng mga output base sa input na datos. Hayaan akong magbigay ng karagdagang detalye tungkol sa Phi-3-mini at ang kakayahan nito sa inference.

Ang Phi-3-mini ay bahagi ng Phi-3 series ng mga modelo na inilabas ng Microsoft. Ang mga modelong ito ay idinisenyo upang baguhin ang mga posibleng gawin gamit ang Small Language Models (SLMs).

Narito ang ilang mahahalagang punto tungkol sa Phi-3-mini at ang kakayahan nito sa inference:

## **Pangkalahatang-ideya ng Phi-3-mini:**
- Ang Phi-3-mini ay may sukat na 3.8 bilyong parameter.
- Maaari itong patakbuhin hindi lamang sa tradisyunal na mga computing device kundi pati na rin sa mga edge device tulad ng mga mobile device at IoT device.
- Ang paglabas ng Phi-3-mini ay nagbibigay-daan sa mga indibidwal at negosyo na mag-deploy ng SLMs sa iba't ibang hardware device, lalo na sa mga kapaligirang may limitadong resources.
- Sinasaklaw nito ang iba't ibang format ng modelo, kabilang ang tradisyunal na PyTorch format, ang quantized na bersyon ng gguf format, at ang ONNX-based na quantized na bersyon.

## **Pag-access sa Phi-3-mini:**
Para ma-access ang Phi-3-mini, maaari mong gamitin ang [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) sa isang Copilot application. Ang Semantic Kernel ay karaniwang compatible sa Azure OpenAI Service, open-source na mga modelo sa Hugging Face, at mga lokal na modelo.  
Maaari mo ring gamitin ang [Ollama](https://ollama.com) o [LlamaEdge](https://llamaedge.com) para tawagin ang mga quantized na modelo. Pinapayagan ng Ollama ang mga indibidwal na user na tawagin ang iba't ibang quantized na modelo, habang ang LlamaEdge ay nagbibigay ng cross-platform na availability para sa mga GGUF na modelo.

## **Mga Quantized na Modelo:**
Maraming gumagamit ang mas gusto ang paggamit ng quantized na mga modelo para sa lokal na inference. Halimbawa, maaari mong direktang patakbuhin ang Ollama run Phi-3 o i-configure ito offline gamit ang isang Modelfile. Ang Modelfile ay nagtatakda ng GGUF file path at ang prompt format.

## **Mga Posibilidad ng Generative AI:**
Ang pagsasama ng mga SLM tulad ng Phi-3-mini ay nagbubukas ng mga bagong posibilidad para sa generative AI. Ang inference ay unang hakbang lamang; ang mga modelong ito ay maaaring gamitin para sa iba't ibang gawain sa mga kapaligirang may limitadong resources, may latency na kailangang iwasan, at may mga limitasyon sa gastos.

## **Pagbubukas ng Generative AI gamit ang Phi-3-mini: Isang Gabay sa Inference at Deployment**  
Alamin kung paano gamitin ang Semantic Kernel, Ollama/LlamaEdge, at ONNX Runtime para ma-access at ma-infer ang mga Phi-3-mini na modelo, at tuklasin ang mga posibilidad ng generative AI sa iba't ibang senaryo ng aplikasyon.

**Mga Tampok**  
Inference ng phi3-mini na modelo sa:

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)  
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)  
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)  
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)  
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)  

Sa kabuuan, pinapayagan ng Phi-3-mini ang mga developer na tuklasin ang iba't ibang format ng modelo at gamitin ang generative AI sa iba't ibang senaryo ng aplikasyon.

**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.