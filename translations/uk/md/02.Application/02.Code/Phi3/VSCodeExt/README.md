# **Створіть власний Visual Studio Code GitHub Copilot Chat з Microsoft Phi-3 Family**

Ви користувалися агентом робочого простору в GitHub Copilot Chat? Бажаєте створити власного агенту коду для вашої команди? Цей практичний лабораторний проєкт покликаний об’єднати відкриту модель для створення корпоративного агенту бізнес-коду.

## **Основи**

### **Чому обирають Microsoft Phi-3**

Phi-3 — це серія сімейства, що включає phi-3-mini, phi-3-small і phi-3-medium, основані на різних параметрах навчання для генерації тексту, завершення діалогів і генерації коду. Також є phi-3-vision на основі Vision. Він підходить для підприємств або різних команд для створення офлайн-рішень генеративного ШІ.

Рекомендуємо прочитати цей посилання [https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md](https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md)

### **Microsoft GitHub Copilot Chat**

Розширення GitHub Copilot Chat надає інтерфейс чату, який дозволяє вам взаємодіяти з GitHub Copilot і отримувати відповіді на питання, пов’язані з програмуванням, безпосередньо у VS Code, без необхідності шукати документацію або форуми в Інтернеті.

Copilot Chat може використовувати підсвітку синтаксису, відступи та інші функції форматування для покращення зрозумілості згенерованої відповіді. Залежно від типу запитання користувача, результат може містити посилання на контекст, який Copilot використав для створення відповіді, такі як файли вихідного коду або документація, або кнопки для доступу до функціональності VS Code.

- Copilot Chat інтегрується у ваш робочий процес розробника і надає допомогу там, де це потрібно:

- Починайте розмову вбудованого чату безпосередньо з редактора або терміналу для допомоги під час кодування

- Використовуйте перегляд Чату, щоб мати помічника на базі ШІ поруч, який допоможе вам у будь-який час

- Запускайте Швидкий Чат, щоб швидко поставити запитання і повернутися до роботи

Ви можете використовувати GitHub Copilot Chat у різних сценаріях, таких як:

- Відповідь на питання програмування щодо найкращого способу розв’язання задачі

- Пояснення чужого коду і пропозиції щодо покращень

- Запропонування виправлень коду

- Генерація юніт-тестів

- Генерація документації коду

Рекомендуємо прочитати це посилання [https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/copilot-chat?WT.mc_id=aiml-137032-kinfeylo)


###  **Microsoft GitHub Copilot Chat @workspace**

Звернення до **@workspace** в Copilot Chat дозволяє ставити питання про весь ваш кодовий базис. Відповідно до питання, Copilot інтелектуально отримує відповідні файли та символи, які потім посилає у відповіді у вигляді посилань і прикладів коду.

Для відповіді на ваше питання **@workspace** здійснює пошук по тих самих джерелах, які розробник використовував би для переміщення по кодовій базі у VS Code:

- Всі файли у робочому просторі, крім тих, які ігноруються файлом .gitignore

- Структура директорій з вкладеними папками та іменами файлів

- Індекс пошуку коду GitHub, якщо робочий простір є репозиторієм GitHub і проіндексовано пошуком коду

- Символи та визначення у робочому просторі

- Поточний вибраний текст або видимий текст у активному редакторі

Примітка: .gitignore ігнорується, якщо у вас відкритий файл або ви вибрали текст у проігнорованому файлі.

Рекомендуємо прочитати це посилання [[https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/workspace-context?WT.mc_id=aiml-137032-kinfeylo)]


## **Дізнайтеся більше про цю лабораторну роботу**

GitHub Copilot значно підвищив ефективність програмування в підприємствах, і кожне підприємство хоче налаштувати відповідні функції GitHub Copilot. Багато підприємств створили налаштовані розширення, схожі на GitHub Copilot, на основі власних бізнес-сценаріїв і відкритих моделей. Для підприємств налаштовані розширення легше контролювати, але це також впливає на користувацький досвід. Адже GitHub Copilot має потужніші функції для роботи з загальними сценаріями і високою професійністю. Якщо досвід можна зберегти послідовним, краще кастомізувати власне розширення підприємства. GitHub Copilot Chat надає відповідні API для розширення корпоративного досвіду спілкування. Підтримка узгодженого досвіду і наявність налаштованих функцій — це кращий користувацький досвід.

У цій лабораторній роботі головним чином використовується модель Phi-3 у поєднанні з локальним NPU та гібридом Azure для створення кастомного агенту в GitHub Copilot Chat ***@PHI3*** для допомоги корпоративним розробникам у завершенні генерації коду***(@PHI3 /gen)*** та генерації коду на основі зображень ***(@PHI3 /img)***.

![PHI3](../../../../../../../translated_images/uk/cover.1017ebc9a7c46d09.webp)

### ***Примітка:*** 

Ця лабораторія наразі реалізується на AIPC для Intel CPU і Apple Silicon. Ми продовжимо оновлення версії Qualcomm NPU.


## **Лабораторна робота**


| Назва | Опис | AIPC | Apple |
| ------------ | ----------- | -------- |-------- |
| Lab0 - Встановлення (✅) | Налаштування та інсталяція відповідних середовищ і інструментів | [Go](./HOL/AIPC/01.Installations.md) |[Go](./HOL/Apple/01.Installations.md) |
| Lab1 - Запуск Prompt flow з Phi-3-mini (✅) | Спільно з AIPC / Apple Silicon, використання локального NPU для створення генерації коду через Phi-3-mini | [Go](./HOL/AIPC/02.PromptflowWithNPU.md) |  [Go](./HOL/Apple/02.PromptflowWithMLX.md) |
| Lab2 - Розгортання Phi-3-vision на Azure Machine Learning Service (✅) | Генерація коду шляхом розгортання Model Catalog Azure Machine Learning Service – зображення Phi-3-vision | [Go](./HOL/AIPC/03.DeployPhi3VisionOnAzure.md) |[Go](./HOL/Apple/03.DeployPhi3VisionOnAzure.md) |
| Lab3 - Створення агенту @phi-3 в GitHub Copilot Chat (✅)  | Створення кастомного агента Phi-3 в GitHub Copilot Chat для завершення генерації коду, генерації коду графіки, RAG тощо. | [Go](./HOL/AIPC/04.CreatePhi3AgentInVSCode.md) | [Go](./HOL/Apple/04.CreatePhi3AgentInVSCode.md) |
| Зразок коду (✅)  | Завантажити приклад коду | [Go](../../../../../../../code/07.Lab/01/AIPC) | [Go](../../../../../../../code/07.Lab/01/Apple) |


## **Ресурси**

1. Phi-3 Cookbook [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook)

2. Дізнайтеся більше про GitHub Copilot [https://learn.microsoft.com/training/paths/copilot/](https://learn.microsoft.com/training/paths/copilot/?WT.mc_id=aiml-137032-kinfeylo)

3. Дізнайтеся більше про GitHub Copilot Chat [https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/](https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/?WT.mc_id=aiml-137032-kinfeylo)

4. Дізнайтеся більше про GitHub Copilot Chat API [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat?WT.mc_id=aiml-137032-kinfeylo)

5. Дізнайтеся більше про Microsoft Foundry [https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/](https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/?WT.mc_id=aiml-137032-kinfeylo)

6. Дізнайтеся більше про Model Catalog Microsoft Foundry [https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмову від відповідальності**:
Цей документ був перекладений за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критичної інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->