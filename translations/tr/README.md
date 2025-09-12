<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "698f7f3d48ebc9e25a273d7c8b7e31c5",
  "translation_date": "2025-09-12T13:49:23+00:00",
  "source_file": "README.md",
  "language_code": "tr"
}
-->
# Phi Yemek Kitabı: Microsoft'un Phi Modelleriyle Uygulamalı Örnekler

[![GitHub Codespaces'te örnekleri açın ve kullanın](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Dev Containers'da Aç](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub katkıda bulunanlar](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub sorunlar](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub çekme istekleri](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PR'ler Hoş Geldiniz](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub izleyiciler](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub çatallar](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub yıldızlar](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi, Microsoft tarafından geliştirilen bir dizi açık kaynaklı yapay zeka modelidir.

Phi, çok dilli, akıl yürütme, metin/sohbet üretimi, kodlama, görseller, ses ve diğer senaryolarda oldukça iyi performans gösteren, şu anda en güçlü ve maliyet açısından en verimli küçük dil modeli (SLM) olarak öne çıkmaktadır.

Phi'yi bulutta veya uç cihazlarda dağıtabilir ve sınırlı bilgi işlem gücüyle kolayca üretken yapay zeka uygulamaları geliştirebilirsiniz.

Bu kaynakları kullanmaya başlamak için şu adımları izleyin:
1. **Depoyu Çatallayın**: [![GitHub çatallar](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo) bağlantısına tıklayın.
2. **Depoyu Klonlayın**: `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Microsoft AI Discord Topluluğuna Katılın ve uzmanlarla ve diğer geliştiricilerle tanışın**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![kapak](../../imgs/cover.png)

### 🌐 Çok Dilli Destek

#### GitHub Action ile Desteklenir (Otomatik ve Her Zaman Güncel)

[Fransızca](../fr/README.md) | [İspanyolca](../es/README.md) | [Almanca](../de/README.md) | [Rusça](../ru/README.md) | [Arapça](../ar/README.md) | [Farsça](../fa/README.md) | [Urduca](../ur/README.md) | [Çince (Basitleştirilmiş)](../zh/README.md) | [Çince (Geleneksel, Makao)](../mo/README.md) | [Çince (Geleneksel, Hong Kong)](../hk/README.md) | [Çince (Geleneksel, Tayvan)](../tw/README.md) | [Japonca](../ja/README.md) | [Korece](../ko/README.md) | [Hintçe](../hi/README.md) 
[Bengalce](../bn/README.md) | [Marathi](../mr/README.md) | [Nepalce](../ne/README.md) | [Pencapça (Gurmukhi)](../pa/README.md) | [Portekizce (Portekiz)](../pt/README.md) | [Portekizce (Brezilya)](../br/README.md) | [İtalyanca](../it/README.md) | [Lehçe](../pl/README.md) | [Türkçe](./README.md) | [Yunanca](../el/README.md) | [Tayca](../th/README.md) | [İsveççe](../sv/README.md) | [Danca](../da/README.md) | [Norveççe](../no/README.md) | [Fince](../fi/README.md) | [Felemenkçe](../nl/README.md) | [İbranice](../he/README.md) | [Vietnamca](../vi/README.md) | [Endonezce](../id/README.md) | [Malayca](../ms/README.md) | [Tagalog (Filipince)](../tl/README.md) | [Svahili](../sw/README.md) | [Macarca](../hu/README.md) | [Çekçe](../cs/README.md) | [Slovakça](../sk/README.md) | [Romence](../ro/README.md) | [Bulgarca](../bg/README.md) | [Sırpça (Kiril)](../sr/README.md) | [Hırvatça](../hr/README.md) | [Slovence](../sl/README.md)

## İçindekiler

- Giriş
  - [Phi Ailesine Hoş Geldiniz](./md/01.Introduction/01/01.PhiFamily.md)
  - [Ortamınızı Kurma](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [Temel Teknolojileri Anlama](./md/01.Introduction/01/01.Understandingtech.md)
  - [Phi Modelleri için Yapay Zeka Güvenliği](./md/01.Introduction/01/01.AISafety.md)
  - [Phi Donanım Desteği](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Phi Modelleri ve Platformlar Arası Kullanılabilirlik](./md/01.Introduction/01/01.Edgeandcloud.md)
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
    -  [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md)

- Phi Ailesi Çıkarımı
    - [iOS'ta Phi Çıkarımı](./md/01.Introduction/03/iOS_Inference.md)
    - [Android'de Phi Çıkarımı](./md/01.Introduction/03/Android_Inference.md)
    - [Jetson'da Phi Çıkarımı](./md/01.Introduction/03/Jetson_Inference.md)
    - [AI PC'de Phi Çıkarımı](./md/01.Introduction/03/AIPC_Inference.md)
    - [Apple MLX Framework ile Phi Çıkarımı](./md/01.Introduction/03/MLX_Inference.md)
    - [Yerel Sunucuda Phi Çıkarımı](./md/01.Introduction/03/Local_Server_Inference.md)
    - [AI Toolkit Kullanarak Uzaktan Sunucuda Phi Çıkarımı](./md/01.Introduction/03/Remote_Interence.md)
    - [Rust ile Phi Çıkarımı](./md/01.Introduction/03/Rust_Inference.md)
    - [Yerelde Phi--Vision Çıkarımı](./md/01.Introduction/03/Vision_Inference.md)
    - [Kaito AKS, Azure Containers ile Phi Çıkarımı (resmi destek)](./md/01.Introduction/03/Kaito_Inference.md)
-  [Phi Ailesini Kuantize Etme](./md/01.Introduction/04/QuantifyingPhi.md)
    - [Phi-3.5 / 4'ü llama.cpp kullanarak kuantize etme](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [Phi-3.5 / 4'ü onnxruntime için üretken yapay zeka uzantıları kullanarak kuantize etme](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Phi-3.5 / 4'ü Intel OpenVINO kullanarak kuantize etme](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Phi-3.5 / 4'ü Apple MLX Framework kullanarak kuantize etme](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

-  Phi Değerlendirme
    - [Sorumlu AI](./md/01.Introduction/05/ResponsibleAI.md)
    - [Değerlendirme için Azure AI Foundry](./md/01.Introduction/05/AIFoundry.md)
    - [Değerlendirme için Promptflow Kullanımı](./md/01.Introduction/05/Promptflow.md)
 
- Azure AI Search ile RAG
    - [Phi-4-mini ve Phi-4-multimodal(RAG) ile Azure AI Search Kullanımı](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Phi uygulama geliştirme örnekleri
  - Metin ve Sohbet Uygulamaları
    - Phi-4 Örnekleri 🆕
      - [📓] [Phi-4-mini ONNX Modeli ile Sohbet](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Phi-4 yerel ONNX Modeli ile Sohbet .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Phi-4 ONNX ile Sementik Kernel Kullanarak .NET Konsol Uygulaması](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Phi-3 / 3.5 Örnekleri
      - [Phi3, ONNX Runtime Web ve WebGPU kullanarak tarayıcıda yerel sohbet botu](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVino Sohbet](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [Çoklu Model - Etkileşimli Phi-3-mini ve OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - Phi-3 için bir sarmalayıcı oluşturma ve MLFlow kullanımı](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [Model Optimizasyonu - Olive ile Phi-3-mini modelini ONNX Runtime Web için optimize etme](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [Phi-3 mini-4k-instruct-onnx ile WinUI3 Uygulaması](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      - [WinUI3 Çoklu Model AI Destekli Notlar Uygulama Örneği](https://github.com/microsoft/ai-powered-notes-winui3-sample)
- [Phi-3 modellerini Prompt flow ile özelleştirme ve entegre etme](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
- [Azure AI Foundry'de Phi-3 modellerini Prompt flow ile özelleştirme ve entegre etme](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
- [Microsoft'un Sorumlu AI İlkelerine odaklanarak Azure AI Foundry'de özelleştirilmiş Phi-3 / Phi-3.5 Modelini değerlendirme](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
- [📓] [Phi-3.5-mini-instruct dil tahmini örneği (Çince/İngilizce)](../../md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
- [Phi-3.5-Instruct WebGPU RAG Sohbet Botu](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
- [Windows GPU kullanarak Phi-3.5-Instruct ONNX ile Prompt flow çözümü oluşturma](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
- [Microsoft Phi-3.5 tflite kullanarak Android uygulaması oluşturma](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
- [Microsoft.ML.OnnxRuntime kullanarak yerel ONNX Phi-3 modeli ile Soru-Cevap .NET Örneği](../../md/04.HOL/dotnet/src/LabsPhi301)
- [Semantic Kernel ve Phi-3 ile Konsol sohbet .NET uygulaması](../../md/04.HOL/dotnet/src/LabsPhi302)

- Azure AI Inference SDK Kod Tabanlı Örnekler 
  - Phi-4 Örnekleri 🆕
    - [📓] [Phi-4-multimodal kullanarak proje kodu oluşturma](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
  - Phi-3 / 3.5 Örnekleri
    - [Microsoft Phi-3 Ailesi ile kendi Visual Studio Code GitHub Copilot Sohbetinizi oluşturun](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
    - [GitHub Modelleri ile Phi-3.5 kullanarak kendi Visual Studio Code Sohbet Copilot Ajanınızı oluşturun](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

- Gelişmiş Akıl Yürütme Örnekleri
  - Phi-4 Örnekleri 🆕
    - [📓] [Phi-4-mini-reasoning veya Phi-4-reasoning Örnekleri](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
    - [📓] [Microsoft Olive ile Phi-4-mini-reasoning özelleştirme](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
    - [📓] [Apple MLX ile Phi-4-mini-reasoning özelleştirme](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
    - [📓] [GitHub Modelleri ile Phi-4-mini-reasoning](../../md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
    - [📓] [Azure AI Foundry Modelleri ile Phi-4-mini-reasoning](../../md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
- Demolar
    - [Hugging Face Spaces'de barındırılan Phi-4-mini demoları](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
    - [Hugging Face Spaces'de barındırılan Phi-4-multimodal demoları](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
- Görsel Örnekler
  - Phi-4 Örnekleri 🆕
    - [📓] [Phi-4-multimodal kullanarak görüntüleri okuyup kod oluşturma](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
  - Phi-3 / 3.5 Örnekleri
    - [📓][Phi-3-vision-Görüntü metnini metne çevirme](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
    - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
    - [📓][Phi-3-vision CLIP Gömme](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
    - [DEMO: Phi-3 Geri Dönüşüm](https://github.com/jennifermarsman/PhiRecycling/)
    - [Phi-3-vision - Görsel dil asistanı - Phi3-Vision ve OpenVINO ile](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
    - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
    - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
    - [📓][Phi-3.5 Vision çoklu çerçeve veya çoklu görüntü örneği](../../md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
    - [Microsoft.ML.OnnxRuntime .NET kullanarak yerel ONNX Modeli ile Phi-3 Vision](../../md/04.HOL/dotnet/src/LabsPhi303)
    - [Microsoft.ML.OnnxRuntime .NET kullanarak menü tabanlı Phi-3 Vision Yerel ONNX Modeli](../../md/04.HOL/dotnet/src/LabsPhi304)

- Matematik Örnekleri
  - Phi-4-Mini-Flash-Reasoning-Instruct Örnekleri 🆕 [Phi-4-Mini-Flash-Reasoning-Instruct ile Matematik Demo](../../md/02.Application/09.Math/MathDemo.ipynb)

- Ses Örnekleri
  - Phi-4 Örnekleri 🆕
    - [📓] [Phi-4-multimodal kullanarak ses transkriptleri çıkarma](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
    - [📓] [Phi-4-multimodal Ses Örneği](../../md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
    - [📓] [Phi-4-multimodal Konuşma Çevirisi Örneği](../../md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
    - [.NET konsol uygulaması kullanarak Phi-4-multimodal ile bir ses dosyasını analiz edip transkript oluşturma](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

- MOE Örnekleri
  - Phi-3 / 3.5 Örnekleri
    - [📓] [Phi-3.5 Mixture of Experts Modelleri (MoEs) Sosyal Medya Örneği](../../md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
    - [📓] [NVIDIA NIM Phi-3 MOE, Azure AI Search ve LlamaIndex ile Retrieval-Augmented Generation (RAG) Pipeline oluşturma](../../md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)

- Fonksiyon Çağırma Örnekleri
  - Phi-4 Örnekleri 🆕
    - [📓] [Phi-4-mini ile Fonksiyon Çağırma Kullanımı](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
    - [📓] [Phi-4-mini ile çoklu ajanlar oluşturmak için Fonksiyon Çağırma Kullanımı](../../md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
    - [📓] [Ollama ile Fonksiyon Çağırma Kullanımı](../../md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
    - [📓] [ONNX ile Fonksiyon Çağırma Kullanımı](../../md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)

- Multimodal Karışım Örnekleri
  - Phi-4 Örnekleri 🆕
    - [📓] [Phi-4-multimodal'ı bir Teknoloji gazetecisi olarak kullanma](../../md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
    - [.NET konsol uygulaması kullanarak Phi-4-multimodal ile görüntüleri analiz etme](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Phi Örneklerini Özelleştirme
  - [Özelleştirme Senaryoları](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [Özelleştirme vs RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [Phi-3'ü bir sektör uzmanı yapma](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [Phi-3'ü VS Code için AI Toolkit ile özelleştirme](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Phi-3'ü Azure Machine Learning Service ile özelleştirme](./md/03.FineTuning/Introduce_AzureML.md)
  - [Phi-3'ü Lora ile özelleştirme](./md/03.FineTuning/FineTuning_Lora.md)
  - [Phi-3'ü QLora ile özelleştirme](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Phi-3'ü Azure AI Foundry ile özelleştirme](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Phi-3'ü Azure ML CLI/SDK ile özelleştirme](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Microsoft Olive ile özelleştirme](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Microsoft Olive ile Uygulamalı Laboratuvar](./md/03.FineTuning/olive-lab/readme.md)
  - [Phi-3-vision'ı Weights and Bias ile özelleştirme](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [Phi-3'ü Apple MLX Framework ile özelleştirme](./md/03.FineTuning/FineTuning_MLX.md)
  - [Phi-3-vision'ı özelleştirme (resmi destek)](./md/03.FineTuning/FineTuning_Vision.md)
  - [Phi-3'ü Kaito AKS, Azure Containers ile özelleştirme (resmi destek)](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Phi-3 ve 3.5 Vision'ı Özelleştirme](https://github.com/2U1/Phi3-Vision-Finetune)

- Uygulamalı Laboratuvar
  - [En son modelleri keşfetme: LLM'ler, SLM'ler, yerel geliştirme ve daha fazlası](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [NLP Potansiyelini Açığa Çıkarma: Microsoft Olive ile Özelleştirme](https://github.com/azure/Ignite_FineTuning_workshop)

- Akademik Araştırma Makaleleri ve Yayınlar
  - [Textbooks Are All You Need II: phi-1.5 teknik raporu](https://arxiv.org/abs/2309.05463)
  - [Phi-3 Teknik Raporu: Telefonunuzda Yerel Olarak Çalışan Yüksek Kapasiteli Bir Dil Modeli](https://arxiv.org/abs/2404.14219)
  - [Phi-4 Teknik Raporu](https://arxiv.org/abs/2412.08905)
  - [Phi-4-Mini Teknik Raporu: Mixture-of-LoRAs ile Kompakt ama Güçlü Multimodal Dil Modelleri](https://arxiv.org/abs/2503.01743)
  - [Araç İçi Fonksiyon Çağırma için Küçük Dil Modellerini Optimize Etme](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) PHI-3'ü Çoktan Seçmeli Soru Cevaplama için Özelleştirme: Metodoloji, Sonuçlar ve Zorluklar](https://arxiv.org/abs/2501.01588)
- [Phi-4-reasoning Teknik Raporu](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
- [Phi-4-mini-reasoning Teknik Raporu](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Phi Modellerini Kullanma

### Azure AI Foundry'de Phi

Microsoft Phi'yi nasıl kullanacağınızı ve farklı donanım cihazlarınızda uçtan uca çözümler oluşturmayı öğrenebilirsiniz. Phi'yi kendiniz deneyimlemek için, modellerle oynayarak ve Phi'yi senaryolarınıza göre özelleştirerek başlayabilirsiniz. [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai) üzerinden daha fazla bilgi edinebilirsiniz. [Azure AI Foundry ile Başlarken](/md/02.QuickStart/AzureAIFoundry_QuickStart.md) rehberine göz atabilirsiniz.

**Playground**  
Her modelin, modeli test etmek için ayrılmış bir playground alanı vardır: [Azure AI Playground](https://aka.ms/try-phi3).

### GitHub Modellerinde Phi

Microsoft Phi'yi nasıl kullanacağınızı ve farklı donanım cihazlarınızda uçtan uca çözümler oluşturmayı öğrenebilirsiniz. Phi'yi kendiniz deneyimlemek için, modellerle oynayarak ve Phi'yi senaryolarınıza göre özelleştirerek başlayabilirsiniz. [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) üzerinden daha fazla bilgi edinebilirsiniz. [GitHub Model Catalog ile Başlarken](/md/02.QuickStart/GitHubModel_QuickStart.md) rehberine göz atabilirsiniz.

**Playground**  
Her modelin, modeli test etmek için ayrılmış bir [playground alanı](/md/02.QuickStart/GitHubModel_QuickStart.md) vardır.

### Hugging Face'de Phi

Modeli ayrıca [Hugging Face](https://huggingface.co/microsoft) üzerinde bulabilirsiniz.

**Playground**  
[Hugging Chat playground](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## Sorumlu AI 

Microsoft, müşterilerimizin AI ürünlerimizi sorumlu bir şekilde kullanmalarına yardımcı olmaya, öğrendiklerimizi paylaşmaya ve şeffaflık notları ve etki değerlendirmeleri gibi araçlar aracılığıyla güvene dayalı ortaklıklar kurmaya kararlıdır. Bu kaynakların birçoğunu [https://aka.ms/RAI](https://aka.ms/RAI) adresinde bulabilirsiniz.  
Microsoft’un sorumlu AI yaklaşımı, adalet, güvenilirlik ve güvenlik, gizlilik ve güvenlik, kapsayıcılık, şeffaflık ve hesap verebilirlik gibi AI ilkelerine dayanmaktadır.

Bu örnekte kullanılanlar gibi büyük ölçekli doğal dil, görüntü ve konuşma modelleri, potansiyel olarak adaletsiz, güvenilmez veya saldırgan davranışlar sergileyebilir ve bu da zararlara yol açabilir. Riskler ve sınırlamalar hakkında bilgi sahibi olmak için [Azure OpenAI hizmeti Şeffaflık Notu](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) belgesine başvurabilirsiniz.

Bu riskleri azaltmanın önerilen yaklaşımı, zararlı davranışları tespit edip önleyebilecek bir güvenlik sistemi mimarinize dahil etmektir. [Azure AI İçerik Güvenliği](https://learn.microsoft.com/azure/ai-services/content-safety/overview), uygulamalarda ve hizmetlerde kullanıcı tarafından oluşturulan ve AI tarafından oluşturulan zararlı içerikleri tespit edebilen bağımsız bir koruma katmanı sağlar. Azure AI İçerik Güvenliği, zararlı materyalleri tespit etmenize olanak tanıyan metin ve görüntü API'lerini içerir. Azure AI Foundry içinde, İçerik Güvenliği hizmeti, farklı modlarda zararlı içerikleri tespit etmek için örnek kodları görüntülemenize, keşfetmenize ve denemenize olanak tanır. [Hızlı başlangıç belgeleri](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest), hizmete istek yapma sürecinde size rehberlik eder.

Dikkate alınması gereken bir diğer konu ise genel uygulama performansıdır. Çok modlu ve çok modeller içeren uygulamalarda, performansın sizin ve kullanıcılarınızın beklentilerini karşılaması, zararlı çıktılar üretmemesi anlamına gelir. Genel uygulamanızın performansını değerlendirmek için [Performans ve Kalite ve Risk ve Güvenlik değerlendiricileri](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) kullanabilirsiniz. Ayrıca [özel değerlendiriciler](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators) oluşturma ve değerlendirme yeteneğine sahipsiniz.

AI uygulamanızı geliştirme ortamınızda [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html) kullanarak değerlendirebilirsiniz. Test veri seti veya bir hedef verilerek, üretken AI uygulamanızın çıktıları, seçtiğiniz yerleşik değerlendiriciler veya özel değerlendiriciler ile nicel olarak ölçülür. Azure AI Evaluation SDK ile sisteminizi değerlendirmeye başlamak için [hızlı başlangıç rehberini](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) takip edebilirsiniz. Bir değerlendirme çalıştırmasını gerçekleştirdikten sonra, [sonuçları Azure AI Foundry'de görselleştirebilirsiniz](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Ticari Markalar

Bu proje, projeler, ürünler veya hizmetler için ticari markalar veya logolar içerebilir. Microsoft ticari markalarının veya logolarının yetkili kullanımı, [Microsoft'un Ticari Marka ve Marka Yönergeleri](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) ile uyumlu olmalı ve bu yönergeleri takip etmelidir.  
Bu projenin değiştirilmiş sürümlerinde Microsoft ticari markalarının veya logolarının kullanımı, karışıklığa neden olmamalı veya Microsoft sponsorluğunu ima etmemelidir. Üçüncü taraf ticari markalarının veya logolarının kullanımı, ilgili üçüncü tarafların politikalarına tabidir.

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.