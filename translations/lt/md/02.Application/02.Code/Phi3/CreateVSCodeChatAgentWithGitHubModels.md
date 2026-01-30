# **Sukurkite savo Visual Studio Code Chat Copilot Agentą su Phi-3.5 iš GitHub Models**

Ar naudojate Visual Studio Code Copilot? Ypač Chat funkcijoje, galite naudoti skirtingus agentus, kad pagerintumėte projektų kūrimo, rašymo ir palaikymo galimybes Visual Studio Code aplinkoje. Visual Studio Code suteikia API, leidžiantį įmonėms ir asmenims kurti skirtingus agentus pagal jų verslo poreikius, kad išplėstų galimybes įvairiose srityse. Šiame straipsnyje mes sutelksime dėmesį į **Phi-3.5-mini-instruct (128k)** ir **Phi-3.5-vision-instruct (128k)** iš GitHub Models, kad sukurtume savo Visual Studio Code Agentą.

## **Apie Phi-3.5 GitHub Models**

Žinome, kad Phi-3/3.5-mini-instruct iš Phi-3/3.5 šeimos turi stiprius kodo supratimo ir generavimo gebėjimus, kurie lenkia Gemma-2-9b ir Mistral-Nemo-12B-instruct-2407.

![codegen](../../../../../../imgs/02/phi35vscode/codegen.png)

Naujausi GitHub Models jau suteikia prieigą prie Phi-3.5-mini-instruct (128k) ir Phi-3.5-vision-instruct (128k) modelių. Kūrėjai gali juos pasiekti per OpenAI SDK, Azure AI Inference SDK ir REST API.

![gh](../../../../../../imgs/02/phi35vscode/gh.png)

***Pastaba:*** Rekomenduojama naudoti Azure AI Inference SDK, nes jis geriau suderinamas su Azure Model Catalog gamybos aplinkoje.

Toliau pateikiami **Phi-3.5-mini-instruct (128k)** ir **Phi-3.5-vision-instruct (128k)** rezultatai kodo generavimo scenarijuje po integracijos su GitHub Models, taip pat pasiruošimas tolesniems pavyzdžiams.

**Demo: GitHub Models Phi-3.5-mini-instruct (128k) generuoja kodą iš Prompt** ([spustelėkite šią nuorodą](../../../../../../code/09.UpdateSamples/Aug/ghmodel_phi35_instruct_demo.ipynb))

**Demo: GitHub Models Phi-3.5-vision-instruct (128k) generuoja kodą iš vaizdo** ([spustelėkite šią nuorodą](../../../../../../code/09.UpdateSamples/Aug/ghmodel_phi35_vision_demo.ipynb))

## **Apie GitHub Copilot Chat Agentą**

GitHub Copilot Chat Agent gali atlikti įvairias užduotis skirtinguose projektų scenarijuose, remdamasis kodu. Sistema turi keturis agentus: workspace, github, terminal, vscode.

![agent](../../../../../../imgs/02/phi35vscode/agent.png)

Pridėjus agento pavadinimą su „@“, galite greitai atlikti atitinkamą darbą. Įmonėms, jei pridėsite savo verslo susijusį turinį, pvz., reikalavimus, kodavimą, testavimo specifikacijas ir išleidimą, galite turėti galingesnes privačias funkcijas, pagrįstas GitHub Copilot.

Visual Studio Code Chat Agent dabar oficialiai išleido savo API, leidžiantį įmonėms ar įmonių kūrėjams kurti agentus pagal skirtingas programinės įrangos verslo ekosistemas. Remiantis Visual Studio Code Extension Development kūrimo metodu, galite lengvai pasiekti Visual Studio Code Chat Agent API sąsają. Galime kurti remdamiesi šiuo procesu.

![diagram](../../../../../../imgs/02/phi35vscode/diagram.png)

Kūrimo scenarijus gali palaikyti trečiųjų šalių modelių API (pvz., GitHub Models, Azure Model Catalog ir savarankiškai sukurtas paslaugas, pagrįstas atviraisiais modeliais) ir taip pat gali naudoti GitHub Copilot teikiamus gpt-35-turbo, gpt-4 ir gpt-4o modelius.

## **Pridėkite agentą @phicoding, pagrįstą Phi-3.5**

Bandome integruoti Phi-3.5 programavimo galimybes, kad atliktume kodo rašymą, vaizdų generavimą į kodą ir kitas užduotis. Sukurkite agentą, pagrįstą Phi-3.5 - @PHI, štai keletas funkcijų:

1. Sukurkite savęs pristatymą, naudodami GPT-4o, kurį teikia GitHub Copilot, per komandą **@phicoding /help**.

2. Generuokite kodą skirtingoms programavimo kalboms, naudodami **Phi-3.5-mini-instruct (128k)** per komandą **@phicoding /gen**.

3. Generuokite kodą, naudodami **Phi-3.5-vision-instruct (128k)** ir vaizdų užbaigimą per komandą **@phicoding /image**.

![arch](../../../../../../imgs/02/phi35vscode/arch.png)

## **Susiję žingsniai**

1. Įdiekite Visual Studio Code Extension kūrimo palaikymą, naudodami npm.

```bash

npm install --global yo generator-code 

```

2. Sukurkite Visual Studio Code Extension įskiepį (naudojant Typescript kūrimo režimą, pavadintą phiext).

```bash

yo code 

```

3. Atidarykite sukurtą projektą ir modifikuokite package.json. Čia pateikiamos susijusios instrukcijos ir konfigūracijos, taip pat GitHub Models konfigūracija. Atkreipkite dėmesį, kad čia reikia pridėti savo GitHub Models tokeną.

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

4. Modifikuokite src/extension.ts.

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

6. Paleidimas.

***/help***

![help](../../../../../../imgs/02/phi35vscode/help.png)

***@phicoding /help***

![agenthelp](../../../../../../imgs/02/phi35vscode/agenthelp.png)

***@phicoding /gen***

![agentgen](../../../../../../imgs/02/phi35vscode/agentgen.png)

***@phicoding /image***

![agentimage](../../../../../../imgs/02/phi35vscode/agentimage.png)

Galite atsisiųsti pavyzdinį kodą: [spustelėkite](../../../../../../code/09.UpdateSamples/Aug/vscode)

## **Ištekliai**

1. Registruokitės GitHub Models [https://gh.io/models](https://gh.io/models)

2. Sužinokite apie Visual Studio Code Extension kūrimą [https://code.visualstudio.com/api/get-started/your-first-extension](https://code.visualstudio.com/api/get-started/your-first-extension)

3. Sužinokite apie Visual Studio Code Copilot Chat API [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat)

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius naudojant šį vertimą.