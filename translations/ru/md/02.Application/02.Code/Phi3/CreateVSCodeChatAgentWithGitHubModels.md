<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "35bf81388ac6917277b8d9a0c39bdc70",
  "translation_date": "2025-07-17T03:21:08+00:00",
  "source_file": "md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md",
  "language_code": "ru"
}
-->
# **Создайте собственного агента Visual Studio Code Chat Copilot с Phi-3.5 от GitHub Models**

Вы используете Visual Studio Code Copilot? Особенно в чате можно применять разных агентов, чтобы улучшить процесс создания, написания и поддержки проектов в Visual Studio Code. Visual Studio Code предоставляет API, позволяющее компаниям и отдельным разработчикам создавать различных агентов, ориентированных на их бизнес, расширяя возможности в разных специализированных областях. В этой статье мы сосредоточимся на **Phi-3.5-mini-instruct (128k)** и **Phi-3.5-vision-instruct (128k)** от GitHub Models для создания собственного агента Visual Studio Code.

## **О Phi-3.5 в GitHub Models**

Известно, что Phi-3/3.5-mini-instruct из семейства Phi-3/3.5 обладает мощными возможностями понимания и генерации кода, превосходя Gemma-2-9b и Mistral-Nemo-12B-instruct-2407.

![codegen](../../../../../../translated_images/codegen.53be1150ee54d969f06699bbe6f0daf5c6b423ab800181589c61a9e31ccb6e83.ru.png)

Последние версии GitHub Models уже предоставляют доступ к моделям Phi-3.5-mini-instruct (128k) и Phi-3.5-vision-instruct (128k). Разработчики могут использовать их через OpenAI SDK, Azure AI Inference SDK и REST API.

![gh](../../../../../../translated_images/gh.459640c7ceba01d57827546901c205ee7c53e85f6ddd81d2231ef7693d8b08a2.ru.png)

***Note: *** Рекомендуется использовать Azure AI Inference SDK, так как он лучше интегрируется с Azure Model Catalog в производственной среде.

Ниже приведены результаты работы **Phi-3.5-mini-instruct (128k)** и **Phi-3.5-vision-instruct (128k)** в сценарии генерации кода после интеграции с GitHub Models, а также подготовка к следующим примерам.

**Демо: GitHub Models Phi-3.5-mini-instruct (128k) генерация кода по Prompt** ([перейти по ссылке](../../../../../../code/09.UpdateSamples/Aug/ghmodel_phi35_instruct_demo.ipynb))

**Демо: GitHub Models Phi-3.5-vision-instruct (128k) генерация кода по изображению** ([перейти по ссылке](../../../../../../code/09.UpdateSamples/Aug/ghmodel_phi35_vision_demo.ipynb))


## **О GitHub Copilot Chat Agent**

GitHub Copilot Chat Agent может выполнять различные задачи в разных проектных сценариях, опираясь на код. В системе есть четыре агента: workspace, github, terminal, vscode.

![agent](../../../../../../translated_images/agent.3dbb06228f9a618982b8761c2501f1b5124cd8c4611fb882ee09516de29a2153.ru.png)

Добавляя имя агента с символом ‘@’, вы быстро выполняете соответствующую работу. Для предприятий, если добавить собственный бизнес-контент, такой как требования, кодирование, тестовые спецификации и релизы, можно получить более мощные приватные функции на базе GitHub Copilot.

Visual Studio Code Chat Agent официально выпустил API, позволяющий компаниям и корпоративным разработчикам создавать агентов, ориентированных на разные экосистемы программного обеспечения. Используя метод разработки расширений Visual Studio Code, вы легко получите доступ к интерфейсу API Visual Studio Code Chat Agent. Мы можем разрабатывать на основе этого процесса.

![diagram](../../../../../../translated_images/diagram.ca70d2866762f1155a89e483e77537aa08087e04c909992595dc0cbe9b3a6a80.ru.png)

Сценарий разработки поддерживает доступ к API сторонних моделей (например, GitHub Models, Azure Model Catalog и собственных сервисов на базе open source моделей), а также может использовать модели gpt-35-turbo, gpt-4 и gpt-4o, предоставляемые GitHub Copilot.

## **Добавление агента @phicoding на базе Phi-3.5**

Мы пытаемся интегрировать программные возможности Phi-3.5 для выполнения задач по написанию кода, генерации кода по изображению и другим. Создаем агента на основе Phi-3.5 - @PHI, с такими функциями:

1. Генерация самопрезентации на основе GPT-4o, предоставляемой GitHub Copilot, через команду **@phicoding /help**

2. Генерация кода на разных языках программирования на базе **Phi-3.5-mini-instruct (128k)** через команду **@phicoding /gen**

3. Генерация кода на основе **Phi-3.5-vision-instruct (128k)** и дополнение по изображению через команду **@phicoding /image**

![arch](../../../../../../translated_images/arch.5a58a0adfa959a2da4fe954f16e66b008aef250fe81e9062571688c4f1e57068.ru.png)

## **Связанные шаги**

1. Установите поддержку разработки расширений Visual Studio Code с помощью npm

```bash

npm install --global yo generator-code 

```
2. Создайте плагин расширения Visual Studio Code (используя Typescript, с именем phiext)

```bash

yo code 

```

3. Откройте созданный проект и измените package.json. Здесь приведены соответствующие инструкции и настройки, а также конфигурация GitHub Models. Обратите внимание, что необходимо добавить ваш токен GitHub Models.

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

4. Измените src/extension.ts

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

6. Запуск

***/help***

![help](../../../../../../translated_images/help.04c134d2bf9a95418857a947113b38ccad1aef1b8a9f0d9fd80a80719126e11d.ru.png)

***@phicoding /help***

![agenthelp](../../../../../../translated_images/agenthelp.60c68767c941a3fea985d8095f5681ee4529210f94d66ff71ee2b4aea245af31.ru.png)

***@phicoding /gen***

![agentgen](../../../../../../translated_images/agentgen.a16e7735790f764bae0018e6d4b7d6f06554d76a3e955796764af4096bead6d2.ru.png)

***@phicoding /image***

![agentimage](../../../../../../translated_images/agentimage.f5cb52b45ab7d0d1c2d012668cd069dddbd1dfd2ef7cec9c7814eb46f0820d4d.ru.png)

Вы можете скачать пример кода: [кликните здесь](../../../../../../code/09.UpdateSamples/Aug/vscode)

## **Ресурсы**

1. Зарегистрируйтесь в GitHub Models [https://gh.io/models](https://gh.io/models)

2. Изучите разработку расширений Visual Studio Code [https://code.visualstudio.com/api/get-started/your-first-extension](https://code.visualstudio.com/api/get-started/your-first-extension)

3. Узнайте о Visual Studio Code Copilot Chat API [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat)

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, просим учитывать, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обращаться к профессиональному человеческому переводу. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования данного перевода.