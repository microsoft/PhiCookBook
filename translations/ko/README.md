<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8f2577190cbe70305b9de13df37e1c9a",
  "translation_date": "2025-04-04T05:18:09+00:00",
  "source_file": "README.md",
  "language_code": "ko"
}
-->
# Phi Cookbook: Microsoft의 Phi 모델 실습 예제

[![GitHub Codespaces에서 샘플 열기 및 사용](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Dev Containers에서 열기](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub 기여자](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub 이슈](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub 풀 리퀘스트](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PR 환영](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub 감시자](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub 포크](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub 스타](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Azure AI 커뮤니티 Discord](https://dcbadge.vercel.app/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

Phi는 Microsoft에서 개발한 오픈 소스 AI 모델 시리즈입니다.

Phi는 현재 가장 강력하고 비용 효율적인 소형 언어 모델(SLM)로, 다국어, 추론, 텍스트/채팅 생성, 코딩, 이미지, 오디오 및 기타 시나리오에서 매우 우수한 벤치마크를 제공합니다.

Phi를 클라우드 또는 엣지 디바이스에 배포할 수 있으며, 제한된 컴퓨팅 자원으로 생성형 AI 애플리케이션을 쉽게 구축할 수 있습니다.

이 리소스를 사용하려면 다음 단계를 따라 진행하세요:
1. **저장소 포크하기**: 클릭 [![GitHub 포크](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **저장소 클론하기**: `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Microsoft AI Discord 커뮤니티에 가입하여 전문가와 개발자를 만나보세요**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![커버 이미지](../../translated_images/cover.2595d43b382944c601aebf88583314636768eece3d94e8e4448e03a4e5bedef4.ko.png)

## 🌐 다국어 지원
[프랑스어](../fr/README.md) | [스페인어](../es/README.md) | [독일어](../de/README.md) | [러시아어](../ru/README.md) | [아랍어](../ar/README.md) | [페르시아어 (파르시)](../fa/README.md) | [우르두어](../ur/README.md) | [중국어 (간체)](../zh/README.md) | [중국어 (번체, 마카오)](../mo/README.md) | [중국어 (번체, 홍콩)](../hk/README.md) | [중국어 (번체, 대만)](../tw/README.md) | [일본어](../ja/README.md) | [한국어](./README.md) | [힌디어](../hi/README.md) | [벵골어](../bn/README.md) | [마라티어](../mr/README.md) | [네팔어](../ne/README.md) | [펀자브어 (구르무키)](../pa/README.md) | [포르투갈어 (포르투갈)](../pt/README.md) | [포르투갈어 (브라질)](../br/README.md) | [이탈리아어](../it/README.md) | [폴란드어](../pl/README.md) | [터키어](../tr/README.md) | [그리스어](../el/README.md) | [태국어](../th/README.md) | [스웨덴어](../sv/README.md) | [덴마크어](../da/README.md) | [노르웨이어](../no/README.md) | [핀란드어](../fi/README.md) | [네덜란드어](../nl/README.md) | [히브리어](../he/README.md) | [베트남어](../vi/README.md) | [인도네시아어](../id/README.md) | [말레이어](../ms/README.md) | [타갈로그어 (필리핀어)](../tl/README.md) | [스와힐리어](../sw/README.md) | [헝가리어](../hu/README.md) | [체코어](../cs/README.md) | [슬로바키아어](../sk/README.md) | [루마니아어](../ro/README.md) | [불가리아어](../bg/README.md) | [세르비아어 (키릴문자)](../sr/README.md) | [크로아티아어](../hr/README.md) | [슬로베니아어](../sl/README.md)
## 목차

- 소개
  - [Phi 패밀리에 오신 것을 환영합니다](./md/01.Introduction/01/01.PhiFamily.md)
  - [환경 설정하기](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [핵심 기술 이해하기](./md/01.Introduction/01/01.Understandingtech.md)
  - [Phi 모델을 위한 AI 안전성](./md/01.Introduction/01/01.AISafety.md)
  - [Phi 하드웨어 지원](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Phi 모델 및 플랫폼별 가용성](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Guidance-ai와 Phi 사용하기](./md/01.Introduction/01/01.Guidance.md)
  - [GitHub 마켓플레이스 모델](https://github.com/marketplace/models)
  - [Azure AI 모델 카탈로그](https://ai.azure.com)

- 다양한 환경에서 Phi 추론하기
    - [Hugging face](./md/01.Introduction/02/01.HF.md)
    - [GitHub 모델](./md/01.Introduction/02/02.GitHubModel.md)
    - [Azure AI Foundry 모델 카탈로그](./md/01.Introduction/02/03.AzureAIFoundry.md)
    - [Ollama](./md/01.Introduction/02/04.Ollama.md)
    - [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    - [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)

- Phi 패밀리 추론
    - [iOS에서 Phi 추론하기](./md/01.Introduction/03/iOS_Inference.md)
    - [Android에서 Phi 추론하기](./md/01.Introduction/03/Android_Inference.md)
    - [Jetson에서 Phi 추론하기](./md/01.Introduction/03/Jetson_Inference.md)
    - [AI PC에서 Phi 추론하기](./md/01.Introduction/03/AIPC_Inference.md)
    - [Apple MLX 프레임워크로 Phi 추론하기](./md/01.Introduction/03/MLX_Inference.md)
    - [로컬 서버에서 Phi 추론하기](./md/01.Introduction/03/Local_Server_Inference.md)
    - [AI Toolkit을 사용하여 원격 서버에서 Phi 추론하기](./md/01.Introduction/03/Remote_Interence.md)
    - [Rust로 Phi 추론하기](./md/01.Introduction/03/Rust_Inference.md)
    - [로컬에서 Phi--Vision 추론하기](./md/01.Introduction/03/Vision_Inference.md)
    - [Kaito AKS, Azure Containers(공식 지원)을 사용하여 Phi 추론하기](./md/01.Introduction/03/Kaito_Inference.md)

- [Phi 패밀리 양자화](./md/01.Introduction/04/QuantifyingPhi.md)
    - [llama.cpp를 사용하여 Phi-3.5 / 4 양자화하기](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [onnxruntime의 생성 AI 확장을 사용하여 Phi-3.5 / 4 양자화하기](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Intel OpenVINO를 사용하여 Phi-3.5 / 4 양자화하기](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Apple MLX 프레임워크를 사용하여 Phi-3.5 / 4 양자화하기](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

- Phi 평가
- [책임 있는 AI](./md/01.Introduction/05/ResponsibleAI.md)  
    - [평가를 위한 Azure AI Foundry](./md/01.Introduction/05/AIFoundry.md)  
    - [평가를 위한 Promptflow 사용](./md/01.Introduction/05/Promptflow.md)  

- Azure AI Search와 RAG  
    - [Phi-4-mini 및 Phi-4-multimodal(RAG)을 Azure AI Search와 함께 사용하는 방법](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)  

- Phi 애플리케이션 개발 샘플  
  - 텍스트 및 채팅 애플리케이션  
    - Phi-4 샘플 🆕  
      - [📓] [Phi-4-mini ONNX 모델로 채팅하기](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)  
      - [Phi-4 로컬 ONNX 모델 .NET으로 채팅하기](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)  
      - [Semantic Kernel을 사용한 Phi-4 ONNX .NET 콘솔 앱 채팅](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)  
    - Phi-3 / 3.5 샘플  
      - [Phi3, ONNX Runtime Web 및 WebGPU를 사용하여 브라우저에서 로컬 챗봇 실행](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)  
      - [OpenVino 채팅](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)  
      - [다중 모델 - Phi-3-mini 및 OpenAI Whisper와의 상호작용](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)  
      - [MLFlow - 래퍼 구축 및 MLFlow와 함께 Phi-3 사용](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)  
      - [모델 최적화 - Olive를 사용하여 ONNX Runtime Web용 Phi-3-min 모델 최적화 방법](https://github.com/microsoft/Olive/tree/main/examples/phi3)  
      - [Phi-3 mini-4k-instruct-onnx와 함께 WinUI3 앱 제작](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)  
      - [WinUI3 다중 모델 AI 기반 노트 앱 샘플](https://github.com/microsoft/ai-powered-notes-winui3-sample)  
      - [Prompt flow를 사용하여 맞춤형 Phi-3 모델을 미세 조정 및 통합](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)  
      - [Azure AI Foundry에서 Prompt flow를 사용하여 맞춤형 Phi-3 모델을 미세 조정 및 통합](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)  
      - [Microsoft의 책임 있는 AI 원칙을 중심으로 Azure AI Foundry에서 미세 조정된 Phi-3 / Phi-3.5 모델 평가](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)  
      - [📓] [Phi-3.5-mini-instruct 언어 예측 샘플 (중국어/영어)](../../md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)  
      - [Phi-3.5-Instruct WebGPU RAG 챗봇](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)  
      - [Windows GPU를 사용하여 Phi-3.5-Instruct ONNX와 함께 Prompt flow 솔루션 생성](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)  
      - [Microsoft Phi-3.5 tflite를 사용하여 Android 앱 생성](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)  
      - [Microsoft.ML.OnnxRuntime을 사용하여 로컬 ONNX Phi-3 모델로 Q&A .NET 예제](../../md/04.HOL/dotnet/src/LabsPhi301)  
      - [Semantic Kernel과 Phi-3를 사용한 .NET 콘솔 채팅 앱](../../md/04.HOL/dotnet/src/LabsPhi302)  

  - Azure AI Inference SDK 코드 기반 샘플  
    - Phi-4 샘플 🆕  
      - [📓] [Phi-4-multimodal을 사용하여 프로젝트 코드 생성](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)  
    - Phi-3 / 3.5 샘플  
      - [Microsoft Phi-3 패밀리를 사용하여 나만의 Visual Studio Code GitHub Copilot Chat 빌드](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)  
      - [GitHub 모델로 Phi-3.5를 사용하여 Visual Studio Code Chat Copilot 에이전트 생성](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)  

  - 고급 추론 샘플  
    - Phi-4 샘플 🆕  
      - [📓] [Phi-4-mini 추론 샘플](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)  

  - 데모  
      - [Hugging Face Spaces에서 호스팅되는 Phi-4-mini 데모](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)  
      - [Hugging Face Spaces에서 호스팅되는 Phi-4-multimodal 데모](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)  

  - 비전 샘플  
    - Phi-4 샘플 🆕  
      - [📓] [Phi-4-multimodal을 사용하여 이미지 읽기 및 코드 생성](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md)  
    - Phi-3 / 3.5 샘플  
- [📓][Phi-3-vision-Image text to text](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
      - [📓][Phi-3-vision CLIP Embedding](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [DEMO: Phi-3 Recycling](https://github.com/jennifermarsman/PhiRecycling/)
      - [Phi-3-vision - 시각적 언어 어시스턴트 - Phi3-Vision과 OpenVINO 활용](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
      - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
      - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
      - [📓][Phi-3.5 Vision 다중 프레임 또는 다중 이미지 샘플](../../md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
      - [Phi-3 Vision Microsoft.ML.OnnxRuntime .NET을 활용한 로컬 ONNX 모델](../../md/04.HOL/dotnet/src/LabsPhi303)
      - [Microsoft.ML.OnnxRuntime .NET을 활용한 메뉴 기반 Phi-3 Vision 로컬 ONNX 모델](../../md/04.HOL/dotnet/src/LabsPhi304)

  - 오디오 샘플
    - Phi-4 샘플 🆕
      - [📓] [Phi-4-multimodal을 활용한 오디오 텍스트 추출](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
      - [📓] [Phi-4-multimodal 오디오 샘플](../../md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
      - [📓] [Phi-4-multimodal 음성 번역 샘플](../../md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
      - [.NET 콘솔 애플리케이션을 활용하여 Phi-4-multimodal 오디오 파일 분석 및 텍스트 생성](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

  - MOE 샘플
    - Phi-3 / 3.5 샘플
      - [📓] [Phi-3.5 Mixture of Experts Models (MoEs) 소셜 미디어 샘플](../../md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
      - [📓] [NVIDIA NIM Phi-3 MOE, Azure AI Search, 및 LlamaIndex를 활용한 Retrieval-Augmented Generation (RAG) 파이프라인 구축](../../md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)
  - 함수 호출 샘플
    - Phi-4 샘플 🆕
      - [📓] [Phi-4-mini를 활용한 함수 호출 사용](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
      - [📓] [Phi-4-mini를 활용한 다중 에이전트 생성 함수 호출 사용](../../md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
      - [📓] [Ollama를 활용한 함수 호출 사용](../../md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
  - 멀티모달 믹싱 샘플
    - Phi-4 샘플 🆕
      - [📓] [Phi-4-multimodal을 활용하여 기술 저널리스트로 활동](../../md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
      - [.NET 콘솔 애플리케이션을 활용하여 Phi-4-multimodal로 이미지 분석](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Phi 샘플 세부 조정
  - [세부 조정 시나리오](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [세부 조정 vs RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [Phi-3를 산업 전문가로 만들기 위한 세부 조정](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [VS Code용 AI Toolkit을 활용한 Phi-3 세부 조정](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Azure Machine Learning Service를 활용한 Phi-3 세부 조정](./md/03.FineTuning/Introduce_AzureML.md)
  - [Lora를 활용한 Phi-3 세부 조정](./md/03.FineTuning/FineTuning_Lora.md)
  - [QLora를 활용한 Phi-3 세부 조정](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Azure AI Foundry를 활용한 Phi-3 세부 조정](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Azure ML CLI/SDK를 활용한 Phi-3 세부 조정](./md/03.FineTuning/FineTuning_MLSDK.md)
- [Microsoft Olive을 활용한 파인튜닝](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Microsoft Olive 핸즈온 랩을 활용한 파인튜닝](./md/03.FineTuning/olive-lab/readme.md)
  - [Weights and Bias를 활용한 Phi-3-vision 파인튜닝](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [Apple MLX Framework을 활용한 Phi-3 파인튜닝](./md/03.FineTuning/FineTuning_MLX.md)
  - [Phi-3-vision 파인튜닝 (공식 지원)](./md/03.FineTuning/FineTuning_Vision.md)
  - [Kaito AKS 및 Azure Containers를 활용한 Phi-3 파인튜닝 (공식 지원)](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Phi-3 및 3.5 Vision 파인튜닝](https://github.com/2U1/Phi3-Vision-Finetune)

- 핸즈온 랩
  - [최신 모델 탐색: LLMs, SLMs, 로컬 개발 및 기타](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [NLP 잠재력 해제: Microsoft Olive을 활용한 파인튜닝](https://github.com/azure/Ignite_FineTuning_workshop)

- 학술 연구 논문 및 출판물
  - [교과서만으로 충분하다 II: phi-1.5 기술 보고서](https://arxiv.org/abs/2309.05463)
  - [Phi-3 기술 보고서: 휴대폰에서 로컬로 실행 가능한 고성능 언어 모델](https://arxiv.org/abs/2404.14219)
  - [Phi-4 기술 보고서](https://arxiv.org/abs/2412.08905)
  - [Phi-4-Mini 기술 보고서: Mixture-of-LoRAs를 활용한 강력한 멀티모달 언어 모델](https://arxiv.org/abs/2503.01743)
  - [차량 내 기능 호출을 위한 소형 언어 모델 최적화](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) Phi-3의 선택형 질문 답변 파인튜닝: 방법론, 결과 및 도전 과제](https://arxiv.org/abs/2501.01588)

## Phi 모델 사용하기

### Azure AI Foundry에서 Phi

Microsoft Phi를 사용하는 방법과 다양한 하드웨어 장치에서 E2E 솔루션을 구축하는 방법을 배울 수 있습니다. Phi를 직접 경험하려면 모델을 테스트하고 사용자의 시나리오에 맞게 Phi를 커스터마이징해보세요. [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai)를 통해 시작할 수 있으며, [Azure AI Foundry 시작하기](/md/02.QuickStart/AzureAIFoundry_QuickStart.md)에서 자세히 알아볼 수 있습니다.

**Playground**  
각 모델은 전용 테스트 공간을 가지고 있습니다. [Azure AI Playground](https://aka.ms/try-phi3)를 확인해보세요.

### GitHub Models에서 Phi

Microsoft Phi를 사용하는 방법과 다양한 하드웨어 장치에서 E2E 솔루션을 구축하는 방법을 배울 수 있습니다. Phi를 직접 경험하려면 모델을 테스트하고 사용자의 시나리오에 맞게 Phi를 커스터마이징해보세요. [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo)를 통해 시작할 수 있으며, [GitHub Model Catalog 시작하기](/md/02.QuickStart/GitHubModel_QuickStart.md)에서 자세히 알아볼 수 있습니다.

**Playground**  
각 모델은 전용 [테스트 공간](/md/02.QuickStart/GitHubModel_QuickStart.md)을 가지고 있습니다.

### Hugging Face에서 Phi

모델은 [Hugging Face](https://huggingface.co/microsoft)에서도 확인할 수 있습니다.

**Playground**  
[Hugging Chat 테스트 공간](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)을 확인해보세요.

## 책임 있는 AI

Microsoft는 고객이 AI 제품을 책임감 있게 사용할 수 있도록 돕고, 학습 내용을 공유하며, 투명성 노트 및 영향 평가와 같은 도구를 통해 신뢰 기반의 파트너십을 구축하기 위해 노력하고 있습니다. 이러한 리소스는 [https://aka.ms/RAI](https://aka.ms/RAI)에서 확인할 수 있습니다.  
Microsoft의 책임 있는 AI 접근법은 공정성, 신뢰성 및 안전성, 프라이버시와 보안, 포용성, 투명성, 책임감이라는 AI 원칙에 기반을 두고 있습니다.

대규모 자연어, 이미지, 음성 모델은 불공정하거나 신뢰할 수 없거나 불쾌한 방식으로 작동할 가능성이 있으며, 이는 피해를 초래할 수 있습니다. 위험 및 제한 사항에 대해 알고 싶다면 [Azure OpenAI 서비스 투명성 노트](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text)를 참고하세요.

이러한 위험을 완화하기 위한 권장 접근법은 유해한 행동을 감지하고 방지할 수 있는 안전 시스템을 아키텍처에 포함하는 것입니다. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview)는 독립적인 보호 계층을 제공하며, 애플리케이션 및 서비스에서 사용자 생성 및 AI 생성 콘텐츠의 유해성을 감지할 수 있습니다. Azure AI Content Safety는 텍스트 및 이미지 API를 포함하며, 유해한 자료를 감지할 수 있습니다. Azure AI Foundry 내에서 Content Safety 서비스는 다양한 모달리티에서 유해 콘텐츠를 감지하는 샘플 코드를 탐색하고 시도할 수 있는 기능을 제공합니다. [빠른 시작 문서](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest)를 통해 서비스 요청 방법을 안내받을 수 있습니다.

또한 고려해야 할 또 다른 측면은 전체 애플리케이션 성능입니다. 멀티모달 및 멀티모델 애플리케이션의 경우 성능은 시스템이 사용자와 사용자의 기대에 부합하며 유해한 출력을 생성하지 않는 것을 의미합니다. [Performance and Quality 및 Risk and Safety 평가자](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in)를 사용하여 전체 애플리케이션 성능을 평가하는 것이 중요합니다. 또한 [맞춤형 평가자](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators)를 생성하고 평가할 수 있습니다.
Azure AI Evaluation SDK를 사용하여 개발 환경에서 AI 애플리케이션을 평가할 수 있습니다. 테스트 데이터셋이나 목표를 기반으로, 생성형 AI 애플리케이션의 결과물은 기본 제공 평가기나 사용자가 선택한 맞춤 평가기를 통해 정량적으로 측정됩니다. Azure AI Evaluation SDK를 사용하여 시스템을 평가하려면 [빠른 시작 가이드](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk)를 따라 시작할 수 있습니다. 평가 실행을 완료한 후, [Azure AI Foundry에서 결과를 시각화](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results)할 수 있습니다.

## 상표

이 프로젝트는 프로젝트, 제품 또는 서비스와 관련된 상표나 로고를 포함할 수 있습니다. Microsoft 상표나 로고의 허가된 사용은 [Microsoft 상표 및 브랜드 지침](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general)을 준수해야 하며, 이를 따라야 합니다. 이 프로젝트의 수정된 버전에서 Microsoft 상표나 로고를 사용하는 경우, 혼란을 초래하거나 Microsoft의 후원을 암시해서는 안 됩니다. 제삼자의 상표나 로고를 사용하는 경우, 해당 제삼자의 정책을 따라야 합니다.

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서를 해당 언어로 작성된 문서로 간주해야 하며, 중요한 정보에 대해서는 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.