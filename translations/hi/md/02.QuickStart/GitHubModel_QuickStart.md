<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3f37da1518bfb2cc9a8faa427fb0c916",
  "translation_date": "2025-04-04T18:46:58+00:00",
  "source_file": "md\\02.QuickStart\\GitHubModel_QuickStart.md",
  "language_code": "hi"
}
-->
## GitHub मॉडल्स - सीमित सार्वजनिक बीटा

[GitHub Models](https://github.com/marketplace/models) में आपका स्वागत है! हमने Azure AI पर होस्ट किए गए AI मॉडल्स को एक्सप्लोर करने के लिए सब कुछ तैयार कर दिया है।

![GitHubModel](../../../../translated_images/GitHub_ModelCatalog.4fc858ab26afe64c43f5e423ad0c5c733878bb536fdb027a5bcf1f80c41b0633.hi.png)

GitHub Models पर उपलब्ध मॉडल्स के बारे में अधिक जानकारी के लिए [GitHub Model Marketplace](https://github.com/marketplace/models) देखें।

## उपलब्ध मॉडल्स

प्रत्येक मॉडल के पास एक समर्पित प्लेग्राउंड और सैंपल कोड है।

![Phi-3Model_Github](../../../../imgs/01/02/02/GitHub_ModelPlay.png)

### GitHub मॉडल कैटलॉग में Phi-3 मॉडल्स

[Phi-3-Medium-128k-Instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-128k-instruct)

[Phi-3-medium-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-4k-instruct)

[Phi-3-mini-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-128k-instruct)

[Phi-3-mini-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-4k-instruct)

[Phi-3-small-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-128k-instruct)

[Phi-3-small-8k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-8k-instruct)

## शुरुआत कैसे करें

कुछ बुनियादी उदाहरण तैयार हैं जिन्हें आप चला सकते हैं। आप इन्हें सैंपल्स डायरेक्टरी में पा सकते हैं। यदि आप सीधे अपनी पसंदीदा भाषा पर जाना चाहते हैं, तो आप निम्न भाषाओं में उदाहरण पा सकते हैं:

- Python
- JavaScript
- cURL

सैंपल्स और मॉडल्स चलाने के लिए एक समर्पित Codespaces Environment भी उपलब्ध है।

![Getting Started](../../../../translated_images/GitHub_ModelGetStarted.b4b839a081583da39bc976c2f0d8ac4603d3b8c23194b16cc9e0a1014f5611d0.hi.png)

## सैंपल कोड 

नीचे कुछ उपयोग मामलों के लिए कोड स्निपेट्स के उदाहरण दिए गए हैं। Azure AI Inference SDK के बारे में अतिरिक्त जानकारी के लिए, पूरी डाक्यूमेंटेशन और सैंपल्स देखें।

## सेटअप 

1. एक व्यक्तिगत एक्सेस टोकन बनाएं  
आपको टोकन को किसी भी अनुमति देने की आवश्यकता नहीं है। ध्यान दें कि टोकन Microsoft सेवा को भेजा जाएगा।

नीचे दिए गए कोड स्निपेट्स का उपयोग करने के लिए, अपने टोकन को क्लाइंट कोड की कुंजी के रूप में सेट करने के लिए एक एनवायरनमेंट वेरिएबल बनाएं।

यदि आप bash का उपयोग कर रहे हैं:
```
export GITHUB_TOKEN="<your-github-token-goes-here>"
```  
यदि आप powershell में हैं:

```
$Env:GITHUB_TOKEN="<your-github-token-goes-here>"
```  

यदि आप Windows कमांड प्रॉम्प्ट का उपयोग कर रहे हैं:

```
set GITHUB_TOKEN=<your-github-token-goes-here>
```  

## Python सैंपल

### Dependencies इंस्टॉल करें  
pip का उपयोग करके Azure AI Inference SDK इंस्टॉल करें (आवश्यक: Python >=3.8):

```
pip install azure-ai-inference
```  

### एक बेसिक कोड सैंपल चलाएं  

यह सैंपल chat completion API को कॉल करने का एक बेसिक तरीका दिखाता है। यह GitHub AI मॉडल इनफेरेंस एंडपॉइंट और आपके GitHub टोकन का उपयोग कर रहा है। कॉल सिंक्रोनस है।

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

### मल्टी-टर्न बातचीत चलाएं  

यह सैंपल chat completion API के साथ एक मल्टी-टर्न बातचीत दिखाता है। जब आप मॉडल का उपयोग चैट एप्लिकेशन के लिए करते हैं, तो आपको उस बातचीत का इतिहास प्रबंधित करना होगा और नवीनतम संदेशों को मॉडल को भेजना होगा।

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

### आउटपुट को स्ट्रीम करें  

बेहतर उपयोगकर्ता अनुभव के लिए, आप मॉडल की प्रतिक्रिया को स्ट्रीम करना चाहेंगे ताकि पहला टोकन जल्दी दिखाई दे और लंबे उत्तरों के लिए प्रतीक्षा न करनी पड़े।

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

### Dependencies इंस्टॉल करें  

Node.js इंस्टॉल करें।  

निम्नलिखित टेक्स्ट की पंक्तियों को कॉपी करें और इसे package.json नामक फाइल के रूप में अपनी फोल्डर में सेव करें।

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

नोट: @azure/core-sse केवल तब आवश्यक है जब आप chat completions प्रतिक्रिया को स्ट्रीम करते हैं।  

इस फोल्डर में एक टर्मिनल विंडो खोलें और npm install चलाएं।  

नीचे दिए गए प्रत्येक कोड स्निपेट्स के लिए, सामग्री को sample.js फाइल में कॉपी करें और node sample.js के साथ चलाएं।  

### एक बेसिक कोड सैंपल चलाएं  

यह सैंपल chat completion API को कॉल करने का एक बेसिक तरीका दिखाता है। यह GitHub AI मॉडल इनफेरेंस एंडपॉइंट और आपके GitHub टोकन का उपयोग कर रहा है। कॉल सिंक्रोनस है।  

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

### मल्टी-टर्न बातचीत चलाएं  

यह सैंपल chat completion API के साथ एक मल्टी-टर्न बातचीत दिखाता है। जब आप मॉडल का उपयोग चैट एप्लिकेशन के लिए करते हैं, तो आपको उस बातचीत का इतिहास प्रबंधित करना होगा और नवीनतम संदेशों को मॉडल को भेजना होगा।  

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

### आउटपुट को स्ट्रीम करें  
बेहतर उपयोगकर्ता अनुभव के लिए, आप मॉडल की प्रतिक्रिया को स्ट्रीम करना चाहेंगे ताकि पहला टोकन जल्दी दिखाई दे और लंबे उत्तरों के लिए प्रतीक्षा न करनी पड़े।  

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

### एक बेसिक कोड सैंपल चलाएं  

निम्नलिखित को शेल में पेस्ट करें:  

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

### मल्टी-टर्न बातचीत चलाएं  

Chat completion API को कॉल करें और चैट इतिहास पास करें:  

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

### आउटपुट को स्ट्रीम करें  

यह एंडपॉइंट को कॉल करने और प्रतिक्रिया को स्ट्रीम करने का एक उदाहरण है।  

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

## GitHub मॉडल्स के लिए मुफ्त उपयोग और दर सीमाएं  

![Model Catalog](../../../../translated_images/GitHub_Model.0c2abb992151c5407046e2b763af51505ff709f04c0950785e0300fdc8c55a0c.hi.png)

[प्लेग्राउंड और मुफ्त API उपयोग के लिए दर सीमाएं](https://docs.github.com/en/github-models/prototyping-with-ai-models#rate-limits) आपको मॉडल्स के साथ प्रयोग करने और अपने AI एप्लिकेशन का प्रोटोटाइप बनाने में मदद करने के लिए डिज़ाइन की गई हैं। इन सीमाओं से आगे उपयोग के लिए, और अपने एप्लिकेशन को स्केल पर लाने के लिए, आपको Azure खाते से संसाधन प्रदान करने होंगे और वहां से प्रमाणित करना होगा, बजाय अपने GitHub व्यक्तिगत एक्सेस टोकन के। आपके कोड में कुछ भी बदलने की आवश्यकता नहीं है। Azure AI में मुफ्त टियर सीमाओं से आगे जाने का तरीका जानने के लिए इस लिंक का उपयोग करें।

### डिस्क्लोज़र  

याद रखें कि मॉडल के साथ बातचीत करते समय आप AI के साथ प्रयोग कर रहे हैं, इसलिए सामग्री में गलतियाँ संभव हैं।  

यह सुविधा विभिन्न सीमाओं (जैसे प्रति मिनट अनुरोध, प्रति दिन अनुरोध, प्रति अनुरोध टोकन, और समवर्ती अनुरोध) के अधीन है और उत्पादन उपयोग मामलों के लिए डिज़ाइन नहीं की गई है।  

GitHub मॉडल्स Azure AI Content Safety का उपयोग करता है। GitHub Models अनुभव के हिस्से के रूप में इन फ़िल्टरों को बंद नहीं किया जा सकता। यदि आप भुगतान सेवा के माध्यम से मॉडल का उपयोग करने का निर्णय लेते हैं, तो कृपया अपनी आवश्यकताओं को पूरा करने के लिए अपने सामग्री फ़िल्टर कॉन्फ़िगर करें।  

यह सेवा GitHub की प्री-रिलीज़ शर्तों के तहत है।  

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल भाषा में लिखा गया दस्तावेज़ ही आधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।