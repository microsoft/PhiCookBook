<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "698f7f3d48ebc9e25a273d7c8b7e31c5",
  "translation_date": "2025-09-12T14:04:50+00:00",
  "source_file": "README.md",
  "language_code": "ms"
}
-->
# Buku Panduan Phi: Contoh Praktikal dengan Model Phi Microsoft

Phi adalah siri model AI sumber terbuka yang dibangunkan oleh Microsoft.

Phi kini merupakan model bahasa kecil (SLM) yang paling berkuasa dan kos efektif, dengan penilaian yang sangat baik dalam pelbagai bahasa, penaakulan, penjanaan teks/chat, pengekodan, imej, audio, dan senario lain.

Anda boleh melancarkan Phi ke awan atau peranti tepi, dan anda boleh dengan mudah membina aplikasi AI generatif dengan kuasa pengkomputeran yang terhad.

Ikuti langkah-langkah ini untuk mula menggunakan sumber ini:
1. **Fork Repositori**: Klik [![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **Clone Repositori**: `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Sertai Komuniti Discord AI Microsoft dan berhubung dengan pakar serta pembangun lain**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../imgs/cover.png)

### 🌐 Sokongan Pelbagai Bahasa

#### Disokong melalui GitHub Action (Automatik & Sentiasa Terkini)

[French](../fr/README.md) | [Spanish](../es/README.md) | [German](../de/README.md) | [Russian](../ru/README.md) | [Arabic](../ar/README.md) | [Persian (Farsi)](../fa/README.md) | [Urdu](../ur/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Japanese](../ja/README.md) | [Korean](../ko/README.md) | [Hindi](../hi/README.md) 
[Bengali](../bn/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Portuguese (Brazil)](../br/README.md) | [Italian](../it/README.md) | [Polish](../pl/README.md) | [Turkish](../tr/README.md) | [Greek](../el/README.md) | [Thai](../th/README.md) | [Swedish](../sv/README.md) | [Danish](../da/README.md) | [Norwegian](../no/README.md) | [Finnish](../fi/README.md) | [Dutch](../nl/README.md) | [Hebrew](../he/README.md) | [Vietnamese](../vi/README.md) | [Indonesian](../id/README.md) | [Malay](./README.md) | [Tagalog (Filipino)](../tl/README.md) | [Swahili](../sw/README.md) | [Hungarian](../hu/README.md) | [Czech](../cs/README.md) | [Slovak](../sk/README.md) | [Romanian](../ro/README.md) | [Bulgarian](../bg/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Croatian](../hr/README.md) | [Slovenian](../sl/README.md)

## Kandungan

- Pengenalan
  - [Selamat Datang ke Keluarga Phi](./md/01.Introduction/01/01.PhiFamily.md)
  - [Menyiapkan Persekitaran Anda](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [Memahami Teknologi Utama](./md/01.Introduction/01/01.Understandingtech.md)
  - [Keselamatan AI untuk Model Phi](./md/01.Introduction/01/01.AISafety.md)
  - [Sokongan Perkakasan Phi](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Model Phi & Ketersediaan di pelbagai platform](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Menggunakan Guidance-ai dan Phi](./md/01.Introduction/01/01.Guidance.md)
  - [Model Pasar GitHub](https://github.com/marketplace/models)
  - [Katalog Model Azure AI](https://ai.azure.com)

- Inferens Phi dalam persekitaran berbeza
    - [Hugging face](./md/01.Introduction/02/01.HF.md)
    - [Model GitHub](./md/01.Introduction/02/02.GitHubModel.md)
    - [Katalog Model Azure AI Foundry](./md/01.Introduction/02/03.AzureAIFoundry.md)
    - [Ollama](./md/01.Introduction/02/04.Ollama.md)
    - [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    - [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    - [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md)

- Inferens Keluarga Phi
    - [Inferens Phi dalam iOS](./md/01.Introduction/03/iOS_Inference.md)
    - [Inferens Phi dalam Android](./md/01.Introduction/03/Android_Inference.md)
    - [Inferens Phi dalam Jetson](./md/01.Introduction/03/Jetson_Inference.md)
    - [Inferens Phi dalam AI PC](./md/01.Introduction/03/AIPC_Inference.md)
    - [Inferens Phi dengan Apple MLX Framework](./md/01.Introduction/03/MLX_Inference.md)
    - [Inferens Phi dalam Pelayan Tempatan](./md/01.Introduction/03/Local_Server_Inference.md)
    - [Inferens Phi dalam Pelayan Jauh menggunakan AI Toolkit](./md/01.Introduction/03/Remote_Interence.md)
    - [Inferens Phi dengan Rust](./md/01.Introduction/03/Rust_Inference.md)
    - [Inferens Phi--Vision dalam Tempatan](./md/01.Introduction/03/Vision_Inference.md)
    - [Inferens Phi dengan Kaito AKS, Azure Containers (sokongan rasmi)](./md/01.Introduction/03/Kaito_Inference.md)

- [Mengkuantifikasi Keluarga Phi](./md/01.Introduction/04/QuantifyingPhi.md)
    - [Mengkuantifikasi Phi-3.5 / 4 menggunakan llama.cpp](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [Mengkuantifikasi Phi-3.5 / 4 menggunakan sambungan AI generatif untuk onnxruntime](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Mengkuantifikasi Phi-3.5 / 4 menggunakan Intel OpenVINO](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Mengkuantifikasi Phi-3.5 / 4 menggunakan Apple MLX Framework](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

- Penilaian Phi
    - [AI Bertanggungjawab](./md/01.Introduction/05/ResponsibleAI.md)
    - [Penilaian dengan Azure AI Foundry](./md/01.Introduction/05/AIFoundry.md)
    - [Menggunakan Promptflow untuk Penilaian](./md/01.Introduction/05/Promptflow.md)

- RAG dengan Azure AI Search
    - [Cara menggunakan Phi-4-mini dan Phi-4-multimodal (RAG) dengan Azure AI Search](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Contoh pembangunan aplikasi Phi
  - Aplikasi Teks & Chat
    - Contoh Phi-4 🆕
      - [📓] [Chat Dengan Model Phi-4-mini ONNX](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Chat dengan Model Phi-4 ONNX Tempatan .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Aplikasi Konsol .NET Chat dengan Phi-4 ONNX menggunakan Kernel Semantik](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Contoh Phi-3 / 3.5
      - [Chatbot Tempatan dalam pelayar menggunakan Phi3, ONNX Runtime Web dan WebGPU](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [Chat OpenVino](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [Model Pelbagai - Interaktif Phi-3-mini dan OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - Membina pembungkus dan menggunakan Phi-3 dengan MLFlow](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [Pengoptimuman Model - Cara mengoptimumkan model Phi-3-min untuk ONNX Runtime Web dengan Olive](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [Aplikasi WinUI3 dengan Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      - [Aplikasi Nota AI Berkuasa WinUI3 Multi Model](https://github.com/microsoft/ai-powered-notes-winui3-sample)
- [Menyesuaikan dan Mengintegrasikan model Phi-3 tersuai dengan Prompt flow](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
- [Menyesuaikan dan Mengintegrasikan model Phi-3 tersuai dengan Prompt flow dalam Azure AI Foundry](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
- [Menilai Model Phi-3 / Phi-3.5 yang telah disesuaikan dalam Azure AI Foundry dengan fokus pada Prinsip AI Bertanggungjawab Microsoft](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
- [📓] [Contoh ramalan bahasa Phi-3.5-mini-instruct (Cina/Inggeris)](../../md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
- [Chatbot RAG WebGPU Phi-3.5-Instruct](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
- [Menggunakan GPU Windows untuk mencipta penyelesaian Prompt flow dengan Phi-3.5-Instruct ONNX](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
- [Menggunakan Microsoft Phi-3.5 tflite untuk mencipta aplikasi Android](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
- [Contoh Q&A .NET menggunakan model ONNX Phi-3 tempatan dengan Microsoft.ML.OnnxRuntime](../../md/04.HOL/dotnet/src/LabsPhi301)
- [Aplikasi chat konsol .NET dengan Semantic Kernel dan Phi-3](../../md/04.HOL/dotnet/src/LabsPhi302)

- Sampel Kod SDK Inferens Azure AI 
  - Sampel Phi-4 🆕
    - [📓] [Menjana kod projek menggunakan Phi-4-multimodal](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
  - Sampel Phi-3 / 3.5
    - [Membina Chat GitHub Copilot Visual Studio Code anda sendiri dengan Keluarga Microsoft Phi-3](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
    - [Mencipta Ejen Chat Copilot Visual Studio Code anda sendiri dengan Phi-3.5 oleh Model GitHub](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

- Sampel Penalaran Lanjutan
  - Sampel Phi-4 🆕
    - [📓] [Sampel Phi-4-mini-reasoning atau Phi-4-reasoning](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
    - [📓] [Menyesuaikan Phi-4-mini-reasoning dengan Microsoft Olive](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
    - [📓] [Menyesuaikan Phi-4-mini-reasoning dengan Apple MLX](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
    - [📓] [Phi-4-mini-reasoning dengan Model GitHub](../../md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
    - [📓] [Phi-4-mini-reasoning dengan Model Azure AI Foundry](../../md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
- Demo
    - [Demo Phi-4-mini yang dihoskan di Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
    - [Demo Phi-4-multimodal yang dihoskan di Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
- Sampel Penglihatan
  - Sampel Phi-4 🆕
    - [📓] [Menggunakan Phi-4-multimodal untuk membaca imej dan menjana kod](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
  - Sampel Phi-3 / 3.5
    - [📓][Phi-3-vision-Image teks ke teks](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
    - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
    - [📓][Phi-3-vision CLIP Embedding](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
    - [DEMO: Phi-3 Kitar Semula](https://github.com/jennifermarsman/PhiRecycling/)
    - [Phi-3-vision - Pembantu bahasa visual - dengan Phi3-Vision dan OpenVINO](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
    - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
    - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
    - [📓][Phi-3.5 Vision sampel berbilang bingkai atau berbilang imej](../../md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
    - [Phi-3 Vision Model ONNX Tempatan menggunakan Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi303)
    - [Model ONNX Tempatan Phi-3 Vision berdasarkan menu menggunakan Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi304)

- Sampel Matematik
  - Sampel Phi-4-Mini-Flash-Reasoning-Instruct 🆕 [Demo Matematik dengan Phi-4-Mini-Flash-Reasoning-Instruct](../../md/02.Application/09.Math/MathDemo.ipynb)

- Sampel Audio
  - Sampel Phi-4 🆕
    - [📓] [Mengekstrak transkrip audio menggunakan Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
    - [📓] [Sampel Audio Phi-4-multimodal](../../md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
    - [📓] [Sampel Terjemahan Ucapan Phi-4-multimodal](../../md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
    - [Aplikasi konsol .NET menggunakan Phi-4-multimodal Audio untuk menganalisis fail audio dan menjana transkrip](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

- Sampel MOE
  - Sampel Phi-3 / 3.5
    - [📓] [Phi-3.5 Mixture of Experts Models (MoEs) Sampel Media Sosial](../../md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
    - [📓] [Membina Pipeline Retrieval-Augmented Generation (RAG) dengan NVIDIA NIM Phi-3 MOE, Azure AI Search, dan LlamaIndex](../../md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)

- Sampel Panggilan Fungsi
  - Sampel Phi-4 🆕
    - [📓] [Menggunakan Panggilan Fungsi Dengan Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
    - [📓] [Menggunakan Panggilan Fungsi untuk mencipta multi-ejen Dengan Phi-4-mini](../../md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
    - [📓] [Menggunakan Panggilan Fungsi dengan Ollama](../../md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
    - [📓] [Menggunakan Panggilan Fungsi dengan ONNX](../../md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)

- Sampel Pencampuran Multimodal
  - Sampel Phi-4 🆕
    - [📓] [Menggunakan Phi-4-multimodal sebagai wartawan teknologi](../../md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
    - [Aplikasi konsol .NET menggunakan Phi-4-multimodal untuk menganalisis imej](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Menyesuaikan Sampel Phi
  - [Senario Penyesuaian](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [Penyesuaian vs RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [Menyesuaikan Phi-3 untuk menjadi pakar industri](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [Menyesuaikan Phi-3 dengan AI Toolkit untuk VS Code](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Menyesuaikan Phi-3 dengan Perkhidmatan Pembelajaran Mesin Azure](./md/03.FineTuning/Introduce_AzureML.md)
  - [Menyesuaikan Phi-3 dengan Lora](./md/03.FineTuning/FineTuning_Lora.md)
  - [Menyesuaikan Phi-3 dengan QLora](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Menyesuaikan Phi-3 dengan Azure AI Foundry](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Menyesuaikan Phi-3 dengan Azure ML CLI/SDK](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Menyesuaikan dengan Microsoft Olive](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Menyesuaikan dengan Microsoft Olive Hands-On Lab](./md/03.FineTuning/olive-lab/readme.md)
  - [Menyesuaikan Phi-3-vision dengan Weights and Bias](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [Menyesuaikan Phi-3 dengan Kerangka Apple MLX](./md/03.FineTuning/FineTuning_MLX.md)
  - [Menyesuaikan Phi-3-vision (sokongan rasmi)](./md/03.FineTuning/FineTuning_Vision.md)
  - [Menyesuaikan Phi-3 dengan Kaito AKS, Kontena Azure (sokongan rasmi)](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Menyesuaikan Phi-3 dan 3.5 Vision](https://github.com/2U1/Phi3-Vision-Finetune)

- Makmal Hands-On
  - [Meneroka model terkini: LLMs, SLMs, pembangunan tempatan dan banyak lagi](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [Membuka Potensi NLP: Menyesuaikan dengan Microsoft Olive](https://github.com/azure/Ignite_FineTuning_workshop)

- Kertas Penyelidikan Akademik dan Penerbitan
  - [Textbooks Are All You Need II: laporan teknikal phi-1.5](https://arxiv.org/abs/2309.05463)
  - [Laporan Teknikal Phi-3: Model Bahasa yang Sangat Berkemampuan Secara Tempatan di Telefon Anda](https://arxiv.org/abs/2404.14219)
  - [Laporan Teknikal Phi-4](https://arxiv.org/abs/2412.08905)
  - [Laporan Teknikal Phi-4-Mini: Model Bahasa Multimodal yang Padat tetapi Berkuasa melalui Mixture-of-LoRAs](https://arxiv.org/abs/2503.01743)
  - [Mengoptimumkan Model Bahasa Kecil untuk Panggilan Fungsi Dalam Kenderaan](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) Menyesuaikan PHI-3 untuk Menjawab Soalan Pilihan Berganda: Metodologi, Hasil, dan Cabaran](https://arxiv.org/abs/2501.01588)
- [Laporan Teknikal Phi-4-reasoning](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)  
- [Laporan Teknikal Phi-4-mini-reasoning](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)  

## Menggunakan Model Phi  

### Phi di Azure AI Foundry  

Anda boleh mempelajari cara menggunakan Microsoft Phi dan membina penyelesaian E2E pada pelbagai peranti perkakasan anda. Untuk mencuba Phi sendiri, mulakan dengan bermain dengan model dan menyesuaikan Phi untuk senario anda menggunakan [Katalog Model Azure AI Foundry](https://aka.ms/phi3-azure-ai). Anda boleh mengetahui lebih lanjut di Panduan Memulakan [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md).  

**Playground**  
Setiap model mempunyai playground khusus untuk menguji model [Azure AI Playground](https://aka.ms/try-phi3).  

### Phi di Model GitHub  

Anda boleh mempelajari cara menggunakan Microsoft Phi dan membina penyelesaian E2E pada pelbagai peranti perkakasan anda. Untuk mencuba Phi sendiri, mulakan dengan bermain dengan model dan menyesuaikan Phi untuk senario anda menggunakan [Katalog Model GitHub](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo). Anda boleh mengetahui lebih lanjut di Panduan Memulakan [Katalog Model GitHub](/md/02.QuickStart/GitHubModel_QuickStart.md).  

**Playground**  
Setiap model mempunyai [playground khusus untuk menguji model](/md/02.QuickStart/GitHubModel_QuickStart.md).  

### Phi di Hugging Face  

Anda juga boleh menemui model di [Hugging Face](https://huggingface.co/microsoft).  

**Playground**  
[Playground Hugging Chat](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct).  

## AI Bertanggungjawab  

Microsoft komited untuk membantu pelanggan kami menggunakan produk AI kami secara bertanggungjawab, berkongsi pembelajaran kami, dan membina perkongsian berdasarkan kepercayaan melalui alat seperti Transparency Notes dan Penilaian Impak. Banyak sumber ini boleh didapati di [https://aka.ms/RAI](https://aka.ms/RAI).  
Pendekatan Microsoft terhadap AI bertanggungjawab berasaskan prinsip AI kami: keadilan, kebolehpercayaan dan keselamatan, privasi dan keselamatan, keterangkuman, ketelusan, dan akauntabiliti.  

Model bahasa semula jadi, imej, dan pertuturan berskala besar - seperti yang digunakan dalam sampel ini - berpotensi berkelakuan dengan cara yang tidak adil, tidak boleh dipercayai, atau menyinggung, yang boleh menyebabkan kemudaratan. Sila rujuk [Nota Ketelusan Perkhidmatan Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) untuk mengetahui risiko dan batasan.  

Pendekatan yang disyorkan untuk mengurangkan risiko ini adalah dengan memasukkan sistem keselamatan dalam seni bina anda yang dapat mengesan dan mencegah tingkah laku berbahaya. [Keselamatan Kandungan Azure AI](https://learn.microsoft.com/azure/ai-services/content-safety/overview) menyediakan lapisan perlindungan bebas, mampu mengesan kandungan yang dihasilkan pengguna dan AI yang berbahaya dalam aplikasi dan perkhidmatan. Keselamatan Kandungan Azure AI termasuk API teks dan imej yang membolehkan anda mengesan bahan yang berbahaya. Dalam Azure AI Foundry, perkhidmatan Keselamatan Kandungan membolehkan anda melihat, meneroka, dan mencuba kod contoh untuk mengesan kandungan berbahaya merentasi pelbagai mod. Dokumentasi [panduan memulakan](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) berikut membimbing anda melalui membuat permintaan kepada perkhidmatan.  

Aspek lain yang perlu diambil kira adalah prestasi keseluruhan aplikasi. Dengan aplikasi multi-modal dan multi-model, kami menganggap prestasi bermaksud sistem berfungsi seperti yang anda dan pengguna anda harapkan, termasuk tidak menghasilkan output yang berbahaya. Penting untuk menilai prestasi keseluruhan aplikasi anda menggunakan [Penilai Prestasi dan Kualiti serta Risiko dan Keselamatan](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in). Anda juga mempunyai keupayaan untuk mencipta dan menilai dengan [penilai tersuai](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators).  

Anda boleh menilai aplikasi AI anda dalam persekitaran pembangunan anda menggunakan [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html). Dengan dataset ujian atau sasaran, generasi aplikasi AI generatif anda diukur secara kuantitatif dengan penilai terbina dalam atau penilai tersuai pilihan anda. Untuk memulakan dengan azure ai evaluation sdk untuk menilai sistem anda, anda boleh mengikuti [panduan memulakan](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Setelah anda melaksanakan penilaian, anda boleh [memvisualisasikan hasilnya di Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).  

## Tanda Dagangan  

Projek ini mungkin mengandungi tanda dagangan atau logo untuk projek, produk, atau perkhidmatan. Penggunaan tanda dagangan atau logo Microsoft yang dibenarkan tertakluk kepada dan mesti mengikuti [Panduan Tanda Dagangan & Jenama Microsoft](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).  
Penggunaan tanda dagangan atau logo Microsoft dalam versi yang diubah suai projek ini tidak boleh menyebabkan kekeliruan atau menyiratkan penajaan oleh Microsoft. Sebarang penggunaan tanda dagangan atau logo pihak ketiga tertakluk kepada dasar pihak ketiga tersebut.  

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat yang kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.