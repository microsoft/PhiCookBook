<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "eae2c0ea18160a3e7a63ace7b53897d7",
  "translation_date": "2025-05-09T04:58:42+00:00",
  "source_file": "code/07.Lab/01/AIPC/extensions/phi3ext/vsc-extension-quickstart.md",
  "language_code": "sk"
}
-->
# Vitajte vo vašom rozšírení VS Code

## Čo je v priečinku

* Tento priečinok obsahuje všetky súbory potrebné pre vaše rozšírenie.
* `package.json` - toto je manifestový súbor, v ktorom deklarujete svoje rozšírenie a príkaz.
  * Ukážkový plugin zaregistruje príkaz a definuje jeho názov a meno príkazu. Na základe týchto informácií môže VS Code zobraziť príkaz v palete príkazov. Plugin ešte nemusí byť načítaný.
* `src/extension.ts` - toto je hlavný súbor, kde poskytnete implementáciu svojho príkazu.
  * Súbor exportuje jednu funkciu, `activate`, ktorá sa zavolá pri prvom aktivovaní rozšírenia (v tomto prípade spustením príkazu). Vo funkcii `activate` voláme `registerCommand`.
  * Funkciu obsahujúcu implementáciu príkazu odovzdávame ako druhý parameter do `registerCommand`.

## Nastavenie

* nainštalujte odporúčané rozšírenia (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner a dbaeumer.vscode-eslint)

## Začnite hneď

* Stlačte `F5` pre otvorenie nového okna s načítaným rozšírením.
* Spustite svoj príkaz z palety príkazov stlačením (`Ctrl+Shift+P` alebo `Cmd+Shift+P` na Macu) a zadaním `Hello World`.
* Nastavte body prerušenia vo vašom kóde v `src/extension.ts` pre ladenie rozšírenia.
* Výstup z rozšírenia nájdete v debug konzole.

## Urobte zmeny

* Po zmene kódu v `src/extension.ts` môžete rozšírenie znovu spustiť z debug panela.
* Môžete tiež obnoviť (`Ctrl+R` alebo `Cmd+R` na Macu) okno VS Code s vaším rozšírením, aby sa načítali zmeny.

## Preskúmajte API

* Celú sadu nášho API môžete otvoriť v súbore `node_modules/@types/vscode/index.d.ts`.

## Spustite testy

* Nainštalujte [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* Spustite úlohu "watch" cez príkaz **Tasks: Run Task**. Uistite sa, že beží, inak testy nemusia byť nájdené.
* Otvorte zobrazenie Testing z aktivity panela a kliknite na tlačidlo Run Test, alebo použite klávesovú skratku `Ctrl/Cmd + ; A`
* Výsledky testov uvidíte v zobrazení Test Results.
* Robte zmeny v `src/test/extension.test.ts` alebo vytvárajte nové testovacie súbory v priečinku `test`.
  * Poskytnutý test runner bude brať do úvahy iba súbory, ktoré zodpovedajú vzoru názvu `**.test.ts`.
  * V priečinku `test` môžete vytvárať podpriečinky podľa potreby na štruktúrovanie testov.

## Pokročilé možnosti

* Zmenšite veľkosť rozšírenia a zrýchlite jeho spustenie pomocou [zabalenia rozšírenia](https://code.visualstudio.com/api/working-with-extensions/bundling-extension?WT.mc_id=aiml-137032-kinfeylo).
* [Publikujte svoje rozšírenie](https://code.visualstudio.com/api/working-with-extensions/publishing-extension?WT.mc_id=aiml-137032-kinfeylo) na trhu rozšírení VS Code.
* Automatizujte zostavovanie nastavením [Continuous Integration](https://code.visualstudio.com/api/working-with-extensions/continuous-integration?WT.mc_id=aiml-137032-kinfeylo).

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, berte prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne výklady vyplývajúce z použitia tohto prekladu.