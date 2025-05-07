<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a1c62bf7d86d6186bf8d3917196a92a0",
  "translation_date": "2025-05-07T13:37:54+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Kaito.md",
  "language_code": "fa"
}
-->
## تنظیم دقیق با Kaito

[Kaito](https://github.com/Azure/kaito) یک اپراتور است که استقرار مدل‌های استنتاج AI/ML را در یک خوشه Kubernetes به‌صورت خودکار انجام می‌دهد.

Kaito در مقایسه با بیشتر روش‌های متداول استقرار مدل که روی زیرساخت‌های ماشین مجازی ساخته شده‌اند، تفاوت‌های کلیدی زیر را دارد:

- مدیریت فایل‌های مدل با استفاده از ایمیج‌های کانتینری. یک سرور http فراهم شده تا فراخوانی‌های استنتاج با استفاده از کتابخانه مدل انجام شود.
- جلوگیری از تنظیم دستی پارامترهای استقرار برای تطبیق با سخت‌افزار GPU با ارائه تنظیمات پیش‌فرض.
- تخصیص خودکار گره‌های GPU بر اساس نیازهای مدل.
- میزبانی ایمیج‌های بزرگ مدل در Microsoft Container Registry (MCR) عمومی در صورت اجازه داشتن مجوز.

با استفاده از Kaito، روند وارد کردن مدل‌های بزرگ استنتاج AI در Kubernetes تا حد زیادی ساده شده است.

## معماری

Kaito از الگوی طراحی کلاسیک Kubernetes Custom Resource Definition (CRD)/controller پیروی می‌کند. کاربر یک منبع سفارشی `workspace` را مدیریت می‌کند که نیازهای GPU و مشخصات استنتاج را توصیف می‌کند. کنترلرهای Kaito با تطبیق منبع سفارشی `workspace` به صورت خودکار استقرار را انجام می‌دهند.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="معماری Kaito" alt="معماری Kaito">
</div>

شکل بالا نمای کلی معماری Kaito را نشان می‌دهد. اجزای اصلی آن شامل موارد زیر است:

- **کنترلر Workspace**: این کنترلر منبع سفارشی `workspace` را تطبیق می‌دهد، منابع سفارشی `machine` (که در ادامه توضیح داده می‌شود) را برای فعال‌سازی تخصیص خودکار گره ایجاد می‌کند و بار کاری استنتاج (`deployment` یا `statefulset`) را بر اساس تنظیمات پیش‌فرض مدل ایجاد می‌کند.
- **کنترلر Node provisioner**: نام این کنترلر *gpu-provisioner* است که در [نقشه helm gpu-provisioner](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) یافت می‌شود. این کنترلر از CRD `machine` که از [Karpenter](https://sigs.k8s.io/karpenter) منشأ گرفته، برای تعامل با کنترلر workspace استفاده می‌کند. همچنین با APIهای Azure Kubernetes Service (AKS) یکپارچه شده و گره‌های GPU جدید را به خوشه AKS اضافه می‌کند.
> نکته: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) یک مؤلفه متن‌باز است. در صورتی که کنترلرهای دیگر از APIهای [Karpenter-core](https://sigs.k8s.io/karpenter) پشتیبانی کنند، می‌توانند جایگزین آن شوند.

## ویدئوی معرفی  
[مشاهده دمو Kaito](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)

## نصب

لطفاً راهنمای نصب را از [اینجا](https://github.com/Azure/kaito/blob/main/docs/installation.md) بررسی کنید.

## شروع سریع

پس از نصب Kaito، می‌توان با اجرای دستورات زیر سرویس تنظیم دقیق را راه‌اندازی کرد.

```
apiVersion: kaito.sh/v1alpha1
kind: Workspace
metadata:
  name: workspace-tuning-phi-3
resource:
  instanceType: "Standard_NC6s_v3"
  labelSelector:
    matchLabels:
      app: tuning-phi-3
tuning:
  preset:
    name: phi-3-mini-128k-instruct
  method: qlora
  input:
    urls:
      - "https://huggingface.co/datasets/philschmid/dolly-15k-oai-style/resolve/main/data/train-00000-of-00001-54e3756291ca09c6.parquet?download=true"
  output:
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Tuning Output ACR Path
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
```

```sh
$ cat examples/fine-tuning/kaito_workspace_tuning_phi_3.yaml

apiVersion: kaito.sh/v1alpha1
kind: Workspace
metadata:
  name: workspace-tuning-phi-3
resource:
  instanceType: "Standard_NC6s_v3"
  labelSelector:
    matchLabels:
      app: tuning-phi-3
tuning:
  preset:
    name: phi-3-mini-128k-instruct
  method: qlora
  input:
    urls:
      - "https://huggingface.co/datasets/philschmid/dolly-15k-oai-style/resolve/main/data/train-00000-of-00001-54e3756291ca09c6.parquet?download=true"
  output:
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Tuning Output ACR Path
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/fine-tuning/kaito_workspace_tuning_phi_3.yaml
```

وضعیت workspace را می‌توان با اجرای دستور زیر پیگیری کرد. زمانی که ستون WORKSPACEREADY مقدار `True` شود، مدل با موفقیت مستقر شده است.

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

سپس می‌توان آدرس IP کلاستر سرویس استنتاج را یافت و با استفاده از یک پاد موقتی `curl` نقطه پایانی سرویس در کلاستر را آزمایش کرد.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان مادری آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئول هیچ گونه سوءتفاهم یا برداشت نادرستی که ناشی از استفاده از این ترجمه باشد، نیستیم.