<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5113634b77370af6790f9697d5d7de90",
  "translation_date": "2025-07-17T05:31:43+00:00",
  "source_file": "md/02.QuickStart/GitHubModel_QuickStart.md",
  "language_code": "ur"
}
-->
## GitHub Models - محدود عوامی بیٹا

[GitHub Models](https://github.com/marketplace/models) میں خوش آمدید! ہم نے Azure AI پر میزبانی کیے گئے AI ماڈلز کو دریافت کرنے کے لیے سب کچھ تیار کر رکھا ہے۔

![GitHubModel](../../../../translated_images/ur/GitHub_ModelCatalog.aa43c51c36454747.webp)

GitHub Models پر دستیاب ماڈلز کے بارے میں مزید معلومات کے لیے، [GitHub Model Marketplace](https://github.com/marketplace/models) دیکھیں۔

## دستیاب ماڈلز

ہر ماڈل کے لیے ایک مخصوص پلے گراؤنڈ اور نمونہ کوڈ موجود ہے۔

![Phi-3Model_Github](../../../../imgs/01/02/02/GitHub_ModelPlay.png)

### GitHub Model Catalog میں Phi-3 ماڈلز

[Phi-3-Medium-128k-Instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-128k-instruct)

[Phi-3-medium-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-4k-instruct)

[Phi-3-mini-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-128k-instruct)

[Phi-3-mini-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-4k-instruct)

[Phi-3-small-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-128k-instruct)

[Phi-3-small-8k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-8k-instruct)

## شروع کرنے کا طریقہ

چند بنیادی مثالیں آپ کے چلانے کے لیے تیار ہیں۔ آپ انہیں samples ڈائریکٹری میں پا سکتے ہیں۔ اگر آپ اپنی پسندیدہ زبان پر سیدھا جانا چاہتے ہیں، تو آپ درج ذیل زبانوں میں مثالیں دیکھ سکتے ہیں:

- Python  
- JavaScript  
- cURL  

نمونہ اور ماڈلز چلانے کے لیے ایک مخصوص Codespaces ماحول بھی موجود ہے۔

![Getting Started](../../../../translated_images/ur/GitHub_ModelGetStarted.150220a802da6fb6.webp)

## نمونہ کوڈ

نیچے چند استعمال کے کیسز کے لیے مثال کوڈ کے ٹکڑے دیے گئے ہیں۔ Azure AI Inference SDK کے بارے میں مزید معلومات کے لیے مکمل دستاویزات اور نمونے دیکھیں۔

## سیٹ اپ

1. ایک personal access token بنائیں  
آپ کو ٹوکن کے لیے کوئی اجازتیں دینے کی ضرورت نہیں ہے۔ نوٹ کریں کہ یہ ٹوکن مائیکروسافٹ سروس کو بھیجا جائے گا۔

نیچے دیے گئے کوڈ کے ٹکڑوں کو استعمال کرنے کے لیے، ایک environment variable بنائیں اور اپنے ٹوکن کو کلائنٹ کوڈ کے لیے کلید کے طور پر سیٹ کریں۔

اگر آپ bash استعمال کر رہے ہیں:  
```
export GITHUB_TOKEN="<your-github-token-goes-here>"
```  
اگر آپ powershell میں ہیں:  

```
$Env:GITHUB_TOKEN="<your-github-token-goes-here>"
```  

اگر آپ Windows command prompt استعمال کر رہے ہیں:  

```
set GITHUB_TOKEN=<your-github-token-goes-here>
```  

## Python نمونہ

### dependencies انسٹال کریں  
pip کے ذریعے Azure AI Inference SDK انسٹال کریں (ضروریات: Python >=3.8):

```
pip install azure-ai-inference
```  
### ایک بنیادی کوڈ نمونہ چلائیں

یہ نمونہ chat completion API کو بنیادی کال دکھاتا ہے۔ یہ GitHub AI ماڈل inference endpoint اور آپ کے GitHub ٹوکن کا استعمال کر رہا ہے۔ کال synchronous ہے۔

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

### ملٹی ٹرن گفتگو چلائیں

یہ نمونہ chat completion API کے ساتھ ملٹی ٹرن گفتگو دکھاتا ہے۔ جب آپ ماڈل کو چیٹ ایپلیکیشن کے لیے استعمال کرتے ہیں، تو آپ کو اس گفتگو کی تاریخ کو منظم کرنا ہوگا اور تازہ ترین پیغامات ماڈل کو بھیجنے ہوں گے۔

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

### آؤٹ پٹ کو stream کریں

بہتر صارف تجربے کے لیے، آپ ماڈل کے جواب کو stream کرنا چاہیں گے تاکہ پہلا ٹوکن جلد ظاہر ہو اور آپ طویل جوابات کے انتظار سے بچ سکیں۔

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

### dependencies انسٹال کریں

Node.js انسٹال کریں۔

مندرجہ ذیل لائنیں کاپی کریں اور انہیں اپنے فولڈر میں package.json کے طور پر محفوظ کریں۔

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

نوٹ: @azure/core-sse صرف اس وقت درکار ہے جب آپ chat completions کے جواب کو stream کر رہے ہوں۔

اس فولڈر میں ٹرمینل کھولیں اور npm install چلائیں۔

نیچے دیے گئے ہر کوڈ ٹکڑے کے لیے، مواد کو sample.js میں کاپی کریں اور node sample.js کے ساتھ چلائیں۔

### ایک بنیادی کوڈ نمونہ چلائیں

یہ نمونہ chat completion API کو بنیادی کال دکھاتا ہے۔ یہ GitHub AI ماڈل inference endpoint اور آپ کے GitHub ٹوکن کا استعمال کر رہا ہے۔ کال synchronous ہے۔

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

### ملٹی ٹرن گفتگو چلائیں

یہ نمونہ chat completion API کے ساتھ ملٹی ٹرن گفتگو دکھاتا ہے۔ جب آپ ماڈل کو چیٹ ایپلیکیشن کے لیے استعمال کرتے ہیں، تو آپ کو اس گفتگو کی تاریخ کو منظم کرنا ہوگا اور تازہ ترین پیغامات ماڈل کو بھیجنے ہوں گے۔

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

### آؤٹ پٹ کو stream کریں

بہتر صارف تجربے کے لیے، آپ ماڈل کے جواب کو stream کرنا چاہیں گے تاکہ پہلا ٹوکن جلد ظاہر ہو اور آپ طویل جوابات کے انتظار سے بچ سکیں۔

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

### ایک بنیادی کوڈ نمونہ چلائیں

مندرجہ ذیل کو shell میں پیسٹ کریں:

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
### ملٹی ٹرن گفتگو چلائیں

chat completion API کو کال کریں اور chat history بھیجیں:

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
### آؤٹ پٹ کو stream کریں

یہ endpoint کو کال کرنے اور جواب کو stream کرنے کی مثال ہے۔

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

## GitHub Models کے لیے مفت استعمال اور ریٹ لمٹس

![Model Catalog](../../../../translated_images/ur/GitHub_Model.ca6c125cb3117d0e.webp)

[playground اور مفت API استعمال کے لیے rate limits](https://docs.github.com/en/github-models/prototyping-with-ai-models#rate-limits) آپ کو ماڈلز کے ساتھ تجربہ کرنے اور اپنی AI ایپلیکیشن کا پروٹوٹائپ بنانے میں مدد دیتی ہیں۔ ان حدود سے آگے استعمال کے لیے، اور اپنی ایپلیکیشن کو اسکیل کرنے کے لیے، آپ کو Azure اکاؤنٹ سے وسائل فراہم کرنے ہوں گے، اور وہاں سے authentication کرنا ہوگا بجائے اپنے GitHub personal access token کے۔ آپ کو اپنے کوڈ میں کوئی اور تبدیلی کرنے کی ضرورت نہیں۔ Azure AI میں مفت سطح کی حدود سے آگے جانے کے لیے اس لنک کا استعمال کریں۔

### انکشافات

یاد رکھیں کہ جب آپ ماڈل کے ساتھ تعامل کر رہے ہوتے ہیں تو آپ AI کے ساتھ تجربہ کر رہے ہوتے ہیں، اس لیے مواد میں غلطیاں ممکن ہیں۔

یہ فیچر مختلف حدود (جیسے کہ فی منٹ درخواستیں، فی دن درخواستیں، فی درخواست ٹوکنز، اور متوازی درخواستیں) کے تابع ہے اور پروڈکشن استعمال کے لیے نہیں بنایا گیا۔

GitHub Models Azure AI Content Safety استعمال کرتا ہے۔ یہ فلٹرز GitHub Models کے تجربے کے حصے کے طور پر بند نہیں کیے جا سکتے۔ اگر آپ ماڈلز کو کسی ادائیگی شدہ سروس کے ذریعے استعمال کرنے کا فیصلہ کرتے ہیں، تو براہ کرم اپنے مواد کے فلٹرز کو اپنی ضروریات کے مطابق ترتیب دیں۔

یہ سروس GitHub کے Pre-release Terms کے تحت ہے۔

**دستخطی نوٹ**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم پر عائد نہیں ہوتی۔