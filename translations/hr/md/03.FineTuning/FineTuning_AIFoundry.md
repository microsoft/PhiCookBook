# Podešavanje Phi-3 s Microsoft Foundry

 Istražimo kako fino podesiti Microsoftov jezični model Phi-3 Mini koristeći Microsoft Foundry. Fino podešavanje omogućuje prilagodbu Phi-3 Mini za specifične zadatke, čineći ga još moćnijim i svjesnijim konteksta.

## Razmatranja

- **Sposobnosti:** Koji se modeli mogu fino podesiti? Za što se može fino podesiti osnovni model?
- **Trošak:** Koji je model cijena za fino podešavanje
**Prilagodljivost:** Koliko mogu modificirati osnovni model – i na koje načine?
- **Udobnost:** Kako zapravo prolazi fino podešavanje – moram li pisati prilagođeni kod? Moram li donijeti vlastitu računalnu snagu?
- **Sigurnost:** Fino podešeni su modeli poznati po sigurnosnim rizicima – postoje li zaštitne mjere za sprječavanje neželjenih šteta?

![AIFoundry Models](../../../../translated_images/hr/AIFoundryModels.0e1b16f7d0b09b73.webp)

## Priprema za fino podešavanje

### Preduvjeti

> [!NOTE]
> Za modele iz obitelji Phi-3, opcija fino podešavanja uz naplatu po korištenju dostupna je samo za hubove kreirane u regijama **East US 2**.

- Azure pretplata. Ako nemate Azure pretplatu, kreirajte [plaćeni Azure račun](https://azure.microsoft.com/pricing/purchase-options/pay-as-you-go) da biste započeli.

- [AI Foundry projekt](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo).
- Za upravljanje pristupom operacijama u Microsoft Foundry koristi se uloga temeljena na pristupu Azure (Azure RBAC). Da biste izveli korake u ovom članku, vaš korisnički račun mora imati dodijeljenu __Azure AI Developer ulogu__ na grupu resursa.

### Registracija davatelja pretplate

Provjerite je li pretplata registrirana kod pružatelja resursa `Microsoft.Network`.

1. Prijavite se na [Azure portal](https://portal.azure.com).
1. Odaberite **Pretplate** s lijevog izbornika.
1. Odaberite pretplatu koju želite koristiti.
1. Odaberite **Postavke AI projekta** > **Pružatelji resursa** s lijevog izbornika.
1. Potvrdite da je **Microsoft.Network** na listi pružatelja resursa. Ako nije, dodajte ga.

### Priprema podataka

Pripremite svoje podatke za treniranje i validaciju kako biste fino podesili svoj model. Vaši skupovi podataka za treniranje i validaciju sastoje se od primjera unosa i izlaza za način na koji želite da model radi.

Provjerite da svi vaši primjeri za treniranje slijede očekivani format za zaključivanje. Za učinkovito fino podešavanje modela, osigurajte uravnotežen i raznolik skup podataka.

To uključuje održavanje ravnoteže podataka, uključivanje različitih scenarija i povremeno usavršavanje skupa podataka za treniranje kako bi se uskladio s očekivanjima iz stvarnog svijeta, što na kraju vodi do preciznijih i uravnoteženijih odgovora modela.

Različiti tipovi modela zahtijevaju različit format podataka za treniranje.

### Chat konačenje

Podaci za treniranje i validaciju koje koristite **moraju** biti formatirani kao JSON Lines (JSONL) dokument. Za `Phi-3-mini-128k-instruct` skup podataka za fino podešavanje mora biti formatiran u konverzacijskom formatu koji koristi API za chat završetke.

### Primjer formata datoteke

```json
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Is Xbox better than PlayStation?"}, {"role": "assistant", "content": "I apologize, but I cannot provide personal opinions. My primary job is to assist you with any issues related to your Xbox device. Do you have any Xbox-related issues that need addressing?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Can I play PC games on my Xbox?"}, {"role": "assistant", "content": "While Xbox consoles don't natively support PC games, they can play an array of Xbox games, many of which are also available on PC. Can I assist you with finding games compatible with your Xbox device?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "I'm having trouble connecting my Xbox to the Wi-Fi."}, {"role": "assistant", "content": "No worries, let's go through the network settings on your Xbox. Can you please tell me what happens when you try to connect it to the Wi-Fi?"}]}
```

Podržani tip datoteke je JSON Lines. Datoteke se šalju u zadani spremište podataka i postaju dostupne u vašem projektu.

## Fino podešavanje Phi-3 s Microsoft Foundry

Microsoft Foundry omogućuje vam prilagođavanje velikih jezičnih modela vašim osobnim skupovima podataka kroz proces poznat kao fino podešavanje. Fino podešavanje donosi značajnu vrijednost omogućujući prilagodbu i optimizaciju za specifične zadatke i primjene. To rezultira poboljšanim performansama, isplativošću, smanjenom latencijom i prilagođenim izlazima.

![Finetune AI Foundry](../../../../translated_images/hr/AIFoundryfinetune.193aaddce48d553c.webp)

### Kreirajte novi projekt

1. Prijavite se na [Microsoft Foundry](https://ai.azure.com).

1. Odaberite **+New project** za kreiranje novog projekta u Microsoft Foundry.

    ![FineTuneSelect](../../../../translated_images/hr/select-new-project.cd31c0404088d7a3.webp)

1. Obavite sljedeće zadatke:

    - Ime projekta **Hub name**. Mora biti jedinstvena vrijednost.
    - Odaberite **Hub** koji ćete koristiti (kreirajte novi ako je potrebno).

    ![FineTuneSelect](../../../../translated_images/hr/create-project.ca3b71298b90e420.webp)

1. Obavite sljedeće zadatke za kreiranje novog huba:

    - Unesite **Hub name**. Mora biti jedinstvena vrijednost.
    - Odaberite svoju Azure **Pretplatu**.
    - Odaberite **Grupu resursa** za korištenje (kreirajte novu ako je potrebno).
    - Odaberite **Lokaciju** koju želite koristiti.
    - Odaberite **Poveži Azure AI usluge** za korištenje (kreirajte novu ako je potrebno).
    - Odaberite **Poveži Azure AI pretraživanje** na **Preskoči povezivanje**.

    ![FineTuneSelect](../../../../translated_images/hr/create-hub.49e53d235e80779e.webp)

1. Odaberite **Dalje**.
1. Odaberite **Kreiraj projekt**.

### Priprema podataka

Prije fino podešavanja, prikupite ili kreirajte skup podataka relevantan za vaš zadatak, poput uputa za chat, parova pitanja i odgovora ili bilo kojih drugih relevantnih tekstualnih podataka. Očistite i preradite te podatke uklanjajući buku, rješavajući nedostajuće vrijednosti i tokenizirajući tekst.

### Fino podešavanje Phi-3 modela u Microsoft Foundry

> [!NOTE]
> Fino podešavanje Phi-3 modela trenutno je podržano u projektima smještenima u East US 2.

1. Odaberite **Katalog modela** s lijeve strane.

1. Upišite *phi-3* u **tražilicu** i odaberite phi-3 model koji želite koristiti.

    ![FineTuneSelect](../../../../translated_images/hr/select-model.60ef2d4a6a3cec57.webp)

1. Odaberite **Fino podešavanje**.

    ![FineTuneSelect](../../../../translated_images/hr/select-finetune.a976213b543dd9d8.webp)

1. Unesite **Ime fino podešenog modela**.

    ![FineTuneSelect](../../../../translated_images/hr/finetune1.c2b39463f0d34148.webp)

1. Odaberite **Dalje**.

1. Obavite sljedeće zadatke:

    - Odaberite **tip zadatka** na **Chat completion**.
    - Odaberite **Podatke za treniranje** koje želite koristiti. Možete ih učitati preko Microsoft Foundry podataka ili iz lokalnog okruženja.

    ![FineTuneSelect](../../../../translated_images/hr/finetune2.43cb099b1a94442d.webp)

1. Odaberite **Dalje**.

1. Učitajte **Podatke za validaciju** koje želite koristiti ili možete odabrati **Automatska podjela podataka za treniranje**.

    ![FineTuneSelect](../../../../translated_images/hr/finetune3.fd96121b67dcdd92.webp)

1. Odaberite **Dalje**.

1. Obavite sljedeće zadatke:

    - Odaberite **multiplikator veličine serije (Batch size multiplier)** koju želite koristiti.
    - Odaberite **stopu učenja (Learning rate)** koju želite koristiti.
    - Odaberite **epohe (Epochs)** koje želite koristiti.

    ![FineTuneSelect](../../../../translated_images/hr/finetune4.e18b80ffccb5834a.webp)

1. Odaberite **Pošalji** za početak procesa fino podešavanja.

    ![FineTuneSelect](../../../../translated_images/hr/select-submit.0a3802d581bac271.webp)


1. Kada je vaš model fino podešen, status će biti prikazan kao **Dovršeno**, kao što je prikazano na slici ispod. Sada možete postaviti model i koristiti ga u svojoj aplikaciji, u playgroundu ili u prompt flowu. Za više informacija, pogledajte [Kako postaviti Phi-3 obitelj malih jezičnih modela s Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python).

    ![FineTuneSelect](../../../../translated_images/hr/completed.4dc8d2357144cdef.webp)

> [!NOTE]
> Za detaljnije informacije o fino podešavanju Phi-3, posjetite [Fino podešavanje Phi-3 modela u Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/fine-tune-phi-3?tabs=phi-3-mini).

## Čišćenje vaših fino podešenih modela

Možete izbrisati fino podešen model s liste fino podešenih modela u [Microsoft Foundry](https://ai.azure.com) ili s stranice s detaljima modela. Odaberite fino podešen model za brisanje na stranici Fine-tuning, a zatim odaberite gumb Izbriši za brisanje modela.

> [!NOTE]
> Ne možete izbrisati prilagođeni model ako postoji postojeća implementacija. Prvo morate izbrisati implementaciju modela prije nego što možete izbrisati prilagođeni model.

## Troškovi i kvote

### Razmatranja troškova i kvota za Phi-3 modele fino podešene kao usluga

Phi modeli fino podešeni kao usluga nude se od Microsofta i integrirani su s Microsoft Foundry za korištenje. Cijene možete pronaći prilikom [postavljanja](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python) ili fino podešavanja modela pod karticom Cijene i uvjeti u čarobnjaku za postavljanje.

## Filtriranje sadržaja

Modeli postavljeni kao usluga s naplatom prema korištenju zaštićeni su putem Azure AI Content Safety. Kada se postave na krajnje točke u stvarnom vremenu, možete isključiti ovu mogućnost. S omogućenim Azure AI Content Safety, i upit i odgovor prolaze kroz skup klasifikacijskih modela usmjerenih na otkrivanje i sprječavanje prikazivanja štetnog sadržaja. Sustav filtriranja sadržaja otkriva i poduzima mjere za specifične kategorije potencijalno štetnog sadržaja u ulaznim upitima i izlaznim odgovorima. Saznajte više o [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-studio/concepts/content-filtering).

**Konfiguracija fino podešavanja**

Hiperparametri: Definirajte hiperparametre kao što su stopa učenja, veličina serije i broj epoha treniranja.

**Funkcija gubitka**

Odaberite prikladnu funkciju gubitka za svoj zadatak (npr. unakrsna entropija).

**Optimizator**

Odaberite optimizator (npr. Adam) za ažuriranja gradijenta tijekom treniranja.

**Proces fino podešavanja**

- Učitajte unaprijed istrenirani model: učitajte Phi-3 Mini kontrolnu točku.
- Dodajte prilagođene slojeve: dodajte slojeve specifične za zadatak (npr. klasifikacijsko glava za upute chat-a).

**Trenirajte model**
Fino podesite model koristeći pripremljeni skup podataka. Pratite napredak treniranja i prilagođavajte hiperparametre po potrebi.

**Evaluacija i validacija**

Skup za validaciju: podijelite podatke na skupove za treniranje i validaciju.

**Procjena performansi**

Koristite metrike kao što su točnost, F1-skor ili perplexity za procjenu performansi modela.

## Spremite fino podešeni model

**Kontrolna točka**
Spremite kontrolnu točku fino podešenog modela za buduću uporabu.

## Postavljanje

- Postavite kao web uslugu: postavite svoj fino podešeni model kao web uslugu u Microsoft Foundry.
- Testirajte krajnju točku: šaljite testne upite na postavljenu krajnju točku za provjeru funkcionalnosti.

## Iterirajte i poboljšavajte

Iterirajte: ako performanse nisu zadovoljavajuće, iterirajte podešavajući hiperparametre, dodajući više podataka ili fino podešavajući za dodatne epohe.

## Pratite i usavršite

Kontinuirano pratite ponašanje modela i usavršavajte ga po potrebi.

## Prilagodite i proširite

Prilagođeni zadaci: Phi-3 Mini se može fino podesiti za razne zadatke izvan uputa za chat. Istražite druge slučajeve korištenja!
Eksperimentirajte: isprobajte različite arhitekture, kombinacije slojeva i tehnike za poboljšanje performansi.

> [!NOTE]
> Fino podešavanje je iterativni proces. Eksperimentirajte, učite i prilagodite model za postizanje najboljih rezultata za svoj specifični zadatak!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI servisa za prijevod [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo postići točnost, molimo imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni prijevod od strane ljudi. Ne snosimo odgovornost za bilo kakve nesporazume ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->