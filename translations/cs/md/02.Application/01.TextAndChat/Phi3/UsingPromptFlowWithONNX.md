# Použití Windows GPU k vytvoření řešení Prompt flow s Phi-3.5-Instruct ONNX 

Následující dokument je příkladem, jak používat PromptFlow s ONNX (Open Neural Network Exchange) pro vývoj AI aplikací založených na modelech Phi-3.

PromptFlow je sada vývojářských nástrojů navržených ke zjednodušení kompletního vývojového cyklu AI aplikací založených na LLM (Large Language Model), od nápadu a prototypování po testování a hodnocení.

Integrací PromptFlow s ONNX mohou vývojáři:

- Optimalizovat výkon modelu: Využít ONNX pro efektivní inferenci a nasazení modelu.
- Zjednodušit vývoj: Používat PromptFlow pro správu workflow a automatizaci opakujících se úkolů.
- Zlepšit spolupráci: Facilituje lepší spolupráci mezi členy týmu díky sjednocenému vývojovému prostředí.

**Prompt flow** je sada vývojářských nástrojů určených ke zefektivnění kompletního vývojového cyklu AI aplikací založených na LLM, od nápadu, prototypování, testování, hodnocení až po produkční nasazení a monitorování. Usnadňuje prompt engineering a umožňuje vytvářet aplikace LLM s produkční kvalitou.

Prompt flow může pracovat s OpenAI, Azure OpenAI Service a přizpůsobitelnými modely (Huggingface, lokální LLM/SLM). Doufáme, že nasadíme kvantovaný ONNX model Phi-3.5 do lokálních aplikací. Prompt flow nám může pomoci lépe plánovat byznys a dokončit lokální řešení založená na Phi-3.5. V tomto příkladu spojíme ONNX Runtime GenAI knihovnu k dokončení Prompt flow řešení založeného na Windows GPU.

## **Instalace**

### **ONNX Runtime GenAI pro Windows GPU**

Přečtěte si tento návod ke konfiguraci ONNX Runtime GenAI pro Windows GPU [klikněte zde](./ORTWindowGPUGuideline.md)

### **Nastavení Prompt flow ve VSCode**

1. Nainstalujte rozšíření Prompt flow pro VS Code

![pfvscode](../../../../../../translated_images/cs/pfvscode.eff93dfc66a42cbe.webp)

2. Po instalaci rozšíření Prompt flow VS Code klikněte na rozšíření a vyberte **Installation dependencies** podle tohoto návodu nainstalujte Prompt flow SDK ve vašem prostředí

![pfsetup](../../../../../../translated_images/cs/pfsetup.b46e93096f5a254f.webp)

3. Stáhněte [Ukázkový kód](../../../../../../code/09.UpdateSamples/Aug/pf/onnx_inference_pf) a otevřete tento vzorek ve VS Code

![pfsample](../../../../../../translated_images/cs/pfsample.8d89e70584ffe7c4.webp)

4. Otevřete **flow.dag.yaml** a vyberte své Python prostředí

![pfdag](../../../../../../translated_images/cs/pfdag.264a77f7366458ff.webp)

   Otevřete **chat_phi3_ort.py** a změňte umístění Phi-3.5-instruct ONNX modelu

![pfphi](../../../../../../translated_images/cs/pfphi.72da81d74244b45f.webp)

5. Spusťte váš Prompt flow k otestování

Otevřete **flow.dag.yaml** a klikněte na vizuální editor

![pfv](../../../../../../translated_images/cs/pfv.ba8a81f34b20f603.webp)

po kliknutí spusťte test

![pfflow](../../../../../../translated_images/cs/pfflow.4e1135a089b1ce1b.webp)

1. Můžete spustit dávku v terminálu a zkontrolovat více výsledků


```bash

pf run create --file batch_run.yaml --stream --name 'Your eval qa name'    

```

Výsledky můžete zkontrolovat ve vašem výchozím prohlížeči


![pfresult](../../../../../../translated_images/cs/pfresult.c22c826f8062d7cb.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->