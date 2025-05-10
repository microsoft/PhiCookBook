<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4aac6b8a5dcbbe9a32b47be30340cac2",
  "translation_date": "2025-05-09T05:21:52+00:00",
  "source_file": "code/08.RAG/rag_webgpu_chat/README.md",
  "language_code": "sw"
}
-->
Phi-3-mini WebGPU RAG Chatbot

## Demo ya kuonyesha WebGPU na Mfumo wa RAG  
Mfumo wa RAG unaotumia modeli ya Phi-3 Onnx Iliyohifadhiwa unatumia mbinu ya Retrieval-Augmented Generation, ikichanganya nguvu za modeli za Phi-3 na uendeshaji wa ONNX kwa ufanisi wa AI. Mfumo huu ni muhimu katika kurekebisha modeli kwa kazi maalum za sekta, ukitoa mchanganyiko wa ubora, gharama nafuu, na uelewa wa muktadha mrefu. Ni sehemu ya Azure AI, ikitoa uteuzi mpana wa modeli zinazopatikana kwa urahisi, kujaribiwa, na kutumika, zikizingatia mahitaji ya ubinafsishaji ya sekta mbalimbali. Modeli za Phi-3, ikiwa ni pamoja na Phi-3-mini, Phi-3-small, na Phi-3-medium, zinapatikana kwenye Azure AI Model Catalog na zinaweza kurekebishwa na kuendeshwa kwa usimamizi wa kibinafsi au kupitia majukwaa kama HuggingFace na ONNX, zikionyesha dhamira ya Microsoft katika suluhisho za AI zinazopatikana na zenye ufanisi.

## WebGPU ni Nini  
WebGPU ni API ya kisasa ya picha za wavuti iliyoundwa kutoa ufikiaji wa ufanisi wa kitengo cha kuchakata picha (GPU) moja kwa moja kutoka kwa vivinjari vya wavuti. Inakusudiwa kuwa mbadala wa WebGL, ikitoa maboresho kadhaa muhimu:

1. **Ulinganifu na GPU za Kisasa**: WebGPU imejengwa ili kufanya kazi vizuri na usanifu wa GPU wa kisasa, ikitumia API za mfumo kama Vulkan, Metal, na Direct3D 12.  
2. **Ufanisi Bora**: Inasaidia hesabu za GPU za matumizi mbalimbali na shughuli za haraka, ikifanya iwe nzuri kwa uchoraji picha na kazi za kujifunza mashine.  
3. **Vipengele vya Juu**: WebGPU inatoa ufikiaji wa uwezo zaidi wa GPU, kuruhusu picha na kazi za hesabu kuwa za changamano zaidi na za mabadiliko.  
4. **Kupunguza Kazi ya JavaScript**: Kwa kuhamisha kazi zaidi kwa GPU, WebGPU inapunguza sana mzigo wa JavaScript, na kusababisha utendaji bora na uzoefu laini.

WebGPU kwa sasa inaungwa mkono katika vivinjari kama Google Chrome, na kazi inaendelea kupanua msaada kwa majukwaa mengine.

### 03.WebGPU  
Mazingira Yanayohitajika:

**Vivinjari Vinavyoungwa Mkono:**  
- Google Chrome 113+  
- Microsoft Edge 113+  
- Safari 18 (macOS 15)  
- Firefox Nightly.

### Weka WebGPU Kazi:

- Katika Chrome/Microsoft Edge  

Washa bendera ya `chrome://flags/#enable-unsafe-webgpu`.

#### Fungua Kivinjari Chako:  
Anzisha Google Chrome au Microsoft Edge.

#### Nenda Ukurasa wa Bendera:  
Katika sehemu ya anwani, andika `chrome://flags` kisha bonyeza Enter.

#### Tafuta Bendera:  
Katika kisanduku cha utafutaji juu ya ukurasa, andika 'enable-unsafe-webgpu'.

#### Washa Bendera:  
Tafuta bendera #enable-unsafe-webgpu kwenye orodha ya matokeo.

Bonyeza menyu ya kushuka kando yake na chagua Enabled.

#### Anzisha Upya Kivinjari Chako:  

Baada ya kuwasha bendera, utahitaji kuanzisha upya kivinjari chako ili mabadiliko yafanyike kazi. Bonyeza kitufe cha Relaunch kinachoonekana chini ya ukurasa.

- Kwa Linux, anzisha kivinjari kwa kutumia `--enable-features=Vulkan`.  
- Safari 18 (macOS 15) ina WebGPU imewashwa kwa chaguo-msingi.  
- Katika Firefox Nightly, ingiza about:config kwenye sehemu ya anwani na `set dom.webgpu.enabled to true`.

### Kuweka GPU kwa Microsoft Edge  

Hapa ni hatua za kuweka GPU yenye utendaji wa juu kwa Microsoft Edge kwenye Windows:

- **Fungua Mipangilio:** Bonyeza menyu ya Start na chagua Settings.  
- **Mipangilio ya Mfumo:** Nenda kwenye System kisha Display.  
- **Mipangilio ya Picha:** Shuka chini na bonyeza Graphics settings.  
- **Chagua Programu:** Chini ya “Choose an app to set preference,” chagua Desktop app kisha Browse.  
- **Chagua Edge:** Nenda kwenye folda ya usakinishaji ya Edge (kwa kawaida `C:\Program Files (x86)\Microsoft\Edge\Application`) na chagua `msedge.exe`.  
- **Weka Mapendeleo:** Bonyeza Options, chagua High performance, kisha bonyeza Save.  
Hii itahakikisha Microsoft Edge inatumia GPU yako yenye utendaji wa juu kwa utendaji bora.  
- **Anzisha upya** kompyuta yako ili mipangilio hii ifanye kazi.

### Fungua Codespace Yako:  
Nenda kwenye hazina yako GitHub.  
Bonyeza kitufe cha Code kisha chagua Open with Codespaces.

Kama bado huna Codespace, unaweza kuunda moja kwa kubonyeza New codespace.

**Note** Kuweka Mazingira ya Node katika codespace yako  
Kukimbia demo ya npm kutoka GitHub Codespace ni njia nzuri ya kujaribu na kuendeleza mradi wako. Hapa kuna mwongozo wa hatua kwa hatua kukusaidia kuanza:

### Weka Mazingira Yako:  
Mara codespace yako itakapo funguliwa, hakikisha una Node.js na npm vimewekwa. Unaweza kuangalia kwa kukimbia:  
```
node -v
```  
```
npm -v
```

Kama hazijawekwa, unaweza kuzisakinisha kwa kutumia:  
```
sudo apt-get update
```  
```
sudo apt-get install nodejs npm
```

### Nenda kwenye Folda ya Mradi Wako:  
Tumia terminal kuingia kwenye folda ambayo mradi wako wa npm uko:  
```
cd path/to/your/project
```

### Sakinisha Mategemeo:  
Kimbia amri ifuatayo kusakinisha mategemeo yote muhimu yaliyoorodheshwa kwenye faili yako package.json:

```
npm install
```

### Endesha Demo:  
Mara mategemeo yamesakinishwa, unaweza kuendesha script ya demo. Hii kawaida huwekwa katika sehemu ya scripts ya package.json. Kwa mfano, kama script yako ya demo inaitwa start, unaweza kuendesha:

```
npm run build
```  
```
npm run dev
```

### Pata Demo:  
Kama demo yako inahusisha seva ya wavuti, Codespaces itatoa URL ya kuifikia. Tafuta arifa au angalia kichupo cha Ports kupata URL hiyo.

**Note:** Modeli inahitaji kuhifadhiwa kwenye kivinjari, hivyo inaweza kuchukua muda kuipakia.

### Demo ya RAG  
Pakia faili ya markdown `intro_rag.md` to complete the RAG solution. If using codespaces you can download the file located in `01.InferencePhi3/docs/`

### Chagua Faili Yako:  
Bonyeza kitufe kinachosema “Choose File” kuchagua hati unayotaka kupakia.

### Pakia Hati:  
Baada ya kuchagua faili yako, bonyeza kitufe cha “Upload” kupakia hati yako kwa ajili ya RAG (Retrieval-Augmented Generation).

### Anza Mazungumzo Yako:  
Mara hati itakapopakuliwa, unaweza kuanza kikao cha mazungumzo ukitumia RAG kulingana na maudhui ya hati yako.

**Hati ya Kutojulikana**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuwa sahihi, tafadhali fahamu kwamba tafsiri za moja kwa moja zinaweza kuwa na makosa au upungufu wa usahihi. Hati asili katika lugha yake ya asili inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na watu inashauriwa. Hatuna dhamana kwa kutafsiri vibaya au kutoelewana kunakotokana na matumizi ya tafsiri hii.