<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5113634b77370af6790f9697d5d7de90",
  "translation_date": "2025-07-17T05:39:37+00:00",
  "source_file": "md/02.QuickStart/GitHubModel_QuickStart.md",
  "language_code": "id"
}
-->
## GitHub Models - Beta Publik Terbatas

Selamat datang di [GitHub Models](https://github.com/marketplace/models)! Kami sudah menyiapkan semuanya agar Anda bisa menjelajahi Model AI yang dihosting di Azure AI.

![GitHubModel](../../../../translated_images/id/GitHub_ModelCatalog.aa43c51c36454747.png)

Untuk informasi lebih lanjut tentang Model yang tersedia di GitHub Models, lihat [GitHub Model Marketplace](https://github.com/marketplace/models)

## Model yang Tersedia

Setiap model memiliki playground khusus dan contoh kode

![Phi-3Model_Github](../../../../imgs/01/02/02/GitHub_ModelPlay.png)

### Model Phi-3 di Katalog Model GitHub

[Phi-3-Medium-128k-Instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-128k-instruct)

[Phi-3-medium-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-4k-instruct)

[Phi-3-mini-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-128k-instruct)

[Phi-3-mini-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-4k-instruct)

[Phi-3-small-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-128k-instruct)

[Phi-3-small-8k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-8k-instruct)

## Memulai

Ada beberapa contoh dasar yang siap untuk Anda jalankan. Anda bisa menemukannya di direktori samples. Jika ingin langsung ke bahasa favorit Anda, contoh-contoh tersebut tersedia dalam bahasa berikut:

- Python
- JavaScript
- cURL

Tersedia juga lingkungan Codespaces khusus untuk menjalankan contoh dan model.

![Getting Started](../../../../translated_images/id/GitHub_ModelGetStarted.150220a802da6fb6.png)

## Contoh Kode

Berikut adalah potongan kode contoh untuk beberapa kasus penggunaan. Untuk informasi lebih lengkap tentang Azure AI Inference SDK, lihat dokumentasi dan contoh lengkap.

## Setup

1. Buat personal access token  
Anda tidak perlu memberikan izin apapun pada token tersebut. Perlu diingat token akan dikirim ke layanan Microsoft.

Untuk menggunakan potongan kode di bawah, buat variabel lingkungan untuk menyimpan token Anda sebagai kunci untuk kode klien.

Jika menggunakan bash:  
```
export GITHUB_TOKEN="<your-github-token-goes-here>"
```  
Jika menggunakan powershell:  

```
$Env:GITHUB_TOKEN="<your-github-token-goes-here>"
```  

Jika menggunakan command prompt Windows:  

```
set GITHUB_TOKEN=<your-github-token-goes-here>
```  

## Contoh Python

### Instal dependensi  
Instal Azure AI Inference SDK menggunakan pip (Memerlukan: Python >=3.8):

```
pip install azure-ai-inference
```  
### Jalankan contoh kode dasar

Contoh ini menunjukkan panggilan dasar ke API chat completion. Ini menggunakan endpoint inferensi model AI GitHub dan token GitHub Anda. Panggilan ini bersifat sinkron.

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

### Jalankan percakapan multi-giliran

Contoh ini menunjukkan percakapan multi-giliran dengan API chat completion. Saat menggunakan model untuk aplikasi chat, Anda perlu mengelola riwayat percakapan dan mengirim pesan terbaru ke model.

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

### Streaming output

Untuk pengalaman pengguna yang lebih baik, Anda ingin melakukan streaming respons model agar token pertama muncul lebih cepat dan menghindari menunggu respons yang lama.

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

### Instal dependensi

Instal Node.js.

Salin baris teks berikut dan simpan sebagai file package.json di dalam folder Anda.

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

Catatan: @azure/core-sse hanya diperlukan saat Anda melakukan streaming respons chat completions.

Buka terminal di folder ini dan jalankan npm install.

Untuk setiap potongan kode di bawah, salin isinya ke file sample.js dan jalankan dengan node sample.js.

### Jalankan contoh kode dasar

Contoh ini menunjukkan panggilan dasar ke API chat completion. Ini menggunakan endpoint inferensi model AI GitHub dan token GitHub Anda. Panggilan ini bersifat sinkron.

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

### Jalankan percakapan multi-giliran

Contoh ini menunjukkan percakapan multi-giliran dengan API chat completion. Saat menggunakan model untuk aplikasi chat, Anda perlu mengelola riwayat percakapan dan mengirim pesan terbaru ke model.

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

### Streaming output  
Untuk pengalaman pengguna yang lebih baik, Anda ingin melakukan streaming respons model agar token pertama muncul lebih cepat dan menghindari menunggu respons yang lama.

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

### Jalankan contoh kode dasar

Tempelkan berikut ini ke shell:

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
### Jalankan percakapan multi-giliran

Panggil API chat completion dan kirim riwayat chat:

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
### Streaming output

Ini adalah contoh pemanggilan endpoint dan streaming respons.

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

## Penggunaan GRATIS dan Batasan Rate untuk GitHub Models

![Model Catalog](../../../../translated_images/id/GitHub_Model.ca6c125cb3117d0e.png)

[Batasan rate untuk playground dan penggunaan API gratis](https://docs.github.com/en/github-models/prototyping-with-ai-models#rate-limits) dimaksudkan untuk membantu Anda bereksperimen dengan model dan membuat prototipe aplikasi AI Anda. Untuk penggunaan di luar batas tersebut, dan untuk membawa aplikasi Anda ke skala yang lebih besar, Anda harus menyediakan sumber daya dari akun Azure, dan melakukan autentikasi dari sana, bukan menggunakan personal access token GitHub Anda. Anda tidak perlu mengubah apapun di kode Anda. Gunakan tautan ini untuk mengetahui cara melewati batasan free tier di Azure AI.

### Pengungkapan

Ingatlah saat berinteraksi dengan model Anda sedang bereksperimen dengan AI, sehingga kesalahan konten mungkin terjadi.

Fitur ini memiliki berbagai batasan (termasuk permintaan per menit, permintaan per hari, token per permintaan, dan permintaan bersamaan) dan tidak dirancang untuk kasus penggunaan produksi.

GitHub Models menggunakan Azure AI Content Safety. Filter ini tidak dapat dimatikan sebagai bagian dari pengalaman GitHub Models. Jika Anda memutuskan menggunakan model melalui layanan berbayar, harap konfigurasikan filter konten Anda sesuai kebutuhan.

Layanan ini berada di bawah Ketentuan Pra-rilis GitHub.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.