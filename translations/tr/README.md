<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ef3a50368712b1a7483d0def1f70c490",
  "translation_date": "2025-12-21T11:36:41+00:00",
  "source_file": "README.md",
  "language_code": "tr"
}
-->
# Phi Cookbook: Microsoft'un Phi Modelleri ile Uygulamalı Örnekler

[![GitHub Codespaces'ta örnekleri açın ve kullanın](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Dev Containers'ta Aç](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub katkıda bulunanlar](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub sorunları](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub çekme istekleri](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PR'ler Hoş Geldiniz](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub izleyiciler](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub çatallar](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub yıldızları](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi, Microsoft tarafından geliştirilen açık kaynaklı bir dizi yapay zeka modelidir. 

Phi şu anda çok dilli, akıl yürütme, metin/sohbet üretimi, kodlama, görüntüler, ses ve diğer senaryolarda çok iyi kıyaslamalara sahip en güçlü ve maliyet-etkin küçük dil modeli (SLM) serisidir. 

Phi'yi buluta veya uç cihazlara dağıtabilirsiniz ve sınırlı hesaplama gücü ile üretken yapay zeka uygulamaları kolayca oluşturabilirsiniz.

Bu kaynakları kullanmaya başlamak için şu adımları izleyin:
1. **Depoyu Forklayın**: Tıklayın [![GitHub çatallar](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **Depoyu Klonlayın**:   `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Microsoft AI Discord Topluluğuna Katılın ve uzmanlar ile diğer geliştiricilerle tanışın**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![kapak](../../translated_images/cover.eb18d1b9605d754b.tr.png)

### 🌐 Çok Dilli Destek

#### GitHub Action ile Desteklenir (Otomatik & Her Zaman Güncel)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arapça](../ar/README.md) | [Bengalce](../bn/README.md) | [Bulgarca](../bg/README.md) | [Burmaca (Myanmar)](../my/README.md) | [Çince (Basitleştirilmiş)](../zh/README.md) | [Çince (Geleneksel, Hong Kong)](../hk/README.md) | [Çince (Geleneksel, Makao)](../mo/README.md) | [Çince (Geleneksel, Tayvan)](../tw/README.md) | [Hırvatça](../hr/README.md) | [Çekçe](../cs/README.md) | [Danca](../da/README.md) | [Flemenkçe](../nl/README.md) | [Estonca](../et/README.md) | [Fince](../fi/README.md) | [Fransızca](../fr/README.md) | [Almanca](../de/README.md) | [Yunanca](../el/README.md) | [İbranice](../he/README.md) | [Hintçe](../hi/README.md) | [Macarca](../hu/README.md) | [Endonezce](../id/README.md) | [İtalyanca](../it/README.md) | [Japonca](../ja/README.md) | [Kannada](../kn/README.md) | [Korece](../ko/README.md) | [Litvanca](../lt/README.md) | [Malayca](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nijerya Pidgini](../pcm/README.md) | [Norveççe](../no/README.md) | [Farsça (Farsi)](../fa/README.md) | [Lehçe](../pl/README.md) | [Portekizce (Brezilya)](../br/README.md) | [Portekizce (Portekiz)](../pt/README.md) | [Pencapça (Gurmukhi)](../pa/README.md) | [Romence](../ro/README.md) | [Rusça](../ru/README.md) | [Sırpça (Kiril)](../sr/README.md) | [Slovakça](../sk/README.md) | [Slovence](../sl/README.md) | [İspanyolca](../es/README.md) | [Svahili](../sw/README.md) | [İsveççe](../sv/README.md) | [Tagalog (Filipince)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Tayca](../th/README.md) | [Türkçe](./README.md) | [Ukraynaca](../uk/README.md) | [Urduca](../ur/README.md) | [Vietnamca](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## İçindekiler

- Giriş
  - [Phi Ailesine Hoş Geldiniz](./md/01.Introduction/01/01.PhiFamily.md)
  - [Ortamınızı Kurma](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [Temel Teknolojileri Anlamak](./md/01.Introduction/01/01.Understandingtech.md)
  - [Phi Modelleri için Yapay Zeka Güvenliği](./md/01.Introduction/01/01.AISafety.md)
  - [Phi Donanım Desteği](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Phi Modelleri & Platformlar Arası Kullanılabilirlik](./md/01.Introduction/01/01.Edgeandcloud.md)
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

- Phi Ailesiyle Çıkarım
    - [iOS'ta Phi Çıkarımı](./md/01.Introduction/03/iOS_Inference.md)
    - [Android'te Phi Çıkarımı](./md/01.Introduction/03/Android_Inference.md)
    - [Jetson'da Phi Çıkarımı](./md/01.Introduction/03/Jetson_Inference.md)
    - [AI PC'de Phi Çıkarımı](./md/01.Introduction/03/AIPC_Inference.md)
    - [Apple MLX Çerçevesi ile Phi Çıkarımı](./md/01.Introduction/03/MLX_Inference.md)
    - [Yerel Sunucuda Phi Çıkarımı](./md/01.Introduction/03/Local_Server_Inference.md)
    - [AI Toolkit kullanarak Uzaktaki Sunucuda Phi Çıkarımı](./md/01.Introduction/03/Remote_Interence.md)
    - [Rust ile Phi Çıkarımı](./md/01.Introduction/03/Rust_Inference.md)
    - [Yerelde Phi Görüntü Çıkarımı](./md/01.Introduction/03/Vision_Inference.md)
    - [Kaito AKS, Azure Containers ile Phi Çıkarımı (resmi destek)](./md/01.Introduction/03/Kaito_Inference.md)
-  [Phi Ailesinin Kuantizasyonu](./md/01.Introduction/04/QuantifyingPhi.md)
    - [llama.cpp kullanarak Phi-3.5 / 4'ü Kuantize Etme](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [onnxruntime için Generative AI eklentilerini kullanarak Phi-3.5 / 4'ü Kuantize Etme](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Intel OpenVINO kullanarak Phi-3.5 / 4'ü Kuantize Etme](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Apple MLX Çerçevesini kullanarak Phi-3.5 / 4'ü Kuantize Etme](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

-  Phi Değerlendirmesi
    - [Sorumlu Yapay Zeka](./md/01.Introduction/05/ResponsibleAI.md)
    - [Değerlendirme için Azure AI Foundry](./md/01.Introduction/05/AIFoundry.md)
    - [Değerlendirme için Promptflow Kullanımı](./md/01.Introduction/05/Promptflow.md)
 
- Azure AI Search ile RAG
    - [Phi-4-mini ve Phi-4-multimodal (RAG)'ı Azure AI Search ile nasıl kullanırsınız](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Phi uygulama geliştirme örnekleri
  - Metin & Sohbet Uygulamaları
    - Phi-4 Örnekleri 🆕
      - [📓] [Phi-4-mini ONNX Model ile Sohbet](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Phi-4 yerel ONNX Model ile Sohbet .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Phi-4 ONNX kullanarak Semantic Kernel ile Chat .NET Konsol Uygulaması](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Phi-3 / 3.5 Örnekleri
      - [Tarayıcıda Phi3, ONNX Runtime Web ve WebGPU kullanarak Yerel Sohbet Botu](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVINO Sohbeti](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [Çok Modelli - Etkileşimli Phi-3-mini ve OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - Phi-3 için bir sarmalayıcı oluşturma ve MLFlow ile kullanma](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [Model Optimizasyonu - Olive ile ONNX Runtime Web için Phi-3-min modelini nasıl optimize edersiniz](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [Phi-3 mini-4k-instruct-onnx ile WinUI3 Uygulaması](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      -[WinUI3 Çok Modelli Yapay Zekâ Destekli Notlar Uygulaması Örneği](https://github.com/microsoft/ai-powered-notes-winui3-sample)
      - [Özelleştirilmiş Phi-3 modellerini Prompt flow ile İnce Ayar (Fine-tune) yapma ve Entegre Etme](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
      - [Azure AI Foundry'de Prompt flow ile Özelleştirilmiş Phi-3 modellerini İnce Ayar (Fine-tune) yapma ve Entegre Etme](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
      - [Azure AI Foundry'de Microsoft'un Sorumlu Yapay Zekâ İlkelerine Odaklanarak İnce Ayarlanmış Phi-3 / Phi-3.5 Modelini Değerlendirme](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
      - [📓] [Phi-3.5-mini-instruct dil tahmin örneği (Çince/İngilizce)](./md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
      - [Phi-3.5-Instruct WebGPU RAG Sohbet Botu](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
      - [Phi-3.5-Instruct ONNX ile Prompt flow çözümü oluşturmak için Windows GPU kullanımı](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
      - [Android uygulaması oluşturmak için Microsoft Phi-3.5 tflite kullanma](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
      - [Microsoft.ML.OnnxRuntime kullanarak yerel ONNX Phi-3 modeli ile .NET Soru-Cevap Örneği](../../md/04.HOL/dotnet/src/LabsPhi301)
      - [Semantic Kernel ve Phi-3 ile Konsol sohbet .NET uygulaması](../../md/04.HOL/dotnet/src/LabsPhi302)

  - Azure AI Inference SDK Kod Tabanlı Örnekler 
    - Phi-4 Örnekleri 🆕
      - [📓] [Phi-4-multimodal kullanarak proje kodu oluşturma](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
    - Phi-3 / 3.5 Örnekleri
      - [Kendi Visual Studio Code GitHub Copilot Sohbetinizi Microsoft Phi-3 Ailesi ile Oluşturun](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
      - [GitHub Modelleri tarafından sağlanan Phi-3.5 ile kendi Visual Studio Code Chat Copilot Ajanınızı Oluşturun](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

  - Gelişmiş Akıl Yürütme Örnekleri
    - Phi-4 Örnekleri 🆕
      - [📓] [Phi-4-mini-reasoning veya Phi-4-reasoning Örnekleri](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
      - [📓] [Phi-4-mini-reasoning'i Microsoft Olive ile İnce Ayarlama](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Phi-4-mini-reasoning'i Apple MLX ile İnce Ayarlama](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [GitHub Modelleri ile Phi-4-mini-reasoning](./md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
      - [📓] [Azure AI Foundry Modelleri ile Phi-4-mini-reasoning](./md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
  - Demos
      - [Hugging Face Spaces'da barındırılan Phi-4-mini demoları](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
      - [Hugginge Face Spaces'da barındırılan Phi-4-multimodal demoları](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
  - Görsel Örnekler
    - Phi-4 Örnekleri 🆕
      - [📓] [Phi-4-multimodal'i görüntüleri okumak ve kod üretmek için kullanma](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
    - Phi-3 / 3.5 Örnekleri
      -  [📓][Phi-3-vision Görüntü metinden metne](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
      - [📓][Phi-3-vision CLIP Gömme](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [DEMO: Phi-3 Geri Dönüşüm](https://github.com/jennifermarsman/PhiRecycling/)
      - [Phi-3-vision - Görsel dil asistanı - Phi3-Vision ve OpenVINO ile](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
      - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
      - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
      - [📓][Phi-3.5 Vision çoklu kare veya çoklu görüntü örneği](./md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
      - [Microsoft.ML.OnnxRuntime .NET kullanarak Phi-3 Vision Yerel ONNX Modeli](../../md/04.HOL/dotnet/src/LabsPhi303)
      - [Microsoft.ML.OnnxRuntime .NET kullanarak Menü tabanlı Phi-3 Vision Yerel ONNX Modeli](../../md/04.HOL/dotnet/src/LabsPhi304)

  - Matematik Örnekleri
    -  Phi-4-Mini-Flash-Reasoning-Instruct Örnekleri 🆕 [Phi-4-Mini-Flash-Reasoning-Instruct ile Matematik Demo](./md/02.Application/09.Math/MathDemo.ipynb)

  - Ses Örnekleri
    - Phi-4 Örnekleri 🆕
      - [📓] [Phi-4-multimodal kullanarak ses dökümlerini çıkarma](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
      - [📓] [Phi-4-multimodal Ses Örneği](./md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
      - [📓] [Phi-4-multimodal Konuşma Çeviri Örneği](./md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
      - [.NET konsol uygulaması: Phi-4-multimodal Audio kullanarak bir ses dosyasını analiz etme ve döküm oluşturma](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

  - MOE Örnekleri
    - Phi-3 / 3.5 Örnekleri
      - [📓] [Phi-3.5 Mixture of Experts Models (MoEs) Sosyal Medya Örneği](./md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
      - [📓] [NVIDIA NIM Phi-3 MOE, Azure AI Search ve LlamaIndex ile Retrieval-Augmented Generation (RAG) Boru Hattı Oluşturma](./md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)
      - 
  - Fonksiyon Çağırma Örnekleri
    - Phi-4 Örnekleri 🆕
      -  [📓] [Phi-4-mini ile Fonksiyon Çağırmayı Kullanma](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
      -  [📓] [Phi-4-mini ile çoklu ajanlar oluşturmak için Fonksiyon Çağırmayı Kullanma](./md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
      -  [📓] [Ollama ile Fonksiyon Çağırmayı Kullanma](./md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
      -  [📓] [ONNX ile Fonksiyon Çağırmayı Kullanma](./md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)
  - Multimodal Karıştırma Örnekleri
    - Phi-4 Örnekleri 🆕
      -  [📓] [Bir teknoloji gazetecisi olarak Phi-4-multimodal kullanma](./md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
      - [.NET konsol uygulaması: Görüntüleri analiz etmek için Phi-4-multimodal kullanma](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Phi İnce Ayarı Örnekleri
  - [İnce Ayar Senaryoları](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [İnce Ayar vs RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [İnce Ayar: Phi-3'ü bir endüstri uzmanı yapın](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [VS Code için AI Toolkit ile Phi-3'ü İnce Ayarlama](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Azure Machine Learning Service ile Phi-3'ü İnce Ayarlama](./md/03.FineTuning/Introduce_AzureML.md)
  - [Lora ile Phi-3'ü İnce Ayarlama](./md/03.FineTuning/FineTuning_Lora.md)
  - [QLora ile Phi-3'ü İnce Ayarlama](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Azure AI Foundry ile Phi-3'ü İnce Ayarlama](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Azure ML CLI/SDK ile Phi-3'ü İnce Ayarlama](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Microsoft Olive ile İnce Ayar](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Microsoft Olive Uygulamalı Laboratuvar ile İnce Ayar](./md/03.FineTuning/olive-lab/readme.md)
  - [Weights and Bias ile Phi-3-vision'i İnce Ayarlama](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [Apple MLX Framework ile Phi-3'ü İnce Ayarlama](./md/03.FineTuning/FineTuning_MLX.md)
  - [Phi-3-vision'i İnce Ayarlama (resmi destek)](./md/03.FineTuning/FineTuning_Vision.md)
  - [Kaito AKS , Azure Containers(resmi Destek) ile Phi-3'ü İnce Ayarlama](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Phi-3 ve 3.5 Vision'i İnce Ayarlama](https://github.com/2U1/Phi3-Vision-Finetune)

- Uygulamalı Laboratuvar
  - [İleri düzey modelleri keşfetme: LLM'ler, SLM'ler, yerel geliştirme ve daha fazlası](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [NLP Potansiyelini Açığa Çıkarma: Microsoft Olive ile İnce Ayar](https://github.com/azure/Ignite_FineTuning_workshop)

- Akademik Araştırma Makaleleri ve Yayınlar
  - [Textbooks Are All You Need II: phi-1.5 teknik rapor](https://arxiv.org/abs/2309.05463)
  - [Phi-3 Teknik Raporu: Telefonunuzda Yerel Olarak Yüksek Kapasiteli Bir Dil Modeli](https://arxiv.org/abs/2404.14219)
  - [Phi-4 Teknik Raporu](https://arxiv.org/abs/2412.08905)
  - [Phi-4-Mini Teknik Raporu: Mixture-of-LoRAs ile Kompakt ama Güçlü Çok Modlu Dil Modelleri](https://arxiv.org/abs/2503.01743)
  - [Küçük Dil Modellerini Araç İçi Fonksiyon Çağırmaya Optimizasyon](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) PHI-3'ü Çoktan Seçmeli Soru Cevaplama için İnce Ayar: Yöntem, Sonuçlar ve Zorluklar](https://arxiv.org/abs/2501.01588)
  - [Phi-4-reasoning Teknik Raporu](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Phi-4-mini-reasoning Teknik Raporu](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Phi Modellerini Kullanma

### Azure AI Foundry'de Phi

Microsoft Phi'yi nasıl kullanacağınızı ve farklı donanım cihazlarınızda uçtan uca (E2E) çözümler oluşturmayı öğrenebilirsiniz. Phi'yi kendiniz deneyimlemek için modellerle oynayarak ve senaryolarınıza göre Phi'yi özelleştirerek başlayın; bunun için [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai) bağlantısını kullanabilirsiniz. Daha fazlasını [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md) ile Başlarken bölümünde öğrenebilirsiniz.

**Oyun Alanı**
Her modelin testi için ayrılmış bir oyun alanı vardır: [Azure AI Playground](https://aka.ms/try-phi3).

### GitHub Modellerinde Phi

Microsoft Phi'yi nasıl kullanacağınızı ve farklı donanım cihazlarınızda uçtan uca çözümler oluşturmayı öğrenebilirsiniz. Phi'yi kendiniz deneyimlemek için modelle oynayarak ve senaryolarınıza göre Phi'yi özelleştirerek başlayın; bunun için [GitHub Model Kataloğu](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) bağlantısını kullanabilirsiniz. Daha fazlasını [GitHub Model Kataloğu](/md/02.QuickStart/GitHubModel_QuickStart.md) ile Başlarken bölümünde öğrenebilirsiniz.

**Oyun Alanı**
Her modelin testi için ayrılmış bir [modeli test etmek için oyun alanı](/md/02.QuickStart/GitHubModel_QuickStart.md) vardır.

### Hugging Face'te Phi

Modeli ayrıca [Hugging Face](https://huggingface.co/microsoft) üzerinde de bulabilirsiniz.

**Oyun Alanı**
 [Hugging Chat oyun alanı](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

 ## 🎒 Diğer Kurslar

Ekibimiz başka kurslar da sunuyor! İnceleyin:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j Yeni Başlayanlar için](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js Yeni Başlayanlar için](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

---

### Azure / Edge / MCP / Ajanlar
[![AZD Yeni Başlayanlar için](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI Yeni Başlayanlar için](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP Yeni Başlayanlar için](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Ajanları Yeni Başlayanlar için](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Üretken AI Serisi
[![Yeni Başlayanlar için Üretken AI](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Üretken AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Üretken AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Üretken AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Temel Öğrenme
[![ML Yeni Başlayanlar için](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Veri Bilimi Yeni Başlayanlar için](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Yeni Başlayanlar için](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Siber Güvenlik Yeni Başlayanlar için](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Web Geliştirme Yeni Başlayanlar için](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT Yeni Başlayanlar için](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR Geliştirme Yeni Başlayanlar için](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot Serisi
[![AI Eşli Programlama için Copilot](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![C#/.NET için Copilot](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Macerası](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Sorumlu Yapay Zeka 

Microsoft, müşterilerimizin AI ürünlerimizi sorumlu bir şekilde kullanmalarına yardımcı olmaya, öğrendiklerimizi paylaşmaya ve Transparency Notes ve Impact Assessments gibi araçlar aracılığıyla güvene dayalı ortaklıklar kurmaya kararlıdır. Bu kaynakların birçoğunu [https://aka.ms/RAI](https://aka.ms/RAI) adresinde bulabilirsiniz.
Microsoft’un sorumlu yapay zekâ yaklaşımı, adalet, güvenilirlik ve güvenlik, gizlilik ve güvenlik, kapsayıcılık, şeffaflık ve hesap verebilirlik gibi AI ilkelere dayanmaktadır.

Bu örnekte kullanılanlar gibi büyük ölçekli doğal dil, görüntü ve konuşma modelleri adaletsiz, güvenilmez veya saldırgan davranışlar sergileyebilir ve bu da zararlara yol açabilir. Riskler ve sınırlamalar hakkında bilgi sahibi olmak için lütfen [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) belgesine bakın.

Bu riskleri azaltmak için önerilen yaklaşım, mimarinizde zararlı davranışı tespit edip önleyebilen bir güvenlik sistemi dahil etmektir. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview), uygulamalarda ve hizmetlerde kullanıcı tarafından üretilen ve AI tarafından üretilen zararlı içeriği tespit edebilen bağımsız bir koruma katmanı sağlar. Azure AI Content Safety, zararlı materyalleri tespit etmenizi sağlayan metin ve görüntü API'lerini içerir. Azure AI Foundry içinde, Content Safety hizmeti farklı modalitelerde zararlı içeriği tespit etmek için örnek kodu görüntülemenize, keşfetmenize ve denemenize olanak tanır. Aşağıdaki [hızlı başlangıç belgeleri](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) hizmete yapılan istekleri nasıl oluşturacağınızı adım adım gösterir.

Dikkate alınması gereken bir diğer husus ise genel uygulama performansıdır. Çok modlu ve çok modeller içeren uygulamalarda performans, sistemin sizin ve kullanıcılarınızın beklentileri doğrultusunda çalışmasını ifade eder; bu, zararlı çıktılar üretmemeyi de içerir. Genel uygulama performansınızı değerlendirmek için [Performance and Quality and Risk and Safety evaluators](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) kullanmanız önemlidir. Ayrıca [özel değerlendiriciler](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators) ile değerlendirme oluşturma ve değerlendirme yapma imkânınız da vardır.

Geliştirme ortamınızda AI uygulamanızı değerlendirmek için [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html) kullanabilirsiniz. Bir test veri kümesi veya hedef verildiğinde, üretken AI uygulamanızın çıktıları yerleşik değerlendiriciler veya tercih ettiğiniz özel değerlendiriciler ile nicel olarak ölçülür. Sisteminizin değerlendirmesine başlamak için azure ai evaluation sdk ile ilgili [hızlı başlangıç kılavuzunu](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) izleyebilirsiniz. Bir değerlendirme çalıştırması gerçekleştirdiğinizde, [Azure AI Foundry'de sonuçları görselleştirebilirsiniz](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results). 

## Ticari Markalar
Bu proje projeler, ürünler veya hizmetler için ticari markalar veya logolar içerebilir. Microsoft ticari markalarının veya logolarının yetkili kullanımı [Microsoft'un Ticari Marka ve Marka Yönergeleri](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) kapsamında olup bunlara uyulmalıdır.
Bu projenin değiştirilmiş sürümlerinde Microsoft ticari marka veya logolarının kullanımı karışıklığa yol açmamalı veya Microsoft'un sponsorluğunu ima etmemelidir. Üçüncü taraf ticari marka veya logolarının herhangi bir kullanımı ilgili üçüncü tarafın politikalarına tabidir.

## Yardım

AI uygulamaları geliştirirken takılırsanız veya herhangi bir sorunuz olursa, katılın:

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

Ürün geri bildirimi veya oluşturma sırasında ortaya çıkan hatalar için ziyaret edin:

[![Azure AI Foundry Geliştirici Forumu](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Sorumluluk Reddi:
Bu belge, yapay zeka çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Özen göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belge, kendi dilindeki versiyonu yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı nedeniyle ortaya çıkan herhangi bir yanlış anlama veya yanlış yorumdan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->