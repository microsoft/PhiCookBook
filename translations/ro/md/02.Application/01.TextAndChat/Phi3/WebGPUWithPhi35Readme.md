<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b62864faf628eb07f5231d4885555198",
  "translation_date": "2025-05-09T19:00:14+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md",
  "language_code": "ro"
}
-->
# Phi-3.5-Instruct WebGPU RAG Chatbot

## Demo pentru prezentarea WebGPU și a modelului RAG

Modelul RAG cu Phi-3.5 Onnx Hosted folosește abordarea Retrieval-Augmented Generation, combinând puterea modelelor Phi-3.5 cu găzduirea ONNX pentru implementări AI eficiente. Acest model este esențial pentru ajustarea fină a modelelor pentru sarcini specifice domeniului, oferind un echilibru între calitate, costuri și înțelegerea contextului pe termen lung. Face parte din suita Azure AI, oferind o gamă largă de modele ușor de găsit, testat și utilizat, adaptate nevoilor de personalizare ale diverselor industrii.

## Ce este WebGPU  
WebGPU este o API modernă pentru grafică web, concepută pentru a oferi acces eficient la unitatea de procesare grafică (GPU) a dispozitivului direct din browserele web. Este destinat să fie succesorul WebGL, oferind mai multe îmbunătățiri importante:

1. **Compatibilitate cu GPU-urile moderne**: WebGPU este construit să funcționeze perfect cu arhitecturile GPU contemporane, folosind API-uri de sistem precum Vulkan, Metal și Direct3D 12.
2. **Performanță îmbunătățită**: Suportă calculul general pe GPU și operațiuni mai rapide, fiind potrivit atât pentru redarea grafică, cât și pentru sarcini de învățare automată.
3. **Funcții avansate**: WebGPU oferă acces la capabilități GPU mai complexe, permițând sarcini grafice și computaționale mai dinamice și sofisticate.
4. **Reducerea încărcării JavaScript**: Prin delegarea mai multor sarcini către GPU, WebGPU reduce semnificativ încărcarea pe JavaScript, conducând la performanțe mai bune și experiențe mai fluide.

WebGPU este în prezent suportat în browsere precum Google Chrome, iar lucrările continuă pentru extinderea suportului și pe alte platforme.

### 03.WebGPU  
Mediu necesar:

**Browsere suportate:**  
- Google Chrome 113+  
- Microsoft Edge 113+  
- Safari 18 (macOS 15)  
- Firefox Nightly.

### Activarea WebGPU:

- În Chrome/Microsoft Edge  

Activează flag-ul `chrome://flags/#enable-unsafe-webgpu`.

#### Deschide browserul:  
Lansează Google Chrome sau Microsoft Edge.

#### Accesează pagina cu flag-uri:  
În bara de adrese, tastează `chrome://flags` și apasă Enter.

#### Caută flag-ul:  
În caseta de căutare din partea de sus, scrie 'enable-unsafe-webgpu'

#### Activează flag-ul:  
Găsește flag-ul #enable-unsafe-webgpu în lista rezultatelor.

Dă click pe meniul derulant de lângă el și selectează Enabled.

#### Repornirea browserului:  

După activarea flag-ului, va trebui să repornești browserul pentru ca modificările să intre în vigoare. Apasă butonul Relaunch care apare în partea de jos a paginii.

- Pentru Linux, lansează browserul cu `--enable-features=Vulkan`.  
- Safari 18 (macOS 15) are WebGPU activat implicit.  
- În Firefox Nightly, introdu about:config în bara de adrese și `set dom.webgpu.enabled to true`.

### Configurarea GPU pentru Microsoft Edge  

Pașii pentru configurarea unui GPU cu performanță ridicată pentru Microsoft Edge pe Windows:

- **Deschide Setările:** Click pe meniul Start și selectează Settings.  
- **Setări Sistem:** Accesează System și apoi Display.  
- **Setări Grafice:** Derulează în jos și dă click pe Graphics settings.  
- **Alege aplicația:** Sub „Choose an app to set preference,” selectează Desktop app și apoi Browse.  
- **Selectează Edge:** Navighează la folderul de instalare Edge (de obicei `C:\Program Files (x86)\Microsoft\Edge\Application`) și selectează `msedge.exe`.  
- **Setează preferința:** Apasă pe Options, alege High performance și apoi Save.  
Aceasta va asigura că Microsoft Edge folosește GPU-ul de înaltă performanță pentru o experiență mai bună.  
- **Repornește** calculatorul pentru ca aceste setări să fie aplicate.

### Exemple : Te rog să [click aici](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

**Declinare a responsabilității**:  
Acest document a fost tradus folosind serviciul de traducere automată AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un traducător uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.