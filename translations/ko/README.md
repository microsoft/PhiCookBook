<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c2e4b490f4bd424b095f21e38c6af33b",
  "translation_date": "2026-01-05T01:20:56+00:00",
  "source_file": "README.md",
  "language_code": "ko"
}
-->
# Phi Cookbook: Microsoft의 Phi 모델을 활용한 실습 예제

[![GitHub Codespaces에서 샘플 열기 및 사용](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Dev Containers에서 열기](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub 기여자](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub 이슈](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PRs 환영](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub watchers](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub stars](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Azure AI Foundry 디스코드](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi는 Microsoft에서 개발한 오픈 소스 AI 모델 시리즈입니다. 

Phi는 현재 다중 언어, 추론, 텍스트/채팅 생성, 코딩, 이미지, 오디오 및 기타 시나리오에서 매우 우수한 벤치마크를 보이는 가장 강력하고 비용 효율적인 소형 언어 모델(SLM)입니다. 

Phi는 클라우드나 엣지 디바이스에 배포할 수 있으며, 제한된 컴퓨팅 자원으로도 생성형 AI 애플리케이션을 쉽게 빌드할 수 있습니다.

이 리소스를 사용하여 시작하려면 다음 단계를 따르세요:
1. **저장소 포크하기**: 클릭 [![GitHub 포크](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **저장소 클론하기**:   `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Microsoft AI Discord 커뮤니티에 가입하고 전문가 및 동료 개발자들과 만나보세요**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![커버](../../translated_images/cover.eb18d1b9605d754b.ko.png)

### 🌐 다국어 지원

#### GitHub Action을 통해 지원 (자동화 및 항상 최신 상태)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[아랍어](../ar/README.md) | [벵골어](../bn/README.md) | [불가리아어](../bg/README.md) | [버마어 (미얀마)](../my/README.md) | [중국어(간체)](../zh/README.md) | [중국어(번체, 홍콩)](../hk/README.md) | [중국어(번체, 마카오)](../mo/README.md) | [중국어(번체, 대만)](../tw/README.md) | [크로아티아어](../hr/README.md) | [체코어](../cs/README.md) | [덴마크어](../da/README.md) | [네덜란드어](../nl/README.md) | [에스토니아어](../et/README.md) | [핀란드어](../fi/README.md) | [프랑스어](../fr/README.md) | [독일어](../de/README.md) | [그리스어](../el/README.md) | [히브리어](../he/README.md) | [힌디어](../hi/README.md) | [헝가리어](../hu/README.md) | [인도네시아어](../id/README.md) | [이탈리아어](../it/README.md) | [일본어](../ja/README.md) | [칸나다어](../kn/README.md) | [한국어](./README.md) | [리투아니아어](../lt/README.md) | [말레이어](../ms/README.md) | [말라얄람어](../ml/README.md) | [마라티어](../mr/README.md) | [네팔어](../ne/README.md) | [나이지리아 피진어](../pcm/README.md) | [노르웨이어](../no/README.md) | [페르시아어 (파르시)](../fa/README.md) | [폴란드어](../pl/README.md) | [포르투갈어(브라질)](../br/README.md) | [포르투갈어(포르투갈)](../pt/README.md) | [펀자브어 (구르무키)](../pa/README.md) | [루마니아어](../ro/README.md) | [러시아어](../ru/README.md) | [세르비아어 (키릴문자)](../sr/README.md) | [슬로바키아어](../sk/README.md) | [슬로베니아어](../sl/README.md) | [스페인어](../es/README.md) | [스와힐리어](../sw/README.md) | [스웨덴어](../sv/README.md) | [타갈로그어 (필리핀)](../tl/README.md) | [타밀어](../ta/README.md) | [텔루구어](../te/README.md) | [태국어](../th/README.md) | [터키어](../tr/README.md) | [우크라이나어](../uk/README.md) | [우르두어](../ur/README.md) | [베트남어](../vi/README.md)

> **로컬에서 복제하시겠습니까?**

> 이 저장소에는 50개 이상의 언어 번역이 포함되어 있어 다운로드 크기가 크게 증가합니다. 번역 없이 클론하려면 sparse checkout을 사용하세요:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/PhiCookBook.git
> cd PhiCookBook
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> 이렇게 하면 코스를 완료하는 데 필요한 모든 것을 얻을 수 있으며 다운로드가 훨씬 빨라집니다.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## 목차

- 소개
  - [Phi 패밀리에 오신 것을 환영합니다](./md/01.Introduction/01/01.PhiFamily.md)
  - [환경 설정](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [핵심 기술 이해](./md/01.Introduction/01/01.Understandingtech.md)
  - [Phi 모델을 위한 AI 안전](./md/01.Introduction/01/01.AISafety.md)
  - [Phi 하드웨어 지원](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Phi 모델 및 플랫폼별 가용성](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Guidance-ai와 Phi 사용하기](./md/01.Introduction/01/01.Guidance.md)
  - [GitHub Marketplace 모델](https://github.com/marketplace/models)
  - [Azure AI 모델 카탈로그](https://ai.azure.com)

- 다양한 환경에서의 Phi 추론
    -  [Hugging face](./md/01.Introduction/02/01.HF.md)
    -  [GitHub Models](./md/01.Introduction/02/02.GitHubModel.md)
    -  [Azure AI Foundry Model Catalog](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    -  [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md)

- Phi 계열 추론
    - [iOS에서 Phi 추론](./md/01.Introduction/03/iOS_Inference.md)
    - [Android에서 Phi 추론](./md/01.Introduction/03/Android_Inference.md)
    - [Jetson에서 Phi 추론](./md/01.Introduction/03/Jetson_Inference.md)
    - [AI PC에서 Phi 추론](./md/01.Introduction/03/AIPC_Inference.md)
    - [Apple MLX 프레임워크로 Phi 추론](./md/01.Introduction/03/MLX_Inference.md)
    - [로컬 서버에서 Phi 추론](./md/01.Introduction/03/Local_Server_Inference.md)
    - [AI Toolkit을 사용한 원격 서버에서 Phi 추론](./md/01.Introduction/03/Remote_Interence.md)
    - [Rust로 Phi 추론](./md/01.Introduction/03/Rust_Inference.md)
    - [로컬에서 Phi--Vision 추론](./md/01.Introduction/03/Vision_Inference.md)
    - [Kaito AKS, Azure Containers(official support)와 함께하는 Phi 추론](./md/01.Introduction/03/Kaito_Inference.md)
-  [Phi 계열 양자화](./md/01.Introduction/04/QuantifyingPhi.md)
    - [llama.cpp를 사용한 Phi-3.5 / 4 양자화](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [onnxruntime용 Generative AI 확장을 사용한 Phi-3.5 / 4 양자화](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Intel OpenVINO를 사용한 Phi-3.5 / 4 양자화](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Apple MLX 프레임워크를 사용한 Phi-3.5 / 4 양자화](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

-  Phi 평가
    - [책임 있는 AI](./md/01.Introduction/05/ResponsibleAI.md)
    - [평가를 위한 Azure AI Foundry](./md/01.Introduction/05/AIFoundry.md)
    - [평가를 위한 Promptflow 사용](./md/01.Introduction/05/Promptflow.md)
 
- RAG와 Azure AI Search
    - [Azure AI Search와 함께 Phi-4-mini 및 Phi-4-multimodal(RAG)을 사용하는 방법](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Phi 애플리케이션 개발 샘플
  - 텍스트 및 채팅 애플리케이션
    - Phi-4 샘플 🆕
      - [📓] [Phi-4-mini ONNX 모델로 채팅하기](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Phi-4 로컬 ONNX 모델로 채팅 (.NET)](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Sementic Kernel을 사용한 Phi-4 ONNX 기반 Chat .NET 콘솔 앱](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Phi-3 / 3.5 샘플
      - [브라우저에서 Phi3, ONNX Runtime Web 및 WebGPU를 사용한 로컬 챗봇](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVino 채팅](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [멀티 모델 - 대화형 Phi-3-mini 및 OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - 래퍼 생성 및 MLFlow와 Phi-3 사용](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [모델 최적화 - Olive로 ONNX Runtime Web에 대한 Phi-3-min 모델 최적화 방법](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [Phi-3 mini-4k-instruct-onnx를 사용한 WinUI3 앱](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      -[WinUI3 다중 모델 AI 기반 노트 앱 샘플](https://github.com/microsoft/ai-powered-notes-winui3-sample)
      - [Prompt flow로 맞춤 Phi-3 모델 미세 조정 및 통합](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
      - [Azure AI Foundry에서 Prompt flow로 맞춤 Phi-3 모델 미세 조정 및 통합](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
      - [Microsoft의 Responsible AI 원칙에 중점을 두고 Azure AI Foundry에서 미세 조정된 Phi-3 / Phi-3.5 모델 평가](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
      - [📓] [Phi-3.5-mini-instruct 언어 예측 샘플 (중국어/영어)](./md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
      - [Phi-3.5-Instruct WebGPU RAG 챗봇](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
      - [Windows GPU를 사용하여 Phi-3.5-Instruct ONNX로 Prompt flow 솔루션 만들기](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
      - [Microsoft Phi-3.5 tflite를 사용하여 Android 앱 만들기](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
      - [Microsoft.ML.OnnxRuntime을 사용하여 로컬 ONNX Phi-3 모델로 구현한 Q&A .NET 예제](../../md/04.HOL/dotnet/src/LabsPhi301)
      - [Semantic Kernel 및 Phi-3를 사용한 콘솔 채팅 .NET 앱](../../md/04.HOL/dotnet/src/LabsPhi302)

  - Azure AI Inference SDK Code Based Samples 
    - Phi-4 샘플 🆕
      - [📓] [Phi-4-multimodal을 사용하여 프로젝트 코드 생성](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
    - Phi-3 / 3.5 샘플
      - [Microsoft Phi-3 계열로 나만의 Visual Studio Code GitHub Copilot Chat 만들기](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
      - [GitHub Models의 Phi-3.5로 나만의 Visual Studio Code Chat Copilot 에이전트 만들기](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

  - 고급 추론 샘플
    - Phi-4 샘플 🆕
      - [📓] [Phi-4-mini-reasoning 또는 Phi-4-reasoning 샘플](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
      - [📓] [Microsoft Olive로 Phi-4-mini-reasoning 미세 조정](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Apple MLX로 Phi-4-mini-reasoning 미세 조정](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [GitHub Models로 Phi-4-mini-reasoning](./md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
      - [📓] [Azure AI Foundry Models로 Phi-4-mini-reasoning](./md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
  - 데모
      - [Hugging Face Spaces에 호스팅된 Phi-4-mini 데모](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
      - [Hugginge Face Spaces에 호스팅된 Phi-4-multimodal 데모](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
  - 비전 샘플
    - Phi-4 샘플 🆕
      - [📓] [Phi-4-multimodal을 사용하여 이미지를 읽고 코드 생성](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
    - Phi-3 / 3.5 샘플
      -  [📓][Phi-3-vision-이미지 텍스트에서 텍스트로](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
      - [📓][Phi-3-vision CLIP 임베딩](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [데모: Phi-3 Recycling](https://github.com/jennifermarsman/PhiRecycling/)
      - [Phi-3-vision - 시각 언어 어시스턴트 - Phi3-Vision 및 OpenVINO와 함께](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
      - [Phi-3 비전 Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
      - [Phi-3 비전 OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
      - [📓][Phi-3.5 비전 다중 프레임 또는 다중 이미지 샘플](./md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
      - [Microsoft.ML.OnnxRuntime .NET을 사용한 Phi-3 비전 로컬 ONNX 모델](../../md/04.HOL/dotnet/src/LabsPhi303)
      - [메뉴 기반 Phi-3 비전 로컬 ONNX 모델 (Microsoft.ML.OnnxRuntime .NET 사용)](../../md/04.HOL/dotnet/src/LabsPhi304)

  - 수학 샘플
    -  Phi-4-Mini-Flash-Reasoning-Instruct 샘플 🆕 [Phi-4-Mini-Flash-Reasoning-Instruct를 사용한 수학 데모](./md/02.Application/09.Math/MathDemo.ipynb)

  - 오디오 샘플
    - Phi-4 샘플 🆕
      - [📓] [Phi-4-multimodal을 사용한 오디오 전사 추출](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
      - [📓] [Phi-4-multimodal 오디오 샘플](./md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
      - [📓] [Phi-4-multimodal 음성 번역 샘플](./md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
      - [.NET 콘솔 애플리케이션 - Phi-4-multimodal 오디오를 사용하여 오디오 파일 분석 및 전사 생성](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

  - MOE 샘플
    - Phi-3 / 3.5 샘플
      - [📓] [Phi-3.5 Mixture of Experts 모델(MoEs) 소셜 미디어 샘플](./md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
      - [📓] [NVIDIA NIM Phi-3 MOE, Azure AI Search 및 LlamaIndex로 Retrieval-Augmented Generation(RAG) 파이프라인 구축](./md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)
      - 
  - 함수 호출 샘플
    - Phi-4 샘플 🆕
      -  [📓] [Phi-4-mini에서 함수 호출 사용하기](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
      -  [📓] [Phi-4-mini로 멀티 에이전트 생성에 함수 호출 사용하기](./md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
      -  [📓] [Ollama와 함께 함수 호출 사용하기](./md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
      -  [📓] [ONNX와 함께 함수 호출 사용하기](./md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)
  - 멀티모달 믹싱 샘플
    - Phi-4 샘플 🆕
      -  [📓] [기술 기자로서 Phi-4-multimodal 사용하기](./md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
      - [.NET 콘솔 애플리케이션 - Phi-4-multimodal을 사용하여 이미지 분석](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Phi 미세 조정 샘플
  - [미세 조정 시나리오](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [미세 조정 vs RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [Phi-3를 산업 전문가로 만드는 미세 조정](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [VS Code용 AI Toolkit으로 Phi-3 미세 조정](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Azure Machine Learning Service로 Phi-3 미세 조정](./md/03.FineTuning/Introduce_AzureML.md)
  - [Lora로 Phi-3 미세 조정](./md/03.FineTuning/FineTuning_Lora.md)
  - [QLora로 Phi-3 미세 조정](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Azure AI Foundry로 Phi-3 미세 조정](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Azure ML CLI/SDK로 Phi-3 미세 조정](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Microsoft Olive로 미세 조정](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Microsoft Olive 핸즈온 랩으로 미세 조정](./md/03.FineTuning/olive-lab/readme.md)
  - [Weights and Bias로 Phi-3-vision 미세 조정](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [Apple MLX 프레임워크로 Phi-3 미세 조정](./md/03.FineTuning/FineTuning_MLX.md)
  - [Phi-3-vision 미세 조정 (공식 지원)](./md/03.FineTuning/FineTuning_Vision.md)
  - [Kaito AKS , Azure Containers(공식 지원)](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Phi-3 및 3.5 비전 미세 조정](https://github.com/2U1/Phi3-Vision-Finetune)

- 핸즈온 랩
  - [최첨단 모델 탐색: LLM, SLM, 로컬 개발 등](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [NLP 잠재력 열기: Microsoft Olive로 미세 조정](https://github.com/azure/Ignite_FineTuning_workshop)

- 학술 연구 논문 및 출판물
  - [Textbooks Are All You Need II: phi-1.5 기술 보고서](https://arxiv.org/abs/2309.05463)
  - [Phi-3 기술 보고서: 휴대폰에서 로컬로 실행 가능한 고성능 언어 모델](https://arxiv.org/abs/2404.14219)
  - [Phi-4 기술 보고서](https://arxiv.org/abs/2412.08905)
  - [Phi-4-Mini 기술 보고서: Mixture-of-LoRAs를 통한 작고 강력한 멀티모달 언어 모델](https://arxiv.org/abs/2503.01743)
  - [차량 내 기능 호출을 위한 소형 언어 모델 최적화](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) 다지선다형 질문 응답을 위한 PHI-3 파인튜닝: 방법론, 결과 및 과제](https://arxiv.org/abs/2501.01588)
  - [Phi-4-reasoning 기술 보고서](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Phi-4-mini-reasoning 기술 보고서](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Phi 모델 사용하기

### Azure AI Foundry의 Phi

Microsoft Phi를 사용하는 방법과 다양한 하드웨어 장치에서 엔드 투 엔드 솔루션을 구축하는 방법을 배울 수 있습니다. Phi를 직접 경험하려면 모델을 사용해 보고 시나리오에 맞게 Phi를 사용자 지정하면서 [Azure AI Foundry Azure AI 모델 카탈로그](https://aka.ms/phi3-azure-ai)를 사용해 보세요. 자세한 내용은 [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md)의 시작하기 자료를 확인하세요.

**플레이그라운드**
각 모델에는 모델을 테스트할 수 있는 전용 플레이그라운드가 있습니다 [Azure AI Playground](https://aka.ms/try-phi3).

### GitHub Models의 Phi

Microsoft Phi를 사용하는 방법과 다양한 하드웨어 장치에서 엔드 투 엔드 솔루션을 구축하는 방법을 배울 수 있습니다. Phi를 직접 경험하려면 모델을 사용해 보고 시나리오에 맞게 Phi를 사용자 지정하면서 [GitHub 모델 카탈로그](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo)를 사용해 보세요. 자세한 내용은 [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md)의 시작하기 자료를 확인하세요.

**플레이그라운드**
각 모델에는 모델을 테스트할 수 있는 전용 [플레이그라운드](/md/02.QuickStart/GitHubModel_QuickStart.md)가 있습니다.

### Hugging Face의 Phi

모델은 또한 [Hugging Face](https://huggingface.co/microsoft)에서 찾을 수 있습니다.

**플레이그라운드**
[Hugging Chat 플레이그라운드](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

 ## 🎒 기타 강좌

저희 팀은 다른 강좌도 제공합니다! 확인해 보세요:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![초보자를 위한 LangChain4j](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![초보자를 위한 LangChain.js](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

---

### Azure / Edge / MCP / Agents
[![초보자를 위한 AZD](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![초보자를 위한 Edge AI](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![초보자를 위한 MCP](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![초보자를 위한 AI 에이전트](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### 생성형 AI 시리즈
[![초보자를 위한 생성형 AI](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![생성형 AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![생성형 AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![생성형 AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### 핵심 학습
[![초보자를 위한 ML](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![초보자를 위한 데이터 사이언스](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![초보자를 위한 AI](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![초보자를 위한 사이버보안](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![초보자를 위한 웹 개발](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![초보자를 위한 IoT](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![초보자를 위한 XR 개발](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot 시리즈
[![AI 페어 프로그래밍을 위한 Copilot](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![C#/.NET용 Copilot](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot 어드벤처](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## 책임 있는 AI 

Microsoft는 고객이 AI 제품을 책임감 있게 사용할 수 있도록 지원하고, 학습 내용을 공유하며, Transparency Notes 및 영향 평가와 같은 도구를 통해 신뢰 기반 파트너십을 구축하기 위해 노력하고 있습니다. 이러한 리소스의 많은 부분은 [https://aka.ms/RAI](https://aka.ms/RAI)에서 찾을 수 있습니다.
Microsoft의 책임 있는 AI 접근 방식은 공정성, 신뢰성 및 안전성, 개인정보 보호 및 보안, 포용성, 투명성 및 책임성이라는 AI 원칙에 기반을 두고 있습니다.

이 샘플에서 사용된 것과 같은 대규모 자연어, 이미지 및 음성 모델은 불공정하거나 신뢰할 수 없거나 공격적일 수 있는 방식으로 동작하여 피해를 유발할 가능성이 있습니다. 위험과 제한 사항에 대해 알고 싶다면 [Azure OpenAI 서비스 투명성 노트](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text)를 참조하세요.

이러한 위험을 완화하기 위한 권장 접근 방식은 아키텍처에 유해한 동작을 감지하고 방지할 수 있는 안전 시스템을 포함하는 것입니다. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview)는 애플리케이션 및 서비스에서 사용자 생성 및 AI 생성 유해 콘텐츠를 감지할 수 있는 독립적인 보호 계층을 제공합니다. Azure AI Content Safety에는 유해한 자료를 감지할 수 있는 텍스트 및 이미지 API가 포함되어 있습니다. Azure AI Foundry 내에서 Content Safety 서비스는 다양한 모달리티에서 유해한 콘텐츠를 감지하기 위한 샘플 코드를 보고, 탐색하고, 사용해 볼 수 있도록 합니다. 다음의 [빠른 시작 문서](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest)는 서비스에 요청을 보내는 방법을 안내합니다.

고려해야 할 또 다른 측면은 전체 애플리케이션 성능입니다. 멀티모달 및 멀티모델 애플리케이션에서는 시스템이 유해한 출력을 생성하지 않는 것을 포함하여 귀하와 사용자가 기대하는 방식대로 동작하는지를 성능으로 간주합니다. 전체 애플리케이션의 성능을 평가하려면 [성능 및 품질 및 위험 및 안전 평가자](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in)를 사용하여 평가하는 것이 중요합니다. 또한 [사용자 지정 평가자](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators)를 생성하고 평가할 수 있는 기능도 제공합니다.
개발 환경에서 [Azure AI 평가 SDK](https://microsoft.github.io/promptflow/index.html)를 사용하여 AI 애플리케이션을 평가할 수 있습니다. 테스트 데이터셋이나 목표 중 하나를 사용하면, 생성형 AI 애플리케이션의 생성물은 내장 평가자 또는 선택한 사용자 지정 평가자를 통해 정량적으로 측정됩니다. 시스템을 평가하기 위해 Azure AI Evaluation SDK를 시작하려면 [빠른 시작 가이드](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk)를 따라 하실 수 있습니다. 평가 실행을 수행하면 [Azure AI Foundry에서 결과를 시각화할 수 있습니다](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results). 

## 상표

이 프로젝트에는 프로젝트, 제품 또는 서비스의 상표나 로고가 포함되어 있을 수 있습니다. Microsoft 상표 또는 로고의 권한 있는 사용은 [Microsoft의 상표 및 브랜드 지침](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general)을 준수해야 합니다. 이 프로젝트의 수정된 버전에서 Microsoft 상표 또는 로고를 사용하는 경우 혼동을 초래하거나 Microsoft의 후원을 암시해서는 안 됩니다. 제3자 상표 또는 로고의 사용은 해당 제3자의 정책에 따릅니다.

## 도움 받기

AI 앱을 빌드하는 동안 막히거나 질문이 있는 경우, 다음에 참여하세요:

[![Azure AI Foundry 디스코드](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

제품에 대한 피드백이나 빌드 중 오류가 있는 경우 방문하세요:

[![Azure AI Foundry 개발자 포럼](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
면책 조항:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 기하기 위해 노력하고 있으나 자동 번역에는 오류나 부정확성이 있을 수 있습니다. 원문(원어) 문서를 권위 있는 자료로 간주해야 합니다. 중요한 정보의 경우 전문 번역가에 의한 번역을 권장합니다. 본 번역의 사용으로 인해 발생하는 모든 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->