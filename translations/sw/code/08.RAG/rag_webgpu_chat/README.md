<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4aac6b8a5dcbbe9a32b47be30340cac2",
  "translation_date": "2025-07-16T17:20:24+00:00",
  "source_file": "code/08.RAG/rag_webgpu_chat/README.md",
  "language_code": "sw"
}
-->
Phi-3-mini WebGPU RAG Chatbot

## Demo ya kuonyesha WebGPU na Muundo wa RAG  
Muundo wa RAG unaotumia modeli ya Phi-3 Onnx iliyohostiwa unatumia mbinu ya Retrieval-Augmented Generation, ikichanganya nguvu za modeli za Phi-3 na uendeshaji wa ONNX kwa usambazaji wa AI wenye ufanisi. Muundo huu ni muhimu katika kuboresha modeli kwa kazi maalum za sekta, ukitoa mchanganyiko wa ubora, gharama nafuu, na uelewa wa muktadha mrefu. Ni sehemu ya Azure AI, ikitoa uteuzi mpana wa modeli ambazo ni rahisi kupatikana, kujaribiwa, na kutumika, zikikidhi mahitaji ya ubinafsishaji wa sekta mbalimbali. Modeli za Phi-3, ikiwa ni pamoja na Phi-3-mini, Phi-3-small, na Phi-3-medium, zinapatikana kwenye Azure AI Model Catalog na zinaweza kuboreshwa na kusambazwa kwa usimamizi wa mwenyewe au kupitia majukwaa kama HuggingFace na ONNX, zikionyesha dhamira ya Microsoft kwa suluhisho za AI zinazopatikana kwa urahisi na zenye ufanisi.

## WebGPU ni Nini  
WebGPU ni API ya kisasa ya picha za wavuti iliyoundwa kutoa ufikiaji wa ufanisi kwa kitengo cha usindikaji picha (GPU) cha kifaa moja kwa moja kutoka kwa vivinjari vya wavuti. Inakusudiwa kuwa mrithi wa WebGL, ikitoa maboresho kadhaa muhimu:

1. **Ulinganifu na GPU za Kisasa**: WebGPU imejengwa kufanya kazi kwa urahisi na usanifu wa GPU za kisasa, ikitumia API za mfumo kama Vulkan, Metal, na Direct3D 12.  
2. **Utendaji Bora**: Inasaidia hesabu za GPU kwa matumizi ya jumla na operesheni za haraka, ikifanya iwe bora kwa uchoraji picha na kazi za kujifunza mashine.  
3. **Sifa za Juu**: WebGPU inatoa ufikiaji wa uwezo wa juu wa GPU, kuwezesha picha na kazi za hesabu ngumu na zenye mabadiliko mengi.  
4. **Kupunguza Mzigo wa JavaScript**: Kwa kuhamisha kazi zaidi kwa GPU, WebGPU inapunguza kwa kiasi kikubwa mzigo wa JavaScript, na kusababisha utendaji bora na uzoefu laini zaidi.

WebGPU kwa sasa inasaidiwa katika vivinjari kama Google Chrome, na kazi inaendelea kupanua msaada kwa majukwaa mengine.

### 03.WebGPU  
Mazingira Yanayohitajika:

**Vivinjari vinavyosaidiwa:**  
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
Katika upau wa anwani, andika `chrome://flags` kisha bonyeza Enter.

#### Tafuta Bendera:  
Katika kisanduku cha utafutaji juu ya ukurasa, andika 'enable-unsafe-webgpu'

#### Washa Bendera:  
Tafuta bendera ya #enable-unsafe-webgpu kwenye orodha ya matokeo.

Bonyeza menyu ya kushuka kando yake na chagua Enabled.

#### Anzisha Kivinjari Chako Upya:  

Baada ya kuwasha bendera, utahitaji kuanzisha kivinjari chako upya ili mabadiliko yaanze kutumika. Bonyeza kitufe cha Relaunch kinachoonekana chini ya ukurasa.

- Kwa Linux, anzisha kivinjari kwa kutumia `--enable-features=Vulkan`.  
- Safari 18 (macOS 15) ina WebGPU imewashwa kwa chaguo-msingi.  
- Katika Firefox Nightly, ingiza about:config kwenye upau wa anwani na `set dom.webgpu.enabled to true`.

### Kuweka GPU kwa Microsoft Edge  

Hapa kuna hatua za kuweka GPU yenye utendaji wa juu kwa Microsoft Edge kwenye Windows:

- **Fungua Mipangilio:** Bonyeza menyu ya Start na chagua Settings.  
- **Mipangilio ya Mfumo:** Nenda kwenye System kisha Display.  
- **Mipangilio ya Picha:** Telezesha chini na bonyeza Graphics settings.  
- **Chagua Programu:** Chini ya “Choose an app to set preference,” chagua Desktop app kisha Browse.  
- **Chagua Edge:** Nenda kwenye folda ya usakinishaji ya Edge (kawaida `C:\Program Files (x86)\Microsoft\Edge\Application`) na chagua `msedge.exe`.  
- **Weka Upendeleo:** Bonyeza Options, chagua High performance, kisha bonyeza Save.  
Hii itahakikisha Microsoft Edge inatumia GPU yako yenye utendaji wa juu kwa utendaji bora.  
- **Anzisha upya** kompyuta yako ili mipangilio hii ianze kutumika.

### Fungua Codespace Yako:  
Nenda kwenye hazina yako GitHub.  
Bonyeza kitufe cha Code na chagua Open with Codespaces.

Kama bado huna Codespace, unaweza kuunda moja kwa kubonyeza New codespace.

**Note** Kuweka Mazingira ya Node katika codespace yako  
Kukimbia demo ya npm kutoka GitHub Codespace ni njia nzuri ya kujaribu na kuendeleza mradi wako. Hapa kuna mwongozo wa hatua kwa hatua kukusaidia kuanza:

### Weka Mazingira Yako:  
Mara Codespace yako itakapo funguliwa, hakikisha una Node.js na npm vimewekwa. Unaweza kuangalia kwa kukimbia:  
```
node -v
```  
```
npm -v
```

Kama havijawekwa, unaweza kuviweka kwa kutumia:  
```
sudo apt-get update
```  
```
sudo apt-get install nodejs npm
```

### Nenda kwenye Saraka ya Mradi Wako:  
Tumia terminal kuingia kwenye saraka ambapo mradi wako wa npm uko:  
```
cd path/to/your/project
```

### Sakinisha Mategemeo:  
Kimbia amri ifuatayo kusakinisha mategemeo yote muhimu yaliyotajwa katika faili yako package.json:  

```
npm install
```

### Endesha Demo:  
Mara mategemeo yatakapokuwa yamesakinishwa, unaweza kuendesha script ya demo yako. Hii kawaida hutajwa katika sehemu ya scripts ya package.json. Kwa mfano, kama script yako ya demo inaitwa start, unaweza kuendesha:  

```
npm run build
```  
```
npm run dev
```

### Pata Demo:  
Kama demo yako inahusisha seva ya wavuti, Codespaces itatoa URL ya kuifikia. Tafuta taarifa au angalia kichupo cha Ports kupata URL.

**Note:** Modeli inahitaji kuhifadhiwa katika kivinjari, hivyo inaweza kuchukua muda kupakia.

### Demo ya RAG  
Pakia faili la markdown `intro_rag.md` ili kukamilisha suluhisho la RAG. Ikiwa unatumia codespaces unaweza kupakua faili iliyoko katika `01.InferencePhi3/docs/`

### Chagua Faili Yako:  
Bonyeza kitufe kinachosema “Choose File” kuchagua hati unayotaka kupakia.

### Pakia Hati:  
Baada ya kuchagua faili lako, bonyeza kitufe cha “Upload” kupakia hati yako kwa RAG (Retrieval-Augmented Generation).

### Anza Mazungumzo Yako:  
Mara hati itakapopakuliwa, unaweza kuanza kikao cha mazungumzo ukitumia RAG kulingana na yaliyomo katika hati yako.

**Kiarifu cha Kutotegemea**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatubebei dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.