# Phi کتابِ ترکیب: مائیکروسافٹ کے Phi ماڈلز کے ساتھ عملی مثالیں

[![GitHub Codespaces میں نمونے کھولیں اور استعمال کریں](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Dev Containers میں کھولیں](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub کے تعاون کنندگان](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub ایشوز](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub پل ریکویسٹ](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PRs کا خیرمقدم ہے](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub کے نگران](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub فورکز](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub اسٹارز](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi مائیکروسافٹ کی طرف سے تیار کردہ اوپن سورس AI ماڈلز کی ایک سیریز ہے۔

Phi اس وقت سب سے زیادہ طاقتور اور لاگت موثر چھوٹا زبان ماڈل (SLM) ہے، جس کے ملٹی زبان، استدلال، متن/چیٹ تخلیق، کوڈنگ، تصاویر، آڈیو اور دیگر منظرناموں میں بہت اچھے بینچ مارک ہیں۔

آپ Phi کو کلاؤڈ یا ایج ڈیوائسز پر تعینات کر سکتے ہیں، اور محدود کمپیوٹنگ پاور کے ساتھ آسانی سے جنریٹو AI ایپلیکیشنز بنا سکتے ہیں۔

ان وسائل کو استعمال کرنا شروع کرنے کے لیے یہ اقدامات کریں:  
1. **ریپوزیٹری کو فورک کریں**: کلک کریں [![GitHub فورکز](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)  
2. **ریپوزیٹری کلون کریں**: `git clone https://github.com/microsoft/PhiCookBook.git`  
3. [**Microsoft AI Discord کمیونٹی میں شامل ہوں اور ماہرین اور دیگر ڈویلپرز سے ملیں**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/ur/cover.eb18d1b9605d754b.webp)

### 🌐 کثیراللسانی معاونت

#### GitHub Action کے ذریعے سپورٹ یافتہ (خودکار اور ہمیشہ تازہ ترین)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](./README.md) | [Vietnamese](../vi/README.md)

> **مقامی طور پر کلون کرنا پسند کریں؟**  
>  
> اس ریپوزیٹری میں 50 سے زائد زبانوں کے تراجم شامل ہیں جو ڈاؤن لوڈ سائز کو نمایاں طور پر بڑھاتے ہیں۔ ترجمے کے بغیر کلون کرنے کے لیے sparse checkout استعمال کریں:  
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
> یہ آپ کو کورس مکمل کرنے کے لیے درکار تمام چیزیں بہت تیز ڈاؤن لوڈ کے ساتھ دیتا ہے۔  
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## فہرست مضامین

- تعارف  
  - [Phi فیملی میں خوش آمدید](./md/01.Introduction/01/01.PhiFamily.md)  
  - [اپنا ماحول ترتیب دینا](./md/01.Introduction/01/01.EnvironmentSetup.md)  
  - [اہم ٹیکنالوجیز کو سمجھنا](./md/01.Introduction/01/01.Understandingtech.md)  
  - [Phi ماڈلز کے لیے AI سیفٹی](./md/01.Introduction/01/01.AISafety.md)  
  - [Phi ہارڈویئر سپورٹ](./md/01.Introduction/01/01.Hardwaresupport.md)  
  - [Phi ماڈلز اور پلیٹ فارمز پر دستیابی](./md/01.Introduction/01/01.Edgeandcloud.md)  
  - [Guidance-ai اور Phi کا استعمال](./md/01.Introduction/01/01.Guidance.md)  
  - [GitHub مارکیٹ پلیس ماڈلز](https://github.com/marketplace/models)  
  - [Azure AI ماڈل کیٹلاگ](https://ai.azure.com)

- مختلف ماحول میں Phi کا انفرنس  
    -  [Hugging Face](./md/01.Introduction/02/01.HF.md)  
    -  [GitHub ماڈلز](./md/01.Introduction/02/02.GitHubModel.md)  
    -  [Microsoft Foundry ماڈل کیٹلاگ](./md/01.Introduction/02/03.AzureAIFoundry.md)  
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)  
    -  [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)  
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)  
    -  [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md)

- Phi فیملی کا انفرنس  
    - [iOS میں Phi انفرنس](./md/01.Introduction/03/iOS_Inference.md)  
    - [Android میں Phi انفرنس](./md/01.Introduction/03/Android_Inference.md)  
    - [Jetson میں Phi انفرنس](./md/01.Introduction/03/Jetson_Inference.md)  
    - [AI PC میں Phi انفرنس](./md/01.Introduction/03/AIPC_Inference.md)  
    - [Apple MLX فریم ورک کے ساتھ Phi انفرنس](./md/01.Introduction/03/MLX_Inference.md)  
    - [مقامی سرور میں Phi انفرنس](./md/01.Introduction/03/Local_Server_Inference.md)  
    - [AI Toolkit کے ذریعے ریموٹ سرور میں Phi انفرنس](./md/01.Introduction/03/Remote_Interence.md)  
    - [Rust کے ساتھ Phi انفرنس](./md/01.Introduction/03/Rust_Inference.md)  
    - [مقامی میں Phi--Vision انفرنس](./md/01.Introduction/03/Vision_Inference.md)  
    - [Kaito AKS، Azure Containers کے ساتھ Phi انفرنس (سرکاری سپورٹ)](./md/01.Introduction/03/Kaito_Inference.md)  
-  [Phi فیملی کی کوانٹفیکیشن](./md/01.Introduction/04/QuantifyingPhi.md)  
    - [llama.cpp کا استعمال کرتے ہوئے Phi-3.5 / 4 کی کوانٹائزنگ](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)  
    - [onnxruntime کے لیے جنریٹو AI ایکسٹینشنز کے ساتھ Phi-3.5 / 4 کی کوانٹائزنگ](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)  
    - [Intel OpenVINO کا استعمال کرتے ہوئے Phi-3.5 / 4 کی کوانٹائزنگ](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)  
    - [Apple MLX فریم ورک کا استعمال کرتے ہوئے Phi-3.5 / 4 کی کوانٹائزنگ](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

- Phi کا جائزہ  
    - [جوابدہی AI](./md/01.Introduction/05/ResponsibleAI.md)  
    - [Microsoft Foundry جائزے کے لیے](./md/01.Introduction/05/AIFoundry.md)  
    - [Promptflow کا استعمال کرتے ہوئے جائزہ](./md/01.Introduction/05/Promptflow.md)
 
- Azure AI سرچ کے ساتھ RAG  
    - [Phi-4-mini اور Phi-4-multimodal (RAG) کو Azure AI سرچ کے ساتھ کیسے استعمال کریں](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Phi ایپلیکیشن ڈویلپمنٹ کے نمونے  
  - متن اور چیٹ ایپلیکیشنز  
    - Phi-4 نمونے 🆕  
      - [📓] [Phi-4-mini ONNX ماڈل کے ساتھ چیٹ کریں](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)  
      - [Phi-4 مقامی ONNX ماڈل .NET کے ساتھ چیٹ](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)  
      - [Phi-4 ONNX کے ساتھ Sementic Kernel استعمال کرتے ہوئے .NET کنسول ایپ میں چیٹ](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)  
    - Phi-3 / 3.5 نمونے  
      - [براؤزر میں مقامی چیٹ بوٹ جو Phi3, ONNX Runtime Web اور WebGPU استعمال کرتا ہے](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [اوپن وینو چیٹ](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [ملٹی ماڈل - انٹرایکٹو فی-3-منی اور اوپن اے آئی وسپر](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [ایم ایل فلو - ایک ریپر بنانے اور فی-3 کو ایم ایل فلو کے ساتھ استعمال کرنا](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [ماڈل کی اصلاح - فی-3-منی ماڈل کو ONNX رن ٹائم ویب کے لیے اولیو کے ساتھ کیسے بہتر بنائیں](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [ون یو آئی 3 ایپ فی-3 منی-4k-انسٹرکٹ-onnx کے ساتھ](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      -[ون یو آئی 3 ملٹی ماڈل AI پاورڈ نوٹس ایپ سیمپل](https://github.com/microsoft/ai-powered-notes-winui3-sample)
      - [کسٹم فی-3 ماڈلز کو فائن ٹیون اور پرامپٹ فلو کے ساتھ ضم کریں](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
      - [ایژور AI فاؤنڈری میں پرامپٹ فلو کے ساتھ کسٹم فی-3 ماڈلز کو فائن ٹیون اور ضم کرنا](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
      - [ایژور AI فاؤنڈری میں مائیکروسافٹ کے ذمہ دار AI اصولوں پر توجہ دیتے ہوئے فائن ٹیون شدہ فی-3 / فی-3.5 ماڈل کا جائزہ](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
      - [📓] [فی-3.5-منی-انسٹرکٹ زبان کی پیش گوئی کا نمونہ (چینی/انگریزی)](./md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
      - [فی-3.5-انسٹرکٹ WebGPU RAG چیٹ بوٹ](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
      - [ونڈوز GPU کا استعمال کرتے ہوئے فی-3.5-انسٹرکٹ ONNX کے ساتھ پرامپٹ فلو کا حل بنانا](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
      - [مائیکروسافٹ فی-3.5 tflite کا استعمال کرتے ہوئے اینڈرائیڈ ایپ بنانا](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
      - [Q&A .NET مثال جو لوکل ONNX فی-3 ماڈل استعمال کرتی ہے Microsoft.ML.OnnxRuntime کے ساتھ](../../md/04.HOL/dotnet/src/LabsPhi301)
      - [سیمنٹک کرنل اور فی-3 کے ساتھ کنسول چیٹ .NET ایپ](../../md/04.HOL/dotnet/src/LabsPhi302)

  - ایژور AI انفیرنس SDK کوڈ بیسڈ سیمپلز
    - فی-4 سیمپلز 🆕
      - [📓] [فی-4-ملٹی موڈل استعمال کرتے ہوئے پروجیکٹ کوڈ بنائیں](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
    - فی-3 / 3.5 سیمپلز
      - [اپنا ویژول اسٹوڈیو کوڈ GitHub کوپائلٹ چیٹ مائیکروسافٹ فی-3 فیملی کے ساتھ بنائیں](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
      - [اپنا ویژول اسٹوڈیو کوڈ چیٹ کوپائلٹ ایجنٹ فی-3.5 کے ساتھ GitHub ماڈلز استعمال کرکے بنائیں](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

  - ایڈوانسڈ ریزننگ سیمپلز
    - فی-4 سیمپلز 🆕
      - [📓] [فی-4-منی-ریز ننگ یا فی-4-ریز ننگ سیمپلز](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
      - [📓] [مائیکروسافٹ اولیو کے ساتھ فی-4-منی-ریز ننگ کی فائن ٹیوننگ](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [ایپل MLX کے ساتھ فی-4-منی-ریز ننگ کی فائن ٹیوننگ](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [GitHub ماڈلز کے ساتھ فی-4-منی-ریز ننگ](./md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
      - [📓] [ایژور AI فاؤنڈری ماڈلز کے ساتھ فی-4-منی-ریز ننگ](./md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
  - ڈیموز
      - [فی-4-منی ڈیموز ہجی نگ فیس اسپیسز پر ہوسٹ کئے گئے](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
      - [فی-4-ملٹی موڈل ڈیموز ہجی نگ فیس اسپیسز پر ہوسٹ کئے گئے](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
  - وژن سیمپلز
    - فی-4 سیمپلز 🆕
      - [📓] [فی-4-ملٹی موڈل کا استعمال کرتے ہوئے تصاویر پڑھیں اور کوڈ بنائیں](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md)
    - فی-3 / 3.5 سیمپلز
      -  [📓][فی-3-وژن-امیج ٹیکسٹ ٹو ٹیکسٹ](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [فی-3-وژن-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
      - [📓][فی-3-وژن CLIP ایمبیڈنگ](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [ڈیمو: فی-3 ری سائیکلنگ](https://github.com/jennifermarsman/PhiRecycling/)
      - [فی-3-وژن - بصری زبان کی مددگار - فی3-وژن اور اوپن وینو کے ساتھ](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
      - [فی-3 وژن Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
      - [فی-3 وژن اوپن وینو](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
      - [📓][فی-3.5 وژن ملٹی فریم یا ملٹی امیج سیمپل](./md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
      - [فی-3 وژن لوکل ONNX ماڈل Microsoft.ML.OnnxRuntime .NET کے استعمال سے](../../md/04.HOL/dotnet/src/LabsPhi303)
      - [مینیو پر مبنی فی-3 وژن لوکل ONNX ماڈل Microsoft.ML.OnnxRuntime .NET کے استعمال سے](../../md/04.HOL/dotnet/src/LabsPhi304)

  - میتھ سیمپلز
    -  فی-4-منی-فلیش-ریز ننگ-انسٹرکٹ سیمپلز 🆕 [فی-4-منی-فلیش-ریز ننگ-انسٹرکٹ کے ساتھ میتھ ڈیمو](./md/02.Application/09.Math/MathDemo.ipynb)

  - آڈیو سیمپلز
    - فی-4 سیمپلز 🆕
      - [📓] [فی-4-ملٹی موڈل کا استعمال کرتے ہوئے آڈیو ٹرانسکرپٹس نکالنا](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
      - [📓] [فی-4-ملٹی موڈل آڈیو سیمپل](./md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
      - [📓] [فی-4-ملٹی موڈل اسپچ ٹرانسلیشن سیمپل](./md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
      - [.NET کنسول ایپلیکیشن فی-4-ملٹی موڈل آڈیو کا استعمال کرتے ہوئے ایک آڈیو فائل کا تجزیہ اور ٹرانسکرپٹ بنانا](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

  - MOE سیمپلز
    - فی-3 / 3.5 سیمپلز
      - [📓] [فی-3.5 ماہرین کا مجموعہ (MoEs) سوشل میڈیا سیمپل](./md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
      - [📓] [NVIDIA NIM فی-3 MOE، Azure AI سرچ، اور LlamaIndex کے ساتھ ریٹریول-آگمنٹڈ جنریشن (RAG) پائپ لائن بنانا](./md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)
      - 
  - فنکشن کالنگ سیمپلز
    - فی-4 سیمپلز 🆕
      -  [📓] [فی-4-منی کے ساتھ فنکشن کالنگ کا استعمال](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
      -  [📓] [فی-4-منی کے ساتھ ملٹی ایجنٹس بنانے کے لیے فنکشن کالنگ کا استعمال](./md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
      -  [📓] [اولاما کے ساتھ فنکشن کالنگ کا استعمال](./md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
      -  [📓] [ONNX کے ساتھ فنکشن کالنگ کا استعمال](./md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)
  - ملٹی موڈل مکسنگ سیمپلز
    - فی-4 سیمپلز 🆕
      -  [📓] [فی-4-ملٹی موڈل کو ایک ٹیکنالوجی صحافی کے طور پر استعمال کرنا](./md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
      - [.NET کنسول ایپلیکیشن فی-4-ملٹی موڈل کے ذریعے تصاویر کا تجزیہ کرنے کے لیے](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- فائن ٹیوننگ فی سیمپلز
  - [فائن ٹیوننگ کے منظرنامے](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [فائن ٹیوننگ بمقابلہ RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [فی-3 کو صنعت کا ماہر بنائیں](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [VS کوڈ کے لیے AI ٹول کٹ کے ساتھ فی-3 کی فائن ٹیوننگ](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [ایژور مشین لرننگ سروس کے ساتھ فی-3 کی فائن ٹیوننگ](./md/03.FineTuning/Introduce_AzureML.md)
  - [لورا کے ساتھ فی-3 کی فائن ٹیوننگ](./md/03.FineTuning/FineTuning_Lora.md)
  - [QLora کے ساتھ فی-3 کی فائن ٹیوننگ](./md/03.FineTuning/FineTuning_Qlora.md)
  - [ایژور AI فاؤنڈری کے ساتھ فی-3 کی فائن ٹیوننگ](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [ایژور ML CLI/SDK کے ساتھ فی-3 کی فائن ٹیوننگ](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [مائیکروسافٹ اولیو کے ساتھ فائن ٹیوننگ](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [مائیکروسافٹ اولیو ہینڈز آن لیب کے ساتھ فائن ٹیوننگ](./md/03.FineTuning/olive-lab/readme.md)
  - [Weights and Bias کے ساتھ فی-3-وژن کی فائن ٹیوننگ](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [ایپل MLX فریم ورک کے ساتھ فی-3 کی فائن ٹیوننگ](./md/03.FineTuning/FineTuning_MLX.md)
  - [فی-3-وژن کی فائن ٹیوننگ (سرکاری سپورٹ)](./md/03.FineTuning/FineTuning_Vision.md)
  - [Kaito AKS، ایژور کنٹینرز کے ساتھ فی-3 کی فائن ٹیوننگ (سرکاری سپورٹ)](./md/03.FineTuning/FineTuning_Kaito.md)
  - [فی-3 اور 3.5 وژن کی فائن ٹیوننگ](https://github.com/2U1/Phi3-Vision-Finetune)

- ہینڈز آن لیب
  - [جدید ماڈلز کی تلاش: LLMs، SLMs، لوکل ڈیولپمنٹ اور مزید](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [NLP کی صلاحیت کو کھولنا: مائیکروسافٹ اولیو کے ساتھ فائن ٹیوننگ](https://github.com/azure/Ignite_FineTuning_workshop)
- اکیڈمک تحقیقی مقالے اور اشاعتیں  
  - [Textbooks Are All You Need II: phi-1.5 تکنیکی رپورٹ](https://arxiv.org/abs/2309.05463)  
  - [Phi-3 تکنیکی رپورٹ: آپ کے فون پر مقامی طور پر ایک انتہائی قابل زبان کا ماڈل](https://arxiv.org/abs/2404.14219)  
  - [Phi-4 تکنیکی رپورٹ](https://arxiv.org/abs/2412.08905)  
  - [Phi-4-Mini تکنیکی رپورٹ: مکسچر-آف-LoRAs کے ذریعے کمپیکٹ مگر طاقتور ملٹی ماڈل زبان ماڈلز](https://arxiv.org/abs/2503.01743)  
  - [گاڑی میں فنکشن کالنگ کے لیے چھوٹے زبان ماڈلز کی بہتری](https://arxiv.org/abs/2501.02342)  
  - [(WhyPHI) ملٹیپل چوائس سوال جواب کے لیے PHI-3 کی فائن ٹیوننگ: طریقہ کار، نتائج، اور چیلنجز](https://arxiv.org/abs/2501.01588)  
  - [Phi-4-ریزننگ تکنیکی رپورٹ](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)  
  - [Phi-4-منی-ریزننگ تکنیکی رپورٹ](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)  

## فی ماڈلز کا استعمال

### Microsoft Foundry پر فی

آپ سیکھ سکتے ہیں کہ مائیکروسافٹ فی کو کیسے استعمال کریں اور اپنے مختلف ہارڈویئر آلات میں E2E حل کیسے بنائیں۔ فی کو خود تجربہ کرنے کے لیے، ماڈلز کے ساتھ کھیلنا شروع کریں اور اپنے مناظر کے لیے فی کو تخصیص کریں [Microsoft Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai) کے ذریعے آپ مزید جان سکتے ہیں Getting Started with [Microsoft Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md)  

**پلے گراؤنڈ**  
ہر ماڈل کے لیے مخصوص پلے گراؤنڈ ہوتا ہے تاکہ ماڈل کو آزمایا جا سکے [Azure AI Playground](https://aka.ms/try-phi3)۔  

### GitHub ماڈلز پر فی

آپ سیکھ سکتے ہیں کہ مائیکروسافٹ فی کو کیسے استعمال کریں اور اپنے مختلف ہارڈویئر آلات میں E2E حل کیسے بنائیں۔ فی کو خود تجربہ کرنے کے لیے، ماڈل کے ساتھ کھیلنا شروع کریں اور اپنے مناظر کے لیے فی کو تخصیص کریں [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) کے ذریعے آپ مزید جان سکتے ہیں Getting Started with [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md)  

**پلے گراؤنڈ**  
ہر ماڈل کے لیے مخصوص [پلے گراؤنڈ جہاں آپ ماڈل کو آزما سکتے ہیں](/md/02.QuickStart/GitHubModel_QuickStart.md)۔  

### Hugging Face پر فی

آپ ماڈل کو [Hugging Face](https://huggingface.co/microsoft) پر بھی تلاش کر سکتے ہیں۔  

**پلے گراؤنڈ**  
[Hugging Chat playground](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)  

## 🎒 دیگر کورسز

ہماری ٹیم دیگر کورسز بھی تیار کرتی ہے! ملاحظہ کریں:  

<!-- CO-OP TRANSLATOR OTHER COURSES START -->  
### LangChain  
[![LangChain4j for Beginners](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)  
[![LangChain.js for Beginners](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)  
[![LangChain for Beginners](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)  
---  

### Azure / Edge / MCP / Agents  
[![AZD for Beginners](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)  
[![Edge AI for Beginners](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)  
[![MCP for Beginners](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)  
[![AI Agents for Beginners](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)  

---  
 
### جنریٹو AI سیریز  
[![Generative AI for Beginners](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)  
[![Generative AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)  
[![Generative AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)  
[![Generative AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)  

---  
 
### بنیادی تعلیم  
[![ML for Beginners](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)  
[![Data Science for Beginners](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)  
[![AI for Beginners](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)  
[![Cybersecurity for Beginners](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)  
[![Web Dev for Beginners](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)  
[![IoT for Beginners](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)  
[![XR Development for Beginners](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)  

---  
 
### کوپائلٹ سیریز  
[![Copilot for AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)  
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)  
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)  
<!-- CO-OP TRANSLATOR OTHER COURSES END -->  

## ذمہ دارانہ AI  

مائیکروسافٹ اپنے صارفین کی مدد کرنے کے لیے پرعزم ہے کہ وہ ہمارے AI مصنوعات کو ذمہ داری کے ساتھ استعمال کریں، اپنی سیکھ کو شیئر کریں، اور شفافیت نوٹس اور اثر آراء جیسے آلات کے ذریعے اعتماد پر مبنی شراکت داری تشکیل دیں۔ ان میں سے کئی ذرائع [https://aka.ms/RAI](https://aka.ms/RAI) پر دستیاب ہیں۔  
مائیکروسافٹ کا ذمہ دار AI کا طریقہ کار ہمارے AI اصولوں پر مبنی ہے: انصاف، قابل اعتماد اور سلامتی، پرائیویسی اور سیکورٹی، شمولیت، شفافیت، اور حسابدہی۔  

بڑے پیمانے پر قدرتی زبان، تصویر، اور تقریر کے ماڈلز - جیسے اس نمونے میں استعمال ہونے والے - ممکنہ طور پر ایسے طریقوں سے برتاؤ کر سکتے ہیں جو غیر منصفانہ، غیر قابل اعتماد، یا توہین آمیز ہوں، جو نقصان کا باعث بن سکتے ہیں۔ براہ کرم [Azure OpenAI سروس شفافیت نوٹ](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) ملاحظہ کریں تاکہ خطرات اور حدود کے بارے میں آگاہ رہیں۔  

ان خطرات کو کم کرنے کے لیے سفارش کردہ طریقہ یہ ہے کہ اپنی آرکیٹیکچر میں ایک سیفٹی سسٹم شامل کریں جو نقصان دہ رویے کا پتہ لگا سکے اور اسے روک سکے۔ [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) ایک آزاد حفاظتی پرت فراہم کرتا ہے، جو ایپلیکیشنز اور خدمات میں صارف اور AI تیار کردہ نقصان دہ مواد کا پتہ لگا سکتا ہے۔ Azure AI Content Safety میں متن اور تصویر API شامل ہیں جو آپ کو نقصان دہ مواد کا پتہ لگانے کی اجازت دیتی ہیں۔ Microsoft Foundry کے اندر، Content Safety سروس آپ کو مختلف اقسام میں نقصان دہ مواد کی شناخت کرنے کے لیے نمونہ کوڈ دیکھنے، تلاش کرنے اور آزمانے کی سہولت دیتی ہے۔ درج ذیل [quickstart دستاویزات](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) آپ کو سروس کو درخواستیں بھیجنے میں رہنمائی فراہم کرتی ہیں۔
ایک اور پہلو جس پر غور کرنا ضروری ہے وہ مجموعی طور پر ایپلیکیشن کی کارکردگی ہے۔ کثیر النوع اور کثیر ماڈلز والی ایپلیکیشنز کے ساتھ، ہم کارکردگی سے مطلب لیتے ہیں کہ نظام آپ اور آپ کے صارفین کی توقعات کے مطابق کام کرے، بشمول نقصان دہ نتائج پیدا نہ کرنا۔ اپنے مجموعی ایپلیکیشن کی کارکردگی کا جائزہ لینا اہم ہے، جس کے لیے آپ [Performance and Quality and Risk and Safety evaluators](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) استعمال کر سکتے ہیں۔ آپ کے پاس یہ صلاحیت بھی ہے کہ آپ [custom evaluators](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators) بنا کر ان کے ذریعے جائزہ لیں۔

آپ اپنے ڈویلپمنٹ ماحولیاتی نظام میں [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html) استعمال کرتے ہوئے اپنی AI ایپلیکیشن کا جائزہ لے سکتے ہیں۔ چاہے آپ کے پاس ایک ٹیسٹ ڈیٹاسیٹ ہو یا کوئی ہدف، آپ کی تخلیقی AI ایپلیکیشن کی تخلیقات کو بلٹ ان ایویلیو ایٹرز یا اپنی پسند کے کسٹم ایویلیو ایٹرز کے ساتھ مقداری طور پر ناپا جاتا ہے۔ اپنے نظام کا جائزہ لینے کے لیے azure ai evaluation sdk کے ساتھ شروع کرنے کے لیے، آپ [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) پر عمل کر سکتے ہیں۔ ایک بار جب آپ ایویلیوایشن رن کو مکمل کر لیتے ہیں، تو آپ [Microsoft Foundry میں نتائج کو بصری شکل میں دیکھ سکتے ہیں](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results)۔

## ٹریڈ مارکس

یہ پراجیکٹ پروجیکٹس، مصنوعات، یا خدمات کے لئے ٹریڈ مارکس یا لوگوز پر مشتمل ہو سکتا ہے۔ Microsoft کے ٹریڈ مارکس یا لوگوز کا استعمال اجازت یافتہ ہے اور اسے [Microsoft کے Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) کے مطابق ہونا ضروری ہے۔ Microsoft کے ٹریڈ مارکس یا لوگوز کا اس پراجیکٹ کے ترمیم شدہ ورژن میں استعمال الجھن پیدا نہیں کرنا چاہیے اور نہ ہی Microsoft کی اسپانسرشپ کا اشارہ دینا چاہیے۔ تیسرے فریق کے ٹریڈ مارکس یا لوگوز کا استعمال ان تیسرے فریق کی پالیسیوں کے مطابق ہونا چاہیے۔

## مدد حاصل کرنا

اگر آپ کسی مسئلے میں پھنس جائیں یا AI ایپس بنانے کے بارے میں کوئی سوال ہو، تو شامل ہوں:

[![Microsoft Foundry Discord](https://img.shields.io/badge/Discord-Microsoft_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

اگر آپ کے پاس مصنوعات کے بارے میں تاثرات ہوں یا تعمیر کے دوران کوئی غلطی ہو تو یہاں جائیں:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**اعلانِ دستبرداری**:
اس دستاویز کا ترجمہ AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے کیا گیا ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار تراجم میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصلی دستاویز اپنی مادری زبان میں مستند ذریعہ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ورانہ انسانی ترجمہ کی سفارش کی جاتی ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا بدفہمی کے لیے ذمہ دار نہیں ہیں۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->