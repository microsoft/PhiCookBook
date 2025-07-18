<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5c07bb4c3c89a36c9be332a065a9a33c",
  "translation_date": "2025-07-16T15:28:12+00:00",
  "source_file": "README.md",
  "language_code": "cs"
}
-->
# Phi Cookbook: Praktické příklady s modely Phi od Microsoftu

[![Otevřete a používejte ukázky v GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)  
[![Otevřít v Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub přispěvatelé](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)  
[![GitHub issues](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)  
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)  
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub sledující](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)  
[![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)  
[![GitHub hvězdy](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Azure AI Community Discord](https://dcbadge.vercel.app/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

Phi je řada open source AI modelů vyvinutých společností Microsoft.

Phi je v současnosti nejsilnější a nejefektivnější malý jazykový model (SLM) s velmi dobrými výsledky v mnoha jazycích, v oblasti uvažování, generování textu/chatů, kódování, obrázků, zvuku a dalších scénářů.

Phi můžete nasadit do cloudu nebo na edge zařízení a snadno s ním vytvářet generativní AI aplikace i s omezeným výpočetním výkonem.

Postupujte podle těchto kroků, abyste začali používat tyto zdroje:  
1. **Vytvořte fork repozitáře**: Klikněte na [![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)  
2. **Naklonujte repozitář**: `git clone https://github.com/microsoft/PhiCookBook.git`  
3. [**Připojte se ke komunitě Microsoft AI na Discordu a setkejte se s experty a dalšími vývojáři**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/cover.eb18d1b9605d754b30973f4e17c6e11ea4f8473d9686ee378d6e7b44e3c70ac7.cs.png)

### 🌐 Podpora více jazyků

#### Podporováno přes GitHub Action (automatizované a vždy aktuální)

[Francouzština](../fr/README.md) | [Španělština](../es/README.md) | [Němčina](../de/README.md) | [Ruština](../ru/README.md) | [Arabština](../ar/README.md) | [Perština (Fársí)](../fa/README.md) | [Urdu](../ur/README.md) | [Čínština (zjednodušená)](../zh/README.md) | [Čínština (tradiční, Macao)](../mo/README.md) | [Čínština (tradiční, Hongkong)](../hk/README.md) | [Čínština (tradiční, Tchaj-wan)](../tw/README.md) | [Japonština](../ja/README.md) | [Korejština](../ko/README.md) | [Hindština](../hi/README.md)  
[Bengálština](../bn/README.md) | [Maráthština](../mr/README.md) | [Nepálština](../ne/README.md) | [Paňdžábština (Gurmukhí)](../pa/README.md) | [Portugalština (Portugalsko)](../pt/README.md) | [Portugalština (Brazílie)](../br/README.md) | [Italština](../it/README.md) | [Polština](../pl/README.md) | [Turečtina](../tr/README.md) | [Řečtina](../el/README.md) | [Thajština](../th/README.md) | [Švédština](../sv/README.md) | [Dánština](../da/README.md) | [Norština](../no/README.md) | [Finština](../fi/README.md) | [Nizozemština](../nl/README.md) | [Hebrejština](../he/README.md) | [Vietnamština](../vi/README.md) | [Indonéština](../id/README.md) | [Malajština](../ms/README.md) | [Tagalog (Filipínština)](../tl/README.md) | [Svahilština](../sw/README.md) | [Maďarština](../hu/README.md) | [Čeština](./README.md) | [Slovenština](../sk/README.md) | [Rumunština](../ro/README.md) | [Bulharština](../bg/README.md) | [Srbština (cyrilice)](../sr/README.md) | [Chorvatština](../hr/README.md) | [Slovinština](../sl/README.md)

## Obsah

- Úvod  
  - [Vítejte v rodině Phi](./md/01.Introduction/01/01.PhiFamily.md)  
  - [Nastavení prostředí](./md/01.Introduction/01/01.EnvironmentSetup.md)  
  - [Pochopení klíčových technologií](./md/01.Introduction/01/01.Understandingtech.md)  
  - [Bezpečnost AI pro modely Phi](./md/01.Introduction/01/01.AISafety.md)  
  - [Podpora hardwaru Phi](./md/01.Introduction/01/01.Hardwaresupport.md)  
  - [Modely Phi a dostupnost na různých platformách](./md/01.Introduction/01/01.Edgeandcloud.md)  
  - [Použití Guidance-ai a Phi](./md/01.Introduction/01/01.Guidance.md)  
  - [Modely na GitHub Marketplace](https://github.com/marketplace/models)  
  - [Katalog modelů Azure AI](https://ai.azure.com)

- Inference Phi v různých prostředích  
    -  [Hugging face](./md/01.Introduction/02/01.HF.md)  
    -  [GitHub modely](./md/01.Introduction/02/02.GitHubModel.md)  
    -  [Azure AI Foundry Model Catalog](./md/01.Introduction/02/03.AzureAIFoundry.md)  
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)  
    -  [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)  
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)  
    -  [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md)

- Inference Phi Family  
    - [Inference Phi na iOS](./md/01.Introduction/03/iOS_Inference.md)  
    - [Inference Phi na Androidu](./md/01.Introduction/03/Android_Inference.md)  
    - [Inference Phi na Jetsonu](./md/01.Introduction/03/Jetson_Inference.md)  
    - [Inference Phi na AI PC](./md/01.Introduction/03/AIPC_Inference.md)  
    - [Inference Phi s Apple MLX Framework](./md/01.Introduction/03/MLX_Inference.md)  
    - [Inference Phi na lokálním serveru](./md/01.Introduction/03/Local_Server_Inference.md)  
    - [Inference Phi na vzdáleném serveru pomocí AI Toolkit](./md/01.Introduction/03/Remote_Interence.md)  
    - [Inference Phi s Rustem](./md/01.Introduction/03/Rust_Inference.md)  
    - [Inference Phi – Vision lokálně](./md/01.Introduction/03/Vision_Inference.md)  
    - [Inference Phi s Kaito AKS, Azure Containers (oficiální podpora)](./md/01.Introduction/03/Kaito_Inference.md)  
-  [Kvantiﬁkace Phi Family](./md/01.Introduction/04/QuantifyingPhi.md)  
    - [Kvantiﬁkace Phi-3.5 / 4 pomocí llama.cpp](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)  
    - [Kvantiﬁkace Phi-3.5 / 4 pomocí Generative AI rozšíření pro onnxruntime](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)  
    - [Kvantiﬁkace Phi-3.5 / 4 pomocí Intel OpenVINO](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)  
    - [Kvantiﬁkace Phi-3.5 / 4 pomocí Apple MLX Framework](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

- Hodnocení Phi  
    - [Responsible AI](./md/01.Introduction/05/ResponsibleAI.md)  
    - [Azure AI Foundry pro hodnocení](./md/01.Introduction/05/AIFoundry.md)  
    - [Použití Promptflow pro hodnocení](./md/01.Introduction/05/Promptflow.md)

- RAG s Azure AI Search  
    - [Jak používat Phi-4-mini a Phi-4-multimodal (RAG) s Azure AI Search](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Ukázky vývoje aplikací Phi  
  - Textové a chatové aplikace  
    - Phi-4 ukázky 🆕  
      - [📓] [Chat s Phi-4-mini ONNX modelem](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)  
      - [Chat s Phi-4 lokálním ONNX modelem v .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)  
      - [Chat .NET konzolová aplikace s Phi-4 ONNX pomocí Semantic Kernel](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)  
    - Phi-3 / 3.5 ukázky  
      - [Lokální chatbot v prohlížeči s Phi3, ONNX Runtime Web a WebGPU](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)  
      - [OpenVino Chat](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)  
      - [Multi Model – Interaktivní Phi-3-mini a OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)  
      - [MLFlow – Vytvoření wrapperu a použití Phi-3 s MLFlow](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)  
      - [Optimalizace modelu – Jak optimalizovat Phi-3-min model pro ONNX Runtime Web pomocí Olive](https://github.com/microsoft/Olive/tree/main/examples/phi3)  
      - [WinUI3 aplikace s Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)  
      - [WinUI3 Multi Model AI Powered Notes App ukázka](https://github.com/microsoft/ai-powered-notes-winui3-sample)
- [Doladění a integrace vlastních modelů Phi-3 s Prompt flow](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
- [Doladění a integrace vlastních modelů Phi-3 s Prompt flow v Azure AI Foundry](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
- [Hodnocení doladěného modelu Phi-3 / Phi-3.5 v Azure AI Foundry se zaměřením na zásady odpovědné AI od Microsoftu](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
- [📓] [Ukázka jazykového predikčního modelu Phi-3.5-mini-instruct (čínština/angličtina)](../../md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
- [Phi-3.5-Instruct WebGPU RAG Chatbot](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
- [Použití Windows GPU pro vytvoření řešení Prompt flow s Phi-3.5-Instruct ONNX](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
- [Použití Microsoft Phi-3.5 tflite pro vytvoření Android aplikace](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
- [Příklad Q&A v .NET s lokálním ONNX modelem Phi-3 pomocí Microsoft.ML.OnnxRuntime](../../md/04.HOL/dotnet/src/LabsPhi301)
- [Konzolová chatovací aplikace v .NET se Semantic Kernel a Phi-3](../../md/04.HOL/dotnet/src/LabsPhi302)

- Azure AI Inference SDK ukázky založené na kódu  
  - Phi-4 ukázky 🆕  
    - [📓] [Generování kódu projektu pomocí Phi-4-multimodal](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)  
  - Phi-3 / 3.5 ukázky  
    - [Vytvořte si vlastní Visual Studio Code GitHub Copilot Chat s rodinou Microsoft Phi-3](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)  
    - [Vytvořte si vlastního chatovacího agenta pro Visual Studio Code s Phi-3.5 pomocí GitHub modelů](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)  

- Ukázky pokročilého uvažování  
  - Phi-4 ukázky 🆕  
    - [📓] [Ukázky Phi-4-mini-reasoning nebo Phi-4-reasoning](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)  
    - [📓] [Doladění Phi-4-mini-reasoning s Microsoft Olive](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)  
    - [📓] [Doladění Phi-4-mini-reasoning s Apple MLX](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)  
    - [📓] [Phi-4-mini-reasoning s GitHub modely](../../md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)  
    - [📓] [Phi-4-mini-reasoning s Azure AI Foundry modely](../../md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)  
- Dema  
    - [Phi-4-mini dema hostovaná na Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)  
    - [Phi-4-multimodal dema hostovaná na Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)  
- Ukázky pro Vision  
  - Phi-4 ukázky 🆕  
    - [📓] [Použití Phi-4-multimodal pro čtení obrázků a generování kódu](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md)  
  - Phi-3 / 3.5 ukázky  
    - [📓][Phi-3-vision - převod textu z obrázku na text](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)  
    - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)  
    - [📓][Phi-3-vision CLIP embedding](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)  
    - [DEMO: Phi-3 Recycling](https://github.com/jennifermarsman/PhiRecycling/)  
    - [Phi-3-vision - vizuální jazykový asistent s Phi3-Vision a OpenVINO](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)  
    - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)  
    - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)  
    - [📓][Phi-3.5 Vision ukázka s více snímky nebo více obrázky](../../md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)  
    - [Phi-3 Vision lokální ONNX model pomocí Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi303)  
    - [Menu založený Phi-3 Vision lokální ONNX model pomocí Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi304)  

- Ukázky matematiky  
  - Phi-4-Mini-Flash-Reasoning-Instruct ukázky 🆕 [Matematické demo s Phi-4-Mini-Flash-Reasoning-Instruct](../../md/02.Application/09.Math/MathDemo.ipynb)  

- Ukázky zvuku  
  - Phi-4 ukázky 🆕  
    - [📓] [Extrahování přepisů zvuku pomocí Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Transciption/README.md)  
    - [📓] [Phi-4-multimodal ukázka zvuku](../../md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)  
    - [📓] [Phi-4-multimodal ukázka překladu řeči](../../md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)  
    - [.NET konzolová aplikace používající Phi-4-multimodal Audio pro analýzu zvukového souboru a generování přepisu](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)  

- MOE ukázky  
  - Phi-3 / 3.5 ukázky  
    - [📓] [Phi-3.5 Mixture of Experts Models (MoEs) ukázka pro sociální média](../../md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)  
    - [📓] [Vytvoření Retrieval-Augmented Generation (RAG) pipeline s NVIDIA NIM Phi-3 MOE, Azure AI Search a LlamaIndex](../../md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)  

- Ukázky volání funkcí  
  - Phi-4 ukázky 🆕  
    - [📓] [Použití volání funkcí s Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)  
    - [📓] [Použití volání funkcí pro vytvoření multi-agentů s Phi-4-mini](../../md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)  
    - [📓] [Použití volání funkcí s Ollama](../../md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)  
    - [📓] [Použití volání funkcí s ONNX](../../md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)  

- Ukázky multimodálního mixování  
  - Phi-4 ukázky 🆕  
    - [📓] [Použití Phi-4-multimodal jako technologický novinář](../../md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)  
    - [.NET konzolová aplikace používající Phi-4-multimodal pro analýzu obrázků](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)  

- Doladění Phi ukázek  
  - [Scénáře doladění](./md/03.FineTuning/FineTuning_Scenarios.md)  
  - [Doladění vs RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)  
  - [Doladění: Nechte Phi-3 stát se průmyslovým expertem](./md/03.FineTuning/LetPhi3gotoIndustriy.md)  
  - [Doladění Phi-3 s AI Toolkit pro VS Code](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)  
  - [Doladění Phi-3 s Azure Machine Learning Service](./md/03.FineTuning/Introduce_AzureML.md)  
  - [Doladění Phi-3 s Lora](./md/03.FineTuning/FineTuning_Lora.md)  
  - [Doladění Phi-3 s QLora](./md/03.FineTuning/FineTuning_Qlora.md)  
  - [Doladění Phi-3 s Azure AI Foundry](./md/03.FineTuning/FineTuning_AIFoundry.md)  
  - [Doladění Phi-3 s Azure ML CLI/SDK](./md/03.FineTuning/FineTuning_MLSDK.md)  
  - [Doladění s Microsoft Olive](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)  
  - [Doladění s Microsoft Olive Hands-On Lab](./md/03.FineTuning/olive-lab/readme.md)  
  - [Doladění Phi-3-vision s Weights and Bias](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)  
  - [Doladění Phi-3 s Apple MLX Framework](./md/03.FineTuning/FineTuning_MLX.md)  
  - [Doladění Phi-3-vision (oficiální podpora)](./md/03.FineTuning/FineTuning_Vision.md)  
  - [Doladění Phi-3 s Kaito AKS, Azure Containers (oficiální podpora)](./md/03.FineTuning/FineTuning_Kaito.md)  
  - [Doladění Phi-3 a 3.5 Vision](https://github.com/2U1/Phi3-Vision-Finetune)  

- Hands on Lab  
  - [Objevování nejmodernějších modelů: LLMs, SLMs, lokální vývoj a další](https://github.com/microsoft/aitour-exploring-cutting-edge-models)  
  - [Odemknutí potenciálu NLP: Doladění s Microsoft Olive](https://github.com/azure/Ignite_FineTuning_workshop)  

- Akademické výzkumné práce a publikace  
  - [Textbooks Are All You Need II: technická zpráva phi-1.5](https://arxiv.org/abs/2309.05463)  
  - [Phi-3 technická zpráva: Vysoce schopný jazykový model lokálně na vašem telefonu](https://arxiv.org/abs/2404.14219)  
  - [Phi-4 technická zpráva](https://arxiv.org/abs/2412.08905)  
  - [Phi-4-Mini technická zpráva: Kompaktní, ale výkonné multimodální jazykové modely pomocí Mixture-of-LoRAs](https://arxiv.org/abs/2503.01743)  
  - [Optimalizace malých jazykových modelů pro volání funkcí ve vozidle](https://arxiv.org/abs/2501.02342)  
  - [(WhyPHI) Doladění PHI-3 pro odpovídání na otázky s výběrem z více možností: metodologie, výsledky a výzvy](https://arxiv.org/abs/2501.01588)
  - [Phi-4-reasoning Technická zpráva](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Phi-4-mini-reasoning Technická zpráva](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Používání modelů Phi

### Phi na Azure AI Foundry

Můžete se naučit, jak používat Microsoft Phi a jak vytvářet end-to-end řešení na různých hardwarových zařízeních. Abyste si Phi vyzkoušeli sami, začněte hraním s modely a přizpůsobením Phi pro vaše scénáře pomocí [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai). Více se dozvíte v průvodci Začínáme s [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md).

**Playground**  
Každý model má vlastní playground pro testování modelu [Azure AI Playground](https://aka.ms/try-phi3).

### Phi na GitHub modelech

Můžete se naučit, jak používat Microsoft Phi a jak vytvářet end-to-end řešení na různých hardwarových zařízeních. Abyste si Phi vyzkoušeli sami, začněte hraním s modelem a přizpůsobením Phi pro vaše scénáře pomocí [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo). Více se dozvíte v průvodci Začínáme s [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md).

**Playground**  
Každý model má vlastní [playground pro testování modelu](/md/02.QuickStart/GitHubModel_QuickStart.md).

### Phi na Hugging Face

Model najdete také na [Hugging Face](https://huggingface.co/microsoft).

**Playground**  
[Hugging Chat playground](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## Odpovědné AI

Microsoft se zavazuje pomáhat svým zákazníkům používat naše AI produkty zodpovědně, sdílet naše poznatky a budovat důvěru prostřednictvím nástrojů jako Transparency Notes a Impact Assessments. Mnoho z těchto zdrojů najdete na [https://aka.ms/RAI](https://aka.ms/RAI).  
Přístup Microsoftu k odpovědné AI je založen na našich principech AI: spravedlnost, spolehlivost a bezpečnost, ochrana soukromí a bezpečnost, inkluzivita, transparentnost a odpovědnost.

Velké modely pro zpracování přirozeného jazyka, obrazu a řeči – jako ty použité v tomto příkladu – se mohou chovat způsobem, který je nespravedlivý, nespolehlivý nebo urážlivý, což může způsobit škody. Pro informace o rizicích a omezeních si prosím přečtěte [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text).

Doporučený přístup k minimalizaci těchto rizik je začlenit do vaší architektury bezpečnostní systém, který dokáže detekovat a zabránit škodlivému chování. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) poskytuje nezávislou ochrannou vrstvu, která dokáže detekovat škodlivý obsah vytvářený uživateli i AI v aplikacích a službách. Azure AI Content Safety zahrnuje textové a obrazové API, která umožňují detekovat škodlivý materiál. V rámci Azure AI Foundry služba Content Safety umožňuje prohlížet, zkoumat a vyzkoušet ukázkový kód pro detekci škodlivého obsahu napříč různými modalitami. Následující [quickstart dokumentace](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) vás provede, jak posílat požadavky na tuto službu.

Dalším aspektem, který je třeba zvážit, je celkový výkon aplikace. U multimodálních a multimodelových aplikací chápeme výkon tak, že systém funguje podle očekávání vás i vašich uživatelů, včetně toho, že nevytváří škodlivé výstupy. Je důležité hodnotit výkon vaší aplikace pomocí [Performance and Quality a Risk and Safety evaluators](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in). Máte také možnost vytvářet a hodnotit pomocí [vlastních evaluátorů](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators).

Své AI aplikace můžete hodnotit ve vývojovém prostředí pomocí [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html). Na základě testovacího datasetu nebo cíle jsou generace vaší generativní AI aplikace kvantitativně měřeny vestavěnými nebo vlastními evaluátory dle vašeho výběru. Pro začátek s Azure AI Evaluation SDK a hodnocení vašeho systému můžete sledovat [quickstart průvodce](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Po spuštění hodnocení můžete [vizualizovat výsledky v Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Ochranné známky

Tento projekt může obsahovat ochranné známky nebo loga projektů, produktů či služeb. Autorizované používání ochranných známek nebo log Microsoftu podléhá a musí dodržovat [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).  
Používání ochranných známek nebo log Microsoftu v upravených verzích tohoto projektu nesmí způsobovat záměnu ani naznačovat sponzorství Microsoftem. Jakékoli použití ochranných známek nebo log třetích stran podléhá pravidlům těchto třetích stran.

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za závazný zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.