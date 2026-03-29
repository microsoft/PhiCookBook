# **Uporaba Microsoft Foundry za ocenjevanje**

![aistudo](../../../../../translated_images/sl/AIFoundry.9e0b513e999a1c5a.webp)

Kako oceniti svojo generativno AI aplikacijo z uporabo [Microsoft Foundry](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo). Ne glede na to, ali ocenjujete enkratne ali večkratne pogovore, Microsoft Foundry nudi orodja za ocenjevanje zmogljivosti in varnosti modela.

![aistudo](../../../../../translated_images/sl/AIPortfolio.69da59a8e1eaa70f.webp)

## Kako oceniti generativne AI aplikacije z Microsoft Foundry
Za podrobnejša navodila si oglejte [Microsoft Foundry dokumentacijo](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-generative-ai-app?WT.mc_id=aiml-138114-kinfeylo)

Tukaj so koraki za začetek:

## Ocenjevanje generativnih AI modelov v Microsoft Foundry

**Pogoji**

- Testni podatkovni niz v formatu CSV ali JSON.
- Uporabljeni generativni AI model (kot so Phi-3, GPT 3.5, GPT 4 ali modeli Davinci).
- Okolje za izvajanje z računalniškim primerkom za izvajanje ocenjevanja.

## Vgrajene metrike ocenjevanja

Microsoft Foundry omogoča ocenjevanje tako enkratnih kot zapletenih, večkratnih pogovorov.
Za scenarije z Retrieval Augmented Generation (RAG), kjer je model povezan s specifičnimi podatki, lahko zmogljivost ocenite z vgrajenimi metrikami ocenjevanja.
Poleg tega lahko ocenite splošne enkratne scenarije odgovarjanja na vprašanja (ne-RAG).

## Ustvarjanje ocenjevalnega zagona

V uporabniškem vmesniku Microsoft Foundry se premaknite na stran Evaluate ali stran Prompt Flow.
Sledite čarovniku za ustvarjanje ocenjevanja, da nastavite zagon ocenjevanja. Po želji dodajte ime za vaše ocenjevanje.
Izberite scenarij, ki je usklajen z nameni vaše aplikacije.
Izberite eno ali več metrik ocenjevanja za presojo izhoda modela.

## Prilagojeni potek ocenjevanja (Neobvezno)

Za večjo prilagodljivost lahko vzpostavite prilagojen potek ocenjevanja. Prilagodite postopek ocenjevanja glede na vaše specifične zahteve.

## Pregled rezultatov

Po izvedbi ocenjevanja v Microsoft Foundry evidentirajte, si oglejte in analizirajte podrobne metrike ocenjevanja. Pridobite vpoglede v zmogljivosti in omejitve vaše aplikacije.


**Opomba** Microsoft Foundry je trenutno v javni presoji, zato ga uporabljajte za eksperimentiranje in razvoj. Za produkcijske obremenitve razmislite o drugih možnostih. Za več podrobnosti in navodil korak za korakom preučite uradno [dokumentacijo AI Foundry](https://learn.microsoft.com/azure/ai-studio/?WT.mc_id=aiml-138114-kinfeylo).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, upoštevajte, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku velja za avtoritativni vir. Za kritične informacije je priporočljivo uporabiti profesionalni človeški prevod. Nismo odgovorni za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->