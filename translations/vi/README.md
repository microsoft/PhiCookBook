<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a73c59eecd7ad4ec494fd4333a29e208",
  "translation_date": "2025-10-11T11:10:10+00:00",
  "source_file": "README.md",
  "language_code": "vi"
}
-->
# Phi Cookbook: Ví dụ thực hành với các mô hình Phi của Microsoft

[![Mở và sử dụng các mẫu trong GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Mở trong Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![Những người đóng góp trên GitHub](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![Vấn đề trên GitHub](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![Yêu cầu kéo trên GitHub](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![Chào mừng PRs](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![Người theo dõi trên GitHub](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![Fork trên GitHub](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![Sao trên GitHub](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi là một loạt các mô hình AI mã nguồn mở được phát triển bởi Microsoft.

Phi hiện là mô hình ngôn ngữ nhỏ (SLM) mạnh mẽ và tiết kiệm chi phí nhất, với các kết quả đánh giá rất tốt trong đa ngôn ngữ, suy luận, tạo văn bản/chat, mã hóa, hình ảnh, âm thanh và các kịch bản khác.

Bạn có thể triển khai Phi lên đám mây hoặc các thiết bị biên, và dễ dàng xây dựng các ứng dụng AI tạo sinh với sức mạnh tính toán hạn chế.

Hãy làm theo các bước sau để bắt đầu sử dụng tài nguyên này:
1. **Fork kho lưu trữ**: Nhấn [![Fork trên GitHub](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **Clone kho lưu trữ**:   `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Tham gia cộng đồng Microsoft AI Discord và gặp gỡ các chuyên gia cùng các nhà phát triển khác**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../imgs/cover.png)

### 🌐 Hỗ trợ đa ngôn ngữ

#### Được hỗ trợ qua GitHub Action (Tự động & Luôn cập nhật)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../br/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](./README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## Mục lục

- Giới thiệu
  - [Chào mừng đến với gia đình Phi](./md/01.Introduction/01/01.PhiFamily.md)
  - [Thiết lập môi trường của bạn](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [Hiểu các công nghệ chính](./md/01.Introduction/01/01.Understandingtech.md)
  - [An toàn AI cho các mô hình Phi](./md/01.Introduction/01/01.AISafety.md)
  - [Hỗ trợ phần cứng cho Phi](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Các mô hình Phi & khả năng sử dụng trên các nền tảng](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Sử dụng Guidance-ai và Phi](./md/01.Introduction/01/01.Guidance.md)
  - [Các mô hình trên GitHub Marketplace](https://github.com/marketplace/models)
  - [Danh mục mô hình Azure AI](https://ai.azure.com)

- Suy luận Phi trong các môi trường khác nhau
    -  [Hugging face](./md/01.Introduction/02/01.HF.md)
    -  [Mô hình GitHub](./md/01.Introduction/02/02.GitHubModel.md)
    -  [Danh mục mô hình Azure AI Foundry](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    -  [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md)

- Suy luận gia đình Phi
    - [Suy luận Phi trên iOS](./md/01.Introduction/03/iOS_Inference.md)
    - [Suy luận Phi trên Android](./md/01.Introduction/03/Android_Inference.md)
    - [Suy luận Phi trên Jetson](./md/01.Introduction/03/Jetson_Inference.md)
    - [Suy luận Phi trên PC AI](./md/01.Introduction/03/AIPC_Inference.md)
    - [Suy luận Phi với Apple MLX Framework](./md/01.Introduction/03/MLX_Inference.md)
    - [Suy luận Phi trên máy chủ cục bộ](./md/01.Introduction/03/Local_Server_Inference.md)
    - [Suy luận Phi trên máy chủ từ xa bằng AI Toolkit](./md/01.Introduction/03/Remote_Interence.md)
    - [Suy luận Phi với Rust](./md/01.Introduction/03/Rust_Inference.md)
    - [Suy luận Phi--Vision trên cục bộ](./md/01.Introduction/03/Vision_Inference.md)
    - [Suy luận Phi với Kaito AKS, Azure Containers (hỗ trợ chính thức)](./md/01.Introduction/03/Kaito_Inference.md)
-  [Định lượng gia đình Phi](./md/01.Introduction/04/QuantifyingPhi.md)
    - [Định lượng Phi-3.5 / 4 bằng llama.cpp](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [Định lượng Phi-3.5 / 4 bằng các tiện ích mở rộng AI tạo sinh cho onnxruntime](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Định lượng Phi-3.5 / 4 bằng Intel OpenVINO](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Định lượng Phi-3.5 / 4 bằng Apple MLX Framework](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

-  Đánh giá Phi
    - [AI có trách nhiệm](./md/01.Introduction/05/ResponsibleAI.md)
    - [Azure AI Foundry để đánh giá](./md/01.Introduction/05/AIFoundry.md)
    - [Sử dụng Promptflow để đánh giá](./md/01.Introduction/05/Promptflow.md)
 
- RAG với Azure AI Search
    - [Cách sử dụng Phi-4-mini và Phi-4-multimodal (RAG) với Azure AI Search](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Mẫu phát triển ứng dụng Phi
  - Ứng dụng văn bản & chat
    - Mẫu Phi-4 🆕
      - [📓] [Chat với mô hình Phi-4-mini ONNX](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Chat với mô hình Phi-4 ONNX cục bộ .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Ứng dụng console .NET chat với Phi-4 ONNX sử dụng Semantic Kernel](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Mẫu Phi-3 / 3.5
      - [Chatbot cục bộ trong trình duyệt sử dụng Phi3, ONNX Runtime Web và WebGPU](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [Chat OpenVino](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [Mô hình đa - Tương tác Phi-3-mini và OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - Xây dựng một wrapper và sử dụng Phi-3 với MLFlow](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [Tối ưu hóa mô hình - Cách tối ưu hóa mô hình Phi-3-min cho ONNX Runtime Web với Olive](https://github.com/microsoft/Olive/tree/main/examples/phi3)
- [Ứng dụng WinUI3 với Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
- [Mẫu ứng dụng ghi chú AI đa mô hình WinUI3](https://github.com/microsoft/ai-powered-notes-winui3-sample)
- [Tùy chỉnh và tích hợp mô hình Phi-3 với Prompt flow](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
- [Tùy chỉnh và tích hợp mô hình Phi-3 với Prompt flow trong Azure AI Foundry](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
- [Đánh giá mô hình Phi-3 / Phi-3.5 đã được tùy chỉnh trong Azure AI Foundry tập trung vào các nguyên tắc AI có trách nhiệm của Microsoft](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
- [📓] [Mẫu dự đoán ngôn ngữ Phi-3.5-mini-instruct (Trung/Anh)](../../md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
- [Chatbot RAG WebGPU Phi-3.5-Instruct](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
- [Sử dụng GPU Windows để tạo giải pháp Prompt flow với Phi-3.5-Instruct ONNX](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
- [Sử dụng Microsoft Phi-3.5 tflite để tạo ứng dụng Android](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
- [Ví dụ Hỏi & Đáp .NET sử dụng mô hình ONNX Phi-3 cục bộ với Microsoft.ML.OnnxRuntime](../../md/04.HOL/dotnet/src/LabsPhi301)
- [Ứng dụng chat .NET console với Semantic Kernel và Phi-3](../../md/04.HOL/dotnet/src/LabsPhi302)

- Mẫu mã SDK suy luận Azure AI 
  - Mẫu Phi-4 🆕
    - [📓] [Tạo mã dự án sử dụng Phi-4-multimodal](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
  - Mẫu Phi-3 / 3.5
    - [Tự xây dựng Visual Studio Code GitHub Copilot Chat với Microsoft Phi-3 Family](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
    - [Tạo Visual Studio Code Chat Copilot Agent của riêng bạn với Phi-3.5 bằng các mô hình GitHub](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

- Mẫu lý luận nâng cao
  - Mẫu Phi-4 🆕
    - [📓] [Mẫu Phi-4-mini-reasoning hoặc Phi-4-reasoning](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
    - [📓] [Tùy chỉnh Phi-4-mini-reasoning với Microsoft Olive](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
    - [📓] [Tùy chỉnh Phi-4-mini-reasoning với Apple MLX](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
    - [📓] [Phi-4-mini-reasoning với các mô hình GitHub](../../md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
    - [📓] [Phi-4-mini-reasoning với các mô hình Azure AI Foundry](../../md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
- Demo
    - [Demo Phi-4-mini được lưu trữ trên Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
    - [Demo Phi-4-multimodal được lưu trữ trên Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
- Mẫu hình ảnh
  - Mẫu Phi-4 🆕
    - [📓] [Sử dụng Phi-4-multimodal để đọc hình ảnh và tạo mã](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
  - Mẫu Phi-3 / 3.5
    - [📓][Phi-3-vision-Image text to text](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
    - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
    - [📓][Phi-3-vision CLIP Embedding](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
    - [DEMO: Phi-3 Tái chế](https://github.com/jennifermarsman/PhiRecycling/)
    - [Phi-3-vision - Trợ lý ngôn ngữ hình ảnh - với Phi3-Vision và OpenVINO](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
    - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
    - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
    - [📓][Mẫu Phi-3.5 Vision đa khung hình hoặc đa hình ảnh](../../md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
    - [Mô hình ONNX cục bộ Phi-3 Vision sử dụng Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi303)
    - [Mô hình ONNX cục bộ Phi-3 Vision dựa trên menu sử dụng Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi304)

- Mẫu Toán học
  - Mẫu Phi-4-Mini-Flash-Reasoning-Instruct 🆕 [Demo Toán học với Phi-4-Mini-Flash-Reasoning-Instruct](../../md/02.Application/09.Math/MathDemo.ipynb)

- Mẫu Âm thanh
  - Mẫu Phi-4 🆕
    - [📓] [Trích xuất bản ghi âm thanh sử dụng Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
    - [📓] [Mẫu âm thanh Phi-4-multimodal](../../md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
    - [📓] [Mẫu dịch giọng nói Phi-4-multimodal](../../md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
    - [Ứng dụng console .NET sử dụng Phi-4-multimodal Audio để phân tích tệp âm thanh và tạo bản ghi](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

- Mẫu MOE
  - Mẫu Phi-3 / 3.5
    - [📓] [Mẫu mạng xã hội Phi-3.5 Mixture of Experts Models (MoEs)](../../md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
    - [📓] [Xây dựng Pipeline Tạo Nội dung Tăng cường Tìm kiếm (RAG) với NVIDIA NIM Phi-3 MOE, Azure AI Search và LlamaIndex](../../md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)

- Mẫu gọi hàm
  - Mẫu Phi-4 🆕
    - [📓] [Sử dụng Gọi hàm với Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
    - [📓] [Sử dụng Gọi hàm để tạo nhiều tác nhân với Phi-4-mini](../../md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
    - [📓] [Sử dụng Gọi hàm với Ollama](../../md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
    - [📓] [Sử dụng Gọi hàm với ONNX](../../md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)
- Mẫu trộn đa phương thức
  - Mẫu Phi-4 🆕
    - [📓] [Sử dụng Phi-4-multimodal như một nhà báo công nghệ](../../md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
    - [Ứng dụng console .NET sử dụng Phi-4-multimodal để phân tích hình ảnh](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Mẫu tùy chỉnh Phi
  - [Các kịch bản tùy chỉnh](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [Tùy chỉnh so với RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [Tùy chỉnh để Phi-3 trở thành chuyên gia ngành](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [Tùy chỉnh Phi-3 với AI Toolkit cho VS Code](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Tùy chỉnh Phi-3 với Azure Machine Learning Service](./md/03.FineTuning/Introduce_AzureML.md)
  - [Tùy chỉnh Phi-3 với Lora](./md/03.FineTuning/FineTuning_Lora.md)
  - [Tùy chỉnh Phi-3 với QLora](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Tùy chỉnh Phi-3 với Azure AI Foundry](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Tùy chỉnh Phi-3 với Azure ML CLI/SDK](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Tùy chỉnh với Microsoft Olive](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Thực hành tùy chỉnh với Microsoft Olive](./md/03.FineTuning/olive-lab/readme.md)
  - [Tùy chỉnh Phi-3-vision với Weights and Bias](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [Tùy chỉnh Phi-3 với Apple MLX Framework](./md/03.FineTuning/FineTuning_MLX.md)
  - [Tùy chỉnh Phi-3-vision (hỗ trợ chính thức)](./md/03.FineTuning/FineTuning_Vision.md)
  - [Tùy chỉnh Phi-3 với Kaito AKS, Azure Containers (hỗ trợ chính thức)](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Tùy chỉnh Phi-3 và 3.5 Vision](https://github.com/2U1/Phi3-Vision-Finetune)

- Phòng thí nghiệm thực hành
  - [Khám phá các mô hình tiên tiến: LLMs, SLMs, phát triển cục bộ và hơn thế nữa](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [Khai phá tiềm năng NLP: Tùy chỉnh với Microsoft Olive](https://github.com/azure/Ignite_FineTuning_workshop)

- Các bài báo nghiên cứu và ấn phẩm học thuật
  - [Textbooks Are All You Need II: báo cáo kỹ thuật phi-1.5](https://arxiv.org/abs/2309.05463)
  - [Báo cáo kỹ thuật Phi-3: Mô hình ngôn ngữ có khả năng cao trên điện thoại của bạn](https://arxiv.org/abs/2404.14219)
  - [Báo cáo kỹ thuật Phi-4](https://arxiv.org/abs/2412.08905)
  - [Báo cáo kỹ thuật Phi-4-Mini: Mô hình ngôn ngữ đa phương thức nhỏ gọn nhưng mạnh mẽ qua Mixture-of-LoRAs](https://arxiv.org/abs/2503.01743)
  - [Tối ưu hóa các mô hình ngôn ngữ nhỏ cho việc gọi chức năng trong xe](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) Tinh chỉnh PHI-3 cho trả lời câu hỏi trắc nghiệm: Phương pháp, Kết quả và Thách thức](https://arxiv.org/abs/2501.01588)
  - [Báo cáo kỹ thuật Phi-4-reasoning](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Báo cáo kỹ thuật Phi-4-mini-reasoning](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Sử dụng các mô hình Phi

### Phi trên Azure AI Foundry

Bạn có thể tìm hiểu cách sử dụng Microsoft Phi và cách xây dựng các giải pháp E2E trên các thiết bị phần cứng khác nhau. Để trải nghiệm Phi, hãy bắt đầu bằng cách thử nghiệm các mô hình và tùy chỉnh Phi cho các tình huống của bạn thông qua [Danh mục Mô hình Azure AI Foundry](https://aka.ms/phi3-azure-ai). Bạn có thể tìm hiểu thêm tại phần Bắt đầu với [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md).

**Playground**  
Mỗi mô hình đều có một playground riêng để thử nghiệm mô hình [Azure AI Playground](https://aka.ms/try-phi3).

### Phi trên GitHub Models

Bạn có thể tìm hiểu cách sử dụng Microsoft Phi và cách xây dựng các giải pháp E2E trên các thiết bị phần cứng khác nhau. Để trải nghiệm Phi, hãy bắt đầu bằng cách thử nghiệm mô hình và tùy chỉnh Phi cho các tình huống của bạn thông qua [Danh mục Mô hình GitHub](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo). Bạn có thể tìm hiểu thêm tại phần Bắt đầu với [Danh mục Mô hình GitHub](/md/02.QuickStart/GitHubModel_QuickStart.md).

**Playground**  
Mỗi mô hình đều có một [playground riêng để thử nghiệm mô hình](/md/02.QuickStart/GitHubModel_QuickStart.md).

### Phi trên Hugging Face

Bạn cũng có thể tìm thấy mô hình trên [Hugging Face](https://huggingface.co/microsoft).

**Playground**  
[Playground Hugging Chat](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## AI có trách nhiệm

Microsoft cam kết giúp khách hàng sử dụng các sản phẩm AI của chúng tôi một cách có trách nhiệm, chia sẻ những bài học kinh nghiệm và xây dựng các mối quan hệ đối tác dựa trên sự tin tưởng thông qua các công cụ như Ghi chú Minh bạch và Đánh giá Tác động. Nhiều tài nguyên này có thể được tìm thấy tại [https://aka.ms/RAI](https://aka.ms/RAI).  
Cách tiếp cận của Microsoft đối với AI có trách nhiệm dựa trên các nguyên tắc AI của chúng tôi: công bằng, đáng tin cậy và an toàn, quyền riêng tư và bảo mật, tính bao gồm, minh bạch và trách nhiệm.

Các mô hình ngôn ngữ, hình ảnh và giọng nói quy mô lớn - như những mô hình được sử dụng trong ví dụ này - có thể hành xử theo cách không công bằng, không đáng tin cậy hoặc gây xúc phạm, dẫn đến những tác hại. Vui lòng tham khảo [Ghi chú Minh bạch của dịch vụ Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) để được thông tin về các rủi ro và hạn chế.

Cách tiếp cận được khuyến nghị để giảm thiểu những rủi ro này là bao gồm một hệ thống an toàn trong kiến trúc của bạn có thể phát hiện và ngăn chặn hành vi gây hại. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) cung cấp một lớp bảo vệ độc lập, có khả năng phát hiện nội dung do người dùng và AI tạo ra có hại trong các ứng dụng và dịch vụ. Azure AI Content Safety bao gồm các API văn bản và hình ảnh cho phép bạn phát hiện nội dung có hại. Trong Azure AI Foundry, dịch vụ Content Safety cho phép bạn xem, khám phá và thử nghiệm mã mẫu để phát hiện nội dung có hại trên các phương thức khác nhau. Tài liệu [hướng dẫn nhanh](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) sau đây sẽ hướng dẫn bạn cách gửi yêu cầu đến dịch vụ.

Một khía cạnh khác cần xem xét là hiệu suất tổng thể của ứng dụng. Với các ứng dụng đa phương thức và đa mô hình, chúng tôi coi hiệu suất là việc hệ thống hoạt động như bạn và người dùng mong đợi, bao gồm không tạo ra các đầu ra có hại. Điều quan trọng là đánh giá hiệu suất của ứng dụng tổng thể của bạn bằng cách sử dụng [các công cụ đánh giá Hiệu suất và Chất lượng, Rủi ro và An toàn](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in). Bạn cũng có thể tạo và đánh giá bằng [các công cụ đánh giá tùy chỉnh](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators).

Bạn có thể đánh giá ứng dụng AI của mình trong môi trường phát triển bằng [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html). Với một tập dữ liệu kiểm tra hoặc mục tiêu, các kết quả tạo ra từ ứng dụng AI của bạn được đo lường định lượng bằng các công cụ đánh giá tích hợp hoặc tùy chỉnh mà bạn chọn. Để bắt đầu với Azure AI Evaluation SDK để đánh giá hệ thống của bạn, bạn có thể làm theo [hướng dẫn nhanh](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Sau khi thực hiện một lần đánh giá, bạn có thể [hình dung kết quả trong Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Thương hiệu

Dự án này có thể chứa các thương hiệu hoặc logo cho các dự án, sản phẩm hoặc dịch vụ. Việc sử dụng hợp pháp các thương hiệu hoặc logo của Microsoft phải tuân theo và tuân thủ [Hướng dẫn về Thương hiệu & Nhãn hiệu của Microsoft](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).  
Việc sử dụng các thương hiệu hoặc logo của Microsoft trong các phiên bản sửa đổi của dự án này không được gây nhầm lẫn hoặc ngụ ý rằng Microsoft tài trợ. Việc sử dụng các thương hiệu hoặc logo của bên thứ ba phải tuân theo chính sách của bên thứ ba đó.

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.