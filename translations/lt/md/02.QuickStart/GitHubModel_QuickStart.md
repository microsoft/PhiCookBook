## GitHub modeliai - Ribotas viešas beta testavimas

Sveiki atvykę į [GitHub modelius](https://github.com/marketplace/models)! Viskas paruošta, kad galėtumėte tyrinėti AI modelius, talpinamus Azure AI platformoje.

![GitHubModel](../../../../imgs/01/02/02/GitHub_ModelCatalog.png)

Daugiau informacijos apie modelius, prieinamus GitHub modeliuose, rasite [GitHub Model Marketplace](https://github.com/marketplace/models).

## Prieinami modeliai

Kiekvienas modelis turi dedikuotą testavimo aplinką ir pavyzdinį kodą.

![Phi-3Model_Github](../../../../imgs/01/02/02/GitHub_ModelPlay.png)

### Phi-3 modeliai GitHub modelių kataloge

[Phi-3-Medium-128k-Instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-128k-instruct)

[Phi-3-medium-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-4k-instruct)

[Phi-3-mini-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-128k-instruct)

[Phi-3-mini-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-4k-instruct)

[Phi-3-small-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-128k-instruct)

[Phi-3-small-8k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-8k-instruct)

## Pradžia

Yra keletas pagrindinių pavyzdžių, paruoštų paleidimui. Juos galite rasti pavyzdžių kataloge. Jei norite iškart pereiti prie savo mėgstamos programavimo kalbos, pavyzdžius rasite šiose kalbose:

- Python
- JavaScript
- cURL

Taip pat yra dedikuota Codespaces aplinka, skirta pavyzdžiams ir modeliams paleisti.

![Pradžia](../../../../imgs/01/02/02/GitHub_ModelGetStarted.png)

## Pavyzdinis kodas

Žemiau pateikiami pavyzdiniai kodai keliems naudojimo atvejams. Daugiau informacijos apie Azure AI Inference SDK rasite pilnoje dokumentacijoje ir pavyzdžiuose.

## Nustatymai

1. Sukurkite asmeninį prieigos raktą  
Jums nereikia suteikti jokių leidimų raktui. Atkreipkite dėmesį, kad raktas bus siunčiamas į Microsoft paslaugą.

Norėdami naudoti žemiau pateiktus kodo fragmentus, sukurkite aplinkos kintamąjį, kad nustatytumėte savo raktą kaip klientinio kodo raktą.

Jei naudojate bash:  
```
export GITHUB_TOKEN="<your-github-token-goes-here>"
```  
Jei naudojate powershell:  
```
$Env:GITHUB_TOKEN="<your-github-token-goes-here>"
```  

Jei naudojate Windows komandinę eilutę:  
```
set GITHUB_TOKEN=<your-github-token-goes-here>
```  

## Python pavyzdys

### Įdiekite priklausomybes  
Įdiekite Azure AI Inference SDK naudodami pip (Reikalavimai: Python >=3.8):  
```
pip install azure-ai-inference
```  

### Paleiskite pagrindinį kodo pavyzdį  

Šis pavyzdys demonstruoja pagrindinį API kvietimą pokalbių užbaigimui. Jis naudoja GitHub AI modelio inferencijos galinį tašką ir jūsų GitHub raktą. Kvietimas yra sinchroninis.  
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

### Paleiskite daugiapakopį pokalbį  

Šis pavyzdys demonstruoja daugiapakopį pokalbį su pokalbių užbaigimo API. Naudojant modelį pokalbių programoje, jums reikės valdyti pokalbio istoriją ir siųsti naujausius pranešimus modeliui.  
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

### Transliuokite išvestį  

Norėdami geresnės vartotojo patirties, norėsite transliuoti modelio atsakymą, kad pirmasis žetonas pasirodytų anksti ir išvengtumėte ilgų atsakymų laukimo.  
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

### Įdiekite priklausomybes  

Įdiekite Node.js.  

Nukopijuokite šias teksto eilutes ir išsaugokite jas kaip failą package.json savo aplanke.  
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

Pastaba: @azure/core-sse reikalingas tik tada, kai transliuojate pokalbių užbaigimo atsakymą.  

Atidarykite terminalo langą šiame aplanke ir paleiskite npm install.  

Kiekvienam žemiau pateiktam kodo fragmentui nukopijuokite turinį į failą sample.js ir paleiskite naudodami node sample.js.  

### Paleiskite pagrindinį kodo pavyzdį  

Šis pavyzdys demonstruoja pagrindinį API kvietimą pokalbių užbaigimui. Jis naudoja GitHub AI modelio inferencijos galinį tašką ir jūsų GitHub raktą. Kvietimas yra sinchroninis.  
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

### Paleiskite daugiapakopį pokalbį  

Šis pavyzdys demonstruoja daugiapakopį pokalbį su pokalbių užbaigimo API. Naudojant modelį pokalbių programoje, jums reikės valdyti pokalbio istoriją ir siųsti naujausius pranešimus modeliui.  
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

### Transliuokite išvestį  
Norėdami geresnės vartotojo patirties, norėsite transliuoti modelio atsakymą, kad pirmasis žetonas pasirodytų anksti ir išvengtumėte ilgų atsakymų laukimo.  
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

### Paleiskite pagrindinį kodo pavyzdį  

Įklijuokite šį kodą į shell:  
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

### Paleiskite daugiapakopį pokalbį  

Kreipkitės į pokalbių užbaigimo API ir perduokite pokalbio istoriją:  
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

### Transliuokite išvestį  

Tai yra pavyzdys, kaip kreiptis į galinį tašką ir transliuoti atsakymą.  
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

## NEMOKAMAS naudojimas ir GitHub modelių apribojimai

![Modelių katalogas](../../../../imgs/01/02/02/GitHub_Model.png)

[Naudojimo apribojimai testavimo aplinkoje ir nemokamo API naudojimo](https://docs.github.com/en/github-models/prototyping-with-ai-models#rate-limits) yra skirti padėti jums eksperimentuoti su modeliais ir kurti AI programos prototipą. Norėdami naudotis paslauga už šių apribojimų ribų ir padidinti savo programos mastą, turite užsisakyti resursus iš Azure paskyros ir autentifikuotis iš ten, o ne naudodami GitHub asmeninį prieigos raktą. Jums nereikia keisti nieko kito savo kode. Naudokite šią nuorodą, kad sužinotumėte, kaip viršyti nemokamo lygio ribas Azure AI.

### Atskleidimai  

Atminkite, kad bendraudami su modeliu eksperimentuojate su AI, todėl galimi turinio klaidos.  

Funkcija yra ribojama įvairiais apribojimais (įskaitant užklausas per minutę, užklausas per dieną, žetonus per užklausą ir lygiagrečias užklausas) ir nėra skirta gamybos naudojimo atvejams.  

GitHub modeliai naudoja Azure AI turinio saugumo filtrus. Šių filtrų negalima išjungti kaip GitHub modelių patirties dalies. Jei nuspręsite naudoti modelius per mokamą paslaugą, konfigūruokite savo turinio filtrus pagal savo poreikius.  

Ši paslauga yra teikiama pagal GitHub išankstinio išleidimo sąlygas.  

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.