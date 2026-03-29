# **Utilizarea Microsoft Foundry pentru evaluare**

![aistudo](../../../../../translated_images/ro/AIFoundry.9e0b513e999a1c5a.webp)

Cum să evaluați aplicația dvs. generativă AI folosind [Microsoft Foundry](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo). Indiferent dacă evaluați conversații cu un singur tur sau mai multe tururi, Microsoft Foundry oferă instrumente pentru evaluarea performanței și siguranței modelului.

![aistudo](../../../../../translated_images/ro/AIPortfolio.69da59a8e1eaa70f.webp)

## Cum să evaluați aplicații AI generative cu Microsoft Foundry
Pentru instrucțiuni mai detaliate, consultați [Documentația Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-generative-ai-app?WT.mc_id=aiml-138114-kinfeylo)

Iată pașii pentru a începe:

## Evaluarea modelelor AI generative în Microsoft Foundry

**Cerințe preliminare**

- Un set de date de test în format CSV sau JSON.
- Un model AI generativ implementat (cum ar fi Phi-3, GPT 3.5, GPT 4 sau modelele Davinci).
- Un runtime cu o instanță de calcul pentru rularea evaluării.

## Metrice de evaluare integrate

Microsoft Foundry vă permite să evaluați atât conversații cu un singur tur, cât și conversații complexe cu mai multe tururi.  
Pentru scenarii Retrieval Augmented Generation (RAG), unde modelul este ancorat în date specifice, puteți evalua performanța folosind metricele de evaluare integrate.  
În plus, puteți evalua scenarii generale de răspuns la întrebări cu un singur tur (non-RAG).

## Crearea unei rulări de evaluare

Din interfața Microsoft Foundry, navigați fie la pagina Evaluate, fie la pagina Prompt Flow.  
Urmați asistentul de creare a evaluării pentru a configura o rulare de evaluare. Furnizați un nume opțional pentru evaluarea dvs.  
Selectați scenariul care se aliniază obiectivelor aplicației dvs.  
Alegeți una sau mai multe metrice de evaluare pentru a analiza rezultatul modelului.

## Flux de evaluare personalizat (opțional)

Pentru o flexibilitate sporită, puteți stabili un flux de evaluare personalizat. Personalizați procesul de evaluare în funcție de cerințele dvs. specifice.

## Vizualizarea rezultatelor

După rularea evaluării, înregistrați, vizualizați și analizați metricele detaliate de evaluare în Microsoft Foundry. Obțineți perspective asupra capacităților și limitărilor aplicației dvs.

**Notă** Microsoft Foundry este în prezent în previzualizare publică, așadar utilizați-l pentru scopuri de experimentare și dezvoltare. Pentru sarcini de producție, luați în considerare alte opțiuni. Explorați documentația oficială [AI Foundry](https://learn.microsoft.com/azure/ai-studio/?WT.mc_id=aiml-138114-kinfeylo) pentru mai multe detalii și instrucțiuni pas cu pas.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru eventuale neînțelegeri sau interpretări greșite care rezultă din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->