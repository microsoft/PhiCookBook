<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5113634b77370af6790f9697d5d7de90",
  "translation_date": "2025-03-27T13:24:23+00:00",
  "source_file": "md\\02.QuickStart\\GitHubModel_QuickStart.md",
  "language_code": "fr"
}
-->
## Modèles GitHub - Bêta publique limitée

Bienvenue sur [GitHub Models](https://github.com/marketplace/models) ! Tout est prêt pour que vous exploriez les modèles d'IA hébergés sur Azure AI.

![GitHubModel](../../../../translated_images/GitHub_ModelCatalog.4fc858ab26afe64c43f5e423ad0c5c733878bb536fdb027a5bcf1f80c41b0633.fr.png)

Pour plus d'informations sur les modèles disponibles sur GitHub Models, consultez le [GitHub Model Marketplace](https://github.com/marketplace/models).

## Modèles disponibles

Chaque modèle dispose d'un espace de test dédié et de code d'exemple.

![Phi-3Model_Github](../../../../imgs/01/02/02/GitHub_ModelPlay.png)

### Modèles Phi-3 dans le catalogue des modèles GitHub

[Phi-3-Medium-128k-Instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-128k-instruct)

[Phi-3-medium-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-4k-instruct)

[Phi-3-mini-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-128k-instruct)

[Phi-3-mini-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-4k-instruct)

[Phi-3-small-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-128k-instruct)

[Phi-3-small-8k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-8k-instruct)

## Premiers pas

Quelques exemples de base sont prêts à être exécutés. Vous pouvez les trouver dans le répertoire des exemples. Si vous souhaitez passer directement à votre langage préféré, les exemples sont disponibles dans les langues suivantes :

- Python
- JavaScript
- cURL

Un environnement dédié Codespaces est également disponible pour exécuter les exemples et les modèles.

![Getting Started](../../../../translated_images/GitHub_ModelGetStarted.b4b839a081583da39bc976c2f0d8ac4603d3b8c23194b16cc9e0a1014f5611d0.fr.png)

## Code d'exemple

Voici des extraits de code pour quelques cas d'utilisation. Pour des informations supplémentaires sur le SDK Azure AI Inference, consultez la documentation complète et les exemples.

## Configuration

1. Créez un jeton d'accès personnel.  
Vous n'avez pas besoin de donner des permissions au jeton. Notez que le jeton sera envoyé à un service Microsoft.

Pour utiliser les extraits de code ci-dessous, créez une variable d'environnement pour définir votre jeton comme clé pour le code client.

Si vous utilisez bash :  
```
export GITHUB_TOKEN="<your-github-token-goes-here>"
```  
Si vous êtes sous PowerShell :  
```
$Env:GITHUB_TOKEN="<your-github-token-goes-here>"
```  

Si vous utilisez l'invite de commande Windows :  
```
set GITHUB_TOKEN=<your-github-token-goes-here>
```  

## Exemple Python

### Installer les dépendances  
Installez le SDK Azure AI Inference avec pip (Requis : Python >=3.8) :  
```
pip install azure-ai-inference
```  

### Exécuter un exemple de base  

Cet exemple démontre un appel de base à l'API de complétion de chat. Il utilise le point de terminaison d'inférence du modèle AI de GitHub et votre jeton GitHub. L'appel est synchrone.  

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

### Exécuter une conversation multi-tours  

Cet exemple démontre une conversation multi-tours avec l'API de complétion de chat. Lors de l'utilisation du modèle pour une application de chat, vous devrez gérer l'historique de cette conversation et envoyer les derniers messages au modèle.  

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

### Diffuser la sortie  

Pour une meilleure expérience utilisateur, vous souhaiterez diffuser la réponse du modèle afin que le premier token apparaisse rapidement et que vous évitiez d'attendre de longues réponses.  

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

### Installer les dépendances  

Installez Node.js.  

Copiez les lignes suivantes et enregistrez-les sous forme de fichier package.json dans votre dossier.  

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

Note : @azure/core-sse est uniquement nécessaire lorsque vous diffusez la réponse des complétions de chat.  

Ouvrez une fenêtre de terminal dans ce dossier et exécutez npm install.  

Pour chacun des extraits de code ci-dessous, copiez le contenu dans un fichier sample.js et exécutez-le avec node sample.js.  

### Exécuter un exemple de base  

Cet exemple démontre un appel de base à l'API de complétion de chat. Il utilise le point de terminaison d'inférence du modèle AI de GitHub et votre jeton GitHub. L'appel est synchrone.  

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

### Exécuter une conversation multi-tours  

Cet exemple démontre une conversation multi-tours avec l'API de complétion de chat. Lors de l'utilisation du modèle pour une application de chat, vous devrez gérer l'historique de cette conversation et envoyer les derniers messages au modèle.  

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

### Diffuser la sortie  
Pour une meilleure expérience utilisateur, vous souhaiterez diffuser la réponse du modèle afin que le premier token apparaisse rapidement et que vous évitiez d'attendre de longues réponses.  

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

### Exécuter un exemple de base  

Collez le texte suivant dans un shell :  

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

### Exécuter une conversation multi-tours  

Appelez l'API de complétion de chat et passez l'historique du chat :  

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

### Diffuser la sortie  

Voici un exemple d'appel du point de terminaison et de diffusion de la réponse.  

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

## Utilisation GRATUITE et limites de taux pour les modèles GitHub  

![Model Catalog](../../../../translated_images/GitHub_Model.0c2abb992151c5407046e2b763af51505ff709f04c0950785e0300fdc8c55a0c.fr.png)  

Les [limites de taux pour l'espace de test et l'utilisation gratuite de l'API](https://docs.github.com/en/github-models/prototyping-with-ai-models#rate-limits) sont conçues pour vous aider à expérimenter avec les modèles et à créer un prototype de votre application d'IA. Pour une utilisation au-delà de ces limites et pour passer à l'échelle avec votre application, vous devez provisionner des ressources à partir d'un compte Azure et vous authentifier depuis ce compte plutôt que d'utiliser votre jeton d'accès personnel GitHub. Vous n'avez rien d'autre à modifier dans votre code. Utilisez ce lien pour découvrir comment dépasser les limites de la version gratuite dans Azure AI.

### Divulgations  

Rappelez-vous qu'en interagissant avec un modèle, vous expérimentez avec l'IA, donc des erreurs de contenu sont possibles.  

Cette fonctionnalité est soumise à diverses limites (y compris les requêtes par minute, les requêtes par jour, les tokens par requête et les requêtes simultanées) et n'est pas conçue pour des cas d'utilisation en production.  

GitHub Models utilise Azure AI Content Safety. Ces filtres ne peuvent pas être désactivés dans le cadre de l'expérience GitHub Models. Si vous décidez d'utiliser des modèles via un service payant, veuillez configurer vos filtres de contenu selon vos besoins.  

Ce service est soumis aux conditions préalables de GitHub.  

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatisée [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des imprécisions. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.