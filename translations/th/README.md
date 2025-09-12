<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "698f7f3d48ebc9e25a273d7c8b7e31c5",
  "translation_date": "2025-09-12T13:52:34+00:00",
  "source_file": "README.md",
  "language_code": "th"
}
-->
# Phi Cookbook: ตัวอย่างการใช้งานจริงกับโมเดล Phi ของ Microsoft

Phi เป็นชุดโมเดล AI แบบโอเพ่นซอร์สที่พัฒนาโดย Microsoft

Phi เป็นโมเดลภาษาขนาดเล็ก (SLM) ที่ทรงพลังและคุ้มค่าที่สุดในปัจจุบัน โดยมีผลการทดสอบที่ยอดเยี่ยมในหลายภาษา การให้เหตุผล การสร้างข้อความ/แชท การเขียนโค้ด ภาพ เสียง และสถานการณ์อื่น ๆ

คุณสามารถปรับใช้ Phi บนคลาวด์หรืออุปกรณ์ปลายทาง และสามารถสร้างแอปพลิเคชัน AI เชิงสร้างสรรค์ได้ง่าย ๆ แม้มีทรัพยากรการประมวลผลจำกัด

ทำตามขั้นตอนเหล่านี้เพื่อเริ่มต้นใช้งานทรัพยากรเหล่านี้:
1. **Fork Repository**: คลิก [![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **Clone Repository**: `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**เข้าร่วมชุมชน Microsoft AI Discord และพบกับผู้เชี่ยวชาญและนักพัฒนาท่านอื่น**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../imgs/cover.png)

### 🌐 รองรับหลายภาษา

#### รองรับผ่าน GitHub Action (อัตโนมัติและอัปเดตเสมอ)

[French](../fr/README.md) | [Spanish](../es/README.md) | [German](../de/README.md) | [Russian](../ru/README.md) | [Arabic](../ar/README.md) | [Persian (Farsi)](../fa/README.md) | [Urdu](../ur/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Japanese](../ja/README.md) | [Korean](../ko/README.md) | [Hindi](../hi/README.md) 
[Bengali](../bn/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Portuguese (Brazil)](../br/README.md) | [Italian](../it/README.md) | [Polish](../pl/README.md) | [Turkish](../tr/README.md) | [Greek](../el/README.md) | [Thai](./README.md) | [Swedish](../sv/README.md) | [Danish](../da/README.md) | [Norwegian](../no/README.md) | [Finnish](../fi/README.md) | [Dutch](../nl/README.md) | [Hebrew](../he/README.md) | [Vietnamese](../vi/README.md) | [Indonesian](../id/README.md) | [Malay](../ms/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Swahili](../sw/README.md) | [Hungarian](../hu/README.md) | [Czech](../cs/README.md) | [Slovak](../sk/README.md) | [Romanian](../ro/README.md) | [Bulgarian](../bg/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Croatian](../hr/README.md) | [Slovenian](../sl/README.md)

## สารบัญ

- บทนำ
  - [ยินดีต้อนรับสู่ครอบครัว Phi](./md/01.Introduction/01/01.PhiFamily.md)
  - [การตั้งค่าสภาพแวดล้อมของคุณ](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [ทำความเข้าใจเทคโนโลยีสำคัญ](./md/01.Introduction/01/01.Understandingtech.md)
  - [ความปลอดภัยของ AI สำหรับโมเดล Phi](./md/01.Introduction/01/01.AISafety.md)
  - [การสนับสนุนฮาร์ดแวร์ของ Phi](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [โมเดล Phi และความพร้อมใช้งานในแพลตฟอร์มต่าง ๆ](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [การใช้งาน Guidance-ai และ Phi](./md/01.Introduction/01/01.Guidance.md)
  - [โมเดลใน GitHub Marketplace](https://github.com/marketplace/models)
  - [Azure AI Model Catalog](https://ai.azure.com)

- การใช้งาน Phi ในสภาพแวดล้อมต่าง ๆ
    - [Hugging face](./md/01.Introduction/02/01.HF.md)
    - [โมเดลใน GitHub](./md/01.Introduction/02/02.GitHubModel.md)
    - [Azure AI Foundry Model Catalog](./md/01.Introduction/02/03.AzureAIFoundry.md)
    - [Ollama](./md/01.Introduction/02/04.Ollama.md)
    - [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    - [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    - [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md)

- การใช้งาน Phi Family
    - [การใช้งาน Phi ใน iOS](./md/01.Introduction/03/iOS_Inference.md)
    - [การใช้งาน Phi ใน Android](./md/01.Introduction/03/Android_Inference.md)
    - [การใช้งาน Phi ใน Jetson](./md/01.Introduction/03/Jetson_Inference.md)
    - [การใช้งาน Phi ใน AI PC](./md/01.Introduction/03/AIPC_Inference.md)
    - [การใช้งาน Phi กับ Apple MLX Framework](./md/01.Introduction/03/MLX_Inference.md)
    - [การใช้งาน Phi ในเซิร์ฟเวอร์ท้องถิ่น](./md/01.Introduction/03/Local_Server_Inference.md)
    - [การใช้งาน Phi ในเซิร์ฟเวอร์ระยะไกลด้วย AI Toolkit](./md/01.Introduction/03/Remote_Interence.md)
    - [การใช้งาน Phi กับ Rust](./md/01.Introduction/03/Rust_Inference.md)
    - [การใช้งาน Phi--Vision ในท้องถิ่น](./md/01.Introduction/03/Vision_Inference.md)
    - [การใช้งาน Phi กับ Kaito AKS, Azure Containers (การสนับสนุนอย่างเป็นทางการ)](./md/01.Introduction/03/Kaito_Inference.md)

- [การปรับขนาด Phi Family](./md/01.Introduction/04/QuantifyingPhi.md)
    - [การปรับขนาด Phi-3.5 / 4 ด้วย llama.cpp](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [การปรับขนาด Phi-3.5 / 4 ด้วย Generative AI extensions สำหรับ onnxruntime](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [การปรับขนาด Phi-3.5 / 4 ด้วย Intel OpenVINO](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [การปรับขนาด Phi-3.5 / 4 ด้วย Apple MLX Framework](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

- การประเมิน Phi
    - [AI ที่รับผิดชอบ](./md/01.Introduction/05/ResponsibleAI.md)
    - [Azure AI Foundry สำหรับการประเมินผล](./md/01.Introduction/05/AIFoundry.md)
    - [การใช้ Promptflow สำหรับการประเมินผล](./md/01.Introduction/05/Promptflow.md)

- RAG กับ Azure AI Search
    - [วิธีการใช้ Phi-4-mini และ Phi-4-multimodal (RAG) กับ Azure AI Search](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- ตัวอย่างการพัฒนาแอปพลิเคชัน Phi
  - แอปพลิเคชันข้อความและแชท
    - ตัวอย่าง Phi-4 🆕
      - [📓] [แชทกับ Phi-4-mini ONNX Model](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [แชทกับ Phi-4 local ONNX Model .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [แชท .NET Console App กับ Phi-4 ONNX โดยใช้ Semantic Kernel](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - ตัวอย่าง Phi-3 / 3.5
      - [แชทบอทในเบราว์เซอร์โดยใช้ Phi3, ONNX Runtime Web และ WebGPU](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVino Chat](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [โมเดลหลายตัว - Phi-3-mini และ OpenAI Whisper แบบโต้ตอบ](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - การสร้าง wrapper และการใช้ Phi-3 กับ MLFlow](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [การปรับแต่งโมเดล - วิธีการปรับแต่ง Phi-3-min model สำหรับ ONNX Runtime Web ด้วย Olive](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [แอป WinUI3 กับ Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      - [แอปบันทึก AI Powered Notes ตัวอย่าง WinUI3](https://github.com/microsoft/ai-powered-notes-winui3-sample)
- [ปรับแต่งและผสานรวมโมเดล Phi-3 แบบกำหนดเองกับ Prompt flow](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)  
- [ปรับแต่งและผสานรวมโมเดล Phi-3 แบบกำหนดเองกับ Prompt flow ใน Azure AI Foundry](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)  
- [ประเมินโมเดล Phi-3 / Phi-3.5 ที่ปรับแต่งใน Azure AI Foundry โดยเน้นหลักการ AI ที่รับผิดชอบของ Microsoft](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)  
- [📓] [ตัวอย่างการทำนายภาษา Phi-3.5-mini-instruct (จีน/อังกฤษ)](../../md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)  
- [Phi-3.5-Instruct WebGPU RAG Chatbot](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)  
- [ใช้ Windows GPU เพื่อสร้างโซลูชัน Prompt flow ด้วย Phi-3.5-Instruct ONNX](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)  
- [ใช้ Microsoft Phi-3.5 tflite เพื่อสร้างแอป Android](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)  
- [ตัวอย่าง Q&A .NET โดยใช้โมเดล Phi-3 แบบ ONNX ในเครื่องผ่าน Microsoft.ML.OnnxRuntime](../../md/04.HOL/dotnet/src/LabsPhi301)  
- [แอปแชทคอนโซล .NET พร้อม Semantic Kernel และ Phi-3](../../md/04.HOL/dotnet/src/LabsPhi302)  

- ตัวอย่างโค้ด Azure AI Inference SDK  
  - ตัวอย่าง Phi-4 🆕  
    - [📓] [สร้างโค้ดโปรเจกต์โดยใช้ Phi-4-multimodal](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)  
  - ตัวอย่าง Phi-3 / 3.5  
    - [สร้าง Visual Studio Code GitHub Copilot Chat ของคุณเองด้วย Microsoft Phi-3 Family](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)  
    - [สร้าง Visual Studio Code Chat Copilot Agent ของคุณเองด้วย Phi-3.5 โดยใช้โมเดล GitHub](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)  

- ตัวอย่างการให้เหตุผลขั้นสูง  
  - ตัวอย่าง Phi-4 🆕  
    - [📓] [ตัวอย่าง Phi-4-mini-reasoning หรือ Phi-4-reasoning](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)  
    - [📓] [ปรับแต่ง Phi-4-mini-reasoning ด้วย Microsoft Olive](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)  
    - [📓] [ปรับแต่ง Phi-4-mini-reasoning ด้วย Apple MLX](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)  
    - [📓] [Phi-4-mini-reasoning ด้วยโมเดล GitHub](../../md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)  
    - [📓] [Phi-4-mini-reasoning ด้วยโมเดล Azure AI Foundry](../../md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)  
- เดโม  
    - [เดโม Phi-4-mini บน Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)  
    - [เดโม Phi-4-multimodal บน Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)  
- ตัวอย่าง Vision  
  - ตัวอย่าง Phi-4 🆕  
    - [📓] [ใช้ Phi-4-multimodal เพื่ออ่านภาพและสร้างโค้ด](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md)  
  - ตัวอย่าง Phi-3 / 3.5  
    - [📓][Phi-3-vision-Image text to text](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)  
    - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)  
    - [📓][Phi-3-vision CLIP Embedding](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)  
    - [DEMO: Phi-3 Recycling](https://github.com/jennifermarsman/PhiRecycling/)  
    - [Phi-3-vision - ผู้ช่วยด้านภาษาภาพ - ด้วย Phi3-Vision และ OpenVINO](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)  
    - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)  
    - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)  
    - [📓][Phi-3.5 Vision ตัวอย่างหลายเฟรมหรือหลายภาพ](../../md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)  
    - [Phi-3 Vision โมเดล ONNX ในเครื่องโดยใช้ Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi303)  
    - [Phi-3 Vision โมเดล ONNX ในเครื่องแบบเมนูโดยใช้ Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi304)  

- ตัวอย่าง Math  
  - ตัวอย่าง Phi-4-Mini-Flash-Reasoning-Instruct 🆕 [เดโม Math ด้วย Phi-4-Mini-Flash-Reasoning-Instruct](../../md/02.Application/09.Math/MathDemo.ipynb)  

- ตัวอย่าง Audio  
  - ตัวอย่าง Phi-4 🆕  
    - [📓] [การดึงถอดเสียงจากเสียงด้วย Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Transciption/README.md)  
    - [📓] [ตัวอย่างเสียง Phi-4-multimodal](../../md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)  
    - [📓] [ตัวอย่างการแปลเสียง Phi-4-multimodal](../../md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)  
    - [แอปคอนโซล .NET โดยใช้ Phi-4-multimodal เพื่อวิเคราะห์ไฟล์เสียงและสร้างถอดเสียง](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)  

- ตัวอย่าง MOE  
  - ตัวอย่าง Phi-3 / 3.5  
    - [📓] [Phi-3.5 Mixture of Experts Models (MoEs) ตัวอย่างโซเชียลมีเดีย](../../md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)  
    - [📓] [สร้าง Retrieval-Augmented Generation (RAG) Pipeline ด้วย NVIDIA NIM Phi-3 MOE, Azure AI Search และ LlamaIndex](../../md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)  

- ตัวอย่าง Function Calling  
  - ตัวอย่าง Phi-4 🆕  
    - [📓] [การใช้ Function Calling กับ Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)  
    - [📓] [การใช้ Function Calling เพื่อสร้าง multi-agents ด้วย Phi-4-mini](../../md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)  
    - [📓] [การใช้ Function Calling กับ Ollama](../../md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)  
    - [📓] [การใช้ Function Calling กับ ONNX](../../md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)  

- ตัวอย่าง Multimodal Mixing  
  - ตัวอย่าง Phi-4 🆕  
    - [📓] [การใช้ Phi-4-multimodal ในฐานะนักข่าวเทคโนโลยี](../../md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)  
    - [แอปคอนโซล .NET โดยใช้ Phi-4-multimodal เพื่อวิเคราะห์ภาพ](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)  

- ตัวอย่างการปรับแต่ง Phi  
  - [สถานการณ์การปรับแต่ง](./md/03.FineTuning/FineTuning_Scenarios.md)  
  - [การปรับแต่ง vs RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)  
  - [การปรับแต่งเพื่อให้ Phi-3 กลายเป็นผู้เชี่ยวชาญในอุตสาหกรรม](./md/03.FineTuning/LetPhi3gotoIndustriy.md)  
  - [การปรับแต่ง Phi-3 ด้วย AI Toolkit สำหรับ VS Code](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)  
  - [การปรับแต่ง Phi-3 ด้วย Azure Machine Learning Service](./md/03.FineTuning/Introduce_AzureML.md)  
  - [การปรับแต่ง Phi-3 ด้วย Lora](./md/03.FineTuning/FineTuning_Lora.md)  
  - [การปรับแต่ง Phi-3 ด้วย QLora](./md/03.FineTuning/FineTuning_Qlora.md)  
  - [การปรับแต่ง Phi-3 ด้วย Azure AI Foundry](./md/03.FineTuning/FineTuning_AIFoundry.md)  
  - [การปรับแต่ง Phi-3 ด้วย Azure ML CLI/SDK](./md/03.FineTuning/FineTuning_MLSDK.md)  
  - [การปรับแต่งด้วย Microsoft Olive](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)  
  - [การปรับแต่งด้วย Microsoft Olive Hands-On Lab](./md/03.FineTuning/olive-lab/readme.md)  
  - [การปรับแต่ง Phi-3-vision ด้วย Weights and Bias](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)  
  - [การปรับแต่ง Phi-3 ด้วย Apple MLX Framework](./md/03.FineTuning/FineTuning_MLX.md)  
  - [การปรับแต่ง Phi-3-vision (การสนับสนุนอย่างเป็นทางการ)](./md/03.FineTuning/FineTuning_Vision.md)  
  - [การปรับแต่ง Phi-3 ด้วย Kaito AKS, Azure Containers (การสนับสนุนอย่างเป็นทางการ)](./md/03.FineTuning/FineTuning_Kaito.md)  
  - [การปรับแต่ง Phi-3 และ 3.5 Vision](https://github.com/2U1/Phi3-Vision-Finetune)  

- Hands on Lab  
  - [สำรวจโมเดลล้ำสมัย: LLMs, SLMs, การพัฒนาในเครื่อง และอื่น ๆ](https://github.com/microsoft/aitour-exploring-cutting-edge-models)  
  - [ปลดล็อกศักยภาพ NLP: การปรับแต่งด้วย Microsoft Olive](https://github.com/azure/Ignite_FineTuning_workshop)  

- งานวิจัยและสิ่งพิมพ์ทางวิชาการ  
  - [Textbooks Are All You Need II: รายงานทางเทคนิค phi-1.5](https://arxiv.org/abs/2309.05463)  
  - [รายงานทางเทคนิค Phi-3: โมเดลภาษาที่มีความสามารถสูงในโทรศัพท์ของคุณ](https://arxiv.org/abs/2404.14219)  
  - [รายงานทางเทคนิค Phi-4](https://arxiv.org/abs/2412.08905)  
  - [รายงานทางเทคนิค Phi-4-Mini: โมเดลภาษามัลติโหมดที่กะทัดรัดแต่ทรงพลังผ่าน Mixture-of-LoRAs](https://arxiv.org/abs/2503.01743)  
  - [การปรับแต่งโมเดลภาษาขนาดเล็กสำหรับการเรียกฟังก์ชันในยานพาหนะ](https://arxiv.org/abs/2501.02342)  
  - [(WhyPHI) การปรับแต่ง PHI-3 สำหรับการตอบคำถามแบบเลือกหลายข้อ: วิธีการ, ผลลัพธ์ และความท้าทาย](https://arxiv.org/abs/2501.01588)  
- [Phi-4-reasoning Technical Report](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)  
- [Phi-4-mini-reasoning Technical Report](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)  

## การใช้งานโมเดล Phi  

### Phi บน Azure AI Foundry  

คุณสามารถเรียนรู้วิธีการใช้งาน Microsoft Phi และวิธีการสร้างโซลูชันแบบ E2E บนอุปกรณ์ฮาร์ดแวร์ต่าง ๆ ของคุณ เพื่อสัมผัสประสบการณ์การใช้งาน Phi ด้วยตัวคุณเอง เริ่มต้นด้วยการทดลองใช้งานโมเดลและปรับแต่ง Phi ให้เหมาะสมกับสถานการณ์ของคุณผ่าน [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai) คุณสามารถเรียนรู้เพิ่มเติมได้ที่ [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md)  

**Playground**  
แต่ละโมเดลมีพื้นที่ทดลองใช้งานเฉพาะ [Azure AI Playground](https://aka.ms/try-phi3)  

### Phi บน GitHub Models  

คุณสามารถเรียนรู้วิธีการใช้งาน Microsoft Phi และวิธีการสร้างโซลูชันแบบ E2E บนอุปกรณ์ฮาร์ดแวร์ต่าง ๆ ของคุณ เพื่อสัมผัสประสบการณ์การใช้งาน Phi ด้วยตัวคุณเอง เริ่มต้นด้วยการทดลองใช้งานโมเดลและปรับแต่ง Phi ให้เหมาะสมกับสถานการณ์ของคุณผ่าน [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) คุณสามารถเรียนรู้เพิ่มเติมได้ที่ [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md)  

**Playground**  
แต่ละโมเดลมีพื้นที่ [ทดลองใช้งานโมเดล](/md/02.QuickStart/GitHubModel_QuickStart.md)  

### Phi บน Hugging Face  

คุณสามารถค้นหาโมเดลได้ที่ [Hugging Face](https://huggingface.co/microsoft)  

**Playground**  
[Hugging Chat playground](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)  

## AI ที่รับผิดชอบ  

Microsoft มุ่งมั่นที่จะช่วยลูกค้าใช้งานผลิตภัณฑ์ AI ของเราอย่างมีความรับผิดชอบ แบ่งปันสิ่งที่เราเรียนรู้ และสร้างความไว้วางใจผ่านเครื่องมือ เช่น Transparency Notes และ Impact Assessments ทรัพยากรเหล่านี้สามารถพบได้ที่ [https://aka.ms/RAI](https://aka.ms/RAI)  
แนวทางของ Microsoft ในการพัฒนา AI ที่รับผิดชอบนั้นยึดหลักการ AI ของเรา ได้แก่ ความเป็นธรรม ความน่าเชื่อถือและความปลอดภัย ความเป็นส่วนตัวและความปลอดภัย ความครอบคลุม ความโปร่งใส และความรับผิดชอบ  

โมเดลขนาดใหญ่สำหรับภาษาธรรมชาติ รูปภาพ และเสียง - เช่นเดียวกับที่ใช้ในตัวอย่างนี้ - อาจมีพฤติกรรมที่ไม่เป็นธรรม ไม่เชื่อถือได้ หรือไม่เหมาะสม ซึ่งอาจก่อให้เกิดความเสียหายได้ โปรดศึกษาข้อมูลเพิ่มเติมใน [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) เพื่อรับทราบถึงความเสี่ยงและข้อจำกัด  

วิธีการที่แนะนำในการลดความเสี่ยงเหล่านี้คือการรวมระบบความปลอดภัยในสถาปัตยกรรมของคุณที่สามารถตรวจจับและป้องกันพฤติกรรมที่เป็นอันตราย [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) ให้การป้องกันในระดับอิสระ สามารถตรวจจับเนื้อหาที่เป็นอันตรายที่สร้างโดยผู้ใช้หรือ AI ในแอปพลิเคชันและบริการ Azure AI Content Safety มี API สำหรับข้อความและรูปภาพที่ช่วยให้คุณตรวจจับเนื้อหาที่เป็นอันตรายได้ ภายใน Azure AI Foundry บริการ Content Safety ช่วยให้คุณดู สำรวจ และทดลองใช้โค้ดตัวอย่างสำหรับการตรวจจับเนื้อหาที่เป็นอันตรายในหลายรูปแบบ เอกสาร [quickstart](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) นี้จะแนะนำวิธีการส่งคำขอไปยังบริการ  

อีกแง่มุมหนึ่งที่ควรพิจารณาคือประสิทธิภาพโดยรวมของแอปพลิเคชัน ด้วยแอปพลิเคชันที่มีหลายรูปแบบและหลายโมเดล เราถือว่าประสิทธิภาพหมายถึงระบบทำงานตามที่คุณและผู้ใช้คาดหวัง รวมถึงไม่สร้างผลลัพธ์ที่เป็นอันตราย การประเมินประสิทธิภาพของแอปพลิเคชันโดยรวมของคุณเป็นสิ่งสำคัญ โดยใช้ [Performance and Quality and Risk and Safety evaluators](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) คุณยังสามารถสร้างและประเมินด้วย [custom evaluators](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators)  

คุณสามารถประเมินแอปพลิเคชัน AI ของคุณในสภาพแวดล้อมการพัฒนาโดยใช้ [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html) โดยใช้ชุดข้อมูลทดสอบหรือเป้าหมาย การสร้าง AI ของคุณจะถูกวัดผลเชิงปริมาณด้วยตัวประเมินที่มีอยู่หรือที่คุณกำหนดเอง เพื่อเริ่มต้นใช้งาน Azure AI Evaluation SDK ในการประเมินระบบของคุณ คุณสามารถทำตาม [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) เมื่อคุณดำเนินการประเมินผลแล้ว คุณสามารถ [ดูผลลัพธ์ใน Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results)  

## เครื่องหมายการค้า  

โครงการนี้อาจมีเครื่องหมายการค้าหรือโลโก้สำหรับโครงการ ผลิตภัณฑ์ หรือบริการ การใช้งานเครื่องหมายการค้าหรือโลโก้ของ Microsoft อย่างถูกต้องต้องเป็นไปตาม [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general)  
การใช้งานเครื่องหมายการค้าหรือโลโก้ของ Microsoft ในเวอร์ชันที่ปรับเปลี่ยนต้องไม่ก่อให้เกิดความสับสนหรือบ่งบอกถึงการสนับสนุนจาก Microsoft การใช้งานเครื่องหมายการค้าหรือโลโก้ของบุคคลที่สามต้องเป็นไปตามนโยบายของบุคคลที่สามนั้น ๆ  

---

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้การแปลมีความถูกต้องมากที่สุด แต่โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาดั้งเดิมควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลภาษามืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดจากการใช้การแปลนี้