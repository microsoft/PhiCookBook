# **Korištenje Microsoft Foundry za evaluaciju**

![aistudo](../../../../../translated_images/hr/AIFoundry.9e0b513e999a1c5a.webp)

Kako evaluirati vašu generativnu AI aplikaciju koristeći [Microsoft Foundry](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo). Bilo da procjenjujete jednokratan ili višekratan razgovor, Microsoft Foundry pruža alate za evaluaciju performansi i sigurnosti modela.

![aistudo](../../../../../translated_images/hr/AIPortfolio.69da59a8e1eaa70f.webp)

## Kako evaluirati generativne AI aplikacije s Microsoft Foundry
Za detaljnije upute pogledajte [Microsoft Foundry dokumentaciju](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-generative-ai-app?WT.mc_id=aiml-138114-kinfeylo)

Evo koraka za početak:

## Evaluacija Generativnih AI Modela u Microsoft Foundry

**Preduvjeti**

- Testni skup podataka u CSV ili JSON formatu.
- Raspoređeni generativni AI model (kao što su Phi-3, GPT 3.5, GPT 4 ili Davinci modeli).
- Runtime s računarskim instancom za izvršavanje evaluacije.

## Ugrađene Metričke za Evaluaciju

Microsoft Foundry omogućuje evaluaciju kako jednokratnih tako i složenih višekratnih razgovora.
Za scenarije Retrieval Augmented Generation (RAG), gdje je model utemeljen na specifičnim podacima, možete procijeniti performanse koristeći ugrađene metričke za evaluaciju.
Također možete evaluirati opće jednokratne scenarije odgovaranja na pitanja (ne-RAG).

## Kreiranje Evaluacijske Sesije

U Microsoft Foundry sučelju, idite na stranicu Evaluate ili Prompt Flow.
Slijedite čarobnjak za kreiranje evaluacije kako biste postavili evaluacijsku sesiju. Unesite opcionalni naziv vaše evaluacije.
Odaberite scenarij koji se podudara s ciljevima vaše aplikacije.
Odaberite jednu ili više metričkih mjera za procjenu izlaza modela.

## Prilagođeni Evaluacijski Tok (Opcionalno)

Za veću fleksibilnost, možete uspostaviti prilagođeni evaluacijski tok. Prilagodite proces evaluacije prema vašim specifičnim zahtjevima.

## Pregled Rezultata

Nakon izvršavanja evaluacije, zabilježite, pogledajte i analizirajte detaljne metričke pokazatelje evaluacije u Microsoft Foundry. Steknite uvide u mogućnosti i ograničenja vaše aplikacije.

**Napomena** Microsoft Foundry je trenutno u javnoj pretpreglednoj fazi, stoga ga koristite za eksperimentiranje i razvoj. Za produkcijske radne zadatke razmotrite druge opcije. Istražite službenu [AI Foundry dokumentaciju](https://learn.microsoft.com/azure/ai-studio/?WT.mc_id=aiml-138114-kinfeylo) za više detalja i korak-po-korak upute.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Odricanje od odgovornosti**:
Ovaj dokument je preveden korištenjem AI usluge za prijevod [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo postići točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati službenim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazuma ili pogrešna tumačenja proizašla iz upotrebe ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->