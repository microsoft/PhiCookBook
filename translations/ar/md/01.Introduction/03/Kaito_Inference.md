<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aca91084bc440431571e00bf30d96ab8",
  "translation_date": "2026-01-05T08:33:35+00:00",
  "source_file": "md/01.Introduction/03/Kaito_Inference.md",
  "language_code": "ar"
}
-->
## الاستدلال باستخدام Kaito

[Kaito](https://github.com/Azure/kaito) هو عامل يقوم بأتمتة نشر موديلات الاستدلال AI/ML في مجموعة Kubernetes.

يمتلك Kaito الفروق الرئيسية التالية مقارنة بمعظم منهجيات نشر الموديلات السائدة المبنية على بنى تحتية للآلات الافتراضية:

- إدارة ملفات الموديل باستخدام صور الحاويات. يتم توفير خادم HTTP لإجراء مكالمات الاستدلال باستخدام مكتبة الموديل.
- تجنب ضبط معلمات النشر لتناسب عتاد GPU من خلال توفير تكوينات مسبقة الإعداد.
- إجراء توفير تلقائي لعُقد GPU بناءً على متطلبات الموديل.
- استضافة صور الموديلات الكبيرة في سجل الحاويات العام لمايكروسوفت (MCR) إذا سمحت الرخصة بذلك.

باستخدام Kaito، يتم تبسيط سير عمل إدخال موديلات الاستدلال الكبيرة في Kubernetes إلى حد كبير.

## الهيكلية

يتبع Kaito نمط تصميم تعريف الموارد المخصصة (CRD) / وحدة التحكم الكلاسيكي في Kubernetes. يدير المستخدم موردًا مخصصًا يسمى `workspace` يصف متطلبات GPU ومواصفات الاستدلال. تقوم وحدات تحكم Kaito بأتمتة النشر عبر التوفيق بين مورد `workspace` المخصص.

<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/website/static/img/ragarch.png" width=80% title="KAITO RAGEngine architecture" alt="KAITO RAGEngine architecture">
</div>

تعرض الصورة أعلاه نظرة عامة على هيكلية Kaito. تتكون مكوناته الرئيسية من:

- **وحدة تحكم workspace**: تقوم بتوفيق مورد `workspace` المخصص، وتنشئ موارد مخصصة `machine` (موضحة أدناه) لتحفيز التوفير التلقائي للعقد، وتنشئ عبء عمل الاستدلال (`deployment` أو `statefulset`) بناءً على التكوينات المسبقة للموديل.
- **وحدة تحكم مزود العقدة**: اسم الوحدة هو *gpu-provisioner* في [مخطط helm الخاص بـ gpu-provisioner](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). تستخدم CRD `machine` المُشتق من [Karpenter](https://sigs.k8s.io/karpenter) للتفاعل مع وحدة تحكم workspace. تتكامل مع واجهات برمجة تطبيقات Azure Kubernetes Service (AKS) لإضافة عقد GPU جديدة إلى مجموعة AKS.
> ملاحظة: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) هو مكون مفتوح المصدر. يمكن استبداله بوحدات تحكم أخرى إذا دعمت واجهات برمجة تطبيقات [Karpenter-core](https://sigs.k8s.io/karpenter).

## التثبيت

يرجى مراجعة إرشادات التثبيت [هنا](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## بدء سريع للاستدلال Phi-3  
[رمز العينة لاستدلال Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # ضبط مسار ACR للإخراج
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3.yaml
```
  
يمكن تتبع حالة workspace من خلال تشغيل الأمر التالي. عندما تصبح عمود WORKSPACEREADY `True`، يكون الموديل قد تم نشره بنجاح.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```
  
بعد ذلك، يمكن العثور على عنوان IP الخاص بخدمة الاستدلال في المجموعة واستخدام بود مؤقت `curl` لاختبار نقطة نهاية الخدمة في المجموعة.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```
  
## بدء سريع للاستدلال Phi-3 مع المحولات

بعد تثبيت Kaito، يمكن تجربة الأوامر التالية لبدء خدمة الاستدلال.

[رمز العينة لاستدلال Phi-3 مع المحولات](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # ضبط مسار الصوت التلقائي الناتج
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3_with_adapters.yaml
```
  
يمكن تتبع حالة workspace من خلال تشغيل الأمر التالي. عندما تصبح عمود WORKSPACEREADY `True`، يكون الموديل قد تم نشره بنجاح.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```
  
بعد ذلك، يمكن العثور على عنوان IP الخاص بخدمة الاستدلال في المجموعة واستخدام بود مؤقت `curl` لاختبار نقطة نهاية الخدمة في المجموعة.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). وبينما نسعى لتحقيق الدقة، يُرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر المعتمد والموثوق. بالنسبة للمعلومات الحساسة أو الهامة، يُنصح باستخدام ترجمة احترافية بشرية. نحن لسنا مسؤولين عن أي سوء فهم أو تفسير خاطئ ينشأ عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->