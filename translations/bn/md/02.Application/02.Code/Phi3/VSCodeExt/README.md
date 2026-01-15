<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "00b7a699de8ac405fa821f4c0f7fc0ab",
  "translation_date": "2025-07-17T03:36:26+00:00",
  "source_file": "md/02.Application/02.Code/Phi3/VSCodeExt/README.md",
  "language_code": "bn"
}
-->
# **Microsoft Phi-3 পরিবারসহ আপনার নিজস্ব Visual Studio Code GitHub Copilot Chat তৈরি করুন**

আপনি কি GitHub Copilot Chat-এ workspace agent ব্যবহার করেছেন? আপনি কি আপনার দলের নিজস্ব কোড এজেন্ট তৈরি করতে চান? এই হ্যান্ডস-অন ল্যাবটি ওপেন সোর্স মডেলকে একত্রিত করে একটি এন্টারপ্রাইজ-স্তরের কোড ব্যবসায়িক এজেন্ট তৈরি করার চেষ্টা করে।

## **ভিত্তি**

### **কেন Microsoft Phi-3 নির্বাচন করবেন**

Phi-3 একটি পরিবার সিরিজ, যার মধ্যে রয়েছে phi-3-mini, phi-3-small, এবং phi-3-medium, যা বিভিন্ন প্রশিক্ষণ প্যারামিটার ভিত্তিক টেক্সট জেনারেশন, ডায়ালগ সম্পূর্ণকরণ, এবং কোড জেনারেশনের জন্য। এছাড়াও Vision ভিত্তিক phi-3-vision রয়েছে। এটি এন্টারপ্রাইজ বা বিভিন্ন দলের জন্য অফলাইন জেনারেটিভ AI সমাধান তৈরি করার জন্য উপযুক্ত।

এই লিঙ্কটি পড়ার পরামর্শ দেওয়া হচ্ছে [https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md](https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md)

### **Microsoft GitHub Copilot Chat**

GitHub Copilot Chat এক্সটেনশন আপনাকে একটি চ্যাট ইন্টারফেস দেয় যা GitHub Copilot-এর সাথে ইন্টারঅ্যাক্ট করতে এবং VS Code-এর মধ্যে সরাসরি কোডিং-সম্পর্কিত প্রশ্নের উত্তর পেতে সাহায্য করে, যাতে আপনাকে ডকুমেন্টেশন ব্রাউজ বা অনলাইন ফোরাম সার্চ করতে হয় না।

Copilot Chat সৃষ্ট উত্তরকে স্পষ্ট করতে সিনট্যাক্স হাইলাইটিং, ইন্ডেন্টেশন এবং অন্যান্য ফরম্যাটিং বৈশিষ্ট্য ব্যবহার করতে পারে। ব্যবহারকারীর প্রশ্নের ধরন অনুযায়ী, ফলাফলটিতে এমন লিঙ্ক থাকতে পারে যা Copilot উত্তর তৈরির জন্য ব্যবহার করেছে, যেমন সোর্স কোড ফাইল বা ডকুমেন্টেশন, অথবা VS Code ফাংশনালিটি অ্যাক্সেস করার জন্য বাটন।

- Copilot Chat আপনার ডেভেলপার ফ্লোতে একীভূত হয় এবং যেখানে প্রয়োজন সেখানে সাহায্য দেয়:

- কোডিং করার সময় সাহায্যের জন্য সরাসরি এডিটর বা টার্মিনাল থেকে ইনলাইন চ্যাট শুরু করুন

- যেকোনো সময় পাশে AI সহকারী পেতে Chat ভিউ ব্যবহার করুন

- দ্রুত প্রশ্ন করার জন্য Quick Chat চালু করুন এবং আপনার কাজের মধ্যে ফিরে যান

GitHub Copilot Chat বিভিন্ন পরিস্থিতিতে ব্যবহার করা যেতে পারে, যেমন:

- সমস্যার সর্বোত্তম সমাধান সম্পর্কে কোডিং প্রশ্নের উত্তর দেওয়া

- অন্য কারো কোড ব্যাখ্যা করা এবং উন্নতির পরামর্শ দেওয়া

- কোড ফিক্স প্রস্তাব করা

- ইউনিট টেস্ট কেস তৈরি করা

- কোড ডকুমেন্টেশন তৈরি করা

এই লিঙ্কটি পড়ার পরামর্শ দেওয়া হচ্ছে [https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/copilot-chat?WT.mc_id=aiml-137032-kinfeylo)

### **Microsoft GitHub Copilot Chat @workspace**

Copilot Chat-এ **@workspace** উল্লেখ করলে আপনি আপনার সম্পূর্ণ কোডবেস সম্পর্কে প্রশ্ন করতে পারেন। প্রশ্নের ভিত্তিতে, Copilot বুদ্ধিমত্তার সাথে প্রাসঙ্গিক ফাইল এবং সিম্বলগুলি উদ্ধার করে, যা পরে তার উত্তরে লিঙ্ক এবং কোড উদাহরণ হিসেবে উল্লেখ করে।

আপনার প্রশ্নের উত্তর দিতে, **@workspace** VS Code-এ কোডবেস নেভিগেট করার সময় ডেভেলপার যে উৎসগুলি ব্যবহার করে সেগুলোর মধ্য দিয়ে অনুসন্ধান করে:

- .gitignore ফাইলে উপেক্ষিত ফাইলগুলি বাদে ওয়ার্কস্পেসের সব ফাইল

- নেস্টেড ফোল্ডার এবং ফাইল নামসহ ডিরেক্টরি স্ট্রাকচার

- যদি ওয়ার্কস্পেস একটি GitHub রিপোজিটরি হয় এবং কোড সার্চ দ্বারা ইনডেক্স করা থাকে, তাহলে GitHub-এর কোড সার্চ ইনডেক্স

- ওয়ার্কস্পেসের সিম্বল এবং ডেফিনিশন

- বর্তমানে নির্বাচিত টেক্সট বা সক্রিয় এডিটরে দৃশ্যমান টেক্সট

দ্রষ্টব্য: যদি আপনি উপেক্ষিত ফাইলের মধ্যে একটি ফাইল খুলে রাখেন বা টেক্সট নির্বাচন করেন, তাহলে .gitignore উপেক্ষা করা হয়।

এই লিঙ্কটি পড়ার পরামর্শ দেওয়া হচ্ছে [[https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/workspace-context?WT.mc_id=aiml-137032-kinfeylo)]

## **এই ল্যাব সম্পর্কে আরও জানুন**

GitHub Copilot এন্টারপ্রাইজগুলোর প্রোগ্রামিং দক্ষতা অনেক উন্নত করেছে, এবং প্রতিটি এন্টারপ্রাইজ GitHub Copilot-এর প্রাসঙ্গিক ফাংশন কাস্টমাইজ করতে চায়। অনেক এন্টারপ্রাইজ তাদের নিজস্ব ব্যবসায়িক পরিস্থিতি এবং ওপেন সোর্স মডেল ভিত্তিক GitHub Copilot-এর মতো কাস্টমাইজড এক্সটেনশন তৈরি করেছে। এন্টারপ্রাইজের জন্য কাস্টমাইজড এক্সটেনশন নিয়ন্ত্রণ করা সহজ, তবে এটি ব্যবহারকারীর অভিজ্ঞতাকেও প্রভাবিত করে। যেহেতু GitHub Copilot সাধারণ পরিস্থিতি এবং পেশাদারিত্বে শক্তিশালী ফাংশনালিটি প্রদান করে, অভিজ্ঞতা যদি সঙ্গতিপূর্ণ রাখা যায় তবে এন্টারপ্রাইজের নিজস্ব এক্সটেনশন কাস্টমাইজ করা ভালো। GitHub Copilot Chat এন্টারপ্রাইজগুলোর জন্য চ্যাট অভিজ্ঞতা সম্প্রসারণের জন্য প্রাসঙ্গিক API প্রদান করে। সঙ্গতিপূর্ণ অভিজ্ঞতা বজায় রাখা এবং কাস্টমাইজড ফাংশন থাকা একটি উন্নত ব্যবহারকারীর অভিজ্ঞতা।

এই ল্যাবটি মূলত Phi-3 মডেলকে স্থানীয় NPU এবং Azure হাইব্রিডের সাথে মিলিয়ে GitHub Copilot Chat-এ একটি কাস্টম এজেন্ট ***@PHI3*** তৈরি করে, যা এন্টারপ্রাইজ ডেভেলপারদের কোড জেনারেশন সম্পন্ন করতে ***(@PHI3 /gen)*** এবং ছবি ভিত্তিক কোড জেনারেট করতে ***(@PHI3 /img)*** সহায়তা করে।

![PHI3](../../../../../../../translated_images/bn/cover.1017ebc9a7c46d09.webp)

### ***দ্রষ্টব্য:***

এই ল্যাবটি বর্তমানে Intel CPU এবং Apple Silicon-এর AIPC-তে বাস্তবায়িত হয়েছে। আমরা Qualcomm সংস্করণের NPU আপডেট চালিয়ে যাব।

## **ল্যাব**

| নাম | বর্ণনা | AIPC | Apple |
| ------------ | ----------- | -------- |-------- |
| Lab0 - ইনস্টলেশন(✅) | সংশ্লিষ্ট পরিবেশ এবং ইনস্টলেশন টুল কনফিগার ও ইনস্টল করুন | [Go](./HOL/AIPC/01.Installations.md) |[Go](./HOL/Apple/01.Installations.md) |
| Lab1 - Phi-3-mini দিয়ে Prompt flow চালানো (✅) | AIPC / Apple Silicon-এর সাথে মিলিয়ে স্থানীয় NPU ব্যবহার করে Phi-3-mini মাধ্যমে কোড জেনারেশন তৈরি | [Go](./HOL/AIPC/02.PromptflowWithNPU.md) |  [Go](./HOL/Apple/02.PromptflowWithMLX.md) |
| Lab2 - Azure Machine Learning Service-এ Phi-3-vision ডিপ্লয় করা(✅) | Azure Machine Learning Service-এর Model Catalog - Phi-3-vision ইমেজ ডিপ্লয় করে কোড জেনারেট করা | [Go](./HOL/AIPC/03.DeployPhi3VisionOnAzure.md) |[Go](./HOL/Apple/03.DeployPhi3VisionOnAzure.md) |
| Lab3 - GitHub Copilot Chat-এ @phi-3 এজেন্ট তৈরি করা(✅)  | GitHub Copilot Chat-এ একটি কাস্টম Phi-3 এজেন্ট তৈরি করে কোড জেনারেশন, গ্রাফ জেনারেশন কোড, RAG ইত্যাদি সম্পন্ন করা | [Go](./HOL/AIPC/04.CreatePhi3AgentInVSCode.md) | [Go](./HOL/Apple/04.CreatePhi3AgentInVSCode.md) |
| Sample Code (✅)  | স্যাম্পল কোড ডাউনলোড করুন | [Go](../../../../../../../code/07.Lab/01/AIPC) | [Go](../../../../../../../code/07.Lab/01/Apple) |

## **রিসোর্স**

1. Phi-3 Cookbook [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook)

2. GitHub Copilot সম্পর্কে আরও জানুন [https://learn.microsoft.com/training/paths/copilot/](https://learn.microsoft.com/training/paths/copilot/?WT.mc_id=aiml-137032-kinfeylo)

3. GitHub Copilot Chat সম্পর্কে আরও জানুন [https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/](https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/?WT.mc_id=aiml-137032-kinfeylo)

4. GitHub Copilot Chat API সম্পর্কে আরও জানুন [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat?WT.mc_id=aiml-137032-kinfeylo)

5. Azure AI Foundry সম্পর্কে আরও জানুন [https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/](https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/?WT.mc_id=aiml-137032-kinfeylo)

6. Azure AI Foundry-এর Model Catalog সম্পর্কে আরও জানুন [https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview)

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার নিজস্ব ভাষায়ই কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ গ্রহণ করার পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহারে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।