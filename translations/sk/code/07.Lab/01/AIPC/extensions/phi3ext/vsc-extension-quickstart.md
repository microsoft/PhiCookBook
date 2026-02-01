# Vitajte vo vašom rozšírení VS Code

## Čo sa nachádza v priečinku

* Tento priečinok obsahuje všetky súbory potrebné pre vaše rozšírenie.
* `package.json` - manifestový súbor, v ktorom deklarujete svoje rozšírenie a príkaz.
  * Ukážkový plugin zaregistruje príkaz a definuje jeho názov a meno príkazu. Na základe týchto informácií môže VS Code zobraziť príkaz v palete príkazov. Plugin sa pritom ešte nemusí načítať.
* `src/extension.ts` - hlavný súbor, kde implementujete svoj príkaz.
  * Súbor exportuje jednu funkciu, `activate`, ktorá sa zavolá pri prvom aktivovaní rozšírenia (v tomto prípade vykonaním príkazu). Vo funkcii `activate` voláme `registerCommand`.
  * Funkciu obsahujúcu implementáciu príkazu odovzdávame ako druhý parameter do `registerCommand`.

## Nastavenie

* nainštalujte odporúčané rozšírenia (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner a dbaeumer.vscode-eslint)

## Začnite hneď

* Stlačte `F5` pre otvorenie nového okna s načítaným rozšírením.
* Spustite svoj príkaz z palety príkazov stlačením (`Ctrl+Shift+P` alebo `Cmd+Shift+P` na Macu) a zadaním `Hello World`.
* Nastavte breakpointy vo svojom kóde v `src/extension.ts` pre ladenie rozšírenia.
* Výstup z rozšírenia nájdete v debug konzole.

## Upravujte

* Po zmene kódu v `src/extension.ts` môžete rozšírenie znovu spustiť z debug panela.
* Tiež môžete obnoviť (`Ctrl+R` alebo `Cmd+R` na Macu) okno VS Code s vaším rozšírením, aby sa načítali zmeny.

## Preskúmajte API

* Kompletnú sadu API nájdete v súbore `node_modules/@types/vscode/index.d.ts`.

## Spustite testy

* Nainštalujte [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* Spustite úlohu "watch" cez príkaz **Tasks: Run Task**. Uistite sa, že beží, inak sa testy nemusia nájsť.
* Otvorte zobrazenie Testing z aktivity a kliknite na tlačidlo "Run Test", alebo použite klávesovú skratku `Ctrl/Cmd + ; A`
* Výsledky testov uvidíte v zobrazení Test Results.
* Upravujte `src/test/extension.test.ts` alebo vytvárajte nové testovacie súbory v priečinku `test`.
  * Poskytnutý test runner bude brať do úvahy len súbory, ktoré zodpovedajú vzoru `**.test.ts`.
  * V priečinku `test` môžete vytvárať podpriečinky na ľubovoľné usporiadanie testov.

## Pokročilé možnosti

* Zmenšite veľkosť rozšírenia a zrýchlite jeho spustenie pomocou [bundlovania rozšírenia](https://code.visualstudio.com/api/working-with-extensions/bundling-extension?WT.mc_id=aiml-137032-kinfeylo).
* [Publikujte svoje rozšírenie](https://code.visualstudio.com/api/working-with-extensions/publishing-extension?WT.mc_id=aiml-137032-kinfeylo) na trhu VS Code rozšírení.
* Automatizujte buildy nastavením [Continuous Integration](https://code.visualstudio.com/api/working-with-extensions/continuous-integration?WT.mc_id=aiml-137032-kinfeylo).

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.