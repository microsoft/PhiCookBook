<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "57f14126c1c6add76b3aef3844dfe4e3",
  "translation_date": "2025-05-09T04:17:28+00:00",
  "source_file": "SECURITY.md",
  "language_code": "bn"
}
-->
## Security

Microsoft আমাদের সফটওয়্যার পণ্য এবং পরিষেবাগুলির নিরাপত্তাকে গুরুত্ব দেয়, যার মধ্যে রয়েছে আমাদের GitHub সংগঠনগুলির মাধ্যমে পরিচালিত সমস্ত সোর্স কোড রিপোজিটরি, যেমন [Microsoft](https://github.com/Microsoft), [Azure](https://github.com/Azure), [DotNet](https://github.com/dotnet), [AspNet](https://github.com/aspnet) এবং [Xamarin](https://github.com/xamarin)।

যদি আপনি মনে করেন যে আপনি Microsoft-এর মালিকানাধীন কোনও রিপোজিটরিতে একটি নিরাপত্তা দুর্বলতা পেয়েছেন যা [Microsoft-এর নিরাপত্তা দুর্বলতার সংজ্ঞা](https://aka.ms/security.md/definition) পূরণ করে, তাহলে নিচে বর্ণিত অনুযায়ী আমাদের জানান।

## Reporting Security Issues

**অনুগ্রহ করে নিরাপত্তা দুর্বলতাগুলি পাবলিক GitHub ইস্যুর মাধ্যমে রিপোর্ট করবেন না।**

এর পরিবর্তে, দয়া করে Microsoft Security Response Center (MSRC)-এ রিপোর্ট করুন [https://msrc.microsoft.com/create-report](https://aka.ms/security.md/msrc/create-report) এ।

আপনি যদি লগইন না করেই সাবমিট করতে চান, তাহলে ইমেইল পাঠান [secure@microsoft.com](mailto:secure@microsoft.com)। সম্ভব হলে, আমাদের PGP কী দিয়ে আপনার বার্তাটি এনক্রিপ্ট করুন; দয়া করে এটি [Microsoft Security Response Center PGP Key পেজ](https://aka.ms/security.md/msrc/pgp) থেকে ডাউনলোড করুন।

আপনি ২৪ ঘণ্টার মধ্যে একটি প্রতিক্রিয়া পাবেন। যদি কোনও কারণে না পান, তাহলে ইমেইলের মাধ্যমে ফলোআপ করুন যাতে আমরা আপনার মূল বার্তাটি পেয়েছি কিনা নিশ্চিত হতে পারি। অতিরিক্ত তথ্য পাওয়া যাবে [microsoft.com/msrc](https://www.microsoft.com/msrc) এ।

অনুগ্রহ করে নিচের তথ্যগুলি (যতটা সম্ভব) অন্তর্ভুক্ত করুন যাতে আমরা সমস্যার প্রকৃতি এবং পরিধি ভালভাবে বুঝতে পারি:

  * সমস্যার ধরন (যেমন buffer overflow, SQL injection, cross-site scripting, ইত্যাদি)
  * সমস্যা সম্পর্কিত সোর্স ফাইলের সম্পূর্ণ পথ
  * প্রভাবিত সোর্স কোডের অবস্থান (tag/branch/commit বা সরাসরি URL)
  * সমস্যা পুনরুত্পাদনের জন্য বিশেষ কোন কনফিগারেশন প্রয়োজন কিনা
  * সমস্যা পুনরুত্পাদনের ধাপে ধাপে নির্দেশনা
  * প্রুফ-অফ-কনসেপ্ট বা exploit কোড (যদি সম্ভব হয়)
  * সমস্যার প্রভাব, এবং কিভাবে একজন আক্রমণকারী এটি কাজে লাগাতে পারে

এই তথ্য আমাদের রিপোর্টটি দ্রুত প্রক্রিয়াজাত করতে সাহায্য করবে।

আপনি যদি বাগ বাউন্টির জন্য রিপোর্ট করছেন, তাহলে আরও সম্পূর্ণ রিপোর্ট উচ্চতর বাউন্টি পুরস্কারের সম্ভাবনা বাড়ায়। আমাদের [Microsoft Bug Bounty Program](https://aka.ms/security.md/msrc/bounty) পেজে আমাদের সক্রিয় প্রোগ্রামগুলোর বিস্তারিত তথ্য পাবেন।

## Preferred Languages

আমরা সকল যোগাযোগ ইংরেজিতে হওয়াকে পছন্দ করি।

## Policy

Microsoft অনুসরণ করে [Coordinated Vulnerability Disclosure](https://aka.ms/security.md/cvd) নীতি।

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে স্বয়ংক্রিয় অনুবাদে ভুল বা অসঙ্গতি থাকতে পারে তা অনুগ্রহ করে বুঝে নিন। মূল নথিটি তার নিজস্ব ভাষায়ই প্রামাণিক উৎস হিসেবে বিবেচিত হবে। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদের পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহারে কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।