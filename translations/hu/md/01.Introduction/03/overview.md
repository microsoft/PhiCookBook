<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1ff728038c4f554b660a36b76cbdd6e",
  "translation_date": "2025-05-09T12:30:57+00:00",
  "source_file": "md/01.Introduction/03/overview.md",
  "language_code": "hu"
}
-->
A Phi-3-mini kontextusában az inference azt a folyamatot jelenti, amikor a modellt használjuk előrejelzések készítésére vagy kimenetek generálására bemeneti adatok alapján. Engedje meg, hogy részletesebben bemutassam a Phi-3-mini-t és annak inference képességeit.

A Phi-3-mini a Microsoft által kiadott Phi-3 modellek sorozatához tartozik. Ezeket a modelleket úgy tervezték, hogy újradefiniálják, mit lehet elérni a Kis Nyelvi Modellekkel (SLM-ek).

Íme néhány fontos pont a Phi-3-mini-ről és annak inference képességeiről:

## **Phi-3-mini áttekintés:**
- A Phi-3-mini paramétermérete 3,8 milliárd.
- Nemcsak hagyományos számítógépeken, hanem élő eszközökön, például mobiltelefonokon és IoT eszközökön is futtatható.
- A Phi-3-mini megjelenése lehetővé teszi magánszemélyek és vállalatok számára, hogy SLM-eket telepítsenek különböző hardvereken, különösen erőforrás-korlátozott környezetekben.
- Több modellformátumot támogat, beleértve a hagyományos PyTorch formátumot, a gguf formátum kvantált változatát, valamint az ONNX-alapú kvantált verziót.

## **Phi-3-mini elérése:**
A Phi-3-mini eléréséhez használhatja a [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) eszközt egy Copilot alkalmazásban. A Semantic Kernel általában kompatibilis az Azure OpenAI Service-szel, a Hugging Face nyílt forráskódú modelljeivel és helyi modellekkel is.
Ezenkívül használhatja az [Ollama](https://ollama.com) vagy [LlamaEdge](https://llamaedge.com) szolgáltatásokat kvantált modellek hívásához. Az Ollama lehetővé teszi egyéni felhasználók számára különböző kvantált modellek használatát, míg a LlamaEdge platformközi elérhetőséget biztosít GGUF modellekhez.

## **Kvantált modellek:**
Sok felhasználó a helyi inference-hez inkább kvantált modelleket használ. Például közvetlenül az Ollama segítségével futtathatja a Phi-3-at, vagy offline konfigurálhatja Modelfile használatával. A Modelfile megadja a GGUF fájl elérési útját és a prompt formátumát.

## **Generatív AI lehetőségek:**
Az olyan SLM-ek, mint a Phi-3-mini kombinálása új lehetőségeket nyit meg a generatív AI területén. Az inference csak az első lépés; ezek a modellek különféle feladatokra használhatók erőforrás-korlátozott, késleltetésre érzékeny és költségkorlátos helyzetekben.

## **Generatív AI kiaknázása a Phi-3-mini segítségével: Útmutató az inference-hez és telepítéshez**
Ismerje meg, hogyan használhatja a Semantic Kernel-t, az Ollama/LlamaEdge-et és az ONNX Runtime-ot a Phi-3-mini modellek eléréséhez és inference-hez, valamint fedezze fel a generatív AI lehetőségeit különféle alkalmazási forgatókönyvekben.

**Funkciók**
Phi-3-mini modell inference a következő platformokon:

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)

Összefoglalva, a Phi-3-mini lehetővé teszi a fejlesztők számára, hogy különböző modellformátumokat fedezzenek fel, és generatív AI-t alkalmazzanak különféle alkalmazási területeken.

**Nyilatkozat**:  
Ezt a dokumentumot az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével fordítottuk le. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javaslunk. Nem vállalunk felelősséget az ebből a fordításból eredő félreértésekért vagy téves értelmezésekért.