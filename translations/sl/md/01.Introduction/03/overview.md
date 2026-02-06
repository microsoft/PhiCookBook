V kontekstu Phi-3-mini se inferenca nanaša na postopek uporabe modela za napovedovanje ali generiranje izhodov na podlagi vhodnih podatkov. Dovolite, da vam predstavim več podrobnosti o Phi-3-mini in njegovih zmogljivostih inferenc.

Phi-3-mini je del serije modelov Phi-3, ki jih je izdal Microsoft. Ti modeli so zasnovani tako, da preoblikujejo možnosti majhnih jezikovnih modelov (SLM).

Tukaj je nekaj ključnih točk o Phi-3-mini in njegovih zmogljivostih inferenc:

## **Pregled Phi-3-mini:**
- Phi-3-mini ima velikost parametrov 3,8 milijarde.
- Lahko teče ne le na tradicionalnih računalniških napravah, ampak tudi na edge napravah, kot so mobilne naprave in IoT naprave.
- Izdaja Phi-3-mini omogoča posameznikom in podjetjem, da namestijo SLM-je na različnih strojnih napravah, zlasti v okoljih z omejenimi viri.
- Podpira različne formate modelov, vključno s tradicionalnim PyTorch formatom, kvantizirano različico formata gguf in kvantizirano različico na osnovi ONNX.

## **Dostop do Phi-3-mini:**
Za dostop do Phi-3-mini lahko uporabite [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) v aplikaciji Copilot. Semantic Kernel je na splošno združljiv z Azure OpenAI Service, odprtokodnimi modeli na Hugging Face in lokalnimi modeli.  
Lahko uporabite tudi [Ollama](https://ollama.com) ali [LlamaEdge](https://llamaedge.com) za klic kvantiziranih modelov. Ollama omogoča posameznim uporabnikom klic različnih kvantiziranih modelov, medtem ko LlamaEdge zagotavlja večplatformno dostopnost za modele GGUF.

## **Kvantizirani modeli:**
Veliko uporabnikov raje uporablja kvantizirane modele za lokalno inferenco. Na primer, lahko neposredno zaženete Ollama run Phi-3 ali ga konfigurirate brez povezave z uporabo Modelfile. Modelfile določa pot do datoteke GGUF in format poziva.

## **Možnosti generativne umetne inteligence:**
Združevanje SLM-jev, kot je Phi-3-mini, odpira nove možnosti za generativno umetno inteligenco. Inferenca je le prvi korak; ti modeli se lahko uporabljajo za različne naloge v okoljih z omejenimi viri, omejitvami latence in stroškovnimi omejitvami.

## **Odklepanje generativne umetne inteligence s Phi-3-mini: Vodnik za inferenco in namestitev**  
Naučite se, kako uporabljati Semantic Kernel, Ollama/LlamaEdge in ONNX Runtime za dostop in inferenco modelov Phi-3-mini ter raziskujte možnosti generativne umetne inteligence v različnih aplikativnih scenarijih.

**Funkcije**  
Inferenca modela phi3-mini v:

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)  
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)  
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)  
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)  
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)  

Za povzetek, Phi-3-mini razvijalcem omogoča raziskovanje različnih formatov modelov in izkoriščanje generativne umetne inteligence v različnih aplikativnih scenarijih.

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za pomembne informacije priporočamo strokovni človeški prevod. Za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.