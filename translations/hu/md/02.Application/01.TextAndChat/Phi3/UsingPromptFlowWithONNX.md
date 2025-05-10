<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "92e7dac1e5af0dd7c94170fdaf6860fe",
  "translation_date": "2025-05-09T18:54:42+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md",
  "language_code": "hu"
}
-->
# Windows GPU használata Prompt flow megoldás létrehozásához Phi-3.5-Instruct ONNX-szel

Az alábbi dokumentum egy példát mutat be arra, hogyan használjuk a PromptFlow-t ONNX (Open Neural Network Exchange) segítségével Phi-3 alapú AI alkalmazások fejlesztéséhez.

A PromptFlow egy fejlesztői eszközkészlet, amely az LLM-alapú (Nagy Nyelvi Modell) AI alkalmazások teljes fejlesztési ciklusát egyszerűsíti, az ötleteléstől és prototípus készítéstől kezdve a tesztelésen és értékelésen át a végső élesítésig.

A PromptFlow és az ONNX integrálásával a fejlesztők:

- Optimalizálhatják a modell teljesítményét: kihasználhatják az ONNX hatékony modell-inferenciáját és telepítését.
- Egyszerűsíthetik a fejlesztést: a PromptFlow segítségével kezelhetik a munkafolyamatokat és automatizálhatják az ismétlődő feladatokat.
- Javíthatják az együttműködést: egységes fejlesztői környezet biztosításával könnyebbé válik a csapatmunka.

**A Prompt flow** egy fejlesztői eszközkészlet, amely az LLM-alapú AI alkalmazások teljes fejlesztési ciklusát egyszerűsíti az ötleteléstől, prototípus készítésen, tesztelésen, értékelésen át egészen az éles telepítésig és monitorozásig. Megkönnyíti a prompt tervezést, és lehetővé teszi, hogy éles minőségű LLM alkalmazásokat építsünk.

A Prompt flow képes csatlakozni az OpenAI-hoz, az Azure OpenAI Service-hez, valamint testreszabható modellekhez (Huggingface, helyi LLM/SLM). Célunk, hogy a Phi-3.5 kvantált ONNX modelljét helyi alkalmazásokba telepítsük. A Prompt flow segít jobb üzleti tervezésben és helyi megoldások elkészítésében Phi-3.5 alapokon. Ebben a példában az ONNX Runtime GenAI könyvtárat kombináljuk a Prompt flow megoldás elkészítéséhez Windows GPU környezetben.

## **Telepítés**

### **ONNX Runtime GenAI Windows GPU-hoz**

Olvasd el ezt az útmutatót az ONNX Runtime GenAI Windows GPU-ra történő beállításához [ide kattintva](./ORTWindowGPUGuideline.md)

### **Prompt flow beállítása VSCode-ban**

1. Telepítsd a Prompt flow VS Code kiterjesztést

![pfvscode](../../../../../../translated_images/pfvscode.79f42ae5dd93ed35c19d6d978ae75831fef40e0b8440ee48b893b5a0597d2260.hu.png)

2. A Prompt flow VS Code kiterjesztés telepítése után kattints a kiterjesztésre, majd válaszd az **Installation dependencies** opciót, és kövesd az útmutatót a Prompt flow SDK telepítéséhez a környezetedben

![pfsetup](../../../../../../translated_images/pfsetup.0c82d99c7760aac29833b37faf4329e67e22279b1c5f37a73724dfa9ebaa32ee.hu.png)

3. Töltsd le a [példakódot](../../../../../../code/09.UpdateSamples/Aug/pf/onnx_inference_pf) és nyisd meg VS Code-ban

![pfsample](../../../../../../translated_images/pfsample.7bf40b133a558d86356dd6bc0e480bad2659d9c5364823dae9b3e6784e6f2d25.hu.png)

4. Nyisd meg a **flow.dag.yaml** fájlt, és válaszd ki a Python környezetedet

![pfdag](../../../../../../translated_images/pfdag.c5eb356fa3a96178cd594de9a5da921c4bbe646a9946f32aa20d344ccbeb51a0.hu.png)

   Nyisd meg a **chat_phi3_ort.py** fájlt, és módosítsd a Phi-3.5-instruct ONNX modell helyét

![pfphi](../../../../../../translated_images/pfphi.fff4b0afea47c92c8481174dbf3092823906fca5b717fc642f78947c3e5bbb39.hu.png)

5. Futtasd a prompt flow-t teszteléshez

Nyisd meg a **flow.dag.yaml** fájlt, és kattints a vizuális szerkesztőre

![pfv](../../../../../../translated_images/pfv.7af6ecd65784a98558b344ba69b5ba6233876823fb435f163e916a632394fc1e.hu.png)

Ezután kattints rá, és futtasd a tesztelést

![pfflow](../../../../../../translated_images/pfflow.9697e0fda67794bb0cf4b78d52e6f5a42002eec935bc2519933064afbbdd34f0.hu.png)

1. Terminálban is futtathatsz batch-et, hogy több eredményt ellenőrizz

```bash

pf run create --file batch_run.yaml --stream --name 'Your eval qa name'    

```

Az eredményeket az alapértelmezett böngésződben tekintheted meg

![pfresult](../../../../../../translated_images/pfresult.972eb57dd5bec646e1aa01148991ba8959897efea396e42cf9d7df259444878d.hu.png)

**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum a saját nyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.