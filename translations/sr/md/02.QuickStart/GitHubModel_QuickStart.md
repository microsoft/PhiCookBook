## GitHub Models - Ограничена јавна бета

Добродошли у [GitHub Models](https://github.com/marketplace/models)! Све је спремно за вас да истражите AI моделе који се налазе на Azure AI.

![GitHubModel](../../../../translated_images/sr/GitHub_ModelCatalog.aa43c51c36454747.webp)

За више информација о моделима доступним на GitHub Models, погледајте [GitHub Model Marketplace](https://github.com/marketplace/models)

## Доступни модели

Сваки модел има посебан playground и пример кода

![Phi-3Model_Github](../../../../imgs/01/02/02/GitHub_ModelPlay.png)

### Phi-3 модели у GitHub Model каталогу

[Phi-3-Medium-128k-Instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-128k-instruct)

[Phi-3-medium-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-4k-instruct)

[Phi-3-mini-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-128k-instruct)

[Phi-3-mini-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-4k-instruct)

[Phi-3-small-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-128k-instruct)

[Phi-3-small-8k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-8k-instruct)

## Почетак рада

Постоје неки основни примери који су спремни за покретање. Можете их пронаћи у директоријуму samples. Ако желите да одмах пређете на свој омиљени језик, примере можете наћи у следећим језицима:

- Python
- JavaScript
- cURL

Постоји и посебно Codespaces окружење за покретање примера и модела.

![Getting Started](../../../../translated_images/sr/GitHub_ModelGetStarted.150220a802da6fb6.webp)

## Примери кода

Испод су примерци кода за неколико случајева употребе. За додатне информације о Azure AI Inference SDK, погледајте пуну документацију и примере.

## Подешавање

1. Креирајте personal access token  
Није потребно да додељујете никакве дозволе токену. Имајте на уму да ће токен бити послат Microsoft сервису.

Да бисте користили примерке кода испод, креирајте environment variable и подесите свој токен као кључ за client код.

Ако користите bash:  
```
export GITHUB_TOKEN="<your-github-token-goes-here>"
```  
Ако сте у powershell:  

```
$Env:GITHUB_TOKEN="<your-github-token-goes-here>"
```  

Ако користите Windows command prompt:  

```
set GITHUB_TOKEN=<your-github-token-goes-here>
```  

## Python пример

### Инсталирање зависности  
Инсталирајте Azure AI Inference SDK помоћу pip (Захтева: Python >=3.8):

```
pip install azure-ai-inference
```  
### Покрени основни пример кода

Овај пример показује основни позив chat completion API-ју. Користи GitHub AI model inference endpoint и ваш GitHub токен. Позив је синхрони.

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

### Покрени разговор са више корака

Овај пример показује разговор са више корака са chat completion API-јем. Када користите модел за chat апликацију, потребно је да управљате историјом тог разговора и шаљете најновије поруке моделу.

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

### Стримовање излаза

За боље корисничко искуство, желећете да стримујете одговор модела тако да први токен буде видљив раније и да избегнете дуго чекање на одговор.

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

### Инсталирање зависности

Инсталирајте Node.js.

Копирајте следеће линије текста и сачувајте их као датотеку package.json унутар вашег фолдера.

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

Напомена: @azure/core-sse је потребан само када стримујете одговоре chat completions.

Отворите терминал у овом фолдеру и покрените npm install.

За сваки од примера кода испод, копирајте садржај у датотеку sample.js и покрените са node sample.js.

### Покрени основни пример кода

Овај пример показује основни позив chat completion API-ју. Користи GitHub AI model inference endpoint и ваш GitHub токен. Позив је синхрони.

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

### Покрени разговор са више корака

Овај пример показује разговор са више корака са chat completion API-јем. Када користите модел за chat апликацију, потребно је да управљате историјом тог разговора и шаљете најновије поруке моделу.

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

### Стримовање излаза  
За боље корисничко искуство, желећете да стримујете одговор модела тако да први токен буде видљив раније и да избегнете дуго чекање на одговор.

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

### Покрени основни пример кода

Налепите следеће у shell:

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
### Покрени разговор са више корака

Позовите chat completion API и проследите историју разговора:

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
### Стримовање излаза

Ово је пример позива endpoint-а и стримовања одговора.

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

## Бесплатна употреба и ограничења за GitHub Models

![Model Catalog](../../../../translated_images/sr/GitHub_Model.ca6c125cb3117d0e.webp)

[Ограничења за playground и бесплатну API употребу](https://docs.github.com/en/github-models/prototyping-with-ai-models#rate-limits) су намењена да вам помогну да експериментишете са моделима и направите прототип своје AI апликације. За коришћење изван тих ограничења, и за скалирање ваше апликације, морате обезбедити ресурсе преко Azure налога и аутентификовати се преко њега уместо преко вашег GitHub personal access token-а. Не морате мењати ништа друго у свом коду. Користите овај линк да сазнате како да пређете границе бесплатног нивоа у Azure AI.

### Обавештења

Имајте на уму да када радите са моделом, експериментишете са AI-јем, па су могуће грешке у садржају.

Ова функција је подложна разним ограничењима (укључујући број захтева по минути, по дану, број токена по захтеву и истовремене захтеве) и није намењена за продукцијске случајеве.

GitHub Models користи Azure AI Content Safety. Ови филтери се не могу искључити као део GitHub Models искуства. Ако одлучите да користите моделе преко плаћене услуге, молимо вас да конфигуришете филтере садржаја у складу са вашим потребама.

Ова услуга је у оквиру GitHub Pre-release Terms.

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI сервиса за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да превод буде тачан, молимо вас да имате у виду да аутоматизовани преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.