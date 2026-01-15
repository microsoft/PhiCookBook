<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5113634b77370af6790f9697d5d7de90",
  "translation_date": "2025-07-17T05:43:38+00:00",
  "source_file": "md/02.QuickStart/GitHubModel_QuickStart.md",
  "language_code": "uk"
}
-->
## GitHub Models - Обмежена публічна бета

Ласкаво просимо до [GitHub Models](https://github.com/marketplace/models)! Усе готово, щоб ви могли досліджувати AI-моделі, розміщені на Azure AI.

![GitHubModel](../../../../translated_images/uk/GitHub_ModelCatalog.aa43c51c36454747.png)

Для отримання додаткової інформації про моделі, доступні на GitHub Models, перегляньте [GitHub Model Marketplace](https://github.com/marketplace/models)

## Доступні моделі

Кожна модель має власний майданчик для тестування та приклади коду

![Phi-3Model_Github](../../../../imgs/01/02/02/GitHub_ModelPlay.png)

### Phi-3 Моделі в каталозі GitHub Model

[Phi-3-Medium-128k-Instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-128k-instruct)

[Phi-3-medium-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-4k-instruct)

[Phi-3-mini-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-128k-instruct)

[Phi-3-mini-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-4k-instruct)

[Phi-3-small-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-128k-instruct)

[Phi-3-small-8k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-8k-instruct)

## Початок роботи

Є кілька базових прикладів, готових до запуску. Ви можете знайти їх у каталозі samples. Якщо хочете одразу перейти до улюбленої мови програмування, приклади доступні для таких мов:

- Python
- JavaScript
- cURL

Також є спеціальне середовище Codespaces для запуску прикладів і моделей.

![Getting Started](../../../../translated_images/uk/GitHub_ModelGetStarted.150220a802da6fb6.png)

## Приклад коду

Нижче наведені приклади коду для кількох сценаріїв використання. Для додаткової інформації про Azure AI Inference SDK дивіться повну документацію та приклади.

## Налаштування

1. Створіть персональний токен доступу  
Вам не потрібно надавати жодних дозволів для токена. Зверніть увагу, що токен буде надіслано до сервісу Microsoft.

Щоб використовувати наведені нижче фрагменти коду, створіть змінну середовища, в якій ваш токен буде ключем для клієнтського коду.

Якщо ви використовуєте bash:  
```
export GITHUB_TOKEN="<your-github-token-goes-here>"
```  
Якщо ви у powershell:  

```
$Env:GITHUB_TOKEN="<your-github-token-goes-here>"
```  

Якщо ви використовуєте командний рядок Windows:  

```
set GITHUB_TOKEN=<your-github-token-goes-here>
```  

## Приклад на Python

### Встановлення залежностей  
Встановіть Azure AI Inference SDK за допомогою pip (потрібен Python версії >=3.8):

```
pip install azure-ai-inference
```  
### Запуск базового прикладу коду

Цей приклад демонструє базовий виклик API для завершення чату. Він використовує кінцеву точку GitHub AI model inference та ваш GitHub токен. Виклик синхронний.

```
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

endpoint = "https://models.inference.ai.azure.com"
# Replace Model_Name 
model_name = "Phi-3-small-8k-instruct"
token = os.environ["GITHUB_TOKEN"]

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

response = client.complete(
    messages=[
        SystemMessage(content="You are a helpful assistant."),
        UserMessage(content="What is the capital of France?"),
    ],
    model=model_name,
    temperature=1.,
    max_tokens=1000,
    top_p=1.
)

print(response.choices[0].message.content)
```

### Запуск багатокрокової розмови

Цей приклад демонструє багатокрокову розмову з API завершення чату. При використанні моделі для чат-додатку потрібно керувати історією розмови та надсилати моделі останні повідомлення.

```
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
# Replace Model_Name
model_name = "Phi-3-small-8k-instruct"

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

messages = [
    SystemMessage(content="You are a helpful assistant."),
    UserMessage(content="What is the capital of France?"),
    AssistantMessage(content="The capital of France is Paris."),
    UserMessage(content="What about Spain?"),
]

response = client.complete(messages=messages, model=model_name)

print(response.choices[0].message.content)
```

### Потокова передача результату

Для кращого користувацького досвіду варто транслювати відповідь моделі, щоб перший токен з’являвся швидко і не доводилось чекати довгі відповіді.

```
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
# Replace Model_Name
model_name = "Phi-3-small-8k-instruct"

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

response = client.complete(
    stream=True,
    messages=[
        SystemMessage(content="You are a helpful assistant."),
        UserMessage(content="Give me 5 good reasons why I should exercise every day."),
    ],
    model=model_name,
)

for update in response:
    if update.choices:
        print(update.choices[0].delta.content or "", end="")

client.close()
```

## JavaScript

### Встановлення залежностей

Встановіть Node.js.

Скопіюйте наведені рядки тексту та збережіть їх у файлі package.json у вашій папці.

```
{
  "type": "module",
  "dependencies": {
    "@azure-rest/ai-inference": "latest",
    "@azure/core-auth": "latest",
    "@azure/core-sse": "latest"
  }
}
```

Примітка: @azure/core-sse потрібен лише для потокової передачі відповіді чат-завершень.

Відкрийте термінал у цій папці та виконайте npm install.

Для кожного з наведених нижче фрагментів коду скопіюйте вміст у файл sample.js і запустіть командою node sample.js.

### Запуск базового прикладу коду

Цей приклад демонструє базовий виклик API для завершення чату. Він використовує кінцеву точку GitHub AI model inference та ваш GitHub токен. Виклик синхронний.

```
import ModelClient from "@azure-rest/ai-inference";
import { AzureKeyCredential } from "@azure/core-auth";

const token = process.env["GITHUB_TOKEN"];
const endpoint = "https://models.inference.ai.azure.com";
// Update your modelname
const modelName = "Phi-3-small-8k-instruct";

export async function main() {

  const client = new ModelClient(endpoint, new AzureKeyCredential(token));

  const response = await client.path("/chat/completions").post({
    body: {
      messages: [
        { role:"system", content: "You are a helpful assistant." },
        { role:"user", content: "What is the capital of France?" }
      ],
      model: modelName,
      temperature: 1.,
      max_tokens: 1000,
      top_p: 1.
    }
  });

  if (response.status !== "200") {
    throw response.body.error;
  }
  console.log(response.body.choices[0].message.content);
}

main().catch((err) => {
  console.error("The sample encountered an error:", err);
});
```

### Запуск багатокрокової розмови

Цей приклад демонструє багатокрокову розмову з API завершення чату. При використанні моделі для чат-додатку потрібно керувати історією розмови та надсилати моделі останні повідомлення.

```
import ModelClient from "@azure-rest/ai-inference";
import { AzureKeyCredential } from "@azure/core-auth";

const token = process.env["GITHUB_TOKEN"];
const endpoint = "https://models.inference.ai.azure.com";
// Update your modelname
const modelName = "Phi-3-small-8k-instruct";

export async function main() {

  const client = new ModelClient(endpoint, new AzureKeyCredential(token));

  const response = await client.path("/chat/completions").post({
    body: {
      messages: [
        { role: "system", content: "You are a helpful assistant." },
        { role: "user", content: "What is the capital of France?" },
        { role: "assistant", content: "The capital of France is Paris." },
        { role: "user", content: "What about Spain?" },
      ],
      model: modelName,
    }
  });

  if (response.status !== "200") {
    throw response.body.error;
  }

  for (const choice of response.body.choices) {
    console.log(choice.message.content);
  }
}

main().catch((err) => {
  console.error("The sample encountered an error:", err);
});
```

### Потокова передача результату

Для кращого користувацького досвіду варто транслювати відповідь моделі, щоб перший токен з’являвся швидко і не доводилось чекати довгі відповіді.

```
import ModelClient from "@azure-rest/ai-inference";
import { AzureKeyCredential } from "@azure/core-auth";
import { createSseStream } from "@azure/core-sse";

const token = process.env["GITHUB_TOKEN"];
const endpoint = "https://models.inference.ai.azure.com";
// Update your modelname
const modelName = "Phi-3-small-8k-instruct";

export async function main() {

  const client = new ModelClient(endpoint, new AzureKeyCredential(token));

  const response = await client.path("/chat/completions").post({
    body: {
      messages: [
        { role: "system", content: "You are a helpful assistant." },
        { role: "user", content: "Give me 5 good reasons why I should exercise every day." },
      ],
      model: modelName,
      stream: true
    }
  }).asNodeStream();

  const stream = response.body;
  if (!stream) {
    throw new Error("The response stream is undefined");
  }

  if (response.status !== "200") {
    stream.destroy();
    throw new Error(`Failed to get chat completions, http operation failed with ${response.status} code`);
  }

  const sseStream = createSseStream(stream);

  for await (const event of sseStream) {
    if (event.data === "[DONE]") {
      return;
    }
    for (const choice of (JSON.parse(event.data)).choices) {
        process.stdout.write(choice.delta?.content ?? ``);
    }
  }
}

main().catch((err) => {
  console.error("The sample encountered an error:", err);
});
```

## REST

### Запуск базового прикладу коду

Вставте наступне у shell:

```
curl -X POST "https://models.inference.ai.azure.com/chat/completions" \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $GITHUB_TOKEN" \
    -d '{
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "What is the capital of France?"
            }
        ],
        "model": "Phi-3-small-8k-instruct"
    }'
```

### Запуск багатокрокової розмови

Викличте API завершення чату та передайте історію розмови:

```
curl -X POST "https://models.inference.ai.azure.com/chat/completions" \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $GITHUB_TOKEN" \
    -d '{
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "What is the capital of France?"
            },
            {
                "role": "assistant",
                "content": "The capital of France is Paris."
            },
            {
                "role": "user",
                "content": "What about Spain?"
            }
        ],
        "model": "Phi-3-small-8k-instruct"
    }'
```

### Потокова передача результату

Це приклад виклику кінцевої точки з потоковою передачею відповіді.

```
curl -X POST "https://models.inference.ai.azure.com/chat/completions" \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $GITHUB_TOKEN" \
    -d '{
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "Give me 5 good reasons why I should exercise every day."
            }
        ],
        "stream": true,
        "model": "Phi-3-small-8k-instruct"
    }'
```

## Безкоштовне використання та обмеження швидкості для GitHub Models

![Model Catalog](../../../../translated_images/uk/GitHub_Model.ca6c125cb3117d0e.png)

[Обмеження швидкості для майданчика та безкоштовного використання API](https://docs.github.com/en/github-models/prototyping-with-ai-models#rate-limits) призначені для того, щоб ви могли експериментувати з моделями та прототипувати свій AI-додаток. Для використання понад ці ліміти та масштабування додатку потрібно виділити ресурси з облікового запису Azure та аутентифікуватися через нього замість персонального токена GitHub. Вам не потрібно змінювати інший код. Використайте це посилання, щоб дізнатися, як вийти за межі безкоштовного рівня в Azure AI.

### Відмови від відповідальності

Пам’ятайте, що при взаємодії з моделлю ви експериментуєте з AI, тому можливі помилки у вмісті.

Функція має різні обмеження (включно з кількістю запитів за хвилину, за день, токенів на запит та одночасних запитів) і не призначена для використання у виробничих сценаріях.

GitHub Models використовує Azure AI Content Safety. Ці фільтри не можна вимкнути в рамках досвіду GitHub Models. Якщо ви вирішите використовувати моделі через платний сервіс, будь ласка, налаштуйте фільтри вмісту відповідно до ваших вимог.

Цей сервіс працює відповідно до Умов попереднього релізу GitHub.

**Відмова від відповідальності**:  
Цей документ було перекладено за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується звертатися до професійного людського перекладу. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.