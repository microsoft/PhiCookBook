<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "35bf81388ac6917277b8d9a0c39bdc70",
  "translation_date": "2025-07-17T03:28:41+00:00",
  "source_file": "md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md",
  "language_code": "ms"
}
-->
# **Cipta Ejen Visual Studio Code Chat Copilot Anda Sendiri dengan Phi-3.5 oleh GitHub Models**

Adakah anda menggunakan Visual Studio Code Copilot? Terutamanya dalam Chat, anda boleh menggunakan ejen yang berbeza untuk meningkatkan keupayaan mencipta, menulis, dan menyelenggara projek dalam Visual Studio Code. Visual Studio Code menyediakan API yang membolehkan syarikat dan individu mencipta ejen yang berbeza berdasarkan perniagaan mereka untuk mengembangkan keupayaan dalam pelbagai bidang proprietari. Dalam artikel ini, kita akan fokus pada **Phi-3.5-mini-instruct (128k)** dan **Phi-3.5-vision-instruct (128k)** daripada GitHub Models untuk mencipta Ejen Visual Studio Code anda sendiri.

## **Mengenai Phi-3.5 pada GitHub Models**

Kita tahu bahawa Phi-3/3.5-mini-instruct dalam Keluarga Phi-3/3.5 mempunyai keupayaan pemahaman dan penjanaan kod yang kukuh, dan mempunyai kelebihan berbanding Gemma-2-9b dan Mistral-Nemo-12B-instruct-2407.

![codegen](../../../../../../translated_images/codegen.53be1150ee54d969.ms.png)

GitHub Models terkini sudah menyediakan akses kepada model Phi-3.5-mini-instruct (128k) dan Phi-3.5-vision-instruct (128k). Pembangun boleh mengaksesnya melalui OpenAI SDK, Azure AI Inference SDK, dan REST API.

![gh](../../../../../../translated_images/gh.459640c7ceba01d5.ms.png)

***Nota:*** Disarankan menggunakan Azure AI Inference SDK di sini, kerana ia boleh bertukar dengan lebih baik menggunakan Azure Model Catalog dalam persekitaran pengeluaran.

Berikut adalah hasil **Phi-3.5-mini-instruct (128k)** dan **Phi-3.5-vision-instruct (128k)** dalam senario penjanaan kod selepas disambungkan dengan GitHub Models, serta persediaan untuk contoh-contoh berikut.

**Demo: GitHub Models Phi-3.5-mini-instruct (128k) menjana kod dari Prompt** ([klik pautan ini](../../../../../../code/09.UpdateSamples/Aug/ghmodel_phi35_instruct_demo.ipynb))

**Demo: GitHub Models Phi-3.5-vision-instruct (128k) menjana kod dari Imej** ([klik pautan ini](../../../../../../code/09.UpdateSamples/Aug/ghmodel_phi35_vision_demo.ipynb))


## **Mengenai GitHub Copilot Chat Agent**

GitHub Copilot Chat Agent boleh melengkapkan pelbagai tugasan dalam pelbagai senario projek berdasarkan kod. Sistem ini mempunyai empat ejen: workspace, github, terminal, vscode

![agent](../../../../../../translated_images/agent.3dbb06228f9a6189.ms.png)

Dengan menambah nama ejen dengan ‘@’, anda boleh menyelesaikan kerja yang sepadan dengan cepat. Untuk perusahaan, jika anda menambah kandungan berkaitan perniagaan anda seperti keperluan, pengekodan, spesifikasi ujian, dan pelepasan, anda boleh mempunyai fungsi peribadi perusahaan yang lebih berkuasa berdasarkan GitHub Copilot.

Visual Studio Code Chat Agent kini secara rasmi telah mengeluarkan API-nya, membolehkan perusahaan atau pembangun perusahaan membangunkan ejen berdasarkan ekosistem perniagaan perisian yang berbeza. Berdasarkan kaedah pembangunan Visual Studio Code Extension Development, anda boleh dengan mudah mengakses antara muka API Visual Studio Code Chat Agent. Kita boleh membangunkan berdasarkan proses ini.

![diagram](../../../../../../translated_images/diagram.ca70d2866762f115.ms.png)

Senario pembangunan boleh menyokong akses kepada API model pihak ketiga (seperti GitHub Models, Azure Model Catalog, dan perkhidmatan binaan sendiri berdasarkan model sumber terbuka) dan juga boleh menggunakan model gpt-35-turbo, gpt-4, dan gpt-4o yang disediakan oleh GitHub Copilot.

## **Tambah Ejen @phicoding berdasarkan Phi-3.5**

Kami cuba mengintegrasikan keupayaan pengaturcaraan Phi-3.5 untuk melengkapkan penulisan kod, penjanaan kod imej dan tugasan lain. Lengkapkan Ejen yang dibina berasaskan Phi-3.5 - @PHI, berikut adalah beberapa fungsi

1. Menjana pengenalan diri berdasarkan GPT-4o yang disediakan oleh GitHub Copilot melalui arahan **@phicoding /help**

2. Menjana kod untuk pelbagai bahasa pengaturcaraan berdasarkan **Phi-3.5-mini-instruct (128k)** melalui arahan **@phicoding /gen**

3. Menjana kod berdasarkan **Phi-3.5-vision-instruct (128k)** dan pelengkap imej melalui arahan **@phicoding /image**

![arch](../../../../../../translated_images/arch.5a58a0adfa959a2d.ms.png)

## **Langkah Berkaitan**

1. Pasang sokongan pembangunan Visual Studio Code Extension menggunakan npm

```bash

npm install --global yo generator-code 

```
2. Cipta plugin Visual Studio Code Extension (menggunakan mod pembangunan Typescript, dinamakan phiext)

```bash

yo code 

```

3. Buka projek yang dicipta dan ubah package.json. Berikut adalah arahan dan konfigurasi berkaitan, serta konfigurasi GitHub Models. Perlu diingat anda perlu menambah token GitHub Models anda di sini.

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

4. Ubah src/extension.ts

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

6. Menjalankan

***/help***

![help](../../../../../../translated_images/help.04c134d2bf9a9541.ms.png)

***@phicoding /help***

![agenthelp](../../../../../../translated_images/agenthelp.60c68767c941a3fe.ms.png)

***@phicoding /gen***

![agentgen](../../../../../../translated_images/agentgen.a16e7735790f764b.ms.png)

***@phicoding /image***

![agentimage](../../../../../../translated_images/agentimage.f5cb52b45ab7d0d1.ms.png)

Anda boleh muat turun kod contoh :[klik](../../../../../../code/09.UpdateSamples/Aug/vscode)

## **Sumber**

1. Daftar GitHub Models [https://gh.io/models](https://gh.io/models)

2. Belajar Pembangunan Visual Studio Code Extension [https://code.visualstudio.com/api/get-started/your-first-extension](https://code.visualstudio.com/api/get-started/your-first-extension)

3. Ketahui tentang Visual Studio Code Coilot Chat API [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.