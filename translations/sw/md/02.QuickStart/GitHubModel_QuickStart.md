<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5113634b77370af6790f9697d5d7de90",
  "translation_date": "2025-05-09T20:20:45+00:00",
  "source_file": "md/02.QuickStart/GitHubModel_QuickStart.md",
  "language_code": "sw"
}
-->
## GitHub Models - Beta ya Umma Iliyopunguzwa

Karibu kwenye [GitHub Models](https://github.com/marketplace/models)! Tuko tayari kabisa kukuwezesha kuchunguza Modeli za AI zilizo kwenye Azure AI.

![GitHubModel](../../../../translated_images/GitHub_ModelCatalog.4fc858ab26afe64c43f5e423ad0c5c733878bb536fdb027a5bcf1f80c41b0633.sw.png)

Kwa maelezo zaidi kuhusu Modeli zinazopatikana kwenye GitHub Models, tembelea [GitHub Model Marketplace](https://github.com/marketplace/models)

## Modeli Zinazopatikana

Kila modeli ina eneo la majaribio na mifano ya msimbo

![Phi-3Model_Github](../../../../imgs/01/02/02/GitHub_ModelPlay.png)

### Modeli za Phi-3 katika Katalogi ya Modeli ya GitHub

[Phi-3-Medium-128k-Instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-128k-instruct)

[Phi-3-medium-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-4k-instruct)

[Phi-3-mini-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-128k-instruct)

[Phi-3-mini-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-4k-instruct)

[Phi-3-small-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-128k-instruct)

[Phi-3-small-8k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-8k-instruct)

## Kuanzia

Kuna mifano michache rahisi tayari kwa ajili yako kuendesha. Unaweza kuipata katika saraka ya samples. Ikiwa unataka kuruka moja kwa moja kwenye lugha unayopenda, mifano ipo katika Lugha zifuatazo:

- Python
- JavaScript
- cURL

Pia kuna Mazingira maalum ya Codespaces kwa ajili ya kuendesha mifano na modeli.

![Getting Started](../../../../translated_images/GitHub_ModelGetStarted.b4b839a081583da39bc976c2f0d8ac4603d3b8c23194b16cc9e0a1014f5611d0.sw.png)

## Msimbo wa Mfano

Hapa chini kuna vipande vya msimbo kwa matumizi mbalimbali. Kwa maelezo zaidi kuhusu Azure AI Inference SDK, angalia nyaraka kamili na mifano.

## Usanidi

1. Tengeneza tokeni ya ufikiaji wa kibinafsi  
Huhitaji kumpa ruhusa yoyote tokeni hiyo. Kumbuka tokeni itatumwa kwa huduma ya Microsoft.

Ili kutumia vipande vya msimbo hapa chini, tengeneza variable ya mazingira kuweka tokeni yako kama ufunguo kwa msimbo wa mteja.

Ikiwa unatumia bash:  
```
export GITHUB_TOKEN="<your-github-token-goes-here>"
```  
Ikiwa uko powershell:  

```
$Env:GITHUB_TOKEN="<your-github-token-goes-here>"
```  

Ikiwa unatumia Windows command prompt:  

```
set GITHUB_TOKEN=<your-github-token-goes-here>
```  

## Mfano wa Python

### Sakinisha tegemezi  
Sakinisha Azure AI Inference SDK kwa kutumia pip (Inahitaji: Python >=3.8):  

```
pip install azure-ai-inference
```  
### Endesha mfano rahisi wa msimbo

Mfano huu unaonyesha mwito rahisi kwa API ya chat completion. Unatumia endpoint ya GitHub AI model inference na tokeni yako ya GitHub. Mwito ni wa moja kwa moja (synchronous).

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

### Endesha mazungumzo ya mizunguko mingi

Mfano huu unaonyesha mazungumzo ya mizunguko mingi kwa API ya chat completion. Unapotumia modeli kwa programu ya mazungumzo, utahitaji kusimamia historia ya mazungumzo na kutuma ujumbe wa hivi karibuni kwa modeli.

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

### Pitia matokeo kwa mtiririko

Kwa uzoefu bora wa mtumiaji, utataka kupitisha jibu la modeli kwa mtiririko ili tokeni ya kwanza ionekane mapema na kuepuka kusubiri majibu marefu.

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

### Sakinisha tegemezi

Sakinisha Node.js.

Nakili mistari ifuatayo na uiweke kama faili package.json ndani ya folda yako.

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

Kumbuka: @azure/core-sse inahitajika tu wakati unapopita majibu ya chat completions.

Fungua dirisha la terminal katika folda hii na endesha npm install.

Kwa kila kipande cha msimbo hapa chini, nakili yaliyomo katika faili sample.js na uendeshe kwa node sample.js.

### Endesha mfano rahisi wa msimbo

Mfano huu unaonyesha mwito rahisi kwa API ya chat completion. Unatumia endpoint ya GitHub AI model inference na tokeni yako ya GitHub. Mwito ni wa moja kwa moja (synchronous).

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

### Endesha mazungumzo ya mizunguko mingi

Mfano huu unaonyesha mazungumzo ya mizunguko mingi kwa API ya chat completion. Unapotumia modeli kwa programu ya mazungumzo, utahitaji kusimamia historia ya mazungumzo na kutuma ujumbe wa hivi karibuni kwa modeli.

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

### Pitia matokeo kwa mtiririko

Kwa uzoefu bora wa mtumiaji, utataka kupitisha jibu la modeli kwa mtiririko ili tokeni ya kwanza ionekane mapema na kuepuka kusubiri majibu marefu.

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

### Endesha mfano rahisi wa msimbo

Bandika yafuatayo kwenye shell:

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
### Endesha mazungumzo ya mizunguko mingi

Piga API ya chat completion na tuma historia ya mazungumzo:

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
### Pitia matokeo kwa mtiririko

Huu ni mfano wa kupiga mwito kwenye endpoint na kupitisha jibu kwa mtiririko.

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

## Matumizi ya BURE na Mipaka ya Kiwango kwa GitHub Models

![Model Catalog](../../../../translated_images/GitHub_Model.0c2abb992151c5407046e2b763af51505ff709f04c0950785e0300fdc8c55a0c.sw.png)

[Mipaka ya kiwango kwa matumizi ya playground na API ya bure](https://docs.github.com/en/github-models/prototyping-with-ai-models#rate-limits) yamekusudiwa kusaidia wewe kujaribu modeli na kutengeneza mfano wa programu yako ya AI. Kwa matumizi zaidi ya mipaka hiyo, na ili kupeleka programu yako kwa kiwango kikubwa, lazima utumie rasilimali kutoka kwa akaunti ya Azure, na uthibitishe kutoka huko badala ya tokeni yako ya ufikiaji wa kibinafsi ya GitHub. Huhitaji kubadilisha kitu kingine chochote kwenye msimbo wako. Tumia kiungo hiki kujifunza jinsi ya kuvuka mipaka ya kiwango cha bure katika Azure AI.

### Tahadhari

Kumbuka unapotumia modeli, una jaribu AI, hivyo makosa katika maudhui yanawezekana.

Huduma hii ina mipaka mbalimbali (ikiwa ni pamoja na maombi kwa dakika, maombi kwa siku, tokeni kwa ombi, na maombi yanayofanyika kwa wakati mmoja) na haijaundwa kwa matumizi ya uzalishaji.

GitHub Models hutumia Azure AI Content Safety. Vichujio hivi haviwezi kuzimwa kama sehemu ya uzoefu wa GitHub Models. Ukiacha kutumia modeli kupitia huduma ya kulipwa, tafadhali sanifu vichujio vya maudhui kulingana na mahitaji yako.

Huduma hii iko chini ya Masharti ya Awali ya GitHub.

**Kang’ang’a**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha kuaminika. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatubeba jukumu lolote kwa kutoelewana au tafsiri mbaya zitokanazo na matumizi ya tafsiri hii.