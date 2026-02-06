# **Make your own Visual Studio Code GitHub Copilot Chat wit Microsoft Phi-3 Family**

You don don use the workspace agent for GitHub Copilot Chat? You wan build your team code agent? Dis hands-on lab dey try combine open source model make e fit build enterprise-level code business agent.

## **Foundation**

### **Why you go choose Microsoft Phi-3**

Phi-3 na family series wey get phi-3-mini, phi-3-small, and phi-3-medium wey dem train with different parameters for text generation, dialogue completion, and code generation. E still get phi-3-vision wey base on Vision. E good for enterprises or different teams wey wan create offline generative AI solutions.

E good make you read dis link [https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md](https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md)

### **Microsoft GitHub Copilot Chat**

The GitHub Copilot Chat extension dey give you chat interface wey allow you interact with GitHub Copilot and get answers to coding-related questions directly inside VS Code, no need make you dey waka through documentation or dey search forum for internet.

Copilot Chat fit use syntax highlighting, indentation, and other formatting features make the generated response clear. Depending on the kain question wey user ask, the result fit get links to context wey Copilot use to generate the response, like source code files or documentation, or buttons wey dey access VS Code functionality.

- Copilot Chat dey integrate inside your developer flow and dey give you help where you need am:

- Start inline chat conversation directly from the editor or the terminal to get help while you dey code

- Use the Chat view to get AI assistant for the side to help you anytime

- Launch Quick Chat to ask small question quickly and return to wetin you dey do

You fit use GitHub Copilot Chat for different scenarios, like:

- Answer coding questions on how best to solve problem

- Explain somebody else code and suggest better ways

- Propose code fixes

- Generate unit test cases

- Generate code documentation

Recommended to read this link [https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/copilot-chat?WT.mc_id=aiml-137032-kinfeylo)


###  **Microsoft GitHub Copilot Chat @workspace**

If you reference **@workspace** for Copilot Chat e dey allow you ask questions about your whole codebase. Based on the question, Copilot go sabi retrieve relevant files and symbols, wey e go then use for the answer as links and code examples. 

To answer your question, **@workspace** dey search through the same sources wey developer go use when dem dey navigate codebase for VS Code:

- All files for the workspace, except files wey .gitignore don ignore

- Directory structure with nested folders and file names

- GitHub's code search index, if the workspace na GitHub repository and e don dey indexed by code search

- Symbols and definitions wey dey the workspace

- Currently selected text or visible text wey dey the active editor

Note: .gitignore no go block am if you open the file or you get text wey you don select inside ignored file.

Recommended to read this link [[https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/workspace-context?WT.mc_id=aiml-137032-kinfeylo)]


## **Know more about this Lab**

GitHub Copilot don improve programming efficiency for enterprises wella, and every enterprise dey hope to customize relevant features of GitHub Copilot. Plenty enterprises don customize Extensions like GitHub Copilot based on their own business needs and open source models. For enterprises, customized Extensions dey easier to control, but e fit still affect user experience. After all, GitHub Copilot get strong power for general scenarios and professional work. If the experience fit remain consistent, e go better to customize the enterprise own Extension. GitHub Copilot Chat dey provide APIs wey enterprises fit use to expand the Chat experience. Maintain consistent experience plus get customized functions na beta user experience.

This lab mainly dey use the Phi-3 model combine with local NPU and Azure hybrid make dem build custom Agent for GitHub Copilot Chat ***@PHI3*** to help enterprise developers finish code generation***(@PHI3 /gen)*** and generate code based on images ***(@PHI3 /img)***.

![PHI3](../../../../../../../translated_images/cover.1017ebc9a7c46d09.pcm.png)

### ***Note:*** 

This lab dey implemented for AIPC on Intel CPU and Apple Silicon now. We go continue to update the Qualcomm NPU version.

## **Lab**


| Name | Description | AIPC | Apple |
| ------------ | ----------- | -------- |-------- |
| Lab0 - Installations(✅) | Configure and install related environments and installation tools | [Go](./HOL/AIPC/01.Installations.md) |[Go](./HOL/Apple/01.Installations.md) |
| Lab1 - Run Prompt flow with Phi-3-mini (✅) | Combined with AIPC / Apple Silicon, using local NPU to create code generation through Phi-3-mini | [Go](./HOL/AIPC/02.PromptflowWithNPU.md) |  [Go](./HOL/Apple/02.PromptflowWithMLX.md) |
| Lab2 - Deploy Phi-3-vision on Azure Machine Learning Service(✅) | Generate code by deploying Azure Machine Learning Service's Model Catalog - Phi-3-vision image | [Go](./HOL/AIPC/03.DeployPhi3VisionOnAzure.md) |[Go](./HOL/Apple/03.DeployPhi3VisionOnAzure.md) |
| Lab3 - Create a @phi-3 agent in GitHub Copilot Chat(✅)  | Create a custom Phi-3 agent in GitHub Copilot Chat to complete code generation, graph generation code, RAG, etc. | [Go](./HOL/AIPC/04.CreatePhi3AgentInVSCode.md) | [Go](./HOL/Apple/04.CreatePhi3AgentInVSCode.md) |
| Sample Code (✅)  | Download sample code | [Go](../../../../../../../code/07.Lab/01/AIPC) | [Go](../../../../../../../code/07.Lab/01/Apple) |


## **Resources**

1. Phi-3 Cookbook [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook)

2. Make you sabi more about GitHub Copilot [https://learn.microsoft.com/training/paths/copilot/](https://learn.microsoft.com/training/paths/copilot/?WT.mc_id=aiml-137032-kinfeylo)

3. Make you sabi more about GitHub Copilot Chat [https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/](https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/?WT.mc_id=aiml-137032-kinfeylo)

4. Make you sabi more about GitHub Copilot Chat API [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat?WT.mc_id=aiml-137032-kinfeylo)

5. Make you sabi more about Azure AI Foundry [https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/](https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/?WT.mc_id=aiml-137032-kinfeylo)

6. Make you sabi more about Azure AI Foundry's Model Catalog [https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Disclaimer:
Dis document na AI (Co‑op Translator) translate am. Even though we dey try make everything correct, abeg note say automatic translation fit get errors or wrong meaning. Di original document for im own language remain di main/official source. For important matter, e better make professional human translator check am. We no dey liable for any misunderstanding or wrong interpretation wey fit come from dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->