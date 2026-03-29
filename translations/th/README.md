# Phi Cookbook: ตัวอย่างใช้งานจริงกับโมเดล Phi ของ Microsoft

[![เปิดและใช้ตัวอย่างใน GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![เปิดใน Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![ผู้ร่วมพัฒนา GitHub](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![ประเด็น GitHub](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![คำร้องขอ pull ของ GitHub](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![ยินดีรับ PR](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![ผู้ติดตาม GitHub](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![การแยกสาขา GitHub](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![ดาว GitHub](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi คือชุดโมเดล AI แบบเปิดที่พัฒนาโดย Microsoft

Phi เป็นโมเดลภาษาขนาดเล็ก (SLM) ที่ทรงพลังและคุ้มค่าที่สุดในขณะนี้ พร้อมด้วยประสิทธิภาพที่ดีมากในหลายภาษา, การให้เหตุผล, การสร้างข้อความ/แชท, การเขียนโค้ด, รูปภาพ, เสียง และสถานการณ์อื่นๆ

คุณสามารถปรับใช้ Phi บนคลาวด์หรืออุปกรณ์ปลายทาง และสร้างแอปพลิเคชัน AI แบบสร้างสรรค์ได้อย่างง่ายดายแม้มีพลังการประมวลผลจำกัด

ทำตามขั้นตอนเหล่านี้เพื่อเริ่มต้นใช้ทรัพยากรเหล่านี้:
1. **แยกที่เก็บ (Fork the Repository)**: คลิก [![การแยกสาขา GitHub](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **โคลนที่เก็บ (Clone the Repository)**: `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**เข้าร่วมชุมชน Microsoft AI Discord และพบกับผู้เชี่ยวชาญรวมทั้งนักพัฒนาร่วมกัน**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![ปก](../../translated_images/th/cover.eb18d1b9605d754b.webp)

### 🌐 รองรับหลายภาษา

#### รองรับผ่าน GitHub Action (อัตโนมัติ & อัปเดตตลอดเวลา)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[ภาษาอาหรับ](../ar/README.md) | [ภาษาเบงกาลี](../bn/README.md) | [ภาษาบัลแกเรีย](../bg/README.md) | [ภาษาพม่า (เมียนมา)](../my/README.md) | [ภาษาจีน (ตัวย่อ)](../zh-CN/README.md) | [ภาษาจีน (ตัวเต็ม, ฮ่องกง)](../zh-HK/README.md) | [ภาษาจีน (ตัวเต็ม, มาเก๊า)](../zh-MO/README.md) | [ภาษาจีน (ตัวเต็ม, ไต้หวัน)](../zh-TW/README.md) | [ภาษาโครเอเชีย](../hr/README.md) | [ภาษาเช็ก](../cs/README.md) | [ภาษาเดนมาร์ก](../da/README.md) | [ภาษาดัตช์](../nl/README.md) | [ภาษาเอสโตเนีย](../et/README.md) | [ภาษาฟินนิช](../fi/README.md) | [ภาษาฝรั่งเศส](../fr/README.md) | [ภาษาเยอรมัน](../de/README.md) | [ภาษากรีก](../el/README.md) | [ภาษาฮีบรู](../he/README.md) | [ภาษาฮินดี](../hi/README.md) | [ภาษาฮังการี](../hu/README.md) | [ภาษาอินโดนีเซีย](../id/README.md) | [ภาษาอิตาเลียน](../it/README.md) | [ภาษาญี่ปุ่น](../ja/README.md) | [ภาษากันนาดา](../kn/README.md) | [ภาษาเกาหลี](../ko/README.md) | [ภาษา Литва](../lt/README.md) | [ภาษามาเลย์](../ms/README.md) | [ภาษามาลายาลัม](../ml/README.md) | [ภาษามราฐี](../mr/README.md) | [ภาษาเนปาล](../ne/README.md) | [ภาษาไนจีเรียพิทชิน](../pcm/README.md) | [ภาษานอร์เวย์](../no/README.md) | [ภาษาเปอร์เซีย (ฟาร์ซี)](../fa/README.md) | [ภาษาโปแลนด์](../pl/README.md) | [ภาษาโปรตุเกส (บราซิล)](../pt-BR/README.md) | [ภาษาโปรตุเกส (โปรตุเกส)](../pt-PT/README.md) | [ภาษาปันจาบี (กูร์มูขี)](../pa/README.md) | [ภาษาโรมาเนีย](../ro/README.md) | [ภาษารัสเซีย](../ru/README.md) | [ภาษาเซอร์เบีย (ซิริลลิก)](../sr/README.md) | [ภาษาสโลวัก](../sk/README.md) | [ภาษาสโลวีเนีย](../sl/README.md) | [ภาษาสเปน](../es/README.md) | [ภาษาสวาฮิลี](../sw/README.md) | [ภาษาสวีเดน](../sv/README.md) | [ภาษาตากาล็อก (ฟิลิปปินส์)](../tl/README.md) | [ภาษาทมิฬ](../ta/README.md) | [ภาษาเทลูกู](../te/README.md) | [ภาษาไทย](./README.md) | [ภาษาตุรกี](../tr/README.md) | [ภาษา ยูเครน](../uk/README.md) | [ภาษาอูรดู](../ur/README.md) | [ภาษาเวียดนาม](../vi/README.md)

> **ต้องการโคลนแบบท้องถิ่นหรือไม่?**
>
> ที่เก็บนี้รวมการแปลมากกว่า 50 ภาษา ซึ่งจะเพิ่มขนาดดาวน์โหลดมากอย่างมีนัยสำคัญ เพื่อโคลนโดยไม่มีการแปล ให้ใช้ sparse checkout:
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
> นี่จะมอบทุกอย่างที่คุณต้องการเพื่อทำคอร์สให้เสร็จด้วยความเร็วในการดาวน์โหลดที่เร็วขึ้นมาก
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## สารบัญ
- บทนำ - [ยินดีต้อนรับสู่ Phi Family](./md/01.Introduction/01/01.PhiFamily.md) - [การตั้งค่าสภาพแวดล้อมของคุณ](./md/01.Introduction/01/01.EnvironmentSetup.md) - [การทำความเข้าใจเทคโนโลยีหลัก](./md/01.Introduction/01/01.Understandingtech.md) - [ความปลอดภัยของ AI สำหรับ Phi Models](./md/01.Introduction/01/01.AISafety.md) - [การสนับสนุนฮาร์ดแวร์ Phi](./md/01.Introduction/01/01.Hardwaresupport.md) - [Phi Models & การใช้งานในแพลตฟอร์มต่างๆ](./md/01.Introduction/01/01.Edgeandcloud.md) - [การใช้ Guidance-ai และ Phi](./md/01.Introduction/01/01.Guidance.md) - [GitHub Marketplace Models](https://github.com/marketplace/models) - [Azure AI Model Catalog](https://ai.azure.com) - การทำนาย Phi ในสภาพแวดล้อมต่างๆ - [Hugging face](./md/01.Introduction/02/01.HF.md) - [GitHub Models](./md/01.Introduction/02/02.GitHubModel.md) - [Microsoft Foundry Model Catalog](./md/01.Introduction/02/03.AzureAIFoundry.md) - [Ollama](./md/01.Introduction/02/04.Ollama.md) - [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md) - [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md) - [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md) - การทำนาย Phi Family - [การทำนาย Phi บน iOS](./md/01.Introduction/03/iOS_Inference.md) - [การทำนาย Phi บน Android](./md/01.Introduction/03/Android_Inference.md) - [การทำนาย Phi บน Jetson](./md/01.Introduction/03/Jetson_Inference.md) - [การทำนาย Phi บน AI PC](./md/01.Introduction/03/AIPC_Inference.md) - [การทำนาย Phi ด้วย Apple MLX Framework](./md/01.Introduction/03/MLX_Inference.md) - [การทำนาย Phi ใน Local Server](./md/01.Introduction/03/Local_Server_Inference.md) - [การทำนาย Phi ใน Remote Server โดยใช้ AI Toolkit](./md/01.Introduction/03/Remote_Interence.md) - [การทำนาย Phi ด้วย Rust](./md/01.Introduction/03/Rust_Inference.md) - [การทำนาย Phi--Vision ใน Local](./md/01.Introduction/03/Vision_Inference.md) - [การทำนาย Phi ด้วย Kaito AKS, Azure Containers (สนับสนุนอย่างเป็นทางการ)](./md/01.Introduction/03/Kaito_Inference.md) - [การทำ Quantifying Phi Family](./md/01.Introduction/04/QuantifyingPhi.md) - [การทำ Quantizing Phi-3.5 / 4 ด้วย llama.cpp](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md) - [การทำ Quantizing Phi-3.5 / 4 ด้วย Generative AI extensions สำหรับ onnxruntime](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md) - [การทำ Quantizing Phi-3.5 / 4 ด้วย Intel OpenVINO](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md) - [การทำ Quantizing Phi-3.5 / 4 ด้วย Apple MLX Framework](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md) - การประเมิน Phi - [AI ที่รับผิดชอบ](./md/01.Introduction/05/ResponsibleAI.md) - [Microsoft Foundry สำหรับการประเมิน](./md/01.Introduction/05/AIFoundry.md) - [การใช้ Promptflow สำหรับการประเมิน](./md/01.Introduction/05/Promptflow.md) - RAG กับ Azure AI Search - [วิธีใช้ Phi-4-mini และ Phi-4-multimodal (RAG) กับ Azure AI Search](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb) - ตัวอย่างการพัฒนาแอปพลิเคชัน Phi - แอปพลิเคชันข้อความ & แชท - ตัวอย่าง Phi-4 - [📓] [แชทกับโมเดล ONNX Phi-4-mini](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md) - [แชทกับโมเดล ONNX Phi-4 ในเครื่อง .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) - [แอปแชท .NET Console กับ Phi-4 ONNX โดยใช้ Semantic Kernel](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) - ตัวอย่าง Phi-3 / 3.5 - [แชทบอทในเครื่องบนเบราว์เซอร์โดยใช้ Phi3, ONNX Runtime Web และ WebGPU](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat) - [OpenVino Chat](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md) - [โมเดลหลายตัว - Phi-3-mini โต้ตอบ และ OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md) - [MLFlow - การสร้าง wrapper และใช้ Phi-3 กับ MLFlow](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md) - [การปรับแต่งโมเดล - วิธีการปรับแต่งโมเดล Phi-3-min สำหรับ ONNX Runtime Web ด้วย Olive](https://github.com/microsoft/Olive/tree/main/examples/phi3) - [แอป WinUI3 กับ Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/) -[ตัวอย่างแอปบันทึกโน้ตพร้อม AI หลายโมเดล WinUI3](https://github.com/microsoft/ai-powered-notes-winui3-sample) - [ปรับแต่งและรวม Phi-3 model แบบกำหนดเองกับ Prompt flow](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md) - [ปรับแต่งและรวม Phi-3 model แบบกำหนดเองกับ Prompt flow ใน Microsoft Foundry](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md) - [การประเมินโมเดล Phi-3 / Phi-3.5 ที่ปรับแต่งใน Microsoft Foundry โดยเน้นที่หลักการ AI ที่รับผิดชอบของ Microsoft](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md) - [📓] [ตัวอย่างการทำนายภาษา Phi-3.5-mini-instruct (จีน/อังกฤษ)](./md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb) - [Phi-3.5-Instruct WebGPU RAG Chatbot](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md) - [ใช้ Windows GPU เพื่อสร้างโซลูชัน Prompt flow กับ Phi-3.5-Instruct ONNX](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md) - [ใช้ Microsoft Phi-3.5 tflite สร้างแอป Android](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md) - [ตัวอย่าง Q&A .NET โดยใช้โมเดล ONNX Phi-3 ท้องถิ่นโดยใช้ Microsoft.ML.OnnxRuntime](../../md/04.HOL/dotnet/src/LabsPhi301) - [แอปแชท Console .NET กับ Semantic Kernel และ Phi-3](../../md/04.HOL/dotnet/src/LabsPhi302) - ตัวอย่างโค้ด SDK การทำนาย Azure AI - ตัวอย่าง Phi-4 - [📓] [สร้างโค้ดโปรเจกต์โดยใช้ Phi-4-multimodal](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md) - ตัวอย่าง Phi-3 / 3.5 - [สร้าง Visual Studio Code GitHub Copilot Chat ของคุณเองด้วย Phi-3 Family ของ Microsoft](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md) - [สร้าง Visual Studio Code Chat Copilot Agent ของคุณเองด้วย Phi-3.5 โดยใช้ GitHub Models](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md) - ตัวอย่างการให้เหตุผลขั้นสูง - ตัวอย่าง Phi-4 - [📓] [ตัวอย่าง Phi-4-mini-reasoning หรือ Phi-4-reasoning](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md) - [📓] [ปรับแต่ง Phi-4-mini-reasoning ด้วย Microsoft Olive](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb) - [📓] [ปรับแต่ง Phi-4-mini-reasoning ด้วย Apple MLX](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb) - [📓] [Phi-4-mini-reasoning กับ GitHub Models](./md/02.Application/02.Code/Phi4r/github_models_inference.ipynb) - [📓] [Phi-4-mini-reasoning กับ Microsoft Foundry Models](./md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb) - 
เดโม - [Phi-4-mini เดโมที่โฮสต์บน Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo) - [Phi-4-multimodal เดโมที่โฮสต์บน Hugginge Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo) - ตัวอย่าง Vision - ตัวอย่าง Phi-4 - [📓] [ใช้ Phi-4-multimodal ในการอ่านภาพและสร้างโค้ด](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) - ตัวอย่าง Phi-3 / 3.5 - [📓][Phi-3-vision-ข้อความจากภาพเป็นข้อความ](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb) - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html) - [📓][Phi-3-vision CLIP Embedding](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb) - [เดโม: Phi-3 Recycling](https://github.com/jennifermarsman/PhiRecycling/) - [Phi-3-vision - ผู้ช่วยภาษาภาพ - ด้วย Phi3-Vision และ OpenVINO](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html) - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md) - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md) - [📓][Phi-3.5 Vision ตัวอย่างหลายเฟรมหรือหลายภาพ](./md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb) - [Phi-3 Vision โมเดล ONNX ภายในเครื่องโดยใช้ Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi303) - [เมนูแบบ Phi-3 Vision โมเดล ONNX ภายในเครื่องโดยใช้ Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi304) - ตัวอย่าง Reasoning-Vision - Phi-4-Reasoning-Vision-15B - [📓] [ใช้ Phi-4-Reasoning-Vision-15B ในการตรวจจับ jaywalking](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_Jaywalking.ipynb) - [📓] [ใช้ Phi-4-Reasoning-Vision-15B ในคณิตศาสตร์](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_Math.ipynb) - [📓] [ใช้ Phi-4-Reasoning-Vision-15B ในการตรวจจับ UI](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_ui.ipynb) - ตัวอย่างคณิตศาสตร์ - ตัวอย่าง Phi-4-Mini-Flash-Reasoning-Instruct [เดโมคณิตศาสตร์กับ Phi-4-Mini-Flash-Reasoning-Instruct](./md/02.Application/09.Math/MathDemo.ipynb) - ตัวอย่างเสียง - ตัวอย่าง Phi-4 - [📓] [แยกข้อความจากเสียงโดยใช้ Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Transciption/README.md) - [📓] [ตัวอย่างเสียง Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Siri/demo.ipynb) - [📓] [ตัวอย่างแปลเสียงด้วย Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Translate/demo.ipynb) - [.NET แอปพลิเคชันคอนโซลโดยใช้ Phi-4-multimodal Audio ในการวิเคราะห์ไฟล์เสียงและสร้างถอดเสียง](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) - ตัวอย่าง MOE - ตัวอย่าง Phi-3 / 3.5 - [📓] [ตัวอย่างโหมดผสมผู้เชี่ยวชาญ (MoEs) Phi-3.5 สำหรับโซเชียลมีเดีย](./md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb) - [📓] [สร้าง Retrieval-Augmented Generation (RAG) Pipeline ด้วย NVIDIA NIM Phi-3 MOE, Azure AI Search, และ LlamaIndex](./md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb) - ตัวอย่างเรียกใช้ฟังก์ชัน - ตัวอย่าง Phi-4 🆕 - [📓] [ใช้ Function Calling กับ Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md) - [📓] [ใช้ Function Calling เพื่อสร้างหลายเอเจนต์กับ Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb) - [📓] [ใช้ Function Calling กับ Ollama](./md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb) - [📓] [ใช้ Function Calling กับ ONNX](./md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb) - ตัวอย่างผสมมัลติโมดัล - ตัวอย่าง Phi-4 🆕 - [📓] [ใช้ Phi-4-multimodal เป็นนักข่าวเทคโนโลยี](./md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb) - [.NET แอปพลิเคชันคอนโซลใช้ Phi-4-multimodal เพื่อวิเคราะห์ภาพ](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) - ตัวอย่างปรับแต่งฝึกสอน Phi - [สถานการณ์การปรับแต่งฝึกสอน](./md/03.FineTuning/FineTuning_Scenarios.md) - [การปรับแต่งฝึกสอนกับ RAG](./md/03.FineTuning/FineTuning_vs_RAG.md) - [ปรับแต่งฝึกสอนให้ Phi-3 เป็นผู้เชี่ยวชาญในอุตสาหกรรม](./md/03.FineTuning/LetPhi3gotoIndustriy.md) - [ปรับแต่งฝึกสอน Phi-3 กับ AI Toolkit สำหรับ VS Code](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md) - [ปรับแต่งฝึกสอน Phi-3 ด้วย Azure Machine Learning Service](./md/03.FineTuning/Introduce_AzureML.md) - [ปรับแต่งฝึกสอน Phi-3 ด้วย Lora](./md/03.FineTuning/FineTuning_Lora.md) - [ปรับแต่งฝึกสอน Phi-3 ด้วย QLora](./md/03.FineTuning/FineTuning_Qlora.md) - [ปรับแต่งฝึกสอน Phi-3 ด้วย Microsoft Foundry](./md/03.FineTuning/FineTuning_AIFoundry.md) - [ปรับแต่งฝึกสอน Phi-3 กับ Azure ML CLI/SDK](./md/03.FineTuning/FineTuning_MLSDK.md) - [ปรับแต่งฝึกสอนด้วย Microsoft Olive](./md/03.FineTuning/FineTuning_MicrosoftOlive.md) - [ห้องปฏิบัติการปรับแต่งฝึกสอนด้วย Microsoft Olive](./md/03.FineTuning/olive-lab/readme.md) - [ปรับแต่งฝึกสอน Phi-3-vision กับ Weights and Bias](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md) - [ปรับแต่งฝึกสอน Phi-3 กับ Apple MLX Framework](./md/03.FineTuning/FineTuning_MLX.md) - [ปรับแต่งฝึกสอน Phi-3-vision (สนับสนุนอย่างเป็นทางการ)](./md/03.FineTuning/FineTuning_Vision.md) - [ปรับแต่งฝึกสอน Phi-3 ด้วย Kaito AKS, Azure Containers (สนับสนุนอย่างเป็นทางการ)](./md/03.FineTuning/FineTuning_Kaito.md) - [ปรับแต่งฝึกสอน Phi-3 และ 3.5 Vision](https://github.com/2U1/Phi3-Vision-Finetune) - ห้องปฏิบัติการ - [สำรวจโมเดลล้ำสมัย: LLMs, SLMs, การพัฒนาในเครื่องและอื่น ๆ](https://github.com/microsoft/aitour-exploring-cutting-edge-models) - [ปลดล็อกศักยภาพ NLP: การปรับแต่งฝึกสอนด้วย Microsoft Olive](https://github.com/azure/Ignite_FineTuning_workshop) - เอกสารวิจัยและงานตีพิมพ์ทางวิชาการ - [Textbooks Are All You Need II: รายงานทางเทคนิค phi-1.5](https://arxiv.org/abs/2309.05463) - [รายงานทางเทคนิค Phi-3: โมเดลภาษาที่มีความสามารถสูงในโทรศัพท์ของคุณ](https://arxiv.org/abs/2404.14219) - [รายงานทางเทคนิค Phi-4](https://arxiv.org/abs/2412.08905) - [รายงานทางเทคนิค Phi-4-Mini: โมเดลภาษามัลติโมดัลขนาดกะทัดรัดแต่ทรงพลังผ่าน Mixture-of-LoRAs](https://arxiv.org/abs/2503.01743) - [การปรับแต่งโมเดลภาษาเล็กเพื่อการเรียกใช้งานฟังก์ชันในรถยนต์](https://arxiv.org/abs/2501.02342) - [(WhyPHI) ปรับแต่ง PHI-3 สำหรับการตอบคำถามแบบหลายตัวเลือก: วิธีการ ผลลัพธ์ และความท้าทาย](https://arxiv.org/abs/2501.01588) - [รายงานทางเทคนิค Phi-4-reasoning](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
- [รายงานทางเทคนิค Phi-4-mini-reasoning](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)
# Phi Cookbook: ตัวอย่างปฏิบัติจริงกับโมเดล Phi ของ Microsoft

[![เปิดและใช้ตัวอย่างใน GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![เปิดใน Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=เปิด&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![ผู้ร่วมพัฒนา GitHub](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![ปัญหา GitHub](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![คำขอดึง GitHub](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![ยินดีรับ PRs](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![ผู้ติดตาม GitHub](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![แยกโฟลว์ GitHub](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![ดาว GitHub](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Discord Microsoft Foundry](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi คือชุดโมเดล AI โอเพนซอร์สที่พัฒนาโดย Microsoft

Phi เป็นโมเดลภาษาเล็ก (SLM) ที่ทรงพลังและคุ้มค่าที่สุดในขณะนี้ โดยมีเกณฑ์มาตรฐานที่ดีมากในด้านหลายภาษา, การให้เหตุผล, การสร้างข้อความ/แชท, การเขียนโค้ด, รูปภาพ, เสียง และสถานการณ์อื่นๆ

คุณสามารถปรับใช้ Phi บนคลาวด์หรืออุปกรณ์ edge และสามารถสร้างแอปพลิเคชัน AI สร้างสรรค์ได้อย่างง่ายดายแม้มีพลังคอมพิวเตอร์จำกัด

ทำตามขั้นตอนเหล่านี้เพื่อเริ่มใช้งานทรัพยากรเหล่านี้:
1. **Fork ที่เก็บข้อมูล**: คลิก [![แยกโฟลว์ GitHub](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **โคลนที่เก็บข้อมูล**:   `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**เข้าร่วมชุมชน Microsoft AI Discord และพบปะผู้เชี่ยวชาญและนักพัฒนาร่วม**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/th/cover.eb18d1b9605d754b.webp)

### 🌐 รองรับหลายภาษา

#### รองรับผ่าน GitHub Action (อัตโนมัติ & อัปเดตเสมอ)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[อาหรับ](../ar/README.md) | [เบงกาลี](../bn/README.md) | [บัลแกเรีย](../bg/README.md) | [พม่า (เมียนมา)](../my/README.md) | [จีน (ตัวย่อ)](../zh-CN/README.md) | [จีน (ตัวเต็ม, ฮ่องกง)](../zh-HK/README.md) | [จีน (ตัวเต็ม, มาเก๊า)](../zh-MO/README.md) | [จีน (ตัวเต็ม, ไต้หวัน)](../zh-TW/README.md) | [โครเอเชีย](../hr/README.md) | [เช็ก](../cs/README.md) | [เดนมาร์ก](../da/README.md) | [ดัตช์](../nl/README.md) | [เอสโตเนีย](../et/README.md) | [ฟินแลนด์](../fi/README.md) | [ฝรั่งเศส](../fr/README.md) | [เยอรมัน](../de/README.md) | [กรีก](../el/README.md) | [ฮีบรู](../he/README.md) | [ฮินดี](../hi/README.md) | [ฮังการี](../hu/README.md) | [อินโดนีเซีย](../id/README.md) | [อิตาลี](../it/README.md) | [ญี่ปุ่น](../ja/README.md) | [กันนาดา](../kn/README.md) | [เกาหลี](../ko/README.md) | [ลิทัวเนีย](../lt/README.md) | [มลายู](../ms/README.md) | [มาลายาลัม](../ml/README.md) | [มราฐี](../mr/README.md) | [เนปาล](../ne/README.md) | [ไนจีเรีย พิดจิน](../pcm/README.md) | [นอร์เวย์](../no/README.md) | [เปอร์เซีย (ฟาร์ซี)](../fa/README.md) | [โปแลนด์](../pl/README.md) | [โปรตุเกส (บราซิล)](../pt-BR/README.md) | [โปรตุเกส (โปรตุเกส)](../pt-PT/README.md) | [ปัญจาบี (กูรมุขี)](../pa/README.md) | [โรมาเนีย](../ro/README.md) | [รัสเซีย](../ru/README.md) | [เซอร์เบียน (ซีริลลิก)](../sr/README.md) | [สโลวัก](../sk/README.md) | [สโลวีเนีย](../sl/README.md) | [สเปน](../es/README.md) | [สวาฮิลี](../sw/README.md) | [สวีเดน](../sv/README.md) | [ตากาล็อก (ฟิลิปปินส์)](../tl/README.md) | [ทมิฬ](../ta/README.md) | [เตลูกู](../te/README.md) | [ไทย](./README.md) | [ตุรกี](../tr/README.md) | [ยูเครน](../uk/README.md) | [อูรดู](../ur/README.md) | [เวียดนาม](../vi/README.md)

> **ต้องการโคลนแบบท้องถิ่น?**
>
> ที่เก็บนี้รวมการแปลภาษา 50+ ภาษา ซึ่งเพิ่มขนาดดาวน์โหลดอย่างมาก เพื่อโคลนโดยไม่แปล ให้ใช้ sparse checkout:
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
> วิธีนี้จะให้คุณทุกสิ่งที่จำเป็นสำหรับหลักสูตรด้วยการดาวน์โหลดที่รวดเร็วยิ่งขึ้น
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## สารบัญ

## การใช้โมเดล Phi

### Phi บน Microsoft Foundry

คุณสามารถเรียนรู้วิธีใช้ Microsoft Phi และวิธีสร้างโซลูชันแบบครบวงจรในอุปกรณ์ฮาร์ดแวร์หลากหลายของคุณ เพื่อทดลอง Phi ด้วยตัวเอง เริ่มต้นโดยการเล่นกับโมเดลและปรับแต่ง Phi สำหรับสถานการณ์ของคุณโดยใช้ [Microsoft Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai) คุณสามารถเรียนรู้เพิ่มเติมได้ที่ การเริ่มต้นใช้งานกับ [Microsoft Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md)

**Playground**
แต่ละโมเดลมี playground เฉพาะเพื่อทดสอบโมเดล [Azure AI Playground](https://aka.ms/try-phi3)

### Phi บน GitHub Models

คุณสามารถเรียนรู้วิธีใช้ Microsoft Phi และวิธีสร้างโซลูชันแบบครบวงจรในอุปกรณ์ฮาร์ดแวร์หลากหลายของคุณ เพื่อทดลอง Phi ด้วยตัวเอง เริ่มต้นโดยการเล่นกับโมเดลและปรับแต่ง Phi สำหรับสถานการณ์ของคุณโดยใช้ [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) คุณสามารถเรียนรู้เพิ่มเติมได้ที่ การเริ่มต้นใช้งานกับ [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md)

**Playground**
แต่ละโมเดลมี [playground เฉพาะเพื่อทดสอบโมเดล](/md/02.QuickStart/GitHubModel_QuickStart.md)

### Phi บน Hugging Face

คุณยังสามารถค้นหาโมเดลได้ที่ [Hugging Face](https://huggingface.co/microsoft)

**Playground**
 [Hugging Chat playground](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

 ## 🎒 หลักสูตรอื่นๆ

ทีมของเราผลิตหลักสูตรอื่นๆ! ตรวจสอบได้ที่:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j สำหรับผู้เริ่มต้น](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js สำหรับผู้เริ่มต้น](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![LangChain สำหรับผู้เริ่มต้น](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### Azure / Edge / MCP / Agents
[![AZD สำหรับผู้เริ่มต้น](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI สำหรับผู้เริ่มต้น](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP สำหรับผู้เริ่มต้น](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Agents สำหรับผู้เริ่มต้น](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### ชุดหลักสูตร Generative AI
[![Generative AI สำหรับผู้เริ่มต้น](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generative AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generative AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generative AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### การเรียนรู้หลัก
[![ML for Beginners](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science for Beginners](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI for Beginners](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Cybersecurity for Beginners](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Web Dev for Beginners](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT for Beginners](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR Development for Beginners](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### ชุด Copilot
[![Copilot for AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## AI ที่มีความรับผิดชอบ

Microsoft มุ่งมั่นที่จะช่วยลูกค้าของเราใช้ผลิตภัณฑ์ AI อย่างมีความรับผิดชอบ แบ่งปันบทเรียนของเรา และสร้างความร่วมมือที่มีพื้นฐานจากความไว้วางใจผ่านเครื่องมือต่างๆ เช่น Transparency Notes และ Impact Assessments แหล่งข้อมูลจำนวนมากเหล่านี้สามารถพบได้ที่ [https://aka.ms/RAI](https://aka.ms/RAI)
แนวทางของ Microsoft ต่อ AI ที่มีความรับผิดชอบนั้นตั้งอยู่บนหลักการ AI ของเราที่เน้นความยุติธรรม น่าเชื่อถือและปลอดภัย ความเป็นส่วนตัวและความปลอดภัย การรวมอยู่ด้วยกัน ความโปร่งใส และความรับผิดชอบ

โมเดลภาษาธรรมชาติ รูปภาพ และเสียงขนาดใหญ่ - เช่นที่ใช้ในตัวอย่างนี้ - อาจมีพฤติกรรมที่ไม่ยุติธรรม ไม่น่าเชื่อถือ หรือเป็นการล่วงละเมิด ซึ่งอาจก่อให้เกิดความเสียหาย โปรดดู [บันทึกความโปร่งใสของบริการ Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) เพื่อรับทราบความเสี่ยงและข้อจำกัด

แนวทางที่แนะนำในการลดความเสี่ยงเหล่านี้คือการรวมระบบความปลอดภัยเข้าไปในสถาปัตยกรรมของคุณที่สามารถตรวจจับและป้องกันพฤติกรรมที่เป็นอันตราย [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) ให้ชั้นการป้องกันอิสระ ที่สามารถตรวจจับเนื้อหาที่เป็นอันตรายซึ่งถูกสร้างโดยผู้ใช้และ AI ในแอปพลิเคชันและบริการ Azure AI Content Safety รวมถึง API สำหรับข้อความและรูปภาพ ที่ช่วยให้คุณตรวจจับเนื้อหาที่เป็นอันตราย ภายใน Microsoft Foundry บริการ Content Safety ช่วยให้คุณดู สำรวจ และลองใช้ตัวอย่างโค้ดในการตรวจจับเนื้อหาที่เป็นอันตรายในแต่ละรูปแบบ เอกสาร [quickstart documentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) ช่วยแนะนำวิธีส่งคำขอไปยังบริการนี้

อีกแง่มุมที่ต้องพิจารณาคือประสิทธิภาพโดยรวมของแอปพลิเคชัน ในแอปพลิเคชันที่เป็นแบบมัลติโหมดและมัลติโมเดล เราพิจารณาว่าประสิทธิภาพหมายความว่าระบบทำงานตามที่คุณและผู้ใช้คาดหวัง รวมถึงไม่สร้างผลลัพธ์ที่เป็นอันตราย การประเมินประสิทธิภาพของแอปพลิเคชันโดยรวมของคุณโดยใช้ [ตัวประเมินประสิทธิภาพ คุณภาพ และความเสี่ยงและความปลอดภัย](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) คุณยังสามารถสร้างและประเมินผลด้วย [ตัวประเมินที่กำหนดเอง](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators)

คุณสามารถประเมินแอปพลิเคชัน AI ของคุณในสภาพแวดล้อมการพัฒนาด้วยการใช้ [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html) โดยเมื่อมีชุดข้อมูลทดสอบหรือเป้าหมาย ระบบการสร้างของ AI ของคุณจะถูกวัดอย่างเป็นปริมาณด้วยตัวประเมินที่สมบูรณ์แบบหรือแบบกำหนดเองที่คุณเลือก ในการเริ่มต้นใช้งาน azure ai evaluation sdk เพื่อประเมินระบบของคุณ คุณสามารถทำตาม [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) เมื่อคุณดำเนินการรันการประเมินแล้ว คุณสามารถ [แสดงผลลัพธ์ใน Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results) ได้

## เครื่องหมายการค้า

โครงการนี้อาจมีเครื่องหมายการค้าหรือโลโก้สำหรับโครงการ ผลิตภัณฑ์ หรือบริการต่างๆ การใช้เครื่องหมายการค้าหรือโลโก้ของ Microsoft อย่างถูกต้องต้องเป็นไปตามและปฏิบัติตาม [แนวทางเครื่องหมายการค้าและตราสินค้าของ Microsoft](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general)
การใช้เครื่องหมายการค้าหรือโลโก้ของ Microsoft ในเวอร์ชันที่แก้ไขของโครงการนี้ต้องไม่ก่อให้เกิดความสับสนหรือสื่อความหมายถึงการสนับสนุนจาก Microsoft การใช้เครื่องหมายการค้าหรือโลโก้ของบุคคลที่สามใดๆ อยู่ภายใต้นโยบายของบุคคลที่สามเหล่านั้น

## การขอความช่วยเหลือ

หากคุณติดขัดหรือต้องการสอบถามเกี่ยวกับการสร้างแอป AI เข้าร่วมได้ที่:

[![Microsoft Foundry Discord](https://img.shields.io/badge/Discord-Microsoft_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

หากคุณมีข้อเสนอแนะเกี่ยวกับผลิตภัณฑ์หรือพบข้อผิดพลาดในขณะสร้าง โปรดเข้าเยี่ยมชม:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ข้อจำกัดความรับผิดชอบ**:  
เอกสารฉบับนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามเพื่อความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความคลาดเคลื่อนได้ เอกสารต้นฉบับในภาษาแม่ของเอกสารจะถือเป็นแหล่งข้อมูลที่มีอำนาจสูงสุด สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดใด ๆ ที่เกิดจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->