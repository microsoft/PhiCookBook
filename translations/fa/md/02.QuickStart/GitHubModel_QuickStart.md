<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5113634b77370af6790f9697d5d7de90",
  "translation_date": "2025-03-27T13:29:31+00:00",
  "source_file": "md\\02.QuickStart\\GitHubModel_QuickStart.md",
  "language_code": "fa"
}
-->
## مدل‌های GitHub - نسخه بتای عمومی محدود

به [مدل‌های GitHub](https://github.com/marketplace/models) خوش آمدید! همه‌چیز آماده است تا مدل‌های هوش مصنوعی میزبانی شده در Azure AI را کشف کنید.

![GitHubModel](../../../../translated_images/GitHub_ModelCatalog.4fc858ab26afe64c43f5e423ad0c5c733878bb536fdb027a5bcf1f80c41b0633.fa.png)

برای اطلاعات بیشتر درباره مدل‌های موجود در GitHub Models، به [بازار مدل‌های GitHub](https://github.com/marketplace/models) سر بزنید.

## مدل‌های موجود

هر مدل یک محیط آزمایشی اختصاصی و کد نمونه دارد.

![Phi-3Model_Github](../../../../imgs/01/02/02/GitHub_ModelPlay.png)

### مدل‌های Phi-3 در کاتالوگ مدل‌های GitHub

[Phi-3-Medium-128k-Instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-128k-instruct)

[Phi-3-medium-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-4k-instruct)

[Phi-3-mini-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-128k-instruct)

[Phi-3-mini-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-4k-instruct)

[Phi-3-small-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-128k-instruct)

[Phi-3-small-8k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-8k-instruct)

## شروع به کار

چند مثال ساده آماده اجرا برای شما وجود دارد. می‌توانید آنها را در پوشه نمونه‌ها پیدا کنید. اگر می‌خواهید مستقیماً به زبان مورد علاقه خود بروید، مثال‌ها را در زبان‌های زیر پیدا خواهید کرد:

- Python  
- JavaScript  
- cURL  

همچنین یک محیط اختصاصی Codespaces برای اجرای نمونه‌ها و مدل‌ها در دسترس است.

![Getting Started](../../../../translated_images/GitHub_ModelGetStarted.b4b839a081583da39bc976c2f0d8ac4603d3b8c23194b16cc9e0a1014f5611d0.fa.png)

## کد نمونه

در زیر کدهای نمونه برای چند مورد استفاده آورده شده است. برای اطلاعات بیشتر درباره Azure AI Inference SDK، به مستندات کامل و نمونه‌ها مراجعه کنید.

## تنظیمات اولیه

1. ایجاد یک توکن دسترسی شخصی  
نیازی نیست که هیچ مجوزی به این توکن بدهید. توجه داشته باشید که این توکن به یک سرویس مایکروسافت ارسال خواهد شد.

برای استفاده از کدهای زیر، یک متغیر محیطی ایجاد کنید تا توکن خود را به‌عنوان کلید برای کد کلاینت تنظیم کنید.

اگر از bash استفاده می‌کنید:  
```
export GITHUB_TOKEN="<your-github-token-goes-here>"
```  
اگر از powershell استفاده می‌کنید:  

```
$Env:GITHUB_TOKEN="<your-github-token-goes-here>"
```  

اگر از خط فرمان ویندوز استفاده می‌کنید:  

```
set GITHUB_TOKEN=<your-github-token-goes-here>
```  

## نمونه Python

### نصب وابستگی‌ها  
Azure AI Inference SDK را با استفاده از pip نصب کنید (نیازمند: Python >=3.8):  

```
pip install azure-ai-inference
```  

### اجرای یک نمونه کد پایه  

این نمونه یک فراخوانی پایه به API تکمیل چت را نشان می‌دهد. این نمونه از نقطه پایانی استنتاج مدل AI GitHub و توکن GitHub شما استفاده می‌کند. این فراخوانی به‌صورت همزمان انجام می‌شود.

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

### اجرای یک مکالمه چند مرحله‌ای  

این نمونه یک مکالمه چند مرحله‌ای با API تکمیل چت را نشان می‌دهد. هنگام استفاده از مدل برای یک برنامه چت، باید تاریخچه مکالمه را مدیریت کرده و جدیدترین پیام‌ها را به مدل ارسال کنید.

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

### استریم خروجی  

برای تجربه بهتر کاربر، می‌خواهید پاسخ مدل را استریم کنید تا اولین توکن زودتر نمایش داده شود و از انتظار برای پاسخ‌های طولانی جلوگیری کنید.

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

خطوط زیر را کپی کرده و به‌عنوان یک فایل package.json داخل پوشه خود ذخیره کنید.  

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

توجه: @azure/core-sse تنها زمانی نیاز است که پاسخ تکمیل چت را استریم کنید.  

یک پنجره ترمینال را در این پوشه باز کرده و npm install را اجرا کنید.  

برای هر یک از کدهای زیر، محتوا را در یک فایل sample.js کپی کرده و با node sample.js اجرا کنید.  

### اجرای یک نمونه کد پایه  

این نمونه یک فراخوانی پایه به API تکمیل چت را نشان می‌دهد. این نمونه از نقطه پایانی استنتاج مدل AI GitHub و توکن GitHub شما استفاده می‌کند. این فراخوانی به‌صورت همزمان انجام می‌شود.

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

### اجرای یک مکالمه چند مرحله‌ای  

این نمونه یک مکالمه چند مرحله‌ای با API تکمیل چت را نشان می‌دهد. هنگام استفاده از مدل برای یک برنامه چت، باید تاریخچه مکالمه را مدیریت کرده و جدیدترین پیام‌ها را به مدل ارسال کنید.

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

### استریم خروجی  

برای تجربه بهتر کاربر، می‌خواهید پاسخ مدل را استریم کنید تا اولین توکن زودتر نمایش داده شود و از انتظار برای پاسخ‌های طولانی جلوگیری کنید.

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

### اجرای یک نمونه کد پایه  

متن زیر را در یک شل کپی کنید:  

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

### اجرای یک مکالمه چند مرحله‌ای  

API تکمیل چت را فراخوانی کرده و تاریخچه چت را ارسال کنید:  

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

### استریم خروجی  

این نمونه‌ای از فراخوانی نقطه پایانی و استریم پاسخ است.

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

## استفاده رایگان و محدودیت‌های نرخ برای مدل‌های GitHub  

![Model Catalog](../../../../translated_images/GitHub_Model.0c2abb992151c5407046e2b763af51505ff709f04c0950785e0300fdc8c55a0c.fa.png)

[محدودیت‌های نرخ برای محیط آزمایش و استفاده رایگان از API](https://docs.github.com/en/github-models/prototyping-with-ai-models#rate-limits) برای کمک به شما در آزمایش مدل‌ها و نمونه‌سازی برنامه AI شما طراحی شده‌اند. برای استفاده فراتر از این محدودیت‌ها و مقیاس‌بندی برنامه خود، باید منابعی را از یک حساب Azure تهیه کنید و از آنجا احراز هویت کنید، به‌جای استفاده از توکن دسترسی شخصی GitHub. نیازی به تغییر چیز دیگری در کد شما نیست. از این لینک استفاده کنید تا بیاموزید چگونه می‌توانید از محدودیت‌های سطح رایگان در Azure AI فراتر بروید.

### افشاگری‌ها  

به یاد داشته باشید که هنگام تعامل با یک مدل، شما در حال آزمایش هوش مصنوعی هستید، بنابراین احتمال اشتباه در محتوا وجود دارد.  

این ویژگی تحت محدودیت‌های مختلفی قرار دارد (از جمله درخواست‌ها در دقیقه، درخواست‌ها در روز، توکن‌ها در هر درخواست، و درخواست‌های همزمان) و برای موارد استفاده تولیدی طراحی نشده است.  

مدل‌های GitHub از Azure AI Content Safety استفاده می‌کنند. این فیلترها به‌عنوان بخشی از تجربه مدل‌های GitHub قابل غیرفعال کردن نیستند. اگر تصمیم دارید مدل‌ها را از طریق یک سرویس پولی به کار ببرید، لطفاً فیلترهای محتوای خود را برای برآورده کردن نیازهای خود پیکربندی کنید.  

این سرویس تحت شرایط پیش‌انتشار GitHub است.  

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما تلاش می‌کنیم دقت را حفظ کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان اصلی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حساس، توصیه می‌شود از ترجمه انسانی حرفه‌ای استفاده کنید. ما مسئول هیچ‌گونه سوءتفاهم یا تفسیر نادرست ناشی از استفاده از این ترجمه نیستیم.