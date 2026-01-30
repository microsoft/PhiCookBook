## Kaito کے ساتھ فائن ٹیوننگ

[Kaito](https://github.com/Azure/kaito) ایک آپریٹر ہے جو Kubernetes کلسٹر میں AI/ML inference ماڈل کی تعیناتی کو خودکار بناتا ہے۔

Kaito کے درج ذیل اہم فرق ہیں جو زیادہ تر روایتی ماڈل تعیناتی کے طریقوں سے مختلف ہیں جو ورچوئل مشین انفراسٹرکچر پر مبنی ہوتے ہیں:

- ماڈل فائلز کو container images کے ذریعے منظم کرنا۔ ماڈل لائبریری کے ذریعے inference کالز کرنے کے لیے ایک http سرور فراہم کیا جاتا ہے۔
- GPU ہارڈویئر کے مطابق تعیناتی کے پیرامیٹرز کو ایڈجسٹ کرنے کی ضرورت نہیں، کیونکہ پری سیٹ کنفیگریشنز مہیا کی جاتی ہیں۔
- ماڈل کی ضروریات کے مطابق GPU نوڈز خودکار طور پر فراہم کرنا۔
- اگر لائسنس اجازت دیتا ہے تو بڑے ماڈل امیجز کو Microsoft Container Registry (MCR) میں ہوسٹ کرنا۔

Kaito کے استعمال سے Kubernetes میں بڑے AI inference ماڈلز کو شامل کرنے کا ورک فلو کافی آسان ہو جاتا ہے۔

## فن تعمیر

Kaito کلاسیکی Kubernetes Custom Resource Definition (CRD)/controller ڈیزائن پیٹرن کی پیروی کرتا ہے۔ صارف ایک `workspace` کسٹم ریسورس کو منظم کرتا ہے جو GPU کی ضروریات اور inference کی وضاحت بیان کرتا ہے۔ Kaito کنٹرولرز `workspace` کسٹم ریسورس کو reconcile کر کے تعیناتی کو خودکار بناتے ہیں۔
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

اوپر دی گئی تصویر Kaito کے فن تعمیر کا جائزہ پیش کرتی ہے۔ اس کے اہم اجزاء درج ذیل ہیں:

- **Workspace controller**: یہ `workspace` کسٹم ریسورس کو reconcile کرتا ہے، `machine` (نیچے وضاحت کی گئی ہے) کسٹم ریسورسز بناتا ہے تاکہ نوڈ کی خودکار فراہمی کو متحرک کیا جا سکے، اور ماڈل کی پری سیٹ کنفیگریشنز کی بنیاد پر inference ورک لوڈ (`deployment` یا `statefulset`) تخلیق کرتا ہے۔
- **Node provisioner controller**: اس کنٹرولر کا نام [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) میں *gpu-provisioner* ہے۔ یہ `machine` CRD استعمال کرتا ہے جو [Karpenter](https://sigs.k8s.io/karpenter) سے ماخوذ ہے تاکہ workspace controller کے ساتھ تعامل کرے۔ یہ Azure Kubernetes Service (AKS) APIs کے ساتھ مربوط ہو کر AKS کلسٹر میں نئے GPU نوڈز شامل کرتا ہے۔
> Note: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) ایک اوپن سورس کمپونینٹ ہے۔ اگر دوسرے کنٹرولرز [Karpenter-core](https://sigs.k8s.io/karpenter) APIs کی حمایت کرتے ہیں تو انہیں اس کی جگہ استعمال کیا جا سکتا ہے۔

## جائزہ ویڈیو  
[Kaito ڈیمو دیکھیں](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)

## تنصیب

براہ کرم تنصیب کی رہنمائی [یہاں](https://github.com/Azure/kaito/blob/main/docs/installation.md) دیکھیں۔

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

workspace کی حالت کو درج ذیل کمانڈ چلا کر ٹریک کیا جا سکتا ہے۔ جب WORKSPACEREADY کالم `True` ہو جائے، تو ماڈل کامیابی سے تعینات ہو چکا ہوتا ہے۔

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

اس کے بعد، inference سروس کا کلسٹر IP معلوم کیا جا سکتا ہے اور عارضی `curl` پوڈ کے ذریعے کلسٹر میں سروس اینڈ پوائنٹ کی جانچ کی جا سکتی ہے۔

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**دستخطی نوٹ**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں ہی معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم پر عائد نہیں ہوتی۔