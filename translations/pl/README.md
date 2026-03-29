# Phi Cookbook: Praktyczne przykłady z modelami Phi Microsoftu

[![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub issues](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub watchers](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub stars](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi to seria otwartoźródłowych modeli AI opracowanych przez Microsoft.

Phi jest obecnie najpotężniejszym i najbardziej opłacalnym małym modelem językowym (SLM), osiągając bardzo dobre wyniki w wielu językach, rozumowaniu, generowaniu tekstu/czatu, kodowaniu, obrazach, dźwięku oraz innych zastosowaniach.

Możesz wdrożyć Phi w chmurze lub na urządzeniach brzegowych i z łatwością tworzyć aplikacje generatywnej AI przy ograniczonej mocy obliczeniowej.

Wykonaj następujące kroki, aby rozpocząć korzystanie z tych zasobów:
1. **Rozgałęź repozytorium**: Kliknij [![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **Sklonuj repozytorium**:   `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Dołącz do społeczności Microsoft AI na Discordzie i poznaj ekspertów oraz innych deweloperów**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/pl/cover.eb18d1b9605d754b.webp)

### 🌐 Wsparcie wielu języków

#### Obsługiwane przez GitHub Action (automatyczne i zawsze aktualne)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabskiego](../ar/README.md) | [Bengalskiego](../bn/README.md) | [Bułgarskiego](../bg/README.md) | [Birmańskiego (Myanmar)](../my/README.md) | [Chińskiego (uproszczonego)](../zh-CN/README.md) | [Chińskiego (tradycyjnego, Hongkong)](../zh-HK/README.md) | [Chińskiego (tradycyjnego, Makau)](../zh-MO/README.md) | [Chińskiego (tradycyjnego, Tajwan)](../zh-TW/README.md) | [Chorwackiego](../hr/README.md) | [Czeskiego](../cs/README.md) | [Duńskiego](../da/README.md) | [Niderlandzkiego](../nl/README.md) | [Estońskiego](../et/README.md) | [Fińskiego](../fi/README.md) | [Francuskiego](../fr/README.md) | [Niemieckiego](../de/README.md) | [Greckiego](../el/README.md) | [Hebrajskiego](../he/README.md) | [Hindi](../hi/README.md) | [Węgierskiego](../hu/README.md) | [Indonezyjskiego](../id/README.md) | [Włoskiego](../it/README.md) | [Japońskiego](../ja/README.md) | [Kannada](../kn/README.md) | [Koreańskiego](../ko/README.md) | [Litewskiego](../lt/README.md) | [Malajskiego](../ms/README.md) | [Malajalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepalskiego](../ne/README.md) | [Nigeryjskiego pidżynu](../pcm/README.md) | [Norweskiego](../no/README.md) | [Perskiego (Farsi)](../fa/README.md) | [Polskiego](./README.md) | [Portugalskiego (Brazylia)](../pt-BR/README.md) | [Portugalskiego (Portugalia)](../pt-PT/README.md) | [Pendżabskiego (Gurmukhi)](../pa/README.md) | [Rumuńskiego](../ro/README.md) | [Rosyjskiego](../ru/README.md) | [Serbskiego (cyrylica)](../sr/README.md) | [Słowackiego](../sk/README.md) | [Słoweńskiego](../sl/README.md) | [Hiszpańskiego](../es/README.md) | [Suahili](../sw/README.md) | [Szwedzkiego](../sv/README.md) | [Tagalog (Filipiński)](../tl/README.md) | [Tamilski](../ta/README.md) | [Telugu](../te/README.md) | [Tajski](../th/README.md) | [Turecki](../tr/README.md) | [Ukraiński](../uk/README.md) | [Urdu](../ur/README.md) | [Wietnamski](../vi/README.md)

> **Wolisz klonować lokalnie?**
>
> To repozytorium zawiera ponad 50 tłumaczeń językowych, co znacznie zwiększa rozmiar pobierania. Aby sklonować bez tłumaczeń, użyj sparse checkout:
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
> To daje wszystko, czego potrzebujesz, aby ukończyć kurs znacznie szybciej pobierając pliki.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## Spis treści
- Wprowadzenie - [Witamy w Rodzinie Phi](./md/01.Introduction/01/01.PhiFamily.md) - [Konfiguracja środowiska](./md/01.Introduction/01/01.EnvironmentSetup.md) - [Zrozumienie kluczowych technologii](./md/01.Introduction/01/01.Understandingtech.md) - [Bezpieczeństwo AI dla modeli Phi](./md/01.Introduction/01/01.AISafety.md) - [Wsparcie sprzętowe Phi](./md/01.Introduction/01/01.Hardwaresupport.md) - [Modele Phi i dostępność na różnych platformach](./md/01.Introduction/01/01.Edgeandcloud.md) - [Używanie Guidance-ai i Phi](./md/01.Introduction/01/01.Guidance.md) - [Modele na GitHub Marketplace](https://github.com/marketplace/models) - [Katalog modeli Azure AI](https://ai.azure.com) - Inference Phi w różnych środowiskach - [Hugging face](./md/01.Introduction/02/01.HF.md) - [Modele GitHub](./md/01.Introduction/02/02.GitHubModel.md) - [Katalog modeli Microsoft Foundry](./md/01.Introduction/02/03.AzureAIFoundry.md) - [Ollama](./md/01.Introduction/02/04.Ollama.md) - [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md) - [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md) - [Foundry lokalnie](./md/01.Introduction/02/07.FoundryLocal.md) - Inference Phi Family - [Inference Phi na iOS](./md/01.Introduction/03/iOS_Inference.md) - [Inference Phi na Androidzie](./md/01.Introduction/03/Android_Inference.md) - [Inference Phi na Jetson](./md/01.Introduction/03/Jetson_Inference.md) - [Inference Phi na AI PC](./md/01.Introduction/03/AIPC_Inference.md) - [Inference Phi z wykorzystaniem Apple MLX Framework](./md/01.Introduction/03/MLX_Inference.md) - [Inference Phi na lokalnym serwerze](./md/01.Introduction/03/Local_Server_Inference.md) - [Inference Phi na zdalnym serwerze za pomocą AI Toolkit](./md/01.Introduction/03/Remote_Interence.md) - [Inference Phi z Rust](./md/01.Introduction/03/Rust_Inference.md) - [Inference Phi – Vision lokalnie](./md/01.Introduction/03/Vision_Inference.md) - [Inference Phi z Kaito AKS, kontenery Azure (oficjalne wsparcie)](./md/01.Introduction/03/Kaito_Inference.md) - [Quantifying Phi Family](./md/01.Introduction/04/QuantifyingPhi.md) - [Kwantyzacja Phi-3.5 / 4 za pomocą llama.cpp](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md) - [Kwntyzacja Phi-3.5 / 4 przy użyciu rozszerzeń Generative AI dla onnxruntime](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md) - [Kwntyzacja Phi-3.5 / 4 z użyciem Intel OpenVINO](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md) - [Kwntyzacja Phi-3.5 / 4 za pomocą Apple MLX Framework](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md) - Ocena Phi - [Odpowiedzialne AI](./md/01.Introduction/05/ResponsibleAI.md) - [Microsoft Foundry do oceny](./md/01.Introduction/05/AIFoundry.md) - [Używanie Promptflow do oceny](./md/01.Introduction/05/Promptflow.md) - RAG z Azure AI Search - [Jak używać Phi-4-mini i Phi-4-multimodal (RAG) z Azure AI Search](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb) - Przykłady rozwoju aplikacji Phi - Aplikacje tekstowe i czatowe - Przykłady Phi-4 - [📓] [Czat z modelem Phi-4-mini ONNX](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md) - [Czat z lokalnym modelem Phi-4 ONNX .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) - [Czat .NET Console App z Phi-4 ONNX używając Semantic Kernel](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) - Przykłady Phi-3 / 3.5 - [Lokalny chatbot w przeglądarce używając Phi3, ONNX Runtime Web i WebGPU](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat) - [OpenVino Czat](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md) - [Wielomodelowy - Interaktywny Phi-3-mini i OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md) - [MLFlow - Tworzenie wrappera i używanie Phi-3 z MLFlow](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md) - [Optymalizacja modelu - jak zoptymalizować model Phi-3-min do ONNX Runtime Web za pomocą Olive](https://github.com/microsoft/Olive/tree/main/examples/phi3) - [WinUI3 App z Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/) - [WinUI3 wielomodelowa aplikacja notesów zasilana AI - przykład](https://github.com/microsoft/ai-powered-notes-winui3-sample) - [Dostrajanie i integracja niestandardowych modeli Phi-3 z Prompt flow](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md) - [Dostrajanie i integracja niestandardowych modeli Phi-3 z Prompt flow w Microsoft Foundry](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md) - [Ocena dostrojonego modelu Phi-3 / Phi-3.5 w Microsoft Foundry ze szczególnym uwzględnieniem zasad Odpowiedzialnego AI Microsoftu](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md) - [📓] [Przykład predykcji językowej Phi-3.5-mini-instruct (chiński/angielski)](./md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb) - [Phi-3.5-Instruct WebGPU RAG Chatbot](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md) - [Użycie Windows GPU do stworzenia rozwiązania Prompt flow z Phi-3.5-Instruct ONNX](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md) - [Użycie Microsoft Phi-3.5 tflite do stworzenia aplikacji na Android](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md) - [Przykład Q&A .NET używając lokalnego modelu ONNX Phi-3 z Microsoft.ML.OnnxRuntime](../../md/04.HOL/dotnet/src/LabsPhi301) - [Console chat .NET app z Semantic Kernel i Phi-3](../../md/04.HOL/dotnet/src/LabsPhi302) - Przykłady kodu SDK Azure AI Inference - Przykłady Phi-4 - [📓] [Generowanie kodu projektu z użyciem Phi-4-multimodal](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md) - Przykłady Phi-3 / 3.5 - [Stwórz własny czat GitHub Copilot dla Visual Studio Code z Microsoft Phi-3 Family](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md) - [Stwórz własnego agenta czatu Visual Studio Code Copilot z Phi-3.5 używając modeli GitHub](./md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md) - Przykłady zaawansowanego rozumowania - Przykłady Phi-4 - [📓] [Phi-4-mini-reasoning lub Phi-4-reasoning - przykłady](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md) - [📓] [Dostrajanie Phi-4-mini-reasoning z Microsoft Olive](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb) - [📓] [Dostrajanie Phi-4-mini-reasoning z Apple MLX](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb) - [📓] [Phi-4-mini-reasoning z modelami GitHub](./md/02.Application/02.Code/Phi4r/github_models_inference.ipynb) - [📓] [Phi-4-mini-reasoning z modelami Microsoft Foundry](./md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb) -
Pokazy - [Pokazy Phi-4-mini hostowane na Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo) - [Pokazy Phi-4-multimodal hostowane na Hugginge Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo) - Próbki wizji - Próbki Phi-4 - [📓] [Użyj Phi-4-multimodal do odczytu obrazów i generowania kodu](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) - Próbki Phi-3 / 3.5 - [📓][Phi-3-vision-Obraz tekst na tekst](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb) - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html) - [📓][Phi-3-vision CLIP Embedding](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb) - [DEMO: Phi-3 Recycling](https://github.com/jennifermarsman/PhiRecycling/) - [Phi-3-vision - Asystent języka wizualnego - z Phi3-Vision i OpenVINO](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html) - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md) - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md) - [📓][Phi-3.5 Vision wieloklatkowy lub wieloobrazkowy przykład](./md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb) - [Phi-3 Vision Lokalny Model ONNX używając Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi303) - [Menu oparte na Phi-3 Vision Lokalnym Modelu ONNX używając Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi304) - Próbki Rozumowania-Wizji - Phi-4-Reasoning-Vision-15B - [📓] [Używanie Phi-4-Reasoning-Vision-15B do wykrywania nielegalnego przechodzenia przez ulicę](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_Jaywalking.ipynb) - [📓] [Używanie Phi-4-Reasoning-Vision-15B do matematyki](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_Math.ipynb) - [📓] [Używanie Phi-4-Reasoning-Vision-15B do wykrywania interfejsu użytkownika](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_ui.ipynb) - Próbki matematyczne - Próbki Phi-4-Mini-Flash-Reasoning-Instruct [Demo matematyczne z Phi-4-Mini-Flash-Reasoning-Instruct](./md/02.Application/09.Math/MathDemo.ipynb) - Próbki audio - Próbki Phi-4 - [📓] [Wydobywanie transkryptów audio za pomocą Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Transciption/README.md) - [📓] [Próbka audio Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Siri/demo.ipynb) - [📓] [Próbka tłumaczenia mowy Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Translate/demo.ipynb) - [Aplikacja konsolowa .NET używająca Phi-4-multimodal Audio do analizy pliku audio i generowania transkryptu](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) - Próbki MOE - Próbki Phi-3 / 3.5 - [📓] [Modele Mieszanki Ekspertów Phi-3.5 (MoEs) Przykład mediów społecznościowych](./md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb) - [📓] [Budowanie potoku Retrieval-Augmented Generation (RAG) z NVIDIA NIM Phi-3 MOE, Azure AI Search i LlamaIndex](./md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb) - - Próbki wywołań funkcji - Próbki Phi-4 🆕 - [📓] [Używanie wywołań funkcji z Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md) - [📓] [Używanie wywołań funkcji do tworzenia multi-agentów z Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb) - [📓] [Używanie wywołań funkcji z Ollama](./md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb) - [📓] [Używanie wywołań funkcji z ONNX](./md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb) - Próbki mieszania multimodalnego - Próbki Phi-4 🆕 - [📓] [Używanie Phi-4-multimodal jako dziennikarza technologicznego](./md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb) - [Aplikacja konsolowa .NET używająca Phi-4-multimodal do analizy obrazów](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) - Próbki dostrajania Phi - [Scenariusze dostrajania](./md/03.FineTuning/FineTuning_Scenarios.md) - [Dostrajanie vs RAG](./md/03.FineTuning/FineTuning_vs_RAG.md) - [Dostrajanie - Pozwól Phi-3 stać się ekspertem branżowym](./md/03.FineTuning/LetPhi3gotoIndustriy.md) - [Dostrajanie Phi-3 z AI Toolkit dla VS Code](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md) - [Dostrajanie Phi-3 z Azure Machine Learning Service](./md/03.FineTuning/Introduce_AzureML.md) - [Dostrajanie Phi-3 z Lora](./md/03.FineTuning/FineTuning_Lora.md) - [Dostrajanie Phi-3 z QLora](./md/03.FineTuning/FineTuning_Qlora.md) - [Dostrajanie Phi-3 z Microsoft Foundry](./md/03.FineTuning/FineTuning_AIFoundry.md) - [Dostrajanie Phi-3 z Azure ML CLI/SDK](./md/03.FineTuning/FineTuning_MLSDK.md) - [Dostrajanie z Microsoft Olive](./md/03.FineTuning/FineTuning_MicrosoftOlive.md) - [Dostrajanie z Microsoft Olive Warsztaty praktyczne](./md/03.FineTuning/olive-lab/readme.md) - [Dostrajanie Phi-3-vision z Weights and Bias](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md) - [Dostrajanie Phi-3 z Apple MLX Framework](./md/03.FineTuning/FineTuning_MLX.md) - [Dostrajanie Phi-3-vision (wsparcie oficjalne)](./md/03.FineTuning/FineTuning_Vision.md) - [Dostrajanie Phi-3 z Kaito AKS, Azure Containers (wsparcie oficjalne)](./md/03.FineTuning/FineTuning_Kaito.md) - [Dostrajanie Phi-3 i 3.5 Vision](https://github.com/2U1/Phi3-Vision-Finetune) - Warsztaty praktyczne - [Eksploracja najnowszych modeli: LLM, SLM, rozwój lokalny i więcej](https://github.com/microsoft/aitour-exploring-cutting-edge-models) - [Odkrywanie potencjału NLP: Dostrajanie z Microsoft Olive](https://github.com/azure/Ignite_FineTuning_workshop) - Prace naukowe i publikacje - [Textbooks Are All You Need II: raport techniczny phi-1.5](https://arxiv.org/abs/2309.05463) - [Raport techniczny Phi-3: bardzo zdolny model językowy lokalnie na twoim telefonie](https://arxiv.org/abs/2404.14219) - [Raport techniczny Phi-4](https://arxiv.org/abs/2412.08905) - [Raport techniczny Phi-4-Mini: kompaktowe, ale potężne multimodalne modele językowe przez mieszankę LoRAs](https://arxiv.org/abs/2503.01743) - [Optymalizacja małych modeli językowych do wywoływania funkcji w pojeździe](https://arxiv.org/abs/2501.02342) - [(WhyPHI) Dostrajanie PHI-3 do odpowiadania na pytania wielokrotnego wyboru: metodologia, wyniki i wyzwania](https://arxiv.org/abs/2501.01588) - [Raport techniczny Phi-4-reasoning](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
- [Raport techniczny Phi-4-mini-reasoning](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)
# Phi Cookbook: Praktyczne przykłady z modelami Phi firmy Microsoft

[![Otwórz i używaj przykładów w GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Otwórz w Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![Współtwórcy GitHub](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![Problemy GitHub](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![Żądania w GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![Zapraszamy do PR](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![Obserwujący GitHub](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![Forki GitHub](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![Gwiazdki GitHub](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi to seria otwartych modeli AI opracowanych przez Microsoft.

Phi to obecnie najpotężniejszy i najbardziej opłacalny mały model językowy (SLM), z bardzo dobrymi wynikami w wielu językach, rozumowaniu, generowaniu tekstu/rozmów, kodowaniu, obrazach, dźwięku i innych scenariuszach.

Możesz wdrażać Phi w chmurze lub na urządzeniach brzegowych, a także łatwo budować aplikacje generatywnej AI przy ograniczonej mocy obliczeniowej.

Wykonaj te kroki, aby rozpocząć korzystanie z tych zasobów:
1. **Forkuj repozytorium**: Kliknij [![Forki GitHub](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **Sklonuj repozytorium**: `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Dołącz do społeczności Microsoft AI na Discord i poznaj ekspertów oraz innych deweloperów**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/pl/cover.eb18d1b9605d754b.webp)

### 🌐 Wielojęzyczne wsparcie

#### Obsługiwane przez GitHub Action (automatyczne i zawsze aktualne)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabski](../ar/README.md) | [Bengalski](../bn/README.md) | [Bułgarski](../bg/README.md) | [Birmański (Myanmar)](../my/README.md) | [Chiński (uproszczony)](../zh-CN/README.md) | [Chiński (tradycyjny, Hong Kong)](../zh-HK/README.md) | [Chiński (tradycyjny, Macau)](../zh-MO/README.md) | [Chiński (tradycyjny, Tajwan)](../zh-TW/README.md) | [Chorwacki](../hr/README.md) | [Czeski](../cs/README.md) | [Duński](../da/README.md) | [Niderlandzki](../nl/README.md) | [Estoński](../et/README.md) | [Fiński](../fi/README.md) | [Francuski](../fr/README.md) | [Niemiecki](../de/README.md) | [Grecki](../el/README.md) | [Hebrajski](../he/README.md) | [Hindi](../hi/README.md) | [Węgierski](../hu/README.md) | [Indonezyjski](../id/README.md) | [Włoski](../it/README.md) | [Japoński](../ja/README.md) | [Kannada](../kn/README.md) | [Koreański](../ko/README.md) | [Litewski](../lt/README.md) | [Malajski](../ms/README.md) | [Malajalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepalski](../ne/README.md) | [Nigeryjski pidgin](../pcm/README.md) | [Norweski](../no/README.md) | [Perski (Farsi)](../fa/README.md) | [Polski](./README.md) | [Portugalski (Brazylia)](../pt-BR/README.md) | [Portugalski (Portugalia)](../pt-PT/README.md) | [Pendżabski (Gurmukhi)](../pa/README.md) | [Rumuński](../ro/README.md) | [Rosyjski](../ru/README.md) | [Serbski (cyrylica)](../sr/README.md) | [Słowacki](../sk/README.md) | [Słoweński](../sl/README.md) | [Hiszpański](../es/README.md) | [Suahili](../sw/README.md) | [Szwedzki](../sv/README.md) | [Tagalog (filipiński)](../tl/README.md) | [Tamilski](../ta/README.md) | [Telugu](../te/README.md) | [Tajski](../th/README.md) | [Turecki](../tr/README.md) | [Ukraiński](../uk/README.md) | [Urdu](../ur/README.md) | [Wietnamski](../vi/README.md)

> **Wolisz klonować lokalnie?**
>
> To repozytorium zawiera ponad 50 tłumaczeń językowych, co znacznie zwiększa rozmiar pobierania. Aby klonować bez tłumaczeń, użyj sparse checkout:
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
> To zapewnia wszystko, co potrzebne do ukończenia kursu z znacznie szybszym pobieraniem.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## Spis treści

## Używanie modeli Phi

### Phi na Microsoft Foundry

Możesz nauczyć się jak używać Microsoft Phi oraz jak budować kompleksowe rozwiązania na różnych urządzeniach sprzętowych. Aby doświadczyć Phi na własnej skórze, zacznij od zabawy z modelami i dostosowywania Phi do swoich scenariuszy za pomocą [Microsoft Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai). Więcej informacji znajdziesz w przewodniku Pierwsze kroki z [Microsoft Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md)

**Plac zabaw**
Każdy model ma dedykowany plac zabaw do testowania modelu [Azure AI Playground](https://aka.ms/try-phi3).

### Phi na GitHub Models

Możesz nauczyć się jak używać Microsoft Phi i jak budować kompleksowe rozwiązania na różnych urządzeniach sprzętowych. Aby doświadczyć Phi na własnej skórze, zacznij zabawę z modelem i dostosuj Phi do swoich scenariuszy korzystając z [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo). Więcej informacji znajdziesz w przewodniku Pierwsze kroki z [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md)

**Plac zabaw**
Każdy model ma dedykowany [plac zabaw do testowania modelu](/md/02.QuickStart/GitHubModel_QuickStart.md).

### Phi na Hugging Face

Model możesz też znaleźć na [Hugging Face](https://huggingface.co/microsoft)

**Plac zabaw**
[Hugging Chat playground](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## 🎒 Inne kursy

Nasz zespół produkuje inne kursy! Sprawdź:

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

### Seria Generatywnej AI
[![Generatywna AI dla początkujących](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generatywna AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generative AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generative AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---

### Podstawowa nauka
[![ML for Beginners](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science for Beginners](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI for Beginners](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Cybersecurity for Beginners](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Web Dev for Beginners](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT for Beginners](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR Development for Beginners](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---

### Seria Copilot
[![Copilot for AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Odpowiedzialna AI

Microsoft angażuje się w pomaganie naszym klientom w odpowiedzialnym korzystaniu z naszych produktów AI, dzieląc się naszymi doświadczeniami i budując zaufanie poprzez narzędzia takie jak Notatki Przejrzystości i Oceny Wpływu. Wiele z tych zasobów można znaleźć na [https://aka.ms/RAI](https://aka.ms/RAI).
Podejście Microsoft do odpowiedzialnej AI opiera się na naszych zasadach AI dotyczących uczciwości, niezawodności i bezpieczeństwa, prywatności i bezpieczeństwa, inkluzywności, przejrzystości oraz odpowiedzialności.

Modele na dużą skalę do przetwarzania języka naturalnego, obrazów i mowy — takie jak te użyte w tym przykładzie — mogą potencjalnie zachowywać się w sposób nieuczciwy, zawodny lub obraźliwy, powodując szkody. Prosimy zapoznać się z [Notatką Przejrzystości usługi Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text), aby być poinformowanym o ryzykach i ograniczeniach.

Zalecanym podejściem do łagodzenia tych ryzyk jest włączenie do architektury systemu bezpieczeństwa, który może wykrywać i zapobiegać szkodliwym zachowaniom. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) zapewnia niezależną warstwę ochrony, zdolną do wykrywania szkodliwych treści generowanych przez użytkownika oraz AI w aplikacjach i usługach. Azure AI Content Safety obejmuje API tekstowe i obrazkowe, które pozwalają na wykrywanie materiałów szkodliwych. W ramach Microsoft Foundry usługa Content Safety pozwala na przeglądanie, eksplorowanie i wypróbowanie przykładowego kodu do wykrywania szkodliwych treści w różnych modalnościach. Następująca [dokumentacja szybkiego startu](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) prowadzi przez proces wykonywania zapytań do usługi.

Innym aspektem do rozważenia jest ogólna wydajność aplikacji. W aplikacjach wielomodalnych i wykorzystujących wiele modeli wydajność oznacza, że system działa zgodnie z oczekiwaniami Twoimi i użytkowników, w tym nie generuje szkodliwych wyników. Ważne jest, aby ocenić wydajność całej aplikacji, korzystając z [ocen wydajności, jakości i ryzyka oraz bezpieczeństwa](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in). Masz również możliwość tworzenia i oceny z użyciem [własnych oceniających](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators).

Możesz ocenić swoją aplikację AI w środowisku programistycznym, korzystając z [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html). Przy użyciu zestawu testowego lub celu generacje Twojej aplikacji AI generatywnej są ilościowo mierzone za pomocą wbudowanych lub własnych oceniających. Aby rozpocząć pracę z azure ai evaluation sdk do oceny swojego systemu, możesz postępować zgodnie z [przewodnikiem szybkiego startu](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Po wykonaniu oceny możesz [wizualizować wyniki w Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Znaki towarowe

Ten projekt może zawierać znaki towarowe lub logotypy projektów, produktów lub usług. Autoryzowane użycie znaków towarowych lub logo Microsoft podlega i musi przestrzegać [Zasad dotyczących znaków towarowych i marki Microsoft](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).
Użycie znaków towarowych lub logo Microsoft w zmodyfikowanych wersjach tego projektu nie może powodować zamieszania ani sugerować sponsorowania przez Microsoft. Wszelkie użycie znaków towarowych lub logotypów stron trzecich podlega politykom tych stron.

## Uzyskanie pomocy

Jeśli utkniesz lub masz pytania dotyczące tworzenia aplikacji AI, dołącz do:

[![Microsoft Foundry Discord](https://img.shields.io/badge/Discord-Microsoft_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

Jeśli masz uwagi dotyczące produktu lub napotkasz błędy podczas tworzenia, odwiedź:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczeń AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym należy traktować jako źródło wiarygodne. W przypadku istotnych informacji zaleca się skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->