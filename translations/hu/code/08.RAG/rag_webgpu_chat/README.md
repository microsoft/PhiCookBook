<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4aac6b8a5dcbbe9a32b47be30340cac2",
  "translation_date": "2025-05-09T05:22:08+00:00",
  "source_file": "code/08.RAG/rag_webgpu_chat/README.md",
  "language_code": "hu"
}
-->
Phi-3-mini WebGPU RAG Chatbot

## Bemutató a WebGPU és a RAG minta szemléltetésére
A RAG minta a Phi-3 Onnx Hosted modellel a Retrieval-Augmented Generation megközelítést alkalmazza, amely ötvözi a Phi-3 modellek erejét az ONNX hosztolással a hatékony AI telepítésekhez. Ez a minta kulcsfontosságú a modellek finomhangolásában speciális feladatokra, egyensúlyt teremtve a minőség, költséghatékonyság és hosszú távú kontextus megértése között. Az Azure AI részeként széles körű modellek közül választhatunk, amelyek könnyen elérhetők, kipróbálhatók és használhatók, kielégítve a különböző iparágak testreszabási igényeit. A Phi-3 modellek, beleértve a Phi-3-mini, Phi-3-small és Phi-3-medium változatokat, elérhetők az Azure AI Model Catalogban, és önállóan vagy olyan platformokon keresztül, mint a HuggingFace és ONNX, finomhangolhatók és telepíthetők, ami a Microsoft elkötelezettségét mutatja az elérhető és hatékony AI megoldások iránt.

## Mi az a WebGPU
A WebGPU egy modern webes grafikus API, amely hatékony hozzáférést biztosít az eszköz grafikus feldolgozó egységéhez (GPU) közvetlenül a böngészőkből. A WebGL utódjaként tervezték, számos fontos fejlesztéssel:

1. **Kompatibilitás a modern GPU-kkal**: A WebGPU zökkenőmentesen működik a korszerű GPU architektúrákkal, kihasználva a rendszer API-kat, mint a Vulkan, Metal és Direct3D 12.
2. **Fokozott teljesítmény**: Támogatja az általános célú GPU számításokat és gyorsabb műveleteket, így alkalmas mind grafikus megjelenítésre, mind gépi tanulási feladatokra.
3. **Fejlett funkciók**: Hozzáférést biztosít fejlettebb GPU képességekhez, lehetővé téve bonyolultabb és dinamikusabb grafikus és számítási munkaterheléseket.
4. **Csökkentett JavaScript terhelés**: A GPU-ra történő nagyobb terhelés átvitelével jelentősen csökkenti a JavaScript terhelését, ami jobb teljesítményt és gördülékenyebb élményt eredményez.

A WebGPU jelenleg olyan böngészőkben támogatott, mint a Google Chrome, és folyamatban van a támogatás bővítése más platformokra.

### 03.WebGPU
Szükséges környezet:

**Támogatott böngészők:** 
- Google Chrome 113+
- Microsoft Edge 113+
- Safari 18 (macOS 15)
- Firefox Nightly.

### WebGPU engedélyezése:

- Chrome/Microsoft Edge-ben

Engedélyezd a `chrome://flags/#enable-unsafe-webgpu` zászlót.

#### Böngésző megnyitása:
Indítsd el a Google Chrome-ot vagy a Microsoft Edge-et.

#### Zászlók oldal megnyitása:
Írd be a címsorba `chrome://flags`, majd nyomj Entert.

#### Keresés a zászló között:
A keresőmezőbe írd be, hogy 'enable-unsafe-webgpu'

#### A zászló engedélyezése:
A találatok között keresd meg a #enable-unsafe-webgpu zászlót.

Kattints a mellette lévő legördülő menüre, és válaszd az Enabled opciót.

#### Böngésző újraindítása:

A zászló engedélyezése után újra kell indítanod a böngészőt, hogy a változtatások érvénybe lépjenek. Kattints az oldal alján megjelenő Relaunch gombra.

- Linux esetén indítsd a böngészőt a `--enable-features=Vulkan` kapcsolóval.
- Safari 18 (macOS 15) esetén a WebGPU alapértelmezetten engedélyezve van.
- Firefox Nightly-ben írd be a címsorba, hogy about:config, majd `set dom.webgpu.enabled to true`.

### GPU beállítása Microsoft Edge-hez

Íme a lépések egy nagy teljesítményű GPU beállításához Microsoft Edge alatt Windows rendszeren:

- **Beállítások megnyitása:** Kattints a Start menüre, majd válaszd a Beállításokat.
- **Rendszerbeállítások:** Lépj a Rendszer, majd a Kijelző menüpontra.
- **Grafikus beállítások:** Görgess le és kattints a Grafikus beállítások elemre.
- **Alkalmazás kiválasztása:** Az „Alkalmazás kiválasztása a preferencia beállításához” alatt válaszd az Asztali alkalmazást, majd a Tallózás lehetőséget.
- **Edge kiválasztása:** Navigálj az Edge telepítési mappájába (általában `C:\Program Files (x86)\Microsoft\Edge\Application`), és válaszd ki a `msedge.exe` fájlt.
- **Preferencia beállítása:** Kattints az Opciók gombra, válaszd a Nagy teljesítmény lehetőséget, majd kattints a Mentésre.
Ez biztosítja, hogy a Microsoft Edge a nagy teljesítményű GPU-dat használja a jobb teljesítmény érdekében.
- **Indítsd újra** a géped a beállítások érvényesítéséhez.

### Kódtered megnyitása:
Navigálj a GitHubon a tárhelyedhez.
Kattints a Code gombra, majd válaszd az Open with Codespaces lehetőséget.

Ha még nincs Codespace-ed, létrehozhatsz egyet a New codespace gombra kattintva.

**Megjegyzés** Node környezet telepítése a codespace-ben
Egy npm demó futtatása GitHub Codespace-ből remek módja a projekt tesztelésének és fejlesztésének. Íme egy lépésről lépésre útmutató:

### Környezet beállítása:
Miután megnyitottad a Codespace-edet, győződj meg róla, hogy a Node.js és az npm telepítve van. Ellenőrizheted ezt a következő parancsok futtatásával:
```
node -v
```
```
npm -v
```

Ha nincs telepítve, telepítheted a következő parancsokkal:
```
sudo apt-get update
```
```
sudo apt-get install nodejs npm
```

### Navigálás a projekt könyvtárába:
Használd a terminált, hogy belépj abba a könyvtárba, ahol az npm projekted található:
```
cd path/to/your/project
```

### Függőségek telepítése:
Futtasd a következő parancsot az összes szükséges függőség telepítéséhez, amelyek a package.json fájlban vannak felsorolva:

```
npm install
```

### Demó futtatása:
Miután a függőségek telepítve vannak, futtathatod a demó scriptedet. Ez általában a package.json scripts részében van megadva. Például, ha a demó scripted neve start, futtasd:

```
npm run build
```
```
npm run dev
```

### Demó elérése:
Ha a demód web szervert használ, a Codespaces egy URL-t biztosít az eléréséhez. Figyeld a értesítéseket, vagy nézd meg a Ports fület az URL megtalálásához.

**Megjegyzés:** A modellnek be kell töltődnie a böngészőben, ezért eltarthat egy ideig, amíg betöltődik.

### RAG Demo
Töltsd fel a `intro_rag.md` to complete the RAG solution. If using codespaces you can download the file located in `01.InferencePhi3/docs/` markdown fájlt.

### Fájl kiválasztása:
Kattints a „Choose File” gombra, hogy kiválaszd a feltölteni kívánt dokumentumot.

### Dokumentum feltöltése:
A fájl kiválasztása után kattints az „Upload” gombra, hogy betöltsd a dokumentumot a RAG (Retrieval-Augmented Generation) használatához.

### Chat indítása:
Miután a dokumentum fel lett töltve, elindíthatod a chatet a RAG segítségével, a dokumentum tartalma alapján.

**Nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hivatalos forrásnak. Kritikus információk esetén professzionális emberi fordítást javaslunk. Nem vállalunk felelősséget az ebből eredő félreértésekért vagy téves értelmezésekért.