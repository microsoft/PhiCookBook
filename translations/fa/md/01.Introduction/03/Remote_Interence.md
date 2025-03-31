<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a54cd3d65b6963e4e8ce21e143c3ab04",
  "translation_date": "2025-03-27T08:03:26+00:00",
  "source_file": "md\\01.Introduction\\03\\Remote_Interence.md",
  "language_code": "fa"
}
-->
# استنتاج از راه دور با مدل تنظیم‌شده

پس از آموزش آداپتورها در محیط از راه دور، از یک برنامه ساده Gradio برای تعامل با مدل استفاده کنید.

![پایان تنظیم دقیق](../../../../../translated_images/log-finetuning-res.4b3ee593f24d3096742d09375adade22b217738cab93bc1139f224e5888a1cbf.fa.png)

### آماده‌سازی منابع Azure  
برای استنتاج از راه دور، باید منابع Azure را با اجرای `AI Toolkit: Provision Azure Container Apps for inference` از منوی فرمان تنظیم کنید. در طول این فرآیند، از شما خواسته می‌شود اشتراک Azure و گروه منابع خود را انتخاب کنید.  
![آماده‌سازی منابع استنتاج](../../../../../translated_images/command-provision-inference.b294f3ae5764ab45b83246d464ad5329b0de20cf380f75a699b4cc6b5495ca11.fa.png)

به‌طور پیش‌فرض، اشتراک و گروه منابع برای استنتاج باید با آن‌هایی که برای تنظیم دقیق استفاده شده‌اند یکسان باشند. استنتاج از همان محیط Azure Container App استفاده کرده و به مدل و آداپتور مدل ذخیره‌شده در Azure Files که در مرحله تنظیم دقیق تولید شده‌اند، دسترسی خواهد داشت.

## استفاده از AI Toolkit  

### استقرار برای استنتاج  
اگر می‌خواهید کد استنتاج را بازبینی کنید یا مدل استنتاج را مجدداً بارگذاری کنید، لطفاً فرمان `AI Toolkit: Deploy for inference` را اجرا کنید. این کار کد جدید شما را با ACA همگام‌سازی کرده و نسخه را مجدداً راه‌اندازی می‌کند.

![استقرار برای استنتاج](../../../../../translated_images/command-deploy.cb6508c973d6257e649aa4f262d3c170a374da3e9810a4f3d9e03935408a592b.fa.png)

پس از تکمیل موفقیت‌آمیز استقرار، مدل اکنون آماده ارزیابی با استفاده از این نقطه پایانی است.

### دسترسی به API استنتاج  

می‌توانید با کلیک بر روی دکمه "*Go to Inference Endpoint*" که در اعلان VSCode نمایش داده می‌شود، به API استنتاج دسترسی پیدا کنید. به‌طور جایگزین، نقطه پایانی وب API در `ACA_APP_ENDPOINT` در `./infra/inference.config.json` و در پنل خروجی قابل مشاهده است.

![نقطه پایانی برنامه](../../../../../translated_images/notification-deploy.00f4267b7aa6a18cfaaec83a7831b5d09311d5d96a70bb4c9d651ea4a41a8af7.fa.png)

> **توجه:** ممکن است چند دقیقه طول بکشد تا نقطه پایانی استنتاج کاملاً عملیاتی شود.

## اجزای استنتاج موجود در قالب  

| پوشه | محتویات |
| ------ |--------- |
| `infra` | شامل تمام تنظیمات لازم برای عملیات از راه دور. |
| `infra/provision/inference.parameters.json` | شامل پارامترها برای قالب‌های bicep، که برای آماده‌سازی منابع Azure برای استنتاج استفاده می‌شوند. |
| `infra/provision/inference.bicep` | شامل قالب‌هایی برای آماده‌سازی منابع Azure برای استنتاج. |
| `infra/inference.config.json` | فایل تنظیماتی که توسط فرمان `AI Toolkit: Provision Azure Container Apps for inference` تولید شده است. این فایل به‌عنوان ورودی برای سایر منوهای فرمان از راه دور استفاده می‌شود. |

### استفاده از AI Toolkit برای تنظیم آماده‌سازی منابع Azure  
[AI Toolkit](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio) را پیکربندی کنید.

Azure Container Apps را برای استنتاج آماده کنید ` command.

You can find configuration parameters in `./infra/provision/inference.parameters.json` file. Here are the details:
| Parameter | Description |
| --------- |------------ |
| `defaultCommands` | This is the commands to initiate a web API. |
| `maximumInstanceCount` | This parameter sets the maximum capacity of GPU instances. |
| `location` | This is the location where Azure resources are provisioned. The default value is the same as the chosen resource group's location. |
| `storageAccountName`, `fileShareName` `acaEnvironmentName`, `acaEnvironmentStorageName`, `acaAppName`,  `acaLogAnalyticsName` | These parameters are used to name the Azure resources for provision. By default, they will be same to the fine-tuning resource name. You can input a new, unused resource name to create your own custom-named resources, or you can input the name of an already existing Azure resource if you'd prefer to use that. For details, refer to the section [Using existing Azure Resources](../../../../../md/01.Introduction/03). |

### Using Existing Azure Resources

By default, the inference provision use the same Azure Container App Environment, Storage Account, Azure File Share, and Azure Log Analytics that were used for fine-tuning. A separate Azure Container App is created solely for the inference API. 

If you have customized the Azure resources during the fine-tuning step or want to use your own existing Azure resources for inference, specify their names in the `./infra/inference.parameters.json` فایل. سپس، فرمان `AI Toolkit: Provision Azure Container Apps for inference` را از منوی فرمان اجرا کنید. این کار منابع مشخص‌شده را به‌روزرسانی کرده و هر منبعی که وجود ندارد را ایجاد می‌کند.

برای مثال، اگر یک محیط کانتینر Azure موجود دارید، فایل `./infra/finetuning.parameters.json` شما باید به این شکل باشد:

```json
{
    "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentParameters.json#",
    "contentVersion": "1.0.0.0",
    "parameters": {
      ...
      "acaEnvironmentName": {
        "value": "<your-aca-env-name>"
      },
      "acaEnvironmentStorageName": {
        "value": null
      },
      ...
    }
  }
```

### آماده‌سازی دستی  
اگر ترجیح می‌دهید منابع Azure را به‌صورت دستی تنظیم کنید، می‌توانید از فایل‌های bicep ارائه‌شده در فایل `./infra/provision` folders. If you have already set up and configured all the Azure resources without using the AI Toolkit command palette, you can simply enter the resource names in the `inference.config.json` استفاده کنید.

برای مثال:

```json
{
  "SUBSCRIPTION_ID": "<your-subscription-id>",
  "RESOURCE_GROUP_NAME": "<your-resource-group-name>",
  "STORAGE_ACCOUNT_NAME": "<your-storage-account-name>",
  "FILE_SHARE_NAME": "<your-file-share-name>",
  "ACA_APP_NAME": "<your-aca-name>",
  "ACA_APP_ENDPOINT": "<your-aca-endpoint>"
}
```

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما تلاش می‌کنیم دقت را رعایت کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی اشتباهات یا نادقتی‌هایی باشند. سند اصلی به زبان بومی خود باید به‌عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حساس، توصیه می‌شود از ترجمه حرفه‌ای انسانی استفاده کنید. ما مسئول هیچ‌گونه سوءتفاهم یا تفسیر نادرست ناشی از استفاده از این ترجمه نیستیم.