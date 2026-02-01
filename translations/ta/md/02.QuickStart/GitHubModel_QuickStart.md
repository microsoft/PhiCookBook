## GitHub Models - வரையறுக்கப்பட்ட பொது பீட்டா

[GitHub Models](https://github.com/marketplace/models) வரவேற்கிறோம்! Azure AI-ல் ஹோஸ்ட் செய்யப்பட்ட AI மாடல்களை ஆராய்வதற்கு அனைத்தும் தயாராக உள்ளது.

![GitHubModel](../../../../imgs/01/02/02/GitHub_ModelCatalog.png)

GitHub Models-ல் கிடைக்கும் மாடல்களுக்கான கூடுதல் தகவலுக்கு, [GitHub Model Marketplace](https://github.com/marketplace/models) பார்க்கவும்.

## கிடைக்கும் மாடல்கள்

ஒவ்வொரு மாடலுக்கும் தனித்துவமான விளையாட்டு மைதானம் மற்றும் மாதிரிக் குறியீடு உள்ளது.

![Phi-3Model_Github](../../../../imgs/01/02/02/GitHub_ModelPlay.png)

### GitHub Model Catalog-ல் உள்ள Phi-3 மாடல்கள்

[Phi-3-Medium-128k-Instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-128k-instruct)

[Phi-3-medium-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-4k-instruct)

[Phi-3-mini-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-128k-instruct)

[Phi-3-mini-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-4k-instruct)

[Phi-3-small-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-128k-instruct)

[Phi-3-small-8k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-8k-instruct)

## தொடங்குவது எப்படி

இங்கே சில அடிப்படை உதாரணங்கள் உங்களுக்கு இயக்க தயாராக உள்ளன. அவற்றை samples கோப்பகத்தில் காணலாம். உங்கள் விருப்பமான மொழிக்கு நேராக செல்ல விரும்பினால், கீழே உள்ள மொழிகளில் உதாரணங்களை காணலாம்:

- Python
- JavaScript
- cURL

மாதிரிகள் மற்றும் மாடல்களை இயக்குவதற்கான தனித்துவமான Codespaces சூழலும் உள்ளது.

![Getting Started](../../../../imgs/01/02/02/GitHub_ModelGetStarted.png)

## மாதிரிக் குறியீடு

கீழே சில பயன்பாடுகளுக்கான உதாரண குறியீடு உள்ளது. Azure AI Inference SDK பற்றிய கூடுதல் தகவலுக்கு முழு ஆவணங்கள் மற்றும் மாதிரிகளை பார்க்கவும்.

## அமைப்பு

1. தனிப்பட்ட அணுகல் டோக்கனை உருவாக்கவும்  
டோக்கனுக்கு எந்த அனுமதிகளையும் வழங்க தேவையில்லை. Microsoft சேவைக்கு டோக்கன் அனுப்பப்படும் என்பதை கவனிக்கவும்.

கீழே உள்ள குறியீடுகளை பயன்படுத்த, உங்கள் டோக்கனை client code க்கான key ஆக அமைக்க ஒரு சூழல் மாறியை உருவாக்கவும்.

நீங்கள் bash பயன்படுத்தினால்:  
```
export GITHUB_TOKEN="<your-github-token-goes-here>"
```
  
நீங்கள் powershell பயன்படுத்தினால்:  
```
$Env:GITHUB_TOKEN="<your-github-token-goes-here>"
```
  
நீங்கள் Windows command prompt பயன்படுத்தினால்:  
```
set GITHUB_TOKEN=<your-github-token-goes-here>
```
  

## Python மாதிரி

### Dependencies நிறுவவும்  
Azure AI Inference SDK ஐ pip மூலம் நிறுவவும் (தேவை: Python >=3.8):  
```
pip install azure-ai-inference
```
  

### அடிப்படை குறியீடு மாதிரியை இயக்கவும்  
இந்த மாதிரி chat completion API க்கு அடிப்படை அழைப்பை காட்டுகிறது. இது GitHub AI மாடல் inference endpoint மற்றும் உங்கள் GitHub டோக்கனை பயன்படுத்துகிறது. அழைப்பு synchronous ஆகும்.  
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
  

### பல முறை உரையாடலை இயக்கவும்  
இந்த மாதிரி chat completion API உடன் பல முறை உரையாடலை காட்டுகிறது. chat பயன்பாட்டிற்காக மாடலை பயன்படுத்தும்போது, அந்த உரையாடலின் வரலாற்றை நிர்வகிக்கவும் மற்றும் சமீபத்திய செய்திகளை மாடலுக்கு அனுப்பவும்.  
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
  

### வெளியீட்டை ஸ்ட்ரீம் செய்யவும்  
சிறந்த பயனர் அனுபவத்திற்காக, மாடலின் பதிலை ஸ்ட்ரீம் செய்ய விரும்புவீர்கள், இதனால் முதல் டோக்கன் விரைவாக தோன்றும் மற்றும் நீண்ட பதில்களுக்கு காத்திருக்க வேண்டிய அவசியம் இல்லை.  
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

### Dependencies நிறுவவும்  
Node.js ஐ நிறுவவும்.  

கீழே உள்ள வரிகளை copy செய்து உங்கள் கோப்பகத்தில் package.json என்ற பெயரில் சேமிக்கவும்.  
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
  

குறிப்பு: @azure/core-sse என்பது chat completions பதிலை ஸ்ட்ரீம் செய்யும்போது மட்டுமே தேவை.  

இந்த கோப்பகத்தில் ஒரு terminal window திறந்து npm install ஐ இயக்கவும்.  

கீழே உள்ள குறியீடு snippet க்கான ஒவ்வொரு கோப்பையும் sample.js என்ற பெயரில் சேமித்து node sample.js மூலம் இயக்கவும்.  

### அடிப்படை குறியீடு மாதிரியை இயக்கவும்  
இந்த மாதிரி chat completion API க்கு அடிப்படை அழைப்பை காட்டுகிறது. இது GitHub AI மாடல் inference endpoint மற்றும் உங்கள் GitHub டோக்கனை பயன்படுத்துகிறது. அழைப்பு synchronous ஆகும்.  
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
  

### பல முறை உரையாடலை இயக்கவும்  
இந்த மாதிரி chat completion API உடன் பல முறை உரையாடலை காட்டுகிறது. chat பயன்பாட்டிற்காக மாடலை பயன்படுத்தும்போது, அந்த உரையாடலின் வரலாற்றை நிர்வகிக்கவும் மற்றும் சமீபத்திய செய்திகளை மாடலுக்கு அனுப்பவும்.  
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
  

### வெளியீட்டை ஸ்ட்ரீம் செய்யவும்  
சிறந்த பயனர் அனுபவத்திற்காக, மாடலின் பதிலை ஸ்ட்ரீம் செய்ய விரும்புவீர்கள், இதனால் முதல் டோக்கன் விரைவாக தோன்றும் மற்றும் நீண்ட பதில்களுக்கு காத்திருக்க வேண்டிய அவசியம் இல்லை.  
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

### அடிப்படை குறியீடு மாதிரியை இயக்கவும்  
கீழே உள்ளதை shell இல் paste செய்யவும்:  
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
  

### பல முறை உரையாடலை இயக்கவும்  
chat completion API ஐ அழைத்து chat வரலாற்றை அனுப்பவும்:  
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
  

### வெளியீட்டை ஸ்ட்ரீம் செய்யவும்  
endpoint ஐ அழைத்து பதிலை ஸ்ட்ரீம் செய்யும் உதாரணம் இது.  
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
  

## GitHub Models க்கான இலவச பயன்பாடு மற்றும் விகித வரம்புகள்

![Model Catalog](../../../../imgs/01/02/02/GitHub_Model.png)

[playground மற்றும் இலவச API பயன்பாட்டுக்கான விகித வரம்புகள்](https://docs.github.com/en/github-models/prototyping-with-ai-models#rate-limits) உங்கள் மாடல்களை ஆராய்வதற்கும், AI பயன்பாட்டை prototype செய்ய உதவுவதற்கும் உருவாக்கப்பட்டவை. அந்த வரம்புகளை மீறி பயன்பாட்டை அளவுக்கு கொண்டு வர, Azure கணக்கில் resourcel்களை வழங்க வேண்டும், மேலும் GitHub தனிப்பட்ட அணுகல் டோக்கனுக்கு பதிலாக அங்கிருந்து authentication செய்ய வேண்டும். உங்கள் குறியீட்டில் வேறு எதையும் மாற்ற தேவையில்லை. Azure AI இல் இலவச tier வரம்புகளை மீறுவது எப்படி என்பதை அறிய இந்த இணைப்பைப் பயன்படுத்தவும்.

### வெளிப்படுத்தல்கள்

மாடலுடன் தொடர்பு கொள்ளும்போது, நீங்கள் AI உடன் பரிசோதனை செய்கிறீர்கள் என்பதை நினைவில் கொள்ளவும், எனவே உள்ளடக்கத் தவறுகள் ஏற்படலாம்.

இந்த அம்சம் பல வரம்புகளுக்கு உட்பட்டது (உதாரணமாக, requests per minute, requests per day, tokens per request, மற்றும் concurrent requests) மற்றும் உற்பத்தி பயன்பாடுகளுக்கு வடிவமைக்கப்படவில்லை.

GitHub Models Azure AI Content Safety ஐ பயன்படுத்துகிறது. GitHub Models அனுபவத்தின் ஒரு பகுதியாக இந்த வடிகட்டிகளை அணைக்க முடியாது. நீங்கள் கட்டண சேவையின் மூலம் மாடல்களை பயன்படுத்த முடிவு செய்தால், உங்கள் தேவைகளை பூர்த்தி செய்ய உங்கள் உள்ளடக்க வடிகட்டிகளை அமைக்கவும்.

இந்த சேவை GitHub இன் Pre-release Terms கீழ் உள்ளது.

---

**குறிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையைப் பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கின்றோம், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறான தகவல்கள் இருக்கக்கூடும் என்பதை தயவுசெய்து கவனத்தில் கொள்ளவும். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்தவொரு தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.