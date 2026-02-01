## GitHub Models - Rajoitettu julkinen beta

Tervetuloa [GitHub Models](https://github.com/marketplace/models) -palveluun! Olemme valmiina, jotta voit tutustua Azure AI:lla isännöityihin tekoälymalleihin.

![GitHubModel](../../../../translated_images/fi/GitHub_ModelCatalog.aa43c51c36454747.webp)

Lisätietoja GitHub Models -palvelussa saatavilla olevista malleista löydät osoitteesta [GitHub Model Marketplace](https://github.com/marketplace/models)

## Saatavilla olevat mallit

Jokaisella mallilla on oma leikkikenttä ja esimerkkikoodi

![Phi-3Model_Github](../../../../imgs/01/02/02/GitHub_ModelPlay.png)

### Phi-3-mallit GitHub Model Catalogissa

[Phi-3-Medium-128k-Instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-128k-instruct)

[Phi-3-medium-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-4k-instruct)

[Phi-3-mini-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-128k-instruct)

[Phi-3-mini-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-4k-instruct)

[Phi-3-small-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-128k-instruct)

[Phi-3-small-8k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-8k-instruct)

## Aloittaminen

Saatavilla on muutama perusesimerkki, jotka voit ajaa heti. Löydät ne samples-kansiosta. Jos haluat hypätä suoraan suosikkikieleesi, esimerkit löytyvät seuraavilta kieliltä:

- Python
- JavaScript
- cURL

Saatavilla on myös oma Codespaces-ympäristö, jossa voit ajaa esimerkkejä ja malleja.

![Getting Started](../../../../translated_images/fi/GitHub_ModelGetStarted.150220a802da6fb6.webp)

## Esimerkkikoodi

Alla on esimerkkikoodipätkiä muutamiin käyttötapauksiin. Lisätietoja Azure AI Inference SDK:sta löydät täydellisestä dokumentaatiosta ja esimerkeistä.

## Asetukset

1. Luo henkilökohtainen käyttöoikeustunnus  
Sinun ei tarvitse antaa tunnukselle mitään oikeuksia. Huomaa, että tunnus lähetetään Microsoftin palveluun.

Käyttääksesi alla olevia koodipätkiä, luo ympäristömuuttuja, johon asetat tunnuksesi avaimena client-koodille.

Jos käytät bashia:  
```
export GITHUB_TOKEN="<your-github-token-goes-here>"
```  
Jos käytät powershelliä:  

```
$Env:GITHUB_TOKEN="<your-github-token-goes-here>"
```  

Jos käytät Windowsin komentokehotetta:  

```
set GITHUB_TOKEN=<your-github-token-goes-here>
```  

## Python-esimerkki

### Asenna riippuvuudet  
Asenna Azure AI Inference SDK pipillä (vaatii: Python >=3.8):

```
pip install azure-ai-inference
```  
### Aja perusesimerkki

Tämä esimerkki näyttää peruskutsun chat completion -rajapintaan. Se hyödyntää GitHub AI -mallin inference-päätepistettä ja GitHub-tunnustasi. Kutsu on synkroninen.

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

### Aja monivaiheinen keskustelu

Tämä esimerkki näyttää monivaiheisen keskustelun chat completion -rajapinnan kanssa. Kun käytät mallia chat-sovelluksessa, sinun täytyy hallita keskustelun historiaa ja lähettää mallille viimeisimmät viestit.

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

### Suoratoista tulos

Parempaa käyttökokemusta varten haluat suoratoistaa mallin vastauksen, jotta ensimmäinen token näkyy nopeasti eikä tarvitse odottaa pitkiä vastauksia.

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

### Asenna riippuvuudet

Asenna Node.js.

Kopioi seuraavat rivit tekstitiedostoon nimeltä package.json kansiosi sisälle.

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

Huom: @azure/core-sse tarvitaan vain, jos suoratoistat chat completion -vastauksia.

Avaa terminaali tässä kansiossa ja aja komento npm install.

Jokaisen alla olevan koodipätkän osalta kopioi sisältö tiedostoon sample.js ja aja komento node sample.js.

### Aja perusesimerkki

Tämä esimerkki näyttää peruskutsun chat completion -rajapintaan. Se hyödyntää GitHub AI -mallin inference-päätepistettä ja GitHub-tunnustasi. Kutsu on synkroninen.

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

### Aja monivaiheinen keskustelu

Tämä esimerkki näyttää monivaiheisen keskustelun chat completion -rajapinnan kanssa. Kun käytät mallia chat-sovelluksessa, sinun täytyy hallita keskustelun historiaa ja lähettää mallille viimeisimmät viestit.

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

### Suoratoista tulos

Parempaa käyttökokemusta varten haluat suoratoistaa mallin vastauksen, jotta ensimmäinen token näkyy nopeasti eikä tarvitse odottaa pitkiä vastauksia.

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

### Aja perusesimerkki

Liitä seuraava shelliin:

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
### Aja monivaiheinen keskustelu

Kutsu chat completion -rajapintaa ja lähetä keskusteluhistoria:

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
### Suoratoista tulos

Tässä esimerkki päätepisteen kutsusta ja vastauksen suoratoistosta.

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

## ILMAINEN käyttö ja rajoitukset GitHub Models -palvelussa

![Model Catalog](../../../../translated_images/fi/GitHub_Model.ca6c125cb3117d0e.webp)

[Leikkikentän ja ilmaisen API-käytön rajoitukset](https://docs.github.com/en/github-models/prototyping-with-ai-models#rate-limits) on tarkoitettu auttamaan sinua kokeilemaan malleja ja prototyyppien tekoon AI-sovelluksessasi. Näiden rajojen ylittävässä käytössä ja sovelluksen skaalaamisessa sinun tulee varata resursseja Azure-tililtä ja autentikoitua sieltä henkilökohtaisen GitHub-käyttöoikeustunnuksen sijaan. Koodissasi ei tarvitse tehdä muita muutoksia. Käytä tätä linkkiä oppiaksesi, miten voit ylittää ilmaiskäytön rajat Azure AI:ssa.

### Ilmoitukset

Muista, että mallin kanssa toimiessasi kokeilet tekoälyä, joten virheitä sisällössä voi esiintyä.

Ominaisuus on rajoitettu (mm. pyynnöt minuutissa, pyynnöt päivässä, tokenit per pyyntö ja samanaikaiset pyynnöt) eikä ole tarkoitettu tuotantokäyttöön.

GitHub Models käyttää Azure AI Content Safety -suodatusta. Näitä suodattimia ei voi poistaa käytöstä GitHub Models -kokemuksessa. Jos päätät käyttää malleja maksullisen palvelun kautta, konfiguroi sisältösuodattimesi tarpeidesi mukaan.

Tämä palvelu on GitHubin esijulkaisuehtojen alainen.

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.