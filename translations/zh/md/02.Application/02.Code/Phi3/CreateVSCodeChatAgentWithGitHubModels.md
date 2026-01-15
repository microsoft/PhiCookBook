<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "35bf81388ac6917277b8d9a0c39bdc70",
  "translation_date": "2025-07-17T03:22:07+00:00",
  "source_file": "md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md",
  "language_code": "zh"
}
-->
# **使用 GitHub Models 的 Phi-3.5 创建你自己的 Visual Studio Code 聊天助手**

你在使用 Visual Studio Code Copilot 吗？尤其是在聊天功能中，你可以使用不同的助手来提升在 Visual Studio Code 中创建、编写和维护项目的能力。Visual Studio Code 提供了一个 API，允许企业和个人基于自身业务创建不同的助手，以扩展在各自专有领域的能力。本文将重点介绍 GitHub Models 的 **Phi-3.5-mini-instruct (128k)** 和 **Phi-3.5-vision-instruct (128k)**，帮助你创建自己的 Visual Studio Code 助手。

## **关于 GitHub Models 上的 Phi-3.5**

我们知道 Phi-3/3.5-mini-instruct 属于 Phi-3/3.5 家族，具备强大的代码理解和生成能力，相较于 Gemma-2-9b 和 Mistral-Nemo-12B-instruct-2407 有明显优势。

![codegen](../../../../../../translated_images/zh/codegen.53be1150ee54d969.png)

最新的 GitHub Models 已经提供了 Phi-3.5-mini-instruct (128k) 和 Phi-3.5-vision-instruct (128k) 模型。开发者可以通过 OpenAI SDK、Azure AI Inference SDK 以及 REST API 访问它们。

![gh](../../../../../../translated_images/zh/gh.459640c7ceba01d5.png)

***Note: *** 建议这里使用 Azure AI Inference SDK，因为它在生产环境中可以更好地与 Azure Model Catalog 切换。

以下是 **Phi-3.5-mini-instruct (128k)** 和 **Phi-3.5-vision-instruct (128k)** 在对接 GitHub Models 后的代码生成场景表现，同时也为后续示例做准备。

**演示：GitHub Models Phi-3.5-mini-instruct (128k) 根据提示生成代码** ([点击此链接](../../../../../../code/09.UpdateSamples/Aug/ghmodel_phi35_instruct_demo.ipynb))

**演示：GitHub Models Phi-3.5-vision-instruct (128k) 根据图片生成代码** ([点击此链接](../../../../../../code/09.UpdateSamples/Aug/ghmodel_phi35_vision_demo.ipynb))


## **关于 GitHub Copilot 聊天助手**

GitHub Copilot 聊天助手可以基于代码完成不同项目场景下的多种任务。系统内置四个助手：workspace、github、terminal、vscode。

![agent](../../../../../../translated_images/zh/agent.3dbb06228f9a6189.png)

通过在助手名称前加‘@’，你可以快速完成对应的工作。对于企业来说，如果添加与自身业务相关的内容，如需求、编码、测试规范和发布，就能基于 GitHub Copilot 拥有更强大的企业私有功能。

Visual Studio Code 聊天助手现已正式发布其 API，允许企业或企业开发者基于不同的软件业务生态开发助手。基于 Visual Studio Code 扩展开发的方式，你可以轻松接入 Visual Studio Code 聊天助手 API 的接口。我们可以基于此流程进行开发。

![diagram](../../../../../../translated_images/zh/diagram.ca70d2866762f115.png)

开发场景支持接入第三方模型 API（如 GitHub Models、Azure Model Catalog 以及基于开源模型自建的服务），也可以使用 GitHub Copilot 提供的 gpt-35-turbo、gpt-4 和 gpt-4o 模型。

## **基于 Phi-3.5 添加一个 Agent @phicoding**

我们尝试整合 Phi-3.5 的编程能力，完成代码编写、图片生成代码等任务。打造一个围绕 Phi-3.5 构建的 Agent —— @PHI，具备以下功能：

1. 通过 **@phicoding /help** 命令，基于 GitHub Copilot 提供的 GPT-4o 生成自我介绍

2. 通过 **@phicoding /gen** 命令，基于 **Phi-3.5-mini-instruct (128k)** 生成不同编程语言的代码

3. 通过 **@phicoding /image** 命令，基于 **Phi-3.5-vision-instruct (128k)** 和图片完成代码生成

![arch](../../../../../../translated_images/zh/arch.5a58a0adfa959a2d.png)

## **相关步骤**

1. 使用 npm 安装 Visual Studio Code 扩展开发支持

```bash

npm install --global yo generator-code 

```

2. 创建一个 Visual Studio Code 扩展插件（使用 Typescript 开发模式，命名为 phiext）

```bash

yo code 

```

3. 打开创建的项目并修改 package.json。这里包含相关说明和配置，以及 GitHub Models 的配置。注意需要在此处添加你的 GitHub Models token。

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

6. 运行

***/help***

![help](../../../../../../translated_images/zh/help.04c134d2bf9a9541.png)

***@phicoding /help***

![agenthelp](../../../../../../translated_images/zh/agenthelp.60c68767c941a3fe.png)

***@phicoding /gen***

![agentgen](../../../../../../translated_images/zh/agentgen.a16e7735790f764b.png)

***@phicoding /image***

![agentimage](../../../../../../translated_images/zh/agentimage.f5cb52b45ab7d0d1.png)

你可以下载示例代码：[点击这里](../../../../../../code/09.UpdateSamples/Aug/vscode)

## **资源**

1. 注册 GitHub Models [https://gh.io/models](https://gh.io/models)

2. 学习 Visual Studio Code 扩展开发 [https://code.visualstudio.com/api/get-started/your-first-extension](https://code.visualstudio.com/api/get-started/your-first-extension)

3. 了解 Visual Studio Code Copilot 聊天 API [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat)

**免责声明**：  
本文件使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始文件的母语版本应被视为权威来源。对于重要信息，建议使用专业人工翻译。对于因使用本翻译而产生的任何误解或误释，我们不承担任何责任。