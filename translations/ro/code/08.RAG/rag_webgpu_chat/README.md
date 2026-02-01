Phi-3-mini WebGPU RAG Chatbot

## Demo pentru prezentarea WebGPU și a modelului RAG
Modelul RAG cu Phi-3 Onnx găzduit folosește abordarea Retrieval-Augmented Generation, combinând puterea modelelor Phi-3 cu găzduirea ONNX pentru implementări AI eficiente. Acest model este esențial pentru ajustarea fină a modelelor pentru sarcini specifice domeniului, oferind un echilibru între calitate, costuri reduse și înțelegerea contextului extins. Face parte din suita Azure AI, oferind o gamă largă de modele ușor de găsit, testat și utilizat, adaptate nevoilor de personalizare ale diferitelor industrii. Modelele Phi-3, inclusiv Phi-3-mini, Phi-3-small și Phi-3-medium, sunt disponibile în Catalogul de modele Azure AI și pot fi ajustate fin și implementate autonom sau prin platforme precum HuggingFace și ONNX, demonstrând angajamentul Microsoft pentru soluții AI accesibile și eficiente.

## Ce este WebGPU
WebGPU este o API modernă pentru grafică web, concepută pentru a oferi acces eficient la unitatea de procesare grafică (GPU) a dispozitivului direct din browserele web. Este destinat să fie succesorul WebGL, oferind mai multe îmbunătățiri cheie:

1. **Compatibilitate cu GPU-uri moderne**: WebGPU este construit pentru a funcționa perfect cu arhitecturi GPU contemporane, folosind API-uri de sistem precum Vulkan, Metal și Direct3D 12.
2. **Performanță îmbunătățită**: Suportă calcule GPU cu scop general și operațiuni mai rapide, fiind potrivit atât pentru redarea grafică, cât și pentru sarcini de învățare automată.
3. **Funcționalități avansate**: WebGPU oferă acces la capabilități GPU mai avansate, permițând sarcini grafice și computaționale mai complexe și dinamice.
4. **Reducerea încărcării JavaScript**: Prin delegarea mai multor sarcini către GPU, WebGPU reduce semnificativ încărcarea pe JavaScript, conducând la performanțe mai bune și experiențe mai fluide.

WebGPU este în prezent suportat în browsere precum Google Chrome, iar lucrările continuă pentru extinderea suportului pe alte platforme.

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

#### Accesează pagina Flags:
În bara de adrese, tastează `chrome://flags` și apasă Enter.

#### Caută flag-ul:
În caseta de căutare din partea de sus, tastează 'enable-unsafe-webgpu'

#### Activează flag-ul:
Găsește flag-ul #enable-unsafe-webgpu în lista rezultatelor.

Dă clic pe meniul derulant de lângă el și selectează Enabled.

#### Repornește browserul:

După activarea flag-ului, va trebui să repornești browserul pentru ca modificările să intre în vigoare. Apasă butonul Relaunch care apare în partea de jos a paginii.

- Pentru Linux, lansează browserul cu `--enable-features=Vulkan`.
- Safari 18 (macOS 15) are WebGPU activat implicit.
- În Firefox Nightly, tastează about:config în bara de adrese și setează `dom.webgpu.enabled` pe true.

### Configurarea GPU pentru Microsoft Edge

Iată pașii pentru a configura un GPU de înaltă performanță pentru Microsoft Edge pe Windows:

- **Deschide Setările:** Apasă pe meniul Start și selectează Setări.
- **Setări sistem:** Mergi la Sistem, apoi la Afișaj.
- **Setări grafice:** Derulează în jos și apasă pe Setări grafice.
- **Alege aplicația:** Sub „Alege o aplicație pentru a seta preferința,” selectează Aplicație desktop și apoi Răsfoiește.
- **Selectează Edge:** Navighează la folderul de instalare Edge (de obicei `C:\Program Files (x86)\Microsoft\Edge\Application`) și selectează `msedge.exe`.
- **Setează preferința:** Apasă pe Opțiuni, alege Performanță înaltă și apoi apasă pe Salvează.  
Aceasta va asigura că Microsoft Edge folosește GPU-ul de înaltă performanță pentru o performanță mai bună.  
- **Repornește** calculatorul pentru ca setările să intre în vigoare.

### Deschide Codespace-ul tău:
Navighează la depozitul tău de pe GitHub.  
Apasă pe butonul Code și selectează Open with Codespaces.

Dacă nu ai încă un Codespace, poți crea unul apăsând pe New codespace.

**Note** Instalarea mediului Node în codespace-ul tău  
Rularea unui demo npm dintr-un GitHub Codespace este o metodă excelentă de a testa și dezvolta proiectul tău. Iată un ghid pas cu pas pentru a începe:

### Configurează-ți mediul:
După ce Codespace-ul este deschis, asigură-te că ai instalat Node.js și npm. Poți verifica rulând:  
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
Folosește terminalul pentru a ajunge în directorul unde se află proiectul tău npm:  
```
cd path/to/your/project
```

### Instalează dependențele:
Rulează comanda următoare pentru a instala toate dependențele necesare listate în fișierul package.json:  

```
npm install
```

### Rulează demo-ul:
După instalarea dependențelor, poți rula scriptul demo. Acesta este de obicei specificat în secțiunea scripts din package.json. De exemplu, dacă scriptul demo se numește start, poți rula:  

```
npm run build
```  
```
npm run dev
```

### Accesează demo-ul:
Dacă demo-ul implică un server web, Codespaces va oferi un URL pentru acces. Caută o notificare sau verifică fila Ports pentru a găsi URL-ul.

**Note:** Modelul trebuie să fie încărcat în cache-ul browserului, așa că poate dura puțin până se încarcă complet.

### Demo RAG
Încarcă fișierul markdown `intro_rag.md` pentru a completa soluția RAG. Dacă folosești codespaces, poți descărca fișierul din `01.InferencePhi3/docs/`

### Selectează fișierul:
Apasă pe butonul „Choose File” pentru a alege documentul pe care vrei să-l încarci.

### Încarcă documentul:
După ce ai selectat fișierul, apasă butonul „Upload” pentru a încărca documentul pentru RAG (Retrieval-Augmented Generation).

### Începe conversația:
Odată ce documentul este încărcat, poți începe o sesiune de chat folosind RAG bazat pe conținutul documentului tău.

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.