<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5113634b77370af6790f9697d5d7de90",
  "translation_date": "2025-07-17T05:33:48+00:00",
  "source_file": "md/02.QuickStart/GitHubModel_QuickStart.md",
  "language_code": "bn"
}
-->
## GitHub Models - সীমিত পাবলিক বিটা

[GitHub Models](https://github.com/marketplace/models)-এ আপনাকে স্বাগতম! আমরা Azure AI-তে হোস্ট করা AI মডেলগুলি অন্বেষণ করার জন্য সবকিছু প্রস্তুত করে রেখেছি।

![GitHubModel](../../../../translated_images/GitHub_ModelCatalog.aa43c51c36454747ca1cc1ffa799db02cc66b4fb7e8495311701adb072442df8.bn.png)

GitHub Models-এ উপলব্ধ মডেলগুলোর সম্পর্কে আরও তথ্যের জন্য, [GitHub Model Marketplace](https://github.com/marketplace/models) দেখুন।

## উপলব্ধ মডেলসমূহ

প্রতিটি মডেলের জন্য একটি নির্দিষ্ট প্লেগ্রাউন্ড এবং নমুনা কোড রয়েছে।

![Phi-3Model_Github](../../../../imgs/01/02/02/GitHub_ModelPlay.png)

### GitHub Model Catalog-এ Phi-3 মডেলসমূহ

[Phi-3-Medium-128k-Instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-128k-instruct)

[Phi-3-medium-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-4k-instruct)

[Phi-3-mini-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-128k-instruct)

[Phi-3-mini-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-4k-instruct)

[Phi-3-small-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-128k-instruct)

[Phi-3-small-8k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-8k-instruct)

## শুরু করা

কিছু মৌলিক উদাহরণ আপনার ব্যবহারের জন্য প্রস্তুত আছে। এগুলো samples ডিরেক্টরিতে পাওয়া যাবে। আপনি যদি সরাসরি আপনার পছন্দের ভাষায় যেতে চান, তাহলে নিচের ভাষাগুলোর উদাহরণগুলো দেখতে পারেন:

- Python
- JavaScript
- cURL

নমুনা এবং মডেল চালানোর জন্য একটি নির্দিষ্ট Codespaces Environment-ও রয়েছে।

![Getting Started](../../../../translated_images/GitHub_ModelGetStarted.150220a802da6fb67944ad93c1a4c7b8a9811e43d77879a149ecf54c02928c6b.bn.png)

## নমুনা কোড

নিচে কয়েকটি ব্যবহারের জন্য উদাহরণ কোড স্নিপেট দেওয়া হয়েছে। Azure AI Inference SDK সম্পর্কে আরও তথ্যের জন্য পূর্ণ ডকুমেন্টেশন এবং নমুনাগুলো দেখুন।

## সেটআপ

1. একটি personal access token তৈরি করুন  
আপনাকে টোকেনের জন্য কোনো অনুমতি দিতে হবে না। মনে রাখবেন, টোকেনটি একটি Microsoft সার্ভিসে পাঠানো হবে।

নিচের কোড স্নিপেটগুলো ব্যবহার করার জন্য, আপনার টোকেনকে ক্লায়েন্ট কোডের কী হিসেবে সেট করার জন্য একটি environment variable তৈরি করুন।

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

### নির্ভরশীলতা ইনস্টল করুন  
pip ব্যবহার করে Azure AI Inference SDK ইনস্টল করুন (প্রয়োজন: Python >=3.8):  

```
pip install azure-ai-inference
```  
### একটি মৌলিক কোড নমুনা চালান

এই নমুনাটি chat completion API-তে একটি মৌলিক কল প্রদর্শন করে। এটি GitHub AI মডেল inference endpoint এবং আপনার GitHub টোকেন ব্যবহার করছে। কলটি synchronous।

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

এই নমুনাটি chat completion API-র মাধ্যমে মাল্টি-টার্ন কথোপকথন দেখায়। যখন মডেলটি একটি চ্যাট অ্যাপ্লিকেশনের জন্য ব্যবহার করবেন, তখন আপনাকে কথোপকথনের ইতিহাস পরিচালনা করতে হবে এবং সর্বশেষ মেসেজগুলো মডেলে পাঠাতে হবে।

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

ভালো ব্যবহারকারীর অভিজ্ঞতার জন্য, আপনি মডেলের প্রতিক্রিয়া স্ট্রিম করতে চাইবেন যাতে প্রথম টোকেন দ্রুত প্রদর্শিত হয় এবং দীর্ঘ প্রতিক্রিয়ার জন্য অপেক্ষা এড়ানো যায়।

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

### নির্ভরশীলতা ইনস্টল করুন

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

দ্রষ্টব্য: @azure/core-sse শুধুমাত্র তখনই প্রয়োজন যখন আপনি chat completions এর প্রতিক্রিয়া স্ট্রিম করবেন।

এই ফোল্ডারে একটি টার্মিনাল উইন্ডো খুলে npm install চালান।

নিচের প্রতিটি কোড স্নিপেটের জন্য, বিষয়বস্তু sample.js নামে একটি ফাইলে কপি করুন এবং node sample.js দিয়ে চালান।

### একটি মৌলিক কোড নমুনা চালান

এই নমুনাটি chat completion API-তে একটি মৌলিক কল প্রদর্শন করে। এটি GitHub AI মডেল inference endpoint এবং আপনার GitHub টোকেন ব্যবহার করছে। কলটি synchronous।

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

এই নমুনাটি chat completion API-র মাধ্যমে মাল্টি-টার্ন কথোপকথন দেখায়। যখন মডেলটি একটি চ্যাট অ্যাপ্লিকেশনের জন্য ব্যবহার করবেন, তখন আপনাকে কথোপকথনের ইতিহাস পরিচালনা করতে হবে এবং সর্বশেষ মেসেজগুলো মডেলে পাঠাতে হবে।

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

ভালো ব্যবহারকারীর অভিজ্ঞতার জন্য, আপনি মডেলের প্রতিক্রিয়া স্ট্রিম করতে চাইবেন যাতে প্রথম টোকেন দ্রুত প্রদর্শিত হয় এবং দীর্ঘ প্রতিক্রিয়ার জন্য অপেক্ষা এড়ানো যায়।

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

নিচের কোডটি একটি শেলে পেস্ট করুন:

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

এটি একটি উদাহরণ যেখানে endpoint কল করে প্রতিক্রিয়া স্ট্রিম করা হচ্ছে।

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

## GitHub Models-এর জন্য ফ্রি ব্যবহার এবং রেট সীমা

![Model Catalog](../../../../translated_images/GitHub_Model.ca6c125cb3117d0ea7c2e204b066ee4619858d28e7b1a419c262443c5e9a2d5b.bn.png)

[প্লেগ্রাউন্ড এবং ফ্রি API ব্যবহারের রেট সীমা](https://docs.github.com/en/github-models/prototyping-with-ai-models#rate-limits) আপনাকে মডেলগুলো পরীক্ষা-নিরীক্ষা এবং AI অ্যাপ্লিকেশন প্রোটোটাইপ করার জন্য সাহায্য করে। এই সীমার বাইরে ব্যবহারের জন্য এবং আপনার অ্যাপ্লিকেশনকে স্কেলে নিয়ে যেতে, আপনাকে Azure অ্যাকাউন্ট থেকে রিসোর্স প্রোভিশন করতে হবে এবং GitHub personal access token-এর পরিবর্তে সেখান থেকে প্রমাণীকরণ করতে হবে। আপনার কোডে অন্য কোনো পরিবর্তন করার দরকার নেই। Azure AI-তে ফ্রি টিয়ার সীমার বাইরে যাওয়ার জন্য এই লিঙ্কটি ব্যবহার করুন।

### প্রকাশনা

মডেলের সাথে কাজ করার সময় মনে রাখবেন, আপনি AI নিয়ে পরীক্ষা-নিরীক্ষা করছেন, তাই বিষয়বস্তুতে ভুল হওয়ার সম্ভাবনা রয়েছে।

এই ফিচারটি বিভিন্ন সীমাবদ্ধতার আওতায় (যেমন প্রতি মিনিটে অনুরোধ, দিনে অনুরোধ, প্রতি অনুরোধ টোকেন সংখ্যা, এবং সমান্তরাল অনুরোধ) এবং এটি প্রোডাকশন ব্যবহারের জন্য ডিজাইন করা হয়নি।

GitHub Models Azure AI Content Safety ব্যবহার করে। এই ফিল্টারগুলো GitHub Models অভিজ্ঞতার অংশ হিসেবে বন্ধ করা যায় না। আপনি যদি পেইড সার্ভিসের মাধ্যমে মডেল ব্যবহার করার সিদ্ধান্ত নেন, তাহলে আপনার কনটেন্ট ফিল্টারগুলো আপনার প্রয়োজন অনুযায়ী কনফিগার করুন।

এই সার্ভিসটি GitHub-এর Pre-release Terms-এর আওতায় রয়েছে।

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার নিজস্ব ভাষায়ই কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ গ্রহণ করার পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহারে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।