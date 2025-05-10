<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "35bf81388ac6917277b8d9a0c39bdc70",
  "translation_date": "2025-05-09T19:04:45+00:00",
  "source_file": "md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md",
  "language_code": "pa"
}
-->
# **ਆਪਣਾ Visual Studio Code Chat Copilot Agent Phi-3.5 ਨਾਲ GitHub Models ਦੁਆਰਾ ਬਣਾਓ**

ਕੀ ਤੁਸੀਂ Visual Studio Code Copilot ਵਰਤ ਰਹੇ ਹੋ? ਖਾਸ ਕਰਕੇ Chat ਵਿੱਚ, ਤੁਸੀਂ ਵੱਖ-ਵੱਖ ਏਜੰਟਾਂ ਦੀ ਵਰਤੋਂ ਕਰ ਸਕਦੇ ਹੋ ਤਾਂ ਜੋ Visual Studio Code ਵਿੱਚ ਪ੍ਰੋਜੈਕਟ ਬਣਾਉਣ, ਲਿਖਣ ਅਤੇ ਸੰਭਾਲਣ ਦੀ ਸਮਰੱਥਾ ਨੂੰ ਵਧਾਇਆ ਜਾ ਸਕੇ। Visual Studio Code ਇੱਕ API ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ ਜੋ ਕੰਪਨੀਆਂ ਅਤੇ ਵਿਅਕਤੀਆਂ ਨੂੰ ਆਪਣੇ ਕਾਰੋਬਾਰ ਦੇ ਅਧਾਰ 'ਤੇ ਵੱਖ-ਵੱਖ ਏਜੰਟ ਬਣਾਉਣ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ, ਤਾਂ ਜੋ ਵੱਖ-ਵੱਖ ਖੇਤਰਾਂ ਵਿੱਚ ਆਪਣੀ ਸਮਰੱਥਾ ਨੂੰ ਵਧਾਇਆ ਜਾ ਸਕੇ। ਇਸ ਲੇਖ ਵਿੱਚ, ਅਸੀਂ GitHub Models ਦੇ **Phi-3.5-mini-instruct (128k)** ਅਤੇ **Phi-3.5-vision-instruct (128k)** 'ਤੇ ਧਿਆਨ ਦੇਵਾਂਗੇ ਤਾਂ ਜੋ ਤੁਸੀਂ ਆਪਣਾ Visual Studio Code Agent ਤਿਆਰ ਕਰ ਸਕੋ।

## **GitHub Models 'ਤੇ Phi-3.5 ਬਾਰੇ**

ਅਸੀਂ ਜਾਣਦੇ ਹਾਂ ਕਿ Phi-3/3.5-mini-instruct Phi-3/3.5 ਪਰਿਵਾਰ ਵਿੱਚ ਕੋਡ ਸਮਝਣ ਅਤੇ ਤਿਆਰ ਕਰਨ ਦੀਆਂ ਮਜ਼ਬੂਤ ਸਮਰੱਥਾਵਾਂ ਰੱਖਦਾ ਹੈ, ਅਤੇ ਇਹ Gemma-2-9b ਅਤੇ Mistral-Nemo-12B-instruct-2407 ਨਾਲੋਂ ਬਿਹਤਰ ਹੈ।

![codegen](../../../../../../translated_images/codegen.eede87d45b849fd8738a7789f44ec3b81c4907d23eebd2b0e3dbd62c939c7cb9.pa.png)

ਨਵੇਂ GitHub Models ਪਹਿਲਾਂ ਹੀ Phi-3.5-mini-instruct (128k) ਅਤੇ Phi-3.5-vision-instruct (128k) ਮਾਡਲਾਂ ਦੀ ਪਹੁੰਚ ਪ੍ਰਦਾਨ ਕਰਦੇ ਹਨ। ਵਿਕਾਸਕਾਰ ਉਹਨਾਂ ਨੂੰ OpenAI SDK, Azure AI Inference SDK, ਅਤੇ REST API ਰਾਹੀਂ ਵਰਤ ਸਕਦੇ ਹਨ।

![gh](../../../../../../translated_images/gh.7fa589617baffe1b3f8a044fb29ee1b46f02645a47f3caa57d493768512b94e8.pa.png)

***Note: *** ਇੱਥੇ Azure AI Inference SDK ਦੀ ਵਰਤੋਂ ਕਰਨ ਦੀ ਸਿਫਾਰਿਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ, ਕਿਉਂਕਿ ਇਹ ਪ੍ਰੋਡਕਸ਼ਨ ਵਾਤਾਵਰਨ ਵਿੱਚ Azure Model Catalog ਨਾਲ ਬਿਹਤਰ ਤਬਦੀਲੀ ਕਰ ਸਕਦਾ ਹੈ।

ਹੇਠਾਂ GitHub Models ਨਾਲ ਡਾਕਿੰਗ ਤੋਂ ਬਾਅਦ ਕੋਡ ਤਿਆਰ ਕਰਨ ਦੇ ਮਾਮਲੇ ਵਿੱਚ **Phi-3.5-mini-instruct (128k)** ਅਤੇ **Phi-3.5-vision-instruct (128k)** ਦੇ ਨਤੀਜੇ ਦਿੱਤੇ ਗਏ ਹਨ, ਅਤੇ ਅਗਲੇ ਉਦਾਹਰਣਾਂ ਲਈ ਤਿਆਰੀ ਵੀ ਕੀਤੀ ਗਈ ਹੈ।

**ਡੈਮੋ: GitHub Models Phi-3.5-mini-instruct (128k) ਤੋਂ Prompt ਦੁਆਰਾ ਕੋਡ ਤਿਆਰ ਕਰਨਾ** ([ਇਸ ਲਿੰਕ 'ਤੇ ਕਲਿੱਕ ਕਰੋ](../../../../../../code/09.UpdateSamples/Aug/ghmodel_phi35_instruct_demo.ipynb))

**ਡੈਮੋ: GitHub Models Phi-3.5-vision-instruct (128k) ਤੋਂ Image ਦੁਆਰਾ ਕੋਡ ਤਿਆਰ ਕਰਨਾ** ([ਇਸ ਲਿੰਕ 'ਤੇ ਕਲਿੱਕ ਕਰੋ](../../../../../../code/09.UpdateSamples/Aug/ghmodel_phi35_vision_demo.ipynb))


## **GitHub Copilot Chat Agent ਬਾਰੇ**

GitHub Copilot Chat Agent ਵੱਖ-ਵੱਖ ਪ੍ਰੋਜੈਕਟ ਸੰਦਰਭਾਂ ਵਿੱਚ ਕੋਡ ਦੇ ਅਧਾਰ 'ਤੇ ਵੱਖ-ਵੱਖ ਕੰਮ ਪੂਰੇ ਕਰ ਸਕਦਾ ਹੈ। ਸਿਸਟਮ ਵਿੱਚ ਚਾਰ ਏਜੰਟ ਹਨ: workspace, github, terminal, vscode

![agent](../../../../../../translated_images/agent.19ff410949975e96c38aa5763545604a33dc923968b6abcd200ff8590c62efd7.pa.png)

ਏਜੰਟ ਦੇ ਨਾਮ ਨਾਲ ‘@’ ਜੋੜ ਕੇ, ਤੁਸੀਂ ਜਲਦੀ ਨਾਲ ਸੰਬੰਧਤ ਕੰਮ ਪੂਰਾ ਕਰ ਸਕਦੇ ਹੋ। ਉਦਯੋਗਾਂ ਲਈ, ਜੇ ਤੁਸੀਂ ਆਪਣਾ ਕਾਰੋਬਾਰੀ ਸੰਬੰਧੀ ਸਮੱਗਰੀ ਜਿਵੇਂ ਕਿ ਲੋੜਾਂ, ਕੋਡਿੰਗ, ਟੈਸਟ ਨਿਰਦੇਸ਼ਾਂ ਅਤੇ ਰਿਲੀਜ਼ ਸ਼ਾਮਲ ਕਰਦੇ ਹੋ, ਤਾਂ ਤੁਸੀਂ GitHub Copilot ਦੇ ਆਧਾਰ 'ਤੇ ਹੋਰ ਤਾਕਤਵਰ ਕਾਰਪੋਰੇਟ ਪ੍ਰਾਈਵੇਟ ਫੰਕਸ਼ਨਾਂ ਪ੍ਰਾਪਤ ਕਰ ਸਕਦੇ ਹੋ।

Visual Studio Code Chat Agent ਨੇ ਹੁਣ ਆਪਣਾ API ਅਧਿਕਾਰਿਕ ਤੌਰ 'ਤੇ ਜਾਰੀ ਕਰ ਦਿੱਤਾ ਹੈ, ਜਿਸ ਨਾਲ ਉਦਯੋਗ ਜਾਂ ਉਦਯੋਗ ਵਿਕਾਸਕਾਰ ਵੱਖ-ਵੱਖ ਸਾਫਟਵੇਅਰ ਕਾਰੋਬਾਰੀ ਪਰਿਵਾਰਾਂ ਦੇ ਅਧਾਰ 'ਤੇ ਏਜੰਟ ਵਿਕਸਿਤ ਕਰ ਸਕਦੇ ਹਨ। Visual Studio Code Extension Development ਦੇ ਵਿਕਾਸ ਤਰੀਕੇ ਦੇ ਆਧਾਰ 'ਤੇ, ਤੁਸੀਂ ਆਸਾਨੀ ਨਾਲ Visual Studio Code Chat Agent API ਦੀ ਇੰਟਰਫੇਸ ਤੱਕ ਪਹੁੰਚ ਕਰ ਸਕਦੇ ਹੋ। ਅਸੀਂ ਇਸ ਪ੍ਰਕਿਰਿਆ ਦੇ ਅਧਾਰ 'ਤੇ ਵਿਕਾਸ ਕਰ ਸਕਦੇ ਹਾਂ।

![diagram](../../../../../../translated_images/diagram.e17900e549fa305114e13994f4091c34860163aaff8e67d206550bfd01bcb004.pa.png)

ਇਹ ਵਿਕਾਸ ਸੰਦਰਭ ਤੀਜੀ-ਪੱਖੀ ਮਾਡਲ APIਜ਼ (ਜਿਵੇਂ GitHub Models, Azure Model Catalog, ਅਤੇ ਖੁੱਲ੍ਹੇ ਸਰੋਤ ਮਾਡਲਾਂ ਦੇ ਆਧਾਰ 'ਤੇ ਬਣਾਈਆਂ ਸੇਵਾਵਾਂ) ਤੱਕ ਪਹੁੰਚ ਦਾ ਸਮਰਥਨ ਕਰਦਾ ਹੈ ਅਤੇ GitHub Copilot ਵੱਲੋਂ ਪ੍ਰਦਾਨ ਕੀਤੇ gpt-35-turbo, gpt-4, ਅਤੇ gpt-4o ਮਾਡਲਾਂ ਦੀ ਵਰਤੋਂ ਵੀ ਕਰ ਸਕਦਾ ਹੈ।

## **Phi-3.5 ਦੇ ਆਧਾਰ 'ਤੇ ਏਜੰਟ @phicoding ਸ਼ਾਮਲ ਕਰੋ**

ਅਸੀਂ Phi-3.5 ਦੀ ਪ੍ਰੋਗ੍ਰਾਮਿੰਗ ਸਮਰੱਥਾ ਨੂੰ ਇਕੱਠਾ ਕਰਨ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ ਤਾਂ ਜੋ ਕੋਡ ਲਿਖਣਾ, ਇਮੇਜ ਜਨਰੇਸ਼ਨ ਕੋਡ ਅਤੇ ਹੋਰ ਕੰਮ ਪੂਰੇ ਕੀਤੇ ਜਾ ਸਕਣ। Phi-3.5 ਦੇ ਆਲੇ-ਦੁਆਲੇ ਬਣਾਇਆ ਗਿਆ ਇੱਕ ਏਜੰਟ - @PHI ਪੂਰਾ ਕਰੋ, ਹੇਠਾਂ ਕੁਝ ਫੰਕਸ਼ਨਾਂ ਹਨ:

1. GitHub Copilot ਵੱਲੋਂ ਪ੍ਰਦਾਨ ਕੀਤੇ GPT-4o ਦੇ ਆਧਾਰ 'ਤੇ **@phicoding /help** ਕਮਾਂਡ ਰਾਹੀਂ ਆਪਣੀ ਪਰਿਚਿਆ ਬਣਾਓ

2. **Phi-3.5-mini-instruct (128k)** ਦੇ ਆਧਾਰ 'ਤੇ ਵੱਖ-ਵੱਖ ਪ੍ਰੋਗ੍ਰਾਮਿੰਗ ਭਾਸ਼ਾਵਾਂ ਲਈ ਕੋਡ ਤਿਆਰ ਕਰੋ **@phicoding /gen** ਕਮਾਂਡ ਰਾਹੀਂ

3. **Phi-3.5-vision-instruct (128k)** ਅਤੇ ਇਮੇਜ ਪੂਰੀ ਕਰਨ ਦੇ ਆਧਾਰ 'ਤੇ ਕੋਡ ਤਿਆਰ ਕਰੋ **@phicoding /image** ਕਮਾਂਡ ਰਾਹੀਂ

![arch](../../../../../../translated_images/arch.c302d58012f0988b02f2275e24d8d21259899ef827d8a7579daecd1dd8b83ffd.pa.png)

## **ਸੰਬੰਧਤ ਕਦਮ**

1. npm ਦੀ ਵਰਤੋਂ ਕਰਕੇ Visual Studio Code Extension ਵਿਕਾਸ ਸਹਾਇਤਾ ਇੰਸਟਾਲ ਕਰੋ

```bash

npm install --global yo generator-code 

```
2. Visual Studio Code Extension ਪਲੱਗਇਨ ਬਣਾਓ (Typescript ਵਿਕਾਸ ਮੋਡ ਵਿੱਚ, ਨਾਮ phiext)

```bash

yo code 

```

3. ਬਣਾਇਆ ਗਿਆ ਪ੍ਰੋਜੈਕਟ ਖੋਲ੍ਹੋ ਅਤੇ package.json ਨੂੰ ਸੋਧੋ। ਇੱਥੇ ਸੰਬੰਧਿਤ ਹਦਾਇਤਾਂ ਅਤੇ ਸੰਰਚਨਾਵਾਂ ਹਨ, ਨਾਲ ਹੀ GitHub Models ਦੀ ਸੰਰਚਨਾ ਵੀ। ਧਿਆਨ ਰੱਖੋ ਕਿ ਤੁਹਾਨੂੰ ਇੱਥੇ ਆਪਣਾ GitHub Models ਟੋਕਨ ਸ਼ਾਮਲ ਕਰਨਾ ਪਵੇਗਾ।

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

4. src/extension.ts ਨੂੰ ਸੋਧੋ

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

6. ਚਲਾਉਣਾ

***/help***

![help](../../../../../../translated_images/help.e26759fe1e92cea3e8788b2157e4383f621254ce001ba4ef6d35fce1e0667e55.pa.png)

***@phicoding /help***

![agenthelp](../../../../../../translated_images/agenthelp.f249f33c3fa449e0a779c78e3c2f3a65820702c03129e52a81a8df369443e413.pa.png)

***@phicoding /gen***

![agentgen](../../../../../../translated_images/agentgen.90c9cb76281be28a6cfdccda08f65043579ef4730a818c34e6f33ab6eb90e38c.pa.png)

***@phicoding /image***

![agentimage](../../../../../../translated_images/agentimage.db0cc3d3bd0ee494170ebd2623623e1012eb9f5786436439e2e36b91ca163172.pa.png)

ਤੁਸੀਂ ਸੈਂਪਲ ਕੋਡ ਡਾਊਨਲੋਡ ਕਰ ਸਕਦੇ ਹੋ :[ਇੱਥੇ ਕਲਿੱਕ ਕਰੋ](../../../../../../code/09.UpdateSamples/Aug/vscode)

## **ਸੰਸਾਧਨ**

1. GitHub Models ਲਈ ਸਾਈਨ ਅੱਪ ਕਰੋ [https://gh.io/models](https://gh.io/models)

2. Visual Studio Code Extension Development ਸਿੱਖੋ [https://code.visualstudio.com/api/get-started/your-first-extension](https://code.visualstudio.com/api/get-started/your-first-extension)

3. Visual Studio Code Coilot Chat API ਬਾਰੇ ਜਾਣੋ [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat)

**ਅਸਵੀਕਾਰੋਤਾ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਆਟੋਮੈਟਿਕ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਥਿਰਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਵਜੋਂ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਨਾਲ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਮੀਆਂ ਜਾਂ ਭ੍ਰਮਾਂ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।