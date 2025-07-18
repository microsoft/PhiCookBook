<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5113634b77370af6790f9697d5d7de90",
  "translation_date": "2025-07-17T05:36:54+00:00",
  "source_file": "md/02.QuickStart/GitHubModel_QuickStart.md",
  "language_code": "el"
}
-->
## GitHub Models - Περιορισμένη Δημόσια Beta

Καλώς ήρθατε στα [GitHub Models](https://github.com/marketplace/models)! Έχουμε όλα έτοιμα για να εξερευνήσετε τα AI Models που φιλοξενούνται στο Azure AI.

![GitHubModel](../../../../translated_images/GitHub_ModelCatalog.aa43c51c36454747ca1cc1ffa799db02cc66b4fb7e8495311701adb072442df8.el.png)

Για περισσότερες πληροφορίες σχετικά με τα διαθέσιμα Models στο GitHub Models, δείτε το [GitHub Model Marketplace](https://github.com/marketplace/models)

## Διαθέσιμα Models

Κάθε μοντέλο έχει το δικό του playground και δείγματα κώδικα

![Phi-3Model_Github](../../../../imgs/01/02/02/GitHub_ModelPlay.png)

### Phi-3 Models στο GitHub Model Catalog

[Phi-3-Medium-128k-Instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-128k-instruct)

[Phi-3-medium-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-medium-4k-instruct)

[Phi-3-mini-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-128k-instruct)

[Phi-3-mini-4k-instruct](https://github.com/marketplace/models/azureml/Phi-3-mini-4k-instruct)

[Phi-3-small-128k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-128k-instruct)

[Phi-3-small-8k-instruct](https://github.com/marketplace/models/azureml/Phi-3-small-8k-instruct)

## Ξεκινώντας

Υπάρχουν μερικά βασικά παραδείγματα έτοιμα για εκτέλεση. Μπορείτε να τα βρείτε στον φάκελο samples. Αν θέλετε να μεταβείτε απευθείας στη γλώσσα που προτιμάτε, τα παραδείγματα είναι διαθέσιμα στις εξής γλώσσες:

- Python
- JavaScript
- cURL

Υπάρχει επίσης ένα ειδικό περιβάλλον Codespaces για την εκτέλεση των δειγμάτων και των μοντέλων.

![Getting Started](../../../../translated_images/GitHub_ModelGetStarted.150220a802da6fb67944ad93c1a4c7b8a9811e43d77879a149ecf54c02928c6b.el.png)

## Δείγματα Κώδικα

Παρακάτω θα βρείτε παραδείγματα κώδικα για μερικές περιπτώσεις χρήσης. Για περισσότερες πληροφορίες σχετικά με το Azure AI Inference SDK, δείτε την πλήρη τεκμηρίωση και τα δείγματα.

## Ρύθμιση

1. Δημιουργήστε ένα προσωπικό access token  
Δεν χρειάζεται να δώσετε δικαιώματα στο token. Σημειώστε ότι το token θα αποσταλεί σε υπηρεσία της Microsoft.

Για να χρησιμοποιήσετε τα παρακάτω αποσπάσματα κώδικα, δημιουργήστε μια μεταβλητή περιβάλλοντος όπου θα ορίσετε το token σας ως κλειδί για τον κώδικα του client.

Αν χρησιμοποιείτε bash:  
```
export GITHUB_TOKEN="<your-github-token-goes-here>"
```  
Αν βρίσκεστε σε powershell:  

```
$Env:GITHUB_TOKEN="<your-github-token-goes-here>"
```  

Αν χρησιμοποιείτε Windows command prompt:  

```
set GITHUB_TOKEN=<your-github-token-goes-here>
```  

## Παράδειγμα Python

### Εγκατάσταση εξαρτήσεων  
Εγκαταστήστε το Azure AI Inference SDK με pip (Απαιτείται: Python >=3.8):

```
pip install azure-ai-inference
```  
### Εκτέλεση βασικού παραδείγματος κώδικα

Αυτό το παράδειγμα δείχνει μια βασική κλήση στο chat completion API. Χρησιμοποιεί το endpoint inference του GitHub AI μοντέλου και το GitHub token σας. Η κλήση είναι συγχρονισμένη.

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

### Εκτέλεση συνομιλίας πολλαπλών γύρων

Αυτό το παράδειγμα δείχνει μια συνομιλία πολλαπλών γύρων με το chat completion API. Όταν χρησιμοποιείτε το μοντέλο για εφαρμογή συνομιλίας, πρέπει να διαχειρίζεστε το ιστορικό της συνομιλίας και να στέλνετε τα πιο πρόσφατα μηνύματα στο μοντέλο.

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

### Ροή εξόδου

Για καλύτερη εμπειρία χρήστη, θα θέλετε να κάνετε streaming την απάντηση του μοντέλου ώστε το πρώτο token να εμφανίζεται νωρίς και να αποφύγετε την αναμονή για μεγάλες απαντήσεις.

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

### Εγκατάσταση εξαρτήσεων

Εγκαταστήστε το Node.js.

Αντιγράψτε τις παρακάτω γραμμές κειμένου και αποθηκεύστε τις σε ένα αρχείο package.json μέσα στο φάκελό σας.

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

Σημείωση: Το @azure/core-sse χρειάζεται μόνο όταν κάνετε streaming των απαντήσεων chat completions.

Ανοίξτε ένα τερματικό σε αυτόν το φάκελο και τρέξτε npm install.

Για κάθε απόσπασμα κώδικα παρακάτω, αντιγράψτε το περιεχόμενο σε ένα αρχείο sample.js και τρέξτε το με node sample.js.

### Εκτέλεση βασικού παραδείγματος κώδικα

Αυτό το παράδειγμα δείχνει μια βασική κλήση στο chat completion API. Χρησιμοποιεί το endpoint inference του GitHub AI μοντέλου και το GitHub token σας. Η κλήση είναι συγχρονισμένη.

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

### Εκτέλεση συνομιλίας πολλαπλών γύρων

Αυτό το παράδειγμα δείχνει μια συνομιλία πολλαπλών γύρων με το chat completion API. Όταν χρησιμοποιείτε το μοντέλο για εφαρμογή συνομιλίας, πρέπει να διαχειρίζεστε το ιστορικό της συνομιλίας και να στέλνετε τα πιο πρόσφατα μηνύματα στο μοντέλο.

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

### Ροή εξόδου  
Για καλύτερη εμπειρία χρήστη, θα θέλετε να κάνετε streaming την απάντηση του μοντέλου ώστε το πρώτο token να εμφανίζεται νωρίς και να αποφύγετε την αναμονή για μεγάλες απαντήσεις.

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

### Εκτέλεση βασικού παραδείγματος κώδικα

Επικολλήστε τα παρακάτω σε ένα shell:

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
### Εκτέλεση συνομιλίας πολλαπλών γύρων

Καλέστε το chat completion API και περάστε το ιστορικό συνομιλίας:

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
### Ροή εξόδου

Αυτό είναι ένα παράδειγμα κλήσης του endpoint με streaming της απάντησης.

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

## Δωρεάν Χρήση και Όρια Ροής για τα GitHub Models

![Model Catalog](../../../../translated_images/GitHub_Model.ca6c125cb3117d0ea7c2e204b066ee4619858d28e7b1a419c262443c5e9a2d5b.el.png)

Τα [όρια ροής για το playground και τη δωρεάν χρήση API](https://docs.github.com/en/github-models/prototyping-with-ai-models#rate-limits) έχουν σχεδιαστεί για να σας βοηθήσουν να πειραματιστείτε με τα μοντέλα και να δημιουργήσετε πρωτότυπα για την AI εφαρμογή σας. Για χρήση πέρα από αυτά τα όρια, και για να κλιμακώσετε την εφαρμογή σας, πρέπει να προμηθευτείτε πόρους από έναν λογαριασμό Azure και να κάνετε authentication από εκεί αντί για το προσωπικό σας GitHub access token. Δεν χρειάζεται να αλλάξετε τίποτα άλλο στον κώδικά σας. Χρησιμοποιήστε αυτόν τον σύνδεσμο για να μάθετε πώς να ξεπεράσετε τα όρια της δωρεάν βαθμίδας στο Azure AI.

### Αποκαλύψεις

Να θυμάστε ότι όταν αλληλεπιδράτε με ένα μοντέλο, πειραματίζεστε με AI, οπότε είναι πιθανό να υπάρχουν λάθη στο περιεχόμενο.

Η λειτουργία υπόκειται σε διάφορα όρια (συμπεριλαμβανομένων αιτημάτων ανά λεπτό, αιτημάτων ανά ημέρα, tokens ανά αίτημα και ταυτόχρονων αιτημάτων) και δεν έχει σχεδιαστεί για παραγωγικές χρήσεις.

Τα GitHub Models χρησιμοποιούν το Azure AI Content Safety. Αυτά τα φίλτρα δεν μπορούν να απενεργοποιηθούν ως μέρος της εμπειρίας GitHub Models. Αν αποφασίσετε να χρησιμοποιήσετε μοντέλα μέσω πληρωμένης υπηρεσίας, παρακαλούμε ρυθμίστε τα φίλτρα περιεχομένου ώστε να καλύπτουν τις ανάγκες σας.

Αυτή η υπηρεσία λειτουργεί υπό τους Όρους Προ-κυκλοφορίας (Pre-release Terms) του GitHub.

**Αποποίηση ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που επιδιώκουμε την ακρίβεια, παρακαλούμε να γνωρίζετε ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη γλώσσα του θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.