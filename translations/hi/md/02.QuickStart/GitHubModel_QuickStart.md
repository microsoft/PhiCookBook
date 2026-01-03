<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5113634b77370af6790f9697d5d7de90",
  "translation_date": "2025-07-17T05:33:31+00:00",
  "source_file": "md/02.QuickStart/GitHubModel_QuickStart.md",
  "language_code": "hi"
}
-->
## GitHub मॉडल्स - सीमित सार्वजनिक बीटा

[GitHub मॉडल्स](https://github.com/marketplace/models) में आपका स्वागत है! हमने Azure AI पर होस्ट किए गए AI मॉडल्स को एक्सप्लोर करने के लिए सब कुछ तैयार कर दिया है।

![GitHubModel](../../../../translated_images/GitHub_ModelCatalog.aa43c51c36454747.hi.png)

GitHub मॉडल्स पर उपलब्ध मॉडल्स के बारे में अधिक जानकारी के लिए, [GitHub मॉडल मार्केटप्लेस](https://github.com/marketplace/models) देखें।

## उपलब्ध मॉडल्स

प्रत्येक मॉडल के लिए एक समर्पित प्लेग्राउंड और नमूना कोड उपलब्ध है।

![Phi-3Model_Github](../../../../imgs/01/02/02/GitHub_ModelPlay.png)

### GitHub मॉडल कैटलॉग में Phi-3 मॉडल्स

[Phi-3-Medium-128k-Instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-128k-instruct)

[Phi-3-medium-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-4k-instruct)

[Phi-3-mini-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-128k-instruct)

[Phi-3-mini-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-4k-instruct)

[Phi-3-small-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-128k-instruct)

[Phi-3-small-8k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-8k-instruct)

## शुरुआत कैसे करें

कुछ बुनियादी उदाहरण आपके लिए चलाने के लिए तैयार हैं। आप इन्हें samples डायरेक्टरी में पा सकते हैं। यदि आप सीधे अपनी पसंदीदा भाषा में जाना चाहते हैं, तो निम्न भाषाओं में उदाहरण उपलब्ध हैं:

- Python
- JavaScript
- cURL

साथ ही, नमूने और मॉडल्स चलाने के लिए एक समर्पित Codespaces Environment भी उपलब्ध है।

![Getting Started](../../../../translated_images/GitHub_ModelGetStarted.150220a802da6fb6.hi.png)

## नमूना कोड

नीचे कुछ उपयोग मामलों के लिए उदाहरण कोड स्निपेट्स दिए गए हैं। Azure AI Inference SDK के बारे में अधिक जानकारी के लिए, पूर्ण दस्तावेज़ और नमूने देखें।

## सेटअप

1. एक personal access token बनाएं  
टोकन को किसी भी अनुमति देने की आवश्यकता नहीं है। ध्यान दें कि यह टोकन Microsoft सेवा को भेजा जाएगा।

नीचे दिए गए कोड स्निपेट्स का उपयोग करने के लिए, अपने टोकन को क्लाइंट कोड के लिए कुंजी के रूप में सेट करने के लिए एक environment variable बनाएं।

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

## Python नमूना

### निर्भरताएँ इंस्टॉल करें  
pip के माध्यम से Azure AI Inference SDK इंस्टॉल करें (आवश्यक: Python >=3.8):  

```
pip install azure-ai-inference
```  
### एक बुनियादी कोड नमूना चलाएं

यह नमूना chat completion API को बेसिक कॉल दिखाता है। यह GitHub AI मॉडल inference endpoint और आपके GitHub टोकन का उपयोग करता है। कॉल synchronous है।

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

यह नमूना chat completion API के साथ मल्टी-टर्न बातचीत दिखाता है। जब आप मॉडल को चैट एप्लिकेशन के लिए उपयोग करते हैं, तो आपको उस बातचीत का इतिहास प्रबंधित करना होगा और नवीनतम संदेश मॉडल को भेजने होंगे।

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

### आउटपुट स्ट्रीम करें

बेहतर उपयोगकर्ता अनुभव के लिए, आप मॉडल की प्रतिक्रिया को स्ट्रीम करना चाहेंगे ताकि पहला टोकन जल्दी दिखे और लंबी प्रतिक्रियाओं के लिए इंतजार न करना पड़े।

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

### निर्भरताएँ इंस्टॉल करें

Node.js इंस्टॉल करें।

निम्नलिखित टेक्स्ट को कॉपी करें और इसे अपने फोल्डर में package.json नामक फाइल के रूप में सेव करें।

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

ध्यान दें: @azure/core-sse केवल तब आवश्यक है जब आप chat completions की प्रतिक्रिया स्ट्रीम करते हैं।

इस फोल्डर में टर्मिनल खोलें और npm install चलाएं।

नीचे दिए गए प्रत्येक कोड स्निपेट के लिए, सामग्री को sample.js नामक फाइल में कॉपी करें और node sample.js के साथ चलाएं।

### एक बुनियादी कोड नमूना चलाएं

यह नमूना chat completion API को बेसिक कॉल दिखाता है। यह GitHub AI मॉडल inference endpoint और आपके GitHub टोकन का उपयोग करता है। कॉल synchronous है।

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

यह नमूना chat completion API के साथ मल्टी-टर्न बातचीत दिखाता है। जब आप मॉडल को चैट एप्लिकेशन के लिए उपयोग करते हैं, तो आपको उस बातचीत का इतिहास प्रबंधित करना होगा और नवीनतम संदेश मॉडल को भेजने होंगे।

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

### आउटपुट स्ट्रीम करें

बेहतर उपयोगकर्ता अनुभव के लिए, आप मॉडल की प्रतिक्रिया को स्ट्रीम करना चाहेंगे ताकि पहला टोकन जल्दी दिखे और लंबी प्रतिक्रियाओं के लिए इंतजार न करना पड़े।

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

### एक बुनियादी कोड नमूना चलाएं

निम्नलिखित को एक शेल में पेस्ट करें:

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

chat completion API को कॉल करें और चैट इतिहास पास करें:

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

### आउटपुट स्ट्रीम करें

यह endpoint को कॉल करने और प्रतिक्रिया स्ट्रीम करने का एक उदाहरण है।

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

## GitHub मॉडल्स के लिए मुफ्त उपयोग और दर सीमाएँ

![Model Catalog](../../../../translated_images/GitHub_Model.ca6c125cb3117d0e.hi.png)

[प्लेग्राउंड और मुफ्त API उपयोग के लिए दर सीमाएँ](https://docs.github.com/en/github-models/prototyping-with-ai-models#rate-limits) आपको मॉडल्स के साथ प्रयोग करने और अपने AI एप्लिकेशन का प्रोटोटाइप बनाने में मदद करने के लिए हैं। इन सीमाओं से आगे उपयोग के लिए, और अपने एप्लिकेशन को स्केल पर लाने के लिए, आपको Azure खाते से संसाधन प्रावधान करना होगा, और वहां से प्रमाणीकरण करना होगा न कि अपने GitHub personal access token से। आपको अपने कोड में कुछ भी बदलने की आवश्यकता नहीं है। Azure AI में मुफ्त स्तर की सीमाओं से आगे जाने के लिए इस लिंक का उपयोग करें।

### खुलासे

जब आप किसी मॉडल के साथ इंटरैक्ट कर रहे होते हैं, तो याद रखें कि आप AI के साथ प्रयोग कर रहे हैं, इसलिए सामग्री में गलतियाँ हो सकती हैं।

यह फीचर विभिन्न सीमाओं (जैसे प्रति मिनट अनुरोध, प्रति दिन अनुरोध, प्रति अनुरोध टोकन, और समवर्ती अनुरोध) के अधीन है और इसे प्रोडक्शन उपयोग के लिए डिज़ाइन नहीं किया गया है।

GitHub मॉडल्स Azure AI Content Safety का उपयोग करता है। ये फ़िल्टर GitHub मॉडल्स अनुभव के हिस्से के रूप में बंद नहीं किए जा सकते। यदि आप भुगतान सेवा के माध्यम से मॉडल्स का उपयोग करने का निर्णय लेते हैं, तो कृपया अपनी सामग्री फ़िल्टर को अपनी आवश्यकताओं के अनुसार कॉन्फ़िगर करें।

यह सेवा GitHub के प्री-रिलीज़ टर्म्स के अधीन है।

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही अधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।