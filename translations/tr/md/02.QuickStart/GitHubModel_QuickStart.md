<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5113634b77370af6790f9697d5d7de90",
  "translation_date": "2025-05-09T20:17:45+00:00",
  "source_file": "md/02.QuickStart/GitHubModel_QuickStart.md",
  "language_code": "tr"
}
-->
## GitHub Modelleri - Sınırlı Genel Beta

[GitHub Modelleri](https://github.com/marketplace/models)'ne hoş geldiniz! Azure AI üzerinde barındırılan Yapay Zeka Modellerini keşfetmeniz için her şey hazır ve sizi bekliyor.

![GitHubModel](../../../../translated_images/GitHub_ModelCatalog.4fc858ab26afe64c43f5e423ad0c5c733878bb536fdb027a5bcf1f80c41b0633.tr.png)

GitHub Modelleri’nde bulunan modeller hakkında daha fazla bilgi için [GitHub Model Marketplace](https://github.com/marketplace/models)’i inceleyebilirsiniz.

## Mevcut Modeller

Her modelin özel bir çalışma alanı ve örnek kodu vardır.

![Phi-3Model_Github](../../../../imgs/01/02/02/GitHub_ModelPlay.png)

### GitHub Model Kataloğundaki Phi-3 Modelleri

[Phi-3-Medium-128k-Instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-128k-instruct)

[Phi-3-medium-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-4k-instruct)

[Phi-3-mini-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-128k-instruct)

[Phi-3-mini-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-4k-instruct)

[Phi-3-small-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-128k-instruct)

[Phi-3-small-8k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-8k-instruct)

## Başlarken

Çalıştırmanız için hazır birkaç temel örnek mevcut. Bunları samples dizininde bulabilirsiniz. Favori programlama dilinize doğrudan geçmek isterseniz, örnekleri aşağıdaki dillerde bulabilirsiniz:

- Python
- JavaScript
- cURL

Ayrıca örnekleri ve modelleri çalıştırmak için özel bir Codespaces Ortamı da bulunmaktadır.

![Getting Started](../../../../translated_images/GitHub_ModelGetStarted.b4b839a081583da39bc976c2f0d8ac4603d3b8c23194b16cc9e0a1014f5611d0.tr.png)

## Örnek Kod

Aşağıda bazı kullanım senaryoları için örnek kod parçacıkları yer almaktadır. Azure AI Inference SDK hakkında daha fazla bilgi için tam dokümantasyon ve örneklere bakabilirsiniz.

## Kurulum

1. Kişisel erişim tokenı oluşturun  
Token için herhangi bir izin vermeniz gerekmez. Token bir Microsoft servisine gönderilecektir.

Aşağıdaki kod parçacıklarını kullanmak için, tokenınızı client kodu için anahtar olarak ayarlayacak bir ortam değişkeni oluşturun.

Eğer bash kullanıyorsanız:  
```
export GITHUB_TOKEN="<your-github-token-goes-here>"
```  
Powershell kullanıyorsanız:  
```
$Env:GITHUB_TOKEN="<your-github-token-goes-here>"
```  
Windows komut istemcisindeyseniz:  
```
set GITHUB_TOKEN=<your-github-token-goes-here>
```

## Python Örneği

### Bağımlılıkları yükleyin  
Azure AI Inference SDK’yı pip ile yükleyin (Gereksinim: Python >=3.8):  
```
pip install azure-ai-inference
```

### Basit bir kod örneği çalıştırın

Bu örnek, chat tamamlayıcı API’ye temel bir çağrı yapmayı gösterir. GitHub AI model çıkarım uç noktasını ve GitHub tokenınızı kullanır. Çağrı eşzamanlıdır.

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

### Çok turlu sohbet yürütün

Bu örnek, chat tamamlayıcı API ile çok turlu bir sohbeti gösterir. Bir sohbet uygulamasında modeli kullanırken, sohbet geçmişini yönetmeniz ve modele en güncel mesajları göndermeniz gerekir.

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

### Çıktıyı akış halinde alın

Daha iyi bir kullanıcı deneyimi için modelin yanıtını akış halinde almayı tercih edersiniz; böylece ilk token erken görünür ve uzun yanıtlar için beklemek zorunda kalmazsınız.

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

### Bağımlılıkları yükleyin

Node.js’i kurun.

Aşağıdaki metin satırlarını kopyalayıp klasörünüzün içine package.json adlı bir dosya olarak kaydedin.

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

Not: @azure/core-sse yalnızca chat tamamlayıcı yanıtlarını akış halinde almak istediğinizde gereklidir.

Bu klasörde bir terminal açın ve npm install komutunu çalıştırın.

Aşağıdaki her kod parçacığını sample.js adlı bir dosyaya yapıştırın ve node sample.js ile çalıştırın.

### Basit bir kod örneği çalıştırın

Bu örnek, chat tamamlayıcı API’ye temel bir çağrı yapmayı gösterir. GitHub AI model çıkarım uç noktasını ve GitHub tokenınızı kullanır. Çağrı eşzamanlıdır.

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

### Çok turlu sohbet yürütün

Bu örnek, chat tamamlayıcı API ile çok turlu bir sohbeti gösterir. Bir sohbet uygulamasında modeli kullanırken, sohbet geçmişini yönetmeniz ve modele en güncel mesajları göndermeniz gerekir.

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

### Çıktıyı akış halinde alın

Daha iyi bir kullanıcı deneyimi için modelin yanıtını akış halinde almayı tercih edersiniz; böylece ilk token erken görünür ve uzun yanıtlar için beklemek zorunda kalmazsınız.

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

### Basit bir kod örneği çalıştırın

Aşağıdakini bir shell’e yapıştırın:

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

### Çok turlu sohbet yürütün

Chat tamamlayıcı API’yi çağırın ve sohbet geçmişini gönderin:

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

### Çıktıyı akış halinde alın

Bu, uç noktayı çağırıp yanıtı akış halinde alma örneğidir.

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

## GitHub Modelleri için ÜCRETSİZ Kullanım ve Oran Sınırları

![Model Catalog](../../../../translated_images/GitHub_Model.0c2abb992151c5407046e2b763af51505ff709f04c0950785e0300fdc8c55a0c.tr.png)

[Playground ve ücretsiz API kullanımı için oran sınırları](https://docs.github.com/en/github-models/prototyping-with-ai-models#rate-limits), modellerle denemeler yapmanıza ve yapay zeka uygulamanızın prototipini oluşturmanıza yardımcı olmak amacıyla konulmuştur. Bu sınırların ötesinde kullanım için ve uygulamanızı ölçeklendirmek istediğinizde, bir Azure hesabından kaynak sağlamanız ve kimlik doğrulamasını GitHub kişisel erişim tokenınız yerine oradan yapmanız gerekir. Kodunuzda başka bir değişiklik yapmanıza gerek yoktur. Ücretsiz katman sınırlarını aşmanın yollarını Azure AI’de keşfetmek için bu bağlantıyı kullanabilirsiniz.

### Açıklamalar

Bir modelle etkileşimde bulunurken yapay zeka ile deneme yaptığınızı unutmayın, bu yüzden içerik hataları olabilir.

Özellik çeşitli sınırlamalara tabidir (dakika başı istek sayısı, günlük istek sayısı, istek başına token sayısı, eşzamanlı istekler gibi) ve üretim kullanım senaryoları için tasarlanmamıştır.

GitHub Modelleri Azure AI İçerik Güvenliği kullanır. Bu filtreler, GitHub Modelleri deneyiminin bir parçası olarak kapatılamaz. Ücretli bir hizmet aracılığıyla modelleri kullanmaya karar verirseniz, içerik filtrelerinizi ihtiyaçlarınıza göre yapılandırmanız gerekir.

Bu hizmet GitHub’ın Ön Sürüm Şartları kapsamındadır.

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi ana dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.