<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1cab9282e04f2e1c388a38dca7763c16",
  "translation_date": "2025-05-09T04:03:47+00:00",
  "source_file": "README.md",
  "language_code": "vi"
}
-->
# Phi Cookbook: Ví dụ thực hành với các mô hình Phi của Microsoft

[![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)  
[![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)  
[![GitHub issues](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)  
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)  
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub watchers](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)  
[![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)  
[![GitHub stars](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Azure AI Community Discord](https://dcbadge.vercel.app/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

Phi là một chuỗi các mô hình AI mã nguồn mở được phát triển bởi Microsoft.

Phi hiện là mô hình ngôn ngữ nhỏ (SLM) mạnh mẽ và tiết kiệm chi phí nhất, với các điểm chuẩn rất tốt trong đa ngôn ngữ, suy luận, tạo văn bản/trò chuyện, lập trình, hình ảnh, âm thanh và nhiều kịch bản khác.

Bạn có thể triển khai Phi trên đám mây hoặc các thiết bị biên, và dễ dàng xây dựng các ứng dụng AI tạo sinh với nguồn lực tính toán hạn chế.

Làm theo các bước sau để bắt đầu sử dụng các tài nguyên này:  
1. **Fork Repository**: Nhấn [![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)  
2. **Clone Repository**: `git clone https://github.com/microsoft/PhiCookBook.git`  
3. [**Tham gia cộng đồng Microsoft AI Discord để gặp gỡ chuyên gia và các nhà phát triển khác**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/cover.2595d43b382944c601aebf88583314636768eece3d94e8e4448e03a4e5bedef4.vi.png)

## 🌐 Hỗ trợ đa ngôn ngữ

### Hỗ trợ qua GitHub Action (Tự động & Luôn cập nhật)

[French](../fr/README.md) | [Spanish](../es/README.md) | [German](../de/README.md) | [Russian](../ru/README.md) | [Arabic](../ar/README.md) | [Persian (Farsi)](../fa/README.md) | [Urdu](../ur/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Japanese](../ja/README.md) | [Korean](../ko/README.md) | [Hindi](../hi/README.md)

### Hỗ trợ qua CLI
[Bengali](../bn/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Portuguese (Brazil)](../br/README.md) | [Italian](../it/README.md) | [Polish](../pl/README.md) | [Turkish](../tr/README.md) | [Greek](../el/README.md) | [Thai](../th/README.md) | [Swedish](../sv/README.md) | [Danish](../da/README.md) | [Norwegian](../no/README.md) | [Finnish](../fi/README.md) | [Dutch](../nl/README.md) | [Hebrew](../he/README.md) | [Vietnamese](./README.md) | [Indonesian](../id/README.md) | [Malay](../ms/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Swahili](../sw/README.md) | [Hungarian](../hu/README.md) | [Czech](../cs/README.md) | [Slovak](../sk/README.md) | [Romanian](../ro/README.md) | [Bulgarian](../bg/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Croatian](../hr/README.md) | [Slovenian](../sl/README.md)


## Mục lục

- Giới thiệu
- [Chào mừng đến với Gia đình Phi](./md/01.Introduction/01/01.PhiFamily.md)
  - [Thiết lập môi trường của bạn](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [Hiểu về các công nghệ chính](./md/01.Introduction/01/01.Understandingtech.md)
  - [An toàn AI cho các mô hình Phi](./md/01.Introduction/01/01.AISafety.md)
  - [Hỗ trợ phần cứng Phi](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Mô hình Phi & Khả năng có mặt trên các nền tảng](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Sử dụng Guidance-ai và Phi](./md/01.Introduction/01/01.Guidance.md)
  - [Mô hình trên GitHub Marketplace](https://github.com/marketplace/models)
  - [Danh mục mô hình AI Azure](https://ai.azure.com)

- Inference Phi trong các môi trường khác nhau
    -  [Hugging face](./md/01.Introduction/02/01.HF.md)
    -  [Mô hình GitHub](./md/01.Introduction/02/02.GitHubModel.md)
    -  [Danh mục mô hình Azure AI Foundry](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [Bộ công cụ AI cho VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)

- Inference Phi Family
    - [Inference Phi trên iOS](./md/01.Introduction/03/iOS_Inference.md)
    - [Inference Phi trên Android](./md/01.Introduction/03/Android_Inference.md)
    - [Inference Phi trên Jetson](./md/01.Introduction/03/Jetson_Inference.md)
    - [Inference Phi trên AI PC](./md/01.Introduction/03/AIPC_Inference.md)
    - [Inference Phi với Apple MLX Framework](./md/01.Introduction/03/MLX_Inference.md)
    - [Inference Phi trên máy chủ cục bộ](./md/01.Introduction/03/Local_Server_Inference.md)
    - [Inference Phi trên máy chủ từ xa bằng AI Toolkit](./md/01.Introduction/03/Remote_Interence.md)
    - [Inference Phi với Rust](./md/01.Introduction/03/Rust_Inference.md)
    - [Inference Phi--Vision trên máy cục bộ](./md/01.Introduction/03/Vision_Inference.md)
    - [Inference Phi với Kaito AKS, Azure Containers (hỗ trợ chính thức)](./md/01.Introduction/03/Kaito_Inference.md)
-  [Định lượng Phi Family](./md/01.Introduction/04/QuantifyingPhi.md)
    - [Định lượng Phi-3.5 / 4 bằng llama.cpp](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [Định lượng Phi-3.5 / 4 bằng tiện ích AI tạo sinh cho onnxruntime](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Định lượng Phi-3.5 / 4 bằng Intel OpenVINO](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Định lượng Phi-3.5 / 4 bằng Apple MLX Framework](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

-  Đánh giá Phi
- [Response AI](./md/01.Introduction/05/ResponsibleAI.md)
    - [Azure AI Foundry cho Đánh giá](./md/01.Introduction/05/AIFoundry.md)
    - [Sử dụng Promptflow cho Đánh giá](./md/01.Introduction/05/Promptflow.md)
 
- RAG với Azure AI Search
    - [Cách sử dụng Phi-4-mini và Phi-4-multimodal(RAG) với Azure AI Search](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Mẫu phát triển ứng dụng Phi
  - Ứng dụng Văn bản & Chat
    - Mẫu Phi-4 🆕
      - [📓] [Chat với Phi-4-mini ONNX Model](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Chat với Phi-4 local ONNX Model .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Ứng dụng Console Chat .NET với Phi-4 ONNX sử dụng Semantic Kernel](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Mẫu Phi-3 / 3.5
      - [Chatbot cục bộ trên trình duyệt sử dụng Phi3, ONNX Runtime Web và WebGPU](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVino Chat](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [Multi Model - Tương tác Phi-3-mini và OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - Xây dựng wrapper và sử dụng Phi-3 với MLFlow](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [Tối ưu mô hình - Cách tối ưu Phi-3-mini cho ONNX Runtime Web với Olive](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [Ứng dụng WinUI3 với Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      - [Ứng dụng ghi chú đa mô hình WinUI3 AI Powered Sample](https://github.com/microsoft/ai-powered-notes-winui3-sample)
      - [Tinh chỉnh và tích hợp các mô hình Phi-3 tùy chỉnh với Prompt flow](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
      - [Tinh chỉnh và tích hợp các mô hình Phi-3 tùy chỉnh với Prompt flow trong Azure AI Foundry](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
      - [Đánh giá mô hình Phi-3 / Phi-3.5 đã tinh chỉnh trong Azure AI Foundry tập trung vào các nguyên tắc Responsible AI của Microsoft](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
      - [📓] [Mẫu dự đoán ngôn ngữ Phi-3.5-mini-instruct (Tiếng Trung/Anh)](../../md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
      - [Phi-3.5-Instruct WebGPU RAG Chatbot](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
      - [Sử dụng Windows GPU để tạo giải pháp Prompt flow với Phi-3.5-Instruct ONNX](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
      - [Sử dụng Microsoft Phi-3.5 tflite để tạo ứng dụng Android](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
      - [Ví dụ Hỏi & Đáp .NET sử dụng mô hình Phi-3 ONNX cục bộ với Microsoft.ML.OnnxRuntime](../../md/04.HOL/dotnet/src/LabsPhi301)
      - [Ứng dụng chat Console .NET với Semantic Kernel và Phi-3](../../md/04.HOL/dotnet/src/LabsPhi302)

  - Mẫu Dựa trên Mã SDK Azure AI Inference 
    - Mẫu Phi-4 🆕
      - [📓] [Tạo mã dự án sử dụng Phi-4-multimodal](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
    - Mẫu Phi-3 / 3.5
      - [Xây dựng Visual Studio Code GitHub Copilot Chat của riêng bạn với Microsoft Phi-3 Family](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
      - [Tạo Chat Copilot Agent cho Visual Studio Code của riêng bạn với Phi-3.5 bằng mô hình GitHub](./md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

  - Mẫu Lý luận Nâng cao
    - Mẫu Phi-4 🆕
      - [📓] [Mẫu Phi-4-mini-reasoning hoặc Phi-4-reasoning](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
      - [📓] [Tinh chỉnh Phi-4-mini-reasoning với Microsoft Olive](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Tinh chỉnh Phi-4-mini-reasoning với Apple MLX](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Phi-4-mini-reasoning với mô hình GitHub](../../md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
- [📓] [Phi-4-mini reasoning với Azure AI Foundry Models](../../md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
  - Demos
      - [Phi-4-mini demos được lưu trữ trên Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
      - [Phi-4-multimodal demos được lưu trữ trên Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
  - Ví dụ về Thị giác
    - Ví dụ Phi-4 🆕
      - [📓] [Sử dụng Phi-4-multimodal để đọc hình ảnh và tạo mã](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
    - Ví dụ Phi-3 / 3.5
      -  [📓][Phi-3-vision - Chuyển đổi văn bản hình ảnh thành văn bản](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
      - [📓][Phi-3-vision CLIP Embedding](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [DEMO: Phi-3 Recycling](https://github.com/jennifermarsman/PhiRecycling/)
      - [Phi-3-vision - Trợ lý ngôn ngữ hình ảnh - với Phi3-Vision và OpenVINO](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
      - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
      - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
      - [📓][Phi-3.5 Vision mẫu đa khung hình hoặc đa hình ảnh](../../md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
      - [Phi-3 Vision Local ONNX Model sử dụng Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi303)
      - [Menu dựa trên Phi-3 Vision Local ONNX Model sử dụng Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi304)

  - Ví dụ âm thanh
    - Ví dụ Phi-4 🆕
      - [📓] [Trích xuất bản ghi âm thanh bằng Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
      - [📓] [Ví dụ âm thanh Phi-4-multimodal](../../md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
      - [📓] [Ví dụ dịch nói Phi-4-multimodal](../../md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
      - [Ứng dụng console .NET sử dụng Phi-4-multimodal Audio để phân tích file âm thanh và tạo bản ghi](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

  - Ví dụ MOE
    - Ví dụ Phi-3 / 3.5
      - [📓] [Phi-3.5 Mixture of Experts Models (MoEs) ví dụ mạng xã hội](../../md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
      - [📓] [Xây dựng pipeline Retrieval-Augmented Generation (RAG) với NVIDIA NIM Phi-3 MOE, Azure AI Search và LlamaIndex](../../md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)
  - Ví dụ gọi hàm
    - Ví dụ Phi-4 🆕
      -  [📓] [Sử dụng Function Calling với Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
      -  [📓] [Sử dụng Function Calling để tạo đa tác nhân với Phi-4-mini](../../md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
      -  [📓] [Sử dụng Function Calling với Ollama](../../md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
  - Ví dụ kết hợp đa phương thức
    - Ví dụ Phi-4 🆕
      -  [📓] [Sử dụng Phi-4-multimodal như một nhà báo công nghệ](../../md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
      - [Ứng dụng console .NET sử dụng Phi-4-multimodal để phân tích hình ảnh](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Fine-tuning Phi Samples
  - [Các kịch bản Fine-tuning](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [Fine-tuning so với RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [Fine-tuning để Phi-3 trở thành chuyên gia ngành](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [Fine-tuning Phi-3 với AI Toolkit cho VS Code](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Fine-tuning Phi-3 với Azure Machine Learning Service](./md/03.FineTuning/Introduce_AzureML.md)
- [Tinh chỉnh Phi-3 với Lora](./md/03.FineTuning/FineTuning_Lora.md)
  - [Tinh chỉnh Phi-3 với QLora](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Tinh chỉnh Phi-3 với Azure AI Foundry](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Tinh chỉnh Phi-3 với Azure ML CLI/SDK](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Tinh chỉnh với Microsoft Olive](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Thực hành tinh chỉnh với Microsoft Olive Hands-On Lab](./md/03.FineTuning/olive-lab/readme.md)
  - [Tinh chỉnh Phi-3-vision với Weights and Bias](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [Tinh chỉnh Phi-3 với Apple MLX Framework](./md/03.FineTuning/FineTuning_MLX.md)
  - [Tinh chỉnh Phi-3-vision (hỗ trợ chính thức)](./md/03.FineTuning/FineTuning_Vision.md)
  - [Tinh chỉnh Phi-3 với Kaito AKS, Azure Containers (hỗ trợ chính thức)](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Tinh chỉnh Phi-3 và 3.5 Vision](https://github.com/2U1/Phi3-Vision-Finetune)

- Thực hành Lab
  - [Khám phá các mô hình tiên tiến: LLMs, SLMs, phát triển cục bộ và nhiều hơn nữa](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [Khai thác tiềm năng NLP: Tinh chỉnh với Microsoft Olive](https://github.com/azure/Ignite_FineTuning_workshop)

- Các bài báo nghiên cứu học thuật và ấn phẩm
  - [Textbooks Are All You Need II: báo cáo kỹ thuật phi-1.5](https://arxiv.org/abs/2309.05463)
  - [Báo cáo kỹ thuật Phi-3: Mô hình ngôn ngữ mạnh mẽ chạy cục bộ trên điện thoại của bạn](https://arxiv.org/abs/2404.14219)
  - [Báo cáo kỹ thuật Phi-4](https://arxiv.org/abs/2412.08905)
  - [Báo cáo kỹ thuật Phi-4-Mini: Mô hình ngôn ngữ đa phương tiện nhỏ gọn nhưng mạnh mẽ qua Mixture-of-LoRAs](https://arxiv.org/abs/2503.01743)
  - [Tối ưu hóa các mô hình ngôn ngữ nhỏ cho chức năng gọi trong xe](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) Tinh chỉnh PHI-3 cho trả lời câu hỏi trắc nghiệm: Phương pháp, kết quả và thách thức](https://arxiv.org/abs/2501.01588)
  - [Báo cáo kỹ thuật Phi-4-reasoning](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Báo cáo kỹ thuật Phi-4-mini-reasoning](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Sử dụng các mô hình Phi

### Phi trên Azure AI Foundry

Bạn có thể tìm hiểu cách sử dụng Microsoft Phi và cách xây dựng các giải pháp đầu-cuối trên các thiết bị phần cứng khác nhau của bạn. Để trải nghiệm Phi trực tiếp, hãy bắt đầu bằng việc thử nghiệm với các mô hình và tùy chỉnh Phi cho các kịch bản của bạn thông qua [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai). Bạn có thể tìm hiểu thêm tại Hướng dẫn bắt đầu với [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md)

**Playground**  
Mỗi mô hình đều có một khu vực thử nghiệm riêng để kiểm tra mô hình tại [Azure AI Playground](https://aka.ms/try-phi3).

### Phi trên GitHub Models

Bạn có thể học cách sử dụng Microsoft Phi và xây dựng các giải pháp đầu-cuối trên các thiết bị phần cứng khác nhau. Để trải nghiệm Phi trực tiếp, hãy thử chơi với mô hình và tùy chỉnh Phi cho các kịch bản của bạn bằng cách sử dụng [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo). Bạn có thể tìm hiểu thêm tại Hướng dẫn bắt đầu với [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md)

**Playground**  
Mỗi mô hình đều có một [khu vực thử nghiệm riêng để kiểm tra mô hình](/md/02.QuickStart/GitHubModel_QuickStart.md).

### Phi trên Hugging Face

Bạn cũng có thể tìm thấy mô hình trên [Hugging Face](https://huggingface.co/microsoft)

**Playground**  
 [Khu vực thử nghiệm Hugging Chat](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## Trách nhiệm AI

Microsoft cam kết giúp khách hàng sử dụng các sản phẩm AI một cách có trách nhiệm, chia sẻ kinh nghiệm và xây dựng các mối quan hệ đối tác dựa trên sự tin tưởng thông qua các công cụ như Transparency Notes và Impact Assessments. Nhiều tài nguyên này có thể được tìm thấy tại [https://aka.ms/RAI](https://aka.ms/RAI).  
Phương pháp tiếp cận trách nhiệm AI của Microsoft dựa trên các nguyên tắc AI về công bằng, độ tin cậy và an toàn, quyền riêng tư và bảo mật, tính bao trùm, minh bạch và trách nhiệm.
Các mô hình ngôn ngữ tự nhiên, hình ảnh và giọng nói quy mô lớn - giống như những mô hình được sử dụng trong ví dụ này - có thể hoạt động theo những cách không công bằng, không đáng tin cậy hoặc gây phản cảm, từ đó gây ra những tác hại. Vui lòng tham khảo [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) để nắm rõ các rủi ro và giới hạn.

Cách tiếp cận được khuyến nghị để giảm thiểu các rủi ro này là tích hợp một hệ thống an toàn trong kiến trúc của bạn có khả năng phát hiện và ngăn chặn hành vi gây hại. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) cung cấp một lớp bảo vệ độc lập, có thể phát hiện nội dung do người dùng và AI tạo ra có tính chất gây hại trong các ứng dụng và dịch vụ. Azure AI Content Safety bao gồm các API văn bản và hình ảnh cho phép bạn phát hiện các tài liệu gây hại. Trong Azure AI Foundry, dịch vụ Content Safety cho phép bạn xem, khám phá và thử nghiệm mã mẫu để phát hiện nội dung gây hại trên nhiều loại hình khác nhau. Tài liệu [quickstart documentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) dưới đây sẽ hướng dẫn bạn cách gửi yêu cầu đến dịch vụ.

Một khía cạnh khác cần lưu ý là hiệu suất tổng thể của ứng dụng. Với các ứng dụng đa mô thức và đa mô hình, hiệu suất được hiểu là hệ thống hoạt động như bạn và người dùng mong đợi, bao gồm cả việc không tạo ra kết quả gây hại. Việc đánh giá hiệu suất tổng thể của ứng dụng là rất quan trọng và bạn có thể sử dụng [Performance and Quality and Risk and Safety evaluators](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) để làm điều này. Bạn cũng có thể tạo và đánh giá bằng các [custom evaluators](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators).

Bạn có thể đánh giá ứng dụng AI của mình trong môi trường phát triển bằng cách sử dụng [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html). Dựa trên bộ dữ liệu kiểm thử hoặc mục tiêu, các kết quả tạo ra bởi ứng dụng AI của bạn sẽ được đo lường định lượng thông qua các evaluator tích hợp sẵn hoặc evaluator tùy chỉnh theo lựa chọn. Để bắt đầu với azure ai evaluation sdk và đánh giá hệ thống của bạn, bạn có thể theo dõi [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Sau khi thực hiện một lần chạy đánh giá, bạn có thể [visualize the results in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Trademarks

Dự án này có thể chứa các nhãn hiệu hoặc logo của các dự án, sản phẩm hoặc dịch vụ. Việc sử dụng nhãn hiệu hoặc logo của Microsoft phải tuân theo và không được vi phạm [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general). Việc sử dụng nhãn hiệu hoặc logo của Microsoft trong các phiên bản chỉnh sửa của dự án này không được gây nhầm lẫn hoặc ngụ ý sự bảo trợ của Microsoft. Mọi việc sử dụng nhãn hiệu hoặc logo của bên thứ ba phải tuân theo chính sách của bên thứ ba đó.

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ nguyên bản nên được coi là nguồn chính thức. Đối với thông tin quan trọng, khuyến nghị sử dụng dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm đối với bất kỳ sự hiểu lầm hay diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.