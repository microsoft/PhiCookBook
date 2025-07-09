<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "00b7a699de8ac405fa821f4c0f7fc0ab",
  "translation_date": "2025-07-09T19:32:14+00:00",
  "source_file": "md/02.Application/02.Code/Phi3/VSCodeExt/README.md",
  "language_code": "uk"
}
-->
# **Створіть власний GitHub Copilot Chat для Visual Studio Code з Microsoft Phi-3 Family**

Ви вже користувалися агентом робочого простору в GitHub Copilot Chat? Хочете створити власного агента для коду вашої команди? Цей практичний лабораторний курс покликаний поєднати відкриту модель для створення корпоративного агента для роботи з кодом.

## **Основи**

### **Чому обирають Microsoft Phi-3**

Phi-3 — це сімейство моделей, яке включає phi-3-mini, phi-3-small та phi-3-medium, що відрізняються параметрами навчання для генерації тексту, завершення діалогів та генерації коду. Також є phi-3-vision, що базується на Vision. Воно підходить для підприємств або різних команд для створення офлайн-рішень генеративного штучного інтелекту.

Рекомендуємо ознайомитися з цим посиланням [https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md](https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md)

### **Microsoft GitHub Copilot Chat**

Розширення GitHub Copilot Chat надає інтерфейс чату, який дозволяє взаємодіяти з GitHub Copilot і отримувати відповіді на питання, пов’язані з програмуванням, безпосередньо у VS Code, без необхідності шукати документацію чи форуми в інтернеті.

Copilot Chat може використовувати підсвічування синтаксису, відступи та інші форматування для кращої зрозумілості згенерованої відповіді. Залежно від типу запиту користувача, результат може містити посилання на контекст, який Copilot використав для формування відповіді, наприклад, файли з кодом або документацію, а також кнопки для доступу до функцій VS Code.

- Copilot Chat інтегрується у ваш робочий процес розробника і надає допомогу там, де це потрібно:

- Починайте чат безпосередньо з редактора або терміналу, щоб отримати допомогу під час кодування

- Використовуйте вигляд Chat, щоб мати AI-помічника поруч у будь-який момент

- Запускайте Quick Chat, щоб швидко поставити питання і повернутися до роботи

GitHub Copilot Chat можна використовувати у різних сценаріях, таких як:

- Відповіді на питання щодо кращих способів розв’язання проблеми

- Пояснення чужого коду та пропозиції щодо покращень

- Пропозиції виправлень коду

- Генерація юніт-тестів

- Генерація документації коду

Рекомендуємо ознайомитися з цим посиланням [https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/copilot-chat?WT.mc_id=aiml-137032-kinfeylo)

###  **Microsoft GitHub Copilot Chat @workspace**

Використання **@workspace** у Copilot Chat дозволяє ставити питання щодо всього вашого коду. Виходячи з запиту, Copilot інтелектуально знаходить релевантні файли та символи, які потім використовує у відповіді у вигляді посилань та прикладів коду.

Для відповіді на ваше питання **@workspace** шукає інформацію у тих же джерелах, що й розробник при навігації по кодовій базі у VS Code:

- Всі файли у робочому просторі, окрім тих, що ігноруються файлом .gitignore

- Структура директорій з вкладеними папками та назвами файлів

- Індекс пошуку коду GitHub, якщо робочий простір є репозиторієм GitHub і проіндексований пошуком коду

- Символи та визначення у робочому просторі

- Поточний виділений текст або видимий текст у активному редакторі

Примітка: .gitignore ігнорується, якщо у вас відкритий файл або виділено текст у файлі, який ігнорується.

Рекомендуємо ознайомитися з цим посиланням [[https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/workspace-context?WT.mc_id=aiml-137032-kinfeylo)]

## **Дізнайтеся більше про цей лабораторний курс**

GitHub Copilot значно підвищив ефективність програмування в підприємствах, і кожне підприємство прагне налаштувати відповідні функції GitHub Copilot під свої потреби. Багато підприємств створили власні розширення, схожі на GitHub Copilot, базуючись на своїх бізнес-сценаріях та відкритих моделях. Для підприємств кастомізовані розширення легше контролювати, але це також впливає на користувацький досвід. Адже GitHub Copilot має потужніші функції для загальних сценаріїв і професіоналізму. Якщо вдасться зберегти послідовний досвід, то краще створити власне корпоративне розширення. GitHub Copilot Chat надає відповідні API для розширення досвіду чату в підприємствах. Підтримка послідовного досвіду разом із кастомізованими функціями — це кращий користувацький досвід.

У цьому лабораторному курсі використовується модель Phi-3 у поєднанні з локальним NPU та гібридом Azure для створення кастомного агента в GitHub Copilot Chat ***@PHI3***, який допомагає корпоративним розробникам у генерації коду***(@PHI3 /gen)*** та створенні коду на основі зображень ***(@PHI3 /img)***.

![PHI3](../../../../../../../imgs/02/vscodeext/cover.png)

### ***Примітка:*** 

Цей лабораторний курс наразі реалізований на AIPC Intel CPU та Apple Silicon. Ми продовжимо оновлення для версії Qualcomm NPU.

## **Лабораторна робота**

| Назва | Опис | AIPC | Apple |
| ------------ | ----------- | -------- |-------- |
| Lab0 - Встановлення(✅) | Налаштування та встановлення необхідних середовищ і інструментів | [Перейти](./HOL/AIPC/01.Installations.md) |[Перейти](./HOL/Apple/01.Installations.md) |
| Lab1 - Запуск Prompt flow з Phi-3-mini (✅) | У поєднанні з AIPC / Apple Silicon, використання локального NPU для генерації коду через Phi-3-mini | [Перейти](./HOL/AIPC/02.PromptflowWithNPU.md) |  [Перейти](./HOL/Apple/02.PromptflowWithMLX.md) |
| Lab2 - Розгортання Phi-3-vision на Azure Machine Learning Service(✅) | Генерація коду шляхом розгортання каталогу моделей Azure Machine Learning Service - Phi-3-vision image | [Перейти](./HOL/AIPC/03.DeployPhi3VisionOnAzure.md) |[Перейти](./HOL/Apple/03.DeployPhi3VisionOnAzure.md) |
| Lab3 - Створення агента @phi-3 у GitHub Copilot Chat(✅)  | Створення кастомного агента Phi-3 у GitHub Copilot Chat для генерації коду, коду графіки, RAG тощо | [Перейти](./HOL/AIPC/04.CreatePhi3AgentInVSCode.md) | [Перейти](./HOL/Apple/04.CreatePhi3AgentInVSCode.md) |
| Приклад коду (✅)  | Завантаження прикладу коду | [Перейти](../../../../../../../code/07.Lab/01/AIPC) | [Перейти](../../../../../../../code/07.Lab/01/Apple) |

## **Ресурси**

1. Phi-3 Cookbook [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook)

2. Дізнайтеся більше про GitHub Copilot [https://learn.microsoft.com/training/paths/copilot/](https://learn.microsoft.com/training/paths/copilot/?WT.mc_id=aiml-137032-kinfeylo)

3. Дізнайтеся більше про GitHub Copilot Chat [https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/](https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/?WT.mc_id=aiml-137032-kinfeylo)

4. Дізнайтеся більше про GitHub Copilot Chat API [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat?WT.mc_id=aiml-137032-kinfeylo)

5. Дізнайтеся більше про Azure AI Foundry [https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/](https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/?WT.mc_id=aiml-137032-kinfeylo)

6. Дізнайтеся більше про каталог моделей Azure AI Foundry [https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview)

**Відмова від відповідальності**:  
Цей документ було перекладено за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується звертатися до професійного людського перекладу. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.