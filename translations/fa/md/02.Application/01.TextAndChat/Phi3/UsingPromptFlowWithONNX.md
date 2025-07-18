<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "92e7dac1e5af0dd7c94170fdaf6860fe",
  "translation_date": "2025-07-17T02:57:18+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md",
  "language_code": "fa"
}
-->
# استفاده از GPU ویندوز برای ایجاد راهکار Prompt flow با Phi-3.5-Instruct ONNX

سند زیر نمونه‌ای است از نحوه استفاده از PromptFlow با ONNX (Open Neural Network Exchange) برای توسعه برنامه‌های هوش مصنوعی مبتنی بر مدل‌های Phi-3.

PromptFlow مجموعه‌ای از ابزارهای توسعه است که برای ساده‌سازی چرخه کامل توسعه برنامه‌های هوش مصنوعی مبتنی بر مدل‌های زبان بزرگ (LLM) طراحی شده است، از ایده‌پردازی و نمونه‌سازی اولیه گرفته تا تست و ارزیابی.

با ادغام PromptFlow با ONNX، توسعه‌دهندگان می‌توانند:

- بهینه‌سازی عملکرد مدل: استفاده از ONNX برای استنتاج و استقرار کارآمد مدل.
- ساده‌سازی توسعه: استفاده از PromptFlow برای مدیریت جریان کاری و خودکارسازی وظایف تکراری.
- افزایش همکاری: تسهیل همکاری بهتر بین اعضای تیم با فراهم کردن محیط توسعه یکپارچه.

**Prompt flow** مجموعه‌ای از ابزارهای توسعه است که برای ساده‌سازی چرخه کامل توسعه برنامه‌های هوش مصنوعی مبتنی بر LLM طراحی شده است، از ایده‌پردازی، نمونه‌سازی اولیه، تست، ارزیابی تا استقرار در تولید و نظارت. این ابزار مهندسی پرامپت را بسیار آسان‌تر می‌کند و به شما امکان می‌دهد برنامه‌های LLM با کیفیت تولید بسازید.

Prompt flow می‌تواند به OpenAI، Azure OpenAI Service و مدل‌های قابل سفارشی‌سازی (Huggingface، LLM/SLM محلی) متصل شود. ما امیدواریم مدل ONNX کوانتیزه شده Phi-3.5 را در برنامه‌های محلی مستقر کنیم. Prompt flow می‌تواند به ما کمک کند کسب‌وکار خود را بهتر برنامه‌ریزی کنیم و راهکارهای محلی مبتنی بر Phi-3.5 را کامل کنیم. در این مثال، ما کتابخانه ONNX Runtime GenAI را برای تکمیل راهکار Prompt flow مبتنی بر GPU ویندوز ترکیب خواهیم کرد.

## **نصب**

### **ONNX Runtime GenAI برای GPU ویندوز**

برای تنظیم ONNX Runtime GenAI برای GPU ویندوز این راهنما را مطالعه کنید [کلیک کنید](./ORTWindowGPUGuideline.md)

### **راه‌اندازی Prompt flow در VSCode**

1. افزونه Prompt flow برای VS Code را نصب کنید

![pfvscode](../../../../../../translated_images/pfvscode.eff93dfc66a42cbef699fc16fa48f3ed3a23361875a3362037d026896395a00d.fa.png)

2. پس از نصب افزونه Prompt flow در VS Code، روی افزونه کلیک کنید و گزینه **Installation dependencies** را انتخاب کنید و طبق این راهنما SDK پرامپت فلو را در محیط خود نصب کنید

![pfsetup](../../../../../../translated_images/pfsetup.b46e93096f5a254f74e8b74ce2be7047ce963ef573d755ec897eb1b78cb9c954.fa.png)

3. [نمونه کد](../../../../../../code/09.UpdateSamples/Aug/pf/onnx_inference_pf) را دانلود کرده و با VS Code این نمونه را باز کنید

![pfsample](../../../../../../translated_images/pfsample.8d89e70584ffe7c4dba182513e3148a989e552c3b8e4948567a6b806b5ae1845.fa.png)

4. فایل **flow.dag.yaml** را باز کنید و محیط پایتون خود را انتخاب کنید

![pfdag](../../../../../../translated_images/pfdag.264a77f7366458ff850a76ae949226391ea382856d543ef9da4b92096aff7e4b.fa.png)

   فایل **chat_phi3_ort.py** را باز کنید و مسیر مدل Phi-3.5-instruct ONNX خود را تغییر دهید

![pfphi](../../../../../../translated_images/pfphi.72da81d74244b45fc78cdfeeb8c7fbd9e7cd610bf2f96814dbade6a4a2dfad7e.fa.png)

5. پرامپت فلو خود را برای تست اجرا کنید

فایل **flow.dag.yaml** را باز کنید و روی ویرایشگر بصری کلیک کنید

![pfv](../../../../../../translated_images/pfv.ba8a81f34b20f603cccee3fe91e94113792ed6f5af28f76ab08e1a0b3e77b33b.fa.png)

پس از کلیک، آن را اجرا کنید تا تست شود

![pfflow](../../../../../../translated_images/pfflow.4e1135a089b1ce1b6348b59edefdb6333e5729b54c8e57f9039b7f9463e68fbd.fa.png)

1. می‌توانید در ترمینال به صورت دسته‌ای اجرا کنید تا نتایج بیشتری ببینید


```bash

pf run create --file batch_run.yaml --stream --name 'Your eval qa name'    

```

می‌توانید نتایج را در مرورگر پیش‌فرض خود مشاهده کنید


![pfresult](../../../../../../translated_images/pfresult.c22c826f8062d7cbe871cff35db4a013dcfefc13fafe5da6710a8549a96a4ceb.fa.png)

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان بومی خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئول هیچ گونه سوءتفاهم یا تفسیر نادرستی که از استفاده این ترجمه ناشی شود، نیستیم.