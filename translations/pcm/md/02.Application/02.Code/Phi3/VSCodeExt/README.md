# **Build your own Visual Studio Code GitHub Copilot Chat wit Microsoft Phi-3 Family**

You don use di workspace agent for GitHub Copilot Chat before? You wan build your own team code agent? Dis hands-on lab hope to join di open source model to build enterprise-level code business agent.

## **Foundation**

### **Why choose Microsoft Phi-3**

Phi-3 na family series, e get phi-3-mini, phi-3-small, and phi-3-medium wey base on different training parameters for text generation, dialogue completion, and code generation. E still get phi-3-vision wey base on Vision. E good for enterprises or different teams to create offline generative AI solutions.

Recommended make you read dis link [https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md](https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md)

### **Microsoft GitHub Copilot Chat**

GitHub Copilot Chat extension dey give you chat interface wey you fit interact wit GitHub Copilot and get answers to coding-related questions directly inside VS Code, no need to waka search documentation or online forums.

Copilot Chat fit use syntax highlighting, indentation, and other formatting features to make di generated response clear. Depending on di kind question wey user ask, di result fit get links to context wey Copilot use generate di response, like source code files or documentation, or buttons to access VS Code functions.

- Copilot Chat join your developer flow and dey give you help where you need am:

- Start inline chat conversation straight from editor or terminal if you need help while you dey do code

- Use di Chat view get AI assistant for side to help you anytime

- Launch Quick Chat ask quick question and quickly return to wetin you dey do

You fit use GitHub Copilot Chat for plenty scenarios, like:

- Answer coding questions on how to best solve problem

- Explain another person code and suggest better way

- Propose code fixes

- Generate unit test cases

- Generate code documentation

Recommended make you read dis link [https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/copilot-chat?WT.mc_id=aiml-137032-kinfeylo)


###  **Microsoft GitHub Copilot Chat @workspace**

If you use **@workspace** for Copilot Chat, e fit let you ask questions about your whole codebase. Based on the question, Copilot sabi find relevant files and symbols and e go use dem as links and code examples for answer.

To answer your question, **@workspace** de search all di places wey developer sabi use when e dey waka inside codebase for VS Code:

- All files inside workspace, except files wey .gitignore don ignore

- Directory structure with nested folders and file names

- GitHub code search index if workspace na GitHub repo and e dey indexed by code search

- Symbols and definitions for workspace

- Di text wey you select or wetin dey visible for active editor

Note: .gitignore no go work if you get file open or you select text inside ignored file.

Recommended make you read dis link [[https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/workspace-context?WT.mc_id=aiml-137032-kinfeylo)]


## **Know more about dis Lab**

GitHub Copilot don improve programming efficiency for enterprises well well, and every enterprise wan customize di relevant functions of GitHub Copilot. Plenty enterprises don customize Extensions wey resemble GitHub Copilot based on their own business cases and open source models. For enterprises, custom Extensions easier to control but e fit affect user experience too. After all, GitHub Copilot get strong functions for general cases and professional settings. If experience fit remain consistent, e go better to customize enterprise own Extension. GitHub Copilot Chat provide APIs for enterprises to expand Chat experience. To maintain consistent experience and still get customized functions go make user experience better.

Dis lab mainly dey use Phi-3 model join local NPU and Azure hybrid to build custom Agent inside GitHub Copilot Chat ***@PHI3*** to help enterprise developers complete code generation***(@PHI3 /gen)*** and make code based on images ***(@PHI3 /img)***.

![PHI3](../../../../../../../translated_images/pcm/cover.1017ebc9a7c46d09.webp)

### ***Note:***

Dis lab dey run now for AIPC of Intel CPU and Apple Silicon. We go continue update for Qualcomm NPU version.


## **Lab**


| Name | Description | AIPC | Apple |
| ------------ | ----------- | -------- |-------- |
| Lab0 - Installations(✅) | Configure and install related environments and installation tools | [Go](./HOL/AIPC/01.Installations.md) |[Go](./HOL/Apple/01.Installations.md) |
| Lab1 - Run Prompt flow with Phi-3-mini (✅) | Join AIPC / Apple Silicon together, use local NPU to create code generation wit Phi-3-mini | [Go](./HOL/AIPC/02.PromptflowWithNPU.md) |  [Go](./HOL/Apple/02.PromptflowWithMLX.md) |
| Lab2 - Deploy Phi-3-vision on Azure Machine Learning Service(✅) | Generate code by deploying Azure Machine Learning Service's Model Catalog - Phi-3-vision image | [Go](./HOL/AIPC/03.DeployPhi3VisionOnAzure.md) |[Go](./HOL/Apple/03.DeployPhi3VisionOnAzure.md) |
| Lab3 - Create a @phi-3 agent in GitHub Copilot Chat(✅)  | Create custom Phi-3 agent inside GitHub Copilot Chat to complete code generation, graph generation code, RAG, etc. | [Go](./HOL/AIPC/04.CreatePhi3AgentInVSCode.md) | [Go](./HOL/Apple/04.CreatePhi3AgentInVSCode.md) |
| Sample Code (✅)  | Download sample code | [Go](../../../../../../../code/07.Lab/01/AIPC) | [Go](../../../../../../../code/07.Lab/01/Apple) |


## **Resources**

1. Phi-3 Cookbook [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook)

2. Learn more about GitHub Copilot [https://learn.microsoft.com/training/paths/copilot/](https://learn.microsoft.com/training/paths/copilot/?WT.mc_id=aiml-137032-kinfeylo)

3. Learn more about GitHub Copilot Chat [https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/](https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/?WT.mc_id=aiml-137032-kinfeylo)

4. Learn more about GitHub Copilot Chat API [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat?WT.mc_id=aiml-137032-kinfeylo)

5. Learn more about Microsoft Foundry [https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/](https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/?WT.mc_id=aiml-137032-kinfeylo)

6. Learn more about Microsoft Foundry's Model Catalog [https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you sabi say automated translations fit get errors or mistakes. Di original document for im own native language na di correct one wey you suppose use. For important tin dem, na professional human translation good pass. We no go responsible for any wahala or wrong understanding wey fit happen from di use of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->