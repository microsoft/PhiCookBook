<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7b4235159486df4000e16b7b46ddfec3",
  "translation_date": "2025-07-16T22:34:12+00:00",
  "source_file": "md/01.Introduction/05/AIFoundry.md",
  "language_code": "hr"
}
-->
# **Korištenje Azure AI Foundry za evaluaciju**

![aistudo](../../../../../translated_images/AIFoundry.9e0b513e999a1c5a.hr.png)

Kako evaluirati svoju generativnu AI aplikaciju koristeći [Azure AI Foundry](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo). Bilo da procjenjujete jednokratne ili višekratne razgovore, Azure AI Foundry nudi alate za procjenu performansi i sigurnosti modela.

![aistudo](../../../../../translated_images/AIPortfolio.69da59a8e1eaa70f.hr.png)

## Kako evaluirati generativne AI aplikacije s Azure AI Foundry
Za detaljnije upute pogledajte [Azure AI Foundry dokumentaciju](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-generative-ai-app?WT.mc_id=aiml-138114-kinfeylo)

Evo koraka za početak:

## Evaluacija generativnih AI modela u Azure AI Foundry

**Preduvjeti**

- Testni skup podataka u CSV ili JSON formatu.
- Implementirani generativni AI model (kao što su Phi-3, GPT 3.5, GPT 4 ili Davinci modeli).
- Runtime s računalnim instancom za izvođenje evaluacije.

## Ugrađene metrike evaluacije

Azure AI Foundry omogućuje evaluaciju jednokratnih i složenih višekratnih razgovora.  
Za Retrieval Augmented Generation (RAG) scenarije, gdje je model utemeljen na specifičnim podacima, možete procijeniti performanse koristeći ugrađene metrike evaluacije.  
Također, moguće je evaluirati opće scenarije jednokratnog odgovaranja na pitanja (ne-RAG).

## Kreiranje evaluacijskog pokretanja

U Azure AI Foundry sučelju, idite na stranicu Evaluate ili Prompt Flow.  
Slijedite čarobnjak za kreiranje evaluacije kako biste postavili evaluacijsko pokretanje. Po želji unesite naziv evaluacije.  
Odaberite scenarij koji odgovara ciljevima vaše aplikacije.  
Izaberite jednu ili više metrika evaluacije za procjenu izlaza modela.

## Prilagođeni evaluacijski tijek (opcionalno)

Za veću fleksibilnost, možete postaviti prilagođeni evaluacijski tijek. Prilagodite proces evaluacije prema svojim specifičnim potrebama.

## Pregled rezultata

Nakon izvođenja evaluacije, zabilježite, pregledajte i analizirajte detaljne metrike evaluacije u Azure AI Foundry. Steknite uvid u mogućnosti i ograničenja vaše aplikacije.

**Note** Azure AI Foundry je trenutno u javnoj pretpreglednoj fazi, stoga ga koristite za eksperimentiranje i razvoj. Za produkcijske zadatke razmotrite druge opcije. Istražite službenu [AI Foundry dokumentaciju](https://learn.microsoft.com/azure/ai-studio/?WT.mc_id=aiml-138114-kinfeylo) za više detalja i korak-po-korak upute.

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati službenim i autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakve nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.