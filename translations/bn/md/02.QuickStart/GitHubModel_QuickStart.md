<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5113634b77370af6790f9697d5d7de90",
  "translation_date": "2025-05-09T20:15:56+00:00",
  "source_file": "md/02.QuickStart/GitHubModel_QuickStart.md",
  "language_code": "bn"
}
-->
## GitHub Models - সীমিত পাবলিক বিটা

[GitHub Models](https://github.com/marketplace/models)-এ আপনাকে স্বাগতম! আমরা সবকিছু প্রস্তুত করে রেখেছি যাতে আপনি Azure AI-তে হোস্ট করা AI মডেলগুলো অন্বেষণ করতে পারেন।

![GitHubModel](../../../../translated_images/GitHub_ModelCatalog.4fc858ab26afe64c43f5e423ad0c5c733878bb536fdb027a5bcf1f80c41b0633.bn.png)

GitHub Models-এ উপলব্ধ মডেলগুলোর সম্পর্কে আরও তথ্যের জন্য, দেখুন [GitHub Model Marketplace](https://github.com/marketplace/models)

## উপলব্ধ মডেলসমূহ

প্রতিটি মডেলের জন্য একটি বিশেষ প্লেগ্রাউন্ড এবং নমুনা কোড রয়েছে

![Phi-3Model_Github](../../../../imgs/01/02/02/GitHub_ModelPlay.png)

### GitHub Model Catalog-এ Phi-3 মডেলসমূহ

[Phi-3-Medium-128k-Instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-128k-instruct)

[Phi-3-medium-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-4k-instruct)

[Phi-3-mini-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-128k-instruct)

[Phi-3-mini-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-4k-instruct)

[Phi-3-small-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-128k-instruct)

[Phi-3-small-8k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-8k-instruct)

## শুরু করা

কিছু মৌলিক উদাহরণ আছে যা আপনি চালাতে প্রস্তুত। এগুলো samples ডিরেক্টরিতে পাবেন। আপনি যদি সরাসরি আপনার পছন্দের ভাষায় যেতে চান, তাহলে নিম্নলিখিত ভাষাগুলোর উদাহরণগুলো দেখতে পারেন:

- Python
- JavaScript
- cURL

নমুনা এবং মডেলগুলো চালানোর জন্য একটি বিশেষ Codespaces Environment-ও রয়েছে।

![Getting Started](../../../../translated_images/GitHub_ModelGetStarted.b4b839a081583da39bc976c2f0d8ac4603d3b8c23194b16cc9e0a1014f5611d0.bn.png)

## নমুনা কোড

নীচে কিছু ব্যবহারিক উদাহরণের কোড স্নিপেট দেওয়া হলো। Azure AI Inference SDK সম্পর্কে বিস্তারিত তথ্য ও আরও নমুনার জন্য সম্পূর্ণ ডকুমেন্টেশন দেখুন।

## সেটআপ

1. একটি personal access token তৈরি করুন  
আপনাকে টোকেনের জন্য কোনো পারমিশন দিতে হবে না। টোকেনটি Microsoft সার্ভিসে পাঠানো হবে।

নিচের কোড স্নিপেটগুলো ব্যবহার করতে, একটি environment variable তৈরি করুন যেখানে আপনার টোকেনটি ক্লায়েন্ট কোডের কী হিসেবে সেট করা থাকবে।

যদি আপনি bash ব্যবহার করেন:  
```
export GITHUB_TOKEN="<your-github-token-goes-here>"
```  
যদি powershell-এ থাকেন:  
```
$Env:GITHUB_TOKEN="<your-github-token-goes-here>"
```  
Windows command prompt ব্যবহার করলে:  
```
set GITHUB_TOKEN=<your-github-token-goes-here>
```

## Python নমুনা

### ডিপেনডেন্সি ইনস্টল করুন  
pip ব্যবহার করে Azure AI Inference SDK ইনস্টল করুন (প্রয়োজন: Python >=3.8):  
```
pip install azure-ai-inference
```

### একটি মৌলিক কোড নমুনা চালান

এই নমুনাটি chat completion API-তে একটি মৌলিক কল দেখায়। এটি GitHub AI মডেল inference endpoint এবং আপনার GitHub টোকেন ব্যবহার করছে। কলটি synchronous।

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

### মাল্টি-টার্ন কথোপকথন চালান

এই নমুনাটি chat completion API-এর মাধ্যমে মাল্টি-টার্ন কথোপকথন প্রদর্শন করে। চ্যাট অ্যাপ্লিকেশনের জন্য মডেল ব্যবহার করার সময়, আপনাকে কথোপকথনের ইতিহাস পরিচালনা করতে হবে এবং সর্বশেষ মেসেজগুলো মডেলে পাঠাতে হবে।

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

### আউটপুট স্ট্রিম করুন

ভালো ব্যবহারকারীর অভিজ্ঞতার জন্য, আপনি মডেলের প্রতিক্রিয়া স্ট্রিম করতে চাইবেন যাতে প্রথম টোকেনটি দ্রুত প্রদর্শিত হয় এবং দীর্ঘ প্রতিক্রিয়ার জন্য অপেক্ষা এড়িয়ে যাওয়া যায়।

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

### ডিপেনডেন্সি ইনস্টল করুন

Node.js ইনস্টল করুন।

নিচের লাইনগুলো কপি করে আপনার ফোল্ডারে package.json নামে একটি ফাইল হিসেবে সংরক্ষণ করুন।

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

দ্রষ্টব্য: @azure/core-sse শুধুমাত্র তখনই প্রয়োজন যখন আপনি chat completions-এর প্রতিক্রিয়া স্ট্রিম করবেন।

এই ফোল্ডারে একটি টার্মিনাল খুলে npm install চালান।

নিচের প্রতিটি কোড স্নিপেটের জন্য, কনটেন্টটি sample.js নামে একটি ফাইলে কপি করুন এবং node sample.js কমান্ড দিয়ে চালান।

### একটি মৌলিক কোড নমুনা চালান

এই নমুনাটি chat completion API-তে একটি মৌলিক কল দেখায়। এটি GitHub AI মডেল inference endpoint এবং আপনার GitHub টোকেন ব্যবহার করছে। কলটি synchronous।

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

### মাল্টি-টার্ন কথোপকথন চালান

এই নমুনাটি chat completion API-এর মাধ্যমে মাল্টি-টার্ন কথোপকথন প্রদর্শন করে। চ্যাট অ্যাপ্লিকেশনের জন্য মডেল ব্যবহার করার সময়, আপনাকে কথোপকথনের ইতিহাস পরিচালনা করতে হবে এবং সর্বশেষ মেসেজগুলো মডেলে পাঠাতে হবে।

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

### আউটপুট স্ট্রিম করুন

ভালো ব্যবহারকারীর অভিজ্ঞতার জন্য, আপনি মডেলের প্রতিক্রিয়া স্ট্রিম করতে চাইবেন যাতে প্রথম টোকেনটি দ্রুত প্রদর্শিত হয় এবং দীর্ঘ প্রতিক্রিয়ার জন্য অপেক্ষা এড়িয়ে যাওয়া যায়।

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

### একটি মৌলিক কোড নমুনা চালান

নিচের কোডটি শেলে পেস্ট করুন:

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

### মাল্টি-টার্ন কথোপকথন চালান

chat completion API কল করুন এবং চ্যাট ইতিহাস পাঠান:

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

### আউটপুট স্ট্রিম করুন

এটি একটি উদাহরণ যেখানে endpoint কল করে প্রতিক্রিয়া স্ট্রিম করা হচ্ছে।

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

## GitHub Models-এর জন্য ফ্রি ব্যবহার এবং রেট লিমিট

![Model Catalog](../../../../translated_images/GitHub_Model.0c2abb992151c5407046e2b763af51505ff709f04c0950785e0300fdc8c55a0c.bn.png)

[প্লেগ্রাউন্ড এবং ফ্রি API ব্যবহারের রেট লিমিটসমূহ](https://docs.github.com/en/github-models/prototyping-with-ai-models#rate-limits) আপনাকে মডেলগুলো পরীক্ষা-নিরীক্ষা এবং AI অ্যাপ্লিকেশন প্রোটোটাইপ তৈরি করতে সাহায্য করার জন্য নির্ধারিত। এই সীমা ছাড়িয়ে ব্যবহার করতে, এবং আপনার অ্যাপ্লিকেশন স্কেল করতে, আপনাকে Azure অ্যাকাউন্ট থেকে রিসোর্স প্রোভিশন করতে হবে এবং GitHub personal access token-এর পরিবর্তে সেখান থেকে অথেনটিকেট করতে হবে। আপনার কোডে অন্য কোনো পরিবর্তন করার প্রয়োজন নেই। Azure AI-তে ফ্রি টিয়ার সীমা ছাড়িয়ে কীভাবে যাবেন তা জানতে এই লিংকটি ব্যবহার করুন।

### তথ্যাদি

মডেলের সাথে ইন্টারঅ্যাক্ট করার সময় মনে রাখবেন, আপনি AI-এর সঙ্গে পরীক্ষা-নিরীক্ষা করছেন, তাই ভুলের সম্ভাবনা রয়েছে।

এই ফিচারটি বিভিন্ন সীমাবদ্ধতার আওতায় (যেমন প্রতি মিনিট অনুরোধ, দৈনিক অনুরোধ, প্রতি অনুরোধ টোকেন সংখ্যা, এবং সমান্তরাল অনুরোধ) এবং এটি প্রোডাকশন ব্যবহারের জন্য ডিজাইন করা হয়নি।

GitHub Models Azure AI Content Safety ব্যবহার করে। এই ফিল্টারগুলো GitHub Models অভিজ্ঞতার অংশ হিসেবে বন্ধ করা যাবে না। আপনি যদি মডেলগুলো পেইড সার্ভিসের মাধ্যমে ব্যবহার করার সিদ্ধান্ত নেন, তবে আপনার কনটেন্ট ফিল্টারগুলো আপনার চাহিদা অনুযায়ী কনফিগার করুন।

এই সার্ভিসটি GitHub-এর প্রি-রিলিজ শর্তাবলীর আওতায় রয়েছে।

**অস্বীকারোক্তি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা সঠিকতার জন্য চেষ্টা করি, তবে অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা ভুল থাকতে পারে। মূল নথিটি তার নিজস্ব ভাষায় কর্তৃত্বপূর্ণ উৎস হিসাবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ প্রয়োজন। এই অনুবাদের ব্যবহারে উদ্ভূত কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।