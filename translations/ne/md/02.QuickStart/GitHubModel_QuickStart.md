<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5113634b77370af6790f9697d5d7de90",
  "translation_date": "2025-05-09T20:16:24+00:00",
  "source_file": "md/02.QuickStart/GitHubModel_QuickStart.md",
  "language_code": "ne"
}
-->
## GitHub मोडेलहरू - सीमित सार्वजनिक बीटा

[GitHub Models](https://github.com/marketplace/models) मा स्वागत छ! हामीले Azure AI मा होस्ट गरिएको AI मोडेलहरू अन्वेषण गर्न तपाईंका लागि सबै कुरा तयार पारेका छौं।

![GitHubModel](../../../../translated_images/GitHub_ModelCatalog.4fc858ab26afe64c43f5e423ad0c5c733878bb536fdb027a5bcf1f80c41b0633.ne.png)

GitHub Models मा उपलब्ध मोडेलहरूको बारेमा थप जानकारीको लागि, [GitHub Model Marketplace](https://github.com/marketplace/models) हेर्नुहोस्।

## उपलब्ध मोडेलहरू

हरेक मोडेलसँग समर्पित playground र नमुना कोड छ।

![Phi-3Model_Github](../../../../imgs/01/02/02/GitHub_ModelPlay.png)

### GitHub Model Catalog मा Phi-3 मोडेलहरू

[Phi-3-Medium-128k-Instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-128k-instruct)

[Phi-3-medium-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-4k-instruct)

[Phi-3-mini-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-128k-instruct)

[Phi-3-mini-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-4k-instruct)

[Phi-3-small-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-128k-instruct)

[Phi-3-small-8k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-8k-instruct)

## सुरु गर्ने तरिका

केही आधारभूत उदाहरणहरू तयार छन् जुन तपाईं चलाउन सक्नुहुन्छ। तपाईंले तिनीहरूलाई samples डिरेक्टरीमा फेला पार्न सक्नुहुन्छ। आफ्नो मनपर्ने भाषामा सिधै जान चाहनुहुन्छ भने, निम्न भाषाहरूमा उदाहरणहरू उपलब्ध छन्:

- Python
- JavaScript
- cURL

त्यसैगरी, नमुना र मोडेलहरू चलाउनको लागि समर्पित Codespaces Environment पनि छ।

![Getting Started](../../../../translated_images/GitHub_ModelGetStarted.b4b839a081583da39bc976c2f0d8ac4603d3b8c23194b16cc9e0a1014f5611d0.ne.png)

## नमुना कोड

तल केही प्रयोगका लागि उदाहरण कोड स्निपेटहरू छन्। Azure AI Inference SDK सम्बन्धी थप जानकारीका लागि पूर्ण दस्तावेज र नमुनाहरू हेर्नुहोस्।

## सेटअप

1. व्यक्तिगत पहुँच टोकन बनाउनुहोस्  
टोकनलाई कुनै अनुमति दिन आवश्यक छैन। ध्यान दिनुहोस् कि टोकन Microsoft सेवामा पठाइनेछ।

तलका कोड स्निपेटहरू प्रयोग गर्न, आफ्नो टोकनलाई client कोडको लागि कुञ्जीको रूपमा सेट गर्न environment variable बनाउनुहोस्।

यदि तपाईं bash प्रयोग गर्दै हुनुहुन्छ:  
```
export GITHUB_TOKEN="<your-github-token-goes-here>"
```  
यदि तपाईं powershell मा हुनुहुन्छ:  

```
$Env:GITHUB_TOKEN="<your-github-token-goes-here>"
```  

यदि तपाईं Windows command prompt मा हुनुहुन्छ:  

```
set GITHUB_TOKEN=<your-github-token-goes-here>
```  

## Python नमुना

### निर्भरता स्थापना गर्नुहोस्  
pip मार्फत Azure AI Inference SDK स्थापना गर्नुहोस् (आवश्यक: Python >=3.8):  

```
pip install azure-ai-inference
```  

### आधारभूत कोड नमुना चलाउनुहोस्  

यो नमुनाले chat completion API लाई आधारभूत रूपमा कसरी कल गर्ने देखाउँछ। यसले GitHub AI मोडेल inference endpoint र तपाईंको GitHub टोकन प्रयोग गर्दछ। कल synchronous छ।  

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

### बहु-पटक संवाद चलाउनुहोस्  

यो नमुनाले chat completion API सँग बहु-पटक संवाद कसरी गर्ने देखाउँछ। च्याट एप्लिकेसनमा मोडेल प्रयोग गर्दा, तपाईंले संवादको इतिहास व्यवस्थापन गर्नुपर्नेछ र मोडेललाई पछिल्लो सन्देशहरू पठाउनु पर्ने हुन्छ।  

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

### आउटपुट स्ट्रिम गर्नुहोस्  

राम्रो प्रयोगकर्ता अनुभवका लागि, मोडेलको प्रतिक्रिया स्ट्रिम गर्नुहोस् ताकि पहिलो टोकन छिटो देखियोस् र लामो प्रतिक्रिया कुर्न नपरोस्।  

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

### निर्भरता स्थापना गर्नुहोस्  

Node.js स्थापना गर्नुहोस्।  

तलका लाइनहरू कपी गरेर आफ्नो फोल्डर भित्र package.json नामक फाइलमा सुरक्षित गर्नुहोस्।  

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

सूचना: @azure/core-sse केवल तब आवश्यक हुन्छ जब तपाईं chat completions को प्रतिक्रिया स्ट्रिम गर्नुहुन्छ।  

यस फोल्डरमा टर्मिनल खोल्नुहोस् र npm install चलाउनुहोस्।  

तलका कोड स्निपेटहरूका लागि, सामग्रीलाई sample.js फाइलमा कपी गरी node sample.js मार्फत चलाउनुहोस्।  

### आधारभूत कोड नमुना चलाउनुहोस्  

यो नमुनाले chat completion API लाई आधारभूत रूपमा कसरी कल गर्ने देखाउँछ। यसले GitHub AI मोडेल inference endpoint र तपाईंको GitHub टोकन प्रयोग गर्दछ। कल synchronous छ।  

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

### बहु-पटक संवाद चलाउनुहोस्  

यो नमुनाले chat completion API सँग बहु-पटक संवाद कसरी गर्ने देखाउँछ। च्याट एप्लिकेसनमा मोडेल प्रयोग गर्दा, तपाईंले संवादको इतिहास व्यवस्थापन गर्नुपर्नेछ र मोडेललाई पछिल्लो सन्देशहरू पठाउनु पर्ने हुन्छ।  

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

### आउटपुट स्ट्रिम गर्नुहोस्  

राम्रो प्रयोगकर्ता अनुभवका लागि, मोडेलको प्रतिक्रिया स्ट्रिम गर्नुहोस् ताकि पहिलो टोकन छिटो देखियोस् र लामो प्रतिक्रिया कुर्न नपरोस्।  

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

### आधारभूत कोड नमुना चलाउनुहोस्  

तलको सामग्री shell मा पेस्ट गर्नुहोस्:  

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

### बहु-पटक संवाद चलाउनुहोस्  

chat completion API कल गर्नुहोस् र च्याट इतिहास पठाउनुहोस्:  

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

### आउटपुट स्ट्रिम गर्नुहोस्  

यो endpoint कल गरेर प्रतिक्रिया स्ट्रिम गर्ने उदाहरण हो।  

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

## GitHub मोडेलहरूको लागि निःशुल्क प्रयोग र दर सीमा

![Model Catalog](../../../../translated_images/GitHub_Model.0c2abb992151c5407046e2b763af51505ff709f04c0950785e0300fdc8c55a0c.ne.png)

[playground र निःशुल्क API प्रयोगका लागि दर सीमा](https://docs.github.com/en/github-models/prototyping-with-ai-models#rate-limits) तपाईंलाई मोडेलहरू प्रयोग गरेर परीक्षण गर्न र AI एप्लिकेसन प्रोटोटाइप बनाउन सहयोग पुर्‍याउन बनाइएका हुन्। ती सीमाभन्दा बाहिर प्रयोग गर्न र तपाईंको एप्लिकेसनलाई स्केल गर्न, Azure खाताबाट स्रोतहरू प्रावधान गर्नुहोस् र त्यहाँबाट प्रमाणिकरण गर्नुहोस्, तपाईंको GitHub व्यक्तिगत पहुँच टोकनको सट्टा। तपाईंले आफ्नो कोडमा अरू केही परिवर्तन गर्नु पर्दैन। Azure AI मा निःशुल्क स्तर सीमाभन्दा बाहिर कसरी जान सकिन्छ भनेर जान्न यो लिंक प्रयोग गर्नुहोस्।  

### खुलासा

मोडेलसँग अन्तरक्रिया गर्दा तपाईं AI सँग प्रयोग गर्दै हुनुहुन्छ भन्ने सम्झनुहोस्, त्यसैले सामग्रीमा त्रुटि हुन सक्ने सम्भावना छ।  

यो सुविधा विभिन्न सीमाहरू (जस्तै प्रति मिनेट अनुरोध, प्रति दिन अनुरोध, प्रति अनुरोध टोकन, र समकालीन अनुरोधहरू) अन्तर्गत छ र उत्पादन उपयोगका लागि डिजाइन गरिएको छैन।  

GitHub Models ले Azure AI Content Safety प्रयोग गर्दछ। यी फिल्टरहरू GitHub Models अनुभवको हिस्सा रूपमा बन्द गर्न सकिँदैन। यदि तपाईंले भुक्तानी सेवा मार्फत मोडेलहरू प्रयोग गर्ने निर्णय गर्नुभयो भने, कृपया आफ्नो सामग्री फिल्टरहरू तपाईंका आवश्यकताहरू अनुरूप कन्फिगर गर्नुहोस्।  

यो सेवा GitHub को प्रि-रिलिज सर्तहरू अन्तर्गत छ।

**अस्वीकरण**:  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) को प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताका लागि प्रयासरत छौं, तर कृपया जान्नुहोस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धता हुन सक्छ। मूल दस्तावेजलाई यसको स्वदेशी भाषामा आधिकारिक स्रोत मानिनु पर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार छैनौं।