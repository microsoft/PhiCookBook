<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7739575218e3244a58516832ad88a9a2",
  "translation_date": "2025-04-03T06:53:36+00:00",
  "source_file": "md\\01.Introduction\\03\\Kaito_Inference.md",
  "language_code": "ur"
}
-->
## کائٹو کے ساتھ انفرنس 

[Kaito](https://github.com/Azure/kaito) ایک آپریٹر ہے جو Kubernetes کلسٹر میں AI/ML انفرنس ماڈل کو خودکار طریقے سے تعینات کرتا ہے۔

کائٹو درج ذیل اہم فرق فراہم کرتا ہے، جو زیادہ تر عام ماڈل تعیناتی طریقوں کے مقابلے میں ہیں، جو ورچوئل مشین انفراسٹرکچر پر مبنی ہیں:

- ماڈل فائلز کو کنٹینر امیجز کے ذریعے منظم کریں۔ ماڈل لائبریری کے ذریعے انفرنس کالز انجام دینے کے لیے ایک HTTP سرور فراہم کیا جاتا ہے۔
- GPU ہارڈویئر کے مطابق تعیناتی پیرامیٹرز کو ٹیون کرنے سے بچیں، پری سیٹ کنفیگریشنز فراہم کرکے۔
- ماڈل کی ضروریات کے مطابق GPU نوڈز کو خودکار طریقے سے پروویژن کریں۔
- اگر لائسنس اجازت دے تو بڑے ماڈل امیجز کو Microsoft Container Registry (MCR) میں عوامی طور پر ہوسٹ کریں۔

کائٹو کے استعمال سے Kubernetes میں بڑے AI انفرنس ماڈلز کو شامل کرنے کا ورک فلو کافی حد تک آسان ہو جاتا ہے۔

## آرکیٹیکچر

کائٹو کلاسک Kubernetes Custom Resource Definition(CRD)/کنٹرولر ڈیزائن پیٹرن کی پیروی کرتا ہے۔ صارف ایک `workspace` کسٹم ریسورس کا انتظام کرتا ہے جو GPU کی ضروریات اور انفرنس تفصیلات کو بیان کرتا ہے۔ کائٹو کنٹرولرز `workspace` کسٹم ریسورس کو ہم آہنگ کرکے تعیناتی کو خودکار بناتے ہیں۔
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

اوپر دی گئی تصویر کائٹو آرکیٹیکچر کا جائزہ پیش کرتی ہے۔ اس کے اہم اجزاء درج ذیل ہیں:

- **ورک اسپیس کنٹرولر**: یہ `workspace` کسٹم ریسورس کو ہم آہنگ کرتا ہے، `machine` (نیچے وضاحت کی گئی ہے) کسٹم ریسورسز تخلیق کرتا ہے تاکہ نوڈ کی خودکار پروویژننگ کو متحرک کیا جا سکے، اور ماڈل کی پری سیٹ کنفیگریشنز کے مطابق انفرنس ورک لوڈ (`deployment` یا `statefulset`) تخلیق کرتا ہے۔
- **نوڈ پروویژنر کنٹرولر**: اس کنٹرولر کا نام [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) میں *gpu-provisioner* ہے۔ یہ `machine` CRD استعمال کرتا ہے جو [Karpenter](https://sigs.k8s.io/karpenter) سے اخذ کیا گیا ہے تاکہ ورک اسپیس کنٹرولر کے ساتھ تعامل کیا جا سکے۔ یہ Azure Kubernetes Service(AKS) APIs کے ساتھ انضمام کرتا ہے تاکہ AKS کلسٹر میں نئے GPU نوڈز شامل کیے جا سکیں۔
> نوٹ: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) ایک اوپن سورس جزو ہے۔ اگر وہ [Karpenter-core](https://sigs.k8s.io/karpenter) APIs کو سپورٹ کرتے ہیں تو اسے دوسرے کنٹرولرز کے ساتھ تبدیل کیا جا سکتا ہے۔

## انسٹالیشن

انسٹالیشن کی رہنمائی کے لیے [یہاں](https://github.com/Azure/kaito/blob/main/docs/installation.md) دیکھیں۔

## جلدی سے شروع کریں انفرنس Phi-3
[سمپل کوڈ انفرنس Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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

ورک اسپیس کی حالت درج ذیل کمانڈ چلا کر ٹریک کی جا سکتی ہے۔ جب WORKSPACEREADY کالم `True` ہو جائے، تو ماڈل کامیابی سے تعینات ہو چکا ہوتا ہے۔

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

اس کے بعد، انفرنس سروس کے کلسٹر آئی پی کو تلاش کریں اور کلسٹر میں سروس اینڈ پوائنٹ کو ٹیسٹ کرنے کے لیے ایک عارضی `curl` پوڈ استعمال کریں۔

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## جلدی سے شروع کریں انفرنس Phi-3 ایڈاپٹرز کے ساتھ

کائٹو انسٹال کرنے کے بعد، انفرنس سروس شروع کرنے کے لیے درج ذیل کمانڈز آزمائیں۔

[سمپل کوڈ انفرنس Phi-3 ایڈاپٹرز کے ساتھ](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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

ورک اسپیس کی حالت درج ذیل کمانڈ چلا کر ٹریک کی جا سکتی ہے۔ جب WORKSPACEREADY کالم `True` ہو جائے، تو ماڈل کامیابی سے تعینات ہو چکا ہوتا ہے۔

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

اس کے بعد، انفرنس سروس کے کلسٹر آئی پی کو تلاش کریں اور کلسٹر میں سروس اینڈ پوائنٹ کو ٹیسٹ کرنے کے لیے ایک عارضی `curl` پوڈ استعمال کریں۔

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**ڈسکلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کے لیے کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا غلط فہمیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی اصل زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ورانہ انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے لیے ہم ذمہ دار نہیں ہیں۔