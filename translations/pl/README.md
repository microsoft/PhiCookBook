<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4987daf30687ad3850757c9eae3f5411",
  "translation_date": "2025-10-17T10:20:52+00:00",
  "source_file": "README.md",
  "language_code": "pl"
}
-->
# Phi Cookbook: Praktyczne przykłady z modelami Phi od Microsoftu

[![Otwórz i użyj przykładów w GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Otwórz w Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![Współtwórcy GitHub](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![Problemy GitHub](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![Pull requesty GitHub](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![Obserwujący GitHub](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![Forki GitHub](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![Gwiazdy GitHub](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi to seria otwartych modeli AI opracowanych przez Microsoft.

Phi jest obecnie najpotężniejszym i najbardziej opłacalnym małym modelem językowym (SLM), osiągającym bardzo dobre wyniki w wielojęzyczności, rozumowaniu, generowaniu tekstu/czatu, kodowaniu, obrazach, dźwięku i innych scenariuszach.

Możesz wdrożyć Phi w chmurze lub na urządzeniach brzegowych, a także łatwo budować aplikacje generatywne AI przy ograniczonej mocy obliczeniowej.

Postępuj zgodnie z poniższymi krokami, aby rozpocząć korzystanie z tych zasobów:
1. **Zforkuj repozytorium**: Kliknij [![Forki GitHub](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **Sklonuj repozytorium**:   `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Dołącz do społeczności Microsoft AI Discord i poznaj ekspertów oraz innych programistów**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../imgs/cover.png)

### 🌐 Obsługa wielu języków

#### Obsługiwane przez GitHub Action (Automatyczne i zawsze aktualne)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabski](../ar/README.md) | [Bengalski](../bn/README.md) | [Bułgarski](../bg/README.md) | [Birmański (Myanmar)](../my/README.md) | [Chiński (uproszczony)](../zh/README.md) | [Chiński (tradycyjny, Hongkong)](../hk/README.md) | [Chiński (tradycyjny, Makau)](../mo/README.md) | [Chiński (tradycyjny, Tajwan)](../tw/README.md) | [Chorwacki](../hr/README.md) | [Czeski](../cs/README.md) | [Duński](../da/README.md) | [Holenderski](../nl/README.md) | [Estoński](../et/README.md) | [Fiński](../fi/README.md) | [Francuski](../fr/README.md) | [Niemiecki](../de/README.md) | [Grecki](../el/README.md) | [Hebrajski](../he/README.md) | [Hindi](../hi/README.md) | [Węgierski](../hu/README.md) | [Indonezyjski](../id/README.md) | [Włoski](../it/README.md) | [Japoński](../ja/README.md) | [Koreański](../ko/README.md) | [Litewski](../lt/README.md) | [Malajski](../ms/README.md) | [Marathi](../mr/README.md) | [Nepalski](../ne/README.md) | [Norweski](../no/README.md) | [Perski (Farsi)](../fa/README.md) | [Polski](./README.md) | [Portugalski (Brazylia)](../br/README.md) | [Portugalski (Portugalia)](../pt/README.md) | [Pendżabski (Gurmukhi)](../pa/README.md) | [Rumuński](../ro/README.md) | [Rosyjski](../ru/README.md) | [Serbski (cyrylica)](../sr/README.md) | [Słowacki](../sk/README.md) | [Słoweński](../sl/README.md) | [Hiszpański](../es/README.md) | [Suahili](../sw/README.md) | [Szwedzki](../sv/README.md) | [Tagalog (Filipiński)](../tl/README.md) | [Tamilski](../ta/README.md) | [Tajski](../th/README.md) | [Turecki](../tr/README.md) | [Ukraiński](../uk/README.md) | [Urdu](../ur/README.md) | [Wietnamski](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## Spis treści

- Wprowadzenie
  - [Witamy w rodzinie Phi](./md/01.Introduction/01/01.PhiFamily.md)
  - [Konfigurowanie środowiska](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [Zrozumienie kluczowych technologii](./md/01.Introduction/01/01.Understandingtech.md)
  - [Bezpieczeństwo AI dla modeli Phi](./md/01.Introduction/01/01.AISafety.md)
  - [Obsługa sprzętu dla Phi](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Modele Phi i dostępność na różnych platformach](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Korzystanie z Guidance-ai i Phi](./md/01.Introduction/01/01.Guidance.md)
  - [Modele w GitHub Marketplace](https://github.com/marketplace/models)
  - [Katalog modeli Azure AI](https://ai.azure.com)

- Wnioskowanie Phi w różnych środowiskach
    -  [Hugging face](./md/01.Introduction/02/01.HF.md)
    -  [Modele GitHub](./md/01.Introduction/02/02.GitHubModel.md)
    -  [Katalog modeli Azure AI Foundry](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    -  [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md)

- Wnioskowanie rodziny Phi
    - [Wnioskowanie Phi na iOS](./md/01.Introduction/03/iOS_Inference.md)
    - [Wnioskowanie Phi na Androidzie](./md/01.Introduction/03/Android_Inference.md)
    - [Wnioskowanie Phi na Jetson](./md/01.Introduction/03/Jetson_Inference.md)
    - [Wnioskowanie Phi na komputerze AI PC](./md/01.Introduction/03/AIPC_Inference.md)
    - [Wnioskowanie Phi z Apple MLX Framework](./md/01.Introduction/03/MLX_Inference.md)
    - [Wnioskowanie Phi na lokalnym serwerze](./md/01.Introduction/03/Local_Server_Inference.md)
    - [Wnioskowanie Phi na zdalnym serwerze za pomocą AI Toolkit](./md/01.Introduction/03/Remote_Interence.md)
    - [Wnioskowanie Phi z Rust](./md/01.Introduction/03/Rust_Inference.md)
    - [Wnioskowanie Phi--Vision lokalnie](./md/01.Introduction/03/Vision_Inference.md)
    - [Wnioskowanie Phi z Kaito AKS, kontenerami Azure (oficjalne wsparcie)](./md/01.Introduction/03/Kaito_Inference.md)
-  [Kwantyfikacja rodziny Phi](./md/01.Introduction/04/QuantifyingPhi.md)
    - [Kwantyzacja Phi-3.5 / 4 za pomocą llama.cpp](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [Kwantyzacja Phi-3.5 / 4 za pomocą rozszerzeń generatywnych AI dla onnxruntime](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Kwantyzacja Phi-3.5 / 4 za pomocą Intel OpenVINO](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Kwantyzacja Phi-3.5 / 4 za pomocą Apple MLX Framework](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

-  Ewaluacja Phi
    - [Odpowiedzialne AI](./md/01.Introduction/05/ResponsibleAI.md)
    - [Azure AI Foundry dla ewaluacji](./md/01.Introduction/05/AIFoundry.md)
    - [Korzystanie z Promptflow do ewaluacji](./md/01.Introduction/05/Promptflow.md)
 
- RAG z Azure AI Search
    - [Jak używać Phi-4-mini i Phi-4-multimodal (RAG) z Azure AI Search](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Przykłady rozwoju aplikacji Phi
  - Aplikacje tekstowe i czatowe
    - Przykłady Phi-4 🆕
      - [📓] [Czat z modelem Phi-4-mini ONNX](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Czat z lokalnym modelem Phi-4 ONNX .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Konsolowa aplikacja .NET z modelem Phi-4 ONNX używając Semantic Kernel](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Przykłady Phi-3 / 3.5
      - [Lokalny chatbot w przeglądarce używający Phi3, ONNX Runtime Web i WebGPU](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [Czat OpenVino](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [Multi Model - Interaktywny Phi-3-mini i OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - Tworzenie wrappera i używanie Phi-3 z MLFlow](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [Optymalizacja modelu - Jak zoptymalizować model Phi-3-min dla ONNX Runtime Web za pomocą Olive](https://github.com/microsoft/Olive/tree/main/examples/phi3)
- [WinUI3 Aplikacja z Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
- [WinUI3 Przykładowa aplikacja notatek z AI opartą na wielu modelach](https://github.com/microsoft/ai-powered-notes-winui3-sample)
- [Dostosowanie i integracja niestandardowych modeli Phi-3 z Prompt flow](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
- [Dostosowanie i integracja niestandardowych modeli Phi-3 z Prompt flow w Azure AI Foundry](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
- [Ocena dostosowanego modelu Phi-3 / Phi-3.5 w Azure AI Foundry z uwzględnieniem zasad odpowiedzialnej AI Microsoftu](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
- [📓] [Przykład przewidywania języka Phi-3.5-mini-instruct (chiński/angielski)](../../md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
- [Phi-3.5-Instruct WebGPU RAG Chatbot](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
- [Użycie GPU Windows do stworzenia rozwiązania Prompt flow z Phi-3.5-Instruct ONNX](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
- [Użycie Microsoft Phi-3.5 tflite do stworzenia aplikacji na Androida](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
- [Przykład Q&A .NET z lokalnym modelem ONNX Phi-3 używającym Microsoft.ML.OnnxRuntime](../../md/04.HOL/dotnet/src/LabsPhi301)
- [Aplikacja konsolowa .NET do czatu z Semantic Kernel i Phi-3](../../md/04.HOL/dotnet/src/LabsPhi302)

- Przykłady kodu SDK Azure AI Inference 
  - Przykłady Phi-4 🆕
    - [📓] [Generowanie kodu projektu za pomocą Phi-4-multimodal](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
  - Przykłady Phi-3 / 3.5
    - [Stwórz własny czat GitHub Copilot w Visual Studio Code z rodziną Phi-3 Microsoftu](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
    - [Stwórz własnego agenta czatu Copilot w Visual Studio Code z Phi-3.5 za pomocą modeli GitHub](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

- Zaawansowane przykłady rozumowania
  - Przykłady Phi-4 🆕
    - [📓] [Przykłady Phi-4-mini-reasoning lub Phi-4-reasoning](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
    - [📓] [Dostosowanie Phi-4-mini-reasoning za pomocą Microsoft Olive](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
    - [📓] [Dostosowanie Phi-4-mini-reasoning za pomocą Apple MLX](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
    - [📓] [Phi-4-mini-reasoning z modelami GitHub](../../md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
    - [📓] [Phi-4-mini-reasoning z modelami Azure AI Foundry](../../md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
- Dema
    - [Dema Phi-4-mini hostowane na Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
    - [Dema Phi-4-multimodal hostowane na Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
- Przykłady wizji
  - Przykłady Phi-4 🆕
    - [📓] [Użycie Phi-4-multimodal do odczytu obrazów i generowania kodu](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
  - Przykłady Phi-3 / 3.5
    - [📓][Phi-3-vision-Obraz tekst na tekst](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
    - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
    - [📓][Phi-3-vision CLIP Embedding](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
    - [DEMO: Phi-3 Recycling](https://github.com/jennifermarsman/PhiRecycling/)
    - [Phi-3-vision - Asystent językowy wizualny - z Phi3-Vision i OpenVINO](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
    - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
    - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
    - [📓][Phi-3.5 Vision przykład wieloklatkowy lub wieloobrazowy](../../md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
    - [Phi-3 Vision Lokalny model ONNX używający Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi303)
    - [Menu oparte na Phi-3 Vision Lokalny model ONNX używający Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi304)

- Przykłady matematyczne
  - Phi-4-Mini-Flash-Reasoning-Instruct Przykłady 🆕 [Demo matematyczne z Phi-4-Mini-Flash-Reasoning-Instruct](../../md/02.Application/09.Math/MathDemo.ipynb)

- Przykłady audio
  - Przykłady Phi-4 🆕
    - [📓] [Ekstrakcja transkrypcji audio za pomocą Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
    - [📓] [Phi-4-multimodal Przykład audio](../../md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
    - [📓] [Phi-4-multimodal Przykład tłumaczenia mowy](../../md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
    - [Aplikacja konsolowa .NET używająca Phi-4-multimodal Audio do analizy pliku audio i generowania transkrypcji](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

- Przykłady MOE
  - Przykłady Phi-3 / 3.5
    - [📓] [Phi-3.5 Mixture of Experts Models (MoEs) Przykład mediów społecznościowych](../../md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
    - [📓] [Budowanie Retrieval-Augmented Generation (RAG) Pipeline z NVIDIA NIM Phi-3 MOE, Azure AI Search i LlamaIndex](../../md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)

- Przykłady wywoływania funkcji
  - Przykłady Phi-4 🆕
    - [📓] [Użycie wywoływania funkcji z Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
    - [📓] [Użycie wywoływania funkcji do tworzenia multi-agentów z Phi-4-mini](../../md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
    - [📓] [Użycie wywoływania funkcji z Ollama](../../md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
    - [📓] [Użycie wywoływania funkcji z ONNX](../../md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)

- Przykłady mieszania multimodalnego
  - Przykłady Phi-4 🆕
    - [📓] [Użycie Phi-4-multimodal jako dziennikarz technologiczny](../../md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
    - [Aplikacja konsolowa .NET używająca Phi-4-multimodal do analizy obrazów](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Przykłady dostosowywania Phi
  - [Scenariusze dostosowywania](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [Dostosowywanie vs RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [Dostosowywanie Phi-3 jako ekspert branżowy](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [Dostosowywanie Phi-3 za pomocą AI Toolkit dla VS Code](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Dostosowywanie Phi-3 za pomocą Azure Machine Learning Service](./md/03.FineTuning/Introduce_AzureML.md)
  - [Dostosowywanie Phi-3 za pomocą Lora](./md/03.FineTuning/FineTuning_Lora.md)
  - [Dostosowywanie Phi-3 za pomocą QLora](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Dostosowywanie Phi-3 za pomocą Azure AI Foundry](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Dostosowywanie Phi-3 za pomocą Azure ML CLI/SDK](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Dostosowywanie za pomocą Microsoft Olive](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Dostosowywanie za pomocą Microsoft Olive Hands-On Lab](./md/03.FineTuning/olive-lab/readme.md)
  - [Dostosowywanie Phi-3-vision za pomocą Weights and Bias](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [Dostosowywanie Phi-3 za pomocą Apple MLX Framework](./md/03.FineTuning/FineTuning_MLX.md)
  - [Dostosowywanie Phi-3-vision (oficjalne wsparcie)](./md/03.FineTuning/FineTuning_Vision.md)
  - [Dostosowywanie Phi-3 z Kaito AKS, Azure Containers (oficjalne wsparcie)](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Dostosowywanie Phi-3 i 3.5 Vision](https://github.com/2U1/Phi3-Vision-Finetune)

- Laboratoria praktyczne
  - [Eksploracja najnowszych modeli: LLM, SLM, lokalny rozwój i więcej](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [Odkrywanie potencjału NLP: Dostosowywanie z Microsoft Olive](https://github.com/azure/Ignite_FineTuning_workshop)

- Akademickie prace badawcze i publikacje
  - [Textbooks Are All You Need II: phi-1.5 raport techniczny](https://arxiv.org/abs/2309.05463)
  - [Phi-3 Raport techniczny: Wysoce zdolny model językowy lokalnie na Twoim telefonie](https://arxiv.org/abs/2404.14219)
  - [Phi-4 Raport techniczny](https://arxiv.org/abs/2412.08905)
  - [Phi-4-Mini Raport techniczny: Kompaktowe, ale potężne modele językowe multimodalne za pomocą Mixture-of-LoRAs](https://arxiv.org/abs/2503.01743)
  - [Optymalizacja małych modeli językowych do wywoływania funkcji w pojazdach](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) Dostosowywanie PHI-3 do odpowiedzi na pytania wielokrotnego wyboru: metodologia, wyniki i wyzwania](https://arxiv.org/abs/2501.01588)
  - [Raport techniczny Phi-4-reasoning](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Raport techniczny Phi-4-mini-reasoning](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Korzystanie z modeli Phi

### Phi na Azure AI Foundry

Możesz dowiedzieć się, jak korzystać z Microsoft Phi i budować rozwiązania E2E na różnych urządzeniach sprzętowych. Aby samodzielnie wypróbować Phi, zacznij od testowania modeli i dostosowywania Phi do swoich scenariuszy, korzystając z [Katalogu Modeli Azure AI Foundry](https://aka.ms/phi3-azure-ai). Więcej informacji znajdziesz w sekcji Rozpoczęcie pracy z [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md).

**Playground**  
Każdy model ma dedykowany playground do testowania modelu [Azure AI Playground](https://aka.ms/try-phi3).

### Phi na GitHub Models

Możesz dowiedzieć się, jak korzystać z Microsoft Phi i budować rozwiązania E2E na różnych urządzeniach sprzętowych. Aby samodzielnie wypróbować Phi, zacznij od testowania modelu i dostosowywania Phi do swoich scenariuszy, korzystając z [Katalogu Modeli GitHub](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo). Więcej informacji znajdziesz w sekcji Rozpoczęcie pracy z [Katalogiem Modeli GitHub](/md/02.QuickStart/GitHubModel_QuickStart.md).

**Playground**  
Każdy model ma dedykowany [playground do testowania modelu](/md/02.QuickStart/GitHubModel_QuickStart.md).

### Phi na Hugging Face

Model można również znaleźć na [Hugging Face](https://huggingface.co/microsoft).

**Playground**  
[Playground Hugging Chat](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct).

## Odpowiedzialna AI

Microsoft zobowiązuje się do wspierania klientów w odpowiedzialnym korzystaniu z naszych produktów AI, dzielenia się doświadczeniami oraz budowania partnerskich relacji opartych na zaufaniu poprzez narzędzia takie jak Transparency Notes i Impact Assessments. Wiele z tych zasobów można znaleźć na stronie [https://aka.ms/RAI](https://aka.ms/RAI).  
Podejście Microsoft do odpowiedzialnej AI opiera się na naszych zasadach AI: sprawiedliwości, niezawodności i bezpieczeństwa, prywatności i ochrony, inkluzywności, przejrzystości oraz odpowiedzialności.

Modele językowe, obrazowe i mowy na dużą skalę - takie jak te używane w tym przykładzie - mogą potencjalnie działać w sposób niesprawiedliwy, zawodny lub obraźliwy, co może prowadzić do szkód. Prosimy o zapoznanie się z [notą przejrzystości usługi Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text), aby być świadomym ryzyk i ograniczeń.

Zalecanym podejściem do ograniczenia tych ryzyk jest uwzględnienie systemu bezpieczeństwa w architekturze, który może wykrywać i zapobiegać szkodliwym zachowaniom. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) zapewnia niezależną warstwę ochrony, zdolną do wykrywania szkodliwych treści generowanych przez użytkowników i AI w aplikacjach i usługach. Azure AI Content Safety obejmuje API tekstowe i obrazowe, które pozwalają na wykrywanie materiałów szkodliwych. W ramach Azure AI Foundry, usługa Content Safety umożliwia przeglądanie, eksplorowanie i testowanie przykładowego kodu do wykrywania szkodliwych treści w różnych modalnościach. Następująca [dokumentacja szybkiego startu](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) prowadzi przez proces składania zapytań do usługi.

Innym aspektem, który należy wziąć pod uwagę, jest ogólna wydajność aplikacji. W przypadku aplikacji multimodalnych i wielomodelowych, wydajność oznacza, że system działa zgodnie z oczekiwaniami użytkowników, w tym nie generuje szkodliwych wyników. Ważne jest, aby ocenić wydajność całej aplikacji, korzystając z [ocen wydajności, jakości oraz ryzyka i bezpieczeństwa](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in). Możesz również tworzyć i oceniać [własne oceny](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators).

Możesz ocenić swoją aplikację AI w środowisku deweloperskim, korzystając z [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html). Na podstawie zestawu testowego lub celu, generacje aplikacji AI są ilościowo mierzone za pomocą wbudowanych lub własnych ocen, które wybierzesz. Aby rozpocząć korzystanie z Azure AI Evaluation SDK do oceny systemu, możesz skorzystać z [przewodnika szybkiego startu](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Po wykonaniu oceny możesz [wizualizować wyniki w Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Znaki towarowe

Ten projekt może zawierać znaki towarowe lub logotypy projektów, produktów lub usług. Autoryzowane użycie znaków towarowych lub logotypów Microsoft podlega i musi być zgodne z [Wytycznymi dotyczącymi znaków towarowych i marki Microsoft](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).  
Użycie znaków towarowych lub logotypów Microsoft w zmodyfikowanych wersjach tego projektu nie może powodować zamieszania ani sugerować sponsorowania przez Microsoft. Wszelkie użycie znaków towarowych lub logotypów stron trzecich podlega politykom tych stron trzecich.

## Uzyskiwanie pomocy

Jeśli napotkasz trudności lub masz pytania dotyczące budowy aplikacji AI, dołącz do:

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

Jeśli masz uwagi dotyczące produktu lub napotkasz błędy podczas budowy, odwiedź:

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za autorytatywne źródło. W przypadku informacji krytycznych zaleca się profesjonalne tłumaczenie przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.