<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1ff728038c4f554b660a36b76cbdd6e",
  "translation_date": "2025-07-16T21:12:25+00:00",
  "source_file": "md/01.Introduction/03/overview.md",
  "language_code": "hu"
}
-->
A Phi-3-mini esetében az inferencia azt a folyamatot jelenti, amikor a modellt használjuk előrejelzések készítésére vagy kimenetek generálására a bemeneti adatok alapján. Hadd adjak részletesebb tájékoztatást a Phi-3-mini-ről és az inferencia képességeiről.

A Phi-3-mini a Microsoft által kiadott Phi-3 modellek sorozatának része. Ezek a modellek arra lettek tervezve, hogy újradefiniálják, mit lehet elérni a Kis Nyelvi Modellekkel (SLM-ek).

Íme néhány fontos pont a Phi-3-mini-ről és az inferencia képességeiről:

## **Phi-3-mini áttekintés:**
- A Phi-3-mini paramétermérete 3,8 milliárd.
- Nemcsak hagyományos számítógépes eszközökön, hanem élőhelyi eszközökön, például mobiltelefonokon és IoT eszközökön is futtatható.
- A Phi-3-mini megjelenése lehetővé teszi egyének és vállalatok számára, hogy SLM-eket telepítsenek különböző hardvereszközökön, különösen erőforrás-korlátozott környezetekben.
- Többféle modellformátumot támogat, beleértve a hagyományos PyTorch formátumot, a gguf formátum kvantált változatát, valamint az ONNX-alapú kvantált verziót.

## **Phi-3-mini elérése:**
A Phi-3-mini eléréséhez használhatod a [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) alkalmazást egy Copilot alkalmazásban. A Semantic Kernel általában kompatibilis az Azure OpenAI Service-szel, a Hugging Face nyílt forráskódú modelljeivel, valamint helyi modellekkel.
Használhatod továbbá az [Ollama](https://ollama.com) vagy a [LlamaEdge](https://llamaedge.com) szolgáltatásokat is a kvantált modellek hívására. Az Ollama lehetővé teszi egyéni felhasználók számára különböző kvantált modellek használatát, míg a LlamaEdge platformok közötti elérhetőséget biztosít a GGUF modellekhez.

## **Kvantált modellek:**
Sok felhasználó előnyben részesíti a kvantált modellek helyi inferenciához való használatát. Például közvetlenül futtathatod az Ollama-val a Phi-3-at, vagy offline konfigurálhatod Modelfile segítségével. A Modelfile megadja a GGUF fájl elérési útját és a prompt formátumát.

## **Generatív AI lehetőségek:**
Az olyan SLM-ek, mint a Phi-3-mini kombinálása új lehetőségeket nyit a generatív AI számára. Az inferencia csak az első lépés; ezek a modellek különféle feladatokra használhatók erőforrás-korlátozott, késleltetés-korlátozott és költség-korlátozott helyzetekben.

## **Generatív AI kiaknázása a Phi-3-mini segítségével: Útmutató az inferenciához és telepítéshez**  
Ismerd meg, hogyan használhatod a Semantic Kernel-t, az Ollama/LlamaEdge-t és az ONNX Runtime-ot a Phi-3-mini modellek eléréséhez és inferenciájához, valamint fedezd fel a generatív AI lehetőségeit különböző alkalmazási forgatókönyvekben.

**Funkciók**  
Inferenciát végezhetsz phi3-mini modellel az alábbi platformokon:

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)  
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)  
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)  
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)  
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)  

Összefoglalva, a Phi-3-mini lehetővé teszi a fejlesztők számára, hogy különböző modellformátumokat fedezzenek fel, és kihasználják a generatív AI előnyeit számos alkalmazási területen.

**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.