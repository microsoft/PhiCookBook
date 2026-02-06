# **GitHub Modelleri ile Phi-3.5 kullanarak kendi Visual Studio Code Chat Copilot Ajanınızı Oluşturun**

Visual Studio Code Copilot kullanıyor musunuz? Özellikle Chat bölümünde, Visual Studio Code’da projeleri oluşturma, yazma ve sürdürme yeteneğini geliştirmek için farklı ajanlar kullanabilirsiniz. Visual Studio Code, şirketlerin ve bireylerin işlerine göre farklı ajanlar oluşturmasına olanak tanıyan bir API sağlar ve böylece farklı özel alanlarda yeteneklerini genişletebilirler. Bu yazıda, GitHub Modelleri’nin **Phi-3.5-mini-instruct (128k)** ve **Phi-3.5-vision-instruct (128k)** modellerine odaklanarak kendi Visual Studio Code Ajanınızı nasıl oluşturacağınızı anlatacağız.

## **GitHub Modellerindeki Phi-3.5 Hakkında**

Phi-3/3.5 Ailesindeki Phi-3/3.5-mini-instruct modelinin güçlü kod anlama ve üretme yeteneklerine sahip olduğunu ve Gemma-2-9b ile Mistral-Nemo-12B-instruct-2407 modellerine göre avantajları olduğunu biliyoruz.

![codegen](../../../../../../translated_images/tr/codegen.53be1150ee54d969.webp)

En son GitHub Modelleri, Phi-3.5-mini-instruct (128k) ve Phi-3.5-vision-instruct (128k) modellerine erişim sağlamaktadır. Geliştiriciler bu modellere OpenAI SDK, Azure AI Inference SDK ve REST API üzerinden ulaşabilirler.

![gh](../../../../../../translated_images/tr/gh.459640c7ceba01d5.webp)

***Not:*** Üretim ortamında Azure Model Catalog ile daha iyi geçiş yapabildiği için burada Azure AI Inference SDK kullanılması önerilir.

Aşağıda, GitHub Modelleri ile entegre edildikten sonra kod üretme senaryosunda **Phi-3.5-mini-instruct (128k)** ve **Phi-3.5-vision-instruct (128k)** modellerinin sonuçları yer almakta ve sonraki örnekler için hazırlık yapılmaktadır.

**Demo: GitHub Modelleri Phi-3.5-mini-instruct (128k) ile Prompt’tan Kod Üretimi** ([bu bağlantıya tıklayın](../../../../../../code/09.UpdateSamples/Aug/ghmodel_phi35_instruct_demo.ipynb))

**Demo: GitHub Modelleri Phi-3.5-vision-instruct (128k) ile Görüntüden Kod Üretimi** ([bu bağlantıya tıklayın](../../../../../../code/09.UpdateSamples/Aug/ghmodel_phi35_vision_demo.ipynb))


## **GitHub Copilot Chat Ajanı Hakkında**

GitHub Copilot Chat Ajanı, kod temelinde farklı proje senaryolarında çeşitli görevleri tamamlayabilir. Sistem dört ajan içerir: workspace, github, terminal, vscode

![agent](../../../../../../translated_images/tr/agent.3dbb06228f9a6189.webp)

Ajan adını ‘@’ ile ekleyerek ilgili işi hızlıca tamamlayabilirsiniz. Kuruluşlar için, gereksinimler, kodlama, test spesifikasyonları ve sürüm gibi kendi işlerine dair içerikleri ekleyerek GitHub Copilot tabanlı daha güçlü kurumsal özel fonksiyonlara sahip olunabilir.

Visual Studio Code Chat Ajanı artık resmi olarak API’sini yayınladı ve bu sayede şirketler veya kurumsal geliştiriciler farklı yazılım iş ekosistemlerine dayalı ajanlar geliştirebilir. Visual Studio Code Extension Development geliştirme yöntemi temel alınarak, Visual Studio Code Chat Ajan API arayüzüne kolayca erişilebilir. Bu süreç üzerinden geliştirme yapabiliriz.

![diagram](../../../../../../translated_images/tr/diagram.ca70d2866762f115.webp)

Geliştirme senaryosu, üçüncü taraf model API’lerine (örneğin GitHub Modelleri, Azure Model Catalog ve açık kaynak modeller üzerine kurulu kendi servisleriniz) erişimi destekler ve ayrıca GitHub Copilot tarafından sağlanan gpt-35-turbo, gpt-4 ve gpt-4o modellerini kullanabilir.

## **Phi-3.5 Tabanlı @phicoding Ajanı Ekleme**

Phi-3.5’in programlama yeteneklerini kod yazma, görüntüden kod üretme ve diğer görevleri tamamlamak için entegre etmeye çalışıyoruz. Phi-3.5 etrafında oluşturulmuş bir Ajan - @PHI tamamlandı, işte bazı fonksiyonları:

1. GitHub Copilot tarafından sağlanan GPT-4o tabanlı kendini tanıtma metni oluşturma, **@phicoding /help** komutu ile

2. **Phi-3.5-mini-instruct (128k)** tabanlı farklı programlama dilleri için kod üretme, **@phicoding /gen** komutu ile

3. **Phi-3.5-vision-instruct (128k)** ve görüntü tamamlama tabanlı kod üretme, **@phicoding /image** komutu ile

![arch](../../../../../../translated_images/tr/arch.5a58a0adfa959a2d.webp)

## **İlgili Adımlar**

1. npm kullanarak Visual Studio Code Extension geliştirme desteğini kurun

```bash

npm install --global yo generator-code 

```
2. Visual Studio Code Extension eklentisi oluşturun (Typescript geliştirme modu kullanarak, adı phiext olsun)

```bash

yo code 

```

3. Oluşturduğunuz projeyi açın ve package.json dosyasını düzenleyin. Burada ilgili talimatlar ve konfigürasyonlar ile GitHub Modelleri ayarları yer almakta. GitHub Modelleri token’ınızı buraya eklemeniz gerektiğini unutmayın.

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

4. src/extension.ts dosyasını düzenleyin

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

6. Çalıştırma

***/help***

![help](../../../../../../translated_images/tr/help.04c134d2bf9a9541.webp)

***@phicoding /help***

![agenthelp](../../../../../../translated_images/tr/agenthelp.60c68767c941a3fe.webp)

***@phicoding /gen***

![agentgen](../../../../../../translated_images/tr/agentgen.a16e7735790f764b.webp)

***@phicoding /image***

![agentimage](../../../../../../translated_images/tr/agentimage.f5cb52b45ab7d0d1.webp)

Örnek kodları indirebilirsiniz: [tıklayın](../../../../../../code/09.UpdateSamples/Aug/vscode)

## **Kaynaklar**

1. GitHub Modellerine kayıt olun [https://gh.io/models](https://gh.io/models)

2. Visual Studio Code Extension Geliştirmeyi öğrenin [https://code.visualstudio.com/api/get-started/your-first-extension](https://code.visualstudio.com/api/get-started/your-first-extension)

3. Visual Studio Code Copilot Chat API hakkında bilgi edinin [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat)

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.