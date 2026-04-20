## ម៉ូដែល GitHub - បេតា​សាធារណៈ​មាន​កំណត់

សូមស្វាគμώνទៅកាន់ [ម៉ូដែល GitHub](https://github.com/marketplace/models)! យើងបានត្រៀមអ្វីគ្រប់យ៉ាងរួចរាល់សម្រាប់អ្នកស្វែងរក ម៉ូដែល AI ដែលមានម៉ាស៊ីនផ្ទុកនៅ Azure AI។

![GitHubModel](../../../../translated_images/km/GitHub_ModelCatalog.aa43c51c36454747.webp)

សម្រាប់ព័ត៌មានបន្ថែមអំពីម៉ូដែលដែលអាចប្រើបាននៅលើម៉ូដែល GitHub សូមពិនិត្យទស្សនាទំព័រ [GitHub Model Marketplace](https://github.com/marketplace/models)

## ម៉ូដែលដែលអាចប្រើបាន

ម៉ូដែលនីមួយៗមានទីលានលេង និងកូដឧទាហរណ៍ផ្តាច់មុខ

![Phi-3Model_Github](../../../../imgs/01/02/02/GitHub_ModelPlay.png)

### ម៉ូដែល Phi-3 ក្នុងសៀវភៅម៉ូដែល GitHub

[Phi-3-Medium-128k-Instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-128k-instruct)

[Phi-3-medium-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-4k-instruct)

[Phi-3-mini-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-128k-instruct)

[Phi-3-mini-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-4k-instruct)

[Phi-3-small-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-128k-instruct)

[Phi-3-small-8k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-8k-instruct)

## ចាប់ផ្តើម

មានឧទាហរណ៍មូលដ្ឋានខ្លះៗរួចរាល់សម្រាប់អ្នកដំណើរការ។ អ្នកអាចស្វែងរកពួកវានៅក្នុងថតឧទាហរណ៍។ ប្រសិនបើអ្នកចង់ឆ្លងទៅភាសាបានចំណូលចិត្តរបស់អ្នកដោយផ្ទាល់ អ្នកអាចរកឃើញឧទាហរណ៍នៅក្នុងភាសាខាងក្រោមៈ

- Python
- JavaScript
- cURL

មានបរិស្ថាន Codespaces ផ្តាច់មុខសម្រាប់ដំណើរការឯកសារឧទាហរណ៍ និងម៉ូដែលផងដែរ។

![Getting Started](../../../../translated_images/km/GitHub_ModelGetStarted.150220a802da6fb6.webp)


## កូដឧទាហរណ៍

ខាងក្រោមនេះជាឧទាហរណ៍កូដសម្រាប់ករណីប្រើប្រាស់ខ្លះៗ។ សម្រាប់ព័ត៌មានបន្ថែមអំពី Azure AI Inference SDK សូមមើលឯកសារពេញ និងឧទាហរណ៍។

## ការកំណត់ត្រា

1. បង្កើតកូដសម្ងាត់ផ្ទាល់ខ្លួន
អ្នកមិនត្រូវការផ្ដល់សិទ្ធិឲ្យកូដសម្ងាត់ទេ។ សូមចំណាំថាកូដសម្ងាត់នឹងត្រូវផ្ញើទៅសេវាកម្មរបស់ Microsoft។

ដើម្បីប្រើកូដឧទាហរណ៍ខាងក្រោម សូមបង្កើតអថេរ​បរិស្ថានសម្រាប់កំណត់កូដសម្ងាត់របស់អ្នកជា key សម្រាប់កូដ client។

បើលោកអ្នកប្រើប្រាស់ bash៖
```
export GITHUB_TOKEN="<your-github-token-goes-here>"
```
បើលោកអ្នកនៅក្នុង powershell៖

```
$Env:GITHUB_TOKEN="<your-github-token-goes-here>"
```

បើលោកអ្នកប្រើប្រាស់ Windows command prompt៖

```
set GITHUB_TOKEN=<your-github-token-goes-here>
```

## ឧទាហរណ៍ Python

### ដំឡើងអាស្រ័យភាព
ដំឡើង Azure AI Inference SDK ជាមួយ pip (តម្រូវការ: Python >=3.8):

```
pip install azure-ai-inference
```
### ប្រតិបត្ដិការ​កូដ​មូលដ្ឋាន

ឧទាហរណ៍នេះបង្ហាញពីការហៅមូលដ្ឋានទៅ API chat completion។ វាអំពាវនាវការបញ្ចេញម៉ូដែល AI GitHub និងកូដសម្ងាត់ GitHub របស់អ្នក។ ការហៅនេះគឺសមទេស synchronous ។

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

### ប្រតិបត្ដិការ​សន្ទនា​ច្រើនជំហាន

ឧទាហរណ៍នេះបង្ហាញពីការសន្ទនាច្រើនជំហានជាមួយ API chat completion។ នៅពេលប្រើម៉ូដែលសម្រាប់កម្មវិធីផ្ទាល់ខ្លួន អ្នកត្រូវគ្រប់គ្រងប្រវត្តិសន្ទនានិងផ្ញើសារ​ចុងក្រោយទៅម៉ូដែល។

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

### បញ្ចេញផលប៉ះពាល់ដោយ streaming

សម្រាប់បទពិសោធន៍ប្រើប្រាស់ល្អប្រសើរ អ្នកនឹងចង់បញ្ចេញតបនៃម៉ូដែលដោយ streams ដើម្បីឲ្យ token ដំបូងបង្ហាញបានដើមហើយទៀងទាត់ពីការរង់ចាំនូវការឆ្លើយតបយូរ។

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

### ដំឡើងអាស្រ័យភាព

ដំឡើង Node.js។

ចម្លងខ្សែអក្សរខាងក្រោម ហើយរក្សាទុកជា package.json នៅក្នុងថតរបស់អ្នក។

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

ចំណាំ៖ @azure/core-sse ត្រូវបានប្រើតែពេល streaming chat completions response ឯងគត់។

បើកវីនដូ terminal នៅក្នុងថតនេះ ហើយរត់ npm install។

សម្រាប់កូដឧទាហរណ៍មួយៗខាងក្រោម ចម្លងមាតិកាទៅឯកសារ sample.js ហើយរត់ node sample.js។

### ប្រតិបត្ដិការ​កូដ​មូលដ្ឋាន

ឧទាហរណ៍នេះបង្ហាញការហៅមូលដ្ឋានពី API chat completion។ វាអំពាវនាវម៉ូដែល AI GitHub និងកូដសម្ងាត់ GitHub របស់អ្នក។ ការហៅនេះគឺសមទេស synchronous ។

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

### ប្រតិបត្ដិការ​សន្ទនា​ច្រើនជំហាន

ឧទាហរណ៍នេះបង្ហាញការសន្ទនាច្រើនជំហានជាមួយ API chat completion។ នៅពេលប្រើម៉ូដែលសម្រាប់កម្មវិធីផ្ទាល់ខ្លួន អ្នកត្រូវគ្រប់គ្រងប្រវត្តិសន្ទនានិងផ្ញើសារ​ចុងក្រោយទៅម៉ូដែល។

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

### បញ្ចេញផលប៉ះពាល់ដោយ streaming
សម្រាប់បទពិសោធន៍ប្រើប្រាស់ល្អ ប្រើ შესრულប្រាកដថាអ្នកចង់បញ្ចេញតបដោយ streaming ដើម្បីឲ្យ token ដំបូងបង្ហាញរហ័ស និងជៀសវាងការរង់ចាំច្រើន។

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

### ប្រតិបត្ដិការ​កូដ​មូលដ្ឋាន

បិទភ្ជាប់ខាងក្រោមទៅ shell:

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
### ប្រតិបត្ដិការ​សន្ទនា​ច្រើនជំហាន

ហៅ API chat completion ហើយផ្ញើប្រវត្តិសន្ទនា:

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
### បញ្ចេញផលប៉ះពាល់ដោយ streaming

នេះគឺជាឧទាហរណ៍នៃការហៅ endpoint ហើយ streaming តបវិញ។

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

## ការប្រើប្រាស់ឥតគិតថ្លៃ និងដែនកំណត់អត្រាសម្រាប់ម៉ូដែល GitHub

![Model Catalog](../../../../translated_images/km/GitHub_Model.ca6c125cb3117d0e.webp)

[ដែនកំណត់អត្រាសម្រាប់ទីលានលេង និងការប្រើប្រាស់ API ឥតគិតថ្លៃ](https://docs.github.com/en/github-models/prototyping-with-ai-models#rate-limits) មានគោលបំណងជួយឲ្យអ្នកសាកល្បងម៉ូเดែល និងរៀបចំកម្មវិធី AI របស់អ្នក។ ដើម្បីប្រើប្រាស់លើសដែនកំណត់ទាំងនោះ ហើយដើម្បីពង្រីកកម្មវិធី​របស់អ្នក អ្នកត្រូវចុះបញ្ជីធនធានពីគណនី Azure រួច Authenticate ចេញពីគណនីនោះ ជំនួស token ផ្ទាល់ខ្លួន GitHub របស់អ្នក។ អ្នកមិនចាំបាច់ផ្លាស់ប្ដូរអ្វីក្រៅពីនេះនៅក្នុងកូដរបស់អ្នកទេ។ ប្រើតំណនេះដើម្បីស្វែងរកវិធីខ្ពស់ជាងដែនកំណត់ជាសេវាឥតគិតថ្លៃនៅ Azure AI។

### ការបង្ហាញ

សូមចងចាំពេលមានអារម្មណ៍ទាក់ទងទៅម៉ូដែល អ្នកកំពុងសាកល្បង AI ដោយហេតុនេះកំហុសមាតិកាអាចកើតឡើង។

មុខងារនេះមានដែនកំណត់ជាច្រើន (រួមទាំងសំណើរ​តាម​នាទី, សំណើរ​តាម​ថ្ងៃ, token ក្នុងសំណើ ក៏ដូចជាសំណើរដូចគ្នា) ហើយមិនដែលត្រូវបានរៀបចំសម្រាប់ករណីប្រើប្រាស់ផលិតកម្ម។

ម៉ូដែល GitHub ប្រើ Azure AI Content Safety។ ហ្វ៊ីលធ័រទាំងនេះមិនអាចបិទបានក្នុងបទពិសោធន៍ម៉ូដែល GitHub។ បើ​អ្នកសម្រេច​ចិត្តប្រើម៉ូដែលតាមរយៈសេវាចំណាយថ្លៃ សូមកំណត់ហ្វ៊ីលធ័រមាតិកាឱ្យផ្គូរផ្គង់តាមតម្រូវការរបស់អ្នក។

សេវាកម្មនេះនៅក្រោមលក្ខខ័ណ្ឌលម្អិតមុនចេញផ្សាយរបស់ GitHub។

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**៖  
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាកម្មបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ក្នុងខណៈដែលយើងខិតខំរកភាពត្រឹមត្រូវ សូមយកចិត្តទុកដាក់ថា ការបកប្រែដោយស្វ័យប្រវត្តិអាចមានកំហុស ឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមជាភាសាដើមគួរត្រូវបានគិតថាជាភស្តុតាងសំខាន់។ សម្រាប់ព័ត៌មានសំខាន់ៗ គួរតែប្រើការបកប្រែដោយអ្នកជំនាញមនុស្ស។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសប្រសិនបើប្រើប្រាស់ការបកប្រែនេះឡើយ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->