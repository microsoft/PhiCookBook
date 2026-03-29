# **Použitie Microsoft Foundry na hodnotenie**

![aistudo](../../../../../translated_images/sk/AIFoundry.9e0b513e999a1c5a.webp)

Ako vyhodnotiť svoju generatívnu AI aplikáciu pomocou [Microsoft Foundry](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo). Či už hodnotíte jednorázové alebo viackolové konverzácie, Microsoft Foundry poskytuje nástroje na hodnotenie výkonu a bezpečnosti modelu.

![aistudo](../../../../../translated_images/sk/AIPortfolio.69da59a8e1eaa70f.webp)

## Ako hodnotiť generatívne AI aplikácie pomocou Microsoft Foundry
Podrobnejšie inštrukcie nájdete v [Microsoft Foundry dokumentácii](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-generative-ai-app?WT.mc_id=aiml-138114-kinfeylo)

Tu sú kroky na začatie:

## Hodnotenie generatívnych AI modelov v Microsoft Foundry

**Predpoklady**

- Testovacia dátová sada vo formáte CSV alebo JSON.
- Nasadený generatívny AI model (ako Phi-3, GPT 3.5, GPT 4 alebo Davinci modely).
- Prostredie runtime s výpočtovým inštancom na spustenie hodnotenia.

## Vstavané metriky hodnotenia

Microsoft Foundry umožňuje hodnotiť ako jednorázové, tak aj zložité viackolové konverzácie.  
Pre scenáre Retrieval Augmented Generation (RAG), kde je model založený na konkrétnych dátach, môžete hodnotiť výkon pomocou vstavaných evaluačných metrík.  
Tiež je možné hodnotiť všeobecné jednorázové otázky a odpovede (non-RAG).

## Vytvorenie behu hodnotenia

V používateľskom rozhraní Microsoft Foundry prejdite na stránku Evaluate alebo Prompt Flow.  
Nasledujte sprievodcu vytvorením hodnotenia. Poskytnite voliteľný názov hodnotenia.  
Vyberte scenár, ktorý zodpovedá cieľom vašej aplikácie.  
Zvoľte jednu alebo viac evaluačných metrík na zhodnotenie výstupu modelu.

## Vlastný evaluačný tok (voliteľné)

Pre väčšiu flexibilitu môžete nastaviť vlastný evaluačný tok. Prispôsobte hodnotiaci proces podľa svojich špecifických požiadaviek.

## Zobrazenie výsledkov

Po spustení hodnotenia si v Microsoft Foundry zapíšte, prezrite a analyzujte detailné evaluačné metriky. Získajte prehľad o možnostiach a obmedzeniach vašej aplikácie.

**Poznámka** Microsoft Foundry je momentálne v verejnej predbežnej verzii, preto ho používajte na experimentovanie a vývoj. Pre produkčné nasadenia zvážte iné možnosti. Pre viac informácií a detailné návodné kroky preskúmajte oficiálnu [dokumentáciu AI Foundry](https://learn.microsoft.com/azure/ai-studio/?WT.mc_id=aiml-138114-kinfeylo).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Upozornenie**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->