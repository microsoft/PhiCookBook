<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3f37da1518bfb2cc9a8faa427fb0c916",
  "translation_date": "2025-04-03T07:59:22+00:00",
  "source_file": "md\\02.QuickStart\\GitHubModel_QuickStart.md",
  "language_code": "ur"
}
-->
## GitHub ماڈلز - محدود عوامی بیٹا

[GitHub Models](https://github.com/marketplace/models) میں خوش آمدید! ہم نے سب کچھ تیار کر لیا ہے تاکہ آپ Azure AI پر ہوسٹ کیے گئے AI ماڈلز کو دریافت کر سکیں۔

![GitHubModel](../../../../translated_images/GitHub_ModelCatalog.4fc858ab26afe64c43f5e423ad0c5c733878bb536fdb027a5bcf1f80c41b0633.ur.png)

GitHub Models پر دستیاب ماڈلز کے بارے میں مزید معلومات کے لیے [GitHub Model Marketplace](https://github.com/marketplace/models) دیکھیں۔

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

## شروعات کریں

کچھ بنیادی مثالیں تیار ہیں جو آپ فوراً چلا سکتے ہیں۔ آپ انہیں نمونہ ڈائریکٹری میں تلاش کر سکتے ہیں۔ اگر آپ اپنی پسندیدہ زبان میں کام کرنا چاہتے ہیں تو درج ذیل زبانوں میں مثالیں دستیاب ہیں:

- Python
- JavaScript
- cURL

نمونہ کوڈ اور ماڈلز چلانے کے لیے ایک مخصوص Codespaces Environment بھی دستیاب ہے۔

![Getting Started](../../../../translated_images/GitHub_ModelGetStarted.b4b839a081583da39bc976c2f0d8ac4603d3b8c23194b16cc9e0a1014f5611d0.ur.png)

## نمونہ کوڈ 

ذیل میں چند استعمال کے کیسز کے لیے مثال کے طور پر کوڈ کے ٹکڑے دیے گئے ہیں۔ Azure AI Inference SDK کے بارے میں مزید معلومات اور مکمل دستاویزات کے لیے نمونہ دیکھیں۔

## سیٹ اپ 

1. ایک ذاتی رسائی ٹوکن بنائیں
آپ کو ٹوکن کو کسی بھی قسم کی اجازت دینے کی ضرورت نہیں ہے۔ یاد رکھیں کہ ٹوکن Microsoft سروس کو بھیجا جائے گا۔

ذیل کے کوڈ ٹکڑوں کو استعمال کرنے کے لیے، ایک انوائرمنٹ ویریبل بنائیں اور اپنے ٹوکن کو کلائنٹ کوڈ کے لیے کلید کے طور پر سیٹ کریں۔

اگر آپ bash استعمال کر رہے ہیں:
```
export GITHUB_TOKEN="<your-github-token-goes-here>"
```
اگر آپ پاور شیل میں ہیں:

```
$Env:GITHUB_TOKEN="<your-github-token-goes-here>"
```

اگر آپ Windows کمانڈ پرامپٹ استعمال کر رہے ہیں:

```
set GITHUB_TOKEN=<your-github-token-goes-here>
```

## Python نمونہ

### ضروریات انسٹال کریں
pip کے ذریعے Azure AI Inference SDK انسٹال کریں (ضرورت: Python >=3.8):

```
pip install azure-ai-inference
```
### ایک بنیادی کوڈ نمونہ چلائیں

یہ مثال chat completion API کے لیے ایک بنیادی کال کو ظاہر کرتی ہے۔ یہ GitHub AI ماڈل انفرنس اینڈپوائنٹ اور آپ کے GitHub ٹوکن کا استعمال کر رہی ہے۔ یہ کال ہم وقت ساز ہے۔

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

### ایک کثیر مرحلہ گفتگو چلائیں

یہ مثال chat completion API کے ساتھ ایک کثیر مرحلہ گفتگو کو ظاہر کرتی ہے۔ جب ماڈل کو کسی چیٹ ایپلیکیشن کے لیے استعمال کیا جاتا ہے، تو آپ کو اس گفتگو کی تاریخ کو منظم کرنا ہوگا اور تازہ ترین پیغامات ماڈل کو بھیجنے ہوں گے۔

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

### آؤٹ پٹ کو اسٹریم کریں

بہتر صارف تجربے کے لیے، آپ ماڈل کے جواب کو اسٹریم کرنا چاہیں گے تاکہ پہلا ٹوکن جلد ظاہر ہو اور آپ طویل جوابات کے انتظار سے بچ سکیں۔

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

### ضروریات انسٹال کریں

Node.js انسٹال کریں۔

ذیل کے متن کی لائنز کو کاپی کریں اور انہیں اپنے فولڈر میں ایک فائل package.json کے طور پر محفوظ کریں۔

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

نوٹ: @azure/core-sse صرف اس وقت ضروری ہے جب آپ chat completions کے جواب کو اسٹریم کریں۔

اس فولڈر میں ایک ٹرمینل ونڈو کھولیں اور npm install چلائیں۔

ذیل کے کوڈ ٹکڑوں کے لیے، مواد کو ایک فائل sample.js میں کاپی کریں اور node sample.js کے ساتھ چلائیں۔

### ایک بنیادی کوڈ نمونہ چلائیں

یہ مثال chat completion API کے لیے ایک بنیادی کال کو ظاہر کرتی ہے۔ یہ GitHub AI ماڈل انفرنس اینڈپوائنٹ اور آپ کے GitHub ٹوکن کا استعمال کر رہی ہے۔ یہ کال ہم وقت ساز ہے۔

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

### ایک کثیر مرحلہ گفتگو چلائیں

یہ مثال chat completion API کے ساتھ ایک کثیر مرحلہ گفتگو کو ظاہر کرتی ہے۔ جب ماڈل کو کسی چیٹ ایپلیکیشن کے لیے استعمال کیا جاتا ہے، تو آپ کو اس گفتگو کی تاریخ کو منظم کرنا ہوگا اور تازہ ترین پیغامات ماڈل کو بھیجنے ہوں گے۔

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

### آؤٹ پٹ کو اسٹریم کریں
بہتر صارف تجربے کے لیے، آپ ماڈل کے جواب کو اسٹریم کرنا چاہیں گے تاکہ پہلا ٹوکن جلد ظاہر ہو اور آپ طویل جوابات کے انتظار سے بچ سکیں۔

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

ذیل کے کوڈ کو شیل میں پیسٹ کریں:

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
### ایک کثیر مرحلہ گفتگو چلائیں

chat completion API کو کال کریں اور چیٹ کی تاریخ پاس کریں:

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
### آؤٹ پٹ کو اسٹریم کریں

یہ اینڈپوائنٹ کو کال کرنے اور جواب کو اسٹریم کرنے کی ایک مثال ہے۔

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

## GitHub Models کے لیے مفت استعمال اور شرح کی حدود

![Model Catalog](../../../../translated_images/GitHub_Model.0c2abb992151c5407046e2b763af51505ff709f04c0950785e0300fdc8c55a0c.ur.png)

[پلے گراؤنڈ اور مفت API کے استعمال کی شرح کی حدود](https://docs.github.com/en/github-models/prototyping-with-ai-models#rate-limits) آپ کو ماڈلز کے ساتھ تجربات کرنے اور اپنی AI ایپلیکیشن کا پروٹو ٹائپ بنانے میں مدد دینے کے لیے ہیں۔ ان حدود سے آگے استعمال کرنے کے لیے، اور اپنی ایپلیکیشن کو بڑے پیمانے پر لانے کے لیے، آپ کو Azure اکاؤنٹ سے وسائل فراہم کرنے ہوں گے، اور وہاں سے توثیق کرنی ہوگی بجائے کہ آپ کے GitHub ذاتی رسائی ٹوکن کے۔ آپ کو اپنے کوڈ میں کچھ بھی تبدیل کرنے کی ضرورت نہیں ہے۔ مفت درجے کی حدود سے آگے جانے کے لیے Azure AI میں دریافت کرنے کے لیے اس لنک کا استعمال کریں۔

### انکشافات

یاد رکھیں کہ ماڈل کے ساتھ بات چیت کرتے وقت آپ AI کے ساتھ تجربہ کر رہے ہیں، لہذا مواد میں غلطیاں ممکن ہیں۔

فیچر مختلف حدود کے تابع ہے (جیسے کہ فی منٹ درخواستیں، فی دن درخواستیں، فی درخواست ٹوکنز، اور بیک وقت درخواستیں) اور پروڈکشن استعمال کے کیسز کے لیے نہیں بنایا گیا۔

GitHub Models Azure AI Content Safety استعمال کرتا ہے۔ یہ فلٹرز GitHub Models کے تجربے کے حصے کے طور پر بند نہیں کیے جا سکتے۔ اگر آپ ماڈلز کو کسی ادا شدہ سروس کے ذریعے استعمال کرنے کا فیصلہ کرتے ہیں، تو براہ کرم اپنے مواد کے فلٹرز کو اپنی ضروریات کے مطابق ترتیب دیں۔

یہ سروس GitHub کے پری ریلیز شرائط کے تحت ہے۔

**ڈسکلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کے لیے کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی اصل زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے ذمہ دار نہیں ہیں۔