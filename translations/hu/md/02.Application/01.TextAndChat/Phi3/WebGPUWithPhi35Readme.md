<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b62864faf628eb07f5231d4885555198",
  "translation_date": "2025-05-09T18:59:42+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md",
  "language_code": "hu"
}
-->
# Phi-3.5-Instruct WebGPU RAG Chatbot

## Bemutató a WebGPU és RAG minta szemléltetésére

A RAG minta a Phi-3.5 Onnx Hosted modellel a Retrieval-Augmented Generation megközelítést használja, amely ötvözi a Phi-3.5 modellek erejét az ONNX hosztolással a hatékony AI alkalmazások érdekében. Ez a minta kulcsfontosságú a modellek finomhangolásában iparág-specifikus feladatokra, egyensúlyt teremtve a minőség, költséghatékonyság és hosszú kontextusú megértés között. Az Azure AI csomag része, amely széles körű modelleket kínál, könnyen megtalálható, kipróbálható és használható, kielégítve a különböző iparágak testreszabási igényeit.

## Mi az a WebGPU
A WebGPU egy modern webes grafikus API, amely hatékony hozzáférést biztosít az eszköz grafikus feldolgozó egységéhez (GPU) közvetlenül a böngészőkből. A WebGL utódjának szánják, több fontos fejlesztéssel:

1. **Kompatibilitás a modern GPU-kkal**: A WebGPU zökkenőmentesen működik a mai GPU architektúrákkal, kihasználva olyan rendszer API-kat, mint a Vulkan, Metal és Direct3D 12.
2. **Fokozott teljesítmény**: Támogatja az általános célú GPU számításokat és gyorsabb műveleteket, így alkalmas mind grafikus megjelenítésre, mind gépi tanulási feladatokra.
3. **Fejlettebb funkciók**: A WebGPU hozzáférést biztosít fejlettebb GPU képességekhez, lehetővé téve összetettebb és dinamikusabb grafikus és számítási munkaterheléseket.
4. **Csökkentett JavaScript terhelés**: Azáltal, hogy több feladatot áthelyez a GPU-ra, a WebGPU jelentősen csökkenti a JavaScript terhelését, jobb teljesítményt és gördülékenyebb élményt nyújtva.

Jelenleg a WebGPU támogatott olyan böngészőkben, mint a Google Chrome, és folyamatban van a támogatás kiterjesztése más platformokra.

### 03.WebGPU
Szükséges környezet:

**Támogatott böngészők:** 
- Google Chrome 113+
- Microsoft Edge 113+
- Safari 18 (macOS 15)
- Firefox Nightly.

### WebGPU engedélyezése:

- Chrome/Microsoft Edge esetén

Engedélyezd a `chrome://flags/#enable-unsafe-webgpu` zászlót.

#### Nyisd meg a böngészőt:
Indítsd el a Google Chrome-ot vagy a Microsoft Edge-et.

#### Lépj be a Flags oldalra:
Írd be a címsorba `chrome://flags` és nyomj Entert.

#### Keresd meg a zászlót:
A keresőmezőbe írd be, hogy 'enable-unsafe-webgpu'

#### Engedélyezd a zászlót:
A találatok között keresd meg a #enable-unsafe-webgpu zászlót.

Kattints a legördülő menüre mellette, és válaszd az Enabled opciót.

#### Indítsd újra a böngészőt:

A zászló engedélyezése után újra kell indítanod a böngészőt, hogy a változtatások érvénybe lépjenek. Kattints az oldal alján megjelenő Relaunch gombra.

- Linuxon indítsd a böngészőt a `--enable-features=Vulkan` kapcsolóval.
- Safari 18 (macOS 15) esetén a WebGPU alapértelmezés szerint engedélyezve van.
- Firefox Nightly-ben írd be a címsorba, hogy about:config, majd `set dom.webgpu.enabled to true`.

### GPU beállítása Microsoft Edge-hez

Íme a lépések, hogyan állítsd be a nagy teljesítményű GPU-t Microsoft Edge alatt Windows rendszeren:

- **Nyisd meg a Beállításokat:** Kattints a Start menüre, majd válaszd a Beállítások lehetőséget.
- **Rendszer beállítások:** Lépj a Rendszer menüpontra, majd a Kijelzőre.
- **Grafikus beállítások:** Görgess le és kattints a Grafikus beállítások menüpontra.
- **Alkalmazás kiválasztása:** A „Válassz alkalmazást a preferencia beállításához” alatt válaszd az Asztali alkalmazást, majd kattints a Tallózásra.
- **Edge kiválasztása:** Navigálj az Edge telepítési mappájába (általában `C:\Program Files (x86)\Microsoft\Edge\Application`), és válaszd ki a `msedge.exe` fájlt.
- **Preferencia beállítása:** Kattints az Opciókra, válaszd a Nagy teljesítményt, majd kattints a Mentésre.
Ez biztosítja, hogy a Microsoft Edge a nagy teljesítményű GPU-dat használja a jobb teljesítmény érdekében.
- **Indítsd újra** a géped, hogy a beállítások életbe lépjenek.

### Példák: Kérjük, [kattints erre a linkre](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások tartalmazhatnak hibákat vagy pontatlanságokat. Az eredeti dokumentum anyanyelvű változata tekintendő hiteles forrásnak. Fontos információk esetén szakmai, emberi fordítást javaslunk. Nem vállalunk felelősséget az ebből a fordításból eredő félreértésekért vagy téves értelmezésekért.