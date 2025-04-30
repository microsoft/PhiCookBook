<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3f37da1518bfb2cc9a8faa427fb0c916",
  "translation_date": "2025-04-04T18:46:37+00:00",
  "source_file": "md\\02.QuickStart\\GitHubModel_QuickStart.md",
  "language_code": "hk"
}
-->
## GitHub 模型 - 限量公開測試版

歡迎來到 [GitHub Models](https://github.com/marketplace/models)! 我們已經準備好讓你探索 Azure AI 上託管的 AI 模型。

![GitHubModel](../../../../translated_images/GitHub_ModelCatalog.4fc858ab26afe64c43f5e423ad0c5c733878bb536fdb027a5bcf1f80c41b0633.hk.png)

想了解更多關於 GitHub Models 上提供的模型，可以查看 [GitHub Model Marketplace](https://github.com/marketplace/models)。

## 可用模型

每個模型都有專屬的操作介面和範例代碼。

![Phi-3Model_Github](../../../../imgs/01/02/02/GitHub_ModelPlay.png)

### GitHub 模型目錄中的 Phi-3 模型

[Phi-3-Medium-128k-Instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-128k-instruct)

[Phi-3-medium-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-4k-instruct)

[Phi-3-mini-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-128k-instruct)

[Phi-3-mini-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-4k-instruct)

[Phi-3-small-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-128k-instruct)

[Phi-3-small-8k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-8k-instruct)

## 開始使用

我們提供了一些基本範例，隨時可以執行。你可以在範例目錄中找到它們。如果想直接跳到你喜歡的語言，你可以在以下語言中找到範例：

- Python
- JavaScript
- cURL

此外，我們還提供了專屬的 Codespaces 環境來執行範例和模型。

![Getting Started](../../../../translated_images/GitHub_ModelGetStarted.b4b839a081583da39bc976c2f0d8ac4603d3b8c23194b16cc9e0a1014f5611d0.hk.png)

## 範例代碼 

以下是一些常見使用場景的範例代碼片段。想了解更多 Azure AI Inference SDK 的詳細信息，請參閱完整文檔和範例。

## 設置 

1. 建立個人訪問令牌
你不需要給令牌任何權限。請注意，令牌會發送到 Microsoft 服務。

要使用以下代碼片段，請建立環境變量，將令牌設置為客戶端代碼的密鑰。

如果你使用 bash:
```
export GITHUB_TOKEN="<your-github-token-goes-here>"
```
如果你使用 powershell:

```
$Env:GITHUB_TOKEN="<your-github-token-goes-here>"
```

如果你使用 Windows 命令提示符:

```
set GITHUB_TOKEN=<your-github-token-goes-here>
```

## Python 範例

### 安裝依賴項
使用 pip 安裝 Azure AI Inference SDK (需求: Python >=3.8):

```
pip install azure-ai-inference
```
### 執行基本代碼範例

此範例展示了如何基本調用聊天完成 API。它利用 GitHub AI 模型推理端點和你的 GitHub 令牌。此調用是同步的。

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

### 執行多輪對話

此範例展示了如何進行多輪對話。當模型用於聊天應用程序時，你需要管理對話的歷史記錄，並將最新的消息發送給模型。

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

### 流式輸出

為了更好的用戶體驗，你可能希望流式輸出模型的響應，這樣第一個標記可以早些顯示，避免等待較長的響應。

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

### 安裝依賴項

安裝 Node.js。

將以下文字複製並保存為 package.json 文件到你的資料夾中。

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

注意: @azure/core-sse 只有在流式輸出聊天完成響應時需要。

在此資料夾中打開終端窗口並運行 npm install。

對於以下每個代碼片段，將內容複製到 sample.js 文件中，並使用 node sample.js 執行。

### 執行基本代碼範例

此範例展示了如何基本調用聊天完成 API。它利用 GitHub AI 模型推理端點和你的 GitHub 令牌。此調用是同步的。

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

### 執行多輪對話

此範例展示了如何進行多輪對話。當模型用於聊天應用程序時，你需要管理對話的歷史記錄，並將最新的消息發送給模型。

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

### 流式輸出
為了更好的用戶體驗，你可能希望流式輸出模型的響應，這樣第一個標記可以早些顯示，避免等待較長的響應。

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

### 執行基本代碼範例

將以下內容粘貼到 shell 中：

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
### 執行多輪對話

調用聊天完成 API 並傳遞聊天歷史記錄：

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
### 流式輸出

這是調用端點並流式輸出響應的範例。

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

## GitHub 模型的免費使用及速率限制

![Model Catalog](../../../../translated_images/GitHub_Model.0c2abb992151c5407046e2b763af51505ff709f04c0950785e0300fdc8c55a0c.hk.png)

[操作介面和免費 API 使用的速率限制](https://docs.github.com/en/github-models/prototyping-with-ai-models#rate-limits) 是為了幫助你實驗模型和原型化你的 AI 應用程序。如果需要超過這些限制的使用，並將你的應用程序擴展，你必須從 Azure 帳戶中配置資源，並從那裡進行身份驗證，而不是使用你的 GitHub 個人訪問令牌。你不需要改變代碼中的其他內容。使用此連結了解如何超越 Azure AI 的免費層限制。

### 聲明

請記住，與模型互動時，你是在進行 AI 實驗，所以可能會出現內容錯誤。

此功能受各種限制（包括每分鐘請求數、每日請求數、每次請求的標記數和並發請求數）的約束，並不適用於生產環境的使用場景。

GitHub Models 使用 Azure AI 內容安全。這些過濾器在 GitHub Models 體驗中無法關閉。如果你決定通過付費服務使用模型，請配置你的內容過濾器以滿足需求。

此服務受 GitHub 的預發布條款約束。

**免責聲明**：  
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們致力於確保翻譯準確性，但請注意，自動翻譯可能會包含錯誤或不準確之處。原始語言的文件應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們對於使用此翻譯所引起的任何誤解或誤釋概不負責。