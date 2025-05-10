<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e0a07fd2a30fe2af30b1373df207a5bf",
  "translation_date": "2025-05-09T21:50:26+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Phi-3-visionWandB.md",
  "language_code": "ro"
}
-->
# Prezentare generală a proiectului Phi-3-Vision-128K-Instruct

## Modelul

Phi-3-Vision-128K-Instruct, un model multimodal ușor și de ultimă generație, este elementul central al acestui proiect. Face parte din familia de modele Phi-3 și suportă o lungime a contextului de până la 128.000 de tokeni. Modelul a fost antrenat pe un set diversificat de date, care include date sintetice și site-uri web publice atent filtrate, punând accent pe conținut de înaltă calitate, care necesită raționament. Procesul de antrenament a inclus ajustare fină supravegheată și optimizare directă a preferințelor pentru a asigura respectarea precisă a instrucțiunilor, precum și măsuri robuste de siguranță.

## Crearea datelor de probă este esențială din mai multe motive:

1. **Testare**: Datele de probă îți permit să testezi aplicația în diverse scenarii fără a afecta datele reale. Acest aspect este deosebit de important în fazele de dezvoltare și testare.

2. **Optimizarea performanței**: Cu date de probă care imită scala și complexitatea datelor reale, poți identifica blocajele de performanță și optimiza aplicația în consecință.

3. **Prototipare**: Datele de probă pot fi folosite pentru a crea prototipuri și machete, ajutând la înțelegerea cerințelor utilizatorilor și la obținerea de feedback.

4. **Analiza datelor**: În știința datelor, datele de probă sunt adesea utilizate pentru analiza exploratorie, antrenarea modelelor și testarea algoritmilor.

5. **Securitate**: Folosirea datelor de probă în mediile de dezvoltare și testare poate preveni scurgerile accidentale de date reale sensibile.

6. **Învățare**: Dacă înveți o tehnologie sau un instrument nou, lucrul cu date de probă oferă o modalitate practică de a aplica ceea ce ai învățat.

Ține minte, calitatea datelor tale de probă poate influența semnificativ aceste activități. Acestea ar trebui să fie cât mai apropiate posibil de datele reale, atât ca structură, cât și ca variabilitate.

### Crearea datelor de probă
[Generate DataSet Script](./CreatingSampleData.md)

## Setul de date

Un exemplu bun de set de date de probă este [DBQ/Burberry.Product.prices.United.States dataset](https://huggingface.co/datasets/DBQ/Burberry.Product.prices.United.States) (disponibil pe Huggingface).  
Setul de date de probă conține produse Burberry împreună cu metadate despre categoria produselor, preț și titlu, având în total 3.040 de rânduri, fiecare reprezentând un produs unic. Acest set de date ne permite să testăm capacitatea modelului de a înțelege și interpreta date vizuale, generând texte descriptive care surprind detalii vizuale complexe și caracteristici specifice brandului.

**Note:** Poți folosi orice set de date care include imagini.

## Raționament complex

Modelul trebuie să raționeze asupra prețurilor și denumirilor având la dispoziție doar imaginea. Acest lucru implică nu doar recunoașterea caracteristicilor vizuale, ci și înțelegerea implicațiilor acestora în termeni de valoare a produsului și branding. Prin sintetizarea unor descrieri textuale precise din imagini, proiectul evidențiază potențialul integrării datelor vizuale pentru a îmbunătăți performanța și versatilitatea modelelor în aplicații reale.

## Arhitectura Phi-3 Vision

Arhitectura modelului este o versiune multimodală a unui Phi-3. Procesează atât date textuale, cât și imagini, integrând aceste intrări într-o secvență unificată pentru o înțelegere și generare cuprinzătoare. Modelul folosește straturi de embedding separate pentru text și imagini. Tokenii de text sunt transformați în vectori densi, în timp ce imaginile sunt procesate printr-un model vizual CLIP pentru a extrage embedding-uri de caracteristici. Aceste embedding-uri ale imaginilor sunt apoi proiectate pentru a corespunde dimensiunilor embedding-urilor textului, asigurând o integrare fără probleme.

## Integrarea embedding-urilor text și imagine

Tokenii speciali din secvența de text indică locurile unde embedding-urile imaginilor trebuie inserate. În timpul procesării, acești tokeni speciali sunt înlocuiți cu embedding-urile corespunzătoare ale imaginilor, permițând modelului să gestioneze textul și imaginile ca o singură secvență. Promptul pentru setul nostru de date este formatat folosind tokenul special <|image|> astfel:

```python
text = f"<|user|>\n<|image_1|>What is shown in this image?<|end|><|assistant|>\nProduct: {row['title']}, Category: {row['category3_code']}, Full Price: {row['full_price']}<|end|>"
```

## Cod exemplu
- [Phi-3-Vision Training Script](../../../../code/03.Finetuning/Phi-3-vision-Trainingscript.py)
- [Weights and Bias Example walkthrough](https://wandb.ai/byyoung3/mlnews3/reports/How-to-fine-tune-Phi-3-vision-on-a-custom-dataset--Vmlldzo4MTEzMTg3)

**Declinare a responsabilității**:  
Acest document a fost tradus folosind serviciul de traducere automată AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.