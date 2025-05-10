<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3cbe7629d254f1043193b7fe22524d55",
  "translation_date": "2025-05-09T15:21:51+00:00",
  "source_file": "md/01.Introduction/05/Promptflow.md",
  "language_code": "ro"
}
-->
# **Introduce Promptflow**

[Microsoft Prompt Flow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=aiml-138114-kinfeylo) este un instrument vizual de automatizare a fluxurilor de lucru care permite utilizatorilor să creeze fluxuri automate folosind șabloane predefinite și conectori personalizați. A fost conceput pentru a permite dezvoltatorilor și analiștilor de business să construiască rapid procese automate pentru sarcini precum gestionarea datelor, colaborarea și optimizarea proceselor. Cu Prompt Flow, utilizatorii pot conecta cu ușurință diferite servicii, aplicații și sisteme și pot automatiza procese de business complexe.

Microsoft Prompt Flow este proiectat să eficientizeze ciclul complet de dezvoltare al aplicațiilor AI bazate pe Large Language Models (LLMs). Indiferent dacă te afli în faza de generare de idei, prototipare, testare, evaluare sau implementare a aplicațiilor bazate pe LLM, Prompt Flow simplifică procesul și îți permite să construiești aplicații LLM de calitate pentru producție.

## Iată principalele caracteristici și beneficii ale utilizării Microsoft Prompt Flow:

**Experiență Interactivă de Autoriat**

Prompt Flow oferă o reprezentare vizuală a structurii fluxului tău, făcând proiectele ușor de înțeles și de navigat.
Oferă o experiență de codare asemănătoare unui notebook pentru dezvoltare și depanare eficientă a fluxurilor.

**Variante și Ajustări de Prompt**

Creează și compară multiple variante de prompt pentru a facilita un proces iterativ de rafinare. Evaluează performanța diferitelor prompturi și alege cele mai eficiente.

**Fluxuri de Evaluare Integrate**

Evaluează calitatea și eficacitatea prompturilor și fluxurilor folosind instrumentele de evaluare integrate.
Înțelege cât de bine performează aplicațiile tale bazate pe LLM.

**Resurse Complete**

Prompt Flow include o bibliotecă de instrumente, exemple și șabloane integrate. Aceste resurse servesc ca punct de plecare pentru dezvoltare, inspiră creativitatea și accelerează procesul.

**Colaborare și Pregătire pentru Medii Enterprise**

Sprijină colaborarea în echipă, permițând mai multor utilizatori să lucreze împreună la proiecte de inginerie a prompturilor.
Menține controlul versiunilor și împărtășește cunoștințele eficient. Simplifică întregul proces de inginerie a prompturilor, de la dezvoltare și evaluare până la implementare și monitorizare.

## Evaluarea în Prompt Flow

În Microsoft Prompt Flow, evaluarea joacă un rol crucial în aprecierea performanței modelelor tale AI. Să explorăm cum poți personaliza fluxurile și metricile de evaluare în Prompt Flow:

![PFVizualise](../../../../../translated_images/pfvisualize.93c453890f4088830217fa7308b1a589058ed499bbfff160c85676066b5cbf2d.ro.png)

**Înțelegerea Evaluării în Prompt Flow**

În Prompt Flow, un flux reprezintă o secvență de noduri care procesează inputul și generează output. Fluxurile de evaluare sunt tipuri speciale de fluxuri create pentru a aprecia performanța unei execuții pe baza unor criterii și obiective specifice.

**Caracteristici cheie ale fluxurilor de evaluare**

De obicei, acestea rulează după fluxul testat, folosind outputurile acestuia. Ele calculează scoruri sau metrici pentru a măsura performanța fluxului testat. Metricile pot include acuratețe, scoruri de relevanță sau orice alte măsuri relevante.

### Personalizarea fluxurilor de evaluare

**Definirea inputurilor**

Fluxurile de evaluare trebuie să preia outputurile execuției testate. Definirea inputurilor se face similar cu fluxurile standard.
De exemplu, dacă evaluezi un flux QnA, numește un input „answer”. Dacă evaluezi un flux de clasificare, numește un input „category”. Pot fi necesare și inputuri cu adevărul de teren (de exemplu, etichete reale).

**Outputuri și metrici**

Fluxurile de evaluare produc rezultate care măsoară performanța fluxului testat. Metricile pot fi calculate folosind Python sau LLM. Folosește funcția log_metric() pentru a înregistra metricile relevante.

**Utilizarea fluxurilor de evaluare personalizate**

Dezvoltă propriul flux de evaluare adaptat sarcinilor și obiectivelor tale specifice. Personalizează metricile în funcție de scopurile evaluării.
Aplică acest flux de evaluare personalizat pentru execuții batch în testări la scară largă.

## Metode de evaluare integrate

Prompt Flow oferă și metode de evaluare integrate.
Poți trimite execuții batch și folosi aceste metode pentru a evalua performanța fluxului cu seturi mari de date.
Vizualizează rezultatele evaluării, compară metricile și iterază după nevoie.
Reține, evaluarea este esențială pentru a te asigura că modelele tale AI îndeplinesc criteriile și obiectivele dorite. Consultă documentația oficială pentru instrucțiuni detaliate despre dezvoltarea și utilizarea fluxurilor de evaluare în Microsoft Prompt Flow.

Pe scurt, Microsoft Prompt Flow oferă dezvoltatorilor posibilitatea de a crea aplicații LLM de înaltă calitate prin simplificarea ingineriei prompturilor și prin furnizarea unui mediu robust de dezvoltare. Dacă lucrezi cu LLM-uri, Prompt Flow este un instrument valoros de explorat. Consultă [Prompt Flow Evaluation Documents](https://learn.microsoft.com/azure/machine-learning/prompt-flow/how-to-develop-an-evaluation-flow?view=azureml-api-2?WT.mc_id=aiml-138114-kinfeylo) pentru instrucțiuni detaliate privind dezvoltarea și utilizarea fluxurilor de evaluare în Microsoft Prompt Flow.

**Declinare a responsabilității**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original, în limba sa nativă, trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un traducător uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea în urma utilizării acestei traduceri.