# Phi Cookbook: Praktyczne przykłady z modelami Phi Microsoftu

[![Otwórz i używaj przykładów w GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Otwórz w Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![Współtwórcy GitHub](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![Problemy GitHub](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![Pull requesty GitHub](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![Zapraszamy PR](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![Obserwujący GitHub](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![Forki GitHub](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![Gwiazdki GitHub](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi to seria otwartoźródłowych modeli AI opracowanych przez Microsoft.

Phi jest obecnie najmocniejszym i najbardziej opłacalnym małym modelem językowym (SLM), z bardzo dobrymi wynikami w wielu językach, rozumowaniu, generowaniu tekstu/rozmów, kodowaniu, obrazach, dźwięku i innych scenariuszach.

Możesz wdrożyć Phi w chmurze lub na urządzeniach brzegowych i łatwo budować aplikacje generatywnej sztucznej inteligencji z ograniczoną mocą obliczeniową.

Wykonaj te kroki, aby rozpocząć korzystanie z tych zasobów:
1. **Rozgałęź repozytorium**: Kliknij [![Forki GitHub](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **Sklonuj repozytorium**: `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Dołącz do Microsoft AI Discord Community i poznaj ekspertów oraz innych deweloperów**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/pl/cover.eb18d1b9605d754b.webp)

### 🌐 Wsparcie wielojęzyczne

#### Wspierane przez GitHub Action (Automatycznie i zawsze aktualne)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[arabski](../ar/README.md) | [bengalski](../bn/README.md) | [bułgarski](../bg/README.md) | [birmański (Myanmar)](../my/README.md) | [chiński (uproszczony)](../zh-CN/README.md) | [chiński (tradycyjny, Hong Kong)](../zh-HK/README.md) | [chiński (tradycyjny, Makau)](../zh-MO/README.md) | [chiński (tradycyjny, Tajwan)](../zh-TW/README.md) | [chorwacki](../hr/README.md) | [czeski](../cs/README.md) | [duński](../da/README.md) | [holenderski](../nl/README.md) | [estoński](../et/README.md) | [fiński](../fi/README.md) | [francuski](../fr/README.md) | [niemiecki](../de/README.md) | [grecki](../el/README.md) | [hebrajski](../he/README.md) | [hindi](../hi/README.md) | [węgierski](../hu/README.md) | [indonezyjski](../id/README.md) | [włoski](../it/README.md) | [japoński](../ja/README.md) | [kannada](../kn/README.md) | [khmerski](../km/README.md) | [koreański](../ko/README.md) | [litewski](../lt/README.md) | [malajski](../ms/README.md) | [malajalam](../ml/README.md) | [manipuri (Meitei Mayek)](../mni/README.md) | [marathi](../mr/README.md) | [nepalski](../ne/README.md) | [pidgin nigeryjski](../pcm/README.md) | [norweski](../no/README.md) | [perski (farsi)](../fa/README.md) | [polski](./README.md) | [portugalski (Brazylia)](../pt-BR/README.md) | [portugalski (Portugalia)](../pt-PT/README.md) | [pendżabski (Gurmukhi)](../pa/README.md) | [rumuński](../ro/README.md) | [rosyjski](../ru/README.md) | [serbski (cyrylica)](../sr/README.md) | [słowacki](../sk/README.md) | [słoweński](../sl/README.md) | [hiszpański](../es/README.md) | [suahili](../sw/README.md) | [szwedzki](../sv/README.md) | [tagalog (filipiński)](../tl/README.md) | [tamil](../ta/README.md) | [telugu](../te/README.md) | [tajski](../th/README.md) | [turecki](../tr/README.md) | [ukraiński](../uk/README.md) | [urdu](../ur/README.md) | [wietnamski](../vi/README.md)

> **Wolisz klonować lokalnie?**
>
> To repozytorium zawiera tłumaczenia na ponad 50 języków, co znacznie zwiększa rozmiar pobierania. Aby sklonować bez tłumaczeń, użyj sparse checkout:
>
> **Bash / macOS / Linux:**
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/PhiCookBook.git
> cd PhiCookBook
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
>
> **CMD (Windows):**
> ```cmd
> git clone --filter=blob:none --sparse https://github.com/microsoft/PhiCookBook.git
> cd PhiCookBook
> git sparse-checkout set --no-cone "/*" "!translations" "!translated_images"
> ```
>
> To daje wszystko, czego potrzebujesz, aby ukończyć kurs z dużo szybszym pobieraniem.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## Spis treści

- Wprowadzenie
  - [Witaj w rodzinie Phi](./md/01.Introduction/01/01.PhiFamily.md)
  - [Konfiguracja środowiska](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [Zrozumienie kluczowych technologii](./md/01.Introduction/01/01.Understandingtech.md)
  - [Bezpieczeństwo AI dla modeli Phi](./md/01.Introduction/01/01.AISafety.md)
  - [Wsparcie sprzętowe Phi](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Modele Phi i dostępność na platformach](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Korzystanie z Guidance-ai i Phi](./md/01.Introduction/01/01.Guidance.md)
  - [Modele na rynku GitHub](https://github.com/marketplace/models)
  - [Katalog modele AI Azure](https://ai.azure.com)

- Inference Phi w różnych środowiskach
    -  [Hugging face](./md/01.Introduction/02/01.HF.md)
    -  [Modele GitHub](./md/01.Introduction/02/02.GitHubModel.md)
    -  [Katalog modeli Microsoft Foundry](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [Zestaw narzędzi AI VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    -  [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md)

- Inference Phi Family
    - [Inference Phi w iOS](./md/01.Introduction/03/iOS_Inference.md)
    - [Inference Phi w Androidzie](./md/01.Introduction/03/Android_Inference.md)
    - [Inference Phi w Jetson](./md/01.Introduction/03/Jetson_Inference.md)
    - [Inference Phi na komputerze AI](./md/01.Introduction/03/AIPC_Inference.md)
    - [Inference Phi z Apple MLX Framework](./md/01.Introduction/03/MLX_Inference.md)
    - [Inference Phi na lokalnym serwerze](./md/01.Introduction/03/Local_Server_Inference.md)
    - [Inference Phi na zdalnym serwerze z użyciem AI Toolkit](./md/01.Introduction/03/Remote_Interence.md)
    - [Inference Phi w Rust](./md/01.Introduction/03/Rust_Inference.md)
    - [Inference Phi--Vision lokalnie](./md/01.Introduction/03/Vision_Inference.md)
    - [Inference Phi z Kaito AKS, Azure Containers (oficjalne wsparcie)](./md/01.Introduction/03/Kaito_Inference.md)
-  [Kwantyzacja rodziny Phi](./md/01.Introduction/04/QuantifyingPhi.md)
    - [Kwantyzacja Phi-3.5 / 4 za pomocą llama.cpp](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [Kwantyzacja Phi-3.5 / 4 za pomocą rozszerzeń Generative AI dla onnxruntime](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Kwantyzacja Phi-3.5 / 4 za pomocą Intel OpenVINO](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Kwantyzacja Phi-3.5 / 4 za pomocą Apple MLX Framework](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

-  Ewaluacja Phi
    - [Response AI](./md/01.Introduction/05/ResponsibleAI.md)
    - [Microsoft Foundry do ewaluacji](./md/01.Introduction/05/AIFoundry.md)
    - [Użycie Promptflow do ewaluacji](./md/01.Introduction/05/Promptflow.md)
 
- RAG z Azure AI Search
    - [Jak używać Phi-4-mini i Phi-4-multimodal (RAG) z Azure AI Search](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)
    - [Zero-Cloud lokalny hybrydowy RAG z SQLite FTS5 i phi-4-mini](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-mini_Local_Hybrid_RAG_SQLite_FTS5.ipynb)

- Przykłady rozwoju aplikacji Phi
  - Aplikacje Tekstowe i Czatujące
    - Przykłady Phi-4
      - [📓] [Czat z modelem Phi-4-mini ONNX](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Czat z lokalnym modelem Phi-4 ONNX .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Konsolowa aplikacja czatu .NET z Phi-4 ONNX wykorzystująca Semantic Kernel](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Przykłady Phi-3 / 3.5
      - [Lokalny chatbot w przeglądarce używający Phi3, ONNX Runtime Web i WebGPU](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [Chat OpenVino](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [Multi Model - interaktywny Phi-3-mini i OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - tworzenie wrappera i używanie Phi-3 z MLFlow](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [Optymalizacja modelu - jak zoptymalizować model Phi-3-min dla ONNX Runtime Web z Olive](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [Aplikacja WinUI3 z Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      -[Przykład aplikacji WinUI3 z wieloma modelami zasilanymi AI](https://github.com/microsoft/ai-powered-notes-winui3-sample)
      - [Dostrajanie i integracja własnych modeli Phi-3 z Prompt flow](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
      - [Dostrajanie i integracja własnych modeli Phi-3 z Prompt flow w Microsoft Foundry](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
      - [Ewaluacja dostrojonego modelu Phi-3 / Phi-3.5 w Microsoft Foundry ze skupieniem na zasadach odpowiedzialnej AI Microsoftu](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
      - [📓] [Przykład przewidywania języka Phi-3.5-mini-instruct (chiński/angielski)](./md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
      - [Chatbot Phi-3.5-Instruct WebGPU RAG](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
      - [Użycie Windows GPU do tworzenia rozwiązania Prompt flow z Phi-3.5-Instruct ONNX](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
      - [Użycie Microsoft Phi-3.5 tflite do stworzenia aplikacji na Androida](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
      - [Przykład Q&A .NET używający lokalnego modelu ONNX Phi-3 z Microsoft.ML.OnnxRuntime](../../md/04.HOL/dotnet/src/LabsPhi301)
      - [Konsolowa aplikacja czatu .NET z Semantic Kernel i Phi-3](../../md/04.HOL/dotnet/src/LabsPhi302)

  - Przykłady oparte na Azure AI Inference SDK
    - Przykłady Phi-4
      - [📓] [Generowanie kodu projektu z użyciem Phi-4-multimodal](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
    - Przykłady Phi-3 / 3.5
      - [Zbuduj własnego Visual Studio Code GitHub Copilot Chat z rodziną Microsoft Phi-3](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
      - [Stwórz własnego agenta Visual Studio Code Chat Copilot z Phi-3.5 korzystając z modeli GitHub](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

  - Zaawansowane przykłady rozumowania
    - Przykłady Phi-4 
      - [📓] [Próbki Phi-4-mini-reasoning lub Phi-4-reasoning](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
      - [📓] [Dostrajanie Phi-4-mini-reasoning z Microsoft Olive](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Dostrajanie Phi-4-mini-reasoning z Apple MLX](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Phi-4-mini-reasoning z modelami GitHub](./md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
      - [📓] [Phi-4-mini-reasoning z modelami Microsoft Foundry](./md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
  - Demonstracje
      - [Demonstracje Phi-4-mini hostowane na Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
      - [Demonstracje Phi-4-multimodal hostowane na Hugginge Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
  - Próbki wizji
    - Próbki Phi-4 
      - [📓] [Używanie Phi-4-multimodal do czytania obrazów i generowania kodu](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
    - Próbki Phi-3 / 3.5
      -  [📓][Phi-3-vision-Image tekst na tekst](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
      - [📓][Phi-3-vision CLIP Embedding](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [DEMO: Phi-3 Recycling](https://github.com/jennifermarsman/PhiRecycling/)
      - [Phi-3-vision - asystent języka wizualnego - z Phi3-Vision i OpenVINO](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
      - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
      - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
      - [📓][Phi-3.5 Vision próbka multi-frame lub multi-obraz](./md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
      - [Lokalny model Phi-3 Vision ONNX używając Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi303)
      - [Menu bazujący lokalny model Phi-3 Vision ONNX używając Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi304)

  - Próbki Reasoning-Vision
    - Phi-4-Reasoning-Vision-15B 
      - [📓] [Użycie Phi-4-Reasoning-Vision-15B do wykrywania przechodzenia na czerwonym świetle](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_Jaywalking.ipynb)
      - [📓] [Użycie Phi-4-Reasoning-Vision-15B do matematyki](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_Math.ipynb)
      - [📓] [Użycie Phi-4-Reasoning-Vision-15B do wykrywania UI](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_ui.ipynb)

  - Próbki matematyczne
    -  Phi-4-Mini-Flash-Reasoning-Instruct Próbki  [Demo matematyczne z Phi-4-Mini-Flash-Reasoning-Instruct](./md/02.Application/09.Math/MathDemo.ipynb)

  - Próbki audio
    - Próbki Phi-4 
      - [📓] [Ekstrakcja transkryptów audio za pomocą Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
      - [📓] [Próbka audio Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
      - [📓] [Próbka tłumaczenia mowy Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
      - [.NET aplikacja konsolowa używająca Phi-4-multimodal Audio do analizy pliku audio i generowania transkryptu](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

  - Próbki MOE
    - Próbki Phi-3 / 3.5
      - [📓] [Modele Phi-3.5 Mixture of Experts (MoEs) przykład Social Media](./md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
      - [📓] [Budowanie pipeline'u Retrieval-Augmented Generation (RAG) z NVIDIA NIM Phi-3 MOE, Azure AI Search i LlamaIndex](./md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)
      - 
  - Próbki wywoływania funkcji
    - Próbki Phi-4 🆕
      -  [📓] [Używanie wywoływania funkcji z Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
      -  [📓] [Używanie wywoływania funkcji do tworzenia multi-agentów z Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
      -  [📓] [Używanie wywoływania funkcji z Ollama](./md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
      -  [📓] [Używanie wywoływania funkcji z ONNX](./md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)
  - Próbki mieszania multimodalnego
    - Próbki Phi-4 🆕
      -  [📓] [Używanie Phi-4-multimodal jako dziennikarza technologicznego](./md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
      - [.NET aplikacja konsolowa używająca Phi-4-multimodal do analizy obrazów](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Dostrajanie próbek Phi
  - [Scenariusze dostrajania](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [Dostrajanie kontra RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [Dostrajanie Phi-3, aby stał się ekspertem branżowym](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [Dostrajanie Phi-3 z AI Toolkit dla VS Code](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Dostrajanie Phi-3 z Azure Machine Learning Service](./md/03.FineTuning/Introduce_AzureML.md)
  - [Dostrajanie Phi-3 z Lora](./md/03.FineTuning/FineTuning_Lora.md)
  - [Dostrajanie Phi-3 z QLora](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Dostrajanie Phi-3 z Microsoft Foundry](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Dostrajanie Phi-3 z Azure ML CLI/SDK](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Dostrajanie z Microsoft Olive](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Dostrajanie z Microsoft Olive Laboratorium praktyczne](./md/03.FineTuning/olive-lab/readme.md)
  - [Dostrajanie Phi-3-vision z Weights and Bias](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [Dostrajanie Phi-3 z Apple MLX Framework](./md/03.FineTuning/FineTuning_MLX.md)
  - [Dostrajanie Phi-3-vision (oficjalne wsparcie)](./md/03.FineTuning/FineTuning_Vision.md)
  - [Dostrajanie Phi-3 z Kaito AKS, Azure Containers (oficjalne wsparcie)](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Dostrajanie Phi-3 i 3.5 Vision](https://github.com/2U1/Phi3-Vision-Finetune)

- Laboratorium praktyczne
  - [Odkrywanie nowoczesnych modeli: LLM, SLM, lokalny rozwój i więcej](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [Odblokowanie potencjału NLP: dostrajanie z Microsoft Olive](https://github.com/azure/Ignite_FineTuning_workshop)

- Artykuły akademickie i publikacje
  - [Textbooks Are All You Need II: phi-1.5 raport techniczny](https://arxiv.org/abs/2309.05463)
  - [Phi-3 raport techniczny: Wysoce zdolny model językowy lokalnie na twoim telefonie](https://arxiv.org/abs/2404.14219)
  - [Phi-4 raport techniczny](https://arxiv.org/abs/2412.08905)
  - [Phi-4-Mini raport techniczny: Kompaktowe lecz potężne multimodalne modele językowe za pomocą Mixture-of-LoRAs](https://arxiv.org/abs/2503.01743)
  - [Optymalizacja małych modeli językowych do wywoływania funkcji w pojeździe](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) Dostrajanie PHI-3 do odpowiadania na pytania wielokrotnego wyboru: metodologia, wyniki i wyzwania](https://arxiv.org/abs/2501.01588)
  - [Phi-4-reasoning raport techniczny](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Phi-4-mini-reasoning raport techniczny](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Korzystanie z modeli Phi

### Phi na Microsoft Foundry

Możesz nauczyć się jak używać Microsoft Phi i jak zbudować rozwiązania E2E na różnych urządzeniach sprzętowych. Aby doświadczyć Phi na własne oczy, zacznij od zabawy z modelami i dostosowywania Phi do swoich scenariuszy używając [Microsoft Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai). Więcej informacji znajdziesz w Rozpoczęciu pracy z [Microsoft Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md)

**Placek zabaw**
Każdy model ma dedykowane miejsce do testowania modelu [Azure AI Playground](https://aka.ms/try-phi3).

### Phi na modelach GitHub

Możesz nauczyć się jak używać Microsoft Phi i jak zbudować rozwiązania E2E na różnych urządzeniach sprzętowych. Aby doświadczyć Phi na własne oczy, zacznij od zabawy z modelem i dostosowywania Phi do swoich scenariuszy używając [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo). Więcej informacji znajdziesz w Rozpoczęciu pracy z [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md)

**Placek zabaw**
Każdy model ma dedykowane [miejsce do testowania modelu](/md/02.QuickStart/GitHubModel_QuickStart.md).

### Phi na Hugging Face

Model jest również dostępny na [Hugging Face](https://huggingface.co/microsoft)

**Placek zabaw**
 [Hugging Chat playground](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

 ## 🎒 Inne kursy

Nasz zespół produkuje też inne kursy! Sprawdź:

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
[![AI Agenci dla początkujących](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Seria Generative AI
[![Generative AI dla początkujących](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generative AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generative AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generative AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

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
[![Copilot do programowania w parze AI](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot do C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Odpowiedzialna sztuczna inteligencja 

Microsoft angażuje się w pomaganie naszym klientom w odpowiedzialnym korzystaniu z produktów AI, dzielenie się naszymi doświadczeniami oraz budowanie partnerstw opartych na zaufaniu za pomocą narzędzi takich jak Transparency Notes i Impact Assessments. Wiele z tych zasobów można znaleźć na [https://aka.ms/RAI](https://aka.ms/RAI).
Podejście Microsoft do odpowiedzialnej AI opiera się na naszych zasadach AI: uczciwości, niezawodności i bezpieczeństwie, prywatności i ochronie, inkluzywności, przejrzystości oraz odpowiedzialności.

Modele dużej skali do przetwarzania języka naturalnego, obrazów i mowy - takie jak te użyte w tym przykładzie - mogą potencjalnie zachowywać się w sposób niesprawiedliwy, zawodny lub obraźliwy, co może prowadzić do szkód. Proszę zapoznać się z [Notatką o przejrzystości usługi Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text), aby być świadomym ryzyk i ograniczeń.

Zalecanym podejściem do łagodzenia tych ryzyk jest uwzględnienie w swojej architekturze systemu bezpieczeństwa, który potrafi wykrywać i zapobiegać szkodliwemu zachowaniu. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) zapewnia niezależną warstwę ochrony, zdolną do wykrywania szkodliwych treści generowanych przez użytkowników i AI w aplikacjach i usługach. Azure AI Content Safety obejmuje interfejsy API do tekstu i obrazów, które pozwalają wykrywać materiały szkodliwe. W ramach Microsoft Foundry usługa Content Safety umożliwia przeglądanie, eksplorowanie oraz wypróbowanie przykładowego kodu do wykrywania szkodliwych treści w różnych modalnościach. Następująca [dokumentacja szybkiego startu](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) poprowadzi Cię przez składanie zapytań do usługi.

Kolejnym aspektem do uwzględnienia jest ogólna wydajność aplikacji. W przypadku aplikacji wielomodalnych i wielomodelowych wydajność oznacza, że system działa zgodnie z oczekiwaniami Twoimi i Twoich użytkowników, w tym nie generuje szkodliwych wyników. Ważne jest, aby ocenić wydajność całej aplikacji, korzystając z [ewaluatorów wydajności, jakości oraz ryzyka i bezpieczeństwa](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in). Masz też możliwość tworzenia i oceniania za pomocą [niestandardowych ewaluatorów](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators).

Możesz ocenić swoją aplikację AI w środowisku deweloperskim, używając [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html). Mając albo zestaw testowy, albo cel, wyniki generacji Twojej aplikacji generatywnej AI są mierzone ilościowo przy pomocy wbudowanych ewaluatorów lub wybranych przez Ciebie niestandardowych ewaluatorów. Aby zacząć pracę z azure ai evaluation sdk i ocenić swój system, możesz skorzystać z [przewodnika szybkiego startu](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Po wykonaniu uruchomienia ewaluacji możesz [wizualizować wyniki w Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results). 

## Znaki towarowe

Ten projekt może zawierać znaki towarowe lub logotypy projektów, produktów albo usług. Autoryzowane użycie znaków towarowych lub logotypów Microsoft podlega i musi przestrzegać [Zasad dotyczących znaków towarowych i marek Microsoft](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).
Użycie znaków towarowych lub logotypów Microsoft w zmodyfikowanych wersjach tego projektu nie może powodować zamieszania ani sugerować sponsoringu przez Microsoft. Każde użycie znaków towarowych lub logotypów stron trzecich podlega politykom tych stron trzecich.

## Uzyskiwanie pomocy

Jeśli napotkasz trudności lub masz pytania dotyczące tworzenia aplikacji AI, dołącz do:

[![Microsoft Foundry Discord](https://img.shields.io/badge/Discord-Microsoft_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

Jeśli masz uwagi dotyczące produktu lub napotkasz błędy podczas tworzenia, odwiedź:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->