<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b62864faf628eb07f5231d4885555198",
  "translation_date": "2025-07-17T03:12:20+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md",
  "language_code": "sw"
}
-->
# Phi-3.5-Instruct WebGPU RAG Chatbot

## Demo ya kuonyesha WebGPU na Muundo wa RAG

Muundo wa RAG pamoja na modeli ya Phi-3.5 Onnx iliyohost huchukua mbinu ya Retrieval-Augmented Generation, ikichanganya nguvu za modeli za Phi-3.5 na uendeshaji wa ONNX kwa ufanisi wa AI. Muundo huu ni muhimu katika kuboresha modeli kwa kazi maalum za sekta, ukitoa mchanganyiko wa ubora, gharama nafuu, na uelewa wa muktadha mrefu. Ni sehemu ya suite ya Azure AI, ikitoa uteuzi mpana wa modeli ambazo ni rahisi kupatikana, kujaribu, na kutumia, zikikidhi mahitaji ya ubinafsishaji wa sekta mbalimbali.

## WebGPU ni Nini  
WebGPU ni API ya kisasa ya picha za wavuti iliyoundwa kutoa ufikiaji wa ufanisi kwa kitengo cha usindikaji picha (GPU) moja kwa moja kutoka kwa vivinjari vya wavuti. Inakusudiwa kuwa mrithi wa WebGL, ikitoa maboresho kadhaa muhimu:

1. **Ulinganifu na GPU za Kisasa**: WebGPU imejengwa kufanya kazi kwa urahisi na miundo ya kisasa ya GPU, ikitumia API za mfumo kama Vulkan, Metal, na Direct3D 12.
2. **Utendaji Bora**: Inasaidia hesabu za GPU kwa matumizi ya jumla na operesheni za haraka, ikifanya iwe bora kwa uchoraji wa picha na kazi za kujifunza mashine.
3. **Sifa za Juu**: WebGPU hutoa ufikiaji wa uwezo wa juu wa GPU, kuwezesha picha na kazi za hesabu ngumu na zinazoendelea.
4. **Kupunguza Mzigo wa JavaScript**: Kwa kuhamisha kazi zaidi kwa GPU, WebGPU inapunguza kwa kiasi kikubwa mzigo wa JavaScript, na kusababisha utendaji bora na uzoefu laini zaidi.

WebGPU kwa sasa inaungwa mkono katika vivinjari kama Google Chrome, na kazi inaendelea kupanua msaada kwa majukwaa mengine.

### 03.WebGPU  
Mazingira Yanayohitajika:

**Vivinjari vinavyounga mkono:**  
- Google Chrome 113+  
- Microsoft Edge 113+  
- Safari 18 (macOS 15)  
- Firefox Nightly.

### Washa WebGPU:

- Katika Chrome/Microsoft Edge  

Washia bendera ya `chrome://flags/#enable-unsafe-webgpu`.

#### Fungua Kivinjari Chako:  
Anzisha Google Chrome au Microsoft Edge.

#### Fikia Ukurasa wa Bendera:  
Katika upau wa anwani, andika `chrome://flags` kisha bonyeza Enter.

#### Tafuta Bendera:  
Katika kisanduku cha utafutaji juu ya ukurasa, andika 'enable-unsafe-webgpu'

#### Washa Bendera:  
Tafuta bendera ya #enable-unsafe-webgpu katika orodha ya matokeo.

Bonyeza menyu ya kushuka kando yake na chagua Enabled.

#### Anzisha Upya Kivinjari Chako:  

Baada ya kuwasha bendera, utahitaji kuanzisha upya kivinjari chako ili mabadiliko yaanze kufanya kazi. Bonyeza kitufe cha Relaunch kinachoonekana chini ya ukurasa.

- Kwa Linux, anzisha kivinjari kwa kutumia `--enable-features=Vulkan`.  
- Safari 18 (macOS 15) ina WebGPU imewashwa kwa chaguo-msingi.  
- Katika Firefox Nightly, ingiza about:config katika upau wa anwani na `set dom.webgpu.enabled to true`.

### Kuweka GPU kwa Microsoft Edge  

Hapa kuna hatua za kuweka GPU yenye utendaji wa juu kwa Microsoft Edge kwenye Windows:

- **Fungua Mipangilio:** Bonyeza menyu ya Start na chagua Settings.  
- **Mipangilio ya Mfumo:** Nenda kwenye System kisha Display.  
- **Mipangilio ya Picha:** Teleza chini na bonyeza Graphics settings.  
- **Chagua Programu:** Chini ya “Choose an app to set preference,” chagua Desktop app kisha Browse.  
- **Chagua Edge:** Nenda kwenye folda ya usakinishaji ya Edge (kawaida `C:\Program Files (x86)\Microsoft\Edge\Application`) na chagua `msedge.exe`.  
- **Weka Upendeleo:** Bonyeza Options, chagua High performance, kisha bonyeza Save.  
Hii itahakikisha Microsoft Edge inatumia GPU yako yenye utendaji wa juu kwa utendaji bora.  
- **Anzisha upya** kompyuta yako ili mipangilio hii ifanye kazi.

### Sampuli : Tafadhali [bonyeza kiungo hiki](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

**Kiarifu cha Msamaha**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatubebei dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.