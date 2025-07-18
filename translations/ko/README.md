<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5c07bb4c3c89a36c9be332a065a9a33c",
  "translation_date": "2025-07-16T15:01:21+00:00",
  "source_file": "README.md",
  "language_code": "ko"
}
-->
# Phi 요리책: Microsoft의 Phi 모델을 활용한 실습 예제

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

Phi는 현재 가장 강력하고 비용 효율적인 소형 언어 모델(SLM)로, 다국어, 추론, 텍스트/채팅 생성, 코딩, 이미지, 오디오 등 다양한 시나리오에서 우수한 벤치마크를 자랑합니다.

Phi는 클라우드나 엣지 디바이스에 배포할 수 있으며, 제한된 컴퓨팅 자원으로도 손쉽게 생성형 AI 애플리케이션을 구축할 수 있습니다.

이 리소스를 사용해 시작하려면 다음 단계를 따라주세요:  
1. **저장소 포크하기**: 클릭 [![GitHub 포크](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)  
2. **저장소 클론하기**: `git clone https://github.com/microsoft/PhiCookBook.git`  
3. [**Microsoft AI Discord 커뮤니티에 참여하여 전문가 및 개발자들과 교류하기**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/cover.eb18d1b9605d754b30973f4e17c6e11ea4f8473d9686ee378d6e7b44e3c70ac7.ko.png)

### 🌐 다국어 지원

#### GitHub Action을 통해 지원 (자동화 및 항상 최신 상태 유지)

[프랑스어](../fr/README.md) | [스페인어](../es/README.md) | [독일어](../de/README.md) | [러시아어](../ru/README.md) | [아랍어](../ar/README.md) | [페르시아어 (파르시)](../fa/README.md) | [우르두어](../ur/README.md) | [중국어 (간체)](../zh/README.md) | [중국어 (번체, 마카오)](../mo/README.md) | [중국어 (번체, 홍콩)](../hk/README.md) | [중국어 (번체, 대만)](../tw/README.md) | [일본어](../ja/README.md) | [한국어](./README.md) | [힌디어](../hi/README.md)  
[벵골어](../bn/README.md) | [마라티어](../mr/README.md) | [네팔어](../ne/README.md) | [펀자브어 (구르무키)](../pa/README.md) | [포르투갈어 (포르투갈)](../pt/README.md) | [포르투갈어 (브라질)](../br/README.md) | [이탈리아어](../it/README.md) | [폴란드어](../pl/README.md) | [터키어](../tr/README.md) | [그리스어](../el/README.md) | [태국어](../th/README.md) | [스웨덴어](../sv/README.md) | [덴마크어](../da/README.md) | [노르웨이어](../no/README.md) | [핀란드어](../fi/README.md) | [네덜란드어](../nl/README.md) | [히브리어](../he/README.md) | [베트남어](../vi/README.md) | [인도네시아어](../id/README.md) | [말레이어](../ms/README.md) | [타갈로그어 (필리핀어)](../tl/README.md) | [스와힐리어](../sw/README.md) | [헝가리어](../hu/README.md) | [체코어](../cs/README.md) | [슬로바키아어](../sk/README.md) | [루마니아어](../ro/README.md) | [불가리아어](../bg/README.md) | [세르비아어 (키릴문자)](../sr/README.md) | [크로아티아어](../hr/README.md) | [슬로베니아어](../sl/README.md)

## 목차

- 소개  
  - [Phi 가족에 오신 것을 환영합니다](./md/01.Introduction/01/01.PhiFamily.md)  
  - [환경 설정하기](./md/01.Introduction/01/01.EnvironmentSetup.md)  
  - [핵심 기술 이해하기](./md/01.Introduction/01/01.Understandingtech.md)  
  - [Phi 모델을 위한 AI 안전성](./md/01.Introduction/01/01.AISafety.md)  
  - [Phi 하드웨어 지원](./md/01.Introduction/01/01.Hardwaresupport.md)  
  - [Phi 모델 및 플랫폼별 가용성](./md/01.Introduction/01/01.Edgeandcloud.md)  
  - [Guidance-ai와 Phi 사용하기](./md/01.Introduction/01/01.Guidance.md)  
  - [GitHub Marketplace 모델](https://github.com/marketplace/models)  
  - [Azure AI 모델 카탈로그](https://ai.azure.com)

- 다양한 환경에서 Phi 추론  
  - [Hugging face](./md/01.Introduction/02/01.HF.md)  
  - [GitHub 모델](./md/01.Introduction/02/02.GitHubModel.md)  
  - [Azure AI Foundry 모델 카탈로그](./md/01.Introduction/02/03.AzureAIFoundry.md)  
  - [Ollama](./md/01.Introduction/02/04.Ollama.md)  
  - [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)  
  - [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)  
  - [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md)

- Phi 가족 추론  
  - [iOS에서 Phi 추론](./md/01.Introduction/03/iOS_Inference.md)  
  - [Android에서 Phi 추론](./md/01.Introduction/03/Android_Inference.md)  
  - [Jetson에서 Phi 추론](./md/01.Introduction/03/Jetson_Inference.md)  
  - [AI PC에서 Phi 추론](./md/01.Introduction/03/AIPC_Inference.md)  
  - [Apple MLX 프레임워크로 Phi 추론](./md/01.Introduction/03/MLX_Inference.md)  
  - [로컬 서버에서 Phi 추론](./md/01.Introduction/03/Local_Server_Inference.md)  
  - [AI Toolkit을 사용한 원격 서버에서 Phi 추론](./md/01.Introduction/03/Remote_Interence.md)  
  - [Rust로 Phi 추론](./md/01.Introduction/03/Rust_Inference.md)  
  - [로컬에서 Phi--Vision 추론](./md/01.Introduction/03/Vision_Inference.md)  
  - [Kaito AKS, Azure Containers(공식 지원)와 함께하는 Phi 추론](./md/01.Introduction/03/Kaito_Inference.md)

- Phi 가족 양자화  
  - [llama.cpp를 사용한 Phi-3.5 / 4 양자화](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)  
  - [onnxruntime용 생성형 AI 확장으로 Phi-3.5 / 4 양자화](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)  
  - [Intel OpenVINO를 사용한 Phi-3.5 / 4 양자화](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)  
  - [Apple MLX 프레임워크를 사용한 Phi-3.5 / 4 양자화](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

- Phi 평가  
  - [책임 있는 AI](./md/01.Introduction/05/ResponsibleAI.md)  
  - [평가를 위한 Azure AI Foundry](./md/01.Introduction/05/AIFoundry.md)  
  - [평가를 위한 Promptflow 사용법](./md/01.Introduction/05/Promptflow.md)

- Azure AI Search와 함께하는 RAG  
  - [Phi-4-mini 및 Phi-4-multimodal(RAG)을 Azure AI Search와 함께 사용하는 방법](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Phi 애플리케이션 개발 샘플  
  - 텍스트 및 채팅 애플리케이션  
    - Phi-4 샘플 🆕  
      - [📓] [Phi-4-mini ONNX 모델과 채팅하기](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)  
      - [Phi-4 로컬 ONNX 모델과 채팅하기 (.NET)](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)  
      - [Semantic Kernel을 사용한 Phi-4 ONNX 채팅 .NET 콘솔 앱](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)  
    - Phi-3 / 3.5 샘플  
      - [Phi3, ONNX Runtime Web 및 WebGPU를 사용한 브라우저 내 로컬 챗봇](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)  
      - [OpenVino 채팅](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)  
      - [멀티 모델 - Phi-3-mini와 OpenAI Whisper의 인터랙티브 조합](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)  
      - [MLFlow - 래퍼 빌드 및 Phi-3와 MLFlow 사용하기](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)  
      - [모델 최적화 - Olive를 사용한 Phi-3-min 모델 ONNX Runtime Web 최적화 방법](https://github.com/microsoft/Olive/tree/main/examples/phi3)  
      - [Phi-3 mini-4k-instruct-onnx를 사용한 WinUI3 앱](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)  
      - [WinUI3 멀티 모델 AI 기반 노트 앱 샘플](https://github.com/microsoft/ai-powered-notes-winui3-sample)
- [Prompt flow와 함께 맞춤형 Phi-3 모델 미세 조정 및 통합](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
- [Azure AI Foundry에서 Prompt flow와 함께 맞춤형 Phi-3 모델 미세 조정 및 통합](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
- [Microsoft의 책임 있는 AI 원칙에 중점을 둔 Azure AI Foundry에서 미세 조정된 Phi-3 / Phi-3.5 모델 평가](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
- [📓] [Phi-3.5-mini-instruct 언어 예측 샘플 (중국어/영어)](../../md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
- [Phi-3.5-Instruct WebGPU RAG 챗봇](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
- [Windows GPU를 사용하여 Phi-3.5-Instruct ONNX로 Prompt flow 솔루션 만들기](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
- [Microsoft Phi-3.5 tflite를 사용하여 Android 앱 만들기](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
- [Microsoft.ML.OnnxRuntime를 사용한 로컬 ONNX Phi-3 모델 Q&A .NET 예제](../../md/04.HOL/dotnet/src/LabsPhi301)
- [Semantic Kernel과 Phi-3를 사용한 콘솔 챗 .NET 앱](../../md/04.HOL/dotnet/src/LabsPhi302)

- Azure AI Inference SDK 코드 기반 샘플  
  - Phi-4 샘플 🆕  
    - [📓] [Phi-4-multimodal을 사용한 프로젝트 코드 생성](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)  
  - Phi-3 / 3.5 샘플  
    - [Microsoft Phi-3 패밀리로 나만의 Visual Studio Code GitHub Copilot Chat 만들기](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)  
    - [GitHub 모델로 Phi-3.5를 사용해 나만의 Visual Studio Code Chat Copilot 에이전트 만들기](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)  

- 고급 추론 샘플  
  - Phi-4 샘플 🆕  
    - [📓] [Phi-4-mini-reasoning 또는 Phi-4-reasoning 샘플](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)  
    - [📓] [Microsoft Olive로 Phi-4-mini-reasoning 미세 조정](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)  
    - [📓] [Apple MLX로 Phi-4-mini-reasoning 미세 조정](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)  
    - [📓] [GitHub 모델로 Phi-4-mini-reasoning](../../md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)  
    - [📓] [Azure AI Foundry 모델로 Phi-4-mini-reasoning](../../md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)  
- 데모  
    - [Hugging Face Spaces에서 호스팅되는 Phi-4-mini 데모](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)  
    - [Hugging Face Spaces에서 호스팅되는 Phi-4-multimodal 데모](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)  
- 비전 샘플  
  - Phi-4 샘플 🆕  
    - [📓] [Phi-4-multimodal을 사용해 이미지 읽기 및 코드 생성](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md)  
  - Phi-3 / 3.5 샘플  
    - [📓][Phi-3-vision-이미지 텍스트 변환](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)  
    - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)  
    - [📓][Phi-3-vision CLIP 임베딩](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)  
    - [데모: Phi-3 재활용](https://github.com/jennifermarsman/PhiRecycling/)  
    - [Phi-3-vision - Phi3-Vision과 OpenVINO를 활용한 시각 언어 어시스턴트](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)  
    - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)  
    - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)  
    - [📓][Phi-3.5 Vision 다중 프레임 또는 다중 이미지 샘플](../../md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)  
    - [Microsoft.ML.OnnxRuntime .NET을 사용한 Phi-3 Vision 로컬 ONNX 모델](../../md/04.HOL/dotnet/src/LabsPhi303)  
    - [메뉴 기반 Phi-3 Vision 로컬 ONNX 모델 Microsoft.ML.OnnxRuntime .NET 사용](../../md/04.HOL/dotnet/src/LabsPhi304)  

- 수학 샘플  
  - Phi-4-Mini-Flash-Reasoning-Instruct 샘플 🆕 [Phi-4-Mini-Flash-Reasoning-Instruct를 활용한 수학 데모](../../md/02.Application/09.Math/MathDemo.ipynb)  

- 오디오 샘플  
  - Phi-4 샘플 🆕  
    - [📓] [Phi-4-multimodal을 사용한 오디오 전사 추출](./md/02.Application/05.Audio/Phi4/Transciption/README.md)  
    - [📓] [Phi-4-multimodal 오디오 샘플](../../md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)  
    - [📓] [Phi-4-multimodal 음성 번역 샘플](../../md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)  
    - [Phi-4-multimodal 오디오를 사용해 오디오 파일 분석 및 전사 생성하는 .NET 콘솔 애플리케이션](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)  

- MOE 샘플  
  - Phi-3 / 3.5 샘플  
    - [📓] [Phi-3.5 Mixture of Experts 모델(MoEs) 소셜 미디어 샘플](../../md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)  
    - [📓] [NVIDIA NIM Phi-3 MOE, Azure AI Search, LlamaIndex를 활용한 Retrieval-Augmented Generation (RAG) 파이프라인 구축](../../md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)  
- 함수 호출 샘플  
  - Phi-4 샘플 🆕  
    - [📓] [Phi-4-mini와 함께 함수 호출 사용하기](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)  
    - [📓] [Phi-4-mini로 다중 에이전트 생성 시 함수 호출 사용하기](../../md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)  
    - [📓] [Ollama와 함께 함수 호출 사용하기](../../md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)  
    - [📓] [ONNX와 함께 함수 호출 사용하기](../../md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)  
- 멀티모달 믹싱 샘플  
  - Phi-4 샘플 🆕  
    - [📓] [기술 기자로서 Phi-4-multimodal 사용하기](../../md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)  
    - [Phi-4-multimodal을 사용해 이미지 분석하는 .NET 콘솔 애플리케이션](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)  

- Phi 미세 조정 샘플  
  - [미세 조정 시나리오](./md/03.FineTuning/FineTuning_Scenarios.md)  
  - [미세 조정과 RAG 비교](./md/03.FineTuning/FineTuning_vs_RAG.md)  
  - [Phi-3를 산업 전문가로 만드는 미세 조정](./md/03.FineTuning/LetPhi3gotoIndustriy.md)  
  - [VS Code용 AI Toolkit으로 Phi-3 미세 조정하기](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)  
  - [Azure Machine Learning Service로 Phi-3 미세 조정하기](./md/03.FineTuning/Introduce_AzureML.md)  
  - [Lora로 Phi-3 미세 조정하기](./md/03.FineTuning/FineTuning_Lora.md)  
  - [QLora로 Phi-3 미세 조정하기](./md/03.FineTuning/FineTuning_Qlora.md)  
  - [Azure AI Foundry로 Phi-3 미세 조정하기](./md/03.FineTuning/FineTuning_AIFoundry.md)  
  - [Azure ML CLI/SDK로 Phi-3 미세 조정하기](./md/03.FineTuning/FineTuning_MLSDK.md)  
  - [Microsoft Olive로 미세 조정하기](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)  
  - [Microsoft Olive 실습 랩](./md/03.FineTuning/olive-lab/readme.md)  
  - [Weights and Bias로 Phi-3-vision 미세 조정하기](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)  
  - [Apple MLX 프레임워크로 Phi-3 미세 조정하기](./md/03.FineTuning/FineTuning_MLX.md)  
  - [Phi-3-vision 미세 조정 (공식 지원)](./md/03.FineTuning/FineTuning_Vision.md)  
  - [Kaito AKS, Azure Containers로 Phi-3 미세 조정 (공식 지원)](./md/03.FineTuning/FineTuning_Kaito.md)  
  - [Phi-3 및 3.5 Vision 미세 조정](https://github.com/2U1/Phi3-Vision-Finetune)  

- 실습 랩  
  - [최신 모델 탐색: LLM, SLM, 로컬 개발 등](https://github.com/microsoft/aitour-exploring-cutting-edge-models)  
  - [NLP 잠재력 열기: Microsoft Olive로 미세 조정](https://github.com/azure/Ignite_FineTuning_workshop)  

- 학술 연구 논문 및 출판물  
  - [Textbooks Are All You Need II: phi-1.5 기술 보고서](https://arxiv.org/abs/2309.05463)  
  - [Phi-3 기술 보고서: 휴대폰에서 실행 가능한 고성능 언어 모델](https://arxiv.org/abs/2404.14219)  
  - [Phi-4 기술 보고서](https://arxiv.org/abs/2412.08905)  
  - [Phi-4-Mini 기술 보고서: Mixture-of-LoRAs를 통한 작고 강력한 멀티모달 언어 모델](https://arxiv.org/abs/2503.01743)  
  - [차량 내 함수 호출 최적화를 위한 소형 언어 모델 연구](https://arxiv.org/abs/2501.02342)  
  - [(WhyPHI) 다지선다형 질문 응답을 위한 PHI-3 미세 조정: 방법론, 결과 및 과제](https://arxiv.org/abs/2501.01588)
- [Phi-4-reasoning 기술 보고서](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
- [Phi-4-mini-reasoning 기술 보고서](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Phi 모델 사용하기

### Azure AI Foundry에서 Phi 사용하기

Microsoft Phi를 사용하는 방법과 다양한 하드웨어 장치에서 E2E 솔루션을 구축하는 방법을 배울 수 있습니다. Phi를 직접 경험해보고 싶다면, 모델을 직접 사용해보고 시나리오에 맞게 Phi를 커스터마이징해보세요. [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai)를 통해 시작할 수 있으며, 자세한 내용은 [Azure AI Foundry 시작하기](/md/02.QuickStart/AzureAIFoundry_QuickStart.md)에서 확인할 수 있습니다.

**Playground**  
각 모델마다 전용 playground가 있어 모델을 테스트할 수 있습니다. [Azure AI Playground](https://aka.ms/try-phi3)를 이용해보세요.

### GitHub 모델에서 Phi 사용하기

Microsoft Phi를 사용하는 방법과 다양한 하드웨어 장치에서 E2E 솔루션을 구축하는 방법을 배울 수 있습니다. Phi를 직접 경험해보고 싶다면, 모델을 직접 사용해보고 시나리오에 맞게 Phi를 커스터마이징해보세요. [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo)를 통해 시작할 수 있으며, 자세한 내용은 [GitHub Model Catalog 시작하기](/md/02.QuickStart/GitHubModel_QuickStart.md)에서 확인할 수 있습니다.

**Playground**  
각 모델마다 전용 [playground가 있어 모델을 테스트할 수 있습니다](/md/02.QuickStart/GitHubModel_QuickStart.md).

### Hugging Face에서 Phi 사용하기

[Hugging Face](https://huggingface.co/microsoft)에서도 모델을 찾을 수 있습니다.

**Playground**  
[Hugging Chat playground](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## 책임 있는 AI

Microsoft는 고객이 AI 제품을 책임감 있게 사용할 수 있도록 지원하며, 투명성 노트와 영향 평가 같은 도구를 통해 학습 내용을 공유하고 신뢰 기반의 파트너십을 구축하는 데 최선을 다하고 있습니다. 이러한 자료들은 [https://aka.ms/RAI](https://aka.ms/RAI)에서 확인할 수 있습니다.  
Microsoft의 책임 있는 AI 접근법은 공정성, 신뢰성 및 안전성, 개인정보 보호 및 보안, 포용성, 투명성, 책임성이라는 AI 원칙에 기반하고 있습니다.

이 샘플에서 사용된 대규모 자연어, 이미지, 음성 모델은 불공정하거나 신뢰할 수 없거나 불쾌감을 줄 수 있는 방식으로 작동할 가능성이 있으며, 이로 인해 피해가 발생할 수 있습니다. 위험과 한계에 대해 알고 싶다면 [Azure OpenAI 서비스 투명성 노트](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text)를 참고하세요.

이러한 위험을 완화하기 위한 권장 방법은 아키텍처에 안전 시스템을 포함시켜 해로운 행동을 감지하고 방지하는 것입니다. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview)는 애플리케이션과 서비스에서 사용자 생성 및 AI 생성 콘텐츠의 유해성을 감지할 수 있는 독립적인 보호 계층을 제공합니다. Azure AI Content Safety는 유해한 텍스트와 이미지를 감지할 수 있는 API를 포함하고 있습니다. Azure AI Foundry 내에서는 Content Safety 서비스를 통해 다양한 형태의 유해 콘텐츠를 탐색하고 샘플 코드를 시험해볼 수 있습니다. 다음 [빠른 시작 문서](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest)에서는 서비스에 요청을 보내는 방법을 안내합니다.

또 다른 고려 사항은 전체 애플리케이션 성능입니다. 멀티모달 및 멀티모델 애플리케이션에서는 시스템이 사용자와 개발자가 기대하는 대로 작동하는지, 즉 유해한 출력을 생성하지 않는지를 성능의 기준으로 봅니다. 전체 애플리케이션의 성능을 평가할 때는 [성능 및 품질, 위험 및 안전 평가자](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in)를 활용하는 것이 중요합니다. 또한 [사용자 정의 평가자](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators)를 만들어 평가할 수도 있습니다.

개발 환경에서 AI 애플리케이션을 평가하려면 [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html)를 사용할 수 있습니다. 테스트 데이터셋이나 목표값을 기준으로 생성된 AI 결과물을 내장 평가자 또는 원하는 사용자 정의 평가자를 통해 정량적으로 측정할 수 있습니다. Azure AI Evaluation SDK를 사용해 시스템을 평가하는 방법은 [빠른 시작 가이드](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk)를 참고하세요. 평가 실행 후에는 [Azure AI Foundry에서 결과를 시각화](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results)할 수 있습니다.

## 상표

이 프로젝트에는 프로젝트, 제품 또는 서비스의 상표나 로고가 포함될 수 있습니다. Microsoft 상표나 로고의 사용은 [Microsoft 상표 및 브랜드 가이드라인](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general)을 준수해야 하며, 허가된 경우에만 사용 가능합니다.  
이 프로젝트의 수정된 버전에서 Microsoft 상표나 로고를 사용할 경우 혼동을 일으키거나 Microsoft의 후원을 암시해서는 안 됩니다. 제3자 상표나 로고의 사용은 해당 제3자의 정책을 따라야 합니다.

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원문은 해당 언어의 원본 문서가 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 본 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.