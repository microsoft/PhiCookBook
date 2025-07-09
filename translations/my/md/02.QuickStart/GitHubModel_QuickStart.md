<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5113634b77370af6790f9697d5d7de90",
  "translation_date": "2025-07-09T20:08:26+00:00",
  "source_file": "md/02.QuickStart/GitHubModel_QuickStart.md",
  "language_code": "my"
}
-->
## GitHub Models - အများပြည်သူအတွက် ကန့်သတ်ထားသော Beta

[GitHub Models](https://github.com/marketplace/models) သို့ ကြိုဆိုပါသည်! Azure AI ပေါ်တွင် တင်ထားသော AI မော်ဒယ်များကို စူးစမ်းလေ့လာနိုင်ရန် အားလုံး ပြင်ဆင်ပြီး အသင့်ရှိပါပြီ။

![GitHubModel](../../../../imgs/01/02/02/GitHub_ModelCatalog.png)

GitHub Models တွင် ရရှိနိုင်သော မော်ဒယ်များအကြောင်း ပိုမိုသိရှိလိုပါက [GitHub Model Marketplace](https://github.com/marketplace/models) ကို ကြည့်ရှုနိုင်ပါသည်။

## ရရှိနိုင်သော မော်ဒယ်များ

မော်ဒယ်တိုင်းအတွက် သီးသန့် playground နှင့် နမူနာကုဒ်များ ရှိပါသည်။

![Phi-3Model_Github](../../../../imgs/01/02/02/GitHub_ModelPlay.png)

### GitHub Model Catalog တွင်ရှိသော Phi-3 မော်ဒယ်များ

[Phi-3-Medium-128k-Instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-128k-instruct)

[Phi-3-medium-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-4k-instruct)

[Phi-3-mini-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-128k-instruct)

[Phi-3-mini-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-4k-instruct)

[Phi-3-small-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-128k-instruct)

[Phi-3-small-8k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-8k-instruct)

## စတင်အသုံးပြုခြင်း

သင်စမ်းသပ်အသုံးပြုနိုင်ရန် အခြေခံနမူနာများ အနည်းငယ်ရှိပြီး၊ ၎င်းတို့ကို samples ဖိုလ်ဒါတွင် တွေ့နိုင်ပါသည်။ သင်နှစ်သက်ရာ ဘာသာစကားသို့ တိုက်ရိုက်သွားလိုပါက အောက်ပါ ဘာသာစကားများအတွက် နမူနာများ ရှိပါသည်-

- Python
- JavaScript
- cURL

နမူနာများနှင့် မော်ဒယ်များကို လည်ပတ်ရန် Codespaces Environment သီးသန့်လည်း ရှိပါသည်။

![Getting Started](../../../../imgs/01/02/02/GitHub_ModelGetStarted.png)

## နမူနာကုဒ်

အောက်တွင် အသုံးပြုမှုအမျိုးမျိုးအတွက် နမူနာကုဒ်များ ပါရှိသည်။ Azure AI Inference SDK အကြောင်း ပိုမိုသိရှိလိုပါက အပြည့်အစုံစာတမ်းများနှင့် နမူနာများကို ကြည့်ရှုနိုင်ပါသည်။

## ပြင်ဆင်ခြင်း

1. ကိုယ်ပိုင် access token တစ်ခု ဖန်တီးပါ  
token အတွက် ခွင့်ပြုချက် မလိုအပ်ပါ။ token ကို Microsoft ဝန်ဆောင်မှုသို့ ပို့ပေးမည်ဖြစ်သည်။

အောက်ပါကုဒ်များကို အသုံးပြုရန် သင့် token ကို client code အတွက် key အဖြစ် သတ်မှတ်ထားသော environment variable တစ်ခု ဖန်တီးပါ။

bash အသုံးပြုပါက-  
```
export GITHUB_TOKEN="<your-github-token-goes-here>"
```  
powershell အသုံးပြုပါက-  
```
$Env:GITHUB_TOKEN="<your-github-token-goes-here>"
```  
Windows command prompt အသုံးပြုပါက-  
```
set GITHUB_TOKEN=<your-github-token-goes-here>
```

## Python နမူနာ

### လိုအပ်သော library များ ထည့်သွင်းခြင်း  
pip ဖြင့် Azure AI Inference SDK ကို ထည့်သွင်းပါ (လိုအပ်ချက်- Python >=3.8):  
```
pip install azure-ai-inference
```

### အခြေခံကုဒ်နမူနာ လည်ပတ်ခြင်း

ဤနမူနာသည် chat completion API ကို အခြေခံခေါ်ဆိုမှုတစ်ခု ပြသသည်။ GitHub AI မော်ဒယ် inference endpoint နှင့် သင့် GitHub token ကို အသုံးပြုထားသည်။ ခေါ်ဆိုမှုသည် synchronous ဖြစ်သည်။

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

### မျိုးစုံပြောဆိုမှု လည်ပတ်ခြင်း

ဤနမူနာသည် chat completion API ဖြင့် မျိုးစုံပြောဆိုမှုတစ်ခု ပြသသည်။ chat application အတွက် မော်ဒယ်ကို အသုံးပြုသောအခါ၊ ပြောဆိုမှုမှတ်တမ်းကို စီမံခန့်ခွဲပြီး နောက်ဆုံးစာတိုများကို မော်ဒယ်သို့ ပို့ရန် လိုအပ်ပါသည်။

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

### ထွက်ရှိမှုကို စီးဆင်းစေခြင်း

အသုံးပြုသူအတွေ့အကြုံ ပိုမိုကောင်းမွန်စေရန် မော်ဒယ်၏ တုံ့ပြန်ချက်ကို စီးဆင်းစေလိုပါက ပထမဆုံး token များကို အစောဆုံး ပြသနိုင်ပြီး ကြာရှည်စောင့်ဆိုင်းရမှုကို ရှောင်ရှားနိုင်ပါသည်။

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

### လိုအပ်သော library များ ထည့်သွင်းခြင်း

Node.js ကို ထည့်သွင်းပါ။

အောက်ပါစာကြောင်းများကို ကူးယူပြီး သင့်ဖိုလ်ဒါအတွင်း package.json အဖြစ် သိမ်းဆည်းပါ။

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

မှတ်ချက်- @azure/core-sse သည် chat completions response ကို စီးဆင်းစေချိန်တွင်သာ လိုအပ်ပါသည်။

ဤဖိုလ်ဒါတွင် terminal ကို ဖွင့်ပြီး npm install ကို လည်ပတ်ပါ။

အောက်ပါကုဒ်များကို sample.js ဖိုင်အဖြစ် သိမ်းပြီး node sample.js ဖြင့် လည်ပတ်ပါ။

### အခြေခံကုဒ်နမူနာ လည်ပတ်ခြင်း

ဤနမူနာသည် chat completion API ကို အခြေခံခေါ်ဆိုမှုတစ်ခု ပြသသည်။ GitHub AI မော်ဒယ် inference endpoint နှင့် သင့် GitHub token ကို အသုံးပြုထားသည်။ ခေါ်ဆိုမှုသည် synchronous ဖြစ်သည်။

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

### မျိုးစုံပြောဆိုမှု လည်ပတ်ခြင်း

ဤနမူနာသည် chat completion API ဖြင့် မျိုးစုံပြောဆိုမှုတစ်ခု ပြသသည်။ chat application အတွက် မော်ဒယ်ကို အသုံးပြုသောအခါ၊ ပြောဆိုမှုမှတ်တမ်းကို စီမံခန့်ခွဲပြီး နောက်ဆုံးစာတိုများကို မော်ဒယ်သို့ ပို့ရန် လိုအပ်ပါသည်။

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

### ထွက်ရှိမှုကို စီးဆင်းစေခြင်း

အသုံးပြုသူအတွေ့အကြုံ ပိုမိုကောင်းမွန်စေရန် မော်ဒယ်၏ တုံ့ပြန်ချက်ကို စီးဆင်းစေလိုပါက ပထမဆုံး token များကို အစောဆုံး ပြသနိုင်ပြီး ကြာရှည်စောင့်ဆိုင်းရမှုကို ရှောင်ရှားနိုင်ပါသည်။

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

### အခြေခံကုဒ်နမူနာ လည်ပတ်ခြင်း

အောက်ပါကို shell ထဲတွင် ကူးထည့်ပါ-

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

### မျိုးစုံပြောဆိုမှု လည်ပတ်ခြင်း

chat completion API ကို ခေါ်ဆိုပြီး chat မှတ်တမ်းကို ပေးပို့ပါ-

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

### ထွက်ရှိမှုကို စီးဆင်းစေခြင်း

ဤသည်မှာ endpoint ကို ခေါ်ဆိုပြီး တုံ့ပြန်ချက်ကို စီးဆင်းစေသော နမူနာဖြစ်သည်။

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

## GitHub Models အတွက် အခမဲ့ အသုံးပြုမှုနှင့် အမြန်နှုန်း ကန့်သတ်ချက်များ

![Model Catalog](../../../../imgs/01/02/02/GitHub_Model.png)

[playground နှင့် အခမဲ့ API အသုံးပြုမှုအတွက် rate limits](https://docs.github.com/en/github-models/prototyping-with-ai-models#rate-limits) များသည် မော်ဒယ်များကို စမ်းသပ်ရန်နှင့် AI application များကို prototype ပြုလုပ်ရန် အထောက်အကူပြုရန် ရည်ရွယ်ထားသည်။ ထိုကန့်သတ်ချက်များ ကျော်လွန်၍ သင့် application ကို အရွယ်အစားကြီးစေရန်အတွက် Azure အကောင့်မှ အရင်းအမြစ်များကို စီမံခန့်ခွဲပြီး GitHub ကိုယ်ပိုင် access token အစား အဲဒီနေရာမှ authentication ပြုလုပ်ရမည်ဖြစ်သည်။ သင့်ကုဒ်တွင် အခြားပြောင်းလဲရန် မလိုအပ်ပါ။ Azure AI တွင် အခမဲ့အဆင့်ကန့်သတ်ချက်များ ကျော်လွန်နည်းကို သိရှိလိုပါက ဤလင့်ခ်ကို အသုံးပြုပါ။

### ထုတ်ဖော်ကြေညာချက်များ

မော်ဒယ်နှင့် ဆက်သွယ်စဉ် AI ကို စမ်းသပ်နေသည်ဖြစ်၍ အကြောင်းအရာအမှားများ ဖြစ်ပေါ်နိုင်သည်ကို မှတ်သားပါ။

ဤ feature သည် မိနစ်နှုန်း၊ တစ်ရက်အတွင်း တောင်းဆိုမှုအရေအတွက်၊ တောင်းဆိုမှုတစ်ခုလျှင် token အရေအတွက်နှင့် တပြိုင်နက်တောင်းဆိုမှုအရေအတွက် ကန့်သတ်ချက်များရှိပြီး ထုတ်လုပ်မှုအတွက် မသင့်တော်ပါ။

GitHub Models သည် Azure AI Content Safety ကို အသုံးပြုသည်။ ဤစစ်ထုတ်မှုများကို GitHub Models အတွေ့အကြုံအတွင်း ပိတ်ထား၍ မရပါ။ ပေးချေသည့် ဝန်ဆောင်မှုမှတဆင့် မော်ဒယ်များကို အသုံးပြုလိုပါက သင့်အကြောင်းအရာ စစ်ထုတ်မှုများကို သင့်လိုအပ်ချက်အတိုင်း ပြင်ဆင်ပါ။

ဤဝန်ဆောင်မှုသည် GitHub ၏ Pre-release Terms အောက်တွင် ရှိပါသည်။

**အကြောင်းကြားချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားသော်လည်း အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် မေတ္တာရပ်ခံအပ်ပါသည်။ မူရင်းစာတမ်းကို မိမိဘာသာစကားဖြင့်သာ တရားဝင်အချက်အလက်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်မှ ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုရာမှ ဖြစ်ပေါ်လာနိုင်သည့် နားလည်မှုမှားယွင်းမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။