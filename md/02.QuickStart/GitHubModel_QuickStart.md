## GitHub Models (retired) - Phi Quickstart with the OpenAI SDK

> [!IMPORTANT]
> **GitHub Models was retired on July 30, 2026** ([GitHub changelog](https://github.blog/changelog/2026-07-30-github-models-is-now-retired/)). The playground, model catalog and inference API are no longer available, so the old `https://models.inference.ai.azure.com` and `https://models.github.ai/inference` endpoints no longer work. The Azure AI Inference beta SDK (`azure-ai-inference`) that earlier versions of this page used was also [retired on August 26, 2026](https://learn.microsoft.com/azure/foundry-classic/foundry-models/supported-languages).
>
> The samples below now use the [OpenAI SDK](https://github.com/openai/openai-python) against an OpenAI-compatible endpoint. You can use either:
> - **Microsoft Foundry** (cloud, requires an Azure subscription): deploy a Phi model and use `https://<resource>.openai.azure.com/openai/v1/`. See [Getting started with Microsoft Foundry](./AzureAIFoundry_QuickStart.md) and [Migrate from Azure AI Inference SDK to OpenAI SDK](https://learn.microsoft.com/azure/foundry/how-to/model-inference-to-openai-migration).
> - **Foundry Local** (runs on your own device, no Azure subscription needed): see [Phi in Foundry Local](../01.Introduction/02/07.FoundryLocal.md).

## Setup

The samples read three environment variables:

| Variable | Microsoft Foundry | Foundry Local |
| --- | --- | --- |
| `OPENAI_BASE_URL` | `https://<resource>.openai.azure.com/openai/v1/` | `http://localhost:<port>/v1` (get the port from `foundry server status`) |
| `OPENAI_API_KEY` | The API key of your Foundry resource | Any non-empty value, for example `none` |
| `MODEL` | Your deployment name, for example a deployment of `Phi-4-mini-instruct` | The model ID shown by `foundry model list --loaded --verbose`, after you start a model such as `foundry run phi-4-mini` |

If you're using bash:
```
export OPENAI_BASE_URL="https://<resource>.openai.azure.com/openai/v1/"
export OPENAI_API_KEY="<your-api-key>"
export MODEL="<your-phi-deployment-name>"
```
If you're in powershell:

```
$Env:OPENAI_BASE_URL="https://<resource>.openai.azure.com/openai/v1/"
$Env:OPENAI_API_KEY="<your-api-key>"
$Env:MODEL="<your-phi-deployment-name>"
```

If you're using Windows command prompt:

```
set OPENAI_BASE_URL=https://<resource>.openai.azure.com/openai/v1/
set OPENAI_API_KEY=<your-api-key>
set MODEL=<your-phi-deployment-name>
```

To use Microsoft Entra ID instead of an API key with Microsoft Foundry, see the [migration guide](https://learn.microsoft.com/azure/foundry/how-to/model-inference-to-openai-migration).

## Python Sample

### Install dependencies
Install the OpenAI SDK using pip:

```
pip install openai
```
### Run a basic code sample

This sample demonstrates a basic call to the chat completion API. The call is synchronous.

```python
import os
from openai import OpenAI

client = OpenAI(
    base_url=os.environ["OPENAI_BASE_URL"],
    api_key=os.environ["OPENAI_API_KEY"],
)

response = client.chat.completions.create(
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"},
    ],
    model=os.environ["MODEL"],
    temperature=1.,
    max_tokens=1000,
    top_p=1.
)

print(response.choices[0].message.content)
```

### Run a multi-turn conversation

This sample demonstrates a multi-turn conversation with the chat completion API. When using the model for a chat application, you'll need to manage the history of that conversation and send the latest messages to the model.

```python
import os
from openai import OpenAI

client = OpenAI(
    base_url=os.environ["OPENAI_BASE_URL"],
    api_key=os.environ["OPENAI_API_KEY"],
)

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is the capital of France?"},
    {"role": "assistant", "content": "The capital of France is Paris."},
    {"role": "user", "content": "What about Spain?"},
]

response = client.chat.completions.create(messages=messages, model=os.environ["MODEL"])

print(response.choices[0].message.content)
```

### Stream the output

For a better user experience, you will want to stream the response of the model so that the first token shows up early and you avoid waiting for long responses.

```python
import os
from openai import OpenAI

client = OpenAI(
    base_url=os.environ["OPENAI_BASE_URL"],
    api_key=os.environ["OPENAI_API_KEY"],
)

response = client.chat.completions.create(
    stream=True,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Give me 5 good reasons why I should exercise every day."},
    ],
    model=os.environ["MODEL"],
)

for update in response:
    if update.choices:
        print(update.choices[0].delta.content or "", end="")

client.close()
```
## JavaScript 

### Install dependencies

Install Node.js, then open a terminal in your folder and run:

```
npm install openai
```

For each of the code snippets below, copy the content into a file sample.mjs and run with node sample.mjs.

### Run a basic code sample

This sample demonstrates a basic call to the chat completion API.

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  baseURL: process.env["OPENAI_BASE_URL"],
  apiKey: process.env["OPENAI_API_KEY"],
});

const response = await client.chat.completions.create({
  messages: [
    { role: "system", content: "You are a helpful assistant." },
    { role: "user", content: "What is the capital of France?" }
  ],
  model: process.env["MODEL"],
  temperature: 1.,
  max_tokens: 1000,
  top_p: 1.
});

console.log(response.choices[0].message.content);
```

### Run a multi-turn conversation

This sample demonstrates a multi-turn conversation with the chat completion API. When using the model for a chat application, you'll need to manage the history of that conversation and send the latest messages to the model.

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  baseURL: process.env["OPENAI_BASE_URL"],
  apiKey: process.env["OPENAI_API_KEY"],
});

const response = await client.chat.completions.create({
  messages: [
    { role: "system", content: "You are a helpful assistant." },
    { role: "user", content: "What is the capital of France?" },
    { role: "assistant", content: "The capital of France is Paris." },
    { role: "user", content: "What about Spain?" },
  ],
  model: process.env["MODEL"],
});

for (const choice of response.choices) {
  console.log(choice.message.content);
}
```

### Stream the output
For a better user experience, you will want to stream the response of the model so that the first token shows up early and you avoid waiting for long responses.

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  baseURL: process.env["OPENAI_BASE_URL"],
  apiKey: process.env["OPENAI_API_KEY"],
});

const stream = await client.chat.completions.create({
  messages: [
    { role: "system", content: "You are a helpful assistant." },
    { role: "user", content: "Give me 5 good reasons why I should exercise every day." },
  ],
  model: process.env["MODEL"],
  stream: true
});

for await (const chunk of stream) {
  process.stdout.write(chunk.choices[0]?.delta?.content ?? "");
}
```

## REST 

### Run a basic code sample

Paste the following into a bash shell. Microsoft Foundry reads the key from the `api-key` header; Foundry Local ignores it.

```
curl -X POST "${OPENAI_BASE_URL%/}/chat/completions" \
    -H "Content-Type: application/json" \
    -H "api-key: $OPENAI_API_KEY" \
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
        "model": "'"$MODEL"'"
    }'
```
### Run a multi-turn conversation

Call the chat completion API and pass the chat history:

```
curl -X POST "${OPENAI_BASE_URL%/}/chat/completions" \
    -H "Content-Type: application/json" \
    -H "api-key: $OPENAI_API_KEY" \
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
        "model": "'"$MODEL"'"
    }'
```
### Stream the output

This is an example of calling the endpoint and streaming the response.

```
curl -X POST "${OPENAI_BASE_URL%/}/chat/completions" \
    -H "Content-Type: application/json" \
    -H "api-key: $OPENAI_API_KEY" \
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
        "model": "'"$MODEL"'"
    }'
```

### Disclosures

Remember when interacting with a model you are experimenting with AI, so content mistakes are possible.

If you use Microsoft Foundry, configure the content filters of your deployment to meet your requirements.
