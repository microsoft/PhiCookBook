# Phi Cookbook: Przykłady praktyczne z modelami Phi firmy Microsoft

[![Otwórz i używaj przykładów w GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Otwórz w Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![Współtwórcy GitHub](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![Problemy GitHub](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![Prośby o wprowadzenie zmian GitHub](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![Obserwujący GitHub](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![Forki GitHub](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![Gwiazdki GitHub](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi to seria otwartoźródłowych modeli AI opracowanych przez Microsoft.

Phi jest obecnie najmocniejszym i najbardziej opłacalnym małym modelem językowym (SLM), osiągając bardzo dobre wyniki w wielu językach, wnioskowaniu, generowaniu tekstu/czatu, kodowaniu, obrazach, dźwięku i innych scenariuszach.

Możesz wdrożyć Phi w chmurze lub na urządzeniach brzegowych oraz łatwo tworzyć aplikacje generatywnej sztucznej inteligencji z ograniczoną mocą obliczeniową.

Wykonaj te kroki, aby rozpocząć korzystanie z tych zasobów:
1. **Rozgałęź repozytorium**: Kliknij [![Forki GitHub](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **Sklonuj repozytorium**: `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Dołącz do społeczności Microsoft AI Discord i poznaj ekspertów oraz innych deweloperów**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/pl/cover.eb18d1b9605d754b.webp)

### 🌐 Wsparcie wielojęzyczne

#### Wspierane przez GitHub Action (Automatyczne i zawsze aktualne)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabski](../ar/README.md) | [Bengalski](../bn/README.md) | [Bułgarski](../bg/README.md) | [Birmański (Myanmar)](../my/README.md) | [Chiński (uproszczony)](../zh-CN/README.md) | [Chiński (tradycyjny, Hongkong)](../zh-HK/README.md) | [Chiński (tradycyjny, Makau)](../zh-MO/README.md) | [Chiński (tradycyjny, Tajwan)](../zh-TW/README.md) | [Chorwacki](../hr/README.md) | [Czeski](../cs/README.md) | [Duński](../da/README.md) | [Holenderski](../nl/README.md) | [Estoński](../et/README.md) | [Fiński](../fi/README.md) | [Francuski](../fr/README.md) | [Niemiecki](../de/README.md) | [Grecki](../el/README.md) | [Hebrajski](../he/README.md) | [Hindi](../hi/README.md) | [Węgierski](../hu/README.md) | [Indonezyjski](../id/README.md) | [Włoski](../it/README.md) | [Japoński](../ja/README.md) | [Kannada](../kn/README.md) | [Koreański](../ko/README.md) | [Litewski](../lt/README.md) | [Malajski](../ms/README.md) | [Malajalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepalski](../ne/README.md) | [Pidgin nigeryjski](../pcm/README.md) | [Norweski](../no/README.md) | [Perski (Farsi)](../fa/README.md) | [Polski](./README.md) | [Portugalski (Brazylia)](../pt-BR/README.md) | [Portugalski (Portugalia)](../pt-PT/README.md) | [Pendżabski (Gurmukhi)](../pa/README.md) | [Rumuński](../ro/README.md) | [Rosyjski](../ru/README.md) | [Serbski (cyrylica)](../sr/README.md) | [Słowacki](../sk/README.md) | [Słoweński](../sl/README.md) | [Hiszpański](../es/README.md) | [Suahili](../sw/README.md) | [Szwedzki](../sv/README.md) | [Tagalog (filipiński)](../tl/README.md) | [Tamilski](../ta/README.md) | [Telugu](../te/README.md) | [Tajski](../th/README.md) | [Turecki](../tr/README.md) | [Ukraiński](../uk/README.md) | [Urdu](../ur/README.md) | [Wietnamski](../vi/README.md)

> **Wolisz sklonować lokalnie?**

> To repozytorium zawiera ponad 50 tłumaczeń językowych, co znacznie zwiększa rozmiar pobierania. Aby sklonować bez tłumaczeń, użyj sparse checkout:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/PhiCookBook.git
> cd PhiCookBook
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> Zapewnia to wszystkie potrzebne pliki do ukończenia kursu z dużo szybszym pobieraniem.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## Spis treści

- Wprowadzenie
  - [Witamy w rodzinie Phi](./md/01.Introduction/01/01.PhiFamily.md)
  - [Konfiguracja środowiska](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [Zrozumienie kluczowych technologii](./md/01.Introduction/01/01.Understandingtech.md)
  - [Bezpieczeństwo AI dla modeli Phi](./md/01.Introduction/01/01.AISafety.md)
  - [Wsparcie sprzętowe Phi](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Modele Phi & dostępność na platformach](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Używanie Guidance-ai i Phi](./md/01.Introduction/01/01.Guidance.md)
  - [Modele GitHub Marketplace](https://github.com/marketplace/models)
  - [Katalog modeli Azure AI](https://ai.azure.com)

- Wnioskowanie Phi w różnych środowiskach
    -  [Hugging Face](./md/01.Introduction/02/01.HF.md)
    -  [Modele GitHub](./md/01.Introduction/02/02.GitHubModel.md)
    -  [Katalog modeli Azure AI Foundry](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    -  [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md)

- Wnioskowanie Phi Family
    - [Wnioskowanie Phi na iOS](./md/01.Introduction/03/iOS_Inference.md)
    - [Wnioskowanie Phi na Androidzie](./md/01.Introduction/03/Android_Inference.md)
    - [Wnioskowanie Phi na Jetson](./md/01.Introduction/03/Jetson_Inference.md)
    - [Wnioskowanie Phi na AI PC](./md/01.Introduction/03/AIPC_Inference.md)
    - [Wnioskowanie Phi z Apple MLX Framework](./md/01.Introduction/03/MLX_Inference.md)
    - [Wnioskowanie Phi na lokalnym serwerze](./md/01.Introduction/03/Local_Server_Inference.md)
    - [Wnioskowanie Phi na zdalnym serwerze z użyciem AI Toolkit](./md/01.Introduction/03/Remote_Interence.md)
    - [Wnioskowanie Phi z Rust](./md/01.Introduction/03/Rust_Inference.md)
    - [Wnioskowanie Phi – wizja lokalna](./md/01.Introduction/03/Vision_Inference.md)
    - [Wnioskowanie Phi z Kaito AKS, Azure Containers (wsparcie oficjalne)](./md/01.Introduction/03/Kaito_Inference.md)
-  [Kwantityfikowanie Phi Family](./md/01.Introduction/04/QuantifyingPhi.md)
    - [Kwantityfikowanie Phi-3.5 / 4 przy użyciu llama.cpp](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [Kwantityfikowanie Phi-3.5 / 4 przy użyciu rozszerzeń Generative AI dla onnxruntime](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Kwantityfikowanie Phi-3.5 / 4 przy użyciu Intel OpenVINO](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Kwantityfikowanie Phi-3.5 / 4 przy użyciu Apple MLX Framework](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

-  Ocena Phi
    - [Społeczna odpowiedzialność AI](./md/01.Introduction/05/ResponsibleAI.md)
    - [Azure AI Foundry do oceny](./md/01.Introduction/05/AIFoundry.md)
    - [Używanie Promptflow do oceny](./md/01.Introduction/05/Promptflow.md)

- RAG z Azure AI Search
    - [Jak używać Phi-4-mini i Phi-4-multimodal (RAG) z Azure AI Search](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Przykłady rozwoju aplikacji Phi
  - Aplikacje tekstowe i czatowe
    - Phi-4 Przykłady 🆕
      - [📓] [Czat z modelem Phi-4-mini ONNX](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Czat z lokalnym modelem Phi-4 ONNX w .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Czat w aplikacji konsolowej .NET z modelem Phi-4 ONNX używającym Semantic Kernel](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Phi-3 / 3.5 Przykłady
      - [Lokalny chatbot w przeglądarce używając Phi3, ONNX Runtime Web i WebGPU](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [Czat OpenVino](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [Multi Model - Interaktywny Phi-3-mini i OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - Tworzenie wrappera i używanie Phi-3 z MLFlow](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [Optymalizacja modelu - Jak zoptymalizować model Phi-3-min dla ONNX Runtime Web z Olive](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [Aplikacja WinUI3 z Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      -[Przykład aplikacji WinUI3 Multi Model AI Powered Notes](https://github.com/microsoft/ai-powered-notes-winui3-sample)
      - [Dostrajanie i integracja niestandardowych modeli Phi-3 z Prompt flow](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
      - [Dostrajanie i integracja niestandardowych modeli Phi-3 z Prompt flow w Azure AI Foundry](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
      - [Ocena dostrojonego modelu Phi-3 / Phi-3.5 w Azure AI Foundry z uwzględnieniem zasad odpowiedzialnej AI Microsoft](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
      - [📓] [Przykład predykcji językowej Phi-3.5-mini-instruct (chiński/angielski)](./md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
      - [Phi-3.5-Instruct WebGPU RAG Chatbot](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
      - [Użycie Windows GPU do tworzenia rozwiązania Prompt flow z Phi-3.5-Instruct ONNX](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
      - [Użycie Microsoft Phi-3.5 tflite do tworzenia aplikacji Android](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
      - [Przykład Q&A .NET używając lokalnego modelu ONNX Phi-3 za pomocą Microsoft.ML.OnnxRuntime](../../md/04.HOL/dotnet/src/LabsPhi301)
      - [Aplikacja konsolowa chat .NET z Semantic Kernel i Phi-3](../../md/04.HOL/dotnet/src/LabsPhi302)

  - Przykłady kodu Azure AI Inference SDK 
    - Przykłady Phi-4 🆕
      - [📓] [Generowanie kodu projektu za pomocą Phi-4-multimodal](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
    - Przykłady Phi-3 / 3.5
      - [Zbuduj własny chat GitHub Copilot w Visual Studio Code z rodziną Microsoft Phi-3](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
      - [Stwórz własnego agenta Chat Copilot Visual Studio Code z Phi-3.5 korzystając z modeli GitHub](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

  - Przykłady zaawansowanego rozumowania
    - Przykłady Phi-4 🆕
      - [📓] [Przykłady Phi-4-mini-reasoning lub Phi-4-reasoning](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
      - [📓] [Dostrajanie Phi-4-mini-reasoning z Microsoft Olive](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Dostrajanie Phi-4-mini-reasoning z Apple MLX](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Phi-4-mini-reasoning z modelami GitHub](./md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
      - [📓] [Phi-4-mini-reasoning z modelami Azure AI Foundry](./md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
  - Demo
      - [Demo Phi-4-mini hostowane na Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
      - [Demo Phi-4-multimodal hostowane na Hugginge Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
  - Przykłady wizji
    - Przykłady Phi-4 🆕
      - [📓] [Użyj Phi-4-multimodal do czytania obrazów i generowania kodu](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
    - Przykłady Phi-3 / 3.5
      -  [📓][Phi-3-vision-tekst obrazu do tekstu](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
      - [📓][Phi-3-vision CLIP Embedding](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [DEMO: Phi-3 Recycling](https://github.com/jennifermarsman/PhiRecycling/)
      - [Phi-3-vision - Asystent języka wizualnego - z Phi3-Vision i OpenVINO](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
      - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
      - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
      - [📓][Phi-3.5 Vision przykładowe wieloklatkowe lub wieloobrazowe](./md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
      - [Phi-3 Vision lokalny model ONNX używając Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi303)
      - [Menu bazujące lokalny model ONNX Phi-3 Vision używając Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi304)

  - Przykłady matematyczne
    -  Przykłady Phi-4-Mini-Flash-Reasoning-Instruct 🆕 [Demo matematyczne z Phi-4-Mini-Flash-Reasoning-Instruct](./md/02.Application/09.Math/MathDemo.ipynb)

  - Przykłady audio
    - Przykłady Phi-4 🆕
      - [📓] [Wydobywanie transkrypcji audio za pomocą Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
      - [📓] [Przykład audio Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
      - [📓] [Przykład tłumaczenia mowy Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
      - [Aplikacja konsolowa .NET używająca Phi-4-multimodal do analizy pliku audio i generowania transkrypcji](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

  - Przykłady MOE
    - Przykłady Phi-3 / 3.5
      - [📓] [Modele mieszanki ekspertów Phi-3.5 (MoEs) przykład mediów społecznościowych](./md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
      - [📓] [Budowanie pipeline Retrieval-Augmented Generation (RAG) z NVIDIA NIM Phi-3 MOE, Azure AI Search i LlamaIndex](./md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)
      - 
  - Przykłady wywoływania funkcji
    - Przykłady Phi-4 🆕
      -  [📓] [Użycie wywoływania funkcji z Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
      -  [📓] [Użycie wywoływania funkcji do tworzenia multi-agentów z Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
      -  [📓] [Użycie wywoływania funkcji z Ollama](./md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
      -  [📓] [Użycie wywoływania funkcji z ONNX](./md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)
  - Przykłady miksowania multimodalnego
    - Przykłady Phi-4 🆕
      -  [📓] [Użycie Phi-4-multimodal jako dziennikarza technologicznego](./md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
      - [Aplikacja konsolowa .NET używająca Phi-4-multimodal do analizy obrazów](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Dostrajanie Phi
  - [Scenariusze dostrajania](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [Dostrajanie vs RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [Dostrajanie - Niech Phi-3 stanie się ekspertem branżowym](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [Dostrajanie Phi-3 z AI Toolkit dla VS Code](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Dostrajanie Phi-3 z Azure Machine Learning Service](./md/03.FineTuning/Introduce_AzureML.md)
  - [Dostrajanie Phi-3 z Lora](./md/03.FineTuning/FineTuning_Lora.md)
  - [Dostrajanie Phi-3 z QLora](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Dostrajanie Phi-3 z Azure AI Foundry](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Dostrajanie Phi-3 z Azure ML CLI/SDK](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Dostrajanie z Microsoft Olive](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Laboratorium praktyczne z dostrajaniem Microsoft Olive](./md/03.FineTuning/olive-lab/readme.md)
  - [Dostrajanie Phi-3-vision z Weights and Bias](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [Dostrajanie Phi-3 z Apple MLX Framework](./md/03.FineTuning/FineTuning_MLX.md)
  - [Dostrajanie Phi-3-vision (oficjalne wsparcie)](./md/03.FineTuning/FineTuning_Vision.md)
  - [Dostrajanie Phi-3 z Kaito AKS, Azure Containers (oficjalne wsparcie)](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Dostrajanie Phi-3 i 3.5 Vision](https://github.com/2U1/Phi3-Vision-Finetune)

- Laboratorium praktyczne
  - [Odkrywanie najnowocześniejszych modeli: LLMs, SLMs, lokalny rozwój i więcej](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [Odblokowywanie potencjału NLP: Dostrajanie z Microsoft Olive](https://github.com/azure/Ignite_FineTuning_workshop)

- Prace badawcze i publikacje naukowe

  - [Podręczniki to wszystko, czego potrzebujesz II: raport techniczny phi-1.5](https://arxiv.org/abs/2309.05463)
  - [Raport techniczny Phi-3: Wysoce zdolny model językowy lokalnie na Twoim telefonie](https://arxiv.org/abs/2404.14219)
  - [Raport techniczny Phi-4](https://arxiv.org/abs/2412.08905)
  - [Raport techniczny Phi-4-Mini: Kompaktowe, a jednocześnie potężne multimodalne modele językowe za pomocą mieszanki LoRA](https://arxiv.org/abs/2503.01743)
  - [Optymalizacja małych modeli językowych do wywoływania funkcji w pojeździe](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) Dostosowywanie PHI-3 do odpowiedzi na pytania wielokrotnego wyboru: Metodologia, wyniki i wyzwania](https://arxiv.org/abs/2501.01588)
  - [Raport techniczny Phi-4-reasoning](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Raport techniczny Phi-4-mini-reasoning](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Korzystanie z modeli Phi

### Phi na Azure AI Foundry

Możesz dowiedzieć się, jak korzystać z Microsoft Phi i jak budować rozwiązania E2E na różnych urządzeniach sprzętowych. Aby samodzielnie przetestować Phi, zacznij od zabawy z modelami i dostosowywania Phi do swoich scenariuszy, korzystając z [Katalogu modeli Azure AI Foundry Azure AI](https://aka.ms/phi3-azure-ai). Więcej informacji znajdziesz w rozdziale Rozpoczęcie pracy z [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md)

**Plac zabaw**  
Każdy model ma dedykowany plac zabaw do testowania modelu [Azure AI Playground](https://aka.ms/try-phi3).

### Phi na modelach GitHub

Możesz dowiedzieć się, jak korzystać z Microsoft Phi i jak budować rozwiązania E2E na różnych urządzeniach sprzętowych. Aby samodzielnie przetestować Phi, zacznij od zabawy z modelem i dostosowywania Phi do swoich scenariuszy, korzystając z [Katalogu modeli GitHub](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo). Więcej informacji znajdziesz w rozdziale Rozpoczęcie pracy z [Katalogiem modeli GitHub](/md/02.QuickStart/GitHubModel_QuickStart.md)

**Plac zabaw**  
Każdy model ma dedykowany [plac zabaw do testowania modelu](/md/02.QuickStart/GitHubModel_QuickStart.md).

### Phi na Hugging Face

Model możesz także znaleźć na [Hugging Face](https://huggingface.co/microsoft)

**Plac zabaw**  
[Plac zabaw Hugging Chat](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

 ## 🎒 Inne kursy

Nasz zespół tworzy także inne kursy! Sprawdź:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j dla początkujących](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js dla początkujących](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![LangChain dla początkujących](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### Azure / Edge / MCP / Agenci
[![AZD dla początkujących](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI dla początkujących](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP dla początkujących](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Agenci AI dla początkujących](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Seria Generatywnej AI
[![Generatywna AI dla początkujących](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generatywna AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generatywna AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generatywna AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Core Learning
[![ML dla początkujących](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science dla początkujących](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI dla początkujących](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Cyberbezpieczeństwo dla początkujących](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Web Dev dla początkujących](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT dla początkujących](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR Development dla początkujących](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Seria Copilot
[![Copilot do AI z programowaniem w parach](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot dla C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Przygoda Copilot](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Odpowiedzialna AI

Microsoft zobowiązuje się do pomocy naszym klientom w odpowiedzialnym korzystaniu z naszych produktów AI, dzieląc się naszymi doświadczeniami i budując partnerstwa oparte na zaufaniu za pomocą narzędzi takich jak Notatki dotyczące przejrzystości i Oceny wpływu. Wiele z tych zasobów znajduje się pod adresem [https://aka.ms/RAI](https://aka.ms/RAI).  
Podejście Microsoft do odpowiedzialnej AI opiera się na naszych zasadach AI dotyczących uczciwości, niezawodności i bezpieczeństwa, prywatności i ochrony, inkluzywności, przejrzystości oraz odpowiedzialności.

Duże modele językowe, obrazowe i mowy - takie jak te użyte w tym przykładzie - mogą potencjalnie zachowywać się w sposób nieuczciwy, zawodny lub obraźliwy, co może powodować szkody. Proszę zapoznać się z [Notatką o przejrzystości usługi Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text), aby być poinformowanym o ryzykach i ograniczeniach.

Zalecanym sposobem ograniczenia tych ryzyk jest zamieszczenie w architekturze systemu bezpieczeństwa, który może wykrywać i zapobiegać szkodliwemu zachowaniu. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) zapewnia niezależną warstwę ochrony, zdolną do wykrywania szkodliwych treści generowanych przez użytkowników i AI w aplikacjach i usługach. Azure AI Content Safety obejmuje interfejsy API tekstu i obrazu, które pozwalają wykrywać materiały szkodliwe. W Azure AI Foundry usługa Content Safety pozwala na przeglądanie, eksplorowanie i testowanie przykładowego kodu do wykrywania szkodliwych treści w różnych modalnościach. Następująca [dokumentacja szybkiego startu](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) przeprowadzi Cię przez proces wysyłania żądań do tej usługi.
Innym aspektem, który należy wziąć pod uwagę, jest ogólna wydajność aplikacji. W przypadku aplikacji wielomodalnych i wielomodelowych wydajność rozumiemy jako działanie systemu zgodnie z oczekiwaniami Twoimi i użytkowników, w tym niezapewnianie szkodliwych wyników. Ważne jest, aby ocenić wydajność całej aplikacji za pomocą [oceniania wydajności, jakości, ryzyka i bezpieczeństwa](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in). Masz również możliwość tworzenia i oceniania za pomocą [niestandardowych oceniających](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators).

Możesz ocenić swoją aplikację AI w środowisku programistycznym, korzystając z [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html). Mając do dyspozycji zestaw danych testowych lub cel, generacje Twojej aplikacji generatywnej AI są ilościowo mierzone za pomocą wbudowanych lub wybranych przez Ciebie niestandardowych oceniających. Aby rozpocząć pracę z Azure AI Evaluation SDK i ocenić swój system, możesz skorzystać z [przewodnika szybkiego startu](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Po przeprowadzeniu oceny możesz [zwizualizować wyniki w Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results). 

## Znaki towarowe

Ten projekt może zawierać znaki towarowe lub logotypy projektów, produktów lub usług. Autoryzowane użycie znaków towarowych lub logotypów Microsoft podlega i musi być zgodne z [Wytycznymi dotyczącymi znaków towarowych i marki Microsoft](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).
Użycie znaków towarowych lub logotypów Microsoft w zmodyfikowanych wersjach tego projektu nie może powodować zamieszania ani sugerować sponsorowania przez Microsoft. Każde użycie znaków towarowych lub logotypów stron trzecich podlega ich własnym zasadom.

## Uzyskanie pomocy

Jeśli utkniesz lub masz pytania dotyczące tworzenia aplikacji AI, dołącz do:

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

Jeśli masz uwagi dotyczące produktu lub napotkasz błędy podczas tworzenia, odwiedź:

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być traktowany jako źródło autorytatywne. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->