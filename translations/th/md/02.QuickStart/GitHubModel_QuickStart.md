<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5113634b77370af6790f9697d5d7de90",
  "translation_date": "2025-05-09T20:18:18+00:00",
  "source_file": "md/02.QuickStart/GitHubModel_QuickStart.md",
  "language_code": "th"
}
-->
## GitHub Models - Limited Public Beta

ยินดีต้อนรับสู่ [GitHub Models](https://github.com/marketplace/models)! เราเตรียมทุกอย่างไว้พร้อมให้คุณสำรวจ AI Models ที่โฮสต์บน Azure AI

![GitHubModel](../../../../translated_images/GitHub_ModelCatalog.4fc858ab26afe64c43f5e423ad0c5c733878bb536fdb027a5bcf1f80c41b0633.th.png)

สำหรับข้อมูลเพิ่มเติมเกี่ยวกับ Models ที่มีอยู่ใน GitHub Models โปรดดูที่ [GitHub Model Marketplace](https://github.com/marketplace/models)

## Models Available

แต่ละโมเดลมีพื้นที่เล่นและตัวอย่างโค้ดเฉพาะ

![Phi-3Model_Github](../../../../imgs/01/02/02/GitHub_ModelPlay.png)

### Phi-3 Models in GitHub Model Catalog

[Phi-3-Medium-128k-Instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-128k-instruct)

[Phi-3-medium-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-4k-instruct)

[Phi-3-mini-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-128k-instruct)

[Phi-3-mini-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-4k-instruct)

[Phi-3-small-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-128k-instruct)

[Phi-3-small-8k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-8k-instruct)

## Getting Started

มีตัวอย่างพื้นฐานพร้อมให้คุณลองใช้งาน คุณสามารถหาได้ในโฟลเดอร์ samples หากคุณต้องการไปยังภาษาที่ชื่นชอบโดยตรง ตัวอย่างโค้ดมีในภาษาดังนี้:

- Python
- JavaScript
- cURL

นอกจากนี้ยังมี Codespaces Environment เฉพาะสำหรับรันตัวอย่างและโมเดล

![Getting Started](../../../../translated_images/GitHub_ModelGetStarted.b4b839a081583da39bc976c2f0d8ac4603d3b8c23194b16cc9e0a1014f5611d0.th.png)

## Sample Code

ด้านล่างเป็นตัวอย่างโค้ดสำหรับกรณีการใช้งานบางส่วน สำหรับข้อมูลเพิ่มเติมเกี่ยวกับ Azure AI Inference SDK โปรดดูเอกสารและตัวอย่างโค้ดทั้งหมด

## Setup

1. สร้าง personal access token  
คุณไม่จำเป็นต้องให้สิทธิ์ใดๆ กับ token นี้ โปรดทราบว่า token จะถูกส่งไปยังบริการของ Microsoft

เพื่อใช้ตัวอย่างโค้ดด้านล่าง สร้าง environment variable เพื่อเก็บ token ของคุณเป็นกุญแจสำหรับโค้ดฝั่งไคลเอนต์

ถ้าคุณใช้ bash:  
```
export GITHUB_TOKEN="<your-github-token-goes-here>"
```  
ถ้าคุณใช้ powershell:  

```
$Env:GITHUB_TOKEN="<your-github-token-goes-here>"
```  

ถ้าคุณใช้ Windows command prompt:  

```
set GITHUB_TOKEN=<your-github-token-goes-here>
```  

## Python Sample

### ติดตั้ง dependencies  
ติดตั้ง Azure AI Inference SDK ด้วย pip (ต้องใช้ Python >=3.8):  

```
pip install azure-ai-inference
```  
### รันตัวอย่างโค้ดพื้นฐาน  

ตัวอย่างนี้แสดงการเรียกใช้งาน chat completion API แบบพื้นฐาน โดยใช้ GitHub AI model inference endpoint และ token ของคุณ การเรียกนี้เป็นแบบ synchronous

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

### รันการสนทนาแบบหลายรอบ  

ตัวอย่างนี้แสดงการสนทนาแบบหลายรอบกับ chat completion API เมื่อใช้โมเดลสำหรับแอปแชท คุณจะต้องจัดการประวัติการสนทนาและส่งข้อความล่าสุดไปยังโมเดล

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

### สตรีมผลลัพธ์  

เพื่อประสบการณ์ผู้ใช้ที่ดีกว่า คุณจะต้องสตรีมการตอบกลับของโมเดลเพื่อให้ token แรกแสดงผลเร็วขึ้นและไม่ต้องรอคำตอบนาน

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

### ติดตั้ง dependencies  

ติดตั้ง Node.js  

คัดลอกบรรทัดข้อความด้านล่างและบันทึกเป็นไฟล์ package.json ในโฟลเดอร์ของคุณ  

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

หมายเหตุ: @azure/core-sse จำเป็นเฉพาะเมื่อคุณสตรีมการตอบกลับของ chat completions  

เปิดเทอร์มินัลในโฟลเดอร์นี้แล้วรันคำสั่ง npm install  

สำหรับแต่ละตัวอย่างโค้ดด้านล่าง ให้คัดลอกเนื้อหาไปยังไฟล์ sample.js แล้วรันด้วยคำสั่ง node sample.js  

### รันตัวอย่างโค้ดพื้นฐาน  

ตัวอย่างนี้แสดงการเรียกใช้งาน chat completion API แบบพื้นฐาน โดยใช้ GitHub AI model inference endpoint และ token ของคุณ การเรียกนี้เป็นแบบ synchronous

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

### รันการสนทนาแบบหลายรอบ  

ตัวอย่างนี้แสดงการสนทนาแบบหลายรอบกับ chat completion API เมื่อใช้โมเดลสำหรับแอปแชท คุณจะต้องจัดการประวัติการสนทนาและส่งข้อความล่าสุดไปยังโมเดล

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

### สตรีมผลลัพธ์  

เพื่อประสบการณ์ผู้ใช้ที่ดีกว่า คุณจะต้องสตรีมการตอบกลับของโมเดลเพื่อให้ token แรกแสดงผลเร็วขึ้นและไม่ต้องรอคำตอบนาน

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

### รันตัวอย่างโค้ดพื้นฐาน  

วางคำสั่งต่อไปนี้ใน shell:  

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
### รันการสนทนาแบบหลายรอบ  

เรียก chat completion API พร้อมส่งประวัติการสนทนา:  

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
### สตรีมผลลัพธ์  

นี่คือตัวอย่างการเรียก endpoint และสตรีมการตอบกลับ  

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

## FREE Usage and Rate limits for GitHub Models

![Model Catalog](../../../../translated_images/GitHub_Model.0c2abb992151c5407046e2b763af51505ff709f04c0950785e0300fdc8c55a0c.th.png)

[rate limits for the playground and free API usage](https://docs.github.com/en/github-models/prototyping-with-ai-models#rate-limits) ถูกออกแบบมาเพื่อช่วยให้คุณทดลองกับโมเดลและสร้างต้นแบบแอป AI ของคุณ สำหรับการใช้งานที่เกินขีดจำกัดเหล่านี้ และเพื่อขยายแอปพลิเคชันของคุณ คุณต้องจัดสรรทรัพยากรจากบัญชี Azure และยืนยันตัวตนจากที่นั่นแทนการใช้ GitHub personal access token ของคุณ คุณไม่ต้องเปลี่ยนแปลงโค้ดอื่นใด ใช้ลิงก์นี้เพื่อเรียนรู้วิธีขยายขีดจำกัดฟรีใน Azure AI  

### Disclosures

โปรดจำไว้ว่าเมื่อคุณโต้ตอบกับโมเดล คุณกำลังทดลองกับ AI ซึ่งอาจเกิดข้อผิดพลาดในเนื้อหาได้  

ฟีเจอร์นี้มีข้อจำกัดหลายอย่าง (รวมถึงคำขอต่อวินาที คำขอต่อวัน โทเค็นต่อคำขอ และคำขอพร้อมกัน) และไม่ได้ออกแบบมาสำหรับการใช้งานในสภาพแวดล้อมจริง  

GitHub Models ใช้ Azure AI Content Safety ซึ่งฟิลเตอร์เหล่านี้ไม่สามารถปิดได้ในประสบการณ์ของ GitHub Models หากคุณเลือกใช้โมเดลผ่านบริการแบบชำระเงิน โปรดตั้งค่าฟิลเตอร์เนื้อหาให้ตรงกับความต้องการของคุณ  

บริการนี้อยู่ภายใต้ข้อกำหนด Pre-release ของ GitHub

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาด้วย AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้ความถูกต้อง แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดขึ้นจากการใช้การแปลนี้