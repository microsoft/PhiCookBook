<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "90d0d072cf26ccc1f271a580d3e45d70",
  "translation_date": "2025-07-16T14:45:31+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "sk"
}
-->
# Prispievanie

Tento projekt vítá príspevky a návrhy. Väčšina príspevkov vyžaduje, aby ste súhlasili s Contributor License Agreement (CLA), ktorý potvrdzuje, že máte právo a skutočne nám udeľujete práva na použitie vášho príspevku. Pre podrobnosti navštívte [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com)

Keď odošlete pull request, CLA bot automaticky zistí, či je potrebné poskytnúť CLA, a príslušne označí PR (napr. kontrola stavu, komentár). Jednoducho postupujte podľa pokynov bota. Toto budete musieť urobiť iba raz pre všetky repozitáre používajúce náš CLA.

## Kódex správania

Tento projekt prijal [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
Pre viac informácií si prečítajte [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) alebo kontaktujte [opencode@microsoft.com](mailto:opencode@microsoft.com) s ďalšími otázkami alebo pripomienkami.

## Upozornenia pri vytváraní issues

Prosíme, neotvárajte GitHub issues pre všeobecné otázky podpory, pretože zoznam na GitHub by mal byť používaný na požiadavky na funkcie a hlásenia chýb. Takto môžeme ľahšie sledovať skutočné problémy alebo chyby v kóde a oddeliť všeobecnú diskusiu od samotného kódu.

## Ako prispieť

### Pokyny pre pull requesty

Pri odosielaní pull requestu (PR) do repozitára Phi-3 CookBook, prosím, dodržujte nasledujúce pokyny:

- **Forknite repozitár**: Vždy si najskôr forknete repozitár do svojho účtu pred vykonaním zmien.

- **Oddelené pull requesty (PR)**:
  - Každý typ zmeny odosielajte v samostatnom pull requeste. Napríklad opravy chýb a aktualizácie dokumentácie by mali byť v samostatných PR.
  - Opravy preklepov a menšie aktualizácie dokumentácie je možné podľa potreby skombinovať do jedného PR.

- **Riešenie konfliktov pri zlúčení**: Ak váš pull request vykazuje konflikty pri zlúčení, aktualizujte svoju lokálnu vetvu `main`, aby zodpovedala hlavnému repozitáru pred vykonaním zmien.

- **Odosielanie prekladov**: Pri odosielaní prekladového PR sa uistite, že priečinok s prekladmi obsahuje preklady všetkých súborov z pôvodného priečinka.

### Pokyny na písanie

Pre zabezpečenie konzistencie vo všetkých dokumentoch používajte nasledujúce pravidlá:

- **Formátovanie URL**: Všetky URL uzatvorte do hranatých zátvoriek, za ktorými nasledujú zátvorky bez medzier okolo alebo vo vnútri. Napríklad: `[example](https://www.microsoft.com)`.

- **Relatívne odkazy**: Používajte `./` pre relatívne odkazy na súbory alebo priečinky v aktuálnom adresári a `../` pre tie v nadradenom adresári. Napríklad: `[example](../../path/to/file)` alebo `[example](../../../path/to/file)`.

- **Nie lokálne špecifické jazyky**: Uistite sa, že vaše odkazy neobsahujú jazykové alebo krajinné špecifiká. Napríklad, vyhnite sa `/en-us/` alebo `/en/`.

- **Ukladanie obrázkov**: Všetky obrázky ukladajte do priečinka `./imgs`.

- **Popisné názvy obrázkov**: Obrázky pomenúvajte popisne pomocou anglických znakov, číslic a pomlčiek. Napríklad: `example-image.jpg`.

## GitHub Workflows

Keď odošlete pull request, spustia sa nasledujúce workflow na overenie zmien. Postupujte podľa pokynov nižšie, aby váš pull request prešiel kontrolami workflow:

- [Kontrola nefunkčných relatívnych ciest](../..)
- [Kontrola, či URL neobsahujú lokalizáciu](../..)

### Kontrola nefunkčných relatívnych ciest

Tento workflow zabezpečuje, že všetky relatívne cesty vo vašich súboroch sú správne.

1. Pre overenie správnosti odkazov vykonajte v VS Code nasledujúce kroky:
    - Najazdite kurzorom na ľubovoľný odkaz v súboroch.
    - Stlačte **Ctrl + Kliknutie** pre navigáciu na odkaz.
    - Ak kliknete na odkaz a nefunguje lokálne, workflow sa spustí a odkaz nebude fungovať ani na GitHub.

1. Na opravu tohto problému vykonajte nasledujúce kroky s pomocou návrhov ciest od VS Code:
    - Napíšte `./` alebo `../`.
    - VS Code vám ponúkne dostupné možnosti podľa toho, čo ste zadali.
    - Postupujte podľa cesty kliknutím na požadovaný súbor alebo priečinok, aby ste sa uistili, že cesta je správna.

Po pridaní správnej relatívnej cesty uložte a odošlite zmeny.

### Kontrola, či URL neobsahujú lokalizáciu

Tento workflow zabezpečuje, že žiadna webová URL neobsahuje lokalizáciu špecifickú pre krajinu. Keďže je tento repozitár prístupný globálne, je dôležité, aby URL neobsahovali lokalizáciu vašej krajiny.

1. Pre overenie, že vaše URL neobsahujú lokalizáciu krajiny, vykonajte nasledujúce kroky:

    - Skontrolujte, či sa v URL nenachádza text ako `/en-us/`, `/en/` alebo iná jazyková lokalizácia.
    - Ak tieto texty v URL nie sú, kontrolu prejdete.

1. Na opravu tohto problému vykonajte nasledujúce kroky:
    - Otvorte súbor zvýraznený workflow.
    - Odstráňte lokalizáciu krajiny z URL.

Po odstránení lokalizácie uložte a odošlite zmeny.

### Kontrola nefunkčných URL

Tento workflow zabezpečuje, že každá webová URL vo vašich súboroch funguje a vracia stavový kód 200.

1. Pre overenie správnej funkčnosti URL vykonajte nasledujúce kroky:
    - Skontrolujte stav URL vo vašich súboroch.

2. Na opravu nefunkčných URL vykonajte nasledujúce kroky:
    - Otvorte súbor, ktorý obsahuje nefunkčnú URL.
    - Aktualizujte URL na správnu.

Po oprave URL uložte a odošlite zmeny.

> [!NOTE]
>
> Môžu nastať prípady, keď kontrola URL zlyhá, aj keď je odkaz prístupný. Môže sa to stať z viacerých dôvodov, vrátane:
>
> - **Sieťové obmedzenia:** Servery GitHub actions môžu mať sieťové obmedzenia, ktoré bránia prístupu k určitým URL.
> - **Problémy s časovým limitom:** URL, ktoré odpovedajú príliš dlho, môžu spôsobiť chybu časového limitu vo workflow.
> - **Dočasné problémy so serverom:** Občasné výpadky alebo údržba servera môžu spôsobiť dočasnú nedostupnosť URL počas overovania.

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.