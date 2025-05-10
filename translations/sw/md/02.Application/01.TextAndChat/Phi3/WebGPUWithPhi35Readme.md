<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b62864faf628eb07f5231d4885555198",
  "translation_date": "2025-05-09T18:59:33+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md",
  "language_code": "sw"
}
-->
# Phi-3.5-Instruct WebGPU RAG Chatbot

## Demo ya kuonyesha WebGPU na Mchoro wa RAG

Mchoro wa RAG unaotumia Phi-3.5 Onnx Hosted model hutumia mbinu ya Retrieval-Augmented Generation, ikichanganya nguvu za modeli za Phi-3.5 na uendeshaji wa ONNX kwa ufanisi wa AI. Mchoro huu ni muhimu katika kufinyaza modeli kwa kazi maalum za sekta, ukitoa mchanganyiko wa ubora, gharama nafuu, na uelewa wa muktadha mrefu. Ni sehemu ya Azure AI, ikitoa chaguo nyingi za modeli ambazo ni rahisi kupatikana, kujaribu, na kutumia, zikiendana na mahitaji ya kubinafsisha ya sekta mbalimbali.

## WebGPU ni Nini  
WebGPU ni API ya kisasa ya michoro ya wavuti iliyoundwa kutoa ufikiaji mzuri wa moja kwa moja kwa GPU ya kifaa kutoka kwa vivinjari vya wavuti. Inakusudiwa kuwa mrithi wa WebGL, ikitoa maboresho kadhaa muhimu:

1. **Ulinganifu na GPU za Kisasa**: WebGPU imejengwa kufanya kazi kwa urahisi na miundo ya kisasa ya GPU, ikitumia API za mfumo kama Vulkan, Metal, na Direct3D 12.
2. **Utendaji Bora**: Inaunga mkono hesabu za GPU kwa matumizi ya jumla na operesheni za kasi, ikifaa kwa michoro na kazi za kujifunza mashine.
3. **Sifa Zaidi Zinazoendelea**: WebGPU inatoa ufikiaji wa uwezo wa juu wa GPU, kuwezesha michoro tata na mizigo ya hesabu yenye nguvu zaidi.
4. **Kupunguza Mzigo wa JavaScript**: Kwa kuhamisha kazi zaidi kwa GPU, WebGPU inapunguza mzigo wa JavaScript, na kusababisha utendaji bora na uzoefu laini zaidi.

WebGPU kwa sasa inasaidiwa katika vivinjari kama Google Chrome, na kazi inaendelea kupanua msaada kwa majukwaa mengine.

### 03.WebGPU  
Mazingira Yanayohitajika:

**Vivinjari vinavyotumika:**  
- Google Chrome 113+  
- Microsoft Edge 113+  
- Safari 18 (macOS 15)  
- Firefox Nightly.

### Washa WebGPU:

- Katika Chrome/Microsoft Edge  

Washa bendera ya `chrome://flags/#enable-unsafe-webgpu`.

#### Fungua Kivinjari Chako:  
Anzisha Google Chrome au Microsoft Edge.

#### Fikia Ukurasa wa Bendera:  
Katika mstari wa anwani, andika `chrome://flags` na bonyeza Enter.

#### Tafuta Bendera:  
Katika kisanduku cha utafutaji juu ya ukurasa, andika 'enable-unsafe-webgpu'

#### Washa Bendera:  
Tafuta bendera ya #enable-unsafe-webgpu kwenye orodha ya matokeo.

Bonyeza menyu ya kushuka kando yake na chagua Enabled.

#### Anzisha Kivinjari Chako Upya:  

Baada ya kuwasha bendera, utahitaji kuanzisha kivinjari chako upya ili mabadiliko yaanze kutumika. Bonyeza kitufe cha Relaunch kinachoonekana chini ya ukurasa.

- Kwa Linux, anzisha kivinjari kwa kutumia `--enable-features=Vulkan`.  
- Safari 18 (macOS 15) ina WebGPU imewashwa kwa chaguo-msingi.  
- Katika Firefox Nightly, ingiza about:config katika mstari wa anwani na `set dom.webgpu.enabled to true`.

### Kuandaa GPU kwa Microsoft Edge  

Hapa ni hatua za kuandaa GPU yenye utendaji wa juu kwa Microsoft Edge kwenye Windows:

- **Fungua Settings:** Bonyeza kwenye menyu ya Start na chagua Settings.  
- **Mipangilio ya Mfumo:** Nenda kwenye System kisha Display.  
- **Mipangilio ya Michoro:** Shuka chini na bonyeza Graphics settings.  
- **Chagua Programu:** Chini ya “Choose an app to set preference,” chagua Desktop app kisha Browse.  
- **Chagua Edge:** Nenda kwenye folda ya ufungaji wa Edge (kwa kawaida `C:\Program Files (x86)\Microsoft\Edge\Application`) na chagua `msedge.exe`.  
- **Weka Mapendeleo:** Bonyeza Options, chagua High performance, kisha bonyeza Save.  
Hii itahakikisha Microsoft Edge inatumia GPU yako yenye utendaji wa juu kwa utendaji bora.  
- **Anzisha upya** kompyuta yako ili mipangilio hii itumike.

### Sampuli : Tafadhali [bonyeza hapa](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

**Kikomo cha Majukumu**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuwa sahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au kasoro. Hati asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha uhakika. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inashauriwa. Hatubebeki dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.