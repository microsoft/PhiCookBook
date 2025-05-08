<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e46691923dca7cb2f11d32b1d9d558e0",
  "translation_date": "2025-05-07T14:33:09+00:00",
  "source_file": "md/01.Introduction/03/Kaito_Inference.md",
  "language_code": "fa"
}
-->
## استنتاج با Kaito

[Kaito](https://github.com/Azure/kaito) یک اپراتور است که استقرار مدل‌های استنتاج AI/ML را در یک کلاستر Kubernetes به‌صورت خودکار انجام می‌دهد.

Kaito نسبت به بیشتر روش‌های متداول استقرار مدل که بر بستر ماشین‌های مجازی ساخته شده‌اند، تفاوت‌های کلیدی زیر را دارد:

- مدیریت فایل‌های مدل با استفاده از ایمیج‌های کانتینری. یک سرور http فراهم شده است تا فراخوانی‌های استنتاج با استفاده از کتابخانه مدل انجام شود.
- اجتناب از تنظیم پارامترهای استقرار برای هماهنگی با سخت‌افزار GPU با ارائه پیکربندی‌های پیش‌فرض.
- تأمین خودکار نودهای GPU بر اساس نیازهای مدل.
- میزبانی ایمیج‌های مدل بزرگ در Microsoft Container Registry (MCR) عمومی در صورت اجازه مجوز.

با استفاده از Kaito، روند ورود مدل‌های بزرگ استنتاج AI در Kubernetes تا حد زیادی ساده شده است.

## معماری

Kaito از الگوی طراحی کلاسیک Kubernetes Custom Resource Definition (CRD) / کنترلر پیروی می‌کند. کاربر یک منبع سفارشی `workspace` را مدیریت می‌کند که نیازهای GPU و مشخصات استنتاج را توصیف می‌کند. کنترلرهای Kaito با تطبیق منبع سفارشی `workspace` استقرار را به‌صورت خودکار انجام می‌دهند.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

شکل بالا نمای کلی معماری Kaito را نشان می‌دهد. اجزای اصلی آن شامل موارد زیر است:

- **کنترلر Workspace**: این کنترلر منبع سفارشی `workspace` را تطبیق می‌دهد، منابع سفارشی `machine` (که در ادامه توضیح داده شده) را برای فعال‌سازی تأمین خودکار نودها ایجاد می‌کند و بار کاری استنتاج (`deployment` یا `statefulset`) را بر اساس پیکربندی‌های پیش‌فرض مدل ایجاد می‌کند.
- **کنترلر تأمین نود**: نام این کنترلر *gpu-provisioner* در [نمودار helm gpu-provisioner](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) است. این کنترلر از CRD `machine` که از [Karpenter](https://sigs.k8s.io/karpenter) منشأ گرفته، برای تعامل با کنترلر Workspace استفاده می‌کند. همچنین با APIهای Azure Kubernetes Service (AKS) ادغام می‌شود تا نودهای GPU جدید را به کلاستر AKS اضافه کند.  
> نکته: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) یک کامپوننت متن‌باز است. می‌توان آن را با کنترلرهای دیگر جایگزین کرد اگر از APIهای [Karpenter-core](https://sigs.k8s.io/karpenter) پشتیبانی کنند.

## نصب

لطفاً راهنمای نصب را از [اینجا](https://github.com/Azure/kaito/blob/main/docs/installation.md) بررسی کنید.

## شروع سریع استنتاج Phi-3  
[نمونه کد استنتاج Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

```
apiVersion: kaito.sh/v1alpha1
kind: Workspace
metadata:
  name: workspace-phi-3-mini
resource:
  instanceType: "Standard_NC6s_v3"
  labelSelector:
    matchLabels:
      apps: phi-3
inference:
  preset:
    name: phi-3-mini-4k-instruct
    # Note: This configuration also works with the phi-3-mini-128k-instruct preset
```

```sh
$ cat examples/inference/kaito_workspace_phi_3.yaml

apiVersion: kaito.sh/v1alpha1
kind: Workspace
metadata:
  name: workspace-phi-3-mini
resource:
  instanceType: "Standard_NC6s_v3"
  labelSelector:
    matchLabels:
      app: phi-3-adapter
tuning:
  preset:
    name: phi-3-mini-4k-instruct
  method: qlora
  input:
    urls:
      - "https://huggingface.co/datasets/philschmid/dolly-15k-oai-style/resolve/main/data/train-00000-of-00001-54e3756291ca09c6.parquet?download=true"
  output:
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Tuning Output ACR Path
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3.yaml
```

وضعیت workspace را می‌توان با اجرای فرمان زیر پیگیری کرد. وقتی ستون WORKSPACEREADY مقدار `True` شود، مدل با موفقیت مستقر شده است.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

سپس می‌توان آدرس IP کلاستر سرویس استنتاج را پیدا کرد و با استفاده از یک پاد موقتی `curl` نقطه انتهایی سرویس را در کلاستر تست کرد.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## شروع سریع استنتاج Phi-3 با آداپتورها

پس از نصب Kaito، می‌توان دستورات زیر را برای راه‌اندازی سرویس استنتاج امتحان کرد.

[نمونه کد استنتاج Phi-3 با آداپتورها](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

```
apiVersion: kaito.sh/v1alpha1
kind: Workspace
metadata:
  name: workspace-phi-3-mini-adapter
resource:
  instanceType: "Standard_NC6s_v3"
  labelSelector:
    matchLabels:
      apps: phi-3-adapter
inference:
  preset:
    name: phi-3-mini-128k-instruct
  adapters:
    - source:
        name: "phi-3-adapter"
        image: "ACR_REPO_HERE.azurecr.io/ADAPTER_HERE:0.0.1"
      strength: "1.0"
```

```sh
$ cat examples/inference/kaito_workspace_phi_3_with_adapters.yaml

apiVersion: kaito.sh/v1alpha1
kind: Workspace
metadata:
  name: workspace-phi-3-mini-adapter
resource:
  instanceType: "Standard_NC6s_v3"
  labelSelector:
    matchLabels:
      app: phi-3-adapter
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
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3_with_adapters.yaml
```

وضعیت workspace را می‌توان با اجرای فرمان زیر پیگیری کرد. وقتی ستون WORKSPACEREADY مقدار `True` شود، مدل با موفقیت مستقر شده است.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

سپس می‌توان آدرس IP کلاستر سرویس استنتاج را پیدا کرد و با استفاده از یک پاد موقتی `curl` نقطه انتهایی سرویس را در کلاستر تست کرد.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل اشتباهات یا نواقصی باشند. سند اصلی به زبان مادری خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، توصیه می‌شود از ترجمه حرفه‌ای انسانی استفاده شود. ما مسئول هیچ گونه سوء تفاهم یا برداشت نادرستی که از استفاده از این ترجمه به وجود آید، نیستیم.