<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "05e69691c294289d217150bec390a5fb",
  "translation_date": "2025-04-03T08:05:58+00:00",
  "source_file": "md\\03.FineTuning\\FineTuning_Kaito.md",
  "language_code": "ur"
}
-->
## Kaito کے ساتھ فائن ٹیوننگ 

[Kaito](https://github.com/Azure/kaito) ایک آپریٹر ہے جو Kubernetes کلسٹر میں AI/ML انفیرنس ماڈل ڈیپلائمنٹ کو خودکار بناتا ہے۔

Kaito عام طور پر موجودہ ماڈل ڈیپلائمنٹ طریقوں کے مقابلے میں درج ذیل اہم فرق رکھتا ہے، جو ورچوئل مشین انفراسٹرکچر پر مبنی ہوتے ہیں:

- کنٹینر امیجز کے ذریعے ماڈل فائلز کو منظم کریں۔ ایک HTTP سرور فراہم کیا جاتا ہے تاکہ ماڈل لائبریری استعمال کرتے ہوئے انفیرنس کالز کی جا سکیں۔
- GPU ہارڈویئر کے مطابق ڈیپلائمنٹ پیرامیٹرز کو ٹیون کرنے سے بچیں، اور پہلے سے موجود کنفیگریشنز فراہم کریں۔
- ماڈل کی ضروریات کے مطابق GPU نوڈز کو خودکار طور پر پروویژن کریں۔
- اگر لائسنس اجازت دے، تو بڑے ماڈل امیجز کو Microsoft Container Registry (MCR) میں عوامی طور پر ہوسٹ کریں۔

Kaito کے ذریعے، Kubernetes میں بڑے AI انفیرنس ماڈلز کو شامل کرنے کا ورک فلو بہت حد تک آسان ہو جاتا ہے۔

## آرکیٹیکچر

Kaito کلاسیکی Kubernetes Custom Resource Definition(CRD)/کنٹرولر ڈیزائن پیٹرن کی پیروی کرتا ہے۔ صارف `workspace` کسٹم ریسورس کو منظم کرتا ہے، جو GPU ضروریات اور انفیرنس تفصیلات کو بیان کرتا ہے۔ Kaito کنٹرولرز `workspace` کسٹم ریسورس کو ہم آہنگ کر کے ڈیپلائمنٹ کو خودکار بناتے ہیں۔
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

اوپر دی گئی تصویر میں Kaito آرکیٹیکچر کا خلاصہ پیش کیا گیا ہے۔ اس کے اہم اجزاء درج ذیل ہیں:

- **ورک اسپیس کنٹرولر**: یہ `workspace` کسٹم ریسورس کو ہم آہنگ کرتا ہے، `machine` (جو نیچے وضاحت کی گئی ہے) کسٹم ریسورسز تخلیق کرتا ہے تاکہ نوڈز کو خودکار طور پر پروویژن کیا جا سکے، اور ماڈل کی پہلے سے موجود کنفیگریشنز کی بنیاد پر انفیرنس ورک لوڈ (`deployment` یا `statefulset`) تخلیق کرتا ہے۔
- **نوڈ پروویژنر کنٹرولر**: اس کنٹرولر کا نام [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) میں *gpu-provisioner* ہے۔ یہ `machine` CRD کا استعمال کرتا ہے جو [Karpenter](https://sigs.k8s.io/karpenter) سے اخذ کیا گیا ہے تاکہ ورک اسپیس کنٹرولر کے ساتھ تعامل کیا جا سکے۔ یہ Azure Kubernetes Service(AKS) APIs کے ساتھ انضمام کر کے AKS کلسٹر میں نئے GPU نوڈز شامل کرتا ہے۔  
> نوٹ: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) ایک اوپن سورس جز ہے۔ اگر دوسرے کنٹرولرز [Karpenter-core](https://sigs.k8s.io/karpenter) APIs کو سپورٹ کرتے ہیں تو اسے تبدیل کیا جا سکتا ہے۔

## جائزہ ویڈیو 
[Kaito ڈیمو دیکھیں](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)

## انسٹالیشن

انسٹالیشن کی رہنمائی [یہاں](https://github.com/Azure/kaito/blob/main/docs/installation.md) دیکھیں۔

## فوری آغاز

Kaito انسٹال کرنے کے بعد، فائن ٹیوننگ سروس شروع کرنے کے لیے درج ذیل کمانڈز آزما سکتے ہیں۔

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

ورک اسپیس کی حالت درج ذیل کمانڈ چلا کر ٹریک کی جا سکتی ہے۔ جب WORKSPACEREADY کالم `True` ہو جائے، تو ماڈل کامیابی سے ڈیپلائی ہو چکا ہے۔

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

اس کے بعد، انفیرنس سروس کے کلسٹر آئی پی کو تلاش کریں اور کلسٹر میں سروس اینڈ پوائنٹ کو ٹیسٹ کرنے کے لیے ایک عارضی `curl` پوڈ استعمال کریں۔

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**ڈسکلوزر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کے لیے کوشش کرتے ہیں، لیکن براہ کرم نوٹ کریں کہ خودکار ترجمے میں غلطیاں یا نقصانات ہو سکتے ہیں۔ اصل دستاویز کو اس کی اصل زبان میں معتبر ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ورانہ انسانی ترجمہ کی سفارش کی جاتی ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے ذمہ دار نہیں ہیں۔