# Phi Cookbook: Microsoft의 Phi 모델을 활용한 실습 예제

[![GitHub Codespaces에서 샘플 열기 및 사용](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Dev Containers에서 열기](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub 기여자](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub 이슈](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub 풀 리퀘스트](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PR 환영](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub 감시자](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub 포크](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub 스타](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi는 Microsoft가 개발한 일련의 오픈 소스 AI 모델입니다.

Phi는 현재 매우 뛰어난 다국어, 추론, 텍스트/채팅 생성, 코딩, 이미지, 오디오 및 기타 시나리오에서 매우 우수한 벤치마크를 가진 가장 강력하고 비용 효율적인 소형 언어 모델(SLM)입니다.

Phi는 클라우드 또는 엣지 디바이스에 배포할 수 있으며, 제한된 컴퓨팅 파워로도 쉽게 생성형 AI 애플리케이션을 구축할 수 있습니다.

다음 단계를 따라 이 리소스 사용을 시작하세요:
1. **리포지토리 포크하기**: 클릭 [![GitHub 포크](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **리포지토리 클론하기**: `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Microsoft AI Discord 커뮤니티에 참여하여 전문가 및 개발자와 만나요**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/ko/cover.eb18d1b9605d754b.webp)

### 🌐 다국어 지원

#### GitHub 액션을 통해 지원 (자동화 & 항상 최신 상태)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Korean](./README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **로컬로 클론하기를 선호하시나요?**

> 이 리포지토리는 50개 이상의 언어 번역을 포함하고 있어 다운로드 크기가 상당히 커집니다. 번역 없이 클론하려면 sparse checkout을 사용하세요:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/PhiCookBook.git
> cd PhiCookBook
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> 이 방법은 훨씬 빠른 다운로드로 과정을 완료하는 데 필요한 모든 것을 제공합니다.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## 목차

- 소개
  - [Phi 가족에 오신 것을 환영합니다](./md/01.Introduction/01/01.PhiFamily.md)
  - [환경 설정](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [핵심 기술 이해하기](./md/01.Introduction/01/01.Understandingtech.md)
  - [Phi 모델을 위한 AI 안전성](./md/01.Introduction/01/01.AISafety.md)
  - [Phi 하드웨어 지원](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Phi 모델 및 플랫폼 별 가용성](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Guidance-ai 및 Phi 사용법](./md/01.Introduction/01/01.Guidance.md)
  - [GitHub 마켓플레이스 모델](https://github.com/marketplace/models)
  - [Azure AI 모델 카탈로그](https://ai.azure.com)

- 다양한 환경에서 Phi 추론
    -  [Hugging face](./md/01.Introduction/02/01.HF.md)
    -  [GitHub 모델](./md/01.Introduction/02/02.GitHubModel.md)
    -  [Azure AI Foundry 모델 카탈로그](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    -  [Foundry 로컬](./md/01.Introduction/02/07.FoundryLocal.md)

- Phi 가족 추론
    - [iOS에서 Phi 추론](./md/01.Introduction/03/iOS_Inference.md)
    - [Android에서 Phi 추론](./md/01.Introduction/03/Android_Inference.md)
    - [Jetson에서 Phi 추론](./md/01.Introduction/03/Jetson_Inference.md)
    - [AI PC에서 Phi 추론](./md/01.Introduction/03/AIPC_Inference.md)
    - [Apple MLX 프레임워크로 Phi 추론](./md/01.Introduction/03/MLX_Inference.md)
    - [로컬 서버에서 Phi 추론](./md/01.Introduction/03/Local_Server_Inference.md)
    - [AI Toolkit을 사용한 원격 서버에서 Phi 추론](./md/01.Introduction/03/Remote_Interence.md)
    - [Rust와 함께하는 Phi 추론](./md/01.Introduction/03/Rust_Inference.md)
    - [로컬에서 Phi-비전 추론](./md/01.Introduction/03/Vision_Inference.md)
    - [Kaito AKS, Azure 컨테이너(공식 지원)와 함께하는 Phi 추론](./md/01.Introduction/03/Kaito_Inference.md)
-  [Phi 가족 양자화](./md/01.Introduction/04/QuantifyingPhi.md)
    - [llama.cpp를 사용한 Phi-3.5 / 4 양자화](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [onnxruntime용 생성 AI 확장으로 Phi-3.5 / 4 양자화](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Intel OpenVINO를 사용한 Phi-3.5 / 4 양자화](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Apple MLX 프레임워크를 사용한 Phi-3.5 / 4 양자화](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

- Phi 평가
    - [책임 있는 AI](./md/01.Introduction/05/ResponsibleAI.md)
    - [평가를 위한 Azure AI Foundry](./md/01.Introduction/05/AIFoundry.md)
    - [평가를 위한 Promptflow 사용](./md/01.Introduction/05/Promptflow.md)
 
- Azure AI Search와 RAG
    - [Azure AI Search와 함께하는 Phi-4-mini 및 Phi-4-multimodal(RAG) 사용법](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Phi 애플리케이션 개발 샘플
  - 텍스트 및 채팅 애플리케이션
    - Phi-4 샘플 🆕
      - [📓] [Phi-4-mini ONNX 모델과 채팅하기](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Phi-4 로컬 ONNX 모델 .NET과 채팅](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Sementic Kernel 사용한 Phi-4 ONNX .NET 콘솔 앱 채팅](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Phi-3 / 3.5 샘플
      - [브라우저 내에서 Phi3, ONNX Runtime Web 및 WebGPU를 이용한 로컬 챗봇](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVino 채팅](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [멀티 모델 - 인터랙티브 Phi-3-mini 및 OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - 래퍼 빌드 및 MLFlow와 함께 Phi-3 사용](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [모델 최적화 - Olive를 사용하여 ONNX Runtime Web용 Phi-3-min 모델 최적화 방법](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [Phi-3 mini-4k-instruct-onnx를 사용하는 WinUI3 앱](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      -[WinUI3 멀티 모델 AI 기반 노트 앱 샘플](https://github.com/microsoft/ai-powered-notes-winui3-sample)
      - [Prompt flow를 통한 맞춤형 Phi-3 모델의 미세 조정 및 통합](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
      - [Azure AI Foundry에서 Prompt flow로 맞춤형 Phi-3 모델 미세 조정 및 통합](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
      - [Microsoft의 책임 있는 AI 원칙에 초점을 맞춘 Azure AI Foundry에서 미세 조정된 Phi-3 / Phi-3.5 모델 평가](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
      - [📓] [Phi-3.5-mini-instruct 언어 예측 샘플 (중국어/영어)](./md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
      - [Phi-3.5-Instruct WebGPU RAG 챗봇](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
      - [Phi-3.5-Instruct ONNX와 함께 Windows GPU를 사용하여 Prompt flow 솔루션 생성](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
      - [Microsoft Phi-3.5 tflite를 사용하여 Android 앱 만들기](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
      - [Microsoft.ML.OnnxRuntime를 사용하여 로컬 ONNX Phi-3 모델을 사용하는 Q&A .NET 예제](../../md/04.HOL/dotnet/src/LabsPhi301)
      - [Semantic Kernel 및 Phi-3와 함께하는 콘솔 채팅 .NET 앱](../../md/04.HOL/dotnet/src/LabsPhi302)

  - Azure AI 추론 SDK 코드 기반 샘플
    - Phi-4 샘플 🆕
      - [📓] [Phi-4-multimodal을 사용한 프로젝트 코드 생성](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
    - Phi-3 / 3.5 샘플
      - [Microsoft Phi-3 패밀리와 함께 Visual Studio Code GitHub Copilot Chat 구축](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
      - [GitHub 모델과 함께 Phi-3.5로 Visual Studio Code Chat Copilot 에이전트 구축](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

  - 고급 추론 샘플
    - Phi-4 샘플 🆕
      - [📓] [Phi-4-mini-reasoning 또는 Phi-4-reasoning 샘플](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
      - [📓] [Microsoft Olive로 Phi-4-mini-reasoning 미세 조정](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Apple MLX로 Phi-4-mini-reasoning 미세 조정](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [GitHub 모델들과 함께하는 Phi-4-mini-reasoning](./md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
      - [📓] [Azure AI Foundry 모델들과 함께하는 Phi-4-mini-reasoning](./md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
  - 데모
      - [Hugging Face Spaces에서 호스팅되는 Phi-4-mini 데모](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
      - [Hugging Face Spaces에서 호스팅되는 Phi-4-multimodal 데모](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
  - 비전 샘플
    - Phi-4 샘플 🆕
      - [📓] [Phi-4-multimodal을 사용한 이미지 읽기 및 코드 생성](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md)
    - Phi-3 / 3.5 샘플
      -  [📓][Phi-3-비전-이미지 텍스트 변환](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [Phi-3-비전-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
      - [📓][Phi-3-비전 CLIP 임베딩](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [데모: Phi-3 재활용](https://github.com/jennifermarsman/PhiRecycling/)
      - [Phi-3-비전 - Phi3-Vision 및 OpenVINO와 함께하는 시각 언어 어시스턴트](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
      - [Phi-3 비전 Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
      - [Phi-3 비전 OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
      - [📓][Phi-3.5 비전 다중 프레임 또는 다중 이미지 샘플](./md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
      - [Microsoft.ML.OnnxRuntime .NET을 사용하는 Phi-3 비전 로컬 ONNX 모델](../../md/04.HOL/dotnet/src/LabsPhi303)
      - [메뉴 기반 Phi-3 비전 로컬 ONNX 모델 Microsoft.ML.OnnxRuntime .NET 사용](../../md/04.HOL/dotnet/src/LabsPhi304)

  - 수학 샘플
    - Phi-4-Mini-Flash-Reasoning-Instruct 샘플 🆕 [Phi-4-Mini-Flash-Reasoning-Instruct를 이용한 수학 데모](./md/02.Application/09.Math/MathDemo.ipynb)

  - 오디오 샘플
    - Phi-4 샘플 🆕
      - [📓] [Phi-4-multimodal을 사용한 오디오 대본 추출](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
      - [📓] [Phi-4-multimodal 오디오 샘플](./md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
      - [📓] [Phi-4-multimodal 음성 번역 샘플](./md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
      - [.NET 콘솔 애플리케이션으로 Phi-4-multimodal 오디오를 사용하여 오디오 파일 분석 및 대본 생성](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

  - MOE 샘플
    - Phi-3 / 3.5 샘플
      - [📓] [Phi-3.5 전문가 혼합 모델(MoEs) 소셜 미디어 샘플](./md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
      - [📓] [NVIDIA NIM Phi-3 MOE, Azure AI Search, LlamaIndex를 사용한 검색 보강 생성(RAG) 파이프라인 구축](./md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)
      - 
  - 함수 호출 샘플
    - Phi-4 샘플 🆕
      -  [📓] [Phi-4-mini와 함께 함수 호출 사용](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
      -  [📓] [Phi-4-mini와 함께 다중 에이전트 생성에 함수 호출 사용](./md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
      -  [📓] [Ollama와 함께 함수 호출 사용](./md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
      -  [📓] [ONNX와 함께 함수 호출 사용](./md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)
  - 멀티모달 믹싱 샘플
    - Phi-4 샘플 🆕
      -  [📓] [Phi-4-multimodal을 기술 저널리스트로 활용](./md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
      - [.NET 콘솔 애플리케이션에서 Phi-4-multimodal을 사용하여 이미지 분석](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Phi 미세 조정 샘플
  - [미세 조정 시나리오](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [미세 조정과 RAG 비교](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [Phi-3를 산업 전문가로 만드는 미세 조정](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [VS Code AI Toolkit을 사용한 Phi-3 미세 조정](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Azure Machine Learning Service를 사용한 Phi-3 미세 조정](./md/03.FineTuning/Introduce_AzureML.md)
  - [Lora를 사용한 Phi-3 미세 조정](./md/03.FineTuning/FineTuning_Lora.md)
  - [QLora를 사용한 Phi-3 미세 조정](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Azure AI Foundry에서 Phi-3 미세 조정](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Azure ML CLI/SDK를 사용한 Phi-3 미세 조정](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Microsoft Olive를 사용한 미세 조정](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Microsoft Olive 핸즈온 랩을 통한 미세 조정](./md/03.FineTuning/olive-lab/readme.md)
  - [Weights and Bias를 사용한 Phi-3-vision 미세 조정](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [Apple MLX 프레임워크를 사용한 Phi-3 미세 조정](./md/03.FineTuning/FineTuning_MLX.md)
  - [Phi-3-vision 공식 지원 미세 조정](./md/03.FineTuning/FineTuning_Vision.md)
  - [Kaito AKS, Azure 컨테이너(공식 지원)를 사용한 Phi-3 미세 조정](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Phi-3 및 3.5 비전 미세 조정](https://github.com/2U1/Phi3-Vision-Finetune)

- 핸즈온 랩
  - [최첨단 모델 탐색: LLM, SLM, 로컬 개발 등](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [NLP 잠재력 개방: Microsoft Olive를 이용한 미세 조정](https://github.com/azure/Ignite_FineTuning_workshop)

- 학술 연구 논문 및 출판물
  - [Textbooks Are All You Need II: phi-1.5 technical report](https://arxiv.org/abs/2309.05463)
  - [Phi-3 Technical Report: A Highly Capable Language Model Locally on Your Phone](https://arxiv.org/abs/2404.14219)
  - [Phi-4 Technical Report](https://arxiv.org/abs/2412.08905)
  - [Phi-4-Mini Technical Report: Compact yet Powerful Multimodal Language Models via Mixture-of-LoRAs](https://arxiv.org/abs/2503.01743)
  - [Optimizing Small Language Models for In-Vehicle Function-Calling](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) Fine-Tuning PHI-3 for Multiple-Choice Question Answering: Methodology, Results, and Challenges](https://arxiv.org/abs/2501.01588)
  - [Phi-4-reasoning Technical Report](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Phi-4-mini-reasoning Technical Report](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Phi 모델 사용하기

### Azure AI Foundry에서 Phi

Microsoft Phi를 사용하는 방법과 다양한 하드웨어 장치에서 E2E 솔루션을 구축하는 방법을 배울 수 있습니다. 직접 Phi를 경험하려면 모델을 사용해보고, [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai)를 이용해 시나리오에 맞게 Phi를 커스터마이징해 보세요. 시작에 대한 자세한 내용은 [Azure AI Foundry 시작하기](/md/02.QuickStart/AzureAIFoundry_QuickStart.md)에서 확인할 수 있습니다.

**Playground**  
각 모델마다 모델을 테스트할 수 있는 전용 PlayGround가 있습니다 [Azure AI Playground](https://aka.ms/try-phi3).

### GitHub Models에서 Phi

Microsoft Phi를 사용하는 방법과 다양한 하드웨어 장치에서 E2E 솔루션을 구축하는 방법을 배울 수 있습니다. 직접 Phi를 경험하려면 모델을 사용해 보고, [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo)를 이용해 시나리오에 맞게 Phi를 커스터마이징해 보세요. 시작에 대한 자세한 내용은 [GitHub Model Catalog 시작하기](/md/02.QuickStart/GitHubModel_QuickStart.md)에서 확인할 수 있습니다.

**Playground**  
각 모델마다 모델을 테스트할 수 있는 전용 [Playground](/md/02.QuickStart/GitHubModel_QuickStart.md)가 있습니다.

### Hugging Face에서 Phi

모델을 [Hugging Face](https://huggingface.co/microsoft)에서도 찾을 수 있습니다.

**Playground**  
[Hugging Chat playground](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## 🎒 기타 강좌

우리 팀은 다른 강좌도 제작합니다! 확인해보세요:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j for Beginners](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js for Beginners](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

---

### Azure / Edge / MCP / Agents
[![AZD for Beginners](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI for Beginners](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP for Beginners](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Agents for Beginners](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### 생성 AI 시리즈
[![Generative AI for Beginners](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generative AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generative AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generative AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### 핵심 학습
[![ML for Beginners](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science for Beginners](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI for Beginners](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Cybersecurity for Beginners](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Web Dev for Beginners](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT for Beginners](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR Development for Beginners](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot 시리즈
[![Copilot for AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## 책임 있는 AI

Microsoft는 고객이 AI 제품을 책임감 있게 사용하도록 돕고, 학습 내용을 공유하며, 투명성 노트와 영향 평가와 같은 도구를 통해 신뢰 기반 파트너십을 구축하는 데 최선을 다하고 있습니다. 이러한 자원 중 많은 부분은 [https://aka.ms/RAI](https://aka.ms/RAI)에서 찾을 수 있습니다.  
Microsoft의 책임 있는 AI 접근법은 공정성, 신뢰성 및 안전성, 개인정보 보호 및 보안, 포용성, 투명성 및 책임성이라는 AI 원칙에 기반하고 있습니다.

이 샘플에 사용된 대규모 자연어, 이미지, 음성 모델들은 불공정하거나 신뢰할 수 없거나 불쾌감을 줄 수 있는 방식으로 동작할 수 있어 피해를 초래할 수 있습니다. 위험과 한계에 대해 정보를 제공하는 [Azure OpenAI 서비스 투명성 노트](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text)를 참고하세요.

이러한 위험을 완화하기 위한 권장 방법은 아키텍처에 해로운 행동을 감지하고 방지할 수 있는 안전 시스템을 포함하는 것입니다. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview)는 애플리케이션과 서비스에서 해로운 사용자 생성 및 AI 생성 콘텐츠를 감지할 수 있는 독립적인 보호 계층을 제공합니다. Azure AI Content Safety는 해로운 자료를 탐지할 수 있는 텍스트 및 이미지 API를 포함합니다. Azure AI Foundry 내에서는 Content Safety 서비스가 다양한 형태의 해로운 콘텐츠를 탐지하는 데 사용할 수 있는 샘플 코드 조회, 탐색, 실험 기능을 제공합니다. 다음의 [퀵스타트 문서](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest)는 서비스 요청 방법을 안내합니다.

또 다른 고려 사항은 전체 애플리케이션 성능입니다. 멀티모달 및 멀티모델 애플리케이션의 경우, 시스템이 사용자와 여러분의 기대대로 동작하는 것으로 여기며, 여기에는 해로운 출력물이 생성되지 않는 것도 포함됩니다. [성능 및 품질, 위험 및 안전 평가기](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in)를 사용하여 전체 애플리케이션 성능을 평가하는 것이 중요합니다. 또한 [사용자 정의 평가기](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators)를 만들어 평가할 수도 있습니다.
개발 환경에서 [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html)를 사용하여 AI 애플리케이션을 평가할 수 있습니다. 테스트 데이터 세트 또는 대상이 주어지면 생성 AI 애플리케이션의 생성 결과를 내장 평가자 또는 원하는 맞춤 평가자로 정량적으로 측정합니다. 시스템 평가를 위해 azure ai evaluation sdk를 시작하려면 [빠른 시작 가이드](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk)를 참고하세요. 평가 실행을 완료하면 [Azure AI Foundry에서 결과를 시각화](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results)할 수 있습니다.

## Trademarks

이 프로젝트에는 프로젝트, 제품 또는 서비스의 상표나 로고가 포함될 수 있습니다. Microsoft 상표 또는 로고의 사용 권한은 [Microsoft 상표 및 브랜드 가이드라인](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general)에 따르고 이를 준수해야 합니다.
이 프로젝트의 수정된 버전에서 Microsoft 상표 또는 로고를 사용하는 경우 혼동을 일으키거나 Microsoft 후원을 암시해서는 안 됩니다. 제3자 상표 또는 로고 사용은 해당 제3자의 정책을 준수해야 합니다.

## Getting Help

AI 앱 빌드 작업 중 문제가 있거나 질문이 있을 경우 다음에 참여하세요:

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

제품 피드백이나 빌드 중 오류가 있을 경우 방문하세요:

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있으나, 자동 번역에는 오류나 부정확성이 있을 수 있으니 유의해 주시기 바랍니다. 원문 문서는 해당 언어의 공식 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문 인력에 의한 번역을 권장합니다. 본 번역 사용으로 인한 오해나 오독에 대해서는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->