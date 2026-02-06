# Phi Yemek Kitabı: Microsoft'un Phi Modelleri ile Pratik Örnekler

[![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub issues](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub watchers](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub stars](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi, Microsoft tarafından geliştirilen açık kaynaklı yapay zeka modelleri serisidir.

Phi şu anda çok dilli, akıl yürütme, metin/sohbet üretimi, kodlama, görseller, ses ve diğer senaryolarda çok iyi kıyaslamalarla en güçlü ve maliyet etkin küçük dil modeli (SLM) konumundadır.

Phi'yi bulutta veya uç cihazlarda dağıtabilir ve sınırlı hesaplama gücüyle kolayca üretken yapay zeka uygulamaları oluşturabilirsiniz.

Bu kaynakları kullanmaya başlamak için şu adımları izleyin:
1. **Depoyu Forklayın**: Tıklayın [![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **Depoyu Klonlayın**: `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Microsoft AI Discord Topluluğuna Katılın ve uzmanlar ile diğer geliştiricilerle tanışın**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/tr/cover.eb18d1b9605d754b.webp)

### 🌐 Çoklu Dil Desteği

#### GitHub Action ile Desteklenir (Otomatik ve Her Zaman Güncel)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](./README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **Yerel olarak Klonlamayı mı Tercih Edersiniz?**

> Bu depo 50+ dil çevirisi içerir ve bu da indirme boyutunu önemli ölçüde artırır. Çeviriler olmadan klonlamak için sparse checkout kullanın:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/PhiCookBook.git
> cd PhiCookBook
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> Bu, kursu tamamlamak için ihtiyacınız olan her şeyi çok daha hızlı bir indirme ile sunar.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## İçindekiler

- Giriş
  - [Phi Ailesine Hoş Geldiniz](./md/01.Introduction/01/01.PhiFamily.md)
  - [Ortamınızı Kurma](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [Temel Teknolojileri Anlamak](./md/01.Introduction/01/01.Understandingtech.md)
  - [Phi Modelleri için AI Güvenliği](./md/01.Introduction/01/01.AISafety.md)
  - [Phi Donanım Desteği](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Phi Modelleri ve Platformlarda Bulunabilirlik](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Guidance-ai ve Phi Kullanımı](./md/01.Introduction/01/01.Guidance.md)
  - [GitHub Marketplace Modelleri](https://github.com/marketplace/models)
  - [Azure AI Model Kataloğu](https://ai.azure.com)

- Farklı Ortamlarda Phi Çıkarımı
    -  [Hugging Face](./md/01.Introduction/02/01.HF.md)
    -  [GitHub Modelleri](./md/01.Introduction/02/02.GitHubModel.md)
    -  [Azure AI Foundry Model Kataloğu](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    -  [Foundry Yerel](./md/01.Introduction/02/07.FoundryLocal.md)

- Phi Ailesi Çıkarımı
    - [iOS'ta Phi Çıkarımı](./md/01.Introduction/03/iOS_Inference.md)
    - [Android'te Phi Çıkarımı](./md/01.Introduction/03/Android_Inference.md)
    - [Jetson'da Phi Çıkarımı](./md/01.Introduction/03/Jetson_Inference.md)
    - [AI PC'de Phi Çıkarımı](./md/01.Introduction/03/AIPC_Inference.md)
    - [Apple MLX Framework ile Phi Çıkarımı](./md/01.Introduction/03/MLX_Inference.md)
    - [Yerel Sunucuda Phi Çıkarımı](./md/01.Introduction/03/Local_Server_Inference.md)
    - [AI Toolkit kullanarak Uzak Sunucuda Phi Çıkarımı](./md/01.Introduction/03/Remote_Interence.md)
    - [Rust ile Phi Çıkarımı](./md/01.Introduction/03/Rust_Inference.md)
    - [Yerelde Phi--Vision Çıkarımı](./md/01.Introduction/03/Vision_Inference.md)
    - [Kaito AKS, Azure Containers ile Phi Çıkarımı (resmi destek)](./md/01.Introduction/03/Kaito_Inference.md)
-  [Phi Ailesi Nicelendirme](./md/01.Introduction/04/QuantifyingPhi.md)
    - [llama.cpp kullanarak Phi-3.5 / 4 Nicelendirme](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [onnxruntime için Üretken AI uzantıları kullanarak Phi-3.5 / 4 Nicelendirme](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Intel OpenVINO kullanarak Phi-3.5 / 4 Nicelendirme](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Apple MLX Framework kullanarak Phi-3.5 / 4 Nicelendirme](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

-  Phi Değerlendirme
    - [Sorumlu AI](./md/01.Introduction/05/ResponsibleAI.md)
    - [Azure AI Foundry Değerlendirmesi](./md/01.Introduction/05/AIFoundry.md)
    - [Değerlendirme için Promptflow Kullanımı](./md/01.Introduction/05/Promptflow.md)
 
- Azure AI Search ile RAG
    - [Phi-4-mini ve Phi-4-multimodal(RAG) 'yi Azure AI Search ile Kullanma](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Phi uygulama geliştirme örnekleri
  - Metin ve Sohbet Uygulamaları
    - Phi-4 Örnekleri 🆕
      - [📓] [Phi-4-mini ONNX Modeli ile Sohbet](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Phi-4 yerel ONNX Modeli ile .NET Sohbet](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Sementic Kernel kullanarak Phi-4 ONNX ile .NET Konsol Uygulaması Sohbet](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Phi-3 / 3.5 Örnekleri
      - [Phi3, ONNX Runtime Web ve WebGPU kullanarak tarayıcıda Yerel Sohbetbot](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVino Sohbet](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [Çoklu Model - Etkileşimli Phi-3-mini ve OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - Bir sarmalayıcı oluşturma ve Phi-3'ü MLFlow ile kullanma](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [Model Optimizasyonu - Phi-3-min modelini ONNX Runtime Web için Olive ile nasıl optimize edilir](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [Phi-3 mini-4k-instruct-onnx ile WinUI3 Uygulaması](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      - [WinUI3 Çoklu Model AI Destekli Notlar Uygulaması Örneği](https://github.com/microsoft/ai-powered-notes-winui3-sample)
      - [Özel Phi-3 modellerini Prompt flow ile ince ayar yapın ve entegre edin](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
      - [Azure AI Foundry'de Prompt flow ile özel Phi-3 modellerini ince ayar yapın ve entegre edin](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
      - [Azure AI Foundry'de Microsoft'un Sorumlu AI İlkelerine odaklanarak İnce Ayarlı Phi-3 / Phi-3.5 Modelini Değerlendirin](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
      - [📓] [Phi-3.5-mini-instruct dil tahmin örneği (Çince/İngilizce)](./md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
      - [Phi-3.5-Instruct WebGPU RAG Chatbot](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
      - [Windows GPU kullanarak Phi-3.5-Instruct ONNX ile Prompt flow çözümü oluşturma](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
      - [Microsoft Phi-3.5 tflite kullanarak Android uygulaması oluşturma](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
      - [Microsoft.ML.OnnxRuntime kullanarak yerel ONNX Phi-3 modeli ile Soru-Cevap .NET Örneği](../../md/04.HOL/dotnet/src/LabsPhi301)
      - [Semantic Kernel ve Phi-3 ile Konsol sohbet .NET uygulaması](../../md/04.HOL/dotnet/src/LabsPhi302)

  - Azure AI Inference SDK Kod Tabanlı Örnekler 
    - Phi-4 Örnekleri 🆕
      - [📓] [Phi-4-multimodal kullanarak proje kodu oluşturma](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
    - Phi-3 / 3.5 Örnekler
      - [Microsoft Phi-3 Ailesi ile kendi Visual Studio Code GitHub Copilot Sohbetinizi oluşturun](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
      - [GitHub Modelleri ile Phi-3.5 kullanarak kendi Visual Studio Code Chat Copilot Ajanınızı oluşturun](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

  - Gelişmiş Muhakeme Örnekleri
    - Phi-4 Örnekleri 🆕
      - [📓] [Phi-4-mini-muhakeme veya Phi-4-muhakeme Örnekleri](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
      - [📓] [Microsoft Olive ile Phi-4-mini-muhakeme ince ayarı](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Apple MLX ile Phi-4-mini-muhakeme ince ayarı](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [GitHub Modelleri ile Phi-4-mini-muhakeme](./md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
      - [📓] [Azure AI Foundry Modelleri ile Phi-4-mini-muhakeme](./md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
  - Demo'lar
      - [Phi-4-mini demo'ları Hugging Face Spaces'da barındırılıyor](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
      - [Phi-4-multimodal demo'ları Hugginge Face Spaces'da barındırılıyor](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
  - Görüş Örnekleri
    - Phi-4 Örnekleri 🆕
      - [📓] [Phi-4-multimodal kullanarak görüntüleri okuma ve kod oluşturma](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
    - Phi-3 / 3.5 Örnekler
      -  [📓][Phi-3-görünüm-Görüntü metin metne](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [Phi-3-görünüm-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
      - [📓][Phi-3-görünüm CLIP Gömme](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [DEMO: Phi-3 Geri Dönüşüm](https://github.com/jennifermarsman/PhiRecycling/)
      - [Phi-3-görünüm - Görsel dil asistanı - Phi3-Görünüm ve OpenVINO ile](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
      - [Phi-3 Görünüm Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
      - [Phi-3 Görünüm OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
      - [📓][Phi-3.5 Görünüm çoklu kare veya çoklu görüntü örneği](./md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
      - [Microsoft.ML.OnnxRuntime .NET kullanarak Phi-3 Görünüm Yerel ONNX Modeli](../../md/04.HOL/dotnet/src/LabsPhi303)
      - [Menü tabanlı Phi-3 Görünüm Yerel ONNX Modeli Microsoft.ML.OnnxRuntime .NET kullanarak](../../md/04.HOL/dotnet/src/LabsPhi304)

  - Matematik Örnekleri
    -  Phi-4-Mini-Flash-Muhakeme-Talimat Örnekleri 🆕 [Phi-4-Mini-Flash-Muhakeme-Talimat ile Matematik Demo](./md/02.Application/09.Math/MathDemo.ipynb)

  - Ses Örnekleri
    - Phi-4 Örnekleri 🆕
      - [📓] [Phi-4-multimodal kullanarak ses transkriptleri çıkarma](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
      - [📓] [Phi-4-multimodal Ses Örneği](./md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
      - [📓] [Phi-4-multimodal Konuşma Çevirisi Örneği](./md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
      - [Ses dosyasını analiz etmek ve transkript oluşturmak için Phi-4-multimodal kullanan .NET konsol uygulaması](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

  - MOE Örnekleri
    - Phi-3 / 3.5 Örnekler
      - [📓] [Phi-3.5 Uzman Karışımı Modelleri (MoEs) Sosyal Medya Örneği](./md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
      - [📓] [NVIDIA NIM Phi-3 MOE, Azure AI Search ve LlamaIndex ile Bir Retrieval-Augmented Generation (RAG) İş Akışı Oluşturma](./md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)
      - 
  - Fonksiyon Çağrısı Örnekleri
    - Phi-4 Örnekleri 🆕
      -  [📓] [Phi-4-mini ile Fonksiyon Çağrısı Kullanımı](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
      -  [📓] [Phi-4-mini ile Çoklu Ajanlar oluşturmak için Fonksiyon Çağrısı Kullanımı](./md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
      -  [📓] [Ollama ile Fonksiyon Çağrısı Kullanımı](./md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
      -  [📓] [ONNX ile Fonksiyon Çağrısı Kullanımı](./md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)
  - Çok Modlu Karıştırma Örnekleri
    - Phi-4 Örnekleri 🆕
      -  [📓] [Phi-4-multimodal'i Teknoloji gazetecisi olarak kullanmak](./md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
      - [Phi-4-multimodal kullanarak görüntüleri analiz eden .NET konsol uygulaması](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Phi İnce Ayarı Örnekleri
  - [İnce Ayar Senaryoları](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [İnce Ayar vs RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [Phi-3'ün sektör uzmanı olmasını sağlayan ince ayar](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [AI Toolkit for VS Code ile Phi-3'ü ince ayar yapma](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Azure Machine Learning Service ile Phi-3'ü ince ayar yapma](./md/03.FineTuning/Introduce_AzureML.md)
  - [Lora ile Phi-3'ü ince ayar yapma](./md/03.FineTuning/FineTuning_Lora.md)
  - [QLora ile Phi-3'ü ince ayar yapma](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Azure AI Foundry ile Phi-3'ü ince ayar yapma](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Azure ML CLI/SDK ile Phi-3'ü ince ayar yapma](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Microsoft Olive ile ince ayar yapma](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Microsoft Olive Uygulamalı Laboratuvar ile ince ayar yapma](./md/03.FineTuning/olive-lab/readme.md)
  - [Weights and Bias ile Phi-3-görünümü ince ayar yapma](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [Apple MLX Framework ile Phi-3'ü ince ayar yapma](./md/03.FineTuning/FineTuning_MLX.md)
  - [Phi-3-görünümü ince ayar yapma (resmi destek)](./md/03.FineTuning/FineTuning_Vision.md)
  - [Kaito AKS, Azure Containers ile Phi-3'ü ince ayar yapma (resmi destek)](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Phi-3 ve 3.5 Görünüm İnce Ayarı](https://github.com/2U1/Phi3-Vision-Finetune)

- Uygulamalı Laboratuvar
  - [En yeni modelleri keşfetme: LLM'ler, SLM'ler, yerel geliştirme ve daha fazlası](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [NLP Potansiyelini Açığa Çıkarma: Microsoft Olive ile İnce Ayar](https://github.com/azure/Ignite_FineTuning_workshop)

- Akademik Araştırma Makaleleri ve Yayınlar
  - [Kitaplar İhtiyacınız Olan Her Şeydir II: phi-1.5 teknik raporu](https://arxiv.org/abs/2309.05463)
  - [Phi-3 Teknik Raporu: Telefonunuzda Yerel Olarak Yüksek Kapasiteli Bir Dil Modeli](https://arxiv.org/abs/2404.14219)
  - [Phi-4 Teknik Raporu](https://arxiv.org/abs/2412.08905)
  - [Phi-4-Mini Teknik Raporu: LoRA Karışımıyla Kompakt Ama Güçlü Çok Modlu Dil Modelleri](https://arxiv.org/abs/2503.01743)
  - [Araç İçi Fonksiyon Çağırma İçin Küçük Dil Modellerinin Optimizasyonu](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) Çoktan Seçmeli Soru Cevaplama için PHI-3'ün İncelenmesi: Yöntem, Sonuçlar ve Zorluklar](https://arxiv.org/abs/2501.01588)
  - [Phi-4-mantık Teknik Raporu](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Phi-4-mini-mantık Teknik Raporu](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Phi Modellerini Kullanma

### Azure AI Foundry'de Phi

Microsoft Phi'nin nasıl kullanılacağını ve farklı donanım cihazlarınızda uçtan uca çözümler nasıl oluşturulacağını öğrenebilirsiniz. Phi’yi kendiniz deneyimlemek için, modellerle oynamaya başlayın ve **[Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai)** kullanarak senaryolarınıza göre Phi'yi özelleştirin. Daha fazlasını **[Azure AI Foundry ile Başlarken](/md/02.QuickStart/AzureAIFoundry_QuickStart.md)** bölümünde öğrenebilirsiniz.

**Oyun Alanı**  
Her modelin modelin test edilmesi için ayrılmış bir oyun alanı vardır: [Azure AI Playground](https://aka.ms/try-phi3).

### GitHub Modellerinde Phi

Microsoft Phi'nin nasıl kullanılacağını ve farklı donanım cihazlarınızda uçtan uca çözümler nasıl oluşturulacağını öğrenebilirsiniz. Phi’yi kendiniz deneyimlemek için, modelle oynamaya başlayın ve senaryolarınıza uygun şekilde Phi’yi özelleştirmek için **[GitHub Model Kataloğu](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo)** kullanabilirsiniz. Daha fazlasını **[GitHub Model Kataloğu ile Başlarken](/md/02.QuickStart/GitHubModel_QuickStart.md)** bölümünde öğrenebilirsiniz.

**Oyun Alanı**  
Her modelin test edilmesi için ayrılmış bir [oyun alanı vardır](/md/02.QuickStart/GitHubModel_QuickStart.md).

### Hugging Face Üzerinde Phi

Modeli ayrıca [Hugging Face](https://huggingface.co/microsoft) üzerinde de bulabilirsiniz.

**Oyun Alanı**  
[Hugging Chat oyun alanı](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## 🎒 Diğer Kurslar

Ekibimiz başka kurslar da üretiyor! Göz atın:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![Yeni Başlayanlar için LangChain4j](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![Yeni Başlayanlar için LangChain.js](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

---

### Azure / Edge / MCP / Ajanlar
[![Yeni Başlayanlar için AZD](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Yeni Başlayanlar için Edge AI](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Yeni Başlayanlar için MCP](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Yeni Başlayanlar için AI Ajanlar](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---

### Üretken AI Serisi
[![Yeni Başlayanlar için Üretken AI](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Üretken AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Üretken AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Üretken AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---

### Temel Öğrenme
[![Yeni Başlayanlar için ML](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Yeni Başlayanlar için Veri Bilimi](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![Yeni Başlayanlar için AI](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Yeni Başlayanlar için Siber Güvenlik](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Yeni Başlayanlar için Web Geliştirme](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![Yeni Başlayanlar için IoT](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![Yeni Başlayanlar için XR Geliştirme](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---

### Copilot Serisi
[![Yapay Zeka Eşli Programlama için Copilot](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![C#/.NET için Copilot](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Macerası](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Sorumlu AI

Microsoft, müşterilerimizin yapay zeka ürünlerimizi sorumlu bir şekilde kullanmalarına yardımcı olmayı, öğrendiklerimizi paylaşmayı ve Şeffaflık Notları ve Etki Değerlendirmeleri gibi araçlarla güvene dayalı ortaklıklar kurmayı taahhüt eder. Bu kaynakların çoğu [https://aka.ms/RAI](https://aka.ms/RAI) adresinde bulunabilir.  
Microsoft’un sorumlu AI yaklaşımı, adalet, güvenilirlik ve güvenlik, gizlilik ve güvenlik, kapsayıcılık, şeffaflık ve hesap verebilirlik olmak üzere AI prensiplerimize dayanır.

Bu örnekte kullanılan büyük ölçekli doğal dil, görüntü ve konuşma modelleri, adaletsiz, güvenilmez veya saldırgan davranışlarda bulunabilir ve buna bağlı olarak zararlara neden olabilir. Riskler ve sınırlamalar hakkında bilgi edinmek için lütfen [Azure OpenAI hizmeti Şeffaflık notuna](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) bakınız.

Bu riskleri hafifletmek için önerilen yaklaşım, zararlı davranışı tespit edip önleyebilen bir güvenlik sistemini mimarinize dahil etmektir. [Azure AI İçerik Güvenliği](https://learn.microsoft.com/azure/ai-services/content-safety/overview), uygulamalarda ve hizmetlerde zararlı kullanıcı ve AI tarafından oluşturulan içeriği algılayabilen bağımsız bir koruma katmanı sağlar. Azure AI İçerik Güvenliği, zararlı materyali tespit etmenizi sağlayan metin ve görüntü API’lerini içerir. Azure AI Foundry içinde, İçerik Güvenliği hizmeti farklı modalitelerde zararlı içeriği algılamak için örnek kodları görüntülemenize, keşfetmenize ve denemenize olanak tanır. Aşağıdaki [hızlı başlangıç dokümanı](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) servise istek yapma sürecinde size rehberlik eder.

Dikkate alınması gereken bir diğer husus ise genel uygulama performansıdır. Çok modlu ve çok modeller uygulamalarla, performans derken sistemin sizin ve kullanıcılarınızın beklentilerine uygun şekilde çalışması, zararlı çıktılar üretmemesi kastedilir. Genel uygulamanızın performansını değerlendirmek için [Performans ve Kalite ve Risk ve Güvenlik değerlendirme araçlarını](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) kullanmanız önemlidir. Ayrıca [özel değerlendiriciler](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators) oluşturarak değerlendirme yapma imkanınız da vardır.
Yapay zeka uygulamanızı geliştirme ortamınızda [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html) kullanarak değerlendirebilirsiniz. Test veri seti veya hedef verildiğinde, üretici yapay zeka uygulaması çıktılarını yerleşik değerlendiriciler veya tercih ettiğiniz özel değerlendiricilerle niceliksel olarak ölçebilirsiniz. Sisteminizi değerlendirmek için azure ai evaluation sdk ile başlamanız adına, [hızlı başlangıç kılavuzunu](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) takip edebilirsiniz. Bir değerlendirme çalıştırması gerçekleştirdiğinizde, sonuçları [Azure AI Foundry'de görselleştirebilirsiniz](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Ticari Markalar

Bu proje, projeler, ürünler veya hizmetler için ticari markalar veya logolar içerebilir. Microsoft ticari markalarının veya logolarının yetkili kullanımı, [Microsoft'un Ticari Marka ve Marka Kılavuzları](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) kurallarına bağlıdır ve bu kurallara uyulmalıdır. Microsoft ticari markalarının veya logolarının bu projenin değiştirilmiş versiyonlarında kullanımı, karışıklığa neden olmamalı veya Microsoft sponsorluğunu ima etmemelidir. Üçüncü taraf ticari marka veya logolarının herhangi bir kullanımı, ilgili üçüncü tarafların politikalarına tabidir.

## Yardım Alma

Takıldığınızda veya yapay zeka uygulamaları oluşturma hakkında herhangi bir sorunuz olduğunda katılabilirsiniz:

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

Ürün geri bildirimi vermek veya oluşturma sırasında hatalarla karşılaşırsanız ziyaret edin:

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragat**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstermemize rağmen, otomatik çevirilerin hatalar veya yanlış anlamalar içerebileceğini lütfen unutmayın. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanılmasından kaynaklanan herhangi bir yanlış anlama veya yanlış yorumlamadan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->