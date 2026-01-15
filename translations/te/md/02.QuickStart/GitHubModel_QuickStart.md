<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5113634b77370af6790f9697d5d7de90",
  "translation_date": "2025-12-21T19:03:55+00:00",
  "source_file": "md/02.QuickStart/GitHubModel_QuickStart.md",
  "language_code": "te"
}
-->
## GitHub మోడల్స్ - పరిమితం చేయబడిన పబ్లిక్ బీటా

మీరు [GitHub మోడల్స్](https://github.com/marketplace/models)లోకి స్వాగతం! మా వద్ద Azure AI లో హోస్ట్ చేయబడిన AI మోడల్స్‌ను మీరు అన్వేషించడానికి అన్నీ సిద్ధంగా ఉన్నాయి.

![GitHub మోడల్](../../../../translated_images/te/GitHub_ModelCatalog.aa43c51c36454747.webp)

GitHub మోడల్స్‌లో లభ్యమయ్యే మోడల్స్ గురించి మరింత సమాచారం కోసం, [GitHub Model Marketplace](https://github.com/marketplace/models)ని చూడండి

## లభ్యమయ్యే మోడల్స్

ప్రతి మోడల్‌కు ప్రత్యేక ప్లేగ్రౌండ్ మరియు నమూనా కోడ్ ఉంది 

![Phi-3 మోడల్_Github](../../../../imgs/01/02/02/GitHub_ModelPlay.png)

### GitHub మోడల్ క్యాటలాగ్‌లో Phi-3 మోడల్స్

[Phi-3-Medium-128k-Instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-128k-instruct)

[Phi-3-medium-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-4k-instruct)

[Phi-3-mini-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-128k-instruct)

[Phi-3-mini-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-4k-instruct)

[Phi-3-small-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-128k-instruct)

[Phi-3-small-8k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-8k-instruct)

## ప్రారంభించడానికి

మీరు అమలు చేయడానికి సిద్ధంగా ఉండే కొన్ని ప్రాథమిక ఉదాహరణలు ఉన్నాయి. మీరు వాటిని samples డైరెక్టరీలో కనుగొనవచ్చు. మీకు నేరుగా మీ ప్రియ భాషకు వెళ్లాలనిపిస్తే, మీరు క్రింది భాషలలో ఉదాహరణలను కనుగొనవచ్చు:

- Python
- JavaScript
- cURL

నమూనాలు మరియు మోడల్స్ నడపడానికి ఒక ప్రత్యేక Codespaces పరిసరము కూడా ఉంది। 

![ప్రారంభించడానికి](../../../../translated_images/te/GitHub_ModelGetStarted.150220a802da6fb6.webp)


## నమూనా కోడ్ 

కింద కొన్ని ఉపయోగకరమైన సందర్భాల కోసం ఉదాహరణ కోడ్ స్నిపెట్లను చూడవచ్చు. Azure AI Inference SDK గురించి అదనపు సమాచారం కోసం, పూర్తి డాక్యుమెంటేషన్ మరియు నమూనాలను చూడండి.

## సెటప్ 

1. వ్యక్తిగత యాక్సెస్ టోకెన్ సృష్టించండి
మీరు టోకెన్ కోసం ఏ అనుమతులను ఇవ్వకూడదు. గమనించండి టోకెన్ ఒక Microsoft సేవకు పంపబడే అవకాశం ఉంది.

క్రింది కోడ్ స్నిపెట్లను ఉపయోగించడానికి, మీ టోకెన్‌ను క్లయింట్ కోడ్ కోసం కీగా సెట్ చేయడానికి ఒక ఎన్విరాన్‌మెంట్ వేరియబుల్ సృష్టించండి.

If you're using bash:
```
export GITHUB_TOKEN="<your-github-token-goes-here>"
```
If you're in powershell:

```
$Env:GITHUB_TOKEN="<your-github-token-goes-here>"
```

If you're using Windows command prompt:

```
set GITHUB_TOKEN=<your-github-token-goes-here>
```

## Python నమూనా

### డిపెండెన్సీలు ఇన్స్టాల్ చేయండి
pip ఉపయోగించి Azure AI Inference SDKని ఇన్స్టాల్ చేయండి (అవశ్యకతలు: Python >=3.8):

```
pip install azure-ai-inference
```
### ఒక ప్రాథమిక కోడ్ నమూనాను అమలు చేయండి

ఈ నమూనా chat completion APIకి ఒక ప్రాథమిక కాల్‌ను చూపిస్తుంది. ఇది GitHub AI మోడల్ ఇన్ఫరెన్స్ ఎండ్‌పాయింట్ మరియు మీ GitHub టోకెన్‌ను ఉపయోగిస్తుంది. కాల్ సింక్రోనస్‌గా ఉంటుంది.

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

### బహు-టర్న్ సంభాషణ నిర్వహించండి

ఈ నమూనా chat completion APIతో బహు-టర్న్ సంభాషణను చూపిస్తుంది. చాట్ అప్లికేషన్ కోసం మోడల్‌ను ఉపయోగించినప్పుడు, మీరు ఆ సంభాషణ యొక్క చరిత్రను నిర్వహించి, తాజా సందేశాలను మోడల్‌కు పంపాలి.

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

### అవుట్‌పుట్‌ని స్ట్రీమ్ చేయండి

మరింత మెరుగైన యూజర్ అనుభవం కోసం, మోడల్ యొక్క స్పందనను స్ట్రీమ్ చేయుడం ద్వారా మొదటి టోకెన్ శీఘ్రంగా ప్రదర్శించబడుతుంది మరియు நீలమైన ప్రతిస్పందనలు కోసం వేచి ఉండాల్సిన అవసరం తగ్గుతుంది.

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

### డిపెండెన్సీలు ఇన్స్టాల్ చేయండి

Node.jsని ఇన్స్టాల్ చేయండి.

క్రింది పాఠ్యాన్ని కాపీ చేసి మీ ఫోల్డర్‌లో package.json అని ఫైల్‌గా సేవ్ చేయండి.

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

గమనిక: @azure/core-sse కేవలం మీరు chat completions responseను స్ట్రీమ్ చేసేటప్పుడు అవసరం అవుతుంది.

ఈ ఫోల్డర్‌లో టెర్మినల్ విండో ఓపెన్ చేసి npm install నడపండి.

క్రింద ఉన్న ప్రతి కోడ్ స్నిపెట్ కోసం, కంటెంట్‌ను ఒక sample.js ఫైల్‌లో కాపీ చేసి node sample.js తో నడపండి.

### ఒక ప్రాథమిక కోడ్ నమూనాను అమలు చేయండి

ఈ నమూనా chat completion APIకి ఒక ప్రాథమిక కాల్‌ను చూపిస్తుంది. ఇది GitHub AI మోడల్ ఇన్ఫరెన్స్ ఎండ్‌పాయింట్ మరియు మీ GitHub టోకెన్‌ను ఉపయోగిస్తుంది. కాల్ సింక్రోనస్‌గా ఉంటుంది.

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

### బహు-టర్న్ సంభాషణ నిర్వహించండి

ఈ నమూనా chat completion APIతో బహు-టర్న్ సంభాషణను చూపిస్తుంది. చాట్ అప్లికేషన్ కోసం మోడల్‌ను ఉపయోగించినప్పుడు, మీరు ఆ సంభాషణ యొక్క చరిత్రను నిర్వహించి, తాజా సందేశాలను మోడల్‌కు పంపాలి.

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

### అవుట్‌పుట్‌ని స్ట్రీమ్ చేయండి
మరింత మెరుగైన యూజర్ అనుభవం కోసం, మోడల్ యొక్క స్పందనను స్ట్రీమ్ చేయుడం ద్వారా మొదటి టోకెన్ శీఘ్రంగా ప్రదర్శించబడుతుంది మరియు நீలమైన ప్రతిస్పందనలు కోసం వేచి ఉండాల్సిన అవసరం తగ్గుతుంది.

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

### ఒక ప్రాథమిక కోడ్ నమూనాను అమలు చేయండి

కింద పేర్కొన్నదాన్ని shellలో పేస్ట్ చేయండి:

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
### బహు-టర్న్ సంభాషణను అమలు చేయండి

chat completion APIని కాల్ చేసి చాట్ చరిత్రను పంపండి:

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
### అవుట్‌పుట్‌ని స్ట్రీమ్ చేయండి

ఇది ఎండ్‌పాయింట్‌ను కాల్ చేసి స్పందనను స్ట్రీమ్ చేసే ఉదాహరణ.

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

## GitHub మోడల్స్ కోసం ఉచిత వినియోగం మరియు రేటు పరిమితులు

![మోడల్ క్యాటలాగ్](../../../../translated_images/te/GitHub_Model.ca6c125cb3117d0e.webp)

[playground మరియు ఉచిత API వినియోగం కోసం రేటు పరిమితులు](https://docs.github.com/en/github-models/prototyping-with-ai-models#rate-limits) మోడల్స్‌తో ప్రయోగాలు చేయడానికి మరియు మీ AI అప్లికేషన్‌ను ప్రోటోటైపింగ్ చేయడానికి సహాయపడటానికి ఉద్దేశించబడ్డాయి. ఆ పరిమితులను మించిన వినియోగానికి, మీ అప్లికేషన్‌ను స్కేల్ చేయడానికి మరియు ఉత్పత్తి ఉపయోగాలకి సరిపడా వనరులను అందించడానికి, మీరు Azure అకౌంట్ నుండి వనరులను ప్రొవిషన్ చేయాలి మరియు అక్కడ నుండి authenticate చేయాలి (మీ GitHub వ్యక్తిగత యాక్సెస్ టోకెన్ బదులుగా). మీ కోడ్లో ఇంకేనైనా మార్పు చేయాల్సిన అవసరం లేదు. Azure AIలో ఉచిత స్థాయి పరిమితులను దాటిపోయే విధంగా ఎలా చేయాలో కనుగొనడానికి ఈ లింక్ ఉపయోగించండి.


### వెల్లడింపులు

మోడల్‌తో పరస్పర చర్య చేసే సమయంలో మీరు AIతో ప్రయోగం చేస్తున్నారని గుర్తుంచుకోండి, కాబట్టి కంటెంట్ లో పొరపాట్లు జరిగే అవకాశాలు ఉన్నాయి.

ఈ ఫీచర్ వివిధ పరిమితులకు (నిమిషానికి అభ్యర్థనలు, రోజుకు అభ్యర్థనలు, అభ్యర్థనలో టోకెన్లు, సమకాలీకృత అభ్యర్థనలు మొదలైనవి) విధ్వంసకమయ్యేలా ఉంటుంది మరియు ఉత్పత్తి వినియోగానికి గాను రూపుదిద్దుకోబడలేదు.

GitHub మోడల్స్ Azure AI Content Safetyను ఉపయోగిస్తుంది. ఈ ఫిల్టర్లు GitHub మోడల్స్ అనుభవంలోని భాగంగా ఆఫ్ చేయలేవు. మీరు చెల్లింపు సేవ ద్వారా మోడల్స్‌ను ఉపయోగించాలని నిర్ణయిస్తే, దయచేసి మీ కంటెంట్ ఫిల్టర్లను మీ అవసరాలకు అనుగుణంగా కాన్ఫిగర్ చేయండి.

ఈ సర్వీస్ GitHub యొక్క ప్రి-రిలీజ్ నిబంధనలకు లోబడి ఉంది.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
డిస్క్లైమర్:
ఈ దస్త్రం AI అనువాద సేవ Co-op Translator (https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, ఆటోమేటెడ్ అనువాదాల్లో పొరపాట్లు లేదా లోపాలు ఉండొచ్చు. మూల పత్రాన్ని దాని స్వదేశీ (మూల) భాషలో ఉన్న వర్షన్‌ను అధికారిక మూలంగా పరిగణించాలి. కీలకమైన సమాచారం కోసం వృత్తిపరమైన మానవ అనువాదాన్ని సూచిస్తాము. ఈ అనువాదాన్ని ఉపయోగించడం వల్ల ఏర్పడే ఏవైనా అపార్థాలు లేదా తప్పుగా అర్థం చేసుకోవడాల కారణంగా కలిగే నష్టాలకు మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->