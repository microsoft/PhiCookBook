<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5113634b77370af6790f9697d5d7de90",
  "translation_date": "2025-07-17T05:30:35+00:00",
  "source_file": "md/02.QuickStart/GitHubModel_QuickStart.md",
  "language_code": "de"
}
-->
## GitHub Models – Begrenzte öffentliche Beta

Willkommen bei [GitHub Models](https://github.com/marketplace/models)! Wir haben alles startklar gemacht, damit du die auf Azure AI gehosteten KI-Modelle erkunden kannst.

![GitHubModel](../../../../translated_images/de/GitHub_ModelCatalog.aa43c51c36454747.webp)

Weitere Informationen zu den auf GitHub Models verfügbaren Modellen findest du im [GitHub Model Marketplace](https://github.com/marketplace/models).

## Verfügbare Modelle

Jedes Modell verfügt über eine eigene Spielwiese und Beispielcode.

![Phi-3Model_Github](../../../../imgs/01/02/02/GitHub_ModelPlay.png)

### Phi-3 Modelle im GitHub Modelkatalog

[Phi-3-Medium-128k-Instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-128k-instruct)

[Phi-3-medium-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-4k-instruct)

[Phi-3-mini-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-128k-instruct)

[Phi-3-mini-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-4k-instruct)

[Phi-3-small-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-128k-instruct)

[Phi-3-small-8k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-8k-instruct)

## Erste Schritte

Es gibt einige grundlegende Beispiele, die du direkt ausführen kannst. Du findest sie im Verzeichnis samples. Wenn du direkt zu deiner bevorzugten Programmiersprache springen möchtest, findest du die Beispiele in den folgenden Sprachen:

- Python
- JavaScript
- cURL

Es gibt außerdem eine spezielle Codespaces-Umgebung zum Ausführen der Beispiele und Modelle.

![Getting Started](../../../../translated_images/de/GitHub_ModelGetStarted.150220a802da6fb6.webp)

## Beispielcode

Nachfolgend findest du Beispielcode-Snippets für einige Anwendungsfälle. Für weitere Informationen zum Azure AI Inference SDK siehe die vollständige Dokumentation und Beispiele.

## Einrichtung

1. Erstelle ein persönliches Zugriffstoken  
Du musst dem Token keine Berechtigungen zuweisen. Beachte, dass das Token an einen Microsoft-Dienst gesendet wird.

Um die untenstehenden Codebeispiele zu verwenden, erstelle eine Umgebungsvariable, in der du dein Token als Schlüssel für den Client-Code festlegst.

Wenn du bash verwendest:  
```
export GITHUB_TOKEN="<your-github-token-goes-here>"
```  
Wenn du PowerShell nutzt:  

```
$Env:GITHUB_TOKEN="<your-github-token-goes-here>"
```  

Wenn du die Windows-Eingabeaufforderung verwendest:  

```
set GITHUB_TOKEN=<your-github-token-goes-here>
```  

## Python-Beispiel

### Abhängigkeiten installieren  
Installiere das Azure AI Inference SDK mit pip (Voraussetzung: Python >=3.8):

```
pip install azure-ai-inference
```  
### Einfaches Beispiel ausführen

Dieses Beispiel zeigt einen einfachen Aufruf der Chat Completion API. Es nutzt den GitHub AI Model Inference Endpoint und dein GitHub-Token. Der Aufruf erfolgt synchron.

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

### Mehrstufige Unterhaltung führen

Dieses Beispiel zeigt eine mehrstufige Unterhaltung mit der Chat Completion API. Wenn du das Modell für eine Chat-Anwendung nutzt, musst du den Verlauf der Unterhaltung verwalten und die neuesten Nachrichten an das Modell senden.

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

### Ausgabe streamen

Für eine bessere Nutzererfahrung möchtest du die Antwort des Modells streamen, damit das erste Token früh angezeigt wird und du nicht lange auf die Antwort warten musst.

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

### Abhängigkeiten installieren

Installiere Node.js.

Kopiere die folgenden Zeilen und speichere sie als Datei package.json in deinem Ordner.

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

Hinweis: @azure/core-sse wird nur benötigt, wenn du die Chat Completion-Antwort streamst.

Öffne ein Terminal in diesem Ordner und führe npm install aus.

Für jedes der untenstehenden Codebeispiele kopiere den Inhalt in eine Datei sample.js und führe sie mit node sample.js aus.

### Einfaches Beispiel ausführen

Dieses Beispiel zeigt einen einfachen Aufruf der Chat Completion API. Es nutzt den GitHub AI Model Inference Endpoint und dein GitHub-Token. Der Aufruf erfolgt synchron.

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

### Mehrstufige Unterhaltung führen

Dieses Beispiel zeigt eine mehrstufige Unterhaltung mit der Chat Completion API. Wenn du das Modell für eine Chat-Anwendung nutzt, musst du den Verlauf der Unterhaltung verwalten und die neuesten Nachrichten an das Modell senden.

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

### Ausgabe streamen

Für eine bessere Nutzererfahrung möchtest du die Antwort des Modells streamen, damit das erste Token früh angezeigt wird und du nicht lange auf die Antwort warten musst.

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

### Einfaches Beispiel ausführen

Füge Folgendes in eine Shell ein:

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
### Mehrstufige Unterhaltung führen

Rufe die Chat Completion API auf und übergebe den Chat-Verlauf:

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
### Ausgabe streamen

Dies ist ein Beispiel für den Aufruf des Endpunkts mit Streaming der Antwort.

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

## KOSTENLOSE Nutzung und Ratenbegrenzungen für GitHub Models

![Model Catalog](../../../../translated_images/de/GitHub_Model.ca6c125cb3117d0e.webp)

Die [Ratenbegrenzungen für die Spielwiese und die kostenlose API-Nutzung](https://docs.github.com/en/github-models/prototyping-with-ai-models#rate-limits) sollen dir helfen, Modelle auszuprobieren und deine KI-Anwendung zu prototypisieren. Für die Nutzung über diese Limits hinaus und um deine Anwendung zu skalieren, musst du Ressourcen über ein Azure-Konto bereitstellen und dich dort authentifizieren, anstatt dein persönliches GitHub-Zugriffstoken zu verwenden. Du musst sonst nichts an deinem Code ändern. Nutze diesen Link, um zu erfahren, wie du die kostenlosen Kontingente in Azure AI überschreiten kannst.

### Hinweise

Beachte, dass du beim Interagieren mit einem Modell mit KI experimentierst, weshalb Fehler im Inhalt möglich sind.

Die Funktion unterliegt verschiedenen Beschränkungen (einschließlich Anfragen pro Minute, Anfragen pro Tag, Tokens pro Anfrage und gleichzeitigen Anfragen) und ist nicht für den produktiven Einsatz gedacht.

GitHub Models verwendet Azure AI Content Safety. Diese Filter können im Rahmen der GitHub Models-Erfahrung nicht deaktiviert werden. Wenn du Modelle über einen kostenpflichtigen Dienst nutzt, konfiguriere bitte deine Inhaltsfilter entsprechend deinen Anforderungen.

Dieser Dienst unterliegt den Pre-Release-Bedingungen von GitHub.

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache ist als maßgebliche Quelle zu betrachten. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.