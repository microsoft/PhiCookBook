<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7fe541373802e33568e94e13226d463c",
  "translation_date": "2025-07-09T19:06:13+00:00",
  "source_file": "md/03.FineTuning/Introduce_AzureML.md",
  "language_code": "uk"
}
-->
# **Вступ до Azure Machine Learning Service**

[Azure Machine Learning](https://ml.azure.com?WT.mc_id=aiml-138114-kinfeylo) — це хмарний сервіс для прискорення та управління життєвим циклом проєктів машинного навчання (ML).

Фахівці з ML, дата-сайентисти та інженери можуть використовувати його у своїй щоденній роботі, щоб:

- Навчати та розгортати моделі.
- Керувати операціями машинного навчання (MLOps).
- Ви можете створити модель у Azure Machine Learning або використати модель, побудовану на основі відкритих платформ, таких як PyTorch, TensorFlow або scikit-learn.
- Інструменти MLOps допомагають відстежувати, повторно навчати та повторно розгортати моделі.

## Для кого призначений Azure Machine Learning?

**Дата-сайентисти та ML-інженери**

Вони можуть використовувати інструменти для прискорення та автоматизації своїх щоденних робочих процесів.  
Azure ML надає можливості для забезпечення справедливості, пояснюваності, відстеження та аудиту.

**Розробники застосунків:**  
Вони можуть безшовно інтегрувати моделі у застосунки або сервіси.

**Розробники платформи**

Мають доступ до потужного набору інструментів, підтримуваних надійними API Azure Resource Manager.  
Ці інструменти дозволяють створювати розвинені ML-інструменти.

**Підприємства**

Працюючи в хмарі Microsoft Azure, підприємства отримують переваги знайомої безпеки та контролю доступу на основі ролей.  
Налаштовуйте проєкти для контролю доступу до захищених даних і конкретних операцій.

## Продуктивність для всієї команди  
Проєкти ML часто вимагають команди з різноманітними навичками для створення та підтримки.

Azure ML надає інструменти, які дозволяють:  
- Співпрацювати з командою через спільні ноутбуки, обчислювальні ресурси, безсерверні обчислення, дані та середовища.  
- Розробляти моделі з урахуванням справедливості, пояснюваності, відстеження та аудиту для виконання вимог щодо походження та відповідності.  
- Швидко та легко розгортати ML-моделі в масштабі, а також ефективно керувати ними за допомогою MLOps.  
- Запускати ML-навантаження будь-де з вбудованим управлінням, безпекою та відповідністю.

## Кросплатформенні інструменти

Кожен у команді ML може використовувати улюблені інструменти для виконання завдань.  
Чи то швидкі експерименти, налаштування гіперпараметрів, побудова конвеєрів або керування висновками — ви можете працювати через знайомі інтерфейси, зокрема:  
- Azure Machine Learning Studio  
- Python SDK (v2)  
- Azure CLI (v2)  
- Azure Resource Manager REST APIs

Під час удосконалення моделей і співпраці протягом усього циклу розробки ви можете ділитися та знаходити активи, ресурси й метрики у UI Azure Machine Learning studio.

## **LLM/SLM в Azure ML**

Azure ML додав багато функцій, пов’язаних з LLM/SLM, поєднуючи LLMOps і SLMOps для створення корпоративної платформи генеративного штучного інтелекту.

### **Каталог моделей**

Корпоративні користувачі можуть розгортати різні моделі відповідно до різних бізнес-сценаріїв через Каталог моделей і надавати послуги у форматі Model as Service для розробників або користувачів підприємства.

![models](../../../../imgs/03/ft/models.png)

Каталог моделей у Azure Machine Learning studio — це центр для пошуку та використання широкого спектра моделей, які дозволяють створювати генеративні AI-застосунки. Каталог містить сотні моделей від таких провайдерів, як Azure OpenAI service, Mistral, Meta, Cohere, Nvidia, Hugging Face, включно з моделями, навченими Microsoft. Моделі від провайдерів, окрім Microsoft, є продуктами сторонніх виробників (Non-Microsoft Products), як визначено в Умовах використання продуктів Microsoft, і підпадають під умови, надані разом із моделлю.

### **Конвеєр завдань**

Основна ідея конвеєра машинного навчання — розбити повне завдання ML на багатокроковий робочий процес. Кожен крок — це керований компонент, який можна розробляти, оптимізувати, налаштовувати та автоматизувати окремо. Кроки з’єднані через чітко визначені інтерфейси. Сервіс конвеєрів Azure Machine Learning автоматично координує всі залежності між кроками.

Під час тонкого налаштування SLM / LLM ми можемо керувати даними, навчанням і процесами генерації через Pipeline.

![finetuning](../../../../imgs/03/ft/finetuning.png)

### **Prompt flow**

Переваги використання Azure Machine Learning prompt flow  
Azure Machine Learning prompt flow пропонує низку переваг, які допомагають користувачам перейти від ідеї до експериментів і, зрештою, до готових до виробництва застосунків на основі LLM:

**Гнучкість у розробці промптів**

Інтерактивний досвід створення: Azure Machine Learning prompt flow надає візуальне представлення структури потоку, що дозволяє користувачам легко розуміти та орієнтуватися у своїх проєктах. Також доступний досвід кодування, схожий на роботу з ноутбуком, для ефективної розробки та налагодження потоку.  
Варіанти для налаштування промптів: користувачі можуть створювати та порівнювати кілька варіантів промптів, що сприяє ітеративному вдосконаленню.

Оцінка: вбудовані потоки оцінки дозволяють користувачам оцінювати якість і ефективність своїх промптів і потоків.

Комплексні ресурси: Azure Machine Learning prompt flow включає бібліотеку вбудованих інструментів, зразків і шаблонів, які слугують відправною точкою для розробки, надихають на творчість і прискорюють процес.

**Готовність до корпоративного використання LLM-застосунків**

Співпраця: Azure Machine Learning prompt flow підтримує командну роботу, дозволяючи кільком користувачам спільно працювати над проєктами з розробки промптів, ділитися знаннями та підтримувати контроль версій.

Все в одному: Azure Machine Learning prompt flow оптимізує весь процес розробки промптів — від створення та оцінки до розгортання та моніторингу. Користувачі можуть легко розгортати свої потоки як кінцеві точки Azure Machine Learning і відстежувати їхню продуктивність у реальному часі, забезпечуючи оптимальну роботу та постійне вдосконалення.

Корпоративні рішення Azure Machine Learning: Prompt flow використовує надійні корпоративні рішення Azure Machine Learning, забезпечуючи безпечну, масштабовану та надійну основу для розробки, експериментів і розгортання потоків.

З Azure Machine Learning prompt flow користувачі можуть розкрити свою гнучкість у розробці промптів, ефективно співпрацювати та використовувати корпоративні рішення для успішної розробки та розгортання застосунків на основі LLM.

Поєднуючи обчислювальні потужності, дані та різні компоненти Azure ML, корпоративні розробники можуть легко створювати власні застосунки штучного інтелекту.

**Відмова від відповідальності**:  
Цей документ було перекладено за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується звертатися до професійного людського перекладу. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.