# **Construiește-ți propriul Visual Studio Code GitHub Copilot Chat cu familia Microsoft Phi-3**

Ai folosit agentul pentru spațiul de lucru în GitHub Copilot Chat? Vrei să-ți construiești propriul agent de cod pentru echipa ta? Acest laborator practic speră să combine modelul open source pentru a construi un agent de cod pentru afaceri la nivel enterprise.

## **Fundament**

### **De ce să alegi Microsoft Phi-3**

Phi-3 este o serie de familii, incluzând phi-3-mini, phi-3-small și phi-3-medium bazate pe diferiți parametri de antrenament pentru generarea de text, completarea dialogurilor și generarea de cod. Există și phi-3-vision bazat pe Vision. Este potrivit pentru întreprinderi sau echipe diferite pentru a crea soluții generative AI offline.

Se recomandă lectura acestui link [https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md](https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md)

### **Microsoft GitHub Copilot Chat**

Extensia GitHub Copilot Chat îți oferă o interfață de chat care îți permite să interacționezi cu GitHub Copilot și să primești răspunsuri la întrebări legate de programare direct în VS Code, fără a fi nevoie să navighezi prin documentație sau să cauți pe forumuri online.

Copilot Chat poate folosi evidențierea sintaxei, indentarea și alte caracteristici de formatare pentru a adăuga claritate răspunsului generat. În funcție de tipul întrebării utilizatorului, rezultatul poate conține linkuri către contextul folosit de Copilot pentru generarea răspunsului, cum ar fi fișiere de cod sursă sau documentație, sau butoane pentru accesarea funcționalităților VS Code.

- Copilot Chat se integrează în fluxul tău de dezvoltator și îți oferă asistență acolo unde ai nevoie:

- Începe o conversație de chat inline direct din editor sau terminal pentru ajutor în timp ce scrii cod

- Folosește vizualizarea Chat pentru a avea un asistent AI alături pentru a te ajuta oricând

- Pornește Quick Chat pentru a pune o întrebare rapidă și a reveni la ceea ce faci

Poți folosi GitHub Copilot Chat în diverse scenarii, cum ar fi:

- Răspunsuri la întrebări despre programare privind cea mai bună soluție la o problemă

- Explicarea codului altcuiva și sugestii de îmbunătățire

- Propuneri de corecturi pentru cod

- Generarea de cazuri de testare unitare

- Generarea de documentație pentru cod

Se recomandă lectura acestui link [https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/copilot-chat?WT.mc_id=aiml-137032-kinfeylo)


###  **Microsoft GitHub Copilot Chat @workspace**

Referința **@workspace** în Copilot Chat îți permite să pui întrebări despre întregul tău cod sursă. În funcție de întrebare, Copilot caută inteligent fișiere și simboluri relevante, pe care le referențiază în răspunsul său ca linkuri și exemple de cod.

Pentru a răspunde la întrebarea ta, **@workspace** caută prin aceleași surse pe care le-ar folosi un dezvoltator navigând un cod sursă în VS Code:

- Toate fișierele din spațiul de lucru, cu excepția fișierelor ignorate de fișierul .gitignore

- Structura directoarelor cu foldere și fișiere imbricate

- Indexul de căutare de cod GitHub, dacă spațiul de lucru este un depozit GitHub și este indexat de căutarea de cod

- Simboluri și definiții din spațiul de lucru

- Textul selectat în prezent sau textul vizibil în editorul activ

Notă: .gitignore este ignorat dacă ai un fișier deschis sau ai text selectat în interiorul unui fișier ignorat.

Se recomandă lectura acestui link [[https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/workspace-context?WT.mc_id=aiml-137032-kinfeylo)]


## **Află mai multe despre acest Laborator**

GitHub Copilot a îmbunătățit considerable eficiența programării în întreprinderi, iar fiecare întreprindere speră să personalizeze funcțiile relevante ale GitHub Copilot. Multe întreprinderi au personalizat extensii similare cu GitHub Copilot bazate pe propriile lor scenarii de afaceri și modele open source. Pentru întreprinderi, extensiile personalizate sunt mai ușor de controlat, dar acest lucru afectează și experiența utilizatorului. Până la urmă, GitHub Copilot are funcții mai puternice în gestionarea scenariilor generale și profesionalismului. Dacă experiența poate fi menținută consecventă, ar fi mai bine să se personalizeze propria extensie a întreprinderii. GitHub Copilot Chat oferă API relevante pentru ca întreprinderile să extindă experiența în Chat. Menținerea unei experiențe consistente și având funcții personalizate reprezintă o experiență mai bună pentru utilizator.

Acest laborator folosește în principal modelul Phi-3 combinat cu NPU local și Azure hibrid pentru a construi un agent personalizat în GitHub Copilot Chat ***@PHI3*** pentru a asista dezvoltatorii din întreprindere să finalizeze generarea de cod ***(@PHI3 /gen)*** și generarea de cod bazată pe imagini ***(@PHI3 /img)***.

![PHI3](../../../../../../../translated_images/ro/cover.1017ebc9a7c46d09.webp)

### ***Notă:***

Acest laborator este implementat în prezent în AIPC pe procesor Intel și Apple Silicon. Vom continua să actualizăm versiunea Qualcomm a NPU.


## **Laborator**


| Nume | Descriere | AIPC | Apple |
| ------------ | ----------- | -------- |-------- |
| Lab0 - Instalări(✅) | Configurează și instalează mediile și uneltele necesare | [Go](./HOL/AIPC/01.Installations.md) |[Go](./HOL/Apple/01.Installations.md) |
| Lab1 - Rulează fluxul Prompt cu Phi-3-mini (✅) | Combinat cu AIPC / Apple Silicon, folosind NPU local pentru a crea generare de cod prin Phi-3-mini | [Go](./HOL/AIPC/02.PromptflowWithNPU.md) |  [Go](./HOL/Apple/02.PromptflowWithMLX.md) |
| Lab2 - Desfășoară Phi-3-vision pe Azure Machine Learning Service(✅) | Generează cod prin desfășurarea Catalogului de Modele Azure Machine Learning Service - imagine Phi-3-vision | [Go](./HOL/AIPC/03.DeployPhi3VisionOnAzure.md) |[Go](./HOL/Apple/03.DeployPhi3VisionOnAzure.md) |
| Lab3 - Creează un agent @phi-3 în GitHub Copilot Chat(✅)  | Creează un agent personalizat Phi-3 în GitHub Copilot Chat pentru a completa generarea de cod, generarea de cod grafic, RAG, etc. | [Go](./HOL/AIPC/04.CreatePhi3AgentInVSCode.md) | [Go](./HOL/Apple/04.CreatePhi3AgentInVSCode.md) |
| Cod Exemplu (✅)  | Descarcă codul exemplu | [Go](../../../../../../../code/07.Lab/01/AIPC) | [Go](../../../../../../../code/07.Lab/01/Apple) |


## **Resurse**

1. Phi-3 Cookbook [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook)

2. Află mai multe despre GitHub Copilot [https://learn.microsoft.com/training/paths/copilot/](https://learn.microsoft.com/training/paths/copilot/?WT.mc_id=aiml-137032-kinfeylo)

3. Află mai multe despre GitHub Copilot Chat [https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/](https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/?WT.mc_id=aiml-137032-kinfeylo)

4. Află mai multe despre GitHub Copilot Chat API [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat?WT.mc_id=aiml-137032-kinfeylo)

5. Află mai multe despre Microsoft Foundry [https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/](https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/?WT.mc_id=aiml-137032-kinfeylo)

6. Află mai multe despre Catalogul de Modele Microsoft Foundry [https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite ce pot apărea în urma utilizării acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->