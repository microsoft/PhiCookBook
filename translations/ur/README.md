<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "10139744c0f1757a5ade1c66749e803f",
  "translation_date": "2025-05-04T13:33:20+00:00",
  "source_file": "README.md",
  "language_code": "ur"
}
-->
# Phi Cookbook: Microsoft کے Phi ماڈلز کے ساتھ عملی مثالیں

[![GitHub Codespaces میں نمونے کھولیں اور استعمال کریں](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)  
[![Dev Containers میں کھولیں](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub کے شراکت دار](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)  
[![GitHub مسائل](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)  
[![GitHub پل-ریکویسٹ](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)  
[![PRs خوش آمدید](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub واچرز](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)  
[![GitHub فورکس](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)  
[![GitHub اسٹارز](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Azure AI Community Discord](https://dcbadge.vercel.app/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

Phi مائیکروسافٹ کی طرف سے تیار کردہ ایک اوپن سورس AI ماڈلز کی سیریز ہے۔

Phi فی الحال سب سے طاقتور اور کم قیمت چھوٹا زبان ماڈل (SLM) ہے، جس کے پاس متعدد زبانوں، منطق، متن/چیٹ جنریشن، کوڈنگ، تصاویر، آڈیو اور دیگر حالات میں بہت اچھے بینچ مارکس ہیں۔

آپ Phi کو کلاؤڈ یا ایج ڈیوائسز پر تعینات کر سکتے ہیں، اور محدود کمپیوٹنگ پاور کے ساتھ آسانی سے جنریٹو AI ایپلیکیشنز بنا سکتے ہیں۔

ان وسائل کو استعمال شروع کرنے کے لیے یہ مراحل فالو کریں:  
1. **ریپوزیٹری کو فورک کریں**: کلک کریں [![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)  
2. **ریپوزیٹری کو کلون کریں**: `git clone https://github.com/microsoft/PhiCookBook.git`  
3. [**Microsoft AI Discord کمیونٹی میں شامل ہوں اور ماہرین اور دیگر ڈویلپرز سے ملیں**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/cover.2595d43b382944c601aebf88583314636768eece3d94e8e4448e03a4e5bedef4.ur.png)

## 🌐 کثیراللسانی معاونت
[فرانسیسی](../fr/README.md) | [ہسپانوی](../es/README.md) | [جرمن](../de/README.md) | [روسی](../ru/README.md) | [عربی](../ar/README.md) | [فارسی (دری)](../fa/README.md) | [اردو](./README.md) | [چینی (سادہ)](../zh/README.md) | [چینی (روایتی، مکاو)](../mo/README.md) | [چینی (روایتی، ہانگ کانگ)](../hk/README.md) | [چینی (روایتی، تائیوان)](../tw/README.md) | [جاپانی](../ja/README.md) | [کوریائی](../ko/README.md) | [ہندی](../hi/README.md) [بنگالی](../bn/README.md) | [مراٹھی](../mr/README.md) | [نیپالی](../ne/README.md) | [پنجابی (گرمکھی)](../pa/README.md) | [پرتگالی (پرتگال)](../pt/README.md) | [پرتگالی (برازیل)](../br/README.md) | [اطالوی](../it/README.md) | [پولش](../pl/README.md) | [ترکی](../tr/README.md) | [یونانی](../el/README.md) | [تھائی](../th/README.md) | [سویڈش](../sv/README.md) | [ڈینش](../da/README.md) | [ناروے](../no/README.md) | [فنلندی](../fi/README.md) | [ڈچ](../nl/README.md) | [عبرانی](../he/README.md) | [ویتنامی](../vi/README.md) | [انڈونیشیائی](../id/README.md) | [ملائی](../ms/README.md) | [ٹگالوگ (فلپائنی)](../tl/README.md) | [سواحلی](../sw/README.md) | [ہنگریائی](../hu/README.md) | [چیک](../cs/README.md) | [سلوواک](../sk/README.md) | [رومانیائی](../ro/README.md) | [بلغاریائی](../bg/README.md) | [سربی (سیریلک)](../sr/README.md) | [کروشین](../hr/README.md) | [سلووینیائی](../sl/README.md)
## فہرست مضامین

- تعارف  
  - [Phi فیملی میں خوش آمدید](./md/01.Introduction/01/01.PhiFamily.md)  
  - [اپنے ماحول کی ترتیب](./md/01.Introduction/01/01.EnvironmentSetup.md)  
  - [اہم ٹیکنالوجیز کی سمجھ](./md/01.Introduction/01/01.Understandingtech.md)  
  - [Phi ماڈلز کے لیے AI کی حفاظت](./md/01.Introduction/01/01.AISafety.md)  
  - [Phi ہارڈویئر کی حمایت](./md/01.Introduction/01/01.Hardwaresupport.md)  
  - [Phi ماڈلز اور پلیٹ فارمز پر دستیابی](./md/01.Introduction/01/01.Edgeandcloud.md)  
  - [Guidance-ai اور Phi کا استعمال](./md/01.Introduction/01/01.Guidance.md)  
  - [GitHub مارکیٹ پلیس ماڈلز](https://github.com/marketplace/models)  
  - [Azure AI ماڈل کیٹلاگ](https://ai.azure.com)

- مختلف ماحول میں Inference Phi  
    -  [Hugging face](./md/01.Introduction/02/01.HF.md)  
    -  [GitHub ماڈلز](./md/01.Introduction/02/02.GitHubModel.md)  
    -  [Azure AI Foundry ماڈل کیٹلاگ](./md/01.Introduction/02/03.AzureAIFoundry.md)  
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)  
    -  [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)  
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)

- Inference Phi فیملی  
    - [iOS میں Inference Phi](./md/01.Introduction/03/iOS_Inference.md)  
    - [Android میں Inference Phi](./md/01.Introduction/03/Android_Inference.md)  
    - [Jetson میں Inference Phi](./md/01.Introduction/03/Jetson_Inference.md)  
    - [AI PC میں Inference Phi](./md/01.Introduction/03/AIPC_Inference.md)  
    - [Apple MLX فریم ورک کے ساتھ Inference Phi](./md/01.Introduction/03/MLX_Inference.md)  
    - [لوکل سرور میں Inference Phi](./md/01.Introduction/03/Local_Server_Inference.md)  
    - [ریموٹ سرور میں AI Toolkit کے ذریعے Inference Phi](./md/01.Introduction/03/Remote_Interence.md)  
    - [Rust کے ساتھ Inference Phi](./md/01.Introduction/03/Rust_Inference.md)  
    - [لوکل میں Inference Phi--Vision](./md/01.Introduction/03/Vision_Inference.md)  
    - [Kaito AKS، Azure Containers (سرکاری حمایت) کے ساتھ Inference Phi](./md/01.Introduction/03/Kaito_Inference.md)  
-  [Phi فیملی کی مقدار ناپنا](./md/01.Introduction/04/QuantifyingPhi.md)  
    - [llama.cpp کے ذریعے Phi-3.5 / 4 کی مقدار ناپنا](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)  
    - [onnxruntime کے لیے Generative AI ایکسٹینشنز کے ذریعے Phi-3.5 / 4 کی مقدار ناپنا](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)  
    - [Intel OpenVINO کے ذریعے Phi-3.5 / 4 کی مقدار ناپنا](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)  
    - [Apple MLX فریم ورک کے ذریعے Phi-3.5 / 4 کی مقدار ناپنا](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

-  Phi کا جائزہ
- [Response AI](./md/01.Introduction/05/ResponsibleAI.md)
    - [Azure AI Foundry for Evaluation](./md/01.Introduction/05/AIFoundry.md)
    - [Using Promptflow for Evaluation](./md/01.Introduction/05/Promptflow.md)
 
- RAG with Azure AI Search
    - [Phi-4-mini اور Phi-4-multimodal(RAG) کو Azure AI Search کے ساتھ کیسے استعمال کریں](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Phi application development samples
  - Text & Chat Applications
    - Phi-4 Samples 🆕
      - [📓] [Phi-4-mini ONNX ماڈل کے ساتھ چیٹ کریں](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Phi-4 لوکل ONNX ماڈل .NET کے ساتھ چیٹ کریں](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Semantic Kernel استعمال کرتے ہوئے Phi-4 ONNX کے ساتھ .NET کنسول ایپ میں چیٹ کریں](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Phi-3 / 3.5 Samples
      - [Phi3، ONNX Runtime Web اور WebGPU استعمال کرتے ہوئے براؤزر میں لوکل چیٹ بوٹ](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVino چیٹ](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [متعدد ماڈل - انٹرایکٹو Phi-3-mini اور OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - ایک ریپر بنانا اور Phi-3 کو MLFlow کے ساتھ استعمال کرنا](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [ماڈل کی اصلاح - ONNX Runtime Web کے لیے Phi-3-min ماڈل کو Olive کے ساتھ کیسے بہتر بنایا جائے](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [Phi-3 mini-4k-instruct-onnx کے ساتھ WinUI3 ایپ](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      -[WinUI3 ملٹی ماڈل AI پاورڈ نوٹس ایپ کا نمونہ](https://github.com/microsoft/ai-powered-notes-winui3-sample)
      - [اپنے کسٹم Phi-3 ماڈلز کو Prompt flow کے ساتھ Fine-tune اور انضمام کریں](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
      - [Azure AI Foundry میں Prompt flow کے ساتھ اپنے کسٹم Phi-3 ماڈلز کو Fine-tune اور انضمام کریں](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
      - [Microsoft کے Responsible AI اصولوں پر توجہ دیتے ہوئے Azure AI Foundry میں Fine-tuned Phi-3 / Phi-3.5 ماڈل کا جائزہ لیں](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
      - [📓] [Phi-3.5-mini-instruct زبان کی پیشن گوئی کا نمونہ (چینی/انگریزی)](../../md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
      - [Phi-3.5-Instruct WebGPU RAG چیٹ بوٹ](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
      - [Phi-3.5-Instruct ONNX کے ساتھ Prompt flow حل بنانے کے لیے Windows GPU کا استعمال](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
      - [Android ایپ بنانے کے لیے Microsoft Phi-3.5 tflite کا استعمال](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
      - [Microsoft.ML.OnnxRuntime استعمال کرتے ہوئے لوکل ONNX Phi-3 ماڈل کے ساتھ Q&A .NET مثال](../../md/04.HOL/dotnet/src/LabsPhi301)
      - [Semantic Kernel اور Phi-3 کے ساتھ کنسول چیٹ .NET ایپ](../../md/04.HOL/dotnet/src/LabsPhi302)

  - Azure AI Inference SDK Code Based Samples 
    - Phi-4 Samples 🆕
      - [📓] [Phi-4-multimodal استعمال کرتے ہوئے پروجیکٹ کوڈ بنائیں](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
    - Phi-3 / 3.5 Samples
      - [Microsoft Phi-3 فیملی کے ساتھ اپنا Visual Studio Code GitHub Copilot چیٹ بنائیں](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
      - [GitHub ماڈلز کے ذریعے Phi-3.5 کے ساتھ اپنا Visual Studio Code چیٹ کوپائلٹ ایجنٹ بنائیں](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

  - Advanced Reasoning Samples
    - Phi-4 Samples 🆕
      - [📓] [Phi-4-mini-reasoning یا Phi-4-reasoning کے نمونے](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
      - [📓] [Microsoft Olive کے ساتھ Phi-4-mini-reasoning کو Fine-tune کرنا](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Apple MLX کے ساتھ Phi-4-mini-reasoning کو Fine-tune کرنا](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [GitHub ماڈلز کے ساتھ Phi-4-mini-reasoning](../../md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
- [📓] [Phi-4-mini reasoning with Azure AI Foundry Models](../../md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
  - ڈیموز
      - [Phi-4-mini demos hosted on Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
      - [Phi-4-multimodal demos hosted on Hugginge Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
  - وژن کے نمونے
    - Phi-4 کے نمونے 🆕
      - [📓] [تصاویر پڑھنے اور کوڈ بنانے کے لیے Phi-4-multimodal استعمال کریں](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
    - Phi-3 / 3.5 کے نمونے
      -  [📓][Phi-3-vision-تصویر سے متن تک](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
      - [📓][Phi-3-vision CLIP ایمبیڈنگ](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [DEMO: Phi-3 ری سائیکلنگ](https://github.com/jennifermarsman/PhiRecycling/)
      - [Phi-3-vision - بصری زبان کا معاون - Phi3-Vision اور OpenVINO کے ساتھ](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
      - [Phi-3 وژن Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
      - [Phi-3 وژن OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
      - [📓][Phi-3.5 وژن ملٹی فریم یا ملٹی امیج نمونہ](../../md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
      - [Phi-3 وژن لوکل ONNX ماڈل Microsoft.ML.OnnxRuntime .NET استعمال کرتے ہوئے](../../md/04.HOL/dotnet/src/LabsPhi303)
      - [مینیو کی بنیاد پر Phi-3 وژن لوکل ONNX ماڈل Microsoft.ML.OnnxRuntime .NET استعمال کرتے ہوئے](../../md/04.HOL/dotnet/src/LabsPhi304)

  - آڈیو کے نمونے
    - Phi-4 کے نمونے 🆕
      - [📓] [Phi-4-multimodal سے آڈیو ٹرانسکرپٹس نکالنا](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
      - [📓] [Phi-4-multimodal آڈیو نمونہ](../../md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
      - [📓] [Phi-4-multimodal تقریر ترجمہ کا نمونہ](../../md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
      - [.NET کنسول ایپلیکیشن جو Phi-4-multimodal آڈیو استعمال کرتے ہوئے آڈیو فائل کا تجزیہ اور ٹرانسکرپٹ بناتی ہے](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

  - MOE کے نمونے
    - Phi-3 / 3.5 کے نمونے
      - [📓] [Phi-3.5 Mixture of Experts Models (MoEs) سوشل میڈیا نمونہ](../../md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
      - [📓] [NVIDIA NIM Phi-3 MOE، Azure AI Search، اور LlamaIndex کے ساتھ Retrieval-Augmented Generation (RAG) پائپ لائن بنانا](../../md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)
  - فنکشن کالنگ کے نمونے
    - Phi-4 کے نمونے 🆕
      -  [📓] [Phi-4-mini کے ساتھ فنکشن کالنگ استعمال کرنا](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
      -  [📓] [Phi-4-mini کے ساتھ ملٹی ایجنٹس بنانے کے لیے فنکشن کالنگ استعمال کرنا](../../md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
      -  [📓] [Ollama کے ساتھ فنکشن کالنگ استعمال کرنا](../../md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
  - ملٹی موڈل مکسنگ کے نمونے
    - Phi-4 کے نمونے 🆕
      -  [📓] [Phi-4-multimodal کو ٹیکنالوجی صحافی کے طور پر استعمال کرنا](../../md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
      - [.NET کنسول ایپلیکیشن جو Phi-4-multimodal استعمال کرتے ہوئے تصاویر کا تجزیہ کرتی ہے](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Phi کے نمونوں کی فائن ٹیوننگ
  - [فائن ٹیوننگ کے منظرنامے](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [فائن ٹیوننگ بمقابلہ RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [Phi-3 کو انڈسٹری ایکسپرٹ بنانے کے لیے فائن ٹیوننگ](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [VS Code کے AI Toolkit کے ساتھ Phi-3 کی فائن ٹیوننگ](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Azure Machine Learning Service کے ساتھ Phi-3 کی فائن ٹیوننگ](./md/03.FineTuning/Introduce_AzureML.md)
- [Fine-tuning Phi-3 with Lora](./md/03.FineTuning/FineTuning_Lora.md)
  - [Fine-tuning Phi-3 with QLora](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Fine-tuning Phi-3 with Azure AI Foundry](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Fine-tuning Phi-3 with Azure ML CLI/SDK](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Fine-tuning with Microsoft Olive](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Fine-tuning with Microsoft Olive Hands-On Lab](./md/03.FineTuning/olive-lab/readme.md)
  - [Fine-tuning Phi-3-vision with Weights and Bias](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [Fine-tuning Phi-3 with Apple MLX Framework](./md/03.FineTuning/FineTuning_MLX.md)
  - [Fine-tuning Phi-3-vision (official support)](./md/03.FineTuning/FineTuning_Vision.md)
  - [Fine-Tuning Phi-3 with Kaito AKS , Azure Containers(official Support)](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Fine-Tuning Phi-3 and 3.5 Vision](https://github.com/2U1/Phi3-Vision-Finetune)

- Hands on Lab
  - [جدید ترین ماڈلز کی تلاش: LLMs، SLMs، لوکل ڈیولپمنٹ اور مزید](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [NLP کی صلاحیت کو کھولنا: Microsoft Olive کے ساتھ Fine-Tuning](https://github.com/azure/Ignite_FineTuning_workshop)

- Academic Research Papers and Publications
  - [Textbooks Are All You Need II: phi-1.5 technical report](https://arxiv.org/abs/2309.05463)
  - [Phi-3 Technical Report: آپ کے فون پر ایک انتہائی قابل زبان ماڈل](https://arxiv.org/abs/2404.14219)
  - [Phi-4 Technical Report](https://arxiv.org/abs/2412.08905)
  - [Phi-4-Mini Technical Report: کمپیکٹ لیکن طاقتور ملٹی موڈل زبان ماڈلز Mixture-of-LoRAs کے ذریعے](https://arxiv.org/abs/2503.01743)
  - [گاڑی میں فنکشن کالنگ کے لیے چھوٹے زبان ماڈلز کی اصلاح](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) Fine-Tuning PHI-3 برائے ملٹیپل چوائس سوالات کا جواب دینا: طریقہ کار، نتائج، اور چیلنجز](https://arxiv.org/abs/2501.01588)
  - [Phi-4-reasoning Technical Report](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Phi-4-mini-reasoning Technical Report](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Phi ماڈلز کا استعمال

### Phi on Azure AI Foundry

آپ سیکھ سکتے ہیں کہ Microsoft Phi کو کیسے استعمال کیا جائے اور اپنے مختلف ہارڈویئر ڈیوائسز میں E2E حل کیسے بنائیں۔ Phi کا تجربہ کرنے کے لیے، ماڈلز کے ساتھ کھیلنا شروع کریں اور اپنے مناظر کے لیے Phi کو حسب ضرورت بنائیں [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai) پر۔ آپ مزید جان سکتے ہیں Getting Started with [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md) سے۔

**Playground**  
ہر ماڈل کے لیے ایک مخصوص playground موجود ہے جہاں ماڈل کو آزمایا جا سکتا ہے [Azure AI Playground](https://aka.ms/try-phi3)۔

### Phi on GitHub Models

آپ سیکھ سکتے ہیں کہ Microsoft Phi کو کیسے استعمال کیا جائے اور اپنے مختلف ہارڈویئر ڈیوائسز میں E2E حل کیسے بنائیں۔ Phi کا تجربہ کرنے کے لیے، ماڈل کے ساتھ کھیلنا شروع کریں اور اپنے مناظر کے لیے Phi کو حسب ضرورت بنائیں [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) پر۔ آپ مزید جان سکتے ہیں Getting Started with [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md) سے۔

**Playground**  
ہر ماڈل کے لیے ایک مخصوص [playground جہاں ماڈل کو آزمایا جا سکتا ہے](/md/02.QuickStart/GitHubModel_QuickStart.md)۔

### Phi on Hugging Face

آپ ماڈل کو [Hugging Face](https://huggingface.co/microsoft) پر بھی تلاش کر سکتے ہیں۔

**Playground**  
[Hugging Chat playground](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## ذمہ دار AI

Microsoft اپنے صارفین کی مدد کے لیے پرعزم ہے تاکہ وہ ہمارے AI مصنوعات کو ذمہ داری سے استعمال کریں، اپنے تجربات شیئر کریں، اور شفافیت نوٹس اور اثرات کے جائزوں جیسے ٹولز کے ذریعے اعتماد پر مبنی شراکت داریاں قائم کریں۔ ان میں سے بہت سے وسائل [https://aka.ms/RAI](https://aka.ms/RAI) پر دستیاب ہیں۔  
Microsoft کا ذمہ دار AI کے لیے نقطہ نظر ہمارے AI اصولوں پر مبنی ہے جو انصاف، اعتبار اور حفاظت، پرائیویسی اور سیکیورٹی، شمولیت، شفافیت، اور جوابدہی پر مشتمل ہے۔
نمونے میں استعمال ہونے والے بڑے پیمانے پر قدرتی زبان، تصویر، اور تقریر کے ماڈلز ممکنہ طور پر غیر منصفانہ، غیر قابل اعتماد، یا توہین آمیز طریقوں سے برتاؤ کر سکتے ہیں، جو کہ نقصان دہ ہو سکتے ہیں۔ خطرات اور حدود کے بارے میں آگاہی کے لیے براہ کرم [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) ملاحظہ کریں۔

ان خطرات کو کم کرنے کے لیے تجویز کردہ طریقہ یہ ہے کہ اپنی ساخت میں ایک حفاظتی نظام شامل کریں جو نقصان دہ رویے کا پتہ لگا سکے اور اسے روک سکے۔ [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) ایک آزاد حفاظتی پرت فراہم کرتا ہے جو ایپلیکیشنز اور خدمات میں صارف کی جانب سے اور AI کی جانب سے پیدا کردہ نقصان دہ مواد کا پتہ لگا سکتا ہے۔ Azure AI Content Safety میں ٹیکسٹ اور تصویر کے API شامل ہیں جو نقصان دہ مواد کی نشاندہی کرنے کی اجازت دیتے ہیں۔ Azure AI Foundry کے اندر، Content Safety سروس آپ کو مختلف طریقوں میں نقصان دہ مواد کا پتہ لگانے کے لیے نمونہ کوڈ دیکھنے، تلاش کرنے اور آزمانے کی سہولت دیتی ہے۔ درج ذیل [quickstart documentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) آپ کو سروس سے درخواستیں کرنے کے عمل میں رہنمائی فراہم کرتی ہے۔

ایک اور پہلو جسے مدنظر رکھنا ضروری ہے وہ مجموعی ایپلیکیشن کی کارکردگی ہے۔ کثیر وضع اور کثیر ماڈل ایپلیکیشنز کے ساتھ، ہم کارکردگی کو اس معنی میں لیتے ہیں کہ نظام آپ اور آپ کے صارفین کی توقعات کے مطابق کام کرے، جس میں نقصان دہ نتائج پیدا نہ کرنا بھی شامل ہے۔ اپنی مجموعی ایپلیکیشن کی کارکردگی کا اندازہ لگانے کے لیے [Performance and Quality and Risk and Safety evaluators](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) کا استعمال کریں۔ آپ کے پاس [custom evaluators](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators) بنانے اور ان کا جائزہ لینے کی بھی صلاحیت موجود ہے۔

آپ اپنے AI ایپلیکیشن کا جائزہ اپنے ترقیاتی ماحول میں [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html) کا استعمال کرتے ہوئے لے سکتے ہیں۔ چاہے آپ کے پاس ٹیسٹ ڈیٹا سیٹ ہو یا کوئی ہدف، آپ کی جنریٹیو AI ایپلیکیشن کی جنریشنز کو بلٹ ان یا اپنی پسند کے کسٹم ایولیویٹرز کے ذریعے مقداری طور پر ناپا جاتا ہے۔ اپنے نظام کا جائزہ لینے کے لیے Azure AI Evaluation SDK کے ساتھ شروع کرنے کے لیے، آپ [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) پر عمل کر سکتے ہیں۔ ایک بار جب آپ جائزہ چلائیں گے، تو آپ [Azure AI Foundry میں نتائج کو دیکھ سکتے ہیں](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results)۔

## Trademarks

یہ پروجیکٹ ممکنہ طور پر پروجیکٹس، مصنوعات، یا خدمات کے ٹریڈ مارکس یا لوگوز پر مشتمل ہو سکتا ہے۔ Microsoft کے ٹریڈ مارکس یا لوگوز کے مجاز استعمال کے لیے [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) کی پیروی ضروری ہے۔  
Microsoft کے ٹریڈ مارکس یا لوگوز کا اس پروجیکٹ کے ترمیم شدہ ورژنز میں استعمال الجھن پیدا نہیں کرے گا اور نہ ہی Microsoft کی حمایت کا تاثر دے گا۔ کسی بھی تیسرے فریق کے ٹریڈ مارکس یا لوگوز کا استعمال ان فریقوں کی پالیسیوں کے تابع ہے۔

**دستخط**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کی کوشش کرتے ہیں، براہ کرم آگاہ رہیں کہ خودکار ترجموں میں غلطیاں یا بے دقتیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں ہی معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ تجویز کیا جاتا ہے۔ ہم اس ترجمہ کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تعبیر کے ذمہ دار نہیں ہیں۔