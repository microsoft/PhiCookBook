# Ajustarea fină a Phi-3 cu Microsoft Foundry

 Să explorăm cum să ajustăm fin modelul de limbaj Phi-3 Mini Microsoft folosind Microsoft Foundry. Ajustarea fină vă permite să adaptați Phi-3 Mini pentru sarcini specifice, făcându-l și mai puternic și conștient de context.

## Considerații

- **Capabilități:** Care modele pot fi ajustate fin? La ce poate fi ajustat fin modelul de bază?
- **Cost:** Care este modelul de preț pentru ajustarea fină
**Personalizare:** Cât de mult pot modifica modelul de bază – și în ce moduri?
- **Conveniență:** Cum se realizează de fapt ajustarea fină – trebuie să scriu cod personalizat? Trebuie să aduc propriile resurse de calcul?
- **Siguranță:** Modelele ajustate fin sunt cunoscute pentru riscurile de siguranță – există vreun sistem de protecție pentru a preveni daunele neintenționate?

![AIFoundry Models](../../../../translated_images/ro/AIFoundryModels.0e1b16f7d0b09b73.webp)

## Pregătirea pentru ajustarea fină

### Precondiții

> [!NOTE]
> Pentru modelele din familia Phi-3, oferta de ajustare fină pay-as-you-go este disponibilă doar pentru hub-urile create în regiunile **East US 2**.

- Un abonament Azure. Dacă nu aveți un abonament Azure, creați un [cont Azure plătit](https://azure.microsoft.com/pricing/purchase-options/pay-as-you-go) pentru a începe.

- Un [proiect AI Foundry](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo).
- Controlele de acces bazate pe roluri Azure (Azure RBAC) sunt utilizate pentru a acorda acces la operațiuni în Microsoft Foundry. Pentru a efectua pașii din acest articol, contul dvs. de utilizator trebuie să aibă rolul __Azure AI Developer__ alocat pe grupul de resurse.

### Înregistrarea furnizorului de abonament

Verificați dacă abonamentul este înregistrat la furnizorul de resurse `Microsoft.Network`.

1. Conectați-vă la [portalul Azure](https://portal.azure.com).
1. Selectați **Subscriptions** din meniul din stânga.
1. Selectați abonamentul pe care doriți să-l utilizați.
1. Selectați **AI project settings** > **Resource providers** din meniul din stânga.
1. Confirmați că **Microsoft.Network** se află în lista furnizorilor de resurse. Dacă nu, adăugați-l.

### Pregătirea datelor

Pregătiți datele de antrenament și validare pentru a ajusta fin modelul. Seturile dvs. de date de antrenament și validare constau în exemple de intrare și ieșire pentru modul în care doriți ca modelul să funcționeze.

Asigurați-vă că toate exemplele dvs. de antrenament respectă formatul așteptat pentru inferență. Pentru ajustarea eficientă a modelelor, asigurați un set de date echilibrat și diversificat.

Aceasta implică menținerea echilibrului datelor, includerea mai multor scenarii și rafinarea periodică a datelor de antrenament pentru a alinia așteptările la lumea reală, conducând în cele din urmă la răspunsuri mai precise și echilibrate ale modelului.

Tipurile de model diferă în ceea ce privește formatul datelor de antrenament necesar.

### Completare chat

Datele de antrenament și validare pe care le folosiți **trebuie** să fie formate ca un document JSON Lines (JSONL). Pentru `Phi-3-mini-128k-instruct`, setul de date pentru ajustarea fină trebuie formatat în formatul conversațional folosit de API-ul Chat completions.

### Exemplu de format de fișier

```json
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Is Xbox better than PlayStation?"}, {"role": "assistant", "content": "I apologize, but I cannot provide personal opinions. My primary job is to assist you with any issues related to your Xbox device. Do you have any Xbox-related issues that need addressing?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Can I play PC games on my Xbox?"}, {"role": "assistant", "content": "While Xbox consoles don't natively support PC games, they can play an array of Xbox games, many of which are also available on PC. Can I assist you with finding games compatible with your Xbox device?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "I'm having trouble connecting my Xbox to the Wi-Fi."}, {"role": "assistant", "content": "No worries, let's go through the network settings on your Xbox. Can you please tell me what happens when you try to connect it to the Wi-Fi?"}]}
```

Tipul de fișier acceptat este JSON Lines. Fișierele sunt încărcate în depozitul de date implicit și devin disponibile în proiectul dvs.

## Ajustarea fină a Phi-3 cu Microsoft Foundry

Microsoft Foundry vă permite să personalizați modelele mari de limbaj pe seturile dvs. de date personale folosind un proces numit ajustare fină. Ajustarea fină oferă o valoare semnificativă prin activarea personalizării și optimizării pentru sarcini și aplicații specifice. Aceasta conduce la performanță îmbunătățită, eficiență a costurilor, latență redusă și rezultate adaptate.

![Finetune AI Foundry](../../../../translated_images/ro/AIFoundryfinetune.193aaddce48d553c.webp)

### Crearea unui proiect nou

1. Conectați-vă la [Microsoft Foundry](https://ai.azure.com).

1. Selectați **+New project** pentru a crea un proiect nou în Microsoft Foundry.

    ![FineTuneSelect](../../../../translated_images/ro/select-new-project.cd31c0404088d7a3.webp)

1. Efectuați următoarele sarcini:

    - Numele **Hub**-ului pentru proiect. Trebuie să fie o valoare unică.
    - Selectați **Hub**-ul pe care doriți să-l utilizați (creați unul nou dacă este necesar).

    ![FineTuneSelect](../../../../translated_images/ro/create-project.ca3b71298b90e420.webp)

1. Efectuați următoarele sarcini pentru a crea un hub nou:

    - Introduceți **Hub name**. Trebuie să fie o valoare unică.
    - Selectați **Subscription** Azure.
    - Selectați **Resource group** pe care doriți să-l utilizați (creați unul nou dacă este necesar).
    - Selectați **Location** pe care doriți să o utilizați.
    - Selectați **Connect Azure AI Services** pentru a utiliza (creați unul nou dacă este necesar).
    - Selectați **Connect Azure AI Search** la **Skip connecting**.

    ![FineTuneSelect](../../../../translated_images/ro/create-hub.49e53d235e80779e.webp)

1. Selectați **Next**.
1. Selectați **Create a project**.

### Pregătirea datelor

Înainte de ajustarea fină, colectați sau creați un set de date relevant pentru sarcina dvs., cum ar fi instrucțiuni de chat, perechi întrebare-răspuns sau alte date text pertinente. Curățați și preprocesați aceste date eliminând zgomotul, gestionând valorile lipsă și tokenizând textul.

### Ajustarea fină a modelelor Phi-3 în Microsoft Foundry

> [!NOTE]
> Ajustarea fină a modelelor Phi-3 este susținută în prezent doar în proiectele localizate în East US 2.

1. Selectați **Model catalog** din fila din stânga.

1. Tastați *phi-3* în **bara de căutare** și selectați modelul phi-3 pe care doriți să îl utilizați.

    ![FineTuneSelect](../../../../translated_images/ro/select-model.60ef2d4a6a3cec57.webp)

1. Selectați **Fine-tune**.

    ![FineTuneSelect](../../../../translated_images/ro/select-finetune.a976213b543dd9d8.webp)

1. Introduceți **Numele modelului ajustat fin**.

    ![FineTuneSelect](../../../../translated_images/ro/finetune1.c2b39463f0d34148.webp)

1. Selectați **Next**.

1. Efectuați următoarele sarcini:

    - Selectați **task type** la **Chat completion**.
    - Selectați **Training data** pe care doriți să o folosiți. O puteți încărca prin datele Microsoft Foundry sau din mediul local.

    ![FineTuneSelect](../../../../translated_images/ro/finetune2.43cb099b1a94442d.webp)

1. Selectați **Next**.

1. Încărcați **Validation data** pe care doriți să o folosiți sau puteți selecta **Automatic split of training data**.

    ![FineTuneSelect](../../../../translated_images/ro/finetune3.fd96121b67dcdd92.webp)

1. Selectați **Next**.

1. Efectuați următoarele sarcini:

    - Selectați **Batch size multiplier** pe care doriți să-l utilizați.
    - Selectați **Learning rate** pe care doriți să-l utilizați.
    - Selectați **Epochs** pe care doriți să le utilizați.

    ![FineTuneSelect](../../../../translated_images/ro/finetune4.e18b80ffccb5834a.webp)

1. Selectați **Submit** pentru a începe procesul de ajustare fină.

    ![FineTuneSelect](../../../../translated_images/ro/select-submit.0a3802d581bac271.webp)


1. După ce modelul dvs. este ajustat fin, starea va fi afișată ca **Completed**, așa cum este ilustrat în imaginea de mai jos. Acum puteți implementa modelul și îl puteți utiliza în propria aplicație, în playground sau în prompt flow. Pentru mai multe informații, consultați [Cum să implementați familia de modele mici Phi-3 cu Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python).

    ![FineTuneSelect](../../../../translated_images/ro/completed.4dc8d2357144cdef.webp)

> [!NOTE]
> Pentru informații mai detaliate despre ajustarea fină a Phi-3, vă rugăm să vizitați [Fine-tune Phi-3 models in Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/fine-tune-phi-3?tabs=phi-3-mini).

## Curățarea modelelor ajustate fin

Puteți șterge un model ajustat fin din lista de modele de ajustare din [Microsoft Foundry](https://ai.azure.com) sau din pagina de detalii a modelului. Selectați modelul ajustat fin pe care doriți să-l ștergeți din pagina Fine-tuning, apoi selectați butonul Delete pentru a șterge modelul ajustat fin.

> [!NOTE]
> Nu puteți șterge un model personalizat dacă are o implementare existentă. Trebuie să ștergeți mai întâi implementarea modelului înainte de a putea șterge modelul personalizat.

## Costuri și cote

### Considerații privind costul și cotele pentru modelele Phi-3 ajustate fin ca serviciu

Modelele Phi ajustate fin ca serviciu sunt oferite de Microsoft și integrate cu Microsoft Foundry pentru utilizare. Puteți găsi prețurile atunci când [implementați](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python) sau ajustați fin modelele în fila Pricing and terms din expertul de implementare.

## Filtrarea conținutului

Modelele implementate ca serviciu cu plată pe utilizare sunt protejate de Azure AI Content Safety. Când sunt implementate la endpoint-uri în timp real, puteți opta să dezactivați această capacitate. Cu Azure AI content safety activat, atât promptul, cât și completarea trec printr-un ansamblu de modele de clasificare menite să detecteze și să împiedice generarea de conținut dăunător. Sistemul de filtrare a conținutului detectează și ia măsuri asupra categoriilor specifice de conținut potențial dăunător în ambele prompturi de intrare și completări de ieșire. Aflați mai multe despre [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-studio/concepts/content-filtering).

**Configurația Ajustării Fine**

Hiperparametri: Definiți hiperparametri precum rata de învățare, dimensiunea batch-ului și numărul de epoci de antrenament.

**Funcția de pierdere**

Alegeți o funcție de pierdere potrivită pentru sarcina dvs. (de exemplu, cross-entropy).

**Optimizator**

Selectați un optimizator (de exemplu, Adam) pentru actualizările gradientului în timpul antrenamentului.

**Procesul de Ajustare Fină**

- Încarcă model pre-antrenat: Încarcă checkpoint-ul Phi-3 Mini.
- Adaugă straturi personalizate: Adaugă straturi specifice sarcinii (de exemplu, cap de clasificare pentru instrucțiuni de chat).

**Antrenează Modelul**  
Ajustați fin modelul folosind setul de date pregătit. Monitorizați progresul antrenamentului și ajustați hiperparametrii după necesitate.

**Evaluare și Validare**

Set de validare: Împărțiți datele în seturi de antrenament și validare.

**Evaluare performanță**

Folosiți metrici precum acuratețea, scorul F1 sau perplexitatea pentru a evalua performanța modelului.

## Salvează Modelul Ajustat Fin

**Checkpoint**  
Salvați checkpoint-ul modelului ajustat fin pentru uz viitor.

## Implementare

- Implementați ca serviciu web: Implementați modelul ajustat fin ca serviciu web în Microsoft Foundry.  
- Testați Endpoint-ul: Trimiteți interogări de test către endpoint-ul implementat pentru a verifica funcționalitatea.

## Iterați și Îmbunătățiți

Iterați: Dacă performanța nu este satisfăcătoare, iterați prin ajustarea hiperparametrilor, adăugarea mai multor date sau ajustarea pentru epoci suplimentare.

## Monitorizați și Rafinați

Monitorizați continuu comportamentul modelului și rafinați-l după necesitate.

## Personalizați și Extindeți

Sarcini personalizate: Phi-3 Mini poate fi ajustat fin pentru diverse sarcini dincolo de instrucțiunile de chat. Explorați alte cazuri de utilizare!  
Experimentați: Încercați diferite arhitecturi, combinații de straturi și tehnici pentru a îmbunătăți performanța.

> [!NOTE]
> Ajustarea fină este un proces iterativ. Experimentați, învățați și adaptați modelul pentru a obține cele mai bune rezultate pentru sarcina dvs. specifică!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru eventuale neînțelegeri sau interpretări greșite rezultând din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->