<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "eae2c0ea18160a3e7a63ace7b53897d7",
  "translation_date": "2025-05-09T04:59:03+00:00",
  "source_file": "code/07.Lab/01/AIPC/extensions/phi3ext/vsc-extension-quickstart.md",
  "language_code": "bg"
}
-->
# Добре дошли във вашето разширение за VS Code

## Какво има в папката

* Тази папка съдържа всички необходими файлове за вашето разширение.
* `package.json` - това е манифестният файл, в който декларирате разширението и командата си.
  * Примерният плъгин регистрира команда и определя нейното заглавие и име на командата. С тази информация VS Code може да покаже командата в командния палитър. Все още не е необходимо да зарежда плъгина.
* `src/extension.ts` - това е основният файл, където ще реализирате вашата команда.
  * Файлът експортира една функция, `activate`, която се извиква при първото активиране на разширението (в този случай при изпълнение на командата). Вътре във функцията `activate` извикваме `registerCommand`.
  * Като втори параметър на `registerCommand` подаваме функцията с реализацията на командата.

## Настройка

* Инсталирайте препоръчаните разширения (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner и dbaeumer.vscode-eslint)

## Стартирайте веднага

* Натиснете `F5`, за да отворите нов прозорец с заредено вашето разширение.
* Стартирайте командата си от командния палитър като натиснете (`Ctrl+Shift+P` или `Cmd+Shift+P` на Mac) и въведете `Hello World`.
* Поставяйте точки за спиране в кода си във `src/extension.ts`, за да отстранявате грешки в разширението.
* Намирайте изходните данни от разширението в конзолата за отстраняване на грешки.

## Направете промени

* Можете да рестартирате разширението от лентата за отстраняване на грешки след промяна на кода в `src/extension.ts`.
* Можете също да презаредите (`Ctrl+R` или `Cmd+R` на Mac) прозореца на VS Code с вашето разширение, за да заредите промените.

## Разгледайте API-то

* Можете да отворите пълния набор от API, като отворите файла `node_modules/@types/vscode/index.d.ts`.

## Стартирайте тестове

* Инсталирайте [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* Стартирайте задачата "watch" чрез командата **Tasks: Run Task**. Уверете се, че тя работи, в противен случай тестовете може да не бъдат открити.
* Отворете изгледа Testing от лентата с активности и натиснете бутона Run Test или използвайте клавишната комбинация `Ctrl/Cmd + ; A`
* Вижте резултата от теста в изгледа Test Results.
* Направете промени в `src/test/extension.test.ts` или създайте нови тестови файлове в папката `test`.
  * Предоставеният тестов изпълнител ще разглежда само файлове, които съвпадат с името `**.test.ts`.
  * Можете да създавате папки вътре в `test`, за да структурирате тестовете си както желаете.

## Отидете по-далеч

* Намалете размера на разширението и подобрете времето за стартиране, като [опаковате разширението](https://code.visualstudio.com/api/working-with-extensions/bundling-extension?WT.mc_id=aiml-137032-kinfeylo).
* [Публикувайте разширението си](https://code.visualstudio.com/api/working-with-extensions/publishing-extension?WT.mc_id=aiml-137032-kinfeylo) в маркетплейса за VS Code разширения.
* Автоматизирайте билдовете, като настроите [непрекъсната интеграция](https://code.visualstudio.com/api/working-with-extensions/continuous-integration?WT.mc_id=aiml-137032-kinfeylo).

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI преводаческа услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия първичен език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за никакви недоразумения или неправилни тълкувания, произтичащи от използването на този превод.