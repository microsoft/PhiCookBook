<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aca91084bc440431571e00bf30d96ab8",
  "translation_date": "2026-01-05T17:11:06+00:00",
  "source_file": "md/01.Introduction/03/Kaito_Inference.md",
  "language_code": "ur"
}
-->
## Kaito کے ساتھ استدلال

[Kaito](https://github.com/Azure/kaito) ایک آپریٹر ہے جو Kubernetes کلسٹر میں AI/ML استدلال ماڈل کی تعیناتی کو خودکار بناتا ہے۔

Kaito میں درج ذیل اہم خصوصیات ہیں جو بیشتر مرکزی دھارے کے ماڈل تعیناتی کے طریقہ کار کے مقابلے میں ہیں جو ورچوئل مشین انفراسٹرکچر پر بنائے گئے ہیں:

- ماڈل فائلوں کا انتظام کنٹینر امیجز کا استعمال کرتے ہوئے۔ ماڈل لائبریری کا استعمال کرتے ہوئے استدلال کالز کرنے کے لیے ایک http سرور فراہم کیا جاتا ہے۔
- پری سیٹ کنفیگریشنز فراہم کر کے GPU ہارڈویئر کے مطابق تعیناتی کے پیرا میٹرز کو ٹیون کرنے سے گریز کریں۔
- ماڈل کی ضروریات کی بنیاد پر GPU نوڈز خودکار طور پر فراہم کریں۔
- اگر لائسنس اجازت دیتا ہے تو بڑے ماڈل امیجز کو عوامی Microsoft Container Registry (MCR) میں ہوست کریں۔

Kaito کا استعمال کرتے ہوئے، Kubernetes میں بڑے AI استدلال ماڈلز کے آن بورڈنگ کا ورک فلو کافی آسان ہو جاتا ہے۔

## فن تعمیر

Kaito روایت کے مطابق Kubernetes Custom Resource Definition (CRD) / کنٹرولر ڈیزائن پیٹرن کی پیروی کرتا ہے۔ صارف ایک `workspace` کسٹم ریسورس کا انتظام کرتا ہے جو GPU کی ضروریات اور استدلال کی وضاحت بیان کرتا ہے۔ Kaito کنٹرولرز `workspace` کسٹم ریسورس کے ذریعے تعیناتی کو خودکار بنائیں گے۔

<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/website/static/img/ragarch.png" width=80% title="KAITO RAGEngine architecture" alt="KAITO RAGEngine architecture">
</div>

اوپر دی گئی شکل Kaito کے فن تعمیر کا جائزہ پیش کرتی ہے۔ اس کے مرکزی اجزاء درج ذیل ہیں:

- **Workspace controller**: یہ `workspace` کسٹم ریسورس کی مطابقت پیدا کرتا ہے، node خودکار فراہمی کو متحرک کرنے کے لیے `machine` (نیچے وضاحت کی گئی) کسٹم ریسورسز بناتا ہے، اور ماڈل کی پری سیٹ کنفیگریشنز کی بنیاد پر استدلال کا ورکلوڈ (`deployment` یا `statefulset`) بناتا ہے۔
- **Node provisioner controller**: کنٹرولر کا نام [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) میں *gpu-provisioner* ہے۔ یہ [Karpenter](https://sigs.k8s.io/karpenter) سے نکلے ہوئے `machine` CRD کا استعمال کرتا ہے تاکہ ورک اسپیس کنٹرولر کے ساتھ تعامل کرے۔ یہ Azure Kubernetes Service (AKS) APIs کو مربوط کرتا ہے تاکہ AKS کلسٹر میں نئے GPU نوڈز شامل کیے جا سکیں۔
> نوٹ: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) ایک اوپن سورس کمپونینٹ ہے۔ اگر دیگر کنٹرولرز [Karpenter-core](https://sigs.k8s.io/karpenter) APIs کی حمایت کرتے ہوں تو انہیں اس کے متبادل کے طور پر استعمال کیا جا سکتا ہے۔

## تنصیب

براہ کرم تنصیب کی رہنمائی [یہاں](https://github.com/Azure/kaito/blob/main/docs/installation.md) دیکھیں۔

## تیزی سے شروع کریں Inference Phi-3  
[نمونہ کوڈ Inference Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # آؤٹ پٹ ACR راستہ کو ٹیون کرنا
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3.yaml
```

ورک اسپیس کی حیثیت درج ذیل کمانڈ چلانے سے ٹریک کی جا سکتی ہے۔ جب WORKSPACEREADY کالم `True` ہو جائے، تو ماڈل کامیابی سے تعینات ہو چکا ہوتا ہے۔

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

اس کے بعد، کوئی استدلال سروس کا کلسٹر آئی پی تلاش کر سکتا ہے اور کلستر میں سروس اینڈپوائنٹ کی جانچ کے لیے عارضی `curl` پوڈ استعمال کر سکتا ہے۔

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## تیزی سے شروع کریں Inference Phi-3 اڈاپٹرز کے ساتھ

Kaito انسٹال کرنے کے بعد، کوئی درج ذیل کمانڈز آزما سکتا ہے تاکہ استدلال سروس شروع کی جا سکے۔

[نمونہ کوڈ Inference Phi-3 اڈاپٹرز کے ساتھ](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # ٹوننگ آؤٹ پٹ اے سی آر راہ
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3_with_adapters.yaml
```

ورک اسپیس کی حیثیت درج ذیل کمانڈ چلانے سے ٹریک کی جا سکتی ہے۔ جب WORKSPACEREADY کالم `True` ہو جائے، تو ماڈل کامیابی سے تعینات ہو چکا ہوتا ہے۔

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

اس کے بعد، کوئی استدلال سروس کا کلسٹر آئی پی تلاش کر سکتا ہے اور کلستر میں سروس اینڈپوائنٹ کی جانچ کے لیے عارضی `curl` پوڈ استعمال کر سکتا ہے۔

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ذمہ داری سے استثناء**:
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کی کوشش کرتے ہیں، براہ کرم آگاہ رہیں کہ خودکار تراجم میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں مستند ماخذ سمجھا جانا چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمہ کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم پر نہیں ہوگی۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->