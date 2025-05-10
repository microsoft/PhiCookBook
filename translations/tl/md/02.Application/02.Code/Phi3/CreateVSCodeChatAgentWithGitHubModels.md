<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "35bf81388ac6917277b8d9a0c39bdc70",
  "translation_date": "2025-05-09T19:08:23+00:00",
  "source_file": "md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md",
  "language_code": "tl"
}
-->
# **Lumikha ng sarili mong Visual Studio Code Chat Copilot Agent gamit ang Phi-3.5 mula sa GitHub Models**

Gumagamit ka ba ng Visual Studio Code Copilot? Lalo na sa Chat, maaari kang gumamit ng iba't ibang agents upang mapabuti ang kakayahan sa paggawa, pagsulat, at pagpapanatili ng mga proyekto sa Visual Studio Code. Nagbibigay ang Visual Studio Code ng API na nagpapahintulot sa mga kumpanya at indibidwal na lumikha ng iba't ibang agents base sa kanilang negosyo upang mapalawak ang kanilang kakayahan sa iba't ibang espesyalisadong larangan. Sa artikulong ito, tututukan natin ang **Phi-3.5-mini-instruct (128k)** at **Phi-3.5-vision-instruct (128k)** mula sa GitHub Models upang makagawa ng sarili mong Visual Studio Code Agent.

## **Tungkol sa Phi-3.5 sa GitHub Models**

Alam natin na ang Phi-3/3.5-mini-instruct sa Phi-3/3.5 Family ay may malakas na kakayahan sa pag-unawa at paggawa ng code, at may mga kalamangan kumpara sa Gemma-2-9b at Mistral-Nemo-12B-instruct-2407.

![codegen](../../../../../../translated_images/codegen.eede87d45b849fd8738a7789f44ec3b81c4907d23eebd2b0e3dbd62c939c7cb9.tl.png)

Ang pinakabagong GitHub Models ay nagbibigay na ng access sa Phi-3.5-mini-instruct (128k) at Phi-3.5-vision-instruct (128k) na mga modelo. Maaaring ma-access ito ng mga developer sa pamamagitan ng OpenAI SDK, Azure AI Inference SDK, at REST API.

![gh](../../../../../../translated_images/gh.7fa589617baffe1b3f8a044fb29ee1b46f02645a47f3caa57d493768512b94e8.tl.png)

***Note: *** Mas inirerekomenda ang paggamit ng Azure AI Inference SDK dito, dahil mas maganda ang pag-switch nito sa Azure Model Catalog sa production environment

Narito ang mga resulta ng **Phi-3.5-mini-instruct (128k)** at **Phi-3.5-vision-instruct (128k)** sa senaryo ng paggawa ng code matapos ma-integrate sa GitHub Models, at ito rin ang paghahanda para sa mga susunod na halimbawa

**Demo: GitHub Models Phi-3.5-mini-instruct (128k) gumawa ng code mula sa Prompt** ([click this link](../../../../../../code/09.UpdateSamples/Aug/ghmodel_phi35_instruct_demo.ipynb))

**Demo: GitHub Models Phi-3.5-vision-instruct (128k) gumawa ng code mula sa Imahe** ([click this link](../../../../../../code/09.UpdateSamples/Aug/ghmodel_phi35_vision_demo.ipynb))


## **Tungkol sa GitHub Copilot Chat Agent**

Ang GitHub Copilot Chat Agent ay kayang tapusin ang iba't ibang gawain sa iba't ibang proyekto base sa code. Ang sistema ay may apat na agents: workspace, github, terminal, vscode

![agent](../../../../../../translated_images/agent.19ff410949975e96c38aa5763545604a33dc923968b6abcd200ff8590c62efd7.tl.png)

Sa pamamagitan ng pagdagdag ng pangalan ng agent na may ‘@’, mabilis mong matatapos ang kaukulang trabaho. Para sa mga negosyo, kung idaragdag mo ang mga nilalaman na may kinalaman sa iyong negosyo tulad ng mga requirements, coding, test specifications, at release, magkakaroon ka ng mas malakas na enterprise private functions base sa GitHub Copilot.

Opisyal nang inilabas ang API ng Visual Studio Code Chat Agent, na nagpapahintulot sa mga kumpanya o mga enterprise developer na gumawa ng agents base sa iba't ibang software business ecosystems. Base sa paraan ng pag-develop ng Visual Studio Code Extension Development, madali mong maa-access ang interface ng Visual Studio Code Chat Agent API. Maaari tayong mag-develop gamit ang prosesong ito

![diagram](../../../../../../translated_images/diagram.e17900e549fa305114e13994f4091c34860163aaff8e67d206550bfd01bcb004.tl.png)

Ang senaryo ng pag-develop ay sumusuporta sa pag-access ng third-party model APIs (tulad ng GitHub Models, Azure Model Catalog, at mga self-built na serbisyo base sa open source models) at maaari ring gamitin ang gpt-35-turbo, gpt-4, at gpt-4o na mga modelo na ibinibigay ng GitHub Copilot.

## **Magdagdag ng Agent @phicoding base sa Phi-3.5**

Sinusubukan naming pagsamahin ang kakayahan sa programming ng Phi-3.5 upang tapusin ang pagsulat ng code, paggawa ng code mula sa imahe, at iba pang mga gawain. Gumawa ng isang Agent na nakasentro sa Phi-3.5 - @PHI, narito ang ilang mga function

1. Gumawa ng self-introduction gamit ang GPT-4o na ibinibigay ng GitHub Copilot sa pamamagitan ng **@phicoding /help** na command

2. Gumawa ng code para sa iba't ibang programming languages gamit ang **Phi-3.5-mini-instruct (128k)** sa pamamagitan ng **@phicoding /gen** na command

3. Gumawa ng code base sa **Phi-3.5-vision-instruct (128k)** at kumpletuhin ang code mula sa imahe gamit ang **@phicoding /image** na command

![arch](../../../../../../translated_images/arch.c302d58012f0988b02f2275e24d8d21259899ef827d8a7579daecd1dd8b83ffd.tl.png)

## **Mga kaugnay na hakbang**

1. I-install ang Visual Studio Code Extension development support gamit ang npm

```bash

npm install --global yo generator-code 

```
2. Gumawa ng Visual Studio Code Extension plugin (gamit ang Typescript development mode, pangalanan itong phiext)


```bash

yo code 

```

3. Buksan ang nagawang proyekto at baguhin ang package.json. Narito ang mga kaugnay na tagubilin at mga configuration, pati na rin ang configuration ng GitHub Models. Tandaan na kailangan mong ilagay ang iyong GitHub Models token dito.


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

4. Baguhin ang src/extension.ts


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

6. Pagpapatakbo

***/help***

![help](../../../../../../translated_images/help.e26759fe1e92cea3e8788b2157e4383f621254ce001ba4ef6d35fce1e0667e55.tl.png)

***@phicoding /help***

![agenthelp](../../../../../../translated_images/agenthelp.f249f33c3fa449e0a779c78e3c2f3a65820702c03129e52a81a8df369443e413.tl.png)

***@phicoding /gen***

![agentgen](../../../../../../translated_images/agentgen.90c9cb76281be28a6cfdccda08f65043579ef4730a818c34e6f33ab6eb90e38c.tl.png)


***@phicoding /image***

![agentimage](../../../../../../translated_images/agentimage.db0cc3d3bd0ee494170ebd2623623e1012eb9f5786436439e2e36b91ca163172.tl.png)


Maaari mong i-download ang sample code dito :[click](../../../../../../code/09.UpdateSamples/Aug/vscode)

## **Mga Resources**

1. Mag-sign up sa GitHub Models [https://gh.io/models](https://gh.io/models)

2. Matutunan ang Visual Studio Code Extension Development [https://code.visualstudio.com/api/get-started/your-first-extension](https://code.visualstudio.com/api/get-started/your-first-extension)

3. Alamin ang tungkol sa Visual Studio Code Coilot Chat API [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat)

**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang likas na wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.