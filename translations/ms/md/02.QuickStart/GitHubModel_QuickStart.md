<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5113634b77370af6790f9697d5d7de90",
  "translation_date": "2025-07-17T05:39:53+00:00",
  "source_file": "md/02.QuickStart/GitHubModel_QuickStart.md",
  "language_code": "ms"
}
-->
## GitHub Models - Beta Awam Terhad

Selamat datang ke [GitHub Models](https://github.com/marketplace/models)! Kami telah menyediakan segala-galanya untuk anda meneroka Model AI yang dihoskan di Azure AI.

![GitHubModel](../../../../translated_images/ms/GitHub_ModelCatalog.aa43c51c36454747.png)

Untuk maklumat lanjut mengenai Model yang tersedia di GitHub Models, sila lawati [GitHub Model Marketplace](https://github.com/marketplace/models)

## Model Tersedia

Setiap model mempunyai ruang ujian khusus dan contoh kod

![Phi-3Model_Github](../../../../imgs/01/02/02/GitHub_ModelPlay.png)

### Model Phi-3 dalam Katalog Model GitHub

[Phi-3-Medium-128k-Instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-128k-instruct)

[Phi-3-medium-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-4k-instruct)

[Phi-3-mini-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-128k-instruct)

[Phi-3-mini-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-4k-instruct)

[Phi-3-small-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-128k-instruct)

[Phi-3-small-8k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-8k-instruct)

## Memulakan

Terdapat beberapa contoh asas yang sedia untuk anda jalankan. Anda boleh menemui mereka dalam direktori samples. Jika anda ingin terus ke bahasa kegemaran anda, contoh-contoh tersebut boleh didapati dalam Bahasa berikut:

- Python
- JavaScript
- cURL

Terdapat juga Persekitaran Codespaces khusus untuk menjalankan contoh dan model.

![Getting Started](../../../../translated_images/ms/GitHub_ModelGetStarted.150220a802da6fb6.png)

## Contoh Kod

Di bawah adalah petikan kod contoh untuk beberapa kes penggunaan. Untuk maklumat tambahan mengenai Azure AI Inference SDK, sila rujuk dokumentasi penuh dan contoh.

## Persediaan

1. Cipta token akses peribadi  
Anda tidak perlu memberikan sebarang kebenaran kepada token tersebut. Perlu diingat bahawa token ini akan dihantar ke perkhidmatan Microsoft.

Untuk menggunakan petikan kod di bawah, cipta pembolehubah persekitaran untuk menetapkan token anda sebagai kunci untuk kod klien.

Jika anda menggunakan bash:  
```
export GITHUB_TOKEN="<your-github-token-goes-here>"
```  
Jika anda menggunakan powershell:  

```
$Env:GITHUB_TOKEN="<your-github-token-goes-here>"
```  

Jika anda menggunakan command prompt Windows:  

```
set GITHUB_TOKEN=<your-github-token-goes-here>
```  

## Contoh Python

### Pasang kebergantungan  
Pasang Azure AI Inference SDK menggunakan pip (Memerlukan: Python >=3.8):

```
pip install azure-ai-inference
```  
### Jalankan contoh kod asas

Contoh ini menunjukkan panggilan asas ke API chat completion. Ia menggunakan titik akhir inferens model AI GitHub dan token GitHub anda. Panggilan ini adalah secara segerak.

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

### Jalankan perbualan berbilang giliran

Contoh ini menunjukkan perbualan berbilang giliran dengan API chat completion. Apabila menggunakan model untuk aplikasi chat, anda perlu mengurus sejarah perbualan tersebut dan menghantar mesej terkini ke model.

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

### Alirkan output

Untuk pengalaman pengguna yang lebih baik, anda ingin mengalirkan respons model supaya token pertama muncul lebih awal dan anda tidak perlu menunggu respons yang panjang.

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

### Pasang kebergantungan

Pasang Node.js.

Salin baris teks berikut dan simpan sebagai fail package.json dalam folder anda.

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

Nota: @azure/core-sse hanya diperlukan apabila anda mengalirkan respons chat completions.

Buka tetingkap terminal dalam folder ini dan jalankan npm install.

Untuk setiap petikan kod di bawah, salin kandungan ke dalam fail sample.js dan jalankan dengan node sample.js.

### Jalankan contoh kod asas

Contoh ini menunjukkan panggilan asas ke API chat completion. Ia menggunakan titik akhir inferens model AI GitHub dan token GitHub anda. Panggilan ini adalah secara segerak.

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

### Jalankan perbualan berbilang giliran

Contoh ini menunjukkan perbualan berbilang giliran dengan API chat completion. Apabila menggunakan model untuk aplikasi chat, anda perlu mengurus sejarah perbualan tersebut dan menghantar mesej terkini ke model.

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

### Alirkan output  
Untuk pengalaman pengguna yang lebih baik, anda ingin mengalirkan respons model supaya token pertama muncul lebih awal dan anda tidak perlu menunggu respons yang panjang.

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

### Jalankan contoh kod asas

Tampal yang berikut ke dalam shell:

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
### Jalankan perbualan berbilang giliran

Panggil API chat completion dan hantar sejarah chat:

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
### Alirkan output

Ini adalah contoh memanggil titik akhir dan mengalirkan respons.

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

## Penggunaan PERCUMA dan Had Kadar untuk GitHub Models

![Model Catalog](../../../../translated_images/ms/GitHub_Model.ca6c125cb3117d0e.png)

[Had kadar untuk playground dan penggunaan API percuma](https://docs.github.com/en/github-models/prototyping-with-ai-models#rate-limits) bertujuan untuk membantu anda bereksperimen dengan model dan membuat prototaip aplikasi AI anda. Untuk penggunaan melebihi had tersebut, dan untuk mengembangkan aplikasi anda, anda mesti menyediakan sumber dari akaun Azure, dan mengesahkan dari situ dan bukannya menggunakan token akses peribadi GitHub anda. Anda tidak perlu mengubah apa-apa dalam kod anda. Gunakan pautan ini untuk mengetahui cara melebihi had tahap percuma dalam Azure AI.

### Pendedahan

Ingat bahawa apabila berinteraksi dengan model, anda sedang bereksperimen dengan AI, jadi kesilapan kandungan mungkin berlaku.

Ciri ini tertakluk kepada pelbagai had (termasuk permintaan per minit, permintaan per hari, token per permintaan, dan permintaan serentak) dan tidak direka untuk kes penggunaan produksi.

GitHub Models menggunakan Azure AI Content Safety. Penapis ini tidak boleh dimatikan sebagai sebahagian daripada pengalaman GitHub Models. Jika anda memilih untuk menggunakan model melalui perkhidmatan berbayar, sila konfigurasikan penapis kandungan anda mengikut keperluan anda.

Perkhidmatan ini tertakluk kepada Terma Pra-siaran GitHub.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.