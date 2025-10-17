<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "35bf81388ac6917277b8d9a0c39bdc70",
  "translation_date": "2025-10-11T11:54:34+00:00",
  "source_file": "md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md",
  "language_code": "et"
}
-->
# **Loo oma Visual Studio Code Chat Copilot Agent Phi-3.5 abil GitHub Modelsiga**

Kas kasutad Visual Studio Code Copilotit? Eriti Chatis, kus saad kasutada erinevaid agente, et parandada projektide loomise, kirjutamise ja haldamise võimekust Visual Studio Codes. Visual Studio Code pakub API-d, mis võimaldab ettevõtetel ja üksikisikutel luua erinevaid agente vastavalt oma ärivajadustele, et laiendada nende võimekust erinevates valdkondades. Selles artiklis keskendume **Phi-3.5-mini-instruct (128k)** ja **Phi-3.5-vision-instruct (128k)** mudelitele GitHub Modelsist, et luua oma Visual Studio Code Agent.

## **Phi-3.5 kohta GitHub Modelsis**

Phi-3/3.5-mini-instruct mudel Phi-3/3.5 perekonnast on tuntud oma tugeva koodimõistmise ja genereerimise võime poolest ning omab eeliseid Gemma-2-9b ja Mistral-Nemo-12B-instruct-2407 mudelite ees.

![codegen](../../../../../../imgs/02/phi35vscode/codegen.png)

Viimased GitHub Models mudelid pakuvad juba juurdepääsu Phi-3.5-mini-instruct (128k) ja Phi-3.5-vision-instruct (128k) mudelitele. Arendajad saavad neile ligi OpenAI SDK, Azure AI Inference SDK ja REST API kaudu.

![gh](../../../../../../imgs/02/phi35vscode/gh.png)

***Märkus:*** Siin on soovitatav kasutada Azure AI Inference SDK-d, kuna see võimaldab paremini integreeruda Azure Model Catalogiga tootmiskeskkonnas.

Allpool on toodud **Phi-3.5-mini-instruct (128k)** ja **Phi-3.5-vision-instruct (128k)** tulemused koodigeneratsiooni stsenaariumis pärast GitHub Modelsiga ühendamist, mis valmistab ette järgmised näited.

**Demo: GitHub Models Phi-3.5-mini-instruct (128k) genereerib koodi Prompti põhjal** ([klõpsa siia lingile](../../../../../../code/09.UpdateSamples/Aug/ghmodel_phi35_instruct_demo.ipynb))

**Demo: GitHub Models Phi-3.5-vision-instruct (128k) genereerib koodi pildi põhjal** ([klõpsa siia lingile](../../../../../../code/09.UpdateSamples/Aug/ghmodel_phi35_vision_demo.ipynb))

## **GitHub Copilot Chat Agendi kohta**

GitHub Copilot Chat Agent suudab täita erinevaid ülesandeid erinevates projektistsenaariumides koodi põhjal. Süsteemil on neli agenti: workspace, github, terminal, vscode.

![agent](../../../../../../imgs/02/phi35vscode/agent.png)

Lisades agendi nime koos '@'-märgiga, saad kiiresti täita vastava töö. Ettevõtetele, kui lisada oma äriga seotud sisu, nagu nõuded, koodimine, testispetsifikatsioonid ja väljalasked, on võimalik luua võimsamaid ettevõtte privaatfunktsioone GitHub Copiloti põhjal.

Visual Studio Code Chat Agent on nüüd ametlikult välja andnud oma API, mis võimaldab ettevõtetel või ettevõtte arendajatel arendada agente vastavalt erinevatele tarkvara äriekosüsteemidele. Visual Studio Code Extension Development meetodi abil saab hõlpsasti ligi Visual Studio Code Chat Agent API-le. Arendust saab teha järgmist protsessi järgides.

![diagram](../../../../../../imgs/02/phi35vscode/diagram.png)

Arendusstsenaarium toetab juurdepääsu kolmanda osapoole mudelite API-dele (näiteks GitHub Models, Azure Model Catalog ja avatud lähtekoodiga mudelitele tuginevad iseteeninduslikud teenused) ning samuti saab kasutada GitHub Copiloti pakutavaid gpt-35-turbo, gpt-4 ja gpt-4o mudeleid.

## **Lisa agent @phicoding Phi-3.5 põhjal**

Proovime integreerida Phi-3.5 programmeerimisvõimekust, et täita koodi kirjutamise, pildigeneratsiooni ja muid ülesandeid. Loome Phi-3.5 ümber ehitatud agendi - @PHI. Järgnevalt on toodud mõned funktsioonid:

1. Genereeri enese tutvustus GitHub Copiloti pakutava GPT-4o abil **@phicoding /help** käsu kaudu.

2. Genereeri koodi erinevates programmeerimiskeeltes **Phi-3.5-mini-instruct (128k)** abil **@phicoding /gen** käsu kaudu.

3. Genereeri koodi **Phi-3.5-vision-instruct (128k)** ja pilditäienduse põhjal **@phicoding /image** käsu kaudu.

![arch](../../../../../../imgs/02/phi35vscode/arch.png)

## **Seotud sammud**

1. Paigalda Visual Studio Code Extension arendustugi npm-i abil.

```bash

npm install --global yo generator-code 

```
2. Loo Visual Studio Code Extension plugin (kasutades Typescripti arendusrežiimi, nimega phiext).

```bash

yo code 

```

3. Ava loodud projekt ja muuda package.json faili. Siin on seotud juhised ja konfiguratsioonid, samuti GitHub Models konfiguratsioon. Pane tähele, et siia tuleb lisada oma GitHub Models token.

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

4. Muuda src/extension.ts faili.

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

6. Käivita.

***/help***

![help](../../../../../../imgs/02/phi35vscode/help.png)

***@phicoding /help***

![agenthelp](../../../../../../imgs/02/phi35vscode/agenthelp.png)

***@phicoding /gen***

![agentgen](../../../../../../imgs/02/phi35vscode/agentgen.png)

***@phicoding /image***

![agentimage](../../../../../../imgs/02/phi35vscode/agentimage.png)

Saad alla laadida näidiskoodi: [klõpsa siia](../../../../../../code/09.UpdateSamples/Aug/vscode)

## **Ressursid**

1. Registreeru GitHub Models [https://gh.io/models](https://gh.io/models)

2. Õpi Visual Studio Code Extension arendust [https://code.visualstudio.com/api/get-started/your-first-extension](https://code.visualstudio.com/api/get-started/your-first-extension)

3. Tutvu Visual Studio Code Copilot Chat API-ga [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat)

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.