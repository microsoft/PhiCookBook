<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8f2577190cbe70305b9de13df37e1c9a",
  "translation_date": "2025-04-03T06:08:09+00:00",
  "source_file": "README.md",
  "language_code": "ur"
}
-->
# Phi کُک بُک: مائیکروسافٹ کے Phi ماڈلز کے ساتھ عملی مثالیں

Phi مائیکروسافٹ کی جانب سے تیار کردہ اوپن سورس AI ماڈلز کی ایک سیریز ہے۔

Phi فی الحال سب سے طاقتور اور لاگت کے لحاظ سے مؤثر چھوٹا زبان ماڈل (SLM) ہے، جو مختلف زبانوں، دلیل، متن/چیٹ جنریشن، کوڈنگ، تصاویر، آڈیو اور دیگر منظرناموں میں بہترین نتائج فراہم کرتا ہے۔

آپ Phi کو کلاؤڈ یا ایج ڈیوائسز پر تعینات کر سکتے ہیں، اور محدود کمپیوٹنگ طاقت کے ساتھ آسانی سے جنریٹو AI ایپلی کیشنز بنا سکتے ہیں۔

ان وسائل کو استعمال کرنے کے لیے درج ذیل مراحل پر عمل کریں:
1. **ریپوزٹری کو فورک کریں**: کلک کریں [![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **ریپوزٹری کو کلون کریں**:   `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**مائیکروسافٹ AI ڈسکورڈ کمیونٹی میں شامل ہوں اور ماہرین اور دیگر ڈویلپرز سے ملاقات کریں**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/cover.2595d43b382944c601aebf88583314636768eece3d94e8e4448e03a4e5bedef4.ur.png)

## 🌐 متعدد زبانوں کی حمایت
[فرانسیسی](../fr/README.md) | [ہسپانوی](../es/README.md) | [جرمن](../de/README.md) | [روسی](../ru/README.md) | [عربی](../ar/README.md) | [فارسی](../fa/README.md) | [اردو](./README.md) | [چینی (سادہ)](../zh/README.md) | [چینی (روایتی، مکاؤ)](../mo/README.md) | [چینی (روایتی، ہانگ کانگ)](../hk/README.md) | [چینی (روایتی، تائیوان)](../tw/README.md) | [جاپانی](../ja/README.md) | [کوریائی](../ko/README.md) | [ہندی](../hi/README.md) | [بنگالی](../bn/README.md) | [مراٹھی](../mr/README.md) | [نیپالی](../ne/README.md) | [پنجابی (گرمکھی)](../pa/README.md) | [پرتگالی (پرتگال)](../pt/README.md) | [پرتگالی (برازیل)](../br/README.md) | [اطالوی](../it/README.md) | [پولش](../pl/README.md) | [ترکی](../tr/README.md) | [یونانی](../el/README.md) | [تھائی](../th/README.md) | [سویڈش](../sv/README.md) | [ڈینش](../da/README.md) | [نارویجین](../no/README.md) | [فنش](../fi/README.md) | [ڈچ](../nl/README.md) | [عبرانی](../he/README.md) | [ویتنامی](../vi/README.md) | [انڈونیشیائی](../id/README.md) | [مالائی](../ms/README.md) | [ٹیگالوگ (فلپائنی)](../tl/README.md) | [سواحلی](../sw/README.md) | [ہنگریائی](../hu/README.md) | [چیک](../cs/README.md) | [سلوواک](../sk/README.md) | [رومانیائی](../ro/README.md) | [بلغاریائی](../bg/README.md) | [سربیائی (سیریلیک)](../sr/README.md) | [کروشین](../hr/README.md) | [سلووینیائی](../sl/README.md)
## مواد کا جدول

- تعارف
  - [Phi فیملی میں خوش آمدید](./md/01.Introduction/01/01.PhiFamily.md)
  - [اپنے ماحول کو ترتیب دینا](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [اہم ٹیکنالوجیز کو سمجھنا](./md/01.Introduction/01/01.Understandingtech.md)
  - [Phi ماڈلز کے لیے AI سیفٹی](./md/01.Introduction/01/01.AISafety.md)
  - [Phi ہارڈویئر سپورٹ](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Phi ماڈلز اور پلیٹ فارمز پر دستیابی](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Guidance-ai اور Phi کا استعمال](./md/01.Introduction/01/01.Guidance.md)
  - [GitHub مارکیٹ پلیس ماڈلز](https://github.com/marketplace/models)
  - [Azure AI ماڈل کیٹلاگ](https://ai.azure.com)

- مختلف ماحول میں Phi کا انفرنس
    - [Hugging face](./md/01.Introduction/02/01.HF.md)
    - [GitHub ماڈلز](./md/01.Introduction/02/02.GitHubModel.md)
    - [Azure AI Foundry ماڈل کیٹلاگ](./md/01.Introduction/02/03.AzureAIFoundry.md)
    - [Ollama](./md/01.Introduction/02/04.Ollama.md)
    - [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    - [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)

- Phi فیملی کا انفرنس
    - [iOS میں Phi کا انفرنس](./md/01.Introduction/03/iOS_Inference.md)
    - [Android میں Phi کا انفرنس](./md/01.Introduction/03/Android_Inference.md)
    - [Jetson میں Phi کا انفرنس](./md/01.Introduction/03/Jetson_Inference.md)
    - [AI PC میں Phi کا انفرنس](./md/01.Introduction/03/AIPC_Inference.md)
    - [Apple MLX Framework کے ساتھ Phi کا انفرنس](./md/01.Introduction/03/MLX_Inference.md)
    - [لوکل سرور میں Phi کا انفرنس](./md/01.Introduction/03/Local_Server_Inference.md)
    - [AI Toolkit کے ذریعے ریموٹ سرور میں Phi کا انفرنس](./md/01.Introduction/03/Remote_Interence.md)
    - [Rust کے ساتھ Phi کا انفرنس](./md/01.Introduction/03/Rust_Inference.md)
    - [لوکل میں Phi--Vision کا انفرنس](./md/01.Introduction/03/Vision_Inference.md)
    - [Kaito AKS، Azure Containers (سرکاری سپورٹ) کے ساتھ Phi کا انفرنس](./md/01.Introduction/03/Kaito_Inference.md)

- [Phi فیملی کو مقدار میں لانا](./md/01.Introduction/04/QuantifyingPhi.md)
    - [llama.cpp کا استعمال کرتے ہوئے Phi-3.5 / 4 کو مقدار میں لانا](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [onnxruntime کے لیے Generative AI ایکسٹینشنز کا استعمال کرتے ہوئے Phi-3.5 / 4 کو مقدار میں لانا](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Intel OpenVINO کا استعمال کرتے ہوئے Phi-3.5 / 4 کو مقدار میں لانا](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Apple MLX Framework کا استعمال کرتے ہوئے Phi-3.5 / 4 کو مقدار میں لانا](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

- Phi کا جائزہ
- [ذمہ دار AI](./md/01.Introduction/05/ResponsibleAI.md)  
    - [ایزور AI فاؤنڈری برائے تشخیص](./md/01.Introduction/05/AIFoundry.md)  
    - [پرومپٹ فلو کا استعمال برائے تشخیص](./md/01.Introduction/05/Promptflow.md)  

- Azure AI سرچ کے ساتھ RAG  
    - [Azure AI سرچ کے ساتھ Phi-4-mini اور Phi-4-multimodal (RAG) کا استعمال کیسے کریں](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)  

- Phi ایپلیکیشن ڈیولپمنٹ کے نمونے  
  - ٹیکسٹ اور چیٹ ایپلیکیشنز  
    - Phi-4 نمونے 🆕  
      - [📓] [Phi-4-mini ONNX ماڈل کے ساتھ چیٹ کریں](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)  
      - [Phi-4 لوکل ONNX ماڈل .NET کے ساتھ چیٹ کریں](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)  
      - [سیمینٹک کرنل کا استعمال کرتے ہوئے Phi-4 ONNX کے ساتھ چیٹ .NET کنسول ایپ](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)  
    - Phi-3 / 3.5 نمونے  
      - [Phi3، ONNX رن ٹائم ویب اور WebGPU کا استعمال کرتے ہوئے لوکل چیٹ بوٹ براؤزر میں](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)  
      - [اوپن وینو چیٹ](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)  
      - [ملٹی ماڈل - Phi-3-mini اور OpenAI Whisper کے ساتھ انٹرایکٹو](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)  
      - [MLFlow - ایک ریپر بنانا اور Phi-3 کو MLFlow کے ساتھ استعمال کرنا](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)  
      - [ماڈل آپٹیمائزیشن - ONNX رن ٹائم ویب کے لیے Phi-3-min ماڈل کو Olive کے ساتھ آپٹیمائز کرنے کا طریقہ](https://github.com/microsoft/Olive/tree/main/examples/phi3)  
      - [WinUI3 ایپ کے ساتھ Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)  
      - [WinUI3 ملٹی ماڈل AI پاورڈ نوٹس ایپ نمونہ](https://github.com/microsoft/ai-powered-notes-winui3-sample)  
      - [پرومپٹ فلو کے ساتھ کسٹم Phi-3 ماڈلز کو فائن ٹون اور انٹیگریٹ کریں](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)  
      - [Azure AI فاؤنڈری میں پرومپٹ فلو کے ساتھ کسٹم Phi-3 ماڈلز کو فائن ٹون اور انٹیگریٹ کریں](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)  
      - [Azure AI فاؤنڈری میں مائیکروسافٹ کے ذمہ دار AI اصولوں پر توجہ دیتے ہوئے فائن ٹونڈ Phi-3 / Phi-3.5 ماڈل کی تشخیص کریں](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)  
      - [📓] [Phi-3.5-mini-instruct زبان کی پیشن گوئی کا نمونہ (چینی/انگریزی)](../../md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)  
      - [Phi-3.5-Instruct WebGPU RAG چیٹ بوٹ](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)  
      - [Windows GPU کا استعمال کرتے ہوئے Phi-3.5-Instruct ONNX کے ساتھ پرومپٹ فلو حل بنائیں](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)  
      - [Microsoft Phi-3.5 tflite کا استعمال کرتے ہوئے اینڈرائیڈ ایپ بنائیں](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)  
      - [Microsoft.ML.OnnxRuntime کا استعمال کرتے ہوئے لوکل ONNX Phi-3 ماڈل کے ساتھ Q&A .NET مثال](../../md/04.HOL/dotnet/src/LabsPhi301)  
      - [سیمینٹک کرنل اور Phi-3 کے ساتھ کنسول چیٹ .NET ایپ](../../md/04.HOL/dotnet/src/LabsPhi302)  

  - Azure AI انفرنس SDK کوڈ پر مبنی نمونے  
    - Phi-4 نمونے 🆕  
      - [📓] [Phi-4-multimodal کا استعمال کرتے ہوئے پروجیکٹ کوڈ تیار کریں](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)  
    - Phi-3 / 3.5 نمونے  
      - [Microsoft Phi-3 فیملی کے ساتھ اپنا Visual Studio Code GitHub Copilot چیٹ بنائیں](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)  
      - [GitHub ماڈلز کے ذریعے Phi-3.5 کے ساتھ اپنا Visual Studio Code چیٹ کوپائلٹ ایجنٹ بنائیں](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)  

  - ایڈوانسڈ ریزننگ کے نمونے  
    - Phi-4 نمونے 🆕  
      - [📓] [Phi-4-mini ریزننگ کے نمونے](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)  

  - ڈیموز  
      - [Phi-4-mini ڈیموز جو Hugging Face Spaces پر ہوسٹ کیے گئے ہیں](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)  
      - [Phi-4-multimodal ڈیموز جو Hugging Face Spaces پر ہوسٹ کیے گئے ہیں](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)  

  - وژن کے نمونے  
    - Phi-4 نمونے 🆕  
      - [📓] [Phi-4-multimodal کا استعمال کرتے ہوئے تصاویر پڑھیں اور کوڈ تیار کریں](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md)  
    - Phi-3 / 3.5 نمونے  
-  [📓][Phi-3-vision-Image text to text](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
      - [📓][Phi-3-vision CLIP Embedding](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [ڈیمو: Phi-3 ری سائیکلنگ](https://github.com/jennifermarsman/PhiRecycling/)
      - [Phi-3-vision - بصری زبان کا معاون - Phi3-Vision اور OpenVINO کے ساتھ](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
      - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
      - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
      - [📓][Phi-3.5 Vision کثیر فریم یا کثیر تصویر نمونہ](../../md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
      - [Phi-3 Vision لوکل ONNX ماڈل Microsoft.ML.OnnxRuntime .NET استعمال کرتے ہوئے](../../md/04.HOL/dotnet/src/LabsPhi303)
      - [مینو پر مبنی Phi-3 Vision لوکل ONNX ماڈل Microsoft.ML.OnnxRuntime .NET استعمال کرتے ہوئے](../../md/04.HOL/dotnet/src/LabsPhi304)

  - آڈیو نمونے
    - Phi-4 نمونے 🆕
      - [📓] [آڈیو ٹرانسکرپٹس نکالنا Phi-4-multimodal استعمال کرتے ہوئے](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
      - [📓] [Phi-4-multimodal آڈیو نمونہ](../../md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
      - [📓] [Phi-4-multimodal تقریر ترجمہ نمونہ](../../md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
      - [.NET کنسول ایپلیکیشن Phi-4-multimodal آڈیو استعمال کرتے ہوئے آڈیو فائل کا تجزیہ کرنے اور ٹرانسکرپٹ بنانے کے لیے](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

  - MOE نمونے
    - Phi-3 / 3.5 نمونے
      - [📓] [Phi-3.5 Mixture of Experts Models (MoEs) سوشل میڈیا نمونہ](../../md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
      - [📓] [Retrieval-Augmented Generation (RAG) پائپ لائن بنانا NVIDIA NIM Phi-3 MOE، Azure AI Search، اور LlamaIndex کے ساتھ](../../md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)
  - فنکشن کالنگ نمونے
    - Phi-4 نمونے 🆕
      -  [📓] [فنکشن کالنگ استعمال کرتے ہوئے Phi-4-mini کے ساتھ](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
      -  [📓] [فنکشن کالنگ استعمال کرتے ہوئے کثیر ایجنٹس بنانا Phi-4-mini کے ساتھ](../../md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
      -  [📓] [فنکشن کالنگ Ollama کے ساتھ استعمال کرتے ہوئے](../../md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
  - کثیر ماڈل مکسنگ نمونے
    - Phi-4 نمونے 🆕
      -  [📓] [Phi-4-multimodal استعمال کرتے ہوئے ایک ٹیکنالوجی صحافی کے طور پر](../../md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
      - [.NET کنسول ایپلیکیشن Phi-4-multimodal استعمال کرتے ہوئے تصاویر کا تجزیہ کرنے کے لیے](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Phi نمونوں کی فائن ٹیوننگ
  - [فائن ٹیوننگ کے منظرنامے](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [فائن ٹیوننگ بمقابلہ RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [Phi-3 کو صنعت کا ماہر بنانے کی فائن ٹیوننگ](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [Phi-3 کو AI Toolkit for VS Code کے ساتھ فائن ٹیوننگ](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Phi-3 کو Azure Machine Learning Service کے ساتھ فائن ٹیوننگ](./md/03.FineTuning/Introduce_AzureML.md)
  - [Phi-3 کو Lora کے ساتھ فائن ٹیوننگ](./md/03.FineTuning/FineTuning_Lora.md)
  - [Phi-3 کو QLora کے ساتھ فائن ٹیوننگ](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Phi-3 کو Azure AI Foundry کے ساتھ فائن ٹیوننگ](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Phi-3 کو Azure ML CLI/SDK کے ساتھ فائن ٹیوننگ](./md/03.FineTuning/FineTuning_MLSDK.md)
- [مائیکروسافٹ اولیو کے ساتھ فائن ٹیوننگ](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)  
  - [مائیکروسافٹ اولیو کے ساتھ فائن ٹیوننگ ہینڈز آن لیب](./md/03.FineTuning/olive-lab/readme.md)  
  - [وزن اور بائس کے ساتھ Phi-3-vision کی فائن ٹیوننگ](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)  
  - [ایپل MLX فریم ورک کے ساتھ Phi-3 کی فائن ٹیوننگ](./md/03.FineTuning/FineTuning_MLX.md)  
  - [Phi-3-vision کی فائن ٹیوننگ (آفیشل سپورٹ)](./md/03.FineTuning/FineTuning_Vision.md)  
  - [Kaito AKS، Azure Containers کے ساتھ Phi-3 کی فائن ٹیوننگ (آفیشل سپورٹ)](./md/03.FineTuning/FineTuning_Kaito.md)  
  - [Phi-3 اور 3.5 Vision کی فائن ٹیوننگ](https://github.com/2U1/Phi3-Vision-Finetune)  

- ہینڈز آن لیب  
  - [جدید ماڈلز کی کھوج: LLMs، SLMs، مقامی ترقی اور مزید](https://github.com/microsoft/aitour-exploring-cutting-edge-models)  
  - [NLP کی صلاحیتوں کو کھولنا: مائیکروسافٹ اولیو کے ساتھ فائن ٹیوننگ](https://github.com/azure/Ignite_FineTuning_workshop)  

- تعلیمی تحقیقی مقالے اور اشاعتیں  
  - [Textbooks Are All You Need II: phi-1.5 تکنیکی رپورٹ](https://arxiv.org/abs/2309.05463)  
  - [Phi-3 تکنیکی رپورٹ: ایک انتہائی قابل زبان ماڈل جو آپ کے فون پر مقامی طور پر چل سکتا ہے](https://arxiv.org/abs/2404.14219)  
  - [Phi-4 تکنیکی رپورٹ](https://arxiv.org/abs/2412.08905)  
  - [Phi-4-Mini تکنیکی رپورٹ: Mixture-of-LoRAs کے ذریعے کمپیکٹ لیکن طاقتور ملٹی موڈل لینگویج ماڈلز](https://arxiv.org/abs/2503.01743)  
  - [گاڑی کے اندر فنکشن کالنگ کے لیے چھوٹے زبان ماڈلز کی اصلاح](https://arxiv.org/abs/2501.02342)  
  - [(WhyPHI) متعدد انتخابی سوالات کے جوابات کے لیے PHI-3 کی فائن ٹیوننگ: طریقہ کار، نتائج، اور چیلنجز](https://arxiv.org/abs/2501.01588)  

## Phi ماڈلز کا استعمال  

### Azure AI Foundry پر Phi  

آپ مائیکروسافٹ Phi کو استعمال کرنے اور مختلف ہارڈویئر ڈیوائسز پر E2E سلوشنز بنانے کے طریقے سیکھ سکتے ہیں۔ Phi کو خود تجربہ کرنے کے لیے، ماڈلز کے ساتھ کھیلنا شروع کریں اور اپنے منظرناموں کے لیے Phi کو حسب ضرورت بنائیں۔ مزید معلومات کے لیے [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai) دیکھیں۔ شروع کرنے کے لیے [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md) پر گائیڈ ملاحظہ کریں۔  

**پلے گراؤنڈ**  
ہر ماڈل کا ایک مخصوص پلے گراؤنڈ ہے جہاں آپ ماڈل کو آزما سکتے ہیں [Azure AI Playground](https://aka.ms/try-phi3)۔  

### GitHub ماڈلز پر Phi  

آپ مائیکروسافٹ Phi کو استعمال کرنے اور مختلف ہارڈویئر ڈیوائسز پر E2E سلوشنز بنانے کے طریقے سیکھ سکتے ہیں۔ Phi کو خود تجربہ کرنے کے لیے، ماڈل کے ساتھ کھیلنا شروع کریں اور اپنے منظرناموں کے لیے Phi کو حسب ضرورت بنائیں۔ مزید معلومات کے لیے [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) دیکھیں۔ شروع کرنے کے لیے [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md) پر گائیڈ ملاحظہ کریں۔  

**پلے گراؤنڈ**  
ہر ماڈل کا ایک مخصوص [پلے گراؤنڈ ہے جہاں آپ ماڈل کو آزما سکتے ہیں](/md/02.QuickStart/GitHubModel_QuickStart.md)۔  

### Hugging Face پر Phi  

آپ ماڈل کو [Hugging Face](https://huggingface.co/microsoft) پر بھی تلاش کر سکتے ہیں۔  

**پلے گراؤنڈ**  
[Hugging Chat پلے گراؤنڈ](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)  

## ذمہ دار AI  

مائیکروسافٹ اپنے صارفین کو ہمارے AI پروڈکٹس کو ذمہ داری سے استعمال کرنے میں مدد دینے، اپنی سیکھنے کی معلومات شیئر کرنے، اور شفافیت نوٹس اور اثرات کی تشخیص جیسے ٹولز کے ذریعے اعتماد پر مبنی شراکت داری بنانے کے لیے پرعزم ہے۔ ان وسائل میں سے بہت سے کو [https://aka.ms/RAI](https://aka.ms/RAI) پر پایا جا سکتا ہے۔  
مائیکروسافٹ کا ذمہ دار AI کے حوالے سے نقطہ نظر ہمارے AI اصولوں پر مبنی ہے، جن میں انصاف، قابل اعتبار اور حفاظت، پرائیویسی اور سیکیورٹی، شمولیت، شفافیت، اور جوابدہی شامل ہیں۔  

بڑے پیمانے پر قدرتی زبان، تصاویر، اور آواز کے ماڈلز - جیسے کہ اس نمونے میں استعمال کیے گئے - ممکنہ طور پر غیر منصفانہ، ناقابل اعتماد، یا جارحانہ رویہ اختیار کر سکتے ہیں، جو نقصان کا باعث بن سکتے ہیں۔ خطرات اور حدود سے آگاہ ہونے کے لیے [Azure OpenAI سروس شفافیت نوٹ](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) کو ضرور ملاحظہ کریں۔  

ان خطرات کو کم کرنے کے لیے تجویز کردہ نقطہ نظر یہ ہے کہ آپ اپنی آرکیٹیکچر میں ایک حفاظتی نظام شامل کریں جو نقصان دہ رویے کا پتہ لگانے اور روکنے کی صلاحیت رکھتا ہو۔ [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) ایک آزاد حفاظتی پرت فراہم کرتا ہے، جو ایپلی کیشنز اور سروسز میں نقصان دہ مواد کو پتہ لگانے کے قابل ہے۔ Azure AI Content Safety میں متن اور تصویر کے APIs شامل ہیں جو نقصان دہ مواد کا پتہ لگانے کی اجازت دیتے ہیں۔ Azure AI Foundry کے اندر، Content Safety سروس آپ کو مختلف طریقوں میں نقصان دہ مواد کا پتہ لگانے کے لیے نمونے کے کوڈ کو دیکھنے، دریافت کرنے، اور آزمانے کی اجازت دیتی ہے۔ درج ذیل [کوئیک اسٹارٹ ڈاکیومنٹیشن](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) سروس کے لیے درخواستیں کرنے کے طریقے پر گائیڈ کرتی ہے۔  

ایک اور پہلو جس پر غور کرنا ضروری ہے وہ مجموعی ایپلیکیشن کی کارکردگی ہے۔ ملٹی موڈل اور ملٹی ماڈلز ایپلیکیشنز کے ساتھ، کارکردگی سے مراد یہ ہے کہ نظام آپ اور آپ کے صارفین کی توقعات کے مطابق کام کرتا ہے، بشمول نقصان دہ آؤٹ پٹ پیدا نہ کرنا۔ اپنی مجموعی ایپلیکیشن کی کارکردگی کا جائزہ لینا اہم ہے، جس میں [پرفارمنس اور کوالٹی اور رسک اینڈ سیفٹی ایویلیویٹرز](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) شامل ہیں۔ آپ کے پاس [حسب ضرورت ایویلیویٹرز](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators) بنانے اور ان کا جائزہ لینے کی صلاحیت بھی موجود ہے۔  
آپ اپنے ترقیاتی ماحول میں [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html) استعمال کرتے ہوئے اپنی AI ایپلیکیشن کا جائزہ لے سکتے ہیں۔ دیے گئے ٹیسٹ ڈیٹاسیٹ یا ہدف کی بنیاد پر، آپ کی جنریٹو AI ایپلیکیشن کی تخلیقات کو بلٹ-ان ایویلیوئیٹرز یا آپ کی پسند کے کسٹم ایویلیوئیٹرز کے ذریعے مقداری طور پر ماپا جاتا ہے۔ Azure AI Evaluation SDK کے ساتھ اپنے سسٹم کا جائزہ لینے کے لیے شروع کرنے کے لیے، آپ [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) کی پیروی کر سکتے ہیں۔ جب آپ ایک ایویلیوایشن رن مکمل کرتے ہیں، تو آپ [Azure AI Foundry میں نتائج کو دیکھ سکتے ہیں](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results)۔

## ٹریڈمارکس

یہ پروجیکٹ ان پروجیکٹس، مصنوعات، یا خدمات کے لیے ٹریڈمارکس یا لوگوز پر مشتمل ہو سکتا ہے۔ مائیکروسافٹ کے ٹریڈمارکس یا لوگوز کے مجاز استعمال کو [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) کے مطابق ہونا چاہیے اور ان کی پیروی کرنی چاہیے۔
اس پروجیکٹ کے ترمیم شدہ ورژنز میں مائیکروسافٹ کے ٹریڈمارکس یا لوگوز کا استعمال کسی قسم کی الجھن پیدا نہیں کرنا چاہیے یا مائیکروسافٹ کی اسپانسرشپ کا اشارہ نہیں دینا چاہیے۔ کسی بھی تیسرے فریق کے ٹریڈمارکس یا لوگوز کا استعمال ان تیسرے فریق کی پالیسیوں کے تابع ہے۔

**ڈسکلوزر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کے لئے کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا غیر درستیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی اصل زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لئے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے ذمہ دار نہیں ہیں۔