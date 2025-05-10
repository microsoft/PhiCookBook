<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5113634b77370af6790f9697d5d7de90",
  "translation_date": "2025-05-09T20:19:53+00:00",
  "source_file": "md/02.QuickStart/GitHubModel_QuickStart.md",
  "language_code": "vi"
}
-->
## GitHub Models - Phiên bản Beta Công khai Giới hạn

Chào mừng bạn đến với [GitHub Models](https://github.com/marketplace/models)! Chúng tôi đã chuẩn bị sẵn sàng để bạn khám phá các Mô hình AI được lưu trữ trên Azure AI.

![GitHubModel](../../../../translated_images/GitHub_ModelCatalog.4fc858ab26afe64c43f5e423ad0c5c733878bb536fdb027a5bcf1f80c41b0633.vi.png)

Để biết thêm thông tin về các Mô hình có trên GitHub Models, hãy tham khảo [GitHub Model Marketplace](https://github.com/marketplace/models)

## Các Mô hình Có sẵn

Mỗi mô hình đều có một khu vực thử nghiệm riêng và mã mẫu đi kèm

![Phi-3Model_Github](../../../../imgs/01/02/02/GitHub_ModelPlay.png)

### Các Mô hình Phi-3 trong Danh mục Mô hình GitHub

[Phi-3-Medium-128k-Instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-128k-instruct)

[Phi-3-medium-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-4k-instruct)

[Phi-3-mini-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-128k-instruct)

[Phi-3-mini-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-4k-instruct)

[Phi-3-small-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-128k-instruct)

[Phi-3-small-8k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-8k-instruct)

## Bắt đầu

Có một số ví dụ cơ bản sẵn sàng để bạn chạy. Bạn có thể tìm thấy chúng trong thư mục samples. Nếu bạn muốn chuyển thẳng đến ngôn ngữ yêu thích, các ví dụ có thể được tìm thấy trong các Ngôn ngữ sau:

- Python
- JavaScript
- cURL

Ngoài ra còn có một Môi trường Codespaces chuyên biệt để chạy các mẫu và mô hình.

![Getting Started](../../../../translated_images/GitHub_ModelGetStarted.b4b839a081583da39bc976c2f0d8ac4603d3b8c23194b16cc9e0a1014f5611d0.vi.png)

## Mã mẫu

Dưới đây là các đoạn mã ví dụ cho một số trường hợp sử dụng. Để biết thêm thông tin về Azure AI Inference SDK, xem tài liệu đầy đủ và các mẫu.

## Cài đặt

1. Tạo token truy cập cá nhân  
Bạn không cần cấp quyền gì cho token. Lưu ý rằng token sẽ được gửi đến dịch vụ của Microsoft.

Để sử dụng các đoạn mã bên dưới, hãy tạo biến môi trường để đặt token của bạn làm khóa cho mã client.

Nếu bạn dùng bash:  
```
export GITHUB_TOKEN="<your-github-token-goes-here>"
```  
Nếu bạn dùng powershell:  

```
$Env:GITHUB_TOKEN="<your-github-token-goes-here>"
```  

Nếu bạn dùng Windows command prompt:  

```
set GITHUB_TOKEN=<your-github-token-goes-here>
```  

## Ví dụ Python

### Cài đặt các phụ thuộc  
Cài đặt Azure AI Inference SDK bằng pip (Yêu cầu: Python >=3.8):

```
pip install azure-ai-inference
```  
### Chạy ví dụ mã cơ bản

Ví dụ này minh họa một cuộc gọi cơ bản đến API hoàn thành chat. Nó sử dụng endpoint suy luận mô hình AI GitHub và token GitHub của bạn. Cuộc gọi này là đồng bộ.

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

### Chạy hội thoại nhiều lượt

Ví dụ này minh họa một cuộc hội thoại nhiều lượt với API hoàn thành chat. Khi dùng mô hình cho ứng dụng chat, bạn cần quản lý lịch sử cuộc hội thoại và gửi các tin nhắn mới nhất đến mô hình.

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

### Phát trực tiếp kết quả

Để có trải nghiệm người dùng tốt hơn, bạn nên phát trực tiếp phản hồi từ mô hình để token đầu tiên hiển thị sớm và tránh phải chờ đợi các phản hồi dài.

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

### Cài đặt các phụ thuộc

Cài đặt Node.js.

Sao chép các dòng dưới đây và lưu vào file package.json trong thư mục của bạn.

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

Lưu ý: @azure/core-sse chỉ cần khi bạn phát trực tiếp phản hồi hoàn thành chat.

Mở cửa sổ terminal trong thư mục này và chạy npm install.

Với mỗi đoạn mã bên dưới, sao chép nội dung vào file sample.js và chạy bằng lệnh node sample.js.

### Chạy ví dụ mã cơ bản

Ví dụ này minh họa một cuộc gọi cơ bản đến API hoàn thành chat. Nó sử dụng endpoint suy luận mô hình AI GitHub và token GitHub của bạn. Cuộc gọi này là đồng bộ.

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

### Chạy hội thoại nhiều lượt

Ví dụ này minh họa một cuộc hội thoại nhiều lượt với API hoàn thành chat. Khi dùng mô hình cho ứng dụng chat, bạn cần quản lý lịch sử cuộc hội thoại và gửi các tin nhắn mới nhất đến mô hình.

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

### Phát trực tiếp kết quả  
Để có trải nghiệm người dùng tốt hơn, bạn nên phát trực tiếp phản hồi từ mô hình để token đầu tiên hiển thị sớm và tránh phải chờ đợi các phản hồi dài.

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

### Chạy ví dụ mã cơ bản

Dán đoạn sau vào shell:

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
### Chạy hội thoại nhiều lượt

Gọi API hoàn thành chat và truyền lịch sử chat:

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
### Phát trực tiếp kết quả

Đây là ví dụ gọi endpoint và phát trực tiếp phản hồi.

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

## Sử dụng MIỄN PHÍ và Giới hạn tốc độ cho GitHub Models

![Model Catalog](../../../../translated_images/GitHub_Model.0c2abb992151c5407046e2b763af51505ff709f04c0950785e0300fdc8c55a0c.vi.png)

[Giới hạn tốc độ cho khu vực thử nghiệm và API miễn phí](https://docs.github.com/en/github-models/prototyping-with-ai-models#rate-limits) nhằm giúp bạn thử nghiệm các mô hình và phát triển ứng dụng AI. Để sử dụng vượt quá giới hạn này và mở rộng ứng dụng, bạn phải cấp phát tài nguyên từ tài khoản Azure và xác thực từ đó thay vì dùng token truy cập cá nhân GitHub. Bạn không cần thay đổi gì khác trong mã của mình. Sử dụng liên kết này để tìm hiểu cách vượt qua giới hạn miễn phí trong Azure AI.

### Lưu ý

Hãy nhớ rằng khi tương tác với mô hình, bạn đang thử nghiệm AI nên có thể xảy ra sai sót về nội dung.

Tính năng này bị giới hạn bởi nhiều yếu tố (bao gồm số yêu cầu mỗi phút, mỗi ngày, token mỗi yêu cầu, và số yêu cầu đồng thời) và không thiết kế cho các trường hợp sử dụng sản xuất.

GitHub Models sử dụng Azure AI Content Safety. Các bộ lọc này không thể tắt trong trải nghiệm GitHub Models. Nếu bạn quyết định sử dụng mô hình qua dịch vụ trả phí, vui lòng cấu hình bộ lọc nội dung theo yêu cầu của bạn.

Dịch vụ này đang trong điều khoản Phát hành trước của GitHub.

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn thông tin chính xác nhất. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.