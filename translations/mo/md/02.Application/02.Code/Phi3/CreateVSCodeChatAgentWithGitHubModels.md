<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "35bf81388ac6917277b8d9a0c39bdc70",
  "translation_date": "2025-07-17T03:22:20+00:00",
  "source_file": "md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md",
  "language_code": "mo"
}
-->
# **使用 GitHub Models 的 Phi-3.5 自行打造 Visual Studio Code Chat Copilot Agent**

你是否正在使用 Visual Studio Code Copilot？特別是在 Chat 功能中，你可以使用不同的代理人來提升在 Visual Studio Code 中創建、撰寫及維護專案的能力。Visual Studio Code 提供了一個 API，允許企業和個人根據自身業務打造不同的代理人，以擴展在各種專有領域的能力。本文將聚焦於 GitHub Models 的 **Phi-3.5-mini-instruct (128k)** 與 **Phi-3.5-vision-instruct (128k)**，教你如何打造自己的 Visual Studio Code 代理人。

## **關於 GitHub Models 上的 Phi-3.5**

我們知道 Phi-3/3.5-mini-instruct 屬於 Phi-3/3.5 家族，具備強大的程式碼理解與生成能力，並且在某些方面優於 Gemma-2-9b 與 Mistral-Nemo-12B-instruct-2407。

![codegen](../../../../../../translated_images/mo/codegen.53be1150ee54d969.png)

最新的 GitHub Models 已經提供了 Phi-3.5-mini-instruct (128k) 與 Phi-3.5-vision-instruct (128k) 模型。開發者可以透過 OpenAI SDK、Azure AI Inference SDK 以及 REST API 來存取這些模型。

![gh](../../../../../../translated_images/mo/gh.459640c7ceba01d5.png)

***Note: *** 建議此處使用 Azure AI Inference SDK，因為在生產環境中能更好地與 Azure Model Catalog 切換。

以下展示了 **Phi-3.5-mini-instruct (128k)** 與 **Phi-3.5-vision-instruct (128k)** 在與 GitHub Models 對接後於程式碼生成場景的表現，並為後續範例做準備。

**Demo: GitHub Models Phi-3.5-mini-instruct (128k) 從提示生成程式碼** ([點此連結](../../../../../../code/09.UpdateSamples/Aug/ghmodel_phi35_instruct_demo.ipynb))

**Demo: GitHub Models Phi-3.5-vision-instruct (128k) 從圖片生成程式碼** ([點此連結](../../../../../../code/09.UpdateSamples/Aug/ghmodel_phi35_vision_demo.ipynb))


## **關於 GitHub Copilot Chat Agent**

GitHub Copilot Chat Agent 能根據程式碼在不同專案場景中完成各種任務。系統包含四個代理人：workspace、github、terminal、vscode。

![agent](../../../../../../translated_images/mo/agent.3dbb06228f9a6189.png)

只要在代理人名稱前加上「@」，即可快速完成對應工作。對企業來說，若加入自身業務相關內容，如需求、程式碼、測試規範與發佈流程，便能基於 GitHub Copilot 擁有更強大的企業私有功能。

Visual Studio Code Chat Agent 現已正式釋出 API，允許企業或企業開發者基於不同軟體業務生態系開發代理人。依照 Visual Studio Code 擴充套件開發方式，你可以輕鬆存取 Visual Studio Code Chat Agent API 的介面。我們可以依此流程進行開發。

![diagram](../../../../../../translated_images/mo/diagram.ca70d2866762f115.png)

開發場景支援接入第三方模型 API（如 GitHub Models、Azure Model Catalog，以及基於開源模型自建服務），也能使用 GitHub Copilot 提供的 gpt-35-turbo、gpt-4 與 gpt-4o 模型。

## **基於 Phi-3.5 新增代理人 @phicoding**

我們嘗試整合 Phi-3.5 的程式設計能力，完成程式碼撰寫、圖片生成程式碼等任務。打造一個以 Phi-3.5 為核心的代理人 - @PHI，具備以下功能：

1. 透過 **@phicoding /help** 指令，基於 GitHub Copilot 提供的 GPT-4o 生成自我介紹

2. 透過 **@phicoding /gen** 指令，基於 **Phi-3.5-mini-instruct (128k)** 生成不同程式語言的程式碼

3. 透過 **@phicoding /image** 指令，基於 **Phi-3.5-vision-instruct (128k)** 及圖片完成程式碼生成

![arch](../../../../../../translated_images/mo/arch.5a58a0adfa959a2d.png)

## **相關步驟**

1. 使用 npm 安裝 Visual Studio Code 擴充套件開發支援

```bash

npm install --global yo generator-code 

```

2. 建立 Visual Studio Code 擴充套件插件（使用 Typescript 開發模式，命名為 phiext）

```bash

yo code 

```

3. 開啟已建立的專案並修改 package.json。以下為相關說明與配置，以及 GitHub Models 的設定。請注意，這裡需要加入你的 GitHub Models token。

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

4. 修改 src/extension.ts

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

6. 執行

***/help***

![help](../../../../../../translated_images/mo/help.04c134d2bf9a9541.png)

***@phicoding /help***

![agenthelp](../../../../../../translated_images/mo/agenthelp.60c68767c941a3fe.png)

***@phicoding /gen***

![agentgen](../../../../../../translated_images/mo/agentgen.a16e7735790f764b.png)

***@phicoding /image***

![agentimage](../../../../../../translated_images/mo/agentimage.f5cb52b45ab7d0d1.png)

你可以下載範例程式碼：[點此](../../../../../../code/09.UpdateSamples/Aug/vscode)

## **資源**

1. 註冊 GitHub Models [https://gh.io/models](https://gh.io/models)

2. 學習 Visual Studio Code 擴充套件開發 [https://code.visualstudio.com/api/get-started/your-first-extension](https://code.visualstudio.com/api/get-started/your-first-extension)

3. 了解 Visual Studio Code Copilot Chat API [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat)

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋負責。