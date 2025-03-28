<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "35bf81388ac6917277b8d9a0c39bdc70",
  "translation_date": "2025-03-27T11:32:48+00:00",
  "source_file": "md\\02.Application\\02.Code\\Phi3\\CreateVSCodeChatAgentWithGitHubModels.md",
  "language_code": "fa"
}
-->
# **ساخت Agent چت کوپایلوت ویژوال استودیو کد خودتان با Phi-3.5 از مدل‌های GitHub**

آیا از کوپایلوت ویژوال استودیو کد استفاده می‌کنید؟ به‌خصوص در حالت چت، می‌توانید از عوامل مختلفی استفاده کنید تا توانایی ساخت، نوشتن و نگهداری پروژه‌ها در ویژوال استودیو کد را بهبود ببخشید. ویژوال استودیو کد یک API فراهم کرده است که به شرکت‌ها و افراد اجازه می‌دهد عوامل مختلفی بر اساس نیازهای تجاری خود ایجاد کنند تا قابلیت‌های خود را در زمینه‌های اختصاصی مختلف گسترش دهند. در این مقاله، ما بر روی **Phi-3.5-mini-instruct (128k)** و **Phi-3.5-vision-instruct (128k)** از مدل‌های GitHub تمرکز می‌کنیم تا Agent ویژوال استودیو کد خودتان را بسازید.

## **درباره Phi-3.5 در مدل‌های GitHub**

می‌دانیم که Phi-3/3.5-mini-instruct در خانواده Phi-3/3.5 توانایی‌های قوی درک و تولید کد دارد و نسبت به Gemma-2-9b و Mistral-Nemo-12B-instruct-2407 برتری دارد.

![codegen](../../../../../../translated_images/codegen.eede87d45b849fd8738a7789f44ec3b81c4907d23eebd2b0e3dbd62c939c7cb9.fa.png)

جدیدترین مدل‌های GitHub دسترسی به مدل‌های Phi-3.5-mini-instruct (128k) و Phi-3.5-vision-instruct (128k) را فراهم کرده‌اند. توسعه‌دهندگان می‌توانند از طریق OpenAI SDK، Azure AI Inference SDK و REST API به این مدل‌ها دسترسی پیدا کنند.

![gh](../../../../../../translated_images/gh.7fa589617baffe1b3f8a044fb29ee1b46f02645a47f3caa57d493768512b94e8.fa.png)

***توجه:*** پیشنهاد می‌شود در اینجا از Azure AI Inference SDK استفاده کنید، زیرا این ابزار می‌تواند در محیط تولیدی بهتر با Azure Model Catalog جابجا شود.

نتایج **Phi-3.5-mini-instruct (128k)** و **Phi-3.5-vision-instruct (128k)** در سناریوی تولید کد پس از اتصال به مدل‌های GitHub در زیر آمده است و همچنین برای مثال‌های بعدی آماده شده‌اند:

**دمو: مدل‌های GitHub Phi-3.5-mini-instruct (128k) کد را از Prompt تولید می‌کنند** ([روی این لینک کلیک کنید](../../../../../../code/09.UpdateSamples/Aug/ghmodel_phi35_instruct_demo.ipynb))

**دمو: مدل‌های GitHub Phi-3.5-vision-instruct (128k) کد را از تصویر تولید می‌کنند** ([روی این لینک کلیک کنید](../../../../../../code/09.UpdateSamples/Aug/ghmodel_phi35_vision_demo.ipynb))

## **درباره GitHub Copilot Chat Agent**

GitHub Copilot Chat Agent می‌تواند وظایف مختلفی را در سناریوهای مختلف پروژه بر اساس کد انجام دهد. این سیستم چهار عامل دارد: workspace، github، terminal، vscode.

![agent](../../../../../../translated_images/agent.19ff410949975e96c38aa5763545604a33dc923968b6abcd200ff8590c62efd7.fa.png)

با اضافه کردن نام عامل با ‘@’، می‌توانید به سرعت کار مربوطه را انجام دهید. برای شرکت‌ها، اگر محتوای مرتبط با کسب‌وکار خود مانند نیازها، کدنویسی، مشخصات تست و انتشار را اضافه کنید، می‌توانید بر اساس GitHub Copilot عملکردهای خصوصی قوی‌تری برای شرکت ایجاد کنید.

Agent چت ویژوال استودیو کد اکنون API خود را به‌صورت رسمی منتشر کرده است و به شرکت‌ها یا توسعه‌دهندگان شرکتی اجازه می‌دهد عوامل را بر اساس اکوسیستم‌های نرم‌افزاری مختلف توسعه دهند. بر اساس روش توسعه افزونه ویژوال استودیو کد، می‌توانید به راحتی به رابط API Agent چت ویژوال استودیو کد دسترسی پیدا کنید. ما می‌توانیم بر اساس این فرآیند توسعه دهیم.

![diagram](../../../../../../translated_images/diagram.e17900e549fa305114e13994f4091c34860163aaff8e67d206550bfd01bcb004.fa.png)

این سناریوی توسعه می‌تواند از دسترسی به API مدل‌های شخص ثالث (مانند مدل‌های GitHub، Azure Model Catalog و سرویس‌های خودساخته بر اساس مدل‌های متن‌باز) پشتیبانی کند و همچنین می‌تواند از مدل‌های gpt-35-turbo، gpt-4 و gpt-4o ارائه‌شده توسط GitHub Copilot استفاده کند.

## **اضافه کردن یک Agent با نام @phicoding بر اساس Phi-3.5**

ما تلاش می‌کنیم قابلیت‌های برنامه‌نویسی Phi-3.5 را برای انجام وظایف نوشتن کد، تولید کد از تصاویر و دیگر کارها ادغام کنیم. یک Agent ساخته‌شده حول محور Phi-3.5 - @PHI را کامل می‌کنیم. موارد زیر برخی از قابلیت‌ها هستند:

1. تولید یک معرفی از خود بر اساس GPT-4o ارائه‌شده توسط GitHub Copilot از طریق دستور **@phicoding /help**.

2. تولید کد برای زبان‌های برنامه‌نویسی مختلف بر اساس **Phi-3.5-mini-instruct (128k)** از طریق دستور **@phicoding /gen**.

3. تولید کد بر اساس **Phi-3.5-vision-instruct (128k)** و تکمیل تصویر از طریق دستور **@phicoding /image**.

![arch](../../../../../../translated_images/arch.c302d58012f0988b02f2275e24d8d21259899ef827d8a7579daecd1dd8b83ffd.fa.png)

## **مراحل مرتبط**

1. نصب پشتیبانی از توسعه افزونه ویژوال استودیو کد با استفاده از npm.

```bash

npm install --global yo generator-code 

```

2. ایجاد یک افزونه ویژوال استودیو کد (با استفاده از حالت توسعه تایپ‌اسکریپت، با نام phiext).

```bash

yo code 

```

3. باز کردن پروژه ایجادشده و تغییر فایل package.json. در اینجا دستورالعمل‌ها و تنظیمات مرتبط، همچنین پیکربندی مدل‌های GitHub آورده شده است. توجه داشته باشید که باید توکن مدل‌های GitHub خود را اینجا اضافه کنید.

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

4. تغییر فایل src/extension.ts.

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

6. اجرا.

***/help***

![help](../../../../../../translated_images/help.e26759fe1e92cea3e8788b2157e4383f621254ce001ba4ef6d35fce1e0667e55.fa.png)

***@phicoding /help***

![agenthelp](../../../../../../translated_images/agenthelp.f249f33c3fa449e0a779c78e3c2f3a65820702c03129e52a81a8df369443e413.fa.png)

***@phicoding /gen***

![agentgen](../../../../../../translated_images/agentgen.90c9cb76281be28a6cfdccda08f65043579ef4730a818c34e6f33ab6eb90e38c.fa.png)

***@phicoding /image***

![agentimage](../../../../../../translated_images/agentimage.db0cc3d3bd0ee494170ebd2623623e1012eb9f5786436439e2e36b91ca163172.fa.png)

می‌توانید کد نمونه را دانلود کنید: [کلیک کنید](../../../../../../code/09.UpdateSamples/Aug/vscode)

## **منابع**

1. ثبت‌نام در مدل‌های GitHub [https://gh.io/models](https://gh.io/models)

2. یادگیری توسعه افزونه ویژوال استودیو کد [https://code.visualstudio.com/api/get-started/your-first-extension](https://code.visualstudio.com/api/get-started/your-first-extension)

3. یادگیری درباره API چت ویژوال استودیو کد [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat)

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما تلاش می‌کنیم تا دقت را حفظ کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌ها باشند. سند اصلی به زبان مادری آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، توصیه می‌شود از ترجمه حرفه‌ای انسانی استفاده کنید. ما مسئولیتی در قبال سوء تفاهم‌ها یا برداشت‌های نادرست ناشی از استفاده از این ترجمه نداریم.