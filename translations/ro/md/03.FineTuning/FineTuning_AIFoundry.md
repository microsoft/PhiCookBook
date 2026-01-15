<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c1559c5af6caccf6f623fd43a6b3a9a3",
  "translation_date": "2025-07-17T06:13:20+00:00",
  "source_file": "md/03.FineTuning/FineTuning_AIFoundry.md",
  "language_code": "ro"
}
-->
# Ajustarea fină a Phi-3 cu Azure AI Foundry

Să explorăm cum să ajustăm fin modelul de limbaj Phi-3 Mini de la Microsoft folosind Azure AI Foundry. Ajustarea fină îți permite să adaptezi Phi-3 Mini pentru sarcini specifice, făcându-l și mai puternic și mai conștient de context.

## Considerații

- **Capabilități:** Care modele pot fi ajustate fin? Ce poate face modelul de bază după ajustare?
- **Cost:** Care este modelul de tarifare pentru ajustarea fină?
- **Personalizare:** Cât de mult pot modifica modelul de bază – și în ce moduri?
- **Confort:** Cum se realizează efectiv ajustarea fină – trebuie să scriu cod personalizat? Trebuie să aduc propriul meu sistem de calcul?
- **Siguranță:** Modelele ajustate fin pot prezenta riscuri de siguranță – există măsuri de protecție pentru a preveni daune neintenționate?

![AIFoundry Models](../../../../translated_images/ro/AIFoundryModels.0e1b16f7d0b09b73.png)

## Pregătirea pentru ajustarea fină

### Cerințe preliminare

> [!NOTE]
> Pentru modelele din familia Phi-3, oferta de ajustare fină în regim pay-as-you-go este disponibilă doar pentru hub-uri create în regiunile **East US 2**.

- Un abonament Azure. Dacă nu ai un abonament Azure, creează un [cont Azure plătit](https://azure.microsoft.com/pricing/purchase-options/pay-as-you-go) pentru a începe.

- Un [proiect AI Foundry](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo).
- Controlul accesului bazat pe roluri Azure (Azure RBAC) este folosit pentru a acorda acces la operațiuni în Azure AI Foundry. Pentru a efectua pașii din acest articol, contul tău de utilizator trebuie să aibă rolul __Azure AI Developer__ atribuit pe grupul de resurse.

### Înregistrarea furnizorului de abonament

Verifică dacă abonamentul este înregistrat la furnizorul de resurse `Microsoft.Network`.

1. Autentifică-te în [portalul Azure](https://portal.azure.com).
2. Selectează **Subscriptions** din meniul din stânga.
3. Alege abonamentul pe care vrei să-l folosești.
4. Selectează **AI project settings** > **Resource providers** din meniul din stânga.
5. Confirmă că **Microsoft.Network** este în lista furnizorilor de resurse. Dacă nu, adaugă-l.

### Pregătirea datelor

Pregătește datele de antrenament și validare pentru ajustarea fină a modelului. Seturile tale de date de antrenament și validare trebuie să conțină exemple de input și output care să reflecte modul în care dorești ca modelul să funcționeze.

Asigură-te că toate exemplele de antrenament respectă formatul așteptat pentru inferență. Pentru a ajusta fin modelele eficient, asigură un set de date echilibrat și divers.

Aceasta implică menținerea echilibrului datelor, includerea unor scenarii variate și rafinarea periodică a datelor de antrenament pentru a se alinia cu așteptările din lumea reală, ceea ce conduce la răspunsuri mai precise și echilibrate ale modelului.

Diferitele tipuri de modele necesită formate diferite pentru datele de antrenament.

### Chat Completion

Datele de antrenament și validare pe care le folosești **trebuie** să fie formatate ca un document JSON Lines (JSONL). Pentru `Phi-3-mini-128k-instruct`, setul de date pentru ajustare fină trebuie să fie în format conversațional, folosit de API-ul Chat completions.

### Exemplu de format al fișierului

```json
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Is Xbox better than PlayStation?"}, {"role": "assistant", "content": "I apologize, but I cannot provide personal opinions. My primary job is to assist you with any issues related to your Xbox device. Do you have any Xbox-related issues that need addressing?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Can I play PC games on my Xbox?"}, {"role": "assistant", "content": "While Xbox consoles don't natively support PC games, they can play an array of Xbox games, many of which are also available on PC. Can I assist you with finding games compatible with your Xbox device?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "I'm having trouble connecting my Xbox to the Wi-Fi."}, {"role": "assistant", "content": "No worries, let's go through the network settings on your Xbox. Can you please tell me what happens when you try to connect it to the Wi-Fi?"}]}
```

Tipul de fișier acceptat este JSON Lines. Fișierele sunt încărcate în depozitul de date implicit și puse la dispoziție în proiectul tău.

## Ajustarea fină a Phi-3 cu Azure AI Foundry

Azure AI Foundry îți permite să personalizezi modelele mari de limbaj pe baza propriilor seturi de date, folosind un proces numit ajustare fină. Ajustarea fină oferă valoare semnificativă prin personalizare și optimizare pentru sarcini și aplicații specifice. Aceasta conduce la performanțe îmbunătățite, eficiență a costurilor, latență redusă și rezultate adaptate.

![Finetune AI Foundry](../../../../translated_images/ro/AIFoundryfinetune.193aaddce48d553c.png)

### Crearea unui proiect nou

1. Autentifică-te în [Azure AI Foundry](https://ai.azure.com).

2. Selectează **+New project** pentru a crea un proiect nou în Azure AI Foundry.

    ![FineTuneSelect](../../../../translated_images/ro/select-new-project.cd31c0404088d7a3.png)

3. Efectuează următoarele:

    - Numele **Hub-ului** proiectului. Trebuie să fie o valoare unică.
    - Selectează **Hub-ul** pe care vrei să-l folosești (creează unul nou dacă este necesar).

    ![FineTuneSelect](../../../../translated_images/ro/create-project.ca3b71298b90e420.png)

4. Efectuează următorii pași pentru a crea un hub nou:

    - Introdu **Numele Hub-ului**. Trebuie să fie o valoare unică.
    - Selectează **Abonamentul** Azure.
    - Selectează **Grupul de resurse** pe care vrei să-l folosești (creează unul nou dacă este necesar).
    - Selectează **Locația** pe care dorești să o folosești.
    - Selectează **Connect Azure AI Services** pe care vrei să-l folosești (creează unul nou dacă este necesar).
    - Selectează **Connect Azure AI Search** și alege **Skip connecting**.

    ![FineTuneSelect](../../../../translated_images/ro/create-hub.49e53d235e80779e.png)

5. Selectează **Next**.
6. Selectează **Create a project**.

### Pregătirea datelor

Înainte de ajustarea fină, adună sau creează un set de date relevant pentru sarcina ta, cum ar fi instrucțiuni de chat, perechi întrebări-răspunsuri sau orice alt text relevant. Curăță și preprocesează aceste date eliminând zgomotul, gestionând valorile lipsă și tokenizând textul.

### Ajustarea fină a modelelor Phi-3 în Azure AI Foundry

> [!NOTE]
> Ajustarea fină a modelelor Phi-3 este în prezent suportată doar în proiectele localizate în East US 2.

1. Selectează **Model catalog** din tab-ul din stânga.

2. Tastează *phi-3* în **bara de căutare** și selectează modelul phi-3 pe care dorești să-l folosești.

    ![FineTuneSelect](../../../../translated_images/ro/select-model.60ef2d4a6a3cec57.png)

3. Selectează **Fine-tune**.

    ![FineTuneSelect](../../../../translated_images/ro/select-finetune.a976213b543dd9d8.png)

4. Introdu **Numele modelului ajustat fin**.

    ![FineTuneSelect](../../../../translated_images/ro/finetune1.c2b39463f0d34148.png)

5. Selectează **Next**.

6. Efectuează următoarele:

    - Selectează **tipul sarcinii** ca **Chat completion**.
    - Selectează **datele de antrenament** pe care dorești să le folosești. Le poți încărca prin Azure AI Foundry sau din mediul tău local.

    ![FineTuneSelect](../../../../translated_images/ro/finetune2.43cb099b1a94442d.png)

7. Selectează **Next**.

8. Încarcă **datele de validare** pe care dorești să le folosești sau poți selecta **Automatic split of training data**.

    ![FineTuneSelect](../../../../translated_images/ro/finetune3.fd96121b67dcdd92.png)

9. Selectează **Next**.

10. Efectuează următoarele:

    - Selectează **multiplicatorul dimensiunii batch-ului** pe care dorești să-l folosești.
    - Selectează **rata de învățare** pe care dorești să o folosești.
    - Selectează **numărul de epoci** pe care dorești să-l folosești.

    ![FineTuneSelect](../../../../translated_images/ro/finetune4.e18b80ffccb5834a.png)

11. Selectează **Submit** pentru a începe procesul de ajustare fină.

    ![FineTuneSelect](../../../../translated_images/ro/select-submit.0a3802d581bac271.png)

12. Odată ce modelul tău este ajustat fin, starea va fi afișată ca **Completed**, așa cum se vede în imaginea de mai jos. Acum poți implementa modelul și îl poți folosi în propria aplicație, în playground sau în prompt flow. Pentru mai multe informații, vezi [Cum să implementezi familia de modele mici Phi-3 cu Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python).

    ![FineTuneSelect](../../../../translated_images/ro/completed.4dc8d2357144cdef.png)

> [!NOTE]
> Pentru informații mai detaliate despre ajustarea fină a Phi-3, vizitează [Fine-tune Phi-3 models in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/fine-tune-phi-3?tabs=phi-3-mini).

## Curățarea modelelor ajustate fin

Poți șterge un model ajustat fin din lista de modele de ajustare fină în [Azure AI Foundry](https://ai.azure.com) sau din pagina de detalii a modelului. Selectează modelul ajustat fin pe care vrei să-l ștergi din pagina Fine-tuning, apoi apasă butonul Delete pentru a-l elimina.

> [!NOTE]
> Nu poți șterge un model personalizat dacă are o implementare activă. Trebuie mai întâi să ștergi implementarea modelului înainte de a putea șterge modelul personalizat.

## Costuri și cote

### Considerații privind costurile și cotele pentru modelele Phi-3 ajustate fin ca serviciu

Modelele Phi ajustate fin ca serviciu sunt oferite de Microsoft și integrate cu Azure AI Foundry pentru utilizare. Poți găsi prețurile atunci când [implementezi](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python) sau ajustezi fin modelele, în fila Pricing and terms din expertul de implementare.

## Filtrarea conținutului

Modelele implementate ca serviciu în regim pay-as-you-go sunt protejate de Azure AI Content Safety. Când sunt implementate la endpoint-uri în timp real, poți opta să dezactivezi această funcționalitate. Cu Azure AI Content Safety activat, atât promptul, cât și completarea trec printr-un ansamblu de modele de clasificare care detectează și previn generarea de conținut dăunător. Sistemul de filtrare a conținutului detectează și ia măsuri asupra anumitor categorii de conținut potențial dăunător, atât în prompturi, cât și în completări. Află mai multe despre [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-studio/concepts/content-filtering).

**Configurarea ajustării fine**

Hyperparametri: Definește hyperparametri precum rata de învățare, dimensiunea batch-ului și numărul de epoci de antrenament.

**Funcția de pierdere**

Alege o funcție de pierdere potrivită pentru sarcina ta (de exemplu, cross-entropy).

**Optimizator**

Selectează un optimizator (de exemplu, Adam) pentru actualizările gradientului în timpul antrenamentului.

**Procesul de ajustare fină**

- Încarcă modelul pre-antrenat: Încarcă checkpoint-ul Phi-3 Mini.
- Adaugă straturi personalizate: Adaugă straturi specifice sarcinii (de exemplu, un cap de clasificare pentru instrucțiuni de chat).

**Antrenează modelul**  
Ajustează fin modelul folosind setul tău de date pregătit. Monitorizează progresul antrenamentului și ajustează hyperparametrii după necesitate.

**Evaluare și validare**

Set de validare: Împarte datele în seturi de antrenament și validare.

**Evaluează performanța**

Folosește metrici precum acuratețea, scorul F1 sau perplexitatea pentru a evalua performanța modelului.

## Salvarea modelului ajustat fin

**Checkpoint**  
Salvează checkpoint-ul modelului ajustat fin pentru utilizări viitoare.

## Implementare

- Implementează ca serviciu web: Publică modelul ajustat fin ca serviciu web în Azure AI Foundry.
- Testează endpoint-ul: Trimite interogări de test către endpoint-ul implementat pentru a verifica funcționalitatea.

## Iterează și îmbunătățește

Iterează: Dacă performanța nu este satisfăcătoare, ajustează hyperparametrii, adaugă mai multe date sau continuă ajustarea fină pentru epoci suplimentare.

## Monitorizează și rafinează

Monitorizează continuu comportamentul modelului și rafinează-l după necesitate.

## Personalizează și extinde

Sarcini personalizate: Phi-3 Mini poate fi ajustat fin pentru diverse sarcini dincolo de instrucțiunile de chat. Explorează alte cazuri de utilizare!  
Experimentează: Încearcă arhitecturi diferite, combinații de straturi și tehnici pentru a îmbunătăți performanța.

> [!NOTE]
> Ajustarea fină este un proces iterativ. Experimentează, învață și adaptează modelul pentru a obține cele mai bune rezultate pentru sarcina ta specifică!

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.