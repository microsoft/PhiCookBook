<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a1c62bf7d86d6186bf8d3917196a92a0",
  "translation_date": "2025-03-27T13:54:43+00:00",
  "source_file": "md\\03.FineTuning\\FineTuning_Kaito.md",
  "language_code": "fa"
}
-->
## تنظیم دقیق با Kaito

[Kaito](https://github.com/Azure/kaito) یک اپراتور است که فرآیند استقرار مدل‌های استنتاج AI/ML را در یک کلاستر Kubernetes خودکار می‌کند.

Kaito در مقایسه با اکثر روش‌های متداول استقرار مدل که بر زیرساخت‌های ماشین مجازی ساخته شده‌اند، تفاوت‌های کلیدی زیر را دارد:

- مدیریت فایل‌های مدل با استفاده از تصاویر کانتینر. یک سرور http برای انجام درخواست‌های استنتاج با استفاده از کتابخانه مدل فراهم شده است.
- ارائه تنظیمات از پیش تعیین‌شده برای جلوگیری از نیاز به تنظیم پارامترهای استقرار برای سازگاری با سخت‌افزار GPU.
- تخصیص خودکار نودهای GPU بر اساس نیازهای مدل.
- میزبانی تصاویر مدل‌های بزرگ در Microsoft Container Registry (MCR) عمومی در صورتی که مجوز اجازه دهد.

با استفاده از Kaito، فرآیند وارد کردن مدل‌های استنتاج AI بزرگ در Kubernetes به طور قابل توجهی ساده می‌شود.


## معماری

Kaito از الگوی طراحی کلاسیک Custom Resource Definition(CRD)/controller در Kubernetes پیروی می‌کند. کاربر یک منبع سفارشی `workspace` را مدیریت می‌کند که نیازهای GPU و مشخصات استنتاج را توضیح می‌دهد. کنترلرهای Kaito استقرار را با هماهنگ‌سازی منبع سفارشی `workspace` خودکار می‌کنند.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="معماری Kaito" alt="معماری Kaito">
</div>

تصویر بالا نمای کلی معماری Kaito را نشان می‌دهد. اجزای اصلی آن شامل موارد زیر است:

- **کنترلر Workspace**: منبع سفارشی `workspace` را هماهنگ می‌کند، منابع سفارشی `machine` (که در ادامه توضیح داده شده‌اند) را برای تحریک تخصیص خودکار نود ایجاد می‌کند، و بر اساس تنظیمات پیش‌فرض مدل، بار کاری استنتاج (`deployment` یا `statefulset`) را ایجاد می‌کند.
- **کنترلر تخصیص نود**: نام این کنترلر *gpu-provisioner* است که در [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) قرار دارد. این کنترلر از CRD `machine` که از [Karpenter](https://sigs.k8s.io/karpenter) منشأ گرفته است، برای تعامل با کنترلر Workspace استفاده می‌کند. این کنترلر با APIهای Azure Kubernetes Service(AKS) ادغام شده تا نودهای GPU جدید را به کلاستر AKS اضافه کند.
> توجه: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) یک کامپوننت متن‌باز است. در صورت پشتیبانی از APIهای [Karpenter-core](https://sigs.k8s.io/karpenter)، می‌توان آن را با کنترلرهای دیگر جایگزین کرد.

## ویدئوی معرفی
[دموی Kaito را مشاهده کنید](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)
## نصب

راهنمای نصب را [اینجا](https://github.com/Azure/kaito/blob/main/docs/installation.md) بررسی کنید.

## شروع سریع

پس از نصب Kaito، می‌توانید دستورات زیر را برای شروع سرویس تنظیم دقیق امتحان کنید.

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

وضعیت Workspace را می‌توان با اجرای دستور زیر پیگیری کرد. هنگامی که ستون WORKSPACEREADY به `True` تبدیل شود، مدل با موفقیت مستقر شده است.

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

سپس می‌توانید ip کلاستر سرویس استنتاج را پیدا کنید و از یک `curl` pod موقتی برای آزمایش نقطه پایانی سرویس در کلاستر استفاده کنید.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما برای دقت تلاش می‌کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌هایی باشد. سند اصلی به زبان مادری باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئولیتی در قبال سوءتفاهم‌ها یا تفسیرهای نادرست ناشی از استفاده از این ترجمه نداریم.