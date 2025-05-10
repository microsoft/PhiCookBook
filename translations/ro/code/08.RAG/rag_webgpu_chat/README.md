<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4aac6b8a5dcbbe9a32b47be30340cac2",
  "translation_date": "2025-05-09T05:23:03+00:00",
  "source_file": "code/08.RAG/rag_webgpu_chat/README.md",
  "language_code": "ro"
}
-->
Phi-3-mini WebGPU RAG Chatbot

## Demo pentru prezentarea WebGPU și a Pattern-ului RAG
Pattern-ul RAG cu modelul Phi-3 Onnx găzduit folosește abordarea Retrieval-Augmented Generation, combinând puterea modelelor Phi-3 cu găzduirea ONNX pentru implementări AI eficiente. Acest pattern este esențial pentru ajustarea fină a modelelor pentru sarcini specifice domeniului, oferind un echilibru între calitate, cost-eficiență și înțelegerea contextului extins. Face parte din suita Azure AI, oferind o gamă largă de modele ușor de găsit, testat și utilizat, adaptate nevoilor de personalizare ale diferitelor industrii. Modelele Phi-3, inclusiv Phi-3-mini, Phi-3-small și Phi-3-medium, sunt disponibile în Azure AI Model Catalog și pot fi ajustate fin și implementate fie autogestionat, fie prin platforme precum HuggingFace și ONNX, demonstrând angajamentul Microsoft pentru soluții AI accesibile și eficiente.

## Ce este WebGPU
WebGPU este o API modernă pentru grafică web, creată pentru a oferi acces eficient direct la unitatea de procesare grafică (GPU) a unui dispozitiv din browserele web. Este conceput să fie succesorul WebGL, oferind câteva îmbunătățiri cheie:

1. **Compatibilitate cu GPU-uri moderne**: WebGPU este construit să funcționeze perfect cu arhitecturile GPU contemporane, folosind API-uri de sistem precum Vulkan, Metal și Direct3D 12.
2. **Performanță îmbunătățită**: Suportă calcul general pe GPU și operațiuni mai rapide, fiind potrivit atât pentru redarea grafică, cât și pentru sarcini de machine learning.
3. **Funcționalități avansate**: WebGPU oferă acces la capabilități GPU mai complexe, permițând lucrări grafice și computaționale mai dinamice și sofisticate.
4. **Reducerea încărcării JavaScript**: Prin delegarea mai multor sarcini către GPU, WebGPU reduce semnificativ volumul de lucru al JavaScript, conducând la performanțe mai bune și experiențe mai fluide.

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
Pornește Google Chrome sau Microsoft Edge.

#### Accesează pagina Flags:
În bara de adrese, tastează `chrome://flags` și apasă Enter.

#### Caută flag-ul:
În caseta de căutare din partea de sus, scrie 'enable-unsafe-webgpu'

#### Activează flag-ul:
Găsește flag-ul #enable-unsafe-webgpu în lista de rezultate.

Dă clic pe meniul derulant de lângă el și selectează Enabled.

#### Repornește browserul:

După activarea flag-ului, trebuie să repornești browserul pentru ca modificările să intre în vigoare. Apasă butonul Relaunch care apare în partea de jos a paginii.

- Pentru Linux, pornește browserul cu `--enable-features=Vulkan`.  
- Safari 18 (macOS 15) are WebGPU activat implicit.  
- În Firefox Nightly, tastează about:config în bara de adrese și `set dom.webgpu.enabled to true`.

### Configurarea GPU pentru Microsoft Edge

Pașii pentru a configura un GPU de înaltă performanță pentru Microsoft Edge pe Windows:

- **Deschide Setările:** Dă clic pe meniul Start și selectează Settings.  
- **Setări sistem:** Accesează System, apoi Display.  
- **Setări grafice:** Derulează în jos și dă clic pe Graphics settings.  
- **Alege aplicația:** Sub „Choose an app to set preference”, selectează Desktop app și apoi Browse.  
- **Selectează Edge:** Navighează la folderul de instalare Edge (de obicei `C:\Program Files (x86)\Microsoft\Edge\Application`) și selectează `msedge.exe`.  
- **Setează preferința:** Dă clic pe Options, alege High performance, apoi apasă Save.  
Aceasta va asigura că Microsoft Edge folosește GPU-ul de înaltă performanță pentru o performanță mai bună.  
- **Repornește** calculatorul pentru ca setările să aibă efect.

### Deschide Codespace-ul:
Navighează la repository-ul tău pe GitHub.  
Dă clic pe butonul Code și selectează Open with Codespaces.

Dacă nu ai încă un Codespace, îl poți crea dând clic pe New codespace.

**Note** Instalarea mediului Node în codespace  
Rularea unui demo npm dintr-un GitHub Codespace este o metodă excelentă de a testa și dezvolta proiectul tău. Iată un ghid pas cu pas pentru a începe:

### Configurează-ți mediul:
După ce Codespace-ul este deschis, asigură-te că ai instalate Node.js și npm. Poți verifica rulând:  
```
node -v
```  
```
npm -v
```

Dacă nu sunt instalate, le poți instala folosind:  
```
sudo apt-get update
```  
```
sudo apt-get install nodejs npm
```

### Navighează la directorul proiectului:
Folosește terminalul pentru a merge în directorul unde se află proiectul tău npm:  
```
cd path/to/your/project
```

### Instalează dependențele:
Rulează comanda următoare pentru a instala toate dependențele necesare din fișierul package.json:  

```
npm install
```

### Rulează demo-ul:
După instalarea dependențelor, poți rula scriptul demo. De obicei, acesta este specificat în secțiunea scripts din package.json. De exemplu, dacă scriptul se numește start, rulează:  

```
npm run build
```  
```
npm run dev
```

### Accesează demo-ul:
Dacă demo-ul implică un server web, Codespaces îți va oferi un URL pentru acces. Verifică notificările sau fila Ports pentru a găsi URL-ul.

**Note:** Modelul trebuie să fie cache-uit în browser, deci încărcarea poate dura ceva timp.

### Demo RAG  
Încarcă fișierul markdown `intro_rag.md` to complete the RAG solution. If using codespaces you can download the file located in `01.InferencePhi3/docs/`

### Selectează fișierul:  
Dă clic pe butonul „Choose File” pentru a selecta documentul pe care vrei să-l încarci.

### Încarcă documentul:  
După ce ai ales fișierul, apasă butonul „Upload” pentru a încărca documentul pentru RAG (Retrieval-Augmented Generation).

### Începe chat-ul:  
După ce documentul este încărcat, poți începe o sesiune de chat folosind RAG bazat pe conținutul documentului.

**Declinare a responsabilității**:  
Acest document a fost tradus folosind serviciul de traducere automată AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original, în limba sa nativă, trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.