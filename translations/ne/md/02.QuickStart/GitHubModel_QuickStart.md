<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5113634b77370af6790f9697d5d7de90",
  "translation_date": "2025-07-17T05:34:31+00:00",
  "source_file": "md/02.QuickStart/GitHubModel_QuickStart.md",
  "language_code": "ne"
}
-->
## GitHub मोडेलहरू - सीमित सार्वजनिक बीटा

[GitHub Models](https://github.com/marketplace/models) मा स्वागत छ! हामीले Azure AI मा होस्ट गरिएका AI मोडेलहरू अन्वेषण गर्न तपाईंका लागि सबै तयारी गरिसकेका छौं।

![GitHubModel](../../../../translated_images/GitHub_ModelCatalog.aa43c51c36454747.ne.png)

GitHub Models मा उपलब्ध मोडेलहरूको थप जानकारीका लागि, [GitHub Model Marketplace](https://github.com/marketplace/models) हेर्नुहोस्।

## उपलब्ध मोडेलहरू

प्रत्येक मोडेलसँग समर्पित प्लेग्राउन्ड र नमूना कोड उपलब्ध छ।

![Phi-3Model_Github](../../../../imgs/01/02/02/GitHub_ModelPlay.png)

### GitHub Model Catalog मा Phi-3 मोडेलहरू

[Phi-3-Medium-128k-Instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-128k-instruct)

[Phi-3-medium-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-4k-instruct)

[Phi-3-mini-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-128k-instruct)

[Phi-3-mini-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-4k-instruct)

[Phi-3-small-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-128k-instruct)

[Phi-3-small-8k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-8k-instruct)

## सुरु गर्ने तरिका

तपाईंले चलाउन सक्ने केही आधारभूत उदाहरणहरू तयार छन्। ती तपाईं samples डाइरेक्टरीमा फेला पार्न सक्नुहुन्छ। यदि तपाईं आफ्नो मनपर्ने भाषामा सिधै जान चाहनुहुन्छ भने, निम्न भाषाहरूमा उदाहरणहरू उपलब्ध छन्:

- Python
- JavaScript
- cURL

नमूना र मोडेलहरू चलाउनको लागि समर्पित Codespaces Environment पनि उपलब्ध छ।

![Getting Started](../../../../translated_images/GitHub_ModelGetStarted.150220a802da6fb6.ne.png)

## नमूना कोड

तल केही प्रयोगका लागि उदाहरण कोड स्निपेटहरू छन्। Azure AI Inference SDK को थप जानकारीका लागि पूर्ण कागजात र नमूनाहरू हेर्नुहोस्।

## सेटअप

1. व्यक्तिगत पहुँच टोकन बनाउनुहोस्  
टोकनलाई कुनै अनुमति दिन आवश्यक छैन। ध्यान दिनुहोस् कि टोकन Microsoft सेवामा पठाइनेछ।

तलका कोड स्निपेटहरू प्रयोग गर्न, आफ्नो टोकनलाई क्लाइन्ट कोडको लागि कुञ्जीको रूपमा सेट गर्न वातावरण चर बनाउनुहोस्।

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

## Python नमूना

### निर्भरता स्थापना गर्नुहोस्  
pip मार्फत Azure AI Inference SDK स्थापना गर्नुहोस् (आवश्यक: Python >=3.8):

```
pip install azure-ai-inference
```  
### आधारभूत कोड नमूना चलाउनुहोस्

यो नमूनाले chat completion API को आधारभूत कल देखाउँछ। यसले GitHub AI मोडेल inference endpoint र तपाईंको GitHub टोकन प्रयोग गरिरहेको छ। कल synchronous छ।

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

### बहु-चरण संवाद चलाउनुहोस्

यो नमूनाले chat completion API सँग बहु-चरण संवाद देखाउँछ। च्याट एप्लिकेसनमा मोडेल प्रयोग गर्दा, तपाईंले संवादको इतिहास व्यवस्थापन गर्नुपर्नेछ र मोडेललाई पछिल्लो सन्देशहरू पठाउनुपर्नेछ।

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

उपयोगकर्ताको अनुभव सुधार गर्न, तपाईंले मोडेलको प्रतिक्रिया स्ट्रिम गर्न चाहनुहुनेछ ताकि पहिलो टोकन छिटो देखियोस् र लामो प्रतिक्रियाको लागि पर्खन नपरोस्।

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

तलका लाइनहरू कपी गरेर आफ्नो फोल्डरमा package.json नामक फाइलमा सुरक्षित गर्नुहोस्।

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

सूचना: @azure/core-sse केवल तब आवश्यक हुन्छ जब तपाईं च्याट कम्प्लिशनको प्रतिक्रिया स्ट्रिम गर्नुहुन्छ।

यस फोल्डरमा टर्मिनल खोल्नुहोस् र npm install चलाउनुहोस्।

तलका प्रत्येक कोड स्निपेटलाई sample.js फाइलमा कपी गरी node sample.js चलाउनुहोस्।

### आधारभूत कोड नमूना चलाउनुहोस्

यो नमूनाले chat completion API को आधारभूत कल देखाउँछ। यसले GitHub AI मोडेल inference endpoint र तपाईंको GitHub टोकन प्रयोग गरिरहेको छ। कल synchronous छ।

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

### बहु-चरण संवाद चलाउनुहोस्

यो नमूनाले chat completion API सँग बहु-चरण संवाद देखाउँछ। च्याट एप्लिकेसनमा मोडेल प्रयोग गर्दा, तपाईंले संवादको इतिहास व्यवस्थापन गर्नुपर्नेछ र मोडेललाई पछिल्लो सन्देशहरू पठाउनुपर्नेछ।

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

उपयोगकर्ताको अनुभव सुधार गर्न, तपाईंले मोडेलको प्रतिक्रिया स्ट्रिम गर्न चाहनुहुनेछ ताकि पहिलो टोकन छिटो देखियोस् र लामो प्रतिक्रियाको लागि पर्खन नपरोस्।

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

### आधारभूत कोड नमूना चलाउनुहोस्

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
### बहु-चरण संवाद चलाउनुहोस्

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

## GitHub मोडेलहरूको निःशुल्क प्रयोग र दर सीमाहरू

![Model Catalog](../../../../translated_images/GitHub_Model.ca6c125cb3117d0e.ne.png)

[प्लेग्राउन्ड र निःशुल्क API प्रयोगका लागि दर सीमाहरू](https://docs.github.com/en/github-models/prototyping-with-ai-models#rate-limits) तपाईंलाई मोडेलहरू परीक्षण गर्न र AI एप्लिकेसन प्रोटोटाइप बनाउन मद्दत गर्न बनाइएको हो। ती सीमाहरू भन्दा बढी प्रयोगका लागि, र तपाईंको एप्लिकेसनलाई स्केलमा ल्याउन, तपाईंले Azure खाताबाट स्रोतहरू प्रावधान गर्नुपर्नेछ र त्यहाँबाट प्रमाणिकरण गर्नुपर्नेछ, तपाईंको GitHub व्यक्तिगत पहुँच टोकनको सट्टा। तपाईंले आफ्नो कोडमा अरू केही परिवर्तन गर्न आवश्यक छैन। Azure AI मा निःशुल्क स्तर सीमाहरू पार गर्ने तरिका जान्न यो लिंक प्रयोग गर्नुहोस्।

### खुलासा

मोडेलसँग अन्तरक्रिया गर्दा तपाईं AI सँग प्रयोग गर्दै हुनुहुन्छ भन्ने सम्झनुहोस्, त्यसैले सामग्रीमा त्रुटिहरू हुन सक्छन्।

यो सुविधा विभिन्न सीमाहरू (जस्तै प्रति मिनेट अनुरोध, प्रति दिन अनुरोध, प्रति अनुरोध टोकन, र समवर्ती अनुरोधहरू) अन्तर्गत छ र उत्पादन प्रयोगका लागि डिजाइन गरिएको छैन।

GitHub Models ले Azure AI Content Safety प्रयोग गर्दछ। यी फिल्टरहरू GitHub Models अनुभवको भागको रूपमा बन्द गर्न सकिँदैन। यदि तपाईंले तिर्ने सेवाबाट मोडेलहरू प्रयोग गर्ने निर्णय गर्नुभयो भने, कृपया आफ्नो सामग्री फिल्टरहरू तपाईंको आवश्यकताअनुसार कन्फिगर गर्नुहोस्।

यो सेवा GitHub को प्रि-रिलिज सर्तहरू अन्तर्गत छ।

**अस्वीकरण**:  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताका लागि प्रयासरत छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुन सक्छ। मूल दस्तावेज यसको मूल भाषामा नै अधिकारिक स्रोत मानिनु पर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार छैनौं।