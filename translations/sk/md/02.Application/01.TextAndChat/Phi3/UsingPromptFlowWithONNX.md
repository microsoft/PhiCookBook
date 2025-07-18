<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "92e7dac1e5af0dd7c94170fdaf6860fe",
  "translation_date": "2025-07-17T03:03:25+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md",
  "language_code": "sk"
}
-->
# Použitie Windows GPU na vytvorenie riešenia Prompt flow s Phi-3.5-Instruct ONNX

Nasledujúci dokument je príklad, ako používať PromptFlow s ONNX (Open Neural Network Exchange) na vývoj AI aplikácií založených na modeloch Phi-3.

PromptFlow je súbor vývojových nástrojov navrhnutých na zjednodušenie celého vývojového cyklu AI aplikácií založených na LLM (Large Language Model), od nápadu a prototypovania až po testovanie a hodnotenie.

Integráciou PromptFlow s ONNX môžu vývojári:

- Optimalizovať výkon modelu: Využiť ONNX pre efektívne inferovanie a nasadenie modelu.
- Zjednodušiť vývoj: Použiť PromptFlow na správu pracovného toku a automatizáciu opakujúcich sa úloh.
- Zlepšiť spoluprácu: Uľahčiť spoluprácu medzi členmi tímu poskytnutím jednotného vývojového prostredia.

**Prompt flow** je súbor vývojových nástrojov navrhnutých na zjednodušenie celého vývojového cyklu AI aplikácií založených na LLM, od nápadu, prototypovania, testovania, hodnotenia až po nasadenie do produkcie a monitorovanie. Uľahčuje prompt engineering a umožňuje vytvárať LLM aplikácie s kvalitou vhodnou pre produkciu.

Prompt flow sa dokáže pripojiť k OpenAI, Azure OpenAI Service a prispôsobiteľným modelom (Huggingface, lokálne LLM/SLM). Plánujeme nasadiť kvantizovaný ONNX model Phi-3.5 do lokálnych aplikácií. Prompt flow nám môže pomôcť lepšie naplánovať naše podnikanie a dokončiť lokálne riešenia založené na Phi-3.5. V tomto príklade skombinujeme ONNX Runtime GenAI knižnicu na dokončenie riešenia Prompt flow založeného na Windows GPU.

## **Inštalácia**

### **ONNX Runtime GenAI pre Windows GPU**

Prečítajte si tento návod na nastavenie ONNX Runtime GenAI pre Windows GPU [kliknite sem](./ORTWindowGPUGuideline.md)

### **Nastavenie Prompt flow vo VSCode**

1. Nainštalujte rozšírenie Prompt flow pre VS Code

![pfvscode](../../../../../../translated_images/pfvscode.eff93dfc66a42cbef699fc16fa48f3ed3a23361875a3362037d026896395a00d.sk.png)

2. Po inštalácii rozšírenia Prompt flow vo VS Code kliknite na rozšírenie a vyberte **Installation dependencies**, podľa tohto návodu nainštalujte Prompt flow SDK do vášho prostredia

![pfsetup](../../../../../../translated_images/pfsetup.b46e93096f5a254f74e8b74ce2be7047ce963ef573d755ec897eb1b78cb9c954.sk.png)

3. Stiahnite si [Ukážkový kód](../../../../../../code/09.UpdateSamples/Aug/pf/onnx_inference_pf) a otvorte ho vo VS Code

![pfsample](../../../../../../translated_images/pfsample.8d89e70584ffe7c4dba182513e3148a989e552c3b8e4948567a6b806b5ae1845.sk.png)

4. Otvorte **flow.dag.yaml** a vyberte svoje Python prostredie

![pfdag](../../../../../../translated_images/pfdag.264a77f7366458ff850a76ae949226391ea382856d543ef9da4b92096aff7e4b.sk.png)

   Otvorte **chat_phi3_ort.py** a zmeňte umiestnenie vášho Phi-3.5-instruct ONNX modelu

![pfphi](../../../../../../translated_images/pfphi.72da81d74244b45fc78cdfeeb8c7fbd9e7cd610bf2f96814dbade6a4a2dfad7e.sk.png)

5. Spustite svoj prompt flow na testovanie

Otvorte **flow.dag.yaml** a kliknite na vizuálny editor

![pfv](../../../../../../translated_images/pfv.ba8a81f34b20f603cccee3fe91e94113792ed6f5af28f76ab08e1a0b3e77b33b.sk.png)

Po kliknutí spustite testovanie

![pfflow](../../../../../../translated_images/pfflow.4e1135a089b1ce1b6348b59edefdb6333e5729b54c8e57f9039b7f9463e68fbd.sk.png)

1. Môžete spustiť batch v termináli pre zobrazenie ďalších výsledkov


```bash

pf run create --file batch_run.yaml --stream --name 'Your eval qa name'    

```

Výsledky si môžete pozrieť vo vašom predvolenom prehliadači


![pfresult](../../../../../../translated_images/pfresult.c22c826f8062d7cbe871cff35db4a013dcfefc13fafe5da6710a8549a96a4ceb.sk.png)

**Zrieknutie sa zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.