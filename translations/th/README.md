<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5c07bb4c3c89a36c9be332a065a9a33c",
  "translation_date": "2025-07-16T15:14:21+00:00",
  "source_file": "README.md",
  "language_code": "th"
}
-->
# Phi Cookbook: ตัวอย่างใช้งานจริงกับโมเดล Phi ของ Microsoft

[![เปิดและใช้งานตัวอย่างใน GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)  
[![เปิดใน Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![ผู้ร่วมพัฒนา GitHub](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)  
[![ปัญหา GitHub](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)  
[![คำขอดึง GitHub](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)  
[![ยินดีรับ PRs](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![ผู้ติดตาม GitHub](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)  
[![โฟร์ก GitHub](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)  
[![ดาว GitHub](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![ชุมชน Azure AI Discord](https://dcbadge.vercel.app/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

Phi คือชุดโมเดล AI แบบโอเพนซอร์สที่พัฒนาโดย Microsoft

Phi เป็นโมเดลภาษาเล็ก (SLM) ที่ทรงพลังและคุ้มค่าที่สุดในตอนนี้ โดยมีผลการทดสอบที่ดีมากในหลายภาษา การให้เหตุผล การสร้างข้อความ/แชท การเขียนโค้ด ภาพ เสียง และสถานการณ์อื่นๆ

คุณสามารถนำ Phi ไปใช้งานบนคลาวด์หรืออุปกรณ์ขอบเครือข่าย (edge devices) ได้อย่างง่ายดาย และสร้างแอปพลิเคชัน AI สร้างสรรค์ที่ใช้พลังประมวลผลจำกัดได้

ทำตามขั้นตอนเหล่านี้เพื่อเริ่มต้นใช้งานทรัพยากรนี้:  
1. **Fork ที่เก็บข้อมูล**: คลิก [![โฟร์ก GitHub](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)  
2. **โคลนที่เก็บข้อมูล**: `git clone https://github.com/microsoft/PhiCookBook.git`  
3. [**เข้าร่วมชุมชน Microsoft AI Discord เพื่อพบปะผู้เชี่ยวชาญและนักพัฒนาร่วมกัน**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/cover.eb18d1b9605d754b30973f4e17c6e11ea4f8473d9686ee378d6e7b44e3c70ac7.th.png)

### 🌐 รองรับหลายภาษา

#### รองรับผ่าน GitHub Action (อัตโนมัติและอัปเดตตลอดเวลา)

[ฝรั่งเศส](../fr/README.md) | [สเปน](../es/README.md) | [เยอรมัน](../de/README.md) | [รัสเซีย](../ru/README.md) | [อาหรับ](../ar/README.md) | [เปอร์เซีย (ฟาร์ซี)](../fa/README.md) | [อูรดู](../ur/README.md) | [จีน (ตัวย่อ)](../zh/README.md) | [จีน (ตัวเต็ม, มาเก๊า)](../mo/README.md) | [จีน (ตัวเต็ม, ฮ่องกง)](../hk/README.md) | [จีน (ตัวเต็ม, ไต้หวัน)](../tw/README.md) | [ญี่ปุ่น](../ja/README.md) | [เกาหลี](../ko/README.md) | [ฮินดี](../hi/README.md)  
[เบงกาลี](../bn/README.md) | [มราฐี](../mr/README.md) | [เนปาลี](../ne/README.md) | [ปัญจาบี (กูรมุขี)](../pa/README.md) | [โปรตุเกส (โปรตุเกส)](../pt/README.md) | [โปรตุเกส (บราซิล)](../br/README.md) | [อิตาเลียน](../it/README.md) | [โปแลนด์](../pl/README.md) | [ตุรกี](../tr/README.md) | [กรีก](../el/README.md) | [ไทย](./README.md) | [สวีเดน](../sv/README.md) | [เดนมาร์ก](../da/README.md) | [นอร์เวย์](../no/README.md) | [ฟินแลนด์](../fi/README.md) | [ดัตช์](../nl/README.md) | [ฮีบรู](../he/README.md) | [เวียดนาม](../vi/README.md) | [อินโดนีเซีย](../id/README.md) | [มาเลย์](../ms/README.md) | [ตากาล็อก (ฟิลิปปินส์)](../tl/README.md) | [สวาฮิลี](../sw/README.md) | [ฮังการี](../hu/README.md) | [เช็ก](../cs/README.md) | [สโลวัก](../sk/README.md) | [โรมาเนีย](../ro/README.md) | [บัลแกเรีย](../bg/README.md) | [เซอร์เบีย (ซีริลลิก)](../sr/README.md) | [โครเอเชีย](../hr/README.md) | [สโลวีเนีย](../sl/README.md)

## สารบัญ

- บทนำ  
  - [ยินดีต้อนรับสู่ครอบครัว Phi](./md/01.Introduction/01/01.PhiFamily.md)  
  - [การตั้งค่าสภาพแวดล้อมของคุณ](./md/01.Introduction/01/01.EnvironmentSetup.md)  
  - [ทำความเข้าใจเทคโนโลยีหลัก](./md/01.Introduction/01/01.Understandingtech.md)  
  - [ความปลอดภัย AI สำหรับโมเดล Phi](./md/01.Introduction/01/01.AISafety.md)  
  - [การรองรับฮาร์ดแวร์ Phi](./md/01.Introduction/01/01.Hardwaresupport.md)  
  - [โมเดล Phi & การใช้งานบนแพลตฟอร์มต่างๆ](./md/01.Introduction/01/01.Edgeandcloud.md)  
  - [การใช้ Guidance-ai กับ Phi](./md/01.Introduction/01/01.Guidance.md)  
  - [โมเดลใน GitHub Marketplace](https://github.com/marketplace/models)  
  - [แคตตาล็อกโมเดล Azure AI](https://ai.azure.com)

- การสืบค้น Phi ในสภาพแวดล้อมต่างๆ  
    -  [Hugging face](./md/01.Introduction/02/01.HF.md)  
    -  [โมเดล GitHub](./md/01.Introduction/02/02.GitHubModel.md)  
    -  [แคตตาล็อกโมเดล Azure AI Foundry](./md/01.Introduction/02/03.AzureAIFoundry.md)  
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)  
    -  [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)  
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)  
    -  [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md)

- การสืบค้น Phi Family  
    - [การสืบค้น Phi บน iOS](./md/01.Introduction/03/iOS_Inference.md)  
    - [การสืบค้น Phi บน Android](./md/01.Introduction/03/Android_Inference.md)  
    - [การสืบค้น Phi บน Jetson](./md/01.Introduction/03/Jetson_Inference.md)  
    - [การสืบค้น Phi บน AI PC](./md/01.Introduction/03/AIPC_Inference.md)  
    - [การสืบค้น Phi ด้วย Apple MLX Framework](./md/01.Introduction/03/MLX_Inference.md)  
    - [การสืบค้น Phi บนเซิร์ฟเวอร์ภายในองค์กร](./md/01.Introduction/03/Local_Server_Inference.md)  
    - [การสืบค้น Phi บนเซิร์ฟเวอร์ระยะไกลโดยใช้ AI Toolkit](./md/01.Introduction/03/Remote_Interence.md)  
    - [การสืบค้น Phi ด้วย Rust](./md/01.Introduction/03/Rust_Inference.md)  
    - [การสืบค้น Phi--Vision ในเครื่อง](./md/01.Introduction/03/Vision_Inference.md)  
    - [การสืบค้น Phi ด้วย Kaito AKS, Azure Containers (รองรับอย่างเป็นทางการ)](./md/01.Introduction/03/Kaito_Inference.md)  
-  [การควอนไทซ์ Phi Family](./md/01.Introduction/04/QuantifyingPhi.md)  
    - [การควอนไทซ์ Phi-3.5 / 4 ด้วย llama.cpp](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)  
    - [การควอนไทซ์ Phi-3.5 / 4 ด้วยส่วนขยาย Generative AI สำหรับ onnxruntime](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)  
    - [การควอนไทซ์ Phi-3.5 / 4 ด้วย Intel OpenVINO](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)  
    - [การควอนไทซ์ Phi-3.5 / 4 ด้วย Apple MLX Framework](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

-  การประเมิน Phi  
    - [AI ที่รับผิดชอบ](./md/01.Introduction/05/ResponsibleAI.md)  
    - [Azure AI Foundry สำหรับการประเมิน](./md/01.Introduction/05/AIFoundry.md)  
    - [การใช้ Promptflow สำหรับการประเมิน](./md/01.Introduction/05/Promptflow.md)

- RAG กับ Azure AI Search  
    - [วิธีใช้ Phi-4-mini และ Phi-4-multimodal (RAG) กับ Azure AI Search](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- ตัวอย่างการพัฒนาแอป Phi  
  - แอปข้อความและแชท  
    - ตัวอย่าง Phi-4 🆕  
      - [📓] [แชทกับโมเดล Phi-4-mini ONNX](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)  
      - [แชทกับโมเดล Phi-4 ONNX ในเครื่อง .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)  
      - [แอปคอนโซลแชท .NET กับ Phi-4 ONNX โดยใช้ Sementic Kernel](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)  
    - ตัวอย่าง Phi-3 / 3.5  
      - [แชทบอทในเบราว์เซอร์โดยใช้ Phi3, ONNX Runtime Web และ WebGPU](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)  
      - [แชท OpenVino](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)  
      - [โมเดลหลายตัว - โต้ตอบ Phi-3-mini และ OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)  
      - [MLFlow - สร้าง wrapper และใช้ Phi-3 กับ MLFlow](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)  
      - [การปรับแต่งโมเดล - วิธีปรับแต่งโมเดล Phi-3-min สำหรับ ONNX Runtime Web ด้วย Olive](https://github.com/microsoft/Olive/tree/main/examples/phi3)  
      - [แอป WinUI3 กับ Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)  
      - [ตัวอย่างแอปบันทึกโน้ต AI หลายโมเดลบน WinUI3](https://github.com/microsoft/ai-powered-notes-winui3-sample)
- [ปรับแต่งและรวมโมเดล Phi-3 ที่กำหนดเองกับ Prompt flow](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
- [ปรับแต่งและรวมโมเดล Phi-3 ที่กำหนดเองกับ Prompt flow ใน Azure AI Foundry](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
- [ประเมินผลโมเดล Phi-3 / Phi-3.5 ที่ปรับแต่งแล้วใน Azure AI Foundry โดยเน้นหลักการ Responsible AI ของ Microsoft](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
- [📓] [ตัวอย่างการทำนายภาษาด้วย Phi-3.5-mini-instruct (จีน/อังกฤษ)](../../md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
- [Phi-3.5-Instruct WebGPU RAG Chatbot](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
- [การใช้ Windows GPU เพื่อสร้างโซลูชัน Prompt flow กับ Phi-3.5-Instruct ONNX](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
- [การใช้ Microsoft Phi-3.5 tflite เพื่อสร้างแอป Android](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
- [ตัวอย่าง Q&A .NET โดยใช้โมเดล ONNX Phi-3 บนเครื่องด้วย Microsoft.ML.OnnxRuntime](../../md/04.HOL/dotnet/src/LabsPhi301)
- [แอปแชทคอนโซล .NET พร้อม Semantic Kernel และ Phi-3](../../md/04.HOL/dotnet/src/LabsPhi302)

- ตัวอย่างโค้ด Azure AI Inference SDK  
  - ตัวอย่าง Phi-4 🆕  
    - [📓] [สร้างโค้ดโปรเจกต์โดยใช้ Phi-4-multimodal](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)  
  - ตัวอย่าง Phi-3 / 3.5  
    - [สร้าง Visual Studio Code GitHub Copilot Chat ของคุณเองด้วย Microsoft Phi-3 Family](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)  
    - [สร้าง Visual Studio Code Chat Copilot Agent ของคุณเองด้วย Phi-3.5 โดยใช้ GitHub Models](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)  

- ตัวอย่างการใช้เหตุผลขั้นสูง  
  - ตัวอย่าง Phi-4 🆕  
    - [📓] [ตัวอย่าง Phi-4-mini-reasoning หรือ Phi-4-reasoning](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)  
    - [📓] [การปรับแต่ง Phi-4-mini-reasoning ด้วย Microsoft Olive](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)  
    - [📓] [การปรับแต่ง Phi-4-mini-reasoning ด้วย Apple MLX](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)  
    - [📓] [Phi-4-mini-reasoning กับ GitHub Models](../../md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)  
    - [📓] [Phi-4-mini-reasoning กับ Azure AI Foundry Models](../../md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)  
- ตัวอย่างสาธิต  
    - [Phi-4-mini สาธิตบน Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)  
    - [Phi-4-multimodal สาธิตบน Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)  
- ตัวอย่าง Vision  
  - ตัวอย่าง Phi-4 🆕  
    - [📓] [ใช้ Phi-4-multimodal อ่านภาพและสร้างโค้ด](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md)  
  - ตัวอย่าง Phi-3 / 3.5  
    - [📓][Phi-3-vision-Image text to text](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)  
    - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)  
    - [📓][Phi-3-vision CLIP Embedding](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)  
    - [DEMO: Phi-3 Recycling](https://github.com/jennifermarsman/PhiRecycling/)  
    - [Phi-3-vision - ผู้ช่วยภาษาภาพ - ด้วย Phi3-Vision และ OpenVINO](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)  
    - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)  
    - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)  
    - [📓][ตัวอย่าง Phi-3.5 Vision หลายเฟรมหรือหลายภาพ](../../md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)  
    - [Phi-3 Vision โมเดล ONNX บนเครื่องโดยใช้ Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi303)  
    - [เมนูสำหรับ Phi-3 Vision โมเดล ONNX บนเครื่องโดยใช้ Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi304)  

- ตัวอย่างคณิตศาสตร์  
  - ตัวอย่าง Phi-4-Mini-Flash-Reasoning-Instruct 🆕 [สาธิตคณิตศาสตร์ด้วย Phi-4-Mini-Flash-Reasoning-Instruct](../../md/02.Application/09.Math/MathDemo.ipynb)  

- ตัวอย่างเสียง  
  - ตัวอย่าง Phi-4 🆕  
    - [📓] [การถอดเสียงจากเสียงด้วย Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Transciption/README.md)  
    - [📓] [ตัวอย่างเสียง Phi-4-multimodal](../../md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)  
    - [📓] [ตัวอย่างแปลเสียงพูดด้วย Phi-4-multimodal](../../md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)  
    - [แอปคอนโซล .NET ใช้ Phi-4-multimodal วิเคราะห์ไฟล์เสียงและสร้างถอดความ](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)  

- ตัวอย่าง MOE  
  - ตัวอย่าง Phi-3 / 3.5  
    - [📓] [ตัวอย่าง Phi-3.5 Mixture of Experts Models (MoEs) สำหรับโซเชียลมีเดีย](../../md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)  
    - [📓] [สร้าง Retrieval-Augmented Generation (RAG) Pipeline ด้วย NVIDIA NIM Phi-3 MOE, Azure AI Search และ LlamaIndex](../../md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)  

- ตัวอย่างการเรียกใช้ฟังก์ชัน  
  - ตัวอย่าง Phi-4 🆕  
    - [📓] [การใช้ Function Calling กับ Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)  
    - [📓] [การใช้ Function Calling เพื่อสร้าง multi-agents กับ Phi-4-mini](../../md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)  
    - [📓] [การใช้ Function Calling กับ Ollama](../../md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)  
    - [📓] [การใช้ Function Calling กับ ONNX](../../md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)  

- ตัวอย่างการผสมผสานมัลติโมดัล  
  - ตัวอย่าง Phi-4 🆕  
    - [📓] [ใช้ Phi-4-multimodal เป็นนักข่าวเทคโนโลยี](../../md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)  
    - [แอปคอนโซล .NET ใช้ Phi-4-multimodal วิเคราะห์ภาพ](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)  

- การปรับแต่ง Phi  
  - [สถานการณ์การปรับแต่ง](./md/03.FineTuning/FineTuning_Scenarios.md)  
  - [การปรับแต่งกับ RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)  
  - [ปรับแต่งให้ Phi-3 เป็นผู้เชี่ยวชาญในอุตสาหกรรม](./md/03.FineTuning/LetPhi3gotoIndustriy.md)  
  - [ปรับแต่ง Phi-3 ด้วย AI Toolkit สำหรับ VS Code](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)  
  - [ปรับแต่ง Phi-3 ด้วย Azure Machine Learning Service](./md/03.FineTuning/Introduce_AzureML.md)  
  - [ปรับแต่ง Phi-3 ด้วย Lora](./md/03.FineTuning/FineTuning_Lora.md)  
  - [ปรับแต่ง Phi-3 ด้วย QLora](./md/03.FineTuning/FineTuning_Qlora.md)  
  - [ปรับแต่ง Phi-3 ด้วย Azure AI Foundry](./md/03.FineTuning/FineTuning_AIFoundry.md)  
  - [ปรับแต่ง Phi-3 ด้วย Azure ML CLI/SDK](./md/03.FineTuning/FineTuning_MLSDK.md)  
  - [ปรับแต่งด้วย Microsoft Olive](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)  
  - [ห้องปฏิบัติการปรับแต่งด้วย Microsoft Olive](./md/03.FineTuning/olive-lab/readme.md)  
  - [ปรับแต่ง Phi-3-vision ด้วย Weights and Bias](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)  
  - [ปรับแต่ง Phi-3 ด้วย Apple MLX Framework](./md/03.FineTuning/FineTuning_MLX.md)  
  - [ปรับแต่ง Phi-3-vision (รองรับอย่างเป็นทางการ)](./md/03.FineTuning/FineTuning_Vision.md)  
  - [ปรับแต่ง Phi-3 ด้วย Kaito AKS, Azure Containers (รองรับอย่างเป็นทางการ)](./md/03.FineTuning/FineTuning_Kaito.md)  
  - [ปรับแต่ง Phi-3 และ 3.5 Vision](https://github.com/2U1/Phi3-Vision-Finetune)  

- ห้องปฏิบัติการ  
  - [สำรวจโมเดลล้ำสมัย: LLMs, SLMs, การพัฒนาในเครื่อง และอื่นๆ](https://github.com/microsoft/aitour-exploring-cutting-edge-models)  
  - [ปลดล็อกศักยภาพ NLP: การปรับแต่งด้วย Microsoft Olive](https://github.com/azure/Ignite_FineTuning_workshop)  

- งานวิจัยและสิ่งตีพิมพ์ทางวิชาการ  
  - [Textbooks Are All You Need II: รายงานทางเทคนิค phi-1.5](https://arxiv.org/abs/2309.05463)  
  - [รายงานทางเทคนิค Phi-3: โมเดลภาษาที่มีความสามารถสูงบนโทรศัพท์ของคุณ](https://arxiv.org/abs/2404.14219)  
  - [รายงานทางเทคนิค Phi-4](https://arxiv.org/abs/2412.08905)  
  - [รายงานทางเทคนิค Phi-4-Mini: โมเดลภาษามัลติโมดัลขนาดกะทัดรัดแต่ทรงพลังผ่าน Mixture-of-LoRAs](https://arxiv.org/abs/2503.01743)  
  - [การปรับแต่งโมเดลภาษาขนาดเล็กสำหรับการเรียกใช้ฟังก์ชันในรถยนต์](https://arxiv.org/abs/2501.02342)  
  - [(WhyPHI) การปรับแต่ง PHI-3 สำหรับการตอบคำถามแบบเลือกตอบหลายตัว: วิธีการ ผลลัพธ์ และความท้าทาย](https://arxiv.org/abs/2501.01588)
- [Phi-4-reasoning Technical Report](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
- [Phi-4-mini-reasoning Technical Report](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## การใช้งานโมเดล Phi

### Phi บน Azure AI Foundry

คุณสามารถเรียนรู้วิธีใช้ Microsoft Phi และวิธีสร้างโซลูชันแบบครบวงจร (E2E) บนอุปกรณ์ฮาร์ดแวร์ต่างๆ ของคุณ เพื่อสัมผัสประสบการณ์กับ Phi ด้วยตัวเอง เริ่มต้นด้วยการทดลองเล่นกับโมเดลและปรับแต่ง Phi ให้เหมาะกับสถานการณ์ของคุณผ่าน [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai) คุณสามารถเรียนรู้เพิ่มเติมได้ที่ Getting Started with [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md)

**Playground**  
แต่ละโมเดลจะมี playground เฉพาะสำหรับทดสอบโมเดล [Azure AI Playground](https://aka.ms/try-phi3)

### Phi บน GitHub Models

คุณสามารถเรียนรู้วิธีใช้ Microsoft Phi และวิธีสร้างโซลูชันแบบครบวงจร (E2E) บนอุปกรณ์ฮาร์ดแวร์ต่างๆ ของคุณ เพื่อสัมผัสประสบการณ์กับ Phi ด้วยตัวเอง เริ่มต้นด้วยการทดลองเล่นกับโมเดลและปรับแต่ง Phi ให้เหมาะกับสถานการณ์ของคุณผ่าน [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) คุณสามารถเรียนรู้เพิ่มเติมได้ที่ Getting Started with [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md)

**Playground**  
แต่ละโมเดลจะมี [playground สำหรับทดสอบโมเดล](/md/02.QuickStart/GitHubModel_QuickStart.md)

### Phi บน Hugging Face

คุณยังสามารถค้นหาโมเดลได้ที่ [Hugging Face](https://huggingface.co/microsoft)

**Playground**  
[Hugging Chat playground](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## Responsible AI

Microsoft มุ่งมั่นที่จะช่วยให้ลูกค้าของเราใช้ผลิตภัณฑ์ AI อย่างรับผิดชอบ โดยแบ่งปันความรู้และสร้างความไว้วางใจผ่านเครื่องมือต่างๆ เช่น Transparency Notes และ Impact Assessments ทรัพยากรเหล่านี้ส่วนใหญ่สามารถหาได้ที่ [https://aka.ms/RAI](https://aka.ms/RAI)  
แนวทางของ Microsoft ในการพัฒนา AI อย่างรับผิดชอบยึดหลักตามหลักการ AI ของเราที่เน้นความยุติธรรม ความน่าเชื่อถือและความปลอดภัย ความเป็นส่วนตัวและความมั่นคง ความครอบคลุม ความโปร่งใส และความรับผิดชอบ

โมเดลขนาดใหญ่ที่ใช้กับภาษา ภาพ และเสียง - เช่นโมเดลที่ใช้ในตัวอย่างนี้ - อาจแสดงพฤติกรรมที่ไม่ยุติธรรม ไม่น่าเชื่อถือ หรือไม่เหมาะสม ซึ่งอาจก่อให้เกิดความเสียหายได้ โปรดศึกษาข้อมูลเพิ่มเติมจาก [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) เพื่อรับทราบความเสี่ยงและข้อจำกัด

แนวทางที่แนะนำในการลดความเสี่ยงเหล่านี้คือการรวมระบบความปลอดภัยในสถาปัตยกรรมของคุณที่สามารถตรวจจับและป้องกันพฤติกรรมที่เป็นอันตราย [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) ให้การปกป้องในระดับอิสระ สามารถตรวจจับเนื้อหาที่เป็นอันตรายที่สร้างโดยผู้ใช้และ AI ในแอปพลิเคชันและบริการต่างๆ Azure AI Content Safety มี API สำหรับข้อความและภาพที่ช่วยให้คุณตรวจจับเนื้อหาที่เป็นอันตราย ภายใน Azure AI Foundry บริการ Content Safety ช่วยให้คุณดู สำรวจ และทดลองโค้ดตัวอย่างสำหรับการตรวจจับเนื้อหาที่เป็นอันตรายในหลายรูปแบบ เอกสาร [quickstart documentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) ช่วยแนะนำวิธีการส่งคำขอไปยังบริการนี้

อีกประเด็นที่ควรพิจารณาคือประสิทธิภาพโดยรวมของแอปพลิเคชัน สำหรับแอปพลิเคชันที่ใช้หลายโหมดและหลายโมเดล เรามองว่าประสิทธิภาพหมายถึงระบบทำงานได้ตามที่คุณและผู้ใช้คาดหวัง รวมถึงไม่สร้างผลลัพธ์ที่เป็นอันตราย การประเมินประสิทธิภาพของแอปพลิเคชันโดยรวมจึงเป็นสิ่งสำคัญ โดยใช้ [Performance and Quality and Risk and Safety evaluators](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) คุณยังสามารถสร้างและประเมินด้วย [custom evaluators](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators) ได้ด้วย

คุณสามารถประเมินแอปพลิเคชัน AI ของคุณในสภาพแวดล้อมการพัฒนาด้วย [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html) โดยใช้ชุดข้อมูลทดสอบหรือเป้าหมายที่กำหนด การสร้างสรรค์ของแอปพลิเคชัน generative AI จะถูกวัดเชิงปริมาณด้วย evaluators ที่มีมาให้หรือ evaluators ที่คุณสร้างเอง หากต้องการเริ่มต้นใช้งาน azure ai evaluation sdk เพื่อประเมินระบบของคุณ สามารถติดตาม [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) เมื่อคุณรันการประเมินเสร็จแล้ว คุณสามารถ [ดูผลลัพธ์ใน Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results) ได้

## เครื่องหมายการค้า

โปรเจกต์นี้อาจมีเครื่องหมายการค้าหรือโลโก้ของโปรเจกต์ ผลิตภัณฑ์ หรือบริการต่างๆ การใช้เครื่องหมายการค้าหรือโลโก้ของ Microsoft อย่างถูกต้องต้องเป็นไปตาม [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general)  
การใช้เครื่องหมายการค้าหรือโลโก้ของ Microsoft ในเวอร์ชันที่แก้ไขของโปรเจกต์นี้ต้องไม่ก่อให้เกิดความสับสนหรือสื่อถึงการสนับสนุนจาก Microsoft การใช้เครื่องหมายการค้าหรือโลโก้ของบุคคลที่สามต้องเป็นไปตามนโยบายของเจ้าของเครื่องหมายนั้นๆ

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้ความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลโดยผู้เชี่ยวชาญมนุษย์ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดใด ๆ ที่เกิดจากการใช้การแปลนี้