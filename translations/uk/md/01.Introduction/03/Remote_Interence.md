# Віддалене інференсування з донавченою моделлю

Після навчання адаптерів у віддаленому середовищі, використовуйте простий додаток Gradio для взаємодії з моделлю.

![Навчання завершено](../../../../../translated_images/uk/log-finetuning-res.7b92254e7e822c7f.webp)

### Налаштування ресурсів Azure  
Для віддаленого інференсування потрібно налаштувати ресурси Azure, виконавши команду `AI Toolkit: Provision Azure Container Apps for inference` з палітри команд. Під час цього процесу вам буде запропоновано вибрати підписку Azure та групу ресурсів.  
![Налаштування ресурсу для інференсування](../../../../../translated_images/uk/command-provision-inference.467afc8d351642fc.webp)
   
За замовчуванням підписка та група ресурсів для інференсування мають збігатися з тими, що використовувалися для донавчання. Інференсування використовуватиме те саме середовище Azure Container App і матиме доступ до моделі та адаптера моделі, збережених у Azure Files, які були створені під час кроку донавчання.

## Використання AI Toolkit

### Розгортання для інференсування  
Якщо потрібно змінити код інференсування або перезавантажити модель для інференсування, виконайте команду `AI Toolkit: Deploy for inference`. Це синхронізує ваш останній код з ACA та перезапустить репліку.

![Розгортання для інференсування](../../../../../translated_images/uk/command-deploy.9adb4e310dd0b0ae.webp)

Після успішного завершення розгортання модель готова до оцінки через цей endpoint.

### Доступ до API інференсування

Ви можете отримати доступ до API інференсування, натиснувши кнопку "*Go to Inference Endpoint*" у сповіщенні VSCode. Також веб-адресу API можна знайти у `ACA_APP_ENDPOINT` у файлі `./infra/inference.config.json` та у панелі виводу.

![Endpoint додатку](../../../../../translated_images/uk/notification-deploy.446e480a44b1be58.webp)

> **Note:** Endpoint інференсування може потребувати кілька хвилин для повного запуску.

## Компоненти інференсування, включені в шаблон

| Папка | Вміст |
| ------ |--------- |
| `infra` | Містить усі необхідні конфігурації для віддаленої роботи. |
| `infra/provision/inference.parameters.json` | Містить параметри для bicep-шаблонів, які використовуються для налаштування ресурсів Azure для інференсування. |
| `infra/provision/inference.bicep` | Містить шаблони для налаштування ресурсів Azure для інференсування. |
| `infra/inference.config.json` | Файл конфігурації, створений командою `AI Toolkit: Provision Azure Container Apps for inference`. Використовується як вхідні дані для інших віддалених команд. |

### Використання AI Toolkit для налаштування ресурсів Azure  
Налаштуйте [AI Toolkit](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

Виконайте команду `Provision Azure Container Apps for inference`.

Параметри конфігурації можна знайти у файлі `./infra/provision/inference.parameters.json`. Ось деталі:
| Параметр | Опис |
| --------- |------------ |
| `defaultCommands` | Команди для запуску веб-API. |
| `maximumInstanceCount` | Максимальна кількість GPU-інстансів. |
| `location` | Локація, де будуть створені ресурси Azure. За замовчуванням збігається з локацією вибраної групи ресурсів. |
| `storageAccountName`, `fileShareName`, `acaEnvironmentName`, `acaEnvironmentStorageName`, `acaAppName`,  `acaLogAnalyticsName` | Ці параметри використовуються для іменування ресурсів Azure. За замовчуванням вони співпадають з іменами ресурсів для донавчання. Ви можете вказати нові, невикористані імена для створення власних ресурсів або вказати імена вже існуючих ресурсів Azure, якщо хочете їх використовувати. Детальніше див. у розділі [Використання існуючих ресурсів Azure](../../../../../md/01.Introduction/03). |

### Використання існуючих ресурсів Azure

За замовчуванням для інференсування використовуються ті ж середовище Azure Container App, обліковий запис зберігання, Azure File Share та Azure Log Analytics, що й для донавчання. Окремий Azure Container App створюється виключно для API інференсування.

Якщо ви налаштовували ресурси Azure під час донавчання або хочете використовувати власні існуючі ресурси Azure для інференсування, вкажіть їхні імена у файлі `./infra/inference.parameters.json`. Потім виконайте команду `AI Toolkit: Provision Azure Container Apps for inference` з палітри команд. Це оновить вказані ресурси та створить відсутні.

Наприклад, якщо у вас є існуюче середовище Azure Container, ваш файл `./infra/finetuning.parameters.json` має виглядати так:

```json
{
    "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentParameters.json#",
    "contentVersion": "1.0.0.0",
    "parameters": {
      ...
      "acaEnvironmentName": {
        "value": "<your-aca-env-name>"
      },
      "acaEnvironmentStorageName": {
        "value": null
      },
      ...
    }
  }
```

### Ручне налаштування  
Якщо ви віддаєте перевагу ручному налаштуванню ресурсів Azure, можете скористатися bicep-файлами, що знаходяться у папках `./infra/provision`. Якщо ви вже налаштували всі ресурси Azure без використання палітри команд AI Toolkit, просто введіть імена ресурсів у файлі `inference.config.json`.

Наприклад:

```json
{
  "SUBSCRIPTION_ID": "<your-subscription-id>",
  "RESOURCE_GROUP_NAME": "<your-resource-group-name>",
  "STORAGE_ACCOUNT_NAME": "<your-storage-account-name>",
  "FILE_SHARE_NAME": "<your-file-share-name>",
  "ACA_APP_NAME": "<your-aca-name>",
  "ACA_APP_ENDPOINT": "<your-aca-endpoint>"
}
```

**Відмова від відповідальності**:  
Цей документ було перекладено за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується звертатися до професійного людського перекладу. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.