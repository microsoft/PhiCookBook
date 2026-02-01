# **Visual Studio Code Chat Copilot Agent ஐ GitHub Models மூலம் Phi-3.5 கொண்டு உருவாக்குவது**

Visual Studio Code Copilot ஐ நீங்கள் பயன்படுத்துகிறீர்களா? குறிப்பாக Chat-இல், நீங்கள் பல்வேறு agents-ஐ பயன்படுத்தி Visual Studio Code-ல் திட்டங்களை உருவாக்க, எழுத மற்றும் பராமரிக்க திறனை மேம்படுத்தலாம். Visual Studio Code API-ஐ வழங்குகிறது, இது நிறுவனங்கள் மற்றும் தனிநபர்களுக்கு தங்கள் தொழில்துறை தேவைகளுக்கு ஏற்ப தனிப்பட்ட agents-ஐ உருவாக்க அனுமதிக்கிறது. இந்த கட்டுரையில், **Phi-3.5-mini-instruct (128k)** மற்றும் **Phi-3.5-vision-instruct (128k)** ஆகிய GitHub Models-ஐ பயன்படுத்தி உங்கள் சொந்த Visual Studio Code Agent-ஐ உருவாக்குவது குறித்து கவனம் செலுத்துவோம்.

## **GitHub Models-ல் Phi-3.5 பற்றி**

Phi-3/3.5-mini-instruct மாடல் குடும்பத்தில் உள்ள Phi-3/3.5-க்கு வலுவான code புரிதல் மற்றும் உருவாக்க திறன்கள் உள்ளன, மேலும் Gemma-2-9b மற்றும் Mistral-Nemo-12B-instruct-2407-க்கு மேலான பலன்கள் உள்ளன.

![codegen](../../../../../../imgs/02/phi35vscode/codegen.png)

GitHub Models-இன் சமீபத்திய பதிப்புகள் ஏற்கனவே Phi-3.5-mini-instruct (128k) மற்றும் Phi-3.5-vision-instruct (128k) மாடல்களுக்கு அணுகலை வழங்குகின்றன. டெவலப்பர்கள் OpenAI SDK, Azure AI Inference SDK மற்றும் REST API மூலம் அவற்றை அணுகலாம்.

![gh](../../../../../../imgs/02/phi35vscode/gh.png)

***குறிப்பு:*** Azure AI Inference SDK-ஐ இங்கே பயன்படுத்த பரிந்துரைக்கப்படுகிறது, ஏனெனில் இது உற்பத்தி சூழலில் Azure Model Catalog-இன் மாற்றத்துடன் சிறப்பாக செயல்படுகிறது.

GitHub Models-இன் **Phi-3.5-mini-instruct (128k)** மற்றும் **Phi-3.5-vision-instruct (128k)** மாடல்களுடன் இணைக்கப்பட்ட பிறகு code உருவாக்கச் சூழலில் கிடைத்த முடிவுகள் கீழே கொடுக்கப்பட்டுள்ளன, மேலும் கீழே உள்ள உதாரணங்களுக்கு தயாராகவும் உள்ளது.

**Demo: GitHub Models Phi-3.5-mini-instruct (128k) Prompt-இல் இருந்து code உருவாக்குகிறது** ([இந்த இணைப்பை கிளிக் செய்யவும்](../../../../../../code/09.UpdateSamples/Aug/ghmodel_phi35_instruct_demo.ipynb))

**Demo: GitHub Models Phi-3.5-vision-instruct (128k) Image-இல் இருந்து code உருவாக்குகிறது** ([இந்த இணைப்பை கிளிக் செய்யவும்](../../../../../../code/09.UpdateSamples/Aug/ghmodel_phi35_vision_demo.ipynb))

## **GitHub Copilot Chat Agent பற்றி**

GitHub Copilot Chat Agent code அடிப்படையில் பல்வேறு திட்டச் சூழல்களில் பல்வேறு பணிகளை முடிக்க முடியும். இந்த அமைப்பில் workspace, github, terminal, vscode ஆகிய நான்கு agents உள்ளன.

![agent](../../../../../../imgs/02/phi35vscode/agent.png)

Agent-இன் பெயரை '@' கொண்டு சேர்த்தால், நீங்கள் விரைவாக தொடர்புடைய பணிகளை முடிக்கலாம். நிறுவனங்களுக்கு, தங்கள் சொந்த தொழில்துறை சார்ந்த உள்ளடக்கங்களை (தேவைகள், coding, test specifications, release போன்றவை) சேர்த்தால், GitHub Copilot அடிப்படையில் சக்திவாய்ந்த தனியார் enterprise functions-ஐ பெற முடியும்.

Visual Studio Code Chat Agent இப்போது அதன் API-ஐ அதிகாரப்பூர்வமாக வெளியிட்டுள்ளது, இது நிறுவனங்கள் அல்லது நிறுவன டெவலப்பர்களுக்கு software business ecosystems அடிப்படையில் agents-ஐ உருவாக்க அனுமதிக்கிறது. Visual Studio Code Extension Development முறையின் அடிப்படையில், Visual Studio Code Chat Agent API-யின் இடைமுகத்தை எளிதாக அணுகலாம். இந்த செயல்முறையின் அடிப்படையில் நாம் உருவாக்கலாம்.

![diagram](../../../../../../imgs/02/phi35vscode/diagram.png)

இந்த வளர்ச்சி சூழல் மூலமாக GitHub Models, Azure Model Catalog மற்றும் open source models அடிப்படையில் உருவாக்கப்பட்ட services போன்ற மூன்றாம் தரப்பு மாடல் API-களை அணுக முடியும். மேலும் GitHub Copilot வழங்கும் gpt-35-turbo, gpt-4 மற்றும் gpt-4o மாடல்களையும் பயன்படுத்த முடியும்.

## **Phi-3.5 அடிப்படையில் @phicoding Agent ஐ சேர்க்கவும்**

Phi-3.5-ன் programming திறன்களை ஒருங்கிணைத்து code எழுதுதல், image-ல் இருந்து code உருவாக்குதல் மற்றும் பிற பணிகளை முடிக்க முயற்சிக்கிறோம். Phi-3.5-ஐ மையமாகக் கொண்ட @PHI Agent-ஐ உருவாக்குகிறோம். இதன் சில செயல்பாடுகள் கீழே கொடுக்கப்பட்டுள்ளன:

1. **@phicoding /help** கட்டளையின் மூலம் GitHub Copilot வழங்கும் GPT-4o அடிப்படையில் ஒரு சுய அறிமுகத்தை உருவாக்குதல்.

2. **@phicoding /gen** கட்டளையின் மூலம் **Phi-3.5-mini-instruct (128k)** அடிப்படையில் பல்வேறு programming மொழிகளுக்கான code உருவாக்குதல்.

3. **@phicoding /image** கட்டளையின் மூலம் **Phi-3.5-vision-instruct (128k)** மற்றும் image completion அடிப்படையில் code உருவாக்குதல்.

![arch](../../../../../../imgs/02/phi35vscode/arch.png)

## **தொடர்புடைய படிகள்**

1. npm மூலம் Visual Studio Code Extension Development ஆதரவை நிறுவவும்.

```bash

npm install --global yo generator-code 

```


2. Visual Studio Code Extension plugin ஐ உருவாக்கவும் (Typescript Development Mode-ஐ பயன்படுத்தி, phiext என பெயரிடவும்).

```bash

yo code 

```


3. உருவாக்கப்பட்ட திட்டத்தை திறந்து package.json-ஐ மாற்றவும். இங்கே தொடர்புடைய வழிமுறைகள் மற்றும் GitHub Models-இன் கட்டமைப்புகள் உள்ளன. உங்கள் GitHub Models token-ஐ இங்கே சேர்க்க வேண்டும்.

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


4. src/extension.ts-ஐ மாற்றவும்.

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


6. இயக்குதல்.

***/help***

![help](../../../../../../imgs/02/phi35vscode/help.png)

***@phicoding /help***

![agenthelp](../../../../../../imgs/02/phi35vscode/agenthelp.png)

***@phicoding /gen***

![agentgen](../../../../../../imgs/02/phi35vscode/agentgen.png)

***@phicoding /image***

![agentimage](../../../../../../imgs/02/phi35vscode/agentimage.png)

உதாரண code-ஐ பதிவிறக்கலாம்: [கிளிக் செய்யவும்](../../../../../../code/09.UpdateSamples/Aug/vscode)

## **வளங்கள்**

1. GitHub Models-க்கு பதிவு செய்யவும் [https://gh.io/models](https://gh.io/models)

2. Visual Studio Code Extension Development பற்றி கற்றுக்கொள்ளவும் [https://code.visualstudio.com/api/get-started/your-first-extension](https://code.visualstudio.com/api/get-started/your-first-extension)

3. Visual Studio Code Copilot Chat API பற்றி கற்றுக்கொள்ளவும் [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat)

---

**குறிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையைப் பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கிறோம், ஆனால் தானியக்க மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறான தகவல்கள் இருக்கக்கூடும் என்பதை தயவுசெய்து கவனத்தில் கொள்ளுங்கள். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.