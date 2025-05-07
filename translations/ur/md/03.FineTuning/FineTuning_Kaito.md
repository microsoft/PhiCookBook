<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a1c62bf7d86d6186bf8d3917196a92a0",
  "translation_date": "2025-05-07T13:38:22+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Kaito.md",
  "language_code": "ur"
}
-->
## Fine-Tuning with Kaito 

[Kaito](https://github.com/Azure/kaito) ایک آپریٹر ہے جو Kubernetes کلسٹر میں AI/ML inference ماڈل کی تعیناتی کو خودکار بناتا ہے۔

Kaito کے پاس درج ذیل اہم خصوصیات ہیں جو زیادہ تر مین اسٹریم ماڈل تعیناتی کے طریقہ کار سے مختلف ہیں جو ورچوئل مشین انفراسٹرکچر پر مبنی ہوتے ہیں:

- ماڈل فائلز کو container images کے ذریعے منظم کریں۔ ماڈل لائبریری استعمال کرتے ہوئے inference کالز کرنے کے لیے ایک http سرور فراہم کیا جاتا ہے۔
- GPU ہارڈویئر کے مطابق deployment parameters کو tune کرنے کی ضرورت نہیں کیونکہ پری سیٹ کنفیگریشنز فراہم کی جاتی ہیں۔
- ماڈل کی ضروریات کی بنیاد پر GPU نوڈز کو خودکار طریقے سے مہیا کریں۔
- اگر لائسنس اجازت دیتا ہے تو بڑے ماڈل امیجز کو Microsoft Container Registry (MCR) میں میزبانی کریں۔

Kaito استعمال کرتے ہوئے، Kubernetes میں بڑے AI inference ماڈلز کو onboard کرنے کا ورک فلو بہت آسان ہو جاتا ہے۔

## Architecture

Kaito کلاسک Kubernetes Custom Resource Definition (CRD)/controller ڈیزائن پیٹرن کی پیروی کرتا ہے۔ یوزر ایک `workspace` custom resource کو manage کرتا ہے جو GPU کی ضروریات اور inference کی وضاحت بیان کرتا ہے۔ Kaito controllers تعیناتی کو خودکار بنائیں گے `workspace` custom resource کو reconcile کر کے۔
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

اوپر دیا گیا خاکہ Kaito کے architecture کا جائزہ پیش کرتا ہے۔ اس کے اہم اجزاء درج ذیل ہیں:

- **Workspace controller**: یہ `workspace` custom resource کو reconcile کرتا ہے، نوڈ آٹو پروویژننگ کو trigger کرنے کے لیے `machine` (نیچے وضاحت کی گئی) custom resources بناتا ہے، اور ماڈل کے پری سیٹ کنفیگریشنز کی بنیاد پر inference workload (`deployment` یا `statefulset`) تخلیق کرتا ہے۔
- **Node provisioner controller**: اس controller کا نام [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) میں *gpu-provisioner* ہے۔ یہ [Karpenter](https://sigs.k8s.io/karpenter) سے ماخوذ `machine` CRD استعمال کرتا ہے تاکہ workspace controller کے ساتھ تعامل کرے۔ یہ Azure Kubernetes Service (AKS) APIs کے ساتھ مربوط ہوتا ہے تاکہ AKS کلسٹر میں نئے GPU نوڈز شامل کیے جا سکیں۔
> Note: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) ایک اوپن سورس کمپونینٹ ہے۔ اگر دوسرے controllers [Karpenter-core](https://sigs.k8s.io/karpenter) APIs کی حمایت کرتے ہوں تو اسے تبدیل کیا جا سکتا ہے۔

## Overview video 
[Watch the Kaito Demo](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)

## Installation

براہ کرم انسٹالیشن کی رہنمائی [یہاں](https://github.com/Azure/kaito/blob/main/docs/installation.md) چیک کریں۔

## Quick start

Kaito انسٹال کرنے کے بعد، کوئی درج ذیل کمانڈز آزما سکتا ہے تاکہ fine-tuning سروس شروع کی جا سکے۔

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

ورک اسپیس کی حالت کو درج ذیل کمانڈ چلا کر ٹریک کیا جا سکتا ہے۔ جب WORKSPACEREADY کالم `True` ہو جائے، تو ماڈل کامیابی سے تعینات ہو چکا ہوتا ہے۔

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

اس کے بعد، inference سروس کے کلسٹر IP کو تلاش کریں اور عارضی `curl` پوڈ استعمال کر کے کلسٹر میں سروس اینڈپوائنٹ کی جانچ کریں۔

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**ڈسکلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار ترجموں میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ورانہ انسانی ترجمہ تجویز کیا جاتا ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے لیے ہم ذمہ دار نہیں ہیں۔