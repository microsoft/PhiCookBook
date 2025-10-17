<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5113634b77370af6790f9697d5d7de90",
  "translation_date": "2025-10-11T12:12:36+00:00",
  "source_file": "md/02.QuickStart/GitHubModel_QuickStart.md",
  "language_code": "et"
}
-->
## GitHubi mudelid - piiratud avalik beetaversioon

Tere tulemast [GitHubi mudelitesse](https://github.com/marketplace/models)! Oleme kõik valmis seadistanud, et saaksite uurida Azure AI-s hostitud AI-mudeleid.

![GitHubModel](../../../../imgs/01/02/02/GitHub_ModelCatalog.png)

Lisateabe saamiseks GitHubi mudelites saadaval olevate mudelite kohta vaadake [GitHubi mudelite turgu](https://github.com/marketplace/models).

## Saadaval olevad mudelid

Igal mudelil on oma mänguväljak ja näidiskood.

![Phi-3Model_Github](../../../../imgs/01/02/02/GitHub_ModelPlay.png)

### Phi-3 mudelid GitHubi mudelikataloogis

[Phi-3-Medium-128k-Instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-128k-instruct)

[Phi-3-medium-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-4k-instruct)

[Phi-3-mini-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-128k-instruct)

[Phi-3-mini-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-4k-instruct)

[Phi-3-small-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-128k-instruct)

[Phi-3-small-8k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-8k-instruct)

## Alustamine

Mõned põhinäited on valmis käivitamiseks. Leiate need näidiste kaustast. Kui soovite kohe alustada oma lemmikprogrammeermiskeelega, leiate näited järgmistest keeltest:

- Python
- JavaScript
- cURL

Samuti on olemas spetsiaalne Codespaces'i keskkond näidiste ja mudelite käitamiseks.

![Alustamine](../../../../imgs/01/02/02/GitHub_ModelGetStarted.png)

## Näidiskood

Allpool on näited koodilõikudest mõne kasutusjuhtumi jaoks. Lisateabe saamiseks Azure AI Inference SDK kohta vaadake täielikku dokumentatsiooni ja näidiseid.

## Seadistamine

1. Looge isiklik juurdepääsutoken  
Te ei pea tokenile mingeid õigusi andma. Pange tähele, et token saadetakse Microsofti teenusele.

Koodilõikude kasutamiseks looge keskkonnamuutuja, et määrata oma token kliendikoodi võtmena.

Kui kasutate bash'i:  
```
export GITHUB_TOKEN="<your-github-token-goes-here>"
```
  
Kui kasutate PowerShelli:  
```
$Env:GITHUB_TOKEN="<your-github-token-goes-here>"
```
  
Kui kasutate Windowsi käsuviiba:  
```
set GITHUB_TOKEN=<your-github-token-goes-here>
```
  

## Python näide

### Paigaldage sõltuvused  
Paigaldage Azure AI Inference SDK pip-i abil (nõutav: Python >=3.8):  
```
pip install azure-ai-inference
```
  

### Käivitage lihtne näide  
See näide demonstreerib lihtsat päringut vestluse lõpetamise API-le. Kasutatakse GitHubi AI mudeli järelduspunkti ja teie GitHubi tokenit. Päring on sünkroonne.  
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
  

### Käivitage mitme pöördega vestlus  
See näide demonstreerib mitme pöördega vestlust vestluse lõpetamise API-ga. Kui kasutate mudelit vestlusrakenduses, peate haldama vestluse ajalugu ja saatma mudelile viimased sõnumid.  
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
  

### Väljundi voogesitus  
Parema kasutajakogemuse saavutamiseks soovite mudeli vastuse voogesitada, et esimene token ilmuks varakult ja vältiksite pikkade vastuste ootamist.  
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

### Paigaldage sõltuvused  
Paigaldage Node.js.  

Kopeerige järgmised tekstiread ja salvestage need failina package.json oma kausta.  
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
  
Märkus: @azure/core-sse on vajalik ainult siis, kui voogesitate vestluse lõpetamise vastust.  

Avage terminaliaknas see kaust ja käivitage npm install.  

Iga allpool oleva koodilõigu jaoks kopeerige sisu faili sample.js ja käivitage see käsuga node sample.js.  

### Käivitage lihtne näide  
See näide demonstreerib lihtsat päringut vestluse lõpetamise API-le. Kasutatakse GitHubi AI mudeli järelduspunkti ja teie GitHubi tokenit. Päring on sünkroonne.  
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
  

### Käivitage mitme pöördega vestlus  
See näide demonstreerib mitme pöördega vestlust vestluse lõpetamise API-ga. Kui kasutate mudelit vestlusrakenduses, peate haldama vestluse ajalugu ja saatma mudelile viimased sõnumid.  
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
  

### Väljundi voogesitus  
Parema kasutajakogemuse saavutamiseks soovite mudeli vastuse voogesitada, et esimene token ilmuks varakult ja vältiksite pikkade vastuste ootamist.  
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

### Käivitage lihtne näide  
Kopeerige järgmine kood shelli:  
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
  

### Käivitage mitme pöördega vestlus  
Kutsuge vestluse lõpetamise API ja edastage vestluse ajalugu:  
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
  

### Väljundi voogesitus  
See on näide järelduspunkti kutsumisest ja vastuse voogesitamisest.  
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
  

## TASUTA kasutamine ja GitHubi mudelite kiiruse piirangud

![Mudelite kataloog](../../../../imgs/01/02/02/GitHub_Model.png)

[Kiiruse piirangud mänguväljakule ja tasuta API kasutamisele](https://docs.github.com/en/github-models/prototyping-with-ai-models#rate-limits) on mõeldud selleks, et aidata teil mudeleid katsetada ja oma AI-rakendust prototüüpida. Kui soovite kasutada mudeleid piirangutest kaugemale ja viia oma rakendus suuremahulisse kasutusse, peate Azure'i kontolt ressursse hankima ja sealt autentima, mitte kasutama oma GitHubi isiklikku juurdepääsutokenit. Te ei pea oma koodis midagi muud muutma. Kasutage seda linki, et teada saada, kuidas ületada tasuta taseme piiranguid Azure AI-s.

### Avalikustused

Pidage meeles, et mudeliga suheldes katsetate AI-d, seega võivad esineda sisuvigad.

Funktsioonil on mitmesugused piirangud (sealhulgas päringud minutis, päringud päevas, tokenid päringu kohta ja samaaegsed päringud) ning see ei ole mõeldud tootmiskasutuseks.

GitHubi mudelid kasutavad Azure AI sisuturvalisust. Neid filtreid ei saa GitHubi mudelite kasutuskogemuse osana välja lülitada. Kui otsustate mudeleid kasutada tasulise teenuse kaudu, konfigureerige oma sisufiltrid vastavalt oma nõuetele.

See teenus kuulub GitHubi eellansseerimise tingimuste alla.

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.