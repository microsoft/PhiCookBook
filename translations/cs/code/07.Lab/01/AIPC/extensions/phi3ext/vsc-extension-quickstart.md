<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "eae2c0ea18160a3e7a63ace7b53897d7",
  "translation_date": "2025-05-09T04:58:33+00:00",
  "source_file": "code/07.Lab/01/AIPC/extensions/phi3ext/vsc-extension-quickstart.md",
  "language_code": "cs"
}
-->
# Welcome to your VS Code Extension

## What's in the folder

* This folder contains all of the files necessary for your extension.
* `package.json` - это манифест-файл, в котором вы объявляете своё расширение и команду.
  * Пример плагина регистрирует команду и задаёт её заголовок и имя команды. С этой информацией VS Code может показать команду в палитре команд. При этом плагин ещё не загружается.
* `src/extension.ts` - это основной файл, в котором вы реализуете свою команду.
  * Файл экспортирует одну функцию, `activate`, которая вызывается при первом запуске расширения (в данном случае при выполнении команды). Внутри функции `activate` мы вызываем `registerCommand`.
  * В качестве второго параметра в `registerCommand` передаётся функция с реализацией команды.

## Setup

* установите рекомендуемые расширения (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner и dbaeumer.vscode-eslint)


## Get up and running straight away

* Нажмите `F5`, чтобы открыть новое окно с загруженным расширением.
* Запустите команду из палитры команд, нажав (`Ctrl+Shift+P` или `Cmd+Shift+P` на Mac) и введя `Hello World`.
* Установите точки останова в коде внутри `src/extension.ts` для отладки расширения.
* Просматривайте вывод расширения в консоли отладки.

## Make changes

* Вы можете перезапустить расширение с панели отладки после изменения кода в `src/extension.ts`.
* Также можно перезагрузить (`Ctrl+R` или `Cmd+R` на Mac) окно VS Code с расширением, чтобы применить изменения.


## Explore the API

* Полный набор API доступен в файле `node_modules/@types/vscode/index.d.ts`.

## Run tests

* Установите [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* Запустите задачу "watch" через команду **Tasks: Run Task**. Убедитесь, что она работает, иначе тесты не будут обнаружены.
* Откройте представление Testing на панели активности и нажмите кнопку Run Test, или используйте горячую клавишу `Ctrl/Cmd + ; A`
* Результаты тестов отображаются в представлении Test Results.
* Вносите изменения в `src/test/extension.test.ts` или создавайте новые тесты в папке `test`.
  * Тест-раннер учитывает только файлы, соответствующие шаблону имени `**.test.ts`.
  * Вы можете создавать подпапки внутри `test` для удобной организации тестов.

## Go further

* Уменьшите размер расширения и ускорьте запуск, [объединив ваше расширение](https://code.visualstudio.com/api/working-with-extensions/bundling-extension?WT.mc_id=aiml-137032-kinfeylo).
* [Опубликуйте расширение](https://code.visualstudio.com/api/working-with-extensions/publishing-extension?WT.mc_id=aiml-137032-kinfeylo) в магазине расширений VS Code.
* Автоматизируйте сборки, настроив [непрерывную интеграцию](https://code.visualstudio.com/api/working-with-extensions/continuous-integration?WT.mc_id=aiml-137032-kinfeylo).

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.