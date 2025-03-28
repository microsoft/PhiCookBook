<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5113634b77370af6790f9697d5d7de90",
  "translation_date": "2025-03-27T13:27:28+00:00",
  "source_file": "md\\02.QuickStart\\GitHubModel_QuickStart.md",
  "language_code": "ru"
}
-->
## GitHub Models - Ограниченная публичная бета-версия

Добро пожаловать в [GitHub Models](https://github.com/marketplace/models)! Мы все настроили, чтобы вы могли исследовать AI-модели, размещенные на Azure AI.

![GitHubModel](../../../../translated_images/GitHub_ModelCatalog.4fc858ab26afe64c43f5e423ad0c5c733878bb536fdb027a5bcf1f80c41b0633.ru.png)

Для получения дополнительной информации о моделях, доступных в GitHub Models, посетите [GitHub Model Marketplace](https://github.com/marketplace/models).

## Доступные модели

Каждая модель имеет собственную песочницу и пример кода.

![Phi-3Model_Github](../../../../imgs/01/02/02/GitHub_ModelPlay.png)

### Модели Phi-3 в каталоге GitHub Models

[Phi-3-Medium-128k-Instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-128k-instruct)

[Phi-3-medium-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-4k-instruct)

[Phi-3-mini-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-128k-instruct)

[Phi-3-mini-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-4k-instruct)

[Phi-3-small-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-128k-instruct)

[Phi-3-small-8k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-8k-instruct)

## Начало работы

У нас есть несколько базовых примеров, которые готовы к запуску. Вы можете найти их в каталоге с примерами. Если вы хотите сразу перейти к своему любимому языку программирования, примеры доступны на следующих языках:

- Python
- JavaScript
- cURL

Также доступна выделенная среда Codespaces для запуска примеров и моделей.

![Getting Started](../../../../translated_images/GitHub_ModelGetStarted.b4b839a081583da39bc976c2f0d8ac4603d3b8c23194b16cc9e0a1014f5611d0.ru.png)

## Пример кода

Ниже приведены фрагменты кода для нескольких вариантов использования. Для получения дополнительной информации о Azure AI Inference SDK ознакомьтесь с полной документацией и примерами.

## Настройка

1. Создайте персональный токен доступа  
Токен не требует предоставления каких-либо разрешений. Обратите внимание, что токен будет отправлен в службу Microsoft.

Чтобы использовать приведенные ниже фрагменты кода, создайте переменную окружения, чтобы установить токен в качестве ключа для клиентского кода.

Если вы используете bash:  
```
export GITHUB_TOKEN="<your-github-token-goes-here>"
```  
Если вы используете PowerShell:  

```
$Env:GITHUB_TOKEN="<your-github-token-goes-here>"
```  

Если вы используете командную строку Windows:  

```
set GITHUB_TOKEN=<your-github-token-goes-here>
```  

## Пример для Python

### Установите зависимости  
Установите Azure AI Inference SDK с помощью pip (требуется: Python >=3.8):  

```
pip install azure-ai-inference
```  

### Запустите базовый пример кода  

Этот пример демонстрирует базовый вызов API для завершения чата. Используется конечная точка GitHub AI model inference и ваш токен GitHub. Вызов является синхронным.  

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

### Запустите многотуровой диалог  

Этот пример демонстрирует многотуровой диалог с API завершения чата. При использовании модели для чата вам нужно будет управлять историей беседы и отправлять последние сообщения модели.  

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

### Стриминг вывода  

Для улучшения пользовательского опыта рекомендуется стримить ответ модели, чтобы первые токены отображались сразу, избегая длительного ожидания.  

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

### Установите зависимости  

Установите Node.js.  

Скопируйте следующие строки текста и сохраните их в файл package.json в своей папке.  

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

Примечание: @azure/core-sse требуется только для стриминга ответа завершения чата.  

Откройте окно терминала в этой папке и выполните команду npm install.  

Для каждого из приведенных ниже фрагментов кода скопируйте содержимое в файл sample.js и выполните с помощью node sample.js.  

### Запустите базовый пример кода  

Этот пример демонстрирует базовый вызов API для завершения чата. Используется конечная точка GitHub AI model inference и ваш токен GitHub. Вызов является синхронным.  

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

### Запустите многотуровой диалог  

Этот пример демонстрирует многотуровой диалог с API завершения чата. При использовании модели для чата вам нужно будет управлять историей беседы и отправлять последние сообщения модели.  

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

### Стриминг вывода  
Для улучшения пользовательского опыта рекомендуется стримить ответ модели, чтобы первые токены отображались сразу, избегая длительного ожидания.  

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

### Запустите базовый пример кода  

Вставьте следующее в оболочку:  

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

### Запустите многотуровой диалог  

Вызовите API завершения чата и передайте историю чата:  

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

### Стриминг вывода  

Пример вызова конечной точки и стриминга ответа.  

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

## Бесплатное использование и ограничения для GitHub Models  

![Model Catalog](../../../../translated_images/GitHub_Model.0c2abb992151c5407046e2b763af51505ff709f04c0950785e0300fdc8c55a0c.ru.png)  

[Ограничения для песочницы и бесплатного использования API](https://docs.github.com/en/github-models/prototyping-with-ai-models#rate-limits) предназначены для того, чтобы вы могли экспериментировать с моделями и разрабатывать прототипы вашего AI-приложения. Для использования за пределами этих ограничений и масштабирования приложения необходимо выделить ресурсы из учетной записи Azure и пройти аутентификацию через нее вместо использования вашего персонального токена GitHub. Вам не нужно вносить другие изменения в код. Используйте эту ссылку, чтобы узнать, как выйти за пределы бесплатного уровня в Azure AI.

### Раскрытие информации  

Помните, что при взаимодействии с моделью вы экспериментируете с AI, поэтому возможны ошибки в содержании.  

Функция подчиняется различным ограничениям (включая запросы в минуту, запросы в день, токены на запрос и одновременные запросы) и не предназначена для производственного использования.  

GitHub Models использует Azure AI Content Safety. Эти фильтры нельзя отключить в рамках работы с GitHub Models. Если вы решите использовать модели через платный сервис, настройте фильтры контента в соответствии с вашими требованиями.  

Эта услуга предоставляется в рамках условий предварительного выпуска GitHub.  

**Отказ от ответственности**:  
Этот документ был переведен с использованием сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия обеспечить точность, имейте в виду, что автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неправильные интерпретации, возникшие в результате использования этого перевода.