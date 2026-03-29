# মাইক্রোসফট ফাউন্ড্রিতে ফাইন-টিউন করা Phi-3 / Phi-3.5 মডেল মূল্যায়ন এমনকি মাইক্রোসফটের দায়িত্বশীল AI নীতিগুলির উপর ফোকাস

এই সামগ্রিক (E2E) উদাহরণটি মাইক্রোসফট টেক কমিউনিটির "[Evaluate Fine-tuned Phi-3 / 3.5 Models in Microsoft Foundry Focusing on Microsoft's Responsible AI](https://techcommunity.microsoft.com/blog/educatordeveloperblog/evaluate-fine-tuned-phi-3--3-5-models-in-azure-ai-studio-focusing-on-microsofts-/4227850?WT.mc_id=aiml-137032-kinfeylo)" গাইডের ভিত্তিতে।

## ওভারভিউ

### আপনি কীভাবে মাইক্রোসফট ফাউন্ড্রিতে একটি ফাইন-টিউন করা Phi-3 / Phi-3.5 মডেলের নিরাপত্তা এবং কার্যক্রম মূল্যায়ন করতে পারেন?

মডেল ফাইন-টিউন করলে কখনও কখনও অনিচ্ছাকৃত বা অনাকাঙ্ক্ষিত প্রতিক্রিয়া তৈরি হতে পারে। মডেলটি নিরাপদ এবং কার্যকর থাকে তা নিশ্চিত করতে, মডেলের ক্ষতিকর সামগ্রী তৈরি করার ক্ষমতা এবং সঠিক, প্রাসঙ্গিক, এবং সুসংগত প্রতিক্রিয়া দেওয়ার দক্ষতা মূল্যায়ন করা গুরুত্বপূর্ণ। এই টিউটোরিয়ালে, আপনি শিখবেন কীভাবে মাইক্রোসফট ফাউন্ড্রির সাথে Prompt flow একত্রীকৃত ফাইন-টিউন করা Phi-3 / Phi-3.5 মডেলের নিরাপত্তা এবং কার্যক্ষমতা মূল্যায়ন করবেন।

এখানে মাইক্রোসফট ফাউন্ড্রির একটি মূল্যায়ন প্রক্রিয়া দেখানো হলো।

![Architecture of tutorial.](../../../../../../translated_images/bn/architecture.10bec55250f5d6a4.webp)

*ছবির উৎস: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> Phi-3 / Phi-3.5 সম্পর্কিত আরও বিস্তারিত তথ্য এবং অতিরিক্ত রিসোর্সের জন্য দয়া করে [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723) পরিদর্শন করুন।

### প্রয়োজনীয়তা

- [Python](https://www.python.org/downloads)
- [Azure সাবস্ক্রিপশন](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- ফাইন-টিউন করা Phi-3 / Phi-3.5 মডেল

### বিষয়বস্তু তালিকা

1. [**সিনারিও ১: মাইক্রোসফট ফাউন্ড্রির Prompt flow মূল্যায়নের পরিচিতি**](#scenario-1-introduction-to-azure-ai-studios-prompt-flow-evaluation)

    - [নিরাপত্তা মূল্যায়নের পরিচিতি](#নিরাপত্তা-মূল্যায়নের-পরিচিতি)
    - [কার্যক্ষমতা মূল্যায়নের পরিচিতি](#কার্যক্ষমতা-মূল্যায়নের-পরিচিতি)

1. [**সিনারিও ২: মাইক্রোসফট ফাউন্ড্রিতে Phi-3 / Phi-3.5 মডেল মূল্যায়ন**](#scenario-2-evaluating-the-phi-3--phi-35-model-in-azure-ai-studio)

    - [শুরু করার আগে](#শুরু-করার-আগে)
    - [Phi-3 / Phi-3.5 মডেল মূল্যায়নের জন্য Azure OpenAI ডেপ্লয় করুন](#deploy-azure-openai-to-evaluate-the-phi-3--phi-35-model)
    - [মাইক্রোসফট ফাউন্ড্রির Prompt flow মূল্যায়ন ব্যবহার করে ফাইন-টিউন করা Phi-3 / Phi-3.5 মডেল মূল্যায়ন করুন](#evaluate-the-fine-tuned-phi-3--phi-35-model-using-azure-ai-studios-prompt-flow-evaluation)

1. [অভিনন্দন!](#অভিনন্দন)

## **সিনারিও ১: মাইক্রোসফট ফাউন্ড্রির Prompt flow মূল্যায়নের পরিচিতি**

### নিরাপত্তা মূল্যায়নের পরিচিতি

আপনার AI মডেল নৈতিক এবং নিরাপদ তা নিশ্চিত করতে, মাইক্রোসফটের দায়িত্বশীল AI নীতিগুলির বিরুদ্ধে এটি মূল্যায়ন করা অত্যন্ত গুরুত্বপূর্ণ। মাইক্রোসফট ফাউন্ড্রিতে, নিরাপত্তা মূল্যায়ন আপনাকে আপনার মডেলের জেলব্রেক আক্রমণের প্রতি দুর্বলতা এবং ক্ষতিকর সামগ্রী তৈরি করার সম্ভাবনা মূল্যায়ন করতে সক্ষম করে, যা সরাসরি এই নীতিগুলির সঙ্গে সামঞ্জস্যপূর্ণ।

![Safaty evaluation.](../../../../../../translated_images/bn/safety-evaluation.083586ec88dfa950.webp)

*ছবির উৎস: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### মাইক্রোসফটের দায়িত্বশীল AI নীতিমালা

প্রযুক্তিগত ধাপগুলি শুরু করার আগে, মাইক্রোসফটের দায়িত্বশীল AI নীতিমালা বোঝা অপরিহার্য। এটি একটি নৈতিক কাঠামো যা AI সিস্টেমের দায়িত্বশীল উন্নয়ন, মোতায়েন এবং পরিচালনা পরিচালনার জন্য তৈরি। এই নীতিগুলি AI সিস্টেমের দায়িত্বশীল নকশা, উন্নয়ন এবং মোতায়েনের জন্য পথপ্রদর্শক হিসেবে কাজ করে, নিশ্চিত করে যে AI প্রযুক্তিগুলি ন্যায্য, স্বচ্ছ এবং অন্তর্ভুক্তিমূলকভাবে নির্মিত হয়েছে। এই নীতিমালা AI মডেলগুলির নিরাপত্তা মূল্যায়নের ভিত্তি।

মাইক্রোসফটের দায়িত্বশীল AI নীতিমালা অন্তর্ভুক্ত:

- **ন্যায্যতা ও অন্তর্ভুক্তি**: AI সিস্টেমগুলোকে সবাইকে ন্যায্য আচরণ করতে হবে এবং সমান অবস্থায় থাকা মানুষের বিভিন্ন গোষ্ঠীগুলোর প্রতি ভিন্ন রকম আচরণ এড়াতে হবে। উদাহরণস্বরূপ, যখন AI সিস্টেমগুলি মেডিকেল চিকিৎসা, ঋণের আবেদন, বা কর্মসংস্থান সম্পর্কে পরামর্শ দেয়, তখন তাদের একই লক্ষণ, আর্থিক পরিস্থিতি, অথবা পেশাদার যোগ্যতা থাকা প্রত্যেকের জন্য এক ধরনের সুপারিশ প্রদান করতে হবে।

- **বিশ্বস্ততা ও নিরাপত্তা**: বিশ্বাস গড়ে তুলতে, AI সিস্টেমগুলো নির্ভরযোগ্য, নিরাপদ এবং ধারাবাহিকভাবে কাজ করা অপরিহার্য। এই সিস্টেমগুলোকে তাদের মূল ডিজাইনে যেমন তৈরি করা হয়েছিল, তেমন কাজ করতে হবে, অপ্রত্যাশিত পরিস্থিতিতে নিরাপদ প্রতিক্রিয়া দিতে হবে, এবং ক্ষতিকর হস্তক্ষেপ প্রতিরোধ করতে হবে। সিস্টেমের আচরণ এবং যে বিভিন্ন পরিস্থিতি তারা সামলাতে পারে তা ডিজাইন এবং পরীক্ষা করার সময় ডেভেলপাররা যে পরিস্থিতির আশা করেছিলেন তার প্রতিফলন।

- **স্বচ্ছতা**: যখন AI সিস্টেমগুলো মানুষের জীবনে বিশাল প্রভাব ফেলা সিদ্ধান্ত গ্রহণে সাহায্য করে, তখন মানুষকে বুঝতে হবে সেই সিদ্ধান্তগুলো কিভাবে নেওয়া হয়েছে। উদাহরণস্বরূপ, একটি ব্যাংক AI সিস্টেম ব্যবহার করতে পারে ব্যক্তির ক্রেডিটযোগ্যতা নির্ধারণের জন্য। একটি কোম্পানি AI সিস্টেম ব্যবহার করতে পারে সবচেয়ে যোগ্য প্রার্থীদের নির্বাচন করার জন্য।

- **গোপনীয়তা এবং নিরাপত্তা**: AI আরও বিসদৃঢ় হওয়ার সঙ্গে গোপনীয়তা রক্ষা এবং ব্যক্তিগত ও ব্যবসায়িক তথ্য নিরাপদ রাখা বেশি গুরুত্বপূর্ণ ও জটিল হয়ে উঠেছে। AI ব্যবহারে, গোপনীয়তা ও তথ্য সুরক্ষার প্রতি বিশেষ মনোযোগ প্রয়োজন কারণ AI সিস্টেমগুলোর সঠিক এবং তথ্যভিত্তিক পূর্বাভাস ও সিদ্ধান্ত নেওয়ার জন্য ডেটার প্রবেশাধিকার অপরিহার্য।

- **দায়বদ্ধতা**: যারা AI সিস্টেম ডিজাইন এবং মোতায়েন করেন তাদের জন্য তাদের সিস্টেম কিভাবে পরিচালিত হয় তার দায়িত্ব নেওয়া জরুরি। সংস্থাগুলোকে শিল্প মানদণ্ডের উপর ভিত্তি করে দায়বদ্ধতার নিয়মাবলী তৈরি করা উচিত। এই নিয়মগুলি নিশ্চিত করতে পারে যে AI সিস্টেম কোনো মানুষের জীবনের প্রতি প্রভাব ফেলা সিদ্ধান্তের চূড়ান্ত কর্তৃত্ব নয়। এছাড়াও, এগুলো নিশ্চিত করে মানুষেরা স্বতন্ত্রভাবে স্বয়ংসম্পূর্ণ AI সিস্টেমগুলোর উপর অর্থবহ নিয়ন্ত্রণ বজায় রাখে।

![Fill hub.](../../../../../../translated_images/bn/responsibleai2.c07ef430113fad8c.webp)

*ছবির উৎস: [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> মাইক্রোসফটের দায়িত্বশীল AI নীতিমালা সম্পর্কে আরও জানার জন্য, [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723) পৃষ্ঠাটি দেখুন।

#### নিরাপত্তা সূচক

এই টিউটোরিয়ালে, আপনি মাইক্রোসফট ফাউন্ড্রির নিরাপত্তা সূচক ব্যবহার করে ফাইন-টিউন করা Phi-3 মডেলের নিরাপত্তা মূল্যায়ন করবেন। এই সূচকগুলি মডেলের ক্ষতিকর সামগ্রী তৈরির সম্ভাবনা এবং জেলব্রেক আক্রমণের প্রতি তার দুর্বলতা যাচাই করতে সাহায্য করে। নিরাপত্তা সূচকগুলো হল:

- **স্ব-ক্ষতির সাথে সম্পর্কিত সামগ্রী**: পরীক্ষা করে মডেল স্ব-ক্ষতির সাথে সম্পর্কিত সামগ্রী তৈরি করার প্রবণতা রাখে কিনা।
- **ঘৃণামূলক এবং অন্যায় সামগ্রী**: পরীক্ষা করে মডেল ঘৃণামূলক বা অন্যায় সামগ্রী তৈরি করার প্রবণতা রাখে কিনা।
- **সহিংস সামগ্রী**: পরীক্ষা করে মডেল সহিংস সামগ্রী তৈরি করার প্রবণতা রাখে কিনা।
- **যৌন সম্পর্কিত সামগ্রী**: পরীক্ষা করে মডেল অবৈধ যৌন সম্পর্কিত সামগ্রী তৈরি করার প্রবণতা রাখে কিনা।

এই দিকগুলো মূল্যায়ন করা নিশ্চিত করে যে AI মডেলটি ক্ষতিকর বা আপত্তিকর সামগ্রী তৈরি করছে না, যা সমাজের মূল্যবোধ এবং নিয়ন্ত্রণ মানদণ্ডের সঙ্গে সামঞ্জস্যপূর্ণ।

![Evaluate based on safety.](../../../../../../translated_images/bn/evaluate-based-on-safety.c5df819f5b0bfc07.webp)

### কার্যক্ষমতা মূল্যায়নের পরিচিতি

আপনার AI মডেল প্রত্যাশামত কাজ করছে কি না নিশ্চিত করতে, এটি কার্যক্ষমতা সূচকের বিরুদ্ধে মূল্যায়ন করা গুরুত্বপূর্ণ। মাইক্রোসফট ফাউন্ড্রিতে, কার্যক্ষমতা মূল্যায়ন আপনাকে মডেলের সঠিক, প্রাসঙ্গিক এবং সুসংগত প্রতিক্রিয়া দেওয়ার দক্ষতা মূল্যায়ন করতে দেয়।

![Safaty evaluation.](../../../../../../translated_images/bn/performance-evaluation.48b3e7e01a098740.webp)

*ছবির উৎস: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### কার্যক্ষমতা সূচকসমূহ

এই টিউটোরিয়ালে, আপনি মাইক্রোসফট ফাউন্ড্রির কার্যক্ষমতা সূচক ব্যবহার করে ফাইন-টিউন করা Phi-3 / Phi-3.5 মডেলের কার্যক্ষমতা মূল্যায়ন করবেন। এই সূচকগুলি মডেলের সঠিক, প্রাসঙ্গিক, এবং সুসংগত প্রতিক্রিয়া তৈরির দক্ষতা নিরূপণে সাহায্য করে। কার্যক্ষমতা সূচকসমূহ হল:

- **ভিত্তিপ্রাপ্ততা (Groundedness)**: তৈরি প্রতিক্রিয়া কতটা ইনপুট উৎসের তথ্যের সঙ্গে সামঞ্জস্যপূর্ণ তা মূল্যায়ন।
- **প্রাসঙ্গিকতা (Relevance)**: প্রদত্ত প্রশ্নের সঙ্গে তৈরি প্রতিক্রিয়ার প্রাসঙ্গিকতা মূল্যায়ন।
- **সুসঙ্গতি (Coherence)**: তৈরি করা পাঠ্য কতটা স্বাভাবিকভাবে প্রবাহিত, মানবসদৃশ এবং নিয়মিত পড়ে তা মূল্যায়ন।
- **প্রবাহ (Fluency)**: তৈরি পাঠ্যের ভাষাগত দক্ষতা মূল্যায়ন।
- **GPT সাদৃশ্য (GPT Similarity)**: তৈরি প্রতিক্রিয়ার এবং মূল তথ্যের মিল যাচাই।
- **F1 স্কোর**: তৈরি প্রতিক্রিয়া এবং উৎস ডেটার মধ্যে ভাগাভাগি করা শব্দের অনুপাত হিসাব করে।

এই সূচকগুলো দিয়ে আপনি মডেলের কার্যক্ষমতা মূল্যায়ন করতে পারবেন।

![Evaluate based on performance.](../../../../../../translated_images/bn/evaluate-based-on-performance.3e801c647c7554e8.webp)

## **সিনারিও ২: মাইক্রোসফট ফাউন্ড্রিতে Phi-3 / Phi-3.5 মডেল মূল্যায়ন**

### শুরু করার আগে

এই টিউটোরিয়ালটি পূর্ববর্তী ব্লগ পোস্টের পরবর্তী ধাপ, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" এবং "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)"। এই পোস্টগুলোতে আমরা মাইক্রোসফট ফাউন্ড্রিতে Phi-3 / Phi-3.5 মডেল ফাইন-টিউন এবং Prompt flow এর সাথে একত্রীকরণের প্রক্রিয়া আলোচনা করেছিলাম।

এই টিউটোরিয়ালে, আপনি মাইক্রোসফট ফাউন্ড্রিতে একটি Azure OpenAI মডেল ইভ্যালুয়েটর হিসেবে ডেপ্লয় করবেন এবং এটি ব্যবহার করে আপনার ফাইন-টিউন করা Phi-3 / Phi-3.5 মডেলের মূল্যায়ন করবেন।

এই টিউটোরিয়াল শুরু করার আগে, নিশ্চিত করুন যে আপনার নিম্নলিখিত পূর্বশর্তাদি পূরণ হয়েছে, যা পূর্ববর্তী টিউটোরিয়ালে বর্ণনা করা হয়েছে:

1. ফাইন-টিউন করা Phi-3 / Phi-3.5 মডেল মূল্যায়নের জন্য প্রস্তুত একটি ডেটাসেট।
1. Phi-3 / Phi-3.5 একটি মডেল যা ফাইন-টিউন এবং Azure Machine Learning এ ডেপ্লয় করা হয়েছে।
1. মাইক্রোসফট ফাউন্ড্রিতে আপনার ফাইন-টিউন করা Phi-3 / Phi-3.5 মডেলের সাথে একত্রীকৃত Prompt flow।

> [!NOTE]
> আপনি পূর্ববর্তী ব্লগ পোস্ট থেকে ডাউনলোড করা **ULTRACHAT_200k** ডেটাসেটের data ফোল্ডারে থাকা *test_data.jsonl* ফাইলটিকে ফাইন-টিউন করা Phi-3 / Phi-3.5 মডেল মূল্যায়নের জন্য ডেটাসেট হিসেবে ব্যবহার করবেন।

#### মাইক্রোসফট ফাউন্ড্রিতে Prompt flow এর সাথে কাস্টম Phi-3 / Phi-3.5 মডেল ইন্টিগ্রেশন (প্রথমে কোড পদ্ধতি)

> [!NOTE]
> আপনি যদি "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)"-এ বর্ণিত কম-কোড পদ্ধতি অনুসরণ করে থাকেন, তাহলে এই অনুশীলনটি এড়িয়ে পরবর্তী ধাপে যেতে পারেন।
> তবে, আপনি যদি "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)"-এ বর্ণিত কোড-প্রথম পদ্ধতি অনুসরণ করে Phi-3 / Phi-3.5 মডেল ফাইন-টিউন এবং ডেপ্লয় করে থাকেন, তাহলে আপনার মডেলটি Prompt flow-তে সংযোগ করার প্রক্রিয়াটি একটু আলাদা হবে। এই অনুশীলনে আপনি এই প্রক্রিয়া শিখবেন।

অগ্রসর হওয়ার জন্য, আপনাকে মাইক্রোসফট ফাউন্ড্রির মধ্যে আপনার ফাইন-টিউন করা Phi-3 / Phi-3.5 মডেল Prompt flow-তে সংযুক্ত করতে হবে।

#### মাইক্রোসফট ফাউন্ড্রি হাব তৈরি করুন

প্রকল্প (Project) তৈরি করার আগে একটি হাব তৈরি করতে হবে। একটি হাব রিসোর্স গ্রুপের মতো কাজ করে, যা মাইক্রোসফট ফাউন্ড্রির মধ্যে একাধিক প্রকল্প সংগঠিত এবং পরিচালনা করার সুযোগ দেয়।
1. সাইন ইন করুন [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) এ।

1. বাম দিকের ট্যাব থেকে **All hubs** নির্বাচন করুন।

1. নেভিগেশন মেনু থেকে **+ New hub** নির্বাচন করুন।

    ![Create hub.](../../../../../../translated_images/bn/create-hub.5be78fb1e21ffbf1.webp)

1. নিম্নলিখিত কাজগুলি সম্পন্ন করুন:

    - **Hub name** প্রবেশ করুন। এটি একটি অনন্য মান হতে হবে।
    - আপনার Azure **Subscription** নির্বাচন করুন।
    - ব্যবহারের জন্য **Resource group** নির্বাচন করুন (প্রয়োজনে নতুন একটি তৈরি করুন)।
    - আপনি যেই **Location** ব্যবহার করতে চান তা নির্বাচন করুন।
    - ব্যবহারের জন্য **Connect Azure AI Services** নির্বাচন করুন (প্রয়োজনে নতুন একটি তৈরি করুন)।
    - **Connect Azure AI Search** নির্বাচন করে **Skip connecting** করুন।

    ![Fill hub.](../../../../../../translated_images/bn/fill-hub.baaa108495c71e34.webp)

1. **Next** নির্বাচন করুন।

#### Microsoft Foundry প্রকল্প তৈরি করুন

1. আপনি যে হাবটি তৈরি করেছেন, সেখানে বাম দিকের ট্যাব থেকে **All projects** নির্বাচন করুন।

1. নেভিগেশন মেনু থেকে **+ New project** নির্বাচন করুন।

    ![Select new project.](../../../../../../translated_images/bn/select-new-project.cd31c0404088d7a3.webp)

1. **Project name** প্রবেশ করুন। এটি একটি অনন্য মান হতে হবে।

    ![Create project.](../../../../../../translated_images/bn/create-project.ca3b71298b90e420.webp)

1. **Create a project** নির্বাচন করুন।

#### ফাইন-টিউন করা Phi-3 / Phi-3.5 মডেলের জন্য একটি কাস্টম সংযোগ যোগ করুন

আপনার কাস্টম Phi-3 / Phi-3.5 মডেলকে Prompt flow এর সাথে একীকরণ করতে, আপনাকে মডেলের endpoint এবং key কাস্টম সংযোগে সংরক্ষণ করতে হবে। এই সেটআপটি নিশ্চিত করবে যে আপনি Prompt flow এ আপনার কাস্টম Phi-3 / Phi-3.5 মডেলে অ্যাক্সেস পাবেন।

#### ফাইন-টিউন করা Phi-3 / Phi-3.5 মডেলের api key এবং endpoint uri সেট করুন

1. যান [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) এ।

1. আপনি যে Azure Machine learning workspace তৈরি করেছেন সেখানে নেভিগেট করুন।

1. বাম দিকের ট্যাব থেকে **Endpoints** নির্বাচন করুন।

    ![Select endpoints.](../../../../../../translated_images/bn/select-endpoints.ee7387ecd68bd18d.webp)

1. আপনি যে endpoint তৈরি করেছেন তা নির্বাচন করুন।

    ![Select endpoints.](../../../../../../translated_images/bn/select-endpoint-created.9f63af5e4cf98b2e.webp)

1. নেভিগেশন মেনু থেকে **Consume** নির্বাচন করুন।

1. আপনার **REST endpoint** এবং **Primary key** কপি করুন।

    ![Copy api key and endpoint uri.](../../../../../../translated_images/bn/copy-endpoint-key.0650c3786bd646ab.webp)

#### কাস্টম সংযোগ যোগ করুন

1. যান [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) এ।

1. আপনি যে Microsoft Foundry প্রকল্প তৈরি করেছেন সেখানে নেভিগেট করুন।

1. আপনি যে প্রকল্প তৈরি করেছেন, সেখানে বাম দিকের ট্যাব থেকে **Settings** নির্বাচন করুন।

1. **+ New connection** নির্বাচন করুন।

    ![Select new connection.](../../../../../../translated_images/bn/select-new-connection.fa0f35743758a74b.webp)

1. নেভিগেশন মেনু থেকে **Custom keys** নির্বাচন করুন।

    ![Select custom keys.](../../../../../../translated_images/bn/select-custom-keys.5a3c6b25580a9b67.webp)

1. নিম্নলিখিত কাজগুলি সম্পন্ন করুন:

    - **+ Add key value pairs** নির্বাচন করুন।
    - key name এ **endpoint** লিখুন এবং Azure ML Studio থেকে কপি করা endpoint মানটি value ফিল্ডে পেস্ট করুন।
    - আবার **+ Add key value pairs** নির্বাচন করুন।
    - key name এ **key** লিখুন এবং Azure ML Studio থেকে কপি করা key মানটি value ফিল্ডে পেস্ট করুন।
    - কী যোগ করার পরে, কী গোপন রাখার জন্য **is secret** নির্বাচন করুন।

    ![Add connection.](../../../../../../translated_images/bn/add-connection.ac7f5faf8b10b0df.webp)

1. **Add connection** নির্বাচন করুন।

#### Prompt flow তৈরি করুন

আপনি Microsoft Foundry তে একটি কাস্টম সংযোগ যোগ করেছেন। এখন, নিচের ধাপগুলো অনুসরণ করে একটি Prompt flow তৈরি করুন। এরপর, আপনি এই Prompt flow কে কাস্টম সংযোগের সাথে সংযুক্ত করবেন যাতে ফাইন-টিউন করা মডেল Prompt flow এর মধ্যে ব্যবহার করা যায়।

1. আপনি যে Microsoft Foundry প্রকল্প তৈরি করেছেন সেখানে নেভিগেট করুন।

1. বাম দিকের ট্যাব থেকে **Prompt flow** নির্বাচন করুন।

1. নেভিগেশন মেনু থেকে **+ Create** নির্বাচন করুন।

    ![Select Promptflow.](../../../../../../translated_images/bn/select-promptflow.18ff2e61ab9173eb.webp)

1. নেভিগেশন মেনু থেকে **Chat flow** নির্বাচন করুন।

    ![Select chat flow.](../../../../../../translated_images/bn/select-flow-type.28375125ec9996d3.webp)

1. ব্যবহারের জন্য **Folder name** প্রবেশ করুন।

    ![Select chat flow.](../../../../../../translated_images/bn/enter-name.02ddf8fb840ad430.webp)

1. **Create** নির্বাচন করুন।

#### Prompt flow সেট আপ করুন আপনার কাস্টম Phi-3 / Phi-3.5 মডেলের সাথে চ্যাট করার জন্য

আপনাকে ফাইন-টিউন করা Phi-3 / Phi-3.5 মডেল Prompt flow এ একীভূত করতে হবে। তবে, বিদ্যমান Prompt flow এই উদ্দেশ্যে ডিজাইন করা হয়নি। অতএব, আপনাকে Prompt flow পুনর্নকশা করতে হবে যাতে কাস্টম মডেলটি সংযুক্ত করা যায়।

1. Prompt flow এ নিচের কাজগুলি করুন বিদ্যমান ফ্লো পুনর্নির্মাণের জন্য:

    - **Raw file mode** নির্বাচন করুন।
    - *flow.dag.yml* ফাইলে থাকা সমস্ত কোড মোছা করুন।
    - *flow.dag.yml* ফাইলে নিম্নলিখিত কোড যুক্ত করুন।

        ```yml
        inputs:
          input_data:
            type: string
            default: "Who founded Microsoft?"

        outputs:
          answer:
            type: string
            reference: ${integrate_with_promptflow.output}

        nodes:
        - name: integrate_with_promptflow
          type: python
          source:
            type: code
            path: integrate_with_promptflow.py
          inputs:
            input_data: ${inputs.input_data}
        ```

    - **Save** নির্বাচন করুন।

    ![Select raw file mode.](../../../../../../translated_images/bn/select-raw-file-mode.06c1eca581ce4f53.webp)

1. Prompt flow এ কাস্টম Phi-3 / Phi-3.5 মডেল ব্যবহারের জন্য *integrate_with_promptflow.py* ফাইলে নিচের কোড যুক্ত করুন।

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # লগিং সেটআপ
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG
    )
    logger = logging.getLogger(__name__)

    def query_phi3_model(input_data: str, connection: CustomConnection) -> str:
        """
        Send a request to the Phi-3 / Phi-3.5 model endpoint with the given input data using Custom Connection.
        """

        # "connection" হল কাস্টম কানেকশনের নাম, "endpoint", "key" হল কাস্টম কানেকশনে থাকা চাবিগুলো
        endpoint_url = connection.endpoint
        api_key = connection.key

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
    data = {
        "input_data": [input_data],
        "params": {
            "temperature": 0.7,
            "max_new_tokens": 128,
            "do_sample": True,
            "return_full_text": True
            }
        }
        try:
            response = requests.post(endpoint_url, json=data, headers=headers)
            response.raise_for_status()
            
            # সম্পূর্ণ JSON প্রতিক্রিয়া লগ করুন
            logger.debug(f"Full JSON response: {response.json()}")

            result = response.json()["output"]
            logger.info("Successfully received response from Azure ML Endpoint.")
            return result
        except requests.exceptions.RequestException as e:
            logger.error(f"Error querying Azure ML Endpoint: {e}")
            raise

    @tool
    def my_python_tool(input_data: str, connection: CustomConnection) -> str:
        """
        Tool function to process input data and query the Phi-3 / Phi-3.5 model.
        """
        return query_phi3_model(input_data, connection)

    ```

    ![Paste prompt flow code.](../../../../../../translated_images/bn/paste-promptflow-code.cd6d95b101c0ec28.webp)

> [!NOTE]
> Microsoft Foundry তে Prompt flow ব্যবহারের বিষয়ে আরও বিস্তারিত তথ্যের জন্য, আপনি [Prompt flow in Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow) দেখুন।

1. **Chat input**, **Chat output** নির্বাচন করুন যাতে আপনার মডেলের সাথে চ্যাট সক্ষম হয়।

    ![Select Input Output.](../../../../../../translated_images/bn/select-input-output.c187fc58f25fbfc3.webp)

1. এখন আপনি আপনার কাস্টম Phi-3 / Phi-3.5 মডেলের সাথে চ্যাট করতে প্রস্তুত। পরবর্তী অনুশীলনে, আপনি শিখবেন কীভাবে Prompt flow শুরু করবেন এবং এটি ব্যবহার করে ফাইন-টিউন করা Phi-3 / Phi-3.5 মডেলের সাথে চ্যাট করবেন।

> [!NOTE]
>
> পুনর্নির্মিত ফ্লো নিচের ছবির মতো হওয়া উচিত:
>
> ![Flow example](../../../../../../translated_images/bn/graph-example.82fd1bcdd3fc545b.webp)
>

#### Prompt flow শুরু করুন

1. Prompt flow শুরু করতে **Start compute sessions** নির্বাচন করুন।

    ![Start compute session.](../../../../../../translated_images/bn/start-compute-session.9acd8cbbd2c43df1.webp)

1. প্যারামিটার নতুন করার জন্য **Validate and parse input** নির্বাচন করুন।

    ![Validate input.](../../../../../../translated_images/bn/validate-input.c1adb9543c6495be.webp)

1. আপনি যে কাস্টম সংযোগ তৈরি করেছেন তার **connection** এর **Value** নির্বাচন করুন। উদাহরণস্বরূপ, *connection*।

    ![Connection.](../../../../../../translated_images/bn/select-connection.1f2b59222bcaafef.webp)

#### আপনার কাস্টম Phi-3 / Phi-3.5 মডেলের সাথে চ্যাট করুন

1. **Chat** নির্বাচন করুন।

    ![Select chat.](../../../../../../translated_images/bn/select-chat.0406bd9687d0c49d.webp)

1. ফলাফলের একটি উদাহরণ এখানে দেওয়া হলো: এখন আপনি আপনার কাস্টম Phi-3 / Phi-3.5 মডেলের সাথে চ্যাট করতে পারেন। ফাইন-টিউনিং এর জন্য ব্যবহৃত ডেটার ওপর ভিত্তি করে প্রশ্ন করার পরামর্শ দেওয়া হয়।

    ![Chat with prompt flow.](../../../../../../translated_images/bn/chat-with-promptflow.1cf8cea112359ada.webp)

### Phi-3 / Phi-3.5 মডেল মূল্যায়নের জন্য Azure OpenAI মোডেল ডিপ্লয় করুন

Microsoft Foundry তে Phi-3 / Phi-3.5 মডেল মূল্যায়নের জন্য, আপনাকে একটি Azure OpenAI মডেল ডিপ্লয় করতে হবে। এই মডেলটি Phi-3 / Phi-3.5 মডেলের পারফরম্যান্স মূল্যায়নে ব্যবহৃত হবে।

#### Azure OpenAI ডিপ্লয় করুন

1. [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) এ সাইন ইন করুন।

1. আপনি যে Microsoft Foundry প্রকল্প তৈরি করেছেন সেখানে নেভিগেট করুন।

    ![Select Project.](../../../../../../translated_images/bn/select-project-created.5221e0e403e2c9d6.webp)

1. আপনি যে প্রকল্প তৈরি করেছেন, সেখানে বাম দিকের ট্যাব থেকে **Deployments** নির্বাচন করুন।

1. নেভিগেশন মেনু থেকে **+ Deploy model** নির্বাচন করুন।

1. **Deploy base model** নির্বাচন করুন।

    ![Select Deployments.](../../../../../../translated_images/bn/deploy-openai-model.95d812346b25834b.webp)

1. আপনি যে Azure OpenAI মডেলটি ব্যবহার করতে চান তা নির্বাচন করুন। উদাহরণস্বরূপ, **gpt-4o**।

    ![Select Azure OpenAI model you'd like to use.](../../../../../../translated_images/bn/select-openai-model.959496d7e311546d.webp)

1. **Confirm** নির্বাচন করুন।

### Microsoft Foundry এর Prompt flow মূল্যায়ন ব্যবহার করে ফাইন-টিউন করা Phi-3 / Phi-3.5 মডেল মূল্যায়ন করুন

### একটি নতুন মূল্যায়ন শুরু করুন

1. যান [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) এ।

1. আপনি যে Microsoft Foundry প্রকল্প তৈরি করেছেন সেখানে নেভিগেট করুন।

    ![Select Project.](../../../../../../translated_images/bn/select-project-created.5221e0e403e2c9d6.webp)

1. আপনি যে প্রকল্প তৈরি করেছেন, সেখানে বাম দিকের ট্যাব থেকে **Evaluation** নির্বাচন করুন।

1. নেভিগেশন মেনু থেকে **+ New evaluation** নির্বাচন করুন।

    ![Select evaluation.](../../../../../../translated_images/bn/select-evaluation.2846ad7aaaca7f4f.webp)

1. **Prompt flow** মূল্যায়ন নির্বাচন করুন।

    ![Select Prompt flow evaluation.](../../../../../../translated_images/bn/promptflow-evaluation.cb9758cc19b4760f.webp)

1. নিম্নলিখিত কাজগুলি সম্পন্ন করুন:

    - মূল্যায়নের নাম প্রবেশ করুন। এটি একটি অনন্য মান হতে হবে।
    - কাজের ধরন হিসেবে **Question and answer without context** নির্বাচন করুন। কারণ, এই টিউটোরিয়ালে ব্যবহৃত **UlTRACHAT_200k** ডেটাসেটে কোনো context নেই।
    - আপনি যে prompt flow মূল্যায়ন করতে চান তা নির্বাচন করুন।

    ![Prompt flow evaluation.](../../../../../../translated_images/bn/evaluation-setting1.4aa08259ff7a536e.webp)

1. **Next** নির্বাচন করুন।

1. নিম্নলিখিত কাজগুলি সম্পন্ন করুন:

    - **Add your dataset** নির্বাচন করে ডেটাসেট আপলোড করুন। উদাহরণস্বরূপ, আপনি **ULTRACHAT_200k** ডেটাসেট ডাউনলোড করার সময় অন্তর্ভুক্ত পরীক্ষামূলক ডেটাসেট ফাইল যেমন *test_data.json1* আপলোড করতে পারেন।
    - আপনার ডেটাসেটের সাথে মিল রেখে উপযুক্ত **Dataset column** নির্বাচন করুন। উদাহরণস্বরূপ, যদি আপনি **ULTRACHAT_200k** ডেটাসেট ব্যবহার করছেন, তবে dataset column হিসেবে **${data.prompt}** নির্বাচন করুন।

    ![Prompt flow evaluation.](../../../../../../translated_images/bn/evaluation-setting2.07036831ba58d64e.webp)

1. **Next** নির্বাচন করুন।

1. পারফরম্যান্স এবং গুণগত মান মেট্রিক্স সেট আপ করতে নিম্নলিখিত কাজগুলি করুন:

    - আপনি যে পারফরম্যান্স এবং গুণগত মান মেট্রিক্স ব্যবহার করতে চান তা নির্বাচন করুন।
    - মূল্যায়নের জন্য আপনি যে Azure OpenAI মডেল তৈরি করেছেন তা নির্বাচন করুন। উদাহরণস্বরূপ, **gpt-4o** নির্বাচন করুন।

    ![Prompt flow evaluation.](../../../../../../translated_images/bn/evaluation-setting3-1.d1ae69e3bf80914e.webp)

1. ঝুঁকি ও সুরক্ষা মেট্রিক্স সেট আপ করতে নিম্নলিখিত কাজগুলি করুন:

    - আপনি যে ঝুঁকি এবং সুরক্ষা মেট্রিক্স ব্যবহার করতে চান তা নির্বাচন করুন।
    - আপনি যে থ্রেশহোল্ড দিয়ে ডেফেক্ট রেট গণনা করতে চান তা নির্বাচন করুন। উদাহরণস্বরূপ, **Medium** নির্বাচন করুন।
    - **question** এর জন্য **Data source** হিসেবে **{$data.prompt}** নির্বাচন করুন।
    - **answer** এর জন্য **Data source** হিসেবে **{$run.outputs.answer}** নির্বাচন করুন।
    - **ground_truth** এর জন্য **Data source** হিসেবে **{$data.message}** নির্বাচন করুন।

    ![Prompt flow evaluation.](../../../../../../translated_images/bn/evaluation-setting3-2.d53bd075c60a45a2.webp)

1. **Next** নির্বাচন করুন।

1. মূল্যায়ন শুরু করতে **Submit** নির্বাচন করুন।

1. মূল্যায়ন সম্পন্ন হতে কিছু সময় লাগবে। আপনি **Evaluation** ট্যাবে অগ্রগতি মনিটর করতে পারবেন।

### মূল্যায়নের ফলাফল পর্যালোচনা করুন

> [!NOTE]
> নিচে প্রদত্ত ফলাফল কেবলমাত্র মূল্যায়ন প্রক্রিয়া প্রদর্শনের উদ্দেশ্যে দেয়া হয়েছে। এই টিউটোরিয়ালে আমরা একটি তুলনামূলক ছোট ডেটাসেটে ফাইন-টিউন করা মডেল ব্যবহার করেছি, যার ফলে ফলাফল আদর্শের চেয়ে কম হতে পারে। প্রকৃত ফলাফল ডেটাসেটের আকার, গুণমান এবং বৈচিত্র্য সঙ্গে মডেলের নির্দিষ্ট কনফিগারেশনের উপর ব্যাপকভাবে নির্ভর করে পরিবর্তিত হতে পারে।

মূল্যায়ন শেষ হওয়ার পর, আপনি পারফরম্যান্স এবং সুরক্ষা মেট্রিক্স উভয়ের জন্য ফলাফল পর্যালোচনা করতে পারবেন।
1. পারফরম্যান্স এবং গুণমান মেট্রিক:

    - মডেলের দক্ষতা মূল্যায়ন করুন সঙ্গতিপূর্ণ, স্বচ্ছন্দ এবং প্রাসঙ্গিক প্রতিক্রিয়া তৈরি করতে।

    ![Evaluation result.](../../../../../../translated_images/bn/evaluation-result-gpu.85f48b42dfb74254.webp)

1. ঝুঁকি এবং নিরাপত্তা মেট্রিক:

    - নিশ্চিত করুন যে মডেলের আউটপুট নিরাপদ এবং রেসপন্সিবল AI প্রিন্সিপলের সাথে সামঞ্জস্যপূর্ণ, কোনো ক্ষতিকারক বা আপত্তিকর বিষয়বস্তু এড়িয়ে।

    ![Evaluation result.](../../../../../../translated_images/bn/evaluation-result-gpu-2.1b74e336118f4fd0.webp)

1. আপনি নিচে স্ক্রল করে **বিস্তৃত মেট্রিক ফলাফল** দেখতে পারেন।

    ![Evaluation result.](../../../../../../translated_images/bn/detailed-metrics-result.afa2f5c39a4f5f17.webp)

1. আপনার কাস্টম Phi-3 / Phi-3.5 মডেল পারফরম্যান্স এবং নিরাপত্তা মেট্রিক উভয়ের বিরুদ্ধে মূল্যায়ন করে, আপনি নিশ্চিত করতে পারেন যে মডেল শুধুমাত্র কার্যকর নয়, বরং রেসপন্সিবল AI অনুশীলন মেনে চলে, যা এটিকে বাস্তব বিশ্বের প্রয়োগের জন্য প্রস্তুত করে তোলে।

## অভিনন্দন!

### আপনি এই টিউটোরিয়াল সম্পন্ন করেছেন

আপনি সফলভাবে Microsoft Foundry-তে Prompt flow এর সাথে একীকৃত ফাইন-টিউন করা Phi-3 মডেল মূল্যায়ন করেছেন। এটি একটি গুরুত্বপূর্ণ ধাপ যা নিশ্চিত করে আপনার AI মডেলগুলি কেবল ভাল পারফর্ম করে না, বরং Microsoft-এর রেসপন্সিবল AI নীতিমালা মেনে চলে যা আপনাকে বিশ্বাসযোগ্য এবং নির্ভরযোগ্য AI অ্যাপ্লিকেশন তৈরি করতে সহায়তা করে।

![Architecture.](../../../../../../translated_images/bn/architecture.10bec55250f5d6a4.webp)

## Azure রিসোর্সগুলি পরিস্কার করুন

অতিরিক্ত চার্জ এড়াতে আপনার Azure রিসোর্সগুলি পরিস্কার করুন। Azure পোর্টালে যান এবং নিম্নলিখিত রিসোর্সগুলি মুছে ফেলুন:

- Azure Machine learning রিসোর্স।
- Azure Machine learning মডেল এন্ডপয়েন্ট।
- Microsoft Foundry প্রকল্প রিসোর্স।
- Microsoft Foundry Prompt flow রিসোর্স।

### পরবর্তী ধাপ

#### ডকুমেন্টেশন

- [রেসপন্সিবল AI ড্যাশবোর্ড ব্যবহার করে AI সিস্টেম মূল্যায়ন করুন](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [জেনারেটিভ AI এর জন্য মূল্যায়ন এবং পর্যবেক্ষণ মেট্রিক](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Microsoft Foundry ডকুমেন্টেশন](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Prompt flow ডকুমেন্টেশন](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### প্রশিক্ষণ সামগ্রী

- [Microsoft-এর রেসপন্সিবল AI প্রবাহের পরিচিতি](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Microsoft Foundry পরিচিতি](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### রেফারেন্স

- [রেসপন্সিবল AI কী?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [আপনাকে আরও নিরাপদ এবং বিশ্বাসযোগ্য জেনারেটিভ AI অ্যাপ্লিকেশন তৈরি করতে সহায়তা করার জন্য Azure AI-তে নতুন টুল ঘোষণাঃ](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [জেনারেটিভ AI অ্যাপ্লিকেশনের মূল্যায়ন](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতা নিশ্চিতে চেষ্টা করি, তবুও স্বয়ংক্রিয় অনুবাদে ত্রুটি বা ভুল থাকতে পারে। মূল নথি তার নিজস্ব ভাষায় আনুষ্ঠানিক তথ্যসূত্র হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদের পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহারে সৃষ্ট যেকোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->