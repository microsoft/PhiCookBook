<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "35bf81388ac6917277b8d9a0c39bdc70",
  "translation_date": "2025-07-17T03:26:53+00:00",
  "source_file": "md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md",
  "language_code": "da"
}
-->
# **Opret din egen Visual Studio Code Chat Copilot Agent med Phi-3.5 fra GitHub Models**

Bruger du Visual Studio Code Copilot? Især i Chat kan du bruge forskellige agenter til at forbedre evnen til at skabe, skrive og vedligeholde projekter i Visual Studio Code. Visual Studio Code tilbyder en API, som gør det muligt for virksomheder og enkeltpersoner at skabe forskellige agenter baseret på deres forretning for at udvide deres kapaciteter inden for forskellige proprietære områder. I denne artikel vil vi fokusere på **Phi-3.5-mini-instruct (128k)** og **Phi-3.5-vision-instruct (128k)** fra GitHub Models for at skabe din egen Visual Studio Code Agent.

## **Om Phi-3.5 på GitHub Models**

Vi ved, at Phi-3/3.5-mini-instruct i Phi-3/3.5-familien har stærke evner inden for kodeforståelse og generering, og har fordele i forhold til Gemma-2-9b og Mistral-Nemo-12B-instruct-2407.

![codegen](../../../../../../translated_images/da/codegen.53be1150ee54d969.png)

De nyeste GitHub Models giver allerede adgang til Phi-3.5-mini-instruct (128k) og Phi-3.5-vision-instruct (128k) modellerne. Udviklere kan tilgå dem via OpenAI SDK, Azure AI Inference SDK og REST API.

![gh](../../../../../../translated_images/da/gh.459640c7ceba01d5.png)

***Note:*** Det anbefales at bruge Azure AI Inference SDK her, da det bedre kan skifte mellem Azure Model Catalog i produktionsmiljøet.

Følgende er resultaterne af **Phi-3.5-mini-instruct (128k)** og **Phi-3.5-vision-instruct (128k)** i kodegenereringsscenariet efter integration med GitHub Models, og forbereder også de følgende eksempler.

**Demo: GitHub Models Phi-3.5-mini-instruct (128k) genererer kode fra Prompt** ([klik på dette link](../../../../../../code/09.UpdateSamples/Aug/ghmodel_phi35_instruct_demo.ipynb))

**Demo: GitHub Models Phi-3.5-vision-instruct (128k) genererer kode fra billede** ([klik på dette link](../../../../../../code/09.UpdateSamples/Aug/ghmodel_phi35_vision_demo.ipynb))


## **Om GitHub Copilot Chat Agent**

GitHub Copilot Chat Agent kan udføre forskellige opgaver i forskellige projektscenarier baseret på koden. Systemet har fire agenter: workspace, github, terminal, vscode

![agent](../../../../../../translated_images/da/agent.3dbb06228f9a6189.png)

Ved at tilføje agentens navn med ‘@’ kan du hurtigt udføre det tilsvarende arbejde. For virksomheder, hvis du tilføjer dit eget forretningsrelaterede indhold som krav, kodning, test specifikationer og release, kan du få mere kraftfulde private virksomhedsfunktioner baseret på GitHub Copilot.

Visual Studio Code Chat Agent har nu officielt frigivet sin API, hvilket gør det muligt for virksomheder eller virksomheders udviklere at udvikle agenter baseret på forskellige softwareforretningsekosystemer. Baseret på udviklingsmetoden Visual Studio Code Extension Development kan du nemt tilgå interfacet til Visual Studio Code Chat Agent API. Vi kan udvikle baseret på denne proces.

![diagram](../../../../../../translated_images/da/diagram.ca70d2866762f115.png)

Udviklingsscenariet kan understøtte adgang til tredjeparts model-API’er (såsom GitHub Models, Azure Model Catalog og selvbyggede tjenester baseret på open source-modeller) og kan også bruge gpt-35-turbo, gpt-4 og gpt-4o modellerne leveret af GitHub Copilot.

## **Tilføj en Agent @phicoding baseret på Phi-3.5**

Vi forsøger at integrere programmeringsevnerne i Phi-3.5 til at udføre kode skrivning, billedgenerering af kode og andre opgaver. Fuldfør en Agent bygget omkring Phi-3.5 - @PHI, følgende er nogle funktioner:

1. Generer en selvintroduktion baseret på GPT-4o leveret af GitHub Copilot via **@phicoding /help** kommandoen

2. Generer kode til forskellige programmeringssprog baseret på **Phi-3.5-mini-instruct (128k)** via **@phicoding /gen** kommandoen

3. Generer kode baseret på **Phi-3.5-vision-instruct (128k)** og billedkomplettering via **@phicoding /image** kommandoen

![arch](../../../../../../translated_images/da/arch.5a58a0adfa959a2d.png)

## **Relaterede trin**

1. Installer Visual Studio Code Extension udviklingssupport ved hjælp af npm

```bash

npm install --global yo generator-code 

```
2. Opret en Visual Studio Code Extension plugin (brug Typescript udviklingstilstand, navngivet phiext)

```bash

yo code 

```

3. Åbn det oprettede projekt og rediger package.json. Her er de relaterede instruktioner og konfigurationer samt konfigurationen af GitHub Models. Bemærk, at du skal tilføje din GitHub Models token her.

```json

{
  "name": "phiext",
  "displayName": "phiext",
  "description": "",
  "version": "0.0.1",
  "engines": {
    "vscode": "^1.93.0"
  },
  "categories": [
    "AI",
    "Chat"
  ],
  "activationEvents": [],
  "enabledApiProposals": [
      "chatVariableResolver"
  ],
  "main": "./dist/extension.js",
  "contributes": {
    "chatParticipants": [
        {
            "id": "chat.phicoding",
            "name": "phicoding",
            "description": "Hey! I am Microsoft Phi-3.5, She can help me with coding problems, such as generation code with your natural language, or even generation code about chart from images. Just ask me anything!",
            "isSticky": true,
            "commands": [
                {
                    "name": "help",
                    "description": "Introduce myself to you"
                },
                {
                    "name": "gen",
                    "description": "Generate code for you with Microsoft Phi-3.5-mini-instruct"
                },
                {
                    "name": "image",
                    "description": "Generate code for chart from image(png or jpg) with Microsoft Phi-3.5-vision-instruct, please add image url like this : https://ajaytech.co/wp-content/uploads/2019/09/index.png"
                }
            ]
        }
    ],
    "commands": [
        {
            "command": "phicoding.namesInEditor",
            "title": "Use Microsoft Phi 3.5 in Editor"
        }
    ],
    "configuration": {
      "type": "object",
      "title": "githubmodels",
      "properties": {
        "githubmodels.endpoint": {
          "type": "string",
          "default": "https://models.inference.ai.azure.com",
          "description": "Your GitHub Models Endpoint",
          "order": 0
        },
        "githubmodels.api_key": {
          "type": "string",
          "default": "Your GitHub Models Token",
          "description": "Your GitHub Models Token",
          "order": 1
        },
        "githubmodels.phi35instruct": {
          "type": "string",
          "default": "Phi-3.5-mini-instruct",
          "description": "Your Phi-35-Instruct Model",
          "order": 2
        },
        "githubmodels.phi35vision": {
          "type": "string",
          "default": "Phi-3.5-vision-instruct",
          "description": "Your Phi-35-Vision Model",
          "order": 3
        }
      }
    }
  },
  "scripts": {
    "vscode:prepublish": "npm run package",
    "compile": "webpack",
    "watch": "webpack --watch",
    "package": "webpack --mode production --devtool hidden-source-map",
    "compile-tests": "tsc -p . --outDir out",
    "watch-tests": "tsc -p . -w --outDir out",
    "pretest": "npm run compile-tests && npm run compile && npm run lint",
    "lint": "eslint src",
    "test": "vscode-test"
  },
  "devDependencies": {
    "@types/vscode": "^1.93.0",
    "@types/mocha": "^10.0.7",
    "@types/node": "20.x",
    "@typescript-eslint/eslint-plugin": "^8.3.0",
    "@typescript-eslint/parser": "^8.3.0",
    "eslint": "^9.9.1",
    "typescript": "^5.5.4",
    "ts-loader": "^9.5.1",
    "webpack": "^5.94.0",
    "webpack-cli": "^5.1.4",
    "@vscode/test-cli": "^0.0.10",
    "@vscode/test-electron": "^2.4.1"
  },
  "dependencies": {
    "@types/node-fetch": "^2.6.11",
    "node-fetch": "^3.3.2",
    "@azure-rest/ai-inference": "latest",
    "@azure/core-auth": "latest",
    "@azure/core-sse": "latest"
  }
}


```

4. Rediger src/extension.ts

```typescript

// The module 'vscode' contains the VS Code extensibility API
// Import the module and reference it with the alias vscode in your code below
import * as vscode from 'vscode';
import ModelClient from "@azure-rest/ai-inference";
import { AzureKeyCredential } from "@azure/core-auth";


interface IPhiChatResult extends vscode.ChatResult {
    metadata: {
        command: string;
    };
}


const MODEL_SELECTOR: vscode.LanguageModelChatSelector = { vendor: 'copilot', family: 'gpt-4o' };

function isValidImageUrl(url: string): boolean {
    const regex = /^(https?:\/\/.*\.(?:png|jpg))$/i;
    return regex.test(url);
}
  

// This method is called when your extension is activated
// Your extension is activated the very first time the command is executed
export function activate(context: vscode.ExtensionContext) {

    const codinghandler: vscode.ChatRequestHandler = async (request: vscode.ChatRequest, context: vscode.ChatContext, stream: vscode.ChatResponseStream, token: vscode.CancellationToken): Promise<IPhiChatResult> => {


        const config : any = vscode.workspace.getConfiguration('githubmodels');
        const endPoint: string = config.get('endpoint');
        const apiKey: string = config.get('api_key');
        const phi35instruct: string = config.get('phi35instruct');
        const phi35vision: string = config.get('phi35vision');
        
        if (request.command === 'help') {

            const content = "Welcome to Coding assistant with Microsoft Phi-3.5"; 
            stream.progress(content);


            try {
                const [model] = await vscode.lm.selectChatModels(MODEL_SELECTOR);
                if (model) {
                    const messages = [
                        vscode.LanguageModelChatMessage.User("Please help me express this content in a humorous way: I am a programming assistant who can help you convert natural language into code and generate code based on the charts in the images. output format like this : Hey I am Phi ......")
                    ];
                    const chatResponse = await model.sendRequest(messages, {}, token);
                    for await (const fragment of chatResponse.text) {
                        stream.markdown(fragment);
                    }
                }
            } catch(err) {
                console.log(err);
            }


            return { metadata: { command: 'help' } };

        }

        
        if (request.command === 'gen') {

            const content = "Welcome to use phi-3.5 to generate code";

            stream.progress(content);

            const client = new ModelClient(endPoint, new AzureKeyCredential(apiKey));

            const response = await client.path("/chat/completions").post({
              body: {
                messages: [
                  { role:"system", content: "You are a coding assistant.Help answer all code generation questions." },
                  { role:"user", content: request.prompt }
                ],
                model: phi35instruct,
                temperature: 0.4,
                max_tokens: 1000,
                top_p: 1.
              }
            });

            stream.markdown(response.body.choices[0].message.content);

            return { metadata: { command: 'gen' } };

        }



        
        if (request.command === 'image') {


            const content = "Welcome to use phi-3.5 to generate code from image(png or jpg),image url like this:https://ajaytech.co/wp-content/uploads/2019/09/index.png";

            stream.progress(content);

            if (!isValidImageUrl(request.prompt)) {
                stream.markdown('Please provide a valid image URL');
                return { metadata: { command: 'image' } };
            }
            else
            {

                const client = new ModelClient(endPoint, new AzureKeyCredential(apiKey));
    
                const response = await client.path("/chat/completions").post({
                    body: {
                      messages: [
                        { role: "system", content: "You are a helpful assistant that describes images in details." },
                        { role: "user", content: [
                            { type: "text", text: "Please generate code according to the chart in the picture according to the following requirements\n1. Keep all information in the chart, including data and text\n2. Do not generate additional information that is not included in the chart\n3. Please extract data from the picture, do not generate it from csv\n4. Please save the regenerated chart as a chart and save it to ./output/demo.png"},
                            { type: "image_url", image_url: {url: request.prompt}
                            }
                          ]
                        }
                      ],
                      model: phi35vision,
                      temperature: 0.4,
                      max_tokens: 2048,
                      top_p: 1.
                    }
                  });
    
                
                stream.markdown(response.body.choices[0].message.content);
    
                return { metadata: { command: 'image' } };
            }



        }


        return { metadata: { command: '' } };
    };


    const phi_ext = vscode.chat.createChatParticipant("chat.phicoding", codinghandler);

    phi_ext.iconPath = new vscode.ThemeIcon('sparkle');


    phi_ext.followupProvider = {
        provideFollowups(result: IPhiChatResult, context: vscode.ChatContext, token: vscode.CancellationToken) {
            return [{
                prompt: 'Let us coding with Phi-3.5 😋😋😋😋',
                label: vscode.l10n.t('Enjoy coding with Phi-3.5'),
                command: 'help'
            } satisfies vscode.ChatFollowup];
        }
    };

    context.subscriptions.push(phi_ext);
}

// This method is called when your extension is deactivated
export function deactivate() {}


```

6. Kørsel

***/help***

![help](../../../../../../translated_images/da/help.04c134d2bf9a9541.png)

***@phicoding /help***

![agenthelp](../../../../../../translated_images/da/agenthelp.60c68767c941a3fe.png)

***@phicoding /gen***

![agentgen](../../../../../../translated_images/da/agentgen.a16e7735790f764b.png)

***@phicoding /image***

![agentimage](../../../../../../translated_images/da/agentimage.f5cb52b45ab7d0d1.png)

Du kan downloade eksempel kode: [klik her](../../../../../../code/09.UpdateSamples/Aug/vscode)

## **Ressourcer**

1. Tilmeld dig GitHub Models [https://gh.io/models](https://gh.io/models)

2. Lær Visual Studio Code Extension Development [https://code.visualstudio.com/api/get-started/your-first-extension](https://code.visualstudio.com/api/get-started/your-first-extension)

3. Lær om Visual Studio Code Copilot Chat API [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat)

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.