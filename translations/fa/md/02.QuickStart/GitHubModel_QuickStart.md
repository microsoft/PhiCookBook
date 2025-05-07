<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5113634b77370af6790f9697d5d7de90",
  "translation_date": "2025-05-07T13:07:28+00:00",
  "source_file": "md/02.QuickStart/GitHubModel_QuickStart.md",
  "language_code": "fa"
}
-->
## GitHub Models - نسخه آزمایشی عمومی محدود

به [GitHub Models](https://github.com/marketplace/models) خوش آمدید! همه چیز آماده است تا شما مدل‌های هوش مصنوعی میزبانی‌شده روی Azure AI را بررسی کنید.

![GitHubModel](../../../../translated_images/GitHub_ModelCatalog.aa43c51c36454747ca1cc1ffa799db02cc66b4fb7e8495311701adb072442df8.fa.png)

برای اطلاعات بیشتر درباره مدل‌های موجود در GitHub Models، به [بازار مدل‌های GitHub](https://github.com/marketplace/models) مراجعه کنید.

## مدل‌های موجود

هر مدل دارای یک محیط آزمایشی اختصاصی و نمونه کد است

![Phi-3Model_Github](../../../../imgs/01/02/02/GitHub_ModelPlay.png)

### مدل‌های Phi-3 در فهرست مدل‌های GitHub

[Phi-3-Medium-128k-Instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-128k-instruct)

[Phi-3-medium-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-4k-instruct)

[Phi-3-mini-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-128k-instruct)

[Phi-3-mini-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-4k-instruct)

[Phi-3-small-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-128k-instruct)

[Phi-3-small-8k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-8k-instruct)

## شروع کار

چند مثال ساده آماده اجرا برای شما وجود دارد. می‌توانید آن‌ها را در پوشه samples پیدا کنید. اگر می‌خواهید مستقیماً به زبان مورد علاقه‌تان بروید، نمونه‌ها در زبان‌های زیر موجود هستند:

- Python  
- JavaScript  
- cURL  

همچنین یک محیط اختصاصی Codespaces برای اجرای نمونه‌ها و مدل‌ها فراهم شده است.

![Getting Started](../../../../translated_images/GitHub_ModelGetStarted.150220a802da6fb67944ad93c1a4c7b8a9811e43d77879a149ecf54c02928c6b.fa.png)

## نمونه کد

در ادامه چند قطعه کد نمونه برای چند کاربرد مختلف آورده شده است. برای اطلاعات بیشتر درباره Azure AI Inference SDK، مستندات کامل و نمونه‌ها را ببینید.

## راه‌اندازی

1. یک توکن دسترسی شخصی بسازید  
نیازی نیست به توکن هیچ دسترسی خاصی بدهید. توجه داشته باشید که توکن به یک سرویس مایکروسافت ارسال خواهد شد.

برای استفاده از قطعات کد زیر، یک متغیر محیطی بسازید و توکن خود را به عنوان کلید برای کد کلاینت تنظیم کنید.

اگر از bash استفاده می‌کنید:  
```
export GITHUB_TOKEN="<your-github-token-goes-here>"
```  
اگر در powershell هستید:  

```
$Env:GITHUB_TOKEN="<your-github-token-goes-here>"
```  

اگر از خط فرمان ویندوز استفاده می‌کنید:  

```
set GITHUB_TOKEN=<your-github-token-goes-here>
```  

## نمونه Python

### نصب وابستگی‌ها  
Azure AI Inference SDK را با pip نصب کنید (نیازمند: Python >=3.8):

```
pip install azure-ai-inference
```  
### اجرای نمونه کد ساده

این نمونه یک فراخوانی ساده به API تکمیل چت را نشان می‌دهد. از نقطه پایان مدل هوش مصنوعی GitHub و توکن GitHub شما استفاده می‌کند. این فراخوانی به صورت هم‌زمان است.

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

### اجرای مکالمه چند مرحله‌ای

این نمونه یک مکالمه چند مرحله‌ای با API تکمیل چت را نشان می‌دهد. هنگام استفاده از مدل برای یک برنامه چت، باید تاریخچه مکالمه را مدیریت کرده و آخرین پیام‌ها را به مدل ارسال کنید.

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

### پخش خروجی به صورت جریان

برای تجربه کاربری بهتر، می‌خواهید پاسخ مدل را به صورت جریان دریافت کنید تا اولین توکن زودتر نمایش داده شود و از انتظار طولانی برای پاسخ‌های طولانی جلوگیری شود.

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

### نصب وابستگی‌ها

Node.js را نصب کنید.

خطوط زیر را کپی کرده و در یک فایل package.json داخل پوشه خود ذخیره کنید.

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

توجه: @azure/core-sse فقط زمانی لازم است که پاسخ تکمیل چت را به صورت جریان دریافت کنید.

یک پنجره ترمینال در این پوشه باز کنید و npm install را اجرا کنید.

برای هر کدام از قطعات کد زیر، محتوا را در یک فایل sample.js کپی کنید و با دستور node sample.js اجرا کنید.

### اجرای نمونه کد ساده

این نمونه یک فراخوانی ساده به API تکمیل چت را نشان می‌دهد. از نقطه پایان مدل هوش مصنوعی GitHub و توکن GitHub شما استفاده می‌کند. این فراخوانی به صورت هم‌زمان است.

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

### اجرای مکالمه چند مرحله‌ای

این نمونه یک مکالمه چند مرحله‌ای با API تکمیل چت را نشان می‌دهد. هنگام استفاده از مدل برای یک برنامه چت، باید تاریخچه مکالمه را مدیریت کرده و آخرین پیام‌ها را به مدل ارسال کنید.

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

### پخش خروجی به صورت جریان

برای تجربه کاربری بهتر، می‌خواهید پاسخ مدل را به صورت جریان دریافت کنید تا اولین توکن زودتر نمایش داده شود و از انتظار طولانی برای پاسخ‌های طولانی جلوگیری شود.

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

### اجرای نمونه کد ساده

دستور زیر را در یک شل بچسبانید:

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
### اجرای مکالمه چند مرحله‌ای

API تکمیل چت را فراخوانی کنید و تاریخچه چت را ارسال کنید:

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
### پخش خروجی به صورت جریان

این نمونه‌ای از فراخوانی نقطه پایان و دریافت پاسخ به صورت جریان است.

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

## استفاده رایگان و محدودیت‌های نرخ برای GitHub Models

![Model Catalog](../../../../translated_images/GitHub_Model.ca6c125cb3117d0ea7c2e204b066ee4619858d28e7b1a419c262443c5e9a2d5b.fa.png)

[محدودیت‌های نرخ برای محیط آزمایشی و استفاده رایگان API](https://docs.github.com/en/github-models/prototyping-with-ai-models#rate-limits) به شما کمک می‌کنند تا مدل‌ها را آزمایش کرده و برنامه هوش مصنوعی خود را نمونه‌سازی کنید. برای استفاده فراتر از این محدودیت‌ها و مقیاس‌گذاری برنامه خود، باید منابع را از حساب Azure تهیه کنید و به جای توکن دسترسی شخصی GitHub، از آن احراز هویت کنید. نیازی به تغییر هیچ چیز دیگری در کد خود ندارید. با استفاده از این لینک می‌توانید روش فراتر رفتن از محدودیت‌های رایگان در Azure AI را بیابید.

### افشاگرها

به یاد داشته باشید هنگام تعامل با مدل، در حال آزمایش هوش مصنوعی هستید و امکان اشتباه در محتوا وجود دارد.

این ویژگی محدودیت‌های مختلفی دارد (شامل درخواست‌ها در دقیقه، درخواست‌ها در روز، توکن‌ها در هر درخواست و درخواست‌های همزمان) و برای موارد استفاده تولیدی طراحی نشده است.

GitHub Models از Azure AI Content Safety استفاده می‌کند. این فیلترها در تجربه GitHub Models قابل غیرفعال کردن نیستند. اگر تصمیم به استفاده از مدل‌ها از طریق سرویس پولی گرفتید، لطفاً فیلترهای محتوای خود را مطابق نیازهای خود تنظیم کنید.

این سرویس تحت شرایط پیش‌انتشار GitHub قرار دارد.

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما برای دقت تلاش می‌کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل اشتباهات یا نادرستی‌هایی باشند. سند اصلی به زبان بومی خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، توصیه می‌شود از ترجمه حرفه‌ای انسانی استفاده شود. ما مسئول هیچ گونه سوءتفاهم یا تفسیر نادرستی که از استفاده این ترجمه ناشی شود، نیستیم.