# **আপনার নিজের Visual Studio Code GitHub Copilot Chat Microsoft Phi-3 পরিবার সহ তৈরি করুন**

আপনি কি GitHub Copilot Chat-এ ওয়ার্কস্পেস এজেন্ট ব্যবহার করেছেন? আপনি কি আপনার দলের নিজস্ব কোড এজেন্ট তৈরি করতে চান? এই হাতে-কলমে ল্যাবটি খোলা সোর্স মডেলের সাথে মিলিয়ে একটি এন্টারপ্রাইজ-স্তরের কোড ব্যবসায়িক এজেন্ট তৈরি করার আশা রাখে।

## **মূল ভিত্তি**

### **কেন Microsoft Phi-3 বেছে নেওয়া হয়েছে**

Phi-3 একটি পরিবার সিরিজ, যার মধ্যে রয়েছে phi-3-mini, phi-3-small, এবং phi-3-medium যা টেক্সট উৎপাদন, সংলাপ সম্পূর্ণকরণ এবং কোড উৎপাদনের জন্য বিভিন্ন প্রশিক্ষণ প্যারামিটার ভিত্তিক। এছাড়াও রয়েছে Vision ভিত্তিক phi-3-vision। এটি এন্টারপ্রাইজ বা বিভিন্ন দলের জন্য অফলাইন জেনারেটিভ AI সমাধান তৈরি করতে উপযুক্ত।

এই লিঙ্কটি পড়ার পরামর্শ দেওয়া হয়েছে [https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md](https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md)

### **Microsoft GitHub Copilot Chat**

GitHub Copilot Chat এক্সটেনশন আপনাকে একটি চ্যাট ইন্টারফেস দেয় যা GitHub Copilot-এর সাথে ইন্টারঅ্যাক্ট করতে এবং কোডিং-সম্পর্কিত প্রশ্নগুলির উত্তর সরাসরি VS Code-এর মধ্যে পেতে দেয়, যা আপনাকে ডকুমেন্টেশন অনুসন্ধান বা অনলাইন ফোরাম ব্রাউজ করার প্রয়োজন নেই।

Copilot Chat জেনারেট করা উত্তরের স্পষ্টতা বাড়ানোর জন্য সাইট্যাক্স হাইলাইটিং, ইন্ডেন্টেশন এবং অন্যান্য ফরম্যাটিং ফিচার ব্যবহার করতে পারে। ব্যবহারকারীর প্রশ্নের ধরনের উপর নির্ভর করে, ফলাফলে এমন লিঙ্ক থাকতে পারে যা Copilot উত্তর তৈরির জন্য ব্যবহার করেছে, যেমন সোর্স কোড ফাইল বা ডকুমেন্টেশন, অথবা VS Code এর ফাংশনালিটি অ্যাক্সেস করার জন্য বাটন।

- Copilot Chat আপনার ডেভেলপার ফ্লোতে ইন্টিগ্রেট করে এবং যেখানে চাই সেখানে সাহায্য করে:

- এডিটর বা টার্মিনাল থেকে সরাসরি ইনলাইন চ্যাট শুরু করুন যখন আপনি কোডিং করছেন সাহায্যের জন্য

- Chat ভিউ ব্যবহার করে পাশে একটি AI সহকারী রাখুন যেকোনো সময় সাহায্যের জন্য

- Quick Chat চালু করুন দ্রুত প্রশ্ন জিজ্ঞাসা করার জন্য এবং আবার আপনার কাজ ফিরে যাওয়ার জন্য

আপনি GitHub Copilot Chat বিভিন্ন ক্ষেত্রে ব্যবহার করতে পারেন, যেমন:

- সমস্যার সেরা সমাধানে কোডিং প্রশ্নগুলোর উত্তর দেয়া

- কারো অন্যের কোড ব্যাখ্যা করা এবং উন্নতি প্রস্তাব করা

- কোড ফিক্স প্রস্তাব করা

- ইউনিট টেস্ট কেস তৈরি করা

- কোড ডকুমেন্টেশন তৈরি করা

এই লিঙ্কটি পড়ার পরামর্শ দেওয়া হয়েছে [https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/copilot-chat?WT.mc_id=aiml-137032-kinfeylo)


###  **Microsoft GitHub Copilot Chat @workspace**

Copilot Chat-এ **@workspace** উল্লেখ করলে আপনি আপনার সম্পূর্ণ কোডবেস সম্পর্কে প্রশ্ন করতে পারেন। প্রশ্নের ভিত্তিতে, Copilot বুদ্ধিমত্তার সঙ্গে প্রাসঙ্গিক ফাইল ও সিম্বলগুলি পুনরুদ্ধার করে, যেগুলো পরে উত্তর দেওয়ার সময় লিঙ্ক এবং কোড উদাহরণের মাধ্যমে রেফারেন্স করা হয়।

আপনার প্রশ্নের উত্তর দেওয়ার জন্য, **@workspace** একই উত্সগুলি অনুসন্ধান করে যেগুলো একজন ডেভেলপার VS Code-এ কোডবেস নেভিগেট করার সময় ব্যবহার করে:

- ওয়ার্কস্পেসের সমস্ত ফাইল, .gitignore ফাইলে উপেক্ষিত ফাইলগুলি ছাড়া

- ডিরেক্টরি গঠন সহ nested ফোল্ডার এবং ফাইলের নাম

- GitHub-এর কোড সার্চ ইনডেক্স, যদি ওয়ার্কস্পেস একটি GitHub রিপোজিটরি হয় এবং কোড সার্চ দ্বারা ইনডেক্স করা হয়

- ওয়ার্কস্পেসের সিম্বল এবং ডেফিনিশন

- বর্তমানে নির্বাচিত টেক্সট বা সক্রিয় এডিটরের দৃশ্যমান টেক্সট

বিঃদ্রঃ .gitignore ওভাররাইট হয় যদি আপনি কোনো উপেক্ষিত ফাইলে টেক্সট নির্বাচন করেন বা ফাইলটি ওপেন করেন।

এই লিঙ্কটি পড়ার পরামর্শ দেওয়া হয়েছে [[https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/workspace-context?WT.mc_id=aiml-137032-kinfeylo)]


## **এই ল্যাব সম্পর্কে আরও জানুন**

GitHub Copilot এন্টারপ্রাইজের প্রোগ্রামিং দক্ষতা ব্যাপকভাবে উন্নত করেছে, এবং প্রতিটি এন্টারপ্রাইজ GitHub Copilot-এর প্রাসঙ্গিক ফাংশনগুলি কাস্টমাইজ করতে চায়। অনেক এন্টারপ্রাইজ তাদের নিজস্ব ব্যবসায়িক পরিস্থিতি এবং খোলা সোর্স মডেলের ভিত্তিতে GitHub Copilot-এর অনুরূপ কাস্টম এক্সটেনশন তৈরি করেছে। এন্টারপ্রাইজগুলির জন্য কাস্টমাইজড এক্সটেন্টশন নিয়ন্ত্রণ করা সহজ, তবে এটি ব্যবহারকারীর অভিজ্ঞতাকেও প্রভাবিত করে। শেষ পর্যন্ত, GitHub Copilot সাধারণ পরিস্থিতি এবং পেশাদারিত্ব মোকাবেলায় বেশি কার্যক্ষম। যদি অভিজ্ঞতা ক্রমাগত রাখা যায়, তবে এন্টারপ্রাইজ নিজস্ব কাস্টমাইজড এক্সটেনশন তৈরি করা ভালো হবে। GitHub Copilot Chat এন্টারপ্রাইজদের চ্যাট অভিজ্ঞতায় সম্প্রসারণের জন্য প্রাসঙ্গিক API প্রদান করে। অভিজ্ঞতা রক্ষা ও কাস্টম ফাংশন থাকা একটি উন্নত ব্যবহারকারীর অভিজ্ঞতা।

এই ল্যাবটি মূলত Phi-3 মডেলকে স্থানীয় NPU এবং Azure হাইব্রিডের সাথে সংযুক্ত করে GitHub Copilot Chat-এ একটি কাস্টম এজেন্ট ***@PHI3*** তৈরি করে এন্টারপ্রাইজ ডেভেলপারদের সাহায্য করে কোড জেনারেশন সম্পন্ন করা***(@PHI3 /gen)*** এবং ছবির ভিত্তিতে কোড জেনারেশন করা ***(@PHI3 /img)***।

![PHI3](../../../../../../../translated_images/bn/cover.1017ebc9a7c46d09.webp)

### ***মন্তব্য:***

এই ল্যাবটি বর্তমানে Intel CPU এবং Apple Silicon এর AIPC-তে বাস্তবায়িত হয়েছে। আমরা Qualcomm সংস্করণের NPU আপডেট চালিয়ে যাব।

## **ল্যাব**


| নাম | বর্ণনা | AIPC | Apple |
| ------------ | ----------- | -------- |-------- |
| Lab0 - ইনস্টলেশন(✅) | সম্পর্কিত পরিবেশ এবং ইনস্টলেশন সরঞ্জাম কনফিগার এবং ইনস্টল করা | [যান](./HOL/AIPC/01.Installations.md) |[যান](./HOL/Apple/01.Installations.md) |
| Lab1 - Phi-3-mini সহ Prompt flow চালানো (✅) | AIPC / Apple Silicon সঙ্গে সংযুক্ত, স্থানীয় NPU ব্যবহার করে Phi-3-mini দিয়ে কোড জেনারেশন তৈরি করা | [যান](./HOL/AIPC/02.PromptflowWithNPU.md) |  [যান](./HOL/Apple/02.PromptflowWithMLX.md) |
| Lab2 - Azure Machine Learning Service-এ Phi-3-vision মোতায়েন(✅) | Azure Machine Learning Service-এর Model Catalog - Phi-3-vision ইমেজ মোতায়েন করে কোড জেনারেট করা | [যান](./HOL/AIPC/03.DeployPhi3VisionOnAzure.md) |[যান](./HOL/Apple/03.DeployPhi3VisionOnAzure.md) |
| Lab3 - GitHub Copilot Chat-এ @phi-3 এজেন্ট তৈরি করা(✅)  | GitHub Copilot Chat-এ একটি কাস্টম Phi-3 এজেন্ট তৈরি করে কোড জেনারেশন, গ্রাফ জেনারেশন কোড, RAG ইত্যাদি সম্পন্ন করা | [যান](./HOL/AIPC/04.CreatePhi3AgentInVSCode.md) | [যান](./HOL/Apple/04.CreatePhi3AgentInVSCode.md) |
| নমুনা কোড (✅)  | নমুনা কোড ডাউনলোড করুন | [যান](../../../../../../../code/07.Lab/01/AIPC) | [যান](../../../../../../../code/07.Lab/01/Apple) |


## **সাহায্য সমৃদ্ধ সম্পদ**

1. Phi-3 কুকবুক [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook)

2. GitHub Copilot সম্পর্কে আরও জানুন [https://learn.microsoft.com/training/paths/copilot/](https://learn.microsoft.com/training/paths/copilot/?WT.mc_id=aiml-137032-kinfeylo)

3. GitHub Copilot Chat সম্পর্কে আরও জানুন [https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/](https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/?WT.mc_id=aiml-137032-kinfeylo)

4. GitHub Copilot Chat API সম্পর্কে আরও জানুন [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat?WT.mc_id=aiml-137032-kinfeylo)

5. Microsoft Foundry সম্পর্কে আরও জানুন [https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/](https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/?WT.mc_id=aiml-137032-kinfeylo)

6. Microsoft Foundry এর Model Catalog সম্পর্কে আরও জানুন [https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকারোক্তি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। আমরা সঠিকতার জন্য চেষ্টা করি, কিন্তু অনুগ্রহ করে জানুন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসত্যতা থাকতে পারে। মূল নথিটি এর নিজস্ব ভাষায় কর্তৃত্বপূর্ণ সূত্র হিসাবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ পরামর্শ দেওয়া হয়। এই অনুবাদ ব্যবহারের কারণে হওয়া কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়বদ্ধ নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->