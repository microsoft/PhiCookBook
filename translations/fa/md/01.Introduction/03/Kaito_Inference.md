## استنتاج با کایتو

[Kaito](https://github.com/Azure/kaito) یک اپراتور است که استقرار مدل استنتاج هوش مصنوعی/یادگیری ماشین را در کلاستر کوبرنتیز خودکار می‌کند.

کایتو تفاوت‌های کلیدی زیر را نسبت به بیشتر روش‌های معمول استقرار مدل که روی زیرساخت‌های ماشین مجازی ساخته شده‌اند، دارد:

- مدیریت فایل‌های مدل با استفاده از تصاویر کانتینر. یک سرور http برای انجام فراخوانی‌های استنتاج با استفاده از کتابخانه مدل فراهم شده است.
- جلوگیری از تنظیم پارامترهای استقرار برای تطبیق با سخت‌افزار GPU با ارائه پیکربندی‌های پیش‌تنظیم‌شده.
- تامین خودکار گره‌های GPU بر اساس نیازهای مدل.
- میزبانی تصاویر مدل بزرگ در رجیستری عمومی مایکروسافت کانتینر (MCR) در صورت اجازه مجوز.

با استفاده از کایتو، فرایند وارد کردن مدل‌های بزرگ استنتاج AI در کوبرنتیز تا حد زیادی ساده شده است.

## معماری

کایتو الگوی طراحی کلاسیک تعریف منبع سفارشی (CRD)/کنترلر کوبرنتیز را دنبال می‌کند. کاربر یک منبع سفارشی `workspace` را مدیریت می‌کند که نیازهای GPU و مشخصات استنتاج را توصیف می‌کند. کنترلرهای کایتو با آشتی دادن منبع سفارشی `workspace` استقرار را خودکار می‌کنند.

<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/website/static/img/ragarch.png" width=80% title="معماری KAITO RAGEngine" alt="معماری KAITO RAGEngine">
</div>

شکل بالا نمای کلی معماری کایتو را نمایش می‌دهد. اجزای اصلی آن شامل موارد زیر است:

- **کنترلر Workspace**: این کنترلر منبع سفارشی `workspace` را آشتی می‌دهد، منابع سفارشی `machine` (که در ادامه توضیح داده شده) را برای فعال‌سازی تامین خودکار گره‌ها ایجاد می‌کند و بار کاری استنتاج (`deployment` یا `statefulset`) را بر اساس پیکربندی‌های پیش‌تنظیم مدل می‌سازد.
- **کنترلر تامین گره**: نام کنترلر *gpu-provisioner* در [نمودار Helm gpu-provisioner](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) است. این کنترلر از CRD `machine` منشعب از [Karpenter](https://sigs.k8s.io/karpenter) برای تعامل با کنترلر workspace استفاده می‌کند. این کنترلر با APIهای Azure Kubernetes Service (AKS) ادغام می‌شود تا گره‌های GPU جدید به کلاستر AKS اضافه کند.
> نکته: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) یک مؤلفه متن باز است. در صورت پشتیبانی کنترلرهای دیگر از APIهای [Karpenter-core](https://sigs.k8s.io/karpenter)، می‌توان آن را جایگزین کرد.

## نصب

لطفاً راهنمای نصب را [اینجا](https://github.com/Azure/kaito/blob/main/docs/installation.md) بررسی کنید.

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # تنظیم مسیر خروجی ACR
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3.yaml
```

وضعیت workspace را می‌توان با اجرای فرمان زیر پیگیری کرد. هنگامی که ستون WORKSPACEREADY به `True` تبدیل شود، مدل با موفقیت مستقر شده است.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

در ادامه، می‌توان آی‌پی کلاستر سرویس استنتاج را پیدا کرد و با استفاده از یک پاد موقتی `curl`، نقطه انتهایی سرویس را در کلاستر آزمایش کرد.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## شروع سریع استنتاج Phi-3 با آداپتورها

پس از نصب کایتو، می‌توان از دستورات زیر برای راه‌اندازی یک سرویس استنتاج استفاده کرد.

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # تنظیم مسیر خروجی ACR
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3_with_adapters.yaml
```

وضعیت workspace را می‌توان با اجرای فرمان زیر پیگیری کرد. هنگامی که ستون WORKSPACEREADY به `True` تبدیل شود، مدل با موفقیت مستقر شده است.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

در ادامه، می‌توان آی‌پی کلاستر سرویس استنتاج را پیدا کرد و با استفاده از یک پاد موقتی `curl`، نقطه انتهایی سرویس را در کلاستر آزمایش کرد.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در دقت ترجمه تلاش می‌کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان مادری آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، توصیه می‌شود از ترجمه انسانی حرفه‌ای استفاده کنید. ما در قبال هر گونه سوءتفاهم یا تفسیر نادرست ناشی از استفاده از این ترجمه مسئولیتی نداریم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->