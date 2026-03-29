# **Utilizarea Phi-3 în Microsoft Foundry**

Odată cu dezvoltarea AI generativ, sperăm să utilizăm o platformă unificată pentru a gestiona diferite LLM și SLM, integrarea datelor enterprise, operațiuni de ajustare fină/RAG și evaluarea diferitelor business-uri enterprise după integrarea LLM și SLM, etc., astfel încât aplicațiile AI generative Smart să fie mai bine implementate. [Microsoft Foundry](https://ai.azure.com) este o platformă de aplicații AI generative la nivel enterprise.

![aistudo](../../../../translated_images/ro/aifoundry_home.f28a8127c96c7d93.webp)

Cu Microsoft Foundry, puteți evalua răspunsurile modelelor de limbaj mare (LLM) și orchestra componentele aplicației prompt prin prompt flow pentru performanțe mai bune. Platforma facilitează scalabilitatea pentru transformarea prototipurilor de concept în producție deplină cu ușurință. Monitorizarea continuă și rafinarea susțin succesul pe termen lung.

Putem desfășura rapid modelul Phi-3 pe Microsoft Foundry prin pași simpli și apoi folosi Microsoft Foundry pentru a finaliza lucrări legate de Phi-3 precum Playground/Chat, Fine-tuning, evaluare și altele.

## **1. Pregătire**

Dacă aveți deja instalat [Azure Developer CLI](https://learn.microsoft.com/azure/developer/azure-developer-cli/overview?WT.mc_id=aiml-138114-kinfeylo) pe mașina dvs., utilizarea acestui șablon este la fel de simplă ca rularea acestei comenzi într-un director nou.

## Creare manuală

Crearea unui proiect și a unui hub în Microsoft Foundry este o modalitate excelentă de a organiza și gestiona munca dvs. AI. Iată un ghid pas cu pas pentru a începe:

### Crearea unui proiect în Microsoft Foundry

1. **Accesați Microsoft Foundry**: Autentificați-vă în portalul Microsoft Foundry.
2. **Creați un proiect**:
   - Dacă sunteți într-un proiect, selectați „Microsoft Foundry” în partea stângă sus a paginii pentru a merge la pagina de Start.
   - Selectați „+ Create project”.
   - Introduceți un nume pentru proiect.
   - Dacă aveți un hub, acesta va fi selectat implicit. Dacă aveți acces la mai multe hub-uri, puteți selecta unul diferit din meniul derulant. Dacă doriți să creați un hub nou, selectați „Create new hub” și introduceți un nume.
   - Selectați „Create”.

### Crearea unui hub în Microsoft Foundry

1. **Accesați Microsoft Foundry**: Autentificați-vă cu contul dvs. Azure.
2. **Creați un hub**:
   - Selectați centrul de Management din meniul stâng.
   - Selectați „All resources”, apoi săgeata în jos de lângă „+ New project” și selectați „+ New hub”.
   - În dialogul „Create a new hub”, introduceți un nume pentru hub-ul dvs. (de exemplu, contoso-hub) și modificați celelalte câmpuri după dorință.
   - Selectați „Next”, revizuiți informațiile și apoi selectați „Create”.

Pentru instrucțiuni mai detaliate, puteți consulta documentația oficială [Microsoft](https://learn.microsoft.com/azure/ai-studio/how-to/create-projects).

După crearea cu succes, puteți accesa studioul creat prin [ai.azure.com](https://ai.azure.com/)

Pot exista mai multe proiecte într-un singur AI Foundry. Creați un proiect în AI Foundry pentru pregătire.

Creați Microsoft Foundry [QuickStarts](https://learn.microsoft.com/azure/ai-studio/quickstarts/get-started-code)


## **2. Desfășurarea unui model Phi în Microsoft Foundry**

Faceți clic pe opțiunea Explore a proiectului pentru a intra în Catalogul de modele și selectați Phi-3

Selectați Phi-3-mini-4k-instruct

Faceți clic pe „Deploy” pentru a desfășura modelul Phi-3-mini-4k-instruct

> [!NOTE]
>
> Puteți selecta puterea de calcul la desfășurare

## **3. Playground Chat Phi în Microsoft Foundry**

Mergeți la pagina de desfășurare, selectați Playground și discutați cu Phi-3 din Microsoft Foundry

## **4. Desfășurarea modelului din Microsoft Foundry**

Pentru a desfășura un model din Catalogul de modele Azure, puteți urma acești pași:

- Autentificați-vă în Microsoft Foundry.
- Alegeți modelul pe care doriți să îl desfășurați din catalogul de modele Microsoft Foundry.
- Pe pagina Detalii a modelului, selectați Deploy, apoi selectați Serverless API cu Azure AI Content Safety.
- Selectați proiectul în care doriți să desfășurați modelele. Pentru a folosi oferta Serverless API, spațiul dvs. de lucru trebuie să aparțină regiunii East US 2 sau Sweden Central. Puteți personaliza numele desfășurării.
- În expertul de desfășurare, selectați Prețuri și termeni pentru a afla despre prețuri și termeni de utilizare.
- Selectați Deploy. Așteptați până când desfășurarea este gata și veți fi redirecționat către pagina Desfășurări.
- Selectați Open in playground pentru a începe interacțiunea cu modelul.
- Puteți reveni la pagina Desfășurări, selectați desfășurarea și notați URL-ul Țintă și cheia secretă, pe care le puteți folosi pentru a apela desfășurarea și a genera completări.
- Puteți găsi întotdeauna detaliile punctului final, URL-ul și cheile de acces navigând la tab-ul Build și selectând Desfășurări din secțiunea Componente.

> [!NOTE]
> Vă rugăm să rețineți că contul dvs. trebuie să aibă permisiunile rolului Azure AI Developer pe Grupul de Resurse pentru a realiza acești pași.

## **5. Utilizarea API-ului Phi în Microsoft Foundry**

Puteți accesa https://{Your project name}.region.inference.ml.azure.com/swagger.json prin GET în Postman și îl puteți combina cu cheia pentru a afla despre interfețele puse la dispoziție

Puteți obține foarte convenabil parametrii de solicitare, precum și parametrii de răspuns.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autoritară. Pentru informații critice, este recomandată traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru orice neînțelegeri sau interpretări greșite care rezultă din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->