<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5113634b77370af6790f9697d5d7de90",
  "translation_date": "2025-07-17T05:40:40+00:00",
  "source_file": "md/02.QuickStart/GitHubModel_QuickStart.md",
  "language_code": "hu"
}
-->
## GitHub Modellek – Korlátozott Nyilvános Béta

Üdvözlünk a [GitHub Modellek](https://github.com/marketplace/models) oldalán! Minden készen áll, hogy felfedezd az Azure AI-n futó AI modelleket.

![GitHubModel](../../../../translated_images/hu/GitHub_ModelCatalog.aa43c51c36454747.png)

További információkért a GitHub Modelleken elérhető modellekről, nézd meg a [GitHub Model Marketplace](https://github.com/marketplace/models) oldalt.

## Elérhető Modellek

Minden modellhez külön játszótér és példa kód tartozik.

![Phi-3Model_Github](../../../../imgs/01/02/02/GitHub_ModelPlay.png)

### Phi-3 Modellek a GitHub Model Katalógusban

[Phi-3-Medium-128k-Instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-128k-instruct)

[Phi-3-medium-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-4k-instruct)

[Phi-3-mini-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-128k-instruct)

[Phi-3-mini-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-4k-instruct)

[Phi-3-small-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-128k-instruct)

[Phi-3-small-8k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-8k-instruct)

## Első lépések

Néhány alap példa már készen áll a futtatásra. Ezeket a samples könyvtárban találod. Ha egyből a kedvenc nyelveden szeretnél dolgozni, az alábbi nyelveken érheted el a példákat:

- Python
- JavaScript
- cURL

Van egy dedikált Codespaces környezet is a példák és modellek futtatásához.

![Első lépések](../../../../translated_images/hu/GitHub_ModelGetStarted.150220a802da6fb6.png)

## Példa kód

Az alábbiakban néhány példa kódrészletet találsz különböző felhasználási esetekhez. További információkért az Azure AI Inference SDK-ról, nézd meg a teljes dokumentációt és a példákat.

## Beállítás

1. Hozz létre egy személyes hozzáférési tokent  
Nem szükséges engedélyeket adni a tokennek. Fontos, hogy a token egy Microsoft szolgáltatáshoz kerül elküldésre.

A lentebb található kódrészletek használatához hozz létre egy környezeti változót, amelyben a tokenedet a kliens kód kulcsaként állítod be.

Ha bash-t használsz:  
```
export GITHUB_TOKEN="<your-github-token-goes-here>"
```  
Ha PowerShell-ben vagy:  

```
$Env:GITHUB_TOKEN="<your-github-token-goes-here>"
```  

Ha Windows parancssorban vagy:  

```
set GITHUB_TOKEN=<your-github-token-goes-here>
```  

## Python példa

### Függőségek telepítése  
Telepítsd az Azure AI Inference SDK-t pip-pel (Szükséges: Python >=3.8):

```
pip install azure-ai-inference
```  
### Egy alap példa futtatása

Ez a példa egy egyszerű hívást mutat be a chat completion API-hoz. A GitHub AI modell inferencia végpontját és a GitHub tokenedet használja. A hívás szinkron.

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

### Többfordulós beszélgetés futtatása

Ez a példa egy többfordulós beszélgetést mutat be a chat completion API-val. Chat alkalmazás esetén neked kell kezelni a beszélgetés előzményeit, és a legfrissebb üzeneteket elküldeni a modellnek.

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

### Kimenet streamelése

Jobb felhasználói élmény érdekében érdemes streamelni a modell válaszát, hogy az első tokenek hamar megjelenjenek, és ne kelljen hosszú válaszokra várni.

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

### Függőségek telepítése

Telepítsd a Node.js-t.

Másold be az alábbi sorokat egy package.json nevű fájlba a mappádban.

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

Megjegyzés: az @azure/core-sse csak akkor szükséges, ha streamelni szeretnéd a chat completion válaszokat.

Nyiss egy terminált ebben a mappában, és futtasd az npm install parancsot.

A lentebb található kódrészleteket másold be egy sample.js nevű fájlba, majd futtasd a node sample.js parancsot.

### Egy alap példa futtatása

Ez a példa egy egyszerű hívást mutat be a chat completion API-hoz. A GitHub AI modell inferencia végpontját és a GitHub tokenedet használja. A hívás szinkron.

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

### Többfordulós beszélgetés futtatása

Ez a példa egy többfordulós beszélgetést mutat be a chat completion API-val. Chat alkalmazás esetén neked kell kezelni a beszélgetés előzményeit, és a legfrissebb üzeneteket elküldeni a modellnek.

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

### Kimenet streamelése

Jobb felhasználói élmény érdekében érdemes streamelni a modell válaszát, hogy az első tokenek hamar megjelenjenek, és ne kelljen hosszú válaszokra várni.

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

### Egy alap példa futtatása

Illeszd be a következőt egy shellbe:

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

### Többfordulós beszélgetés futtatása

Hívd meg a chat completion API-t, és add át a beszélgetés előzményeit:

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

### Kimenet streamelése

Ez egy példa az endpoint hívására és a válasz streamelésére.

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

## INGYENES használat és korlátok a GitHub Modellekhez

![Model Katalógus](../../../../translated_images/hu/GitHub_Model.ca6c125cb3117d0e.png)

A [játszótér és az ingyenes API használat](https://docs.github.com/en/github-models/prototyping-with-ai-models#rate-limits) korlátai arra szolgálnak, hogy kísérletezhess a modellekkel és prototípust készíthess az AI alkalmazásodhoz. Ezeken a korlátokon túl, és ha skálázni szeretnéd az alkalmazásodat, Azure fiókból kell erőforrásokat biztosítanod, és onnan hitelesítened a GitHub személyes hozzáférési token helyett. A kódodban egyéb változtatásra nincs szükség. Használd ezt a linket, hogy megtudd, hogyan léphetsz túl az ingyenes szint korlátain az Azure AI-ban.

### Figyelmeztetések

Ne feledd, hogy amikor egy modellel dolgozol, AI-val kísérletezel, így előfordulhatnak tartalmi hibák.

A funkció különböző korlátok alá esik (például percenkénti, napi kérések száma, tokenek száma kérésenként, párhuzamos kérések), és nem alkalmas éles használatra.

A GitHub Modellek az Azure AI Content Safety-t használják. Ezek a szűrők nem kapcsolhatók ki a GitHub Modellek használata során. Ha fizetős szolgáltatáson keresztül használod a modelleket, kérjük, állítsd be a tartalomszűrőket az igényeidnek megfelelően.

Ez a szolgáltatás a GitHub Előzetes kiadási feltételei alatt áll.

**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén szakmai, emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.