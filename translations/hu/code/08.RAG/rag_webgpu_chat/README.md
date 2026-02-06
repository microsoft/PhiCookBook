Phi-3-mini WebGPU RAG Chatbot

## Demo a WebGPU és a RAG minta bemutatására
A RAG minta a Phi-3 Onnx Hosted modellel a Retrieval-Augmented Generation megközelítést használja, amely ötvözi a Phi-3 modellek erejét az ONNX hosztolással a hatékony AI telepítések érdekében. Ez a minta kulcsfontosságú a modellek finomhangolásában iparágspecifikus feladatokra, minőséget, költséghatékonyságot és hosszú kontextusú megértést kínálva. Az Azure AI csomag része, amely széles választékban kínál modelleket, könnyen megtalálhatók, kipróbálhatók és használhatók, megfelelve a különböző iparágak testreszabási igényeinek. A Phi-3 modellek, beleértve a Phi-3-mini, Phi-3-small és Phi-3-medium modelleket, elérhetők az Azure AI Model Catalogban, és önállóan vagy olyan platformokon keresztül, mint a HuggingFace és ONNX, finomhangolhatók és telepíthetők, bemutatva a Microsoft elkötelezettségét a hozzáférhető és hatékony AI megoldások iránt.

## Mi az a WebGPU
A WebGPU egy modern webes grafikus API, amely hatékony hozzáférést biztosít az eszköz grafikus feldolgozó egységéhez (GPU) közvetlenül a böngészőkből. A WebGL utódjának szánják, számos fontos fejlesztéssel:

1. **Kompatibilitás a modern GPU-kkal**: A WebGPU úgy lett tervezve, hogy zökkenőmentesen működjön a korszerű GPU architektúrákkal, kihasználva olyan rendszer API-kat, mint a Vulkan, Metal és Direct3D 12.
2. **Fokozott teljesítmény**: Támogatja az általános célú GPU számításokat és gyorsabb műveleteket, így alkalmas mind grafikus megjelenítésre, mind gépi tanulási feladatokra.
3. **Fejlett funkciók**: A WebGPU hozzáférést biztosít fejlettebb GPU képességekhez, lehetővé téve összetettebb és dinamikusabb grafikus és számítási munkaterheléseket.
4. **Csökkentett JavaScript terhelés**: Azáltal, hogy több feladatot áthárít a GPU-ra, a WebGPU jelentősen csökkenti a JavaScript terhelését, jobb teljesítményt és simább élményt eredményezve.

A WebGPU jelenleg olyan böngészőkben támogatott, mint a Google Chrome, és folyamatosan dolgoznak a támogatás bővítésén más platformokra.

### 03.WebGPU
Szükséges környezet:

**Támogatott böngészők:**  
- Google Chrome 113+  
- Microsoft Edge 113+  
- Safari 18 (macOS 15)  
- Firefox Nightly.

### WebGPU engedélyezése:

- Chrome/Microsoft Edge esetén

Kapcsold be a `chrome://flags/#enable-unsafe-webgpu` kapcsolót.

#### Nyisd meg a böngészőt:
Indítsd el a Google Chrome-ot vagy a Microsoft Edge-et.

#### Lépj be a Flags oldalra:
Írd be a címsorba, hogy `chrome://flags`, majd nyomj Entert.

#### Keresd meg a kapcsolót:
A keresőmezőbe írd be: 'enable-unsafe-webgpu'

#### Kapcsold be a kapcsolót:
A találatok között keresd meg a #enable-unsafe-webgpu kapcsolót.

Kattints a mellette lévő legördülő menüre, és válaszd az Engedélyezett opciót.

#### Indítsd újra a böngészőt:

A kapcsoló bekapcsolása után újra kell indítanod a böngészőt, hogy a változtatások érvénybe lépjenek. Kattints az oldal alján megjelenő Újraindítás gombra.

- Linux esetén indítsd a böngészőt a `--enable-features=Vulkan` kapcsolóval.
- Safari 18 (macOS 15) esetén a WebGPU alapértelmezetten engedélyezve van.
- Firefox Nightly-ben írd be a címsorba, hogy about:config, és állítsd a dom.webgpu.enabled értékét true-ra.

### GPU beállítása Microsoft Edge-hez

Íme a lépések egy nagy teljesítményű GPU beállításához Microsoft Edge alatt Windows rendszeren:

- **Nyisd meg a Beállításokat:** Kattints a Start menüre, majd válaszd a Beállítások menüpontot.
- **Rendszer beállítások:** Menj a Rendszer menüpontra, majd a Kijelzőre.
- **Grafikus beállítások:** Görgess le, és kattints a Grafikus beállítások menüpontra.
- **Alkalmazás kiválasztása:** Az „Alkalmazás kiválasztása a preferencia beállításához” alatt válaszd az Asztali alkalmazást, majd kattints a Tallózásra.
- **Edge kiválasztása:** Navigálj az Edge telepítési mappájába (általában `C:\Program Files (x86)\Microsoft\Edge\Application`), és válaszd ki az `msedge.exe` fájlt.
- **Preferencia beállítása:** Kattints az Opciókra, válaszd a Nagy teljesítmény opciót, majd kattints a Mentésre.
Ez biztosítja, hogy a Microsoft Edge a nagy teljesítményű GPU-dat használja a jobb teljesítmény érdekében.  
- **Indítsd újra** a géped, hogy a beállítások életbe lépjenek.

### Nyisd meg a Codespace-edet:
Navigálj a GitHub tárhelyedhez.  
Kattints a Code gombra, majd válaszd az Open with Codespaces opciót.

Ha még nincs Codespace-ed, létrehozhatsz egyet a New codespace gombra kattintva.

**Megjegyzés** Node környezet telepítése a codespace-edben  
Egy npm demo futtatása GitHub Codespace-ből remek módja a projekt tesztelésének és fejlesztésének. Íme egy lépésről lépésre útmutató a kezdéshez:

### Állítsd be a környezeted:
Miután megnyitottad a Codespace-et, győződj meg róla, hogy telepítve van a Node.js és az npm. Ellenőrizheted a következő parancsokkal:  
```
node -v
```  
```
npm -v
```

Ha nincsenek telepítve, telepítheted őket a következőkkel:  
```
sudo apt-get update
```  
```
sudo apt-get install nodejs npm
```

### Navigálj a projekt könyvtáradba:
Használd a terminált, hogy a npm projekted könyvtárába lépj:  
```
cd path/to/your/project
```

### Telepítsd a függőségeket:
Futtasd a következő parancsot, hogy telepítsd az összes szükséges függőséget, amelyek a package.json fájlban vannak felsorolva:  

```
npm install
```

### Futtasd a demót:
Miután a függőségek telepítve vannak, futtathatod a demo scriptedet. Ez általában a package.json scripts szekciójában van megadva. Például, ha a demo scripted neve start, futtasd:  

```
npm run build
```  
```
npm run dev
```

### Érd el a demót:
Ha a demód web szervert használ, a Codespaces biztosít egy URL-t a hozzáféréshez. Figyeld a értesítéseket vagy nézd meg a Ports fület az URL megtalálásához.

**Megjegyzés:** A modellnek a böngészőben kell lennie cache-elve, ezért a betöltés eltarthat egy ideig.

### RAG Demo
Töltsd fel az `intro_rag.md` markdown fájlt a RAG megoldás befejezéséhez. Ha codespace-et használsz, letöltheted a fájlt a `01.InferencePhi3/docs/` mappából.

### Válaszd ki a fájlodat:
Kattints a „Choose File” gombra, hogy kiválaszd a feltölteni kívánt dokumentumot.

### Töltsd fel a dokumentumot:
A fájl kiválasztása után kattints az „Upload” gombra, hogy betöltsd a dokumentumot a RAG (Retrieval-Augmented Generation) számára.

### Indítsd el a csevegést:
Miután a dokumentum fel lett töltve, elindíthatsz egy csevegést a RAG segítségével, a dokumentum tartalma alapján.

**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Kritikus információk esetén professzionális emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.