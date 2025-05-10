<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "35bf81388ac6917277b8d9a0c39bdc70",
  "translation_date": "2025-05-09T19:08:49+00:00",
  "source_file": "md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md",
  "language_code": "hu"
}
-->
# **Hozd létre saját Visual Studio Code Chat Copilot Agent-ed Phi-3.5-tel a GitHub Models segítségével**

Használod a Visual Studio Code Copilotot? Különösen a Chatben különböző agenteket használhatsz, hogy javítsd a projektek létrehozásának, írásának és karbantartásának képességét a Visual Studio Code-ban. A Visual Studio Code egy API-t biztosít, amely lehetővé teszi cégek és egyének számára, hogy üzleti igényeik alapján különböző agenteket hozzanak létre, bővítve azok képességeit különféle sajátos területeken. Ebben a cikkben a GitHub Models **Phi-3.5-mini-instruct (128k)** és **Phi-3.5-vision-instruct (128k)** modelljeire fókuszálunk, hogy elkészítsd saját Visual Studio Code Agentedet.

## **A Phi-3.5-ről a GitHub Models-en**

Tudjuk, hogy a Phi-3/3.5-mini-instruct a Phi-3/3.5 családban erős kódértési és generálási képességekkel rendelkezik, és előnyökkel bír a Gemma-2-9b és Mistral-Nemo-12B-instruct-2407 modellekkel szemben.

![codegen](../../../../../../translated_images/codegen.eede87d45b849fd8738a7789f44ec3b81c4907d23eebd2b0e3dbd62c939c7cb9.hu.png)

A legfrissebb GitHub Models már elérhetővé teszi a Phi-3.5-mini-instruct (128k) és Phi-3.5-vision-instruct (128k) modelleket. A fejlesztők az OpenAI SDK, az Azure AI Inference SDK és a REST API segítségével érhetik el őket.

![gh](../../../../../../translated_images/gh.7fa589617baffe1b3f8a044fb29ee1b46f02645a47f3caa57d493768512b94e8.hu.png)

***Megjegyzés:*** Ajánlott az Azure AI Inference SDK használata, mert ez jobban tud váltani az Azure Model Catalog és a termelési környezet között.

Az alábbiakban a **Phi-3.5-mini-instruct (128k)** és a **Phi-3.5-vision-instruct (128k)** kódgenerálási szcenárióban elért eredményei láthatók a GitHub Models-zel való integráció után, és ezek szolgálnak az alábbi példák alapjául.

**Demo: GitHub Models Phi-3.5-mini-instruct (128k) kód generálása Prompt alapján** ([kattints ide](../../../../../../code/09.UpdateSamples/Aug/ghmodel_phi35_instruct_demo.ipynb))

**Demo: GitHub Models Phi-3.5-vision-instruct (128k) kód generálása kép alapján** ([kattints ide](../../../../../../code/09.UpdateSamples/Aug/ghmodel_phi35_vision_demo.ipynb))


## **A GitHub Copilot Chat Agent-ről**

A GitHub Copilot Chat Agent különböző feladatokat képes elvégezni különféle projekt szcenáriókban a kód alapján. A rendszer négy agentet tartalmaz: workspace, github, terminal, vscode

![agent](../../../../../../translated_images/agent.19ff410949975e96c38aa5763545604a33dc923968b6abcd200ff8590c62efd7.hu.png)

Az agent nevének '@' jellel való megadásával gyorsan elvégezheted a hozzá tartozó feladatokat. Vállalatok számára, ha üzleti igényekhez kapcsolódó tartalmakat, például követelményeket, kódolást, teszt specifikációkat és kiadást adsz hozzá, erősebb vállalati privát funkciókat érhetsz el a GitHub Copilot segítségével.

A Visual Studio Code Chat Agent most hivatalosan is kiadta API-ját, amely lehetővé teszi vállalatok vagy vállalati fejlesztők számára, hogy különböző szoftver üzleti ökoszisztémák alapján fejlesszenek agenteket. A Visual Studio Code Extension Development fejlesztési módjára építve könnyedén hozzáférhetsz a Visual Studio Code Chat Agent API interfészéhez. Ezen a folyamaton alapulhat a fejlesztés.

![diagram](../../../../../../translated_images/diagram.e17900e549fa305114e13994f4091c34860163aaff8e67d206550bfd01bcb004.hu.png)

A fejlesztési szcenárió támogatja harmadik féltől származó modell API-k (például GitHub Models, Azure Model Catalog, valamint nyílt forráskódú modellekre épülő saját szolgáltatások) elérését, és használhatóak a GitHub Copilot által biztosított gpt-35-turbo, gpt-4 és gpt-4o modellek is.

## **Agent hozzáadása @phicoding névvel Phi-3.5 alapján**

Megpróbáljuk integrálni a Phi-3.5 programozási képességeit, hogy kódírást, képgenerálás kódját és egyéb feladatokat elvégezzünk. Létrehozunk egy Phi-3.5 köré épülő Agentet - @PHI, a következő funkciókkal:

1. Önbemutató generálása a GitHub Copilot által biztosított GPT-4o alapján a **@phicoding /help** parancson keresztül

2. Különböző programozási nyelvekhez kód generálása a **Phi-3.5-mini-instruct (128k)** modell alapján a **@phicoding /gen** parancs segítségével

3. Kód generálása a **Phi-3.5-vision-instruct (128k)** és képalapú kiegészítés a **@phicoding /image** parancs által

![arch](../../../../../../translated_images/arch.c302d58012f0988b02f2275e24d8d21259899ef827d8a7579daecd1dd8b83ffd.hu.png)

## **Kapcsolódó lépések**

1. Telepítsd a Visual Studio Code Extension fejlesztési támogatást npm-mel

```bash

npm install --global yo generator-code 

```
2. Hozz létre egy Visual Studio Code Extension plugint (Typescript fejlesztési módban, neve phiext)

```bash

yo code 

```

3. Nyisd meg a létrehozott projektet és módosítsd a package.json fájlt. Itt találhatók a kapcsolódó utasítások és konfigurációk, valamint a GitHub Models konfigurációja. Figyelj rá, hogy ide kell beillesztened a GitHub Models tokenedet.

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

4. Módosítsd a src/extension.ts fájlt

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

6. Futtatás

***/help***

![help](../../../../../../translated_images/help.e26759fe1e92cea3e8788b2157e4383f621254ce001ba4ef6d35fce1e0667e55.hu.png)

***@phicoding /help***

![agenthelp](../../../../../../translated_images/agenthelp.f249f33c3fa449e0a779c78e3c2f3a65820702c03129e52a81a8df369443e413.hu.png)

***@phicoding /gen***

![agentgen](../../../../../../translated_images/agentgen.90c9cb76281be28a6cfdccda08f65043579ef4730a818c34e6f33ab6eb90e38c.hu.png)

***@phicoding /image***

![agentimage](../../../../../../translated_images/agentimage.db0cc3d3bd0ee494170ebd2623623e1012eb9f5786436439e2e36b91ca163172.hu.png)

A mintakód letölthető innen: [kattints ide](../../../../../../code/09.UpdateSamples/Aug/vscode)

## **Források**

1. Regisztráció a GitHub Models-re [https://gh.io/models](https://gh.io/models)

2. Ismerkedés a Visual Studio Code Extension fejlesztéssel [https://code.visualstudio.com/api/get-started/your-first-extension](https://code.visualstudio.com/api/get-started/your-first-extension)

3. Ismerkedés a Visual Studio Code Copilot Chat API-val [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat)

**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás [Co-op Translator](https://github.com/Azure/co-op-translator) használatával készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Kritikus információk esetén professzionális, emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy félreértelmezésekért.