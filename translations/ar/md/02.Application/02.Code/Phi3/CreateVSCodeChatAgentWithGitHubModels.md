<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "35bf81388ac6917277b8d9a0c39bdc70",
  "translation_date": "2025-03-27T11:31:45+00:00",
  "source_file": "md\\02.Application\\02.Code\\Phi3\\CreateVSCodeChatAgentWithGitHubModels.md",
  "language_code": "ar"
}
-->
# **إنشاء وكيل Visual Studio Code Chat Copilot الخاص بك باستخدام Phi-3.5 من نماذج GitHub**

هل تستخدم Visual Studio Code Copilot؟ خاصة في الدردشة، يمكنك استخدام وكلاء مختلفين لتحسين القدرة على إنشاء المشاريع وكتابتها وصيانتها في Visual Studio Code. يوفر Visual Studio Code واجهة API تسمح للشركات والأفراد بإنشاء وكلاء مختلفين بناءً على احتياجاتهم لتوسيع قدراتهم في مجالات خاصة. في هذه المقالة، سنركز على **Phi-3.5-mini-instruct (128k)** و **Phi-3.5-vision-instruct (128k)** من نماذج GitHub لإنشاء وكيل Visual Studio Code الخاص بك.

## **عن Phi-3.5 في نماذج GitHub**

نعلم أن Phi-3/3.5-mini-instruct في عائلة Phi-3/3.5 يتمتع بقدرات قوية لفهم الكود وتوليده، ويتفوق على Gemma-2-9b و Mistral-Nemo-12B-instruct-2407.

![codegen](../../../../../../translated_images/codegen.eede87d45b849fd8738a7789f44ec3b81c4907d23eebd2b0e3dbd62c939c7cb9.ar.png)

توفر نماذج GitHub الحديثة بالفعل إمكانية الوصول إلى نماذج Phi-3.5-mini-instruct (128k) و Phi-3.5-vision-instruct (128k). يمكن للمطورين الوصول إليها من خلال OpenAI SDK، Azure AI Inference SDK، و REST API.

![gh](../../../../../../translated_images/gh.7fa589617baffe1b3f8a044fb29ee1b46f02645a47f3caa57d493768512b94e8.ar.png)

***ملاحظة:*** يُوصى باستخدام Azure AI Inference SDK هنا، لأنه يمكنه التبديل بشكل أفضل مع Azure Model Catalog في بيئة الإنتاج.

فيما يلي نتائج **Phi-3.5-mini-instruct (128k)** و **Phi-3.5-vision-instruct (128k)** في سيناريو توليد الكود بعد التكامل مع نماذج GitHub، وأيضاً التحضير للأمثلة التالية:

**عرض: نموذج GitHub Phi-3.5-mini-instruct (128k) يولد الكود من Prompt** ([اضغط هنا](../../../../../../code/09.UpdateSamples/Aug/ghmodel_phi35_instruct_demo.ipynb))

**عرض: نموذج GitHub Phi-3.5-vision-instruct (128k) يولد الكود من صورة** ([اضغط هنا](../../../../../../code/09.UpdateSamples/Aug/ghmodel_phi35_vision_demo.ipynb))

## **عن وكيل GitHub Copilot Chat**

يمكن لوكيل GitHub Copilot Chat إكمال مهام مختلفة في سيناريوهات مشاريع مختلفة بناءً على الكود. النظام يحتوي على أربعة وكلاء: workspace، github، terminal، vscode.

![agent](../../../../../../translated_images/agent.19ff410949975e96c38aa5763545604a33dc923968b6abcd200ff8590c62efd7.ar.png)

من خلال إضافة اسم الوكيل مع ‘@’، يمكنك إكمال العمل المطلوب بسرعة. بالنسبة للشركات، إذا قمت بإضافة محتوى متعلق بأعمالك مثل المتطلبات، البرمجة، مواصفات الاختبار، والإصدار، يمكنك الحصول على وظائف قوية خاصة بالشركات بناءً على GitHub Copilot.

تم إصدار واجهة API الخاصة بـ Visual Studio Code Chat Agent رسميًا الآن، مما يسمح للشركات أو مطوري الشركات بتطوير وكلاء بناءً على أنظمة بيئية مختلفة للأعمال. بناءً على طريقة تطوير ملحقات Visual Studio Code، يمكنك بسهولة الوصول إلى واجهة Visual Studio Code Chat Agent API. يمكننا التطوير بناءً على هذه العملية.

![diagram](../../../../../../translated_images/diagram.e17900e549fa305114e13994f4091c34860163aaff8e67d206550bfd01bcb004.ar.png)

يمكن لسيناريو التطوير دعم الوصول إلى واجهات API لنماذج الطرف الثالث (مثل GitHub Models، Azure Model Catalog، والخدمات المبنية ذاتيًا بناءً على نماذج مفتوحة المصدر)، ويمكنه أيضًا استخدام نماذج gpt-35-turbo، gpt-4، و gpt-4o التي يوفرها GitHub Copilot.

## **إضافة وكيل @phicoding بناءً على Phi-3.5**

نحاول دمج قدرات البرمجة لـ Phi-3.5 لإكمال كتابة الكود، توليد الكود من الصور، والمهام الأخرى. اكتمال وكيل مبني حول Phi-3.5 - @PHI، فيما يلي بعض الوظائف:

1. توليد مقدمة ذاتية بناءً على GPT-4o الذي يوفره GitHub Copilot من خلال أمر **@phicoding /help**.

2. توليد الكود للغات البرمجة المختلفة بناءً على **Phi-3.5-mini-instruct (128k)** من خلال أمر **@phicoding /gen**.

3. توليد الكود بناءً على **Phi-3.5-vision-instruct (128k)** وإكمال الصور من خلال أمر **@phicoding /image**.

![arch](../../../../../../translated_images/arch.c302d58012f0988b02f2275e24d8d21259899ef827d8a7579daecd1dd8b83ffd.ar.png)

## **الخطوات ذات الصلة**

1. تثبيت دعم تطوير ملحقات Visual Studio Code باستخدام npm.

```bash

npm install --global yo generator-code 

```

2. إنشاء ملحق Visual Studio Code (باستخدام وضع تطوير Typescript، يسمى phiext).

```bash

yo code 

```

3. فتح المشروع الذي تم إنشاؤه وتعديل package.json. هنا التعليمات والتكوينات ذات الصلة، بالإضافة إلى تكوين نماذج GitHub. لاحظ أنه يجب إضافة رمز الوصول الخاص بنماذج GitHub هنا.

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

4. تعديل src/extension.ts.

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

6. التشغيل:

***/help***

![help](../../../../../../translated_images/help.e26759fe1e92cea3e8788b2157e4383f621254ce001ba4ef6d35fce1e0667e55.ar.png)

***@phicoding /help***

![agenthelp](../../../../../../translated_images/agenthelp.f249f33c3fa449e0a779c78e3c2f3a65820702c03129e52a81a8df369443e413.ar.png)

***@phicoding /gen***

![agentgen](../../../../../../translated_images/agentgen.90c9cb76281be28a6cfdccda08f65043579ef4730a818c34e6f33ab6eb90e38c.ar.png)

***@phicoding /image***

![agentimage](../../../../../../translated_images/agentimage.db0cc3d3bd0ee494170ebd2623623e1012eb9f5786436439e2e36b91ca163172.ar.png)

يمكنك تحميل الكود النموذجي: [اضغط هنا](../../../../../../code/09.UpdateSamples/Aug/vscode)

## **المصادر**

1. التسجيل في نماذج GitHub [https://gh.io/models](https://gh.io/models)

2. تعلم تطوير ملحقات Visual Studio Code [https://code.visualstudio.com/api/get-started/your-first-extension](https://code.visualstudio.com/api/get-started/your-first-extension)

3. تعلم عن واجهة Visual Studio Code Coilot Chat API [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat)

**إخلاء المسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو معلومات غير دقيقة. يجب اعتبار المستند الأصلي بلغته الأصلية هو المصدر الموثوق. بالنسبة للمعلومات الحرجة، يُوصى بالاستعانة بترجمة بشرية احترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة ناتجة عن استخدام هذه الترجمة.