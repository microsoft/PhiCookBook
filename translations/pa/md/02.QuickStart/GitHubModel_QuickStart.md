<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5113634b77370af6790f9697d5d7de90",
  "translation_date": "2025-07-17T05:34:51+00:00",
  "source_file": "md/02.QuickStart/GitHubModel_QuickStart.md",
  "language_code": "pa"
}
-->
## GitHub ਮਾਡਲ - ਸੀਮਿਤ ਪਬਲਿਕ ਬੀਟਾ

[GitHub Models](https://github.com/marketplace/models) ਵਿੱਚ ਤੁਹਾਡਾ ਸਵਾਗਤ ਹੈ! ਅਸੀਂ ਤੁਹਾਡੇ ਲਈ Azure AI ‘ਤੇ ਹੋਸਟ ਕੀਤੇ ਗਏ AI ਮਾਡਲਾਂ ਦੀ ਖੋਜ ਲਈ ਸਾਰਾ ਕੁਝ ਤਿਆਰ ਕਰ ਦਿੱਤਾ ਹੈ।

![GitHubModel](../../../../translated_images/GitHub_ModelCatalog.aa43c51c36454747.pa.png)

GitHub Models ‘ਤੇ ਉਪਲਬਧ ਮਾਡਲਾਂ ਬਾਰੇ ਹੋਰ ਜਾਣਕਾਰੀ ਲਈ, [GitHub Model Marketplace](https://github.com/marketplace/models) ਵੇਖੋ।

## ਉਪਲਬਧ ਮਾਡਲ

ਹਰ ਮਾਡਲ ਲਈ ਇੱਕ ਸਮਰਪਿਤ ਪਲੇਗ੍ਰਾਊਂਡ ਅਤੇ ਨਮੂਨਾ ਕੋਡ ਹੈ।

![Phi-3Model_Github](../../../../imgs/01/02/02/GitHub_ModelPlay.png)

### GitHub Model Catalog ਵਿੱਚ Phi-3 ਮਾਡਲ

[Phi-3-Medium-128k-Instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-128k-instruct)

[Phi-3-medium-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-4k-instruct)

[Phi-3-mini-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-128k-instruct)

[Phi-3-mini-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-4k-instruct)

[Phi-3-small-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-128k-instruct)

[Phi-3-small-8k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-8k-instruct)

## ਸ਼ੁਰੂਆਤ

ਕੁਝ ਬੁਨਿਆਦੀ ਉਦਾਹਰਣਾਂ ਤੁਹਾਡੇ ਲਈ ਤਿਆਰ ਹਨ। ਤੁਸੀਂ ਇਹਨਾਂ ਨੂੰ samples ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ ਲੱਭ ਸਕਦੇ ਹੋ। ਜੇ ਤੁਸੀਂ ਆਪਣੀ ਮਨਪਸੰਦ ਭਾਸ਼ਾ ਵਿੱਚ ਸਿੱਧਾ ਜਾਣਾ ਚਾਹੁੰਦੇ ਹੋ, ਤਾਂ ਉਦਾਹਰਣਾਂ ਹੇਠਾਂ ਦਿੱਤੀਆਂ ਭਾਸ਼ਾਵਾਂ ਵਿੱਚ ਮਿਲਣਗੀਆਂ:

- Python  
- JavaScript  
- cURL  

ਨਮੂਨੇ ਅਤੇ ਮਾਡਲ ਚਲਾਉਣ ਲਈ ਇੱਕ ਸਮਰਪਿਤ Codespaces Environment ਵੀ ਉਪਲਬਧ ਹੈ।

![Getting Started](../../../../translated_images/GitHub_ModelGetStarted.150220a802da6fb6.pa.png)

## ਨਮੂਨਾ ਕੋਡ

ਹੇਠਾਂ ਕੁਝ ਵਰਤੋਂ ਦੇ ਕੇਸਾਂ ਲਈ ਉਦਾਹਰਣ ਕੋਡ ਸਨਿੱਪੇਟ ਦਿੱਤੇ ਗਏ ਹਨ। Azure AI Inference SDK ਬਾਰੇ ਵਧੇਰੇ ਜਾਣਕਾਰੀ ਲਈ ਪੂਰੀ ਡੌਕਯੂਮੈਂਟੇਸ਼ਨ ਅਤੇ ਨਮੂਨੇ ਵੇਖੋ।

## ਸੈਟਅਪ

1. ਇੱਕ personal access token ਬਣਾਓ  
ਤੁਹਾਨੂੰ ਟੋਕਨ ਨੂੰ ਕਿਸੇ ਵੀ ਪਰਮੀਸ਼ਨ ਦੇਣ ਦੀ ਲੋੜ ਨਹੀਂ ਹੈ। ਧਿਆਨ ਰੱਖੋ ਕਿ ਟੋਕਨ ਮਾਈਕ੍ਰੋਸਾਫਟ ਸਰਵਿਸ ਨੂੰ ਭੇਜਿਆ ਜਾਵੇਗਾ।

ਹੇਠਾਂ ਦਿੱਤੇ ਕੋਡ ਸਨਿੱਪੇਟ ਵਰਤਣ ਲਈ, ਆਪਣੇ ਟੋਕਨ ਨੂੰ client ਕੋਡ ਲਈ ਕੁੰਜੀ ਵਜੋਂ ਸੈੱਟ ਕਰਨ ਲਈ ਇੱਕ environment variable ਬਣਾਓ।

ਜੇ ਤੁਸੀਂ bash ਵਰਤ ਰਹੇ ਹੋ:  
```
export GITHUB_TOKEN="<your-github-token-goes-here>"
```  
ਜੇ ਤੁਸੀਂ powershell ਵਿੱਚ ਹੋ:  

```
$Env:GITHUB_TOKEN="<your-github-token-goes-here>"
```  

ਜੇ ਤੁਸੀਂ Windows command prompt ਵਰਤ ਰਹੇ ਹੋ:  

```
set GITHUB_TOKEN=<your-github-token-goes-here>
```  

## Python ਨਮੂਨਾ

### Dependencies ਇੰਸਟਾਲ ਕਰੋ  
pip ਦੀ ਵਰਤੋਂ ਕਰਕੇ Azure AI Inference SDK ਇੰਸਟਾਲ ਕਰੋ (ਲੋੜ: Python >=3.8):  

```
pip install azure-ai-inference
```  
### ਇੱਕ ਬੁਨਿਆਦੀ ਕੋਡ ਨਮੂਨਾ ਚਲਾਓ

ਇਹ ਨਮੂਨਾ chat completion API ਨੂੰ ਬੁਨਿਆਦੀ ਤਰੀਕੇ ਨਾਲ ਕਾਲ ਕਰਦਾ ਹੈ। ਇਹ GitHub AI ਮਾਡਲ ਇਨਫਰੈਂਸ ਐਂਡਪੌਇੰਟ ਅਤੇ ਤੁਹਾਡੇ GitHub ਟੋਕਨ ਦੀ ਵਰਤੋਂ ਕਰਦਾ ਹੈ। ਕਾਲ synchronous ਹੈ।  

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

### ਬਹੁ-ਚਰਚਾ ਸੰਵਾਦ ਚਲਾਓ

ਇਹ ਨਮੂਨਾ chat completion API ਨਾਲ ਬਹੁ-ਚਰਚਾ ਸੰਵਾਦ ਦਿਖਾਉਂਦਾ ਹੈ। ਜਦੋਂ ਤੁਸੀਂ ਮਾਡਲ ਨੂੰ ਚੈਟ ਐਪਲੀਕੇਸ਼ਨ ਲਈ ਵਰਤਦੇ ਹੋ, ਤਾਂ ਤੁਹਾਨੂੰ ਉਸ ਸੰਵਾਦ ਦਾ ਇਤਿਹਾਸ ਸੰਭਾਲਣਾ ਪੈਂਦਾ ਹੈ ਅਤੇ ਮਾਡਲ ਨੂੰ ਤਾਜ਼ਾ ਸੁਨੇਹੇ ਭੇਜਣੇ ਪੈਂਦੇ ਹਨ।  

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

### ਆਉਟਪੁੱਟ ਸਟ੍ਰੀਮ ਕਰੋ

ਵਧੀਆ ਯੂਜ਼ਰ ਅਨੁਭਵ ਲਈ, ਤੁਸੀਂ ਮਾਡਲ ਦੇ ਜਵਾਬ ਨੂੰ ਸਟ੍ਰੀਮ ਕਰਨਾ ਚਾਹੋਗੇ ਤਾਂ ਜੋ ਪਹਿਲਾ ਟੋਕਨ ਜਲਦੀ ਦਿਖਾਈ ਦੇਵੇ ਅਤੇ ਲੰਬੇ ਜਵਾਬਾਂ ਦੀ ਉਡੀਕ ਨਾ ਕਰਨੀ ਪਵੇ।  

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

### Dependencies ਇੰਸਟਾਲ ਕਰੋ

Node.js ਇੰਸਟਾਲ ਕਰੋ।

ਹੇਠਾਂ ਦਿੱਤੀਆਂ ਲਾਈਨਾਂ ਨੂੰ ਕਾਪੀ ਕਰਕੇ ਆਪਣੇ ਫੋਲਡਰ ਵਿੱਚ package.json ਨਾਮਕ ਫਾਇਲ ਵਜੋਂ ਸੇਵ ਕਰੋ।  

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

ਨੋਟ: @azure/core-sse ਸਿਰਫ਼ ਚੈਟ ਕਮਪਲੀਸ਼ਨ ਦੇ ਜਵਾਬ ਨੂੰ ਸਟ੍ਰੀਮ ਕਰਨ ਲਈ ਲੋੜੀਂਦਾ ਹੈ।

ਇਸ ਫੋਲਡਰ ਵਿੱਚ ਟਰਮੀਨਲ ਖੋਲ੍ਹੋ ਅਤੇ npm install ਚਲਾਓ।

ਹੇਠਾਂ ਦਿੱਤੇ ਹਰ ਕੋਡ ਸਨਿੱਪੇਟ ਲਈ, ਸਮੱਗਰੀ ਨੂੰ sample.js ਫਾਇਲ ਵਿੱਚ ਕਾਪੀ ਕਰੋ ਅਤੇ node sample.js ਨਾਲ ਚਲਾਓ।

### ਇੱਕ ਬੁਨਿਆਦੀ ਕੋਡ ਨਮੂਨਾ ਚਲਾਓ

ਇਹ ਨਮੂਨਾ chat completion API ਨੂੰ ਬੁਨਿਆਦੀ ਤਰੀਕੇ ਨਾਲ ਕਾਲ ਕਰਦਾ ਹੈ। ਇਹ GitHub AI ਮਾਡਲ ਇਨਫਰੈਂਸ ਐਂਡਪੌਇੰਟ ਅਤੇ ਤੁਹਾਡੇ GitHub ਟੋਕਨ ਦੀ ਵਰਤੋਂ ਕਰਦਾ ਹੈ। ਕਾਲ synchronous ਹੈ।  

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

### ਬਹੁ-ਚਰਚਾ ਸੰਵਾਦ ਚਲਾਓ

ਇਹ ਨਮੂਨਾ chat completion API ਨਾਲ ਬਹੁ-ਚਰਚਾ ਸੰਵਾਦ ਦਿਖਾਉਂਦਾ ਹੈ। ਜਦੋਂ ਤੁਸੀਂ ਮਾਡਲ ਨੂੰ ਚੈਟ ਐਪਲੀਕੇਸ਼ਨ ਲਈ ਵਰਤਦੇ ਹੋ, ਤਾਂ ਤੁਹਾਨੂੰ ਉਸ ਸੰਵਾਦ ਦਾ ਇਤਿਹਾਸ ਸੰਭਾਲਣਾ ਪੈਂਦਾ ਹੈ ਅਤੇ ਮਾਡਲ ਨੂੰ ਤਾਜ਼ਾ ਸੁਨੇਹੇ ਭੇਜਣੇ ਪੈਂਦੇ ਹਨ।  

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

### ਆਉਟਪੁੱਟ ਸਟ੍ਰੀਮ ਕਰੋ

ਵਧੀਆ ਯੂਜ਼ਰ ਅਨੁਭਵ ਲਈ, ਤੁਸੀਂ ਮਾਡਲ ਦੇ ਜਵਾਬ ਨੂੰ ਸਟ੍ਰੀਮ ਕਰਨਾ ਚਾਹੋਗੇ ਤਾਂ ਜੋ ਪਹਿਲਾ ਟੋਕਨ ਜਲਦੀ ਦਿਖਾਈ ਦੇਵੇ ਅਤੇ ਲੰਬੇ ਜਵਾਬਾਂ ਦੀ ਉਡੀਕ ਨਾ ਕਰਨੀ ਪਵੇ।  

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

### ਇੱਕ ਬੁਨਿਆਦੀ ਕੋਡ ਨਮੂਨਾ ਚਲਾਓ

ਹੇਠਾਂ ਦਿੱਤਾ ਕੋਡ shell ਵਿੱਚ ਪੇਸਟ ਕਰੋ:  

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

### ਬਹੁ-ਚਰਚਾ ਸੰਵਾਦ ਚਲਾਓ

chat completion API ਨੂੰ ਕਾਲ ਕਰੋ ਅਤੇ ਚੈਟ ਇਤਿਹਾਸ ਭੇਜੋ:  

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

### ਆਉਟਪੁੱਟ ਸਟ੍ਰੀਮ ਕਰੋ

ਇਹ ਐਂਡਪੌਇੰਟ ਨੂੰ ਕਾਲ ਕਰਨ ਅਤੇ ਜਵਾਬ ਸਟ੍ਰੀਮ ਕਰਨ ਦਾ ਉਦਾਹਰਣ ਹੈ।  

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

## GitHub ਮਾਡਲਾਂ ਲਈ ਮੁਫ਼ਤ ਵਰਤੋਂ ਅਤੇ ਰੇਟ ਸੀਮਾਵਾਂ

![Model Catalog](../../../../translated_images/GitHub_Model.ca6c125cb3117d0e.pa.png)

[ਪਲੇਗ੍ਰਾਊਂਡ ਅਤੇ ਮੁਫ਼ਤ API ਵਰਤੋਂ ਲਈ ਰੇਟ ਸੀਮਾਵਾਂ](https://docs.github.com/en/github-models/prototyping-with-ai-models#rate-limits) ਤੁਹਾਨੂੰ ਮਾਡਲਾਂ ਨਾਲ ਪ੍ਰਯੋਗ ਕਰਨ ਅਤੇ ਆਪਣੀ AI ਐਪਲੀਕੇਸ਼ਨ ਦਾ ਪ੍ਰੋਟੋਟਾਈਪ ਬਣਾਉਣ ਵਿੱਚ ਮਦਦ ਕਰਨ ਲਈ ਹਨ। ਇਨ੍ਹਾਂ ਸੀਮਾਵਾਂ ਤੋਂ ਬਾਹਰ ਵਰਤੋਂ ਲਈ, ਅਤੇ ਆਪਣੀ ਐਪਲੀਕੇਸ਼ਨ ਨੂੰ ਵੱਡੇ ਪੱਧਰ ‘ਤੇ ਲਿਜਾਣ ਲਈ, ਤੁਹਾਨੂੰ Azure ਖਾਤੇ ਤੋਂ ਸਰੋਤ ਪ੍ਰਦਾਨ ਕਰਨੇ ਪੈਣਗੇ ਅਤੇ ਉਥੋਂ ਪ੍ਰਮਾਣਿਕਤਾ ਕਰਨੀ ਪਵੇਗੀ, ਨਾ ਕਿ ਆਪਣੇ GitHub personal access token ਨਾਲ। ਤੁਹਾਨੂੰ ਆਪਣੇ ਕੋਡ ਵਿੱਚ ਹੋਰ ਕੁਝ ਬਦਲਣ ਦੀ ਲੋੜ ਨਹੀਂ। Azure AI ਵਿੱਚ ਮੁਫ਼ਤ ਟੀਅਰ ਸੀਮਾਵਾਂ ਤੋਂ ਬਾਹਰ ਜਾਣ ਲਈ ਇਸ ਲਿੰਕ ਦੀ ਵਰਤੋਂ ਕਰੋ।

### ਖੁਲਾਸੇ

ਜਦੋਂ ਤੁਸੀਂ ਕਿਸੇ ਮਾਡਲ ਨਾਲ ਇੰਟਰੈਕਟ ਕਰ ਰਹੇ ਹੋ, ਤਾਂ ਯਾਦ ਰੱਖੋ ਕਿ ਤੁਸੀਂ AI ਨਾਲ ਪ੍ਰਯੋਗ ਕਰ ਰਹੇ ਹੋ, ਇਸ ਲਈ ਸਮੱਗਰੀ ਵਿੱਚ ਗਲਤੀਆਂ ਹੋ ਸਕਦੀਆਂ ਹਨ।

ਇਹ ਫੀਚਰ ਵੱਖ-ਵੱਖ ਸੀਮਾਵਾਂ (ਜਿਵੇਂ ਕਿ ਪ੍ਰਤੀ ਮਿੰਟ ਬੇਨਤੀਆਂ, ਪ੍ਰਤੀ ਦਿਨ ਬੇਨਤੀਆਂ, ਪ੍ਰਤੀ ਬੇਨਤੀ ਟੋਕਨ, ਅਤੇ ਸਮਕਾਲੀ ਬੇਨਤੀਆਂ) ਦੇ ਅਧੀਨ ਹੈ ਅਤੇ ਪ੍ਰੋਡਕਸ਼ਨ ਵਰਤੋਂ ਲਈ ਨਹੀਂ ਬਣਾਇਆ ਗਿਆ।

GitHub Models Azure AI Content Safety ਵਰਤਦਾ ਹੈ। ਇਹ ਫਿਲਟਰ GitHub Models ਦੇ ਅਨੁਭਵ ਦਾ ਹਿੱਸਾ ਹੋਣ ਕਰਕੇ ਬੰਦ ਨਹੀਂ ਕੀਤੇ ਜਾ ਸਕਦੇ। ਜੇ ਤੁਸੀਂ ਕਿਸੇ ਭੁਗਤਾਨੀ ਸੇਵਾ ਰਾਹੀਂ ਮਾਡਲ ਵਰਤਦੇ ਹੋ, ਤਾਂ ਕਿਰਪਾ ਕਰਕੇ ਆਪਣੀਆਂ ਸਮੱਗਰੀ ਫਿਲਟਰਾਂ ਨੂੰ ਆਪਣੀਆਂ ਜ਼ਰੂਰਤਾਂ ਅਨੁਸਾਰ ਸੰਰਚਿਤ ਕਰੋ।

ਇਹ ਸੇਵਾ GitHub ਦੇ Pre-release Terms ਦੇ ਅਧੀਨ ਹੈ।

**ਅਸਵੀਕਾਰੋਪਣ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਅਤ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮਰਥਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਉਤਪੰਨ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।