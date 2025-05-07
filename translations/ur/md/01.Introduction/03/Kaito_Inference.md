<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e46691923dca7cb2f11d32b1d9d558e0",
  "translation_date": "2025-05-07T14:33:49+00:00",
  "source_file": "md/01.Introduction/03/Kaito_Inference.md",
  "language_code": "ur"
}
-->
## کائیتو کے ساتھ استنتاج

[Kaito](https://github.com/Azure/kaito) ایک آپریٹر ہے جو Kubernetes کلسٹر میں AI/ML استنتاج ماڈل کی تعیناتی کو خودکار بناتا ہے۔

کائیتو کے درج ذیل اہم فرق ہیں جو زیادہ تر روایتی ماڈل تعیناتی طریقہ کار سے مختلف ہیں جو ورچوئل مشین انفراسٹرکچر پر مبنی ہیں:

- ماڈل فائلوں کا انتظام کنٹینر امیجز کے ذریعے۔ ماڈل لائبریری استعمال کرتے ہوئے استنتاج کالز کرنے کے لیے ایک http سرور فراہم کیا جاتا ہے۔
- GPU ہارڈویئر کے مطابق تعیناتی کے پیرامیٹرز کو ایڈجسٹ کرنے سے گریز، پری سیٹ کنفیگریشنز فراہم کر کے۔
- ماڈل کی ضروریات کی بنیاد پر GPU نوڈز کا خودکار انتظام۔
- اگر لائسنس اجازت دیتا ہے تو بڑے ماڈل امیجز کو Microsoft Container Registry (MCR) میں ہوسٹ کرنا۔

کائیتو استعمال کرتے ہوئے، Kubernetes میں بڑے AI استنتاج ماڈلز کو شامل کرنے کا ورک فلو کافی آسان ہو جاتا ہے۔

## فن تعمیر

کائیتو کلاسک Kubernetes Custom Resource Definition (CRD)/controller ڈیزائن پیٹرن کی پیروی کرتا ہے۔ صارف ایک `workspace` کسٹم ریسورس کا انتظام کرتا ہے جو GPU کی ضروریات اور استنتاج کی وضاحت بیان کرتا ہے۔ کائیتو کنٹرولرز تعیناتی کو خودکار بنائیں گے اور `workspace` کسٹم ریسورس کو ہم آہنگ کریں گے۔
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

اوپر والا خاکہ کائیتو کے فن تعمیر کا جائزہ پیش کرتا ہے۔ اس کے اہم اجزاء درج ذیل ہیں:

- **Workspace controller**: یہ `workspace` کسٹم ریسورس کو ہم آہنگ کرتا ہے، نوڈ آٹو پروویژننگ کو متحرک کرنے کے لیے `machine` (نیچے وضاحت کی گئی) کسٹم ریسورسز بناتا ہے، اور ماڈل کی پری سیٹ کنفیگریشنز کی بنیاد پر استنتاج ورک لوڈ (`deployment` یا `statefulset`) تخلیق کرتا ہے۔
- **Node provisioner controller**: اس کنٹرولر کا نام [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) میں *gpu-provisioner* ہے۔ یہ [Karpenter](https://sigs.k8s.io/karpenter) سے ماخوذ `machine` CRD استعمال کرتا ہے تاکہ workspace controller کے ساتھ تعامل کرے۔ یہ Azure Kubernetes Service (AKS) APIs کے ساتھ انضمام کرتا ہے تاکہ AKS کلسٹر میں نئے GPU نوڈز شامل کیے جا سکیں۔
> نوٹ: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) ایک اوپن سورس کمپونینٹ ہے۔ اگر دوسرے کنٹرولرز [Karpenter-core](https://sigs.k8s.io/karpenter) APIs کی حمایت کرتے ہیں تو اسے تبدیل کیا جا سکتا ہے۔

## تنصیب

براہ کرم تنصیب کی ہدایات [یہاں](https://github.com/Azure/kaito/blob/main/docs/installation.md) دیکھیں۔

## استنتاج Phi-3 کے لیے فوری آغاز
[نمونہ کوڈ استنتاج Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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

ورک اسپیس کی صورتحال درج ذیل کمانڈ چلا کر معلوم کی جا سکتی ہے۔ جب WORKSPACEREADY کالم `True` ہو جائے تو ماڈل کامیابی سے تعینات ہو چکا ہوتا ہے۔

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

اس کے بعد، استنتاج سروس کا کلسٹر IP معلوم کیا جا سکتا ہے اور عارضی `curl` پوڈ کا استعمال کرتے ہوئے کلسٹر میں سروس اینڈ پوائنٹ کی جانچ کی جا سکتی ہے۔

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## اڈاپٹرز کے ساتھ استنتاج Phi-3 کے لیے فوری آغاز

کائیتو انسٹال کرنے کے بعد، درج ذیل کمانڈز آزما کر استنتاج سروس شروع کی جا سکتی ہے۔

[نمونہ کوڈ استنتاج Phi-3 اڈاپٹرز کے ساتھ](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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

ورک اسپیس کی صورتحال درج ذیل کمانڈ چلا کر معلوم کی جا سکتی ہے۔ جب WORKSPACEREADY کالم `True` ہو جائے تو ماڈل کامیابی سے تعینات ہو چکا ہوتا ہے۔

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

اس کے بعد، استنتاج سروس کا کلسٹر IP معلوم کیا جا سکتا ہے اور عارضی `curl` پوڈ کا استعمال کرتے ہوئے کلسٹر میں سروس اینڈ پوائنٹ کی جانچ کی جا سکتی ہے۔

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**ڈس کلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کی کوشش کرتے ہیں، براہ کرم آگاہ رہیں کہ خودکار تراجم میں غلطیاں یا بے ضابطگیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ تجویز کیا جاتا ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم پر عائد نہیں ہوتی۔