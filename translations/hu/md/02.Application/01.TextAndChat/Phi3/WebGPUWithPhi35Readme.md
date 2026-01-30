# Phi-3.5-Instruct WebGPU RAG Chatbot

## Bemutató a WebGPU és a RAG minta szemléltetésére

A RAG minta a Phi-3.5 Onnx Hosted modellel a Retrieval-Augmented Generation megközelítést használja, amely ötvözi a Phi-3.5 modellek erejét az ONNX hosztolással a hatékony AI alkalmazások érdekében. Ez a minta kulcsfontosságú a modellek finomhangolásában iparágspecifikus feladatokra, egyensúlyt teremtve a minőség, költséghatékonyság és a hosszú kontextusú megértés között. Az Azure AI csomag része, amely széles választékban kínál modelleket, könnyen megtalálhatók, kipróbálhatók és használhatók, így megfelelve a különböző iparágak testreszabási igényeinek.

## Mi az a WebGPU
A WebGPU egy modern webes grafikus API, amely hatékony hozzáférést biztosít az eszköz grafikus feldolgozó egységéhez (GPU) közvetlenül a böngészőkből. A WebGL utódjának szánják, számos fontos fejlesztéssel:

1. **Kompatibilitás a modern GPU-kkal**: A WebGPU zökkenőmentesen működik a mai GPU architektúrákkal, kihasználva olyan rendszer API-kat, mint a Vulkan, Metal és Direct3D 12.
2. **Fokozott teljesítmény**: Támogatja az általános célú GPU számításokat és gyorsabb műveleteket, így alkalmas mind grafikus megjelenítésre, mind gépi tanulási feladatokra.
3. **Fejlett funkciók**: Hozzáférést biztosít fejlettebb GPU képességekhez, lehetővé téve összetettebb és dinamikusabb grafikus és számítási munkaterheléseket.
4. **Csökkentett JavaScript terhelés**: Mivel több feladatot áthárít a GPU-ra, a WebGPU jelentősen csökkenti a JavaScript terhelését, jobb teljesítményt és gördülékenyebb élményt eredményezve.

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

Kapcsold be a `chrome://flags/#enable-unsafe-webgpu` zászlót.

#### Nyisd meg a böngészőt:
Indítsd el a Google Chrome-ot vagy a Microsoft Edge-et.

#### Lépj a Flags oldalra:
Írd be a címsorba, hogy `chrome://flags`, majd nyomj Entert.

#### Keresd meg a zászlót:
A lap tetején lévő keresőmezőbe írd be: 'enable-unsafe-webgpu'

#### Engedélyezd a zászlót:
A találatok között keresd meg a #enable-unsafe-webgpu zászlót.

Kattints a mellette lévő legördülő menüre, és válaszd az Engedélyezett opciót.

#### Indítsd újra a böngészőt:

A zászló engedélyezése után újra kell indítanod a böngészőt, hogy a változtatások érvénybe lépjenek. Kattints az oldal alján megjelenő Újraindítás gombra.

- Linux esetén indítsd a böngészőt a `--enable-features=Vulkan` kapcsolóval.
- Safari 18 (macOS 15) esetén a WebGPU alapértelmezetten engedélyezve van.
- Firefox Nightly-ben írd be a címsorba, hogy about:config, és állítsd a dom.webgpu.enabled értékét true-ra.

### GPU beállítása Microsoft Edge-hez

Íme a lépések, hogy magas teljesítményű GPU-t állíts be Microsoft Edge-hez Windows rendszeren:

- **Nyisd meg a Beállításokat:** Kattints a Start menüre, majd válaszd a Beállítások menüpontot.
- **Rendszer beállítások:** Menj a Rendszer, majd a Kijelző menüpontra.
- **Grafikus beállítások:** Görgess le, és kattints a Grafikus beállítások lehetőségre.
- **Alkalmazás kiválasztása:** Az „Alkalmazás kiválasztása a preferencia beállításához” alatt válaszd az Asztali alkalmazást, majd kattints a Tallózás gombra.
- **Edge kiválasztása:** Navigálj az Edge telepítési mappájába (általában `C:\Program Files (x86)\Microsoft\Edge\Application`), és válaszd ki az `msedge.exe` fájlt.
- **Preferencia beállítása:** Kattints az Opciók gombra, válaszd a Magas teljesítmény opciót, majd kattints a Mentésre.
Ez biztosítja, hogy a Microsoft Edge a magas teljesítményű GPU-dat használja a jobb teljesítmény érdekében.
- **Indítsd újra** a géped, hogy a beállítások érvénybe lépjenek.

### Minták : Kérlek, [kattints erre a linkre](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén szakmai, emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.