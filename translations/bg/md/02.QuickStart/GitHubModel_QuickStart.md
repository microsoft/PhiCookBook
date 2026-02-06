## GitHub Models - Ограничена публична бета

Добре дошли в [GitHub Models](https://github.com/marketplace/models)! Всичко е готово и ви очаква да разгледате AI модели, хоствани в Azure AI.

![GitHubModel](../../../../translated_images/bg/GitHub_ModelCatalog.aa43c51c36454747.webp)

За повече информация относно моделите, налични в GitHub Models, разгледайте [GitHub Model Marketplace](https://github.com/marketplace/models)

## Налични модели

Всеки модел има собствена среда за експериментиране и примерен код

![Phi-3Model_Github](../../../../imgs/01/02/02/GitHub_ModelPlay.png)

### Phi-3 модели в GitHub Model Catalog

[Phi-3-Medium-128k-Instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-128k-instruct)

[Phi-3-medium-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-4k-instruct)

[Phi-3-mini-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-128k-instruct)

[Phi-3-mini-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-4k-instruct)

[Phi-3-small-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-128k-instruct)

[Phi-3-small-8k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-8k-instruct)

## Започване

Има няколко основни примера, готови за изпълнение. Можете да ги намерите в директорията samples. Ако искате да преминете директно към предпочитания от вас език, примерите са налични на следните езици:

- Python
- JavaScript
- cURL

Има и специална среда Codespaces за изпълнение на примерите и моделите.

![Getting Started](../../../../translated_images/bg/GitHub_ModelGetStarted.150220a802da6fb6.webp)

## Примерен код

По-долу са показани примерни кодови откъси за няколко случая на употреба. За допълнителна информация относно Azure AI Inference SDK, вижте пълната документация и примери.

## Настройка

1. Създайте личен достъп токен  
Не е необходимо да задавате никакви разрешения на токена. Обърнете внимание, че токенът ще бъде изпратен до услуга на Microsoft.

За да използвате кодовите откъси по-долу, създайте променлива на средата, в която задайте вашия токен като ключ за клиентския код.

Ако използвате bash:  
```
export GITHUB_TOKEN="<your-github-token-goes-here>"
```  
Ако сте в powershell:  

```
$Env:GITHUB_TOKEN="<your-github-token-goes-here>"
```  

Ако използвате Windows команден ред:  

```
set GITHUB_TOKEN=<your-github-token-goes-here>
```  

## Python пример

### Инсталиране на зависимости  
Инсталирайте Azure AI Inference SDK с pip (Изисква: Python >=3.8):

```
pip install azure-ai-inference
```  
### Изпълнение на основен примерен код

Този пример показва основно извикване на chat completion API. Използва се GitHub AI модел inference endpoint и вашия GitHub токен. Извикването е синхронно.

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

### Изпълнение на многократен разговор

Този пример показва многократен разговор с chat completion API. При използване на модела за чат приложение, трябва да управлявате историята на разговора и да изпращате последните съобщения към модела.

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

### Поточно извеждане

За по-добро потребителско изживяване, ще искате да стриймвате отговора на модела, така че първият токен да се появи рано и да избегнете чакане при дълги отговори.

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

### Инсталиране на зависимости

Инсталирайте Node.js.

Копирайте следните редове и ги запазете като файл package.json в папката си.

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

Забележка: @azure/core-sse е необходим само при стриймване на отговорите от chat completions.

Отворете терминал в тази папка и изпълнете npm install.

За всеки от кодовите откъси по-долу, копирайте съдържанието във файл sample.js и го стартирайте с node sample.js.

### Изпълнение на основен примерен код

Този пример показва основно извикване на chat completion API. Използва се GitHub AI модел inference endpoint и вашия GitHub токен. Извикването е синхронно.

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

### Изпълнение на многократен разговор

Този пример показва многократен разговор с chat completion API. При използване на модела за чат приложение, трябва да управлявате историята на разговора и да изпращате последните съобщения към модела.

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

### Поточно извеждане  
За по-добро потребителско изживяване, ще искате да стриймвате отговора на модела, така че първият токен да се появи рано и да избегнете чакане при дълги отговори.

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

### Изпълнение на основен примерен код

Поставете следното в shell:

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
### Изпълнение на многократен разговор

Извикайте chat completion API и предайте историята на чата:

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
### Поточно извеждане

Това е пример за извикване на endpoint и стриймване на отговора.

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

## Безплатна употреба и ограничения за GitHub Models

![Model Catalog](../../../../translated_images/bg/GitHub_Model.ca6c125cb3117d0e.webp)

[Ограниченията за playground и безплатната API употреба](https://docs.github.com/en/github-models/prototyping-with-ai-models#rate-limits) са предназначени да ви помогнат да експериментирате с модели и да прототипирате вашето AI приложение. За използване извън тези ограничения и за мащабиране на приложението, трябва да осигурите ресурси от Azure акаунт и да се удостоверите оттам, вместо с вашия GitHub личен достъп токен. Не е необходимо да променяте нищо друго в кода си. Използвайте тази връзка, за да разберете как да преминете отвъд безплатните лимити в Azure AI.

### Разкрития

Имайте предвид, че при взаимодействие с модел експериментирате с AI, затова са възможни грешки в съдържанието.

Функцията е подложена на различни ограничения (включително заявки в минута, заявки на ден, токени на заявка и едновременни заявки) и не е предназначена за производствени случаи.

GitHub Models използва Azure AI Content Safety. Тези филтри не могат да бъдат изключвани като част от GitHub Models. Ако решите да използвате модели чрез платена услуга, моля, конфигурирайте филтрите за съдържание според вашите изисквания.

Тази услуга е под условията за предварително пускане на GitHub.

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI преводаческа услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.