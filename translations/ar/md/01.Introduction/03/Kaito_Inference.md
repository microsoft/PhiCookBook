<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e46691923dca7cb2f11d32b1d9d558e0",
  "translation_date": "2025-03-27T07:37:50+00:00",
  "source_file": "md\\01.Introduction\\03\\Kaito_Inference.md",
  "language_code": "ar"
}
-->
## الاستنتاج باستخدام Kaito

[Kaito](https://github.com/Azure/kaito) هو مشغل يقوم بأتمتة نشر نموذج الاستنتاج AI/ML في مجموعة Kubernetes.

يمتلك Kaito الفروقات الرئيسية التالية مقارنة بمعظم منهجيات نشر النماذج السائدة المبنية على بنية تحتية تعتمد على الآلات الافتراضية:

- إدارة ملفات النماذج باستخدام صور الحاويات. يتم توفير خادم HTTP لإجراء استدعاءات الاستنتاج باستخدام مكتبة النموذج.
- تجنب ضبط معلمات النشر لتناسب أجهزة GPU من خلال توفير تكوينات مُعدة مسبقًا.
- توفير عقد GPU تلقائيًا بناءً على متطلبات النموذج.
- استضافة صور النماذج الكبيرة في سجل الحاويات العام الخاص بـ Microsoft (MCR) إذا سمح الترخيص بذلك.

باستخدام Kaito، يتم تبسيط سير العمل لتبني نماذج الاستنتاج الكبيرة للذكاء الاصطناعي في Kubernetes بشكل كبير.

## البنية المعمارية

يتبع Kaito النمط الكلاسيكي لتعريف الموارد المخصصة (CRD) في Kubernetes/نمط تصميم وحدة التحكم. يقوم المستخدم بإدارة مورد مخصص `workspace` يصف متطلبات GPU ومواصفات الاستنتاج. ستقوم وحدات تحكم Kaito بأتمتة عملية النشر من خلال مطابقة المورد المخصص `workspace`.
<div align="right">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="بنية Kaito">
</div>

تُظهر الصورة أعلاه نظرة عامة على بنية Kaito. وتتألف مكوناته الرئيسية من:

- **وحدة تحكم مساحة العمل**: تقوم بمطابقة المورد المخصص `workspace`، وتُنشئ موارد مخصصة `machine` (موضحة أدناه) لتفعيل التوفير التلقائي للعقد، وتُنشئ عبء العمل الخاص بالاستنتاج (`deployment` أو `statefulset`) بناءً على التكوينات المُعدة مسبقًا للنموذج.
- **وحدة تحكم توفير العقد**: اسم وحدة التحكم هو *gpu-provisioner* في [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). تستخدم CRD `machine` التي نشأت من [Karpenter](https://sigs.k8s.io/karpenter) للتفاعل مع وحدة تحكم مساحة العمل. تتكامل مع واجهات برمجة التطبيقات الخاصة بـ Azure Kubernetes Service (AKS) لإضافة عقد GPU جديدة إلى مجموعة AKS.
> ملاحظة: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) هو مكون مفتوح المصدر. يمكن استبداله بوحدات تحكم أخرى إذا كانت تدعم واجهات برمجة التطبيقات الخاصة بـ [Karpenter-core](https://sigs.k8s.io/karpenter).

## التثبيت

يرجى الاطلاع على إرشادات التثبيت [هنا](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## بدء سريع لاستنتاج Phi-3
[كود استنتاج Phi-3 التجريبي](https://github.com/Azure/kaito/tree/main/examples/inference)

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

يمكن تتبع حالة مساحة العمل عن طريق تشغيل الأمر التالي. عندما تصبح قيمة العمود WORKSPACEREADY هي `True`، فهذا يعني أن النموذج قد تم نشره بنجاح.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

بعد ذلك، يمكن العثور على عنوان IP الخاص بخدمة الاستنتاج واستخدام حاوية `curl` مؤقتة لاختبار نقطة النهاية للخدمة في المجموعة.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## بدء سريع لاستنتاج Phi-3 باستخدام Adapters

بعد تثبيت Kaito، يمكن تجربة الأوامر التالية لبدء خدمة استنتاج.

[كود استنتاج Phi-3 التجريبي باستخدام Adapters](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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

يمكن تتبع حالة مساحة العمل عن طريق تشغيل الأمر التالي. عندما تصبح قيمة العمود WORKSPACEREADY هي `True`، فهذا يعني أن النموذج قد تم نشره بنجاح.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

بعد ذلك، يمكن العثور على عنوان IP الخاص بخدمة الاستنتاج واستخدام حاوية `curl` مؤقتة لاختبار نقطة النهاية للخدمة في المجموعة.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**إخلاء المسؤولية**:  
تم ترجمة هذه الوثيقة باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يُرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار الوثيقة الأصلية بلغتها الأصلية المصدر الموثوق. للحصول على معلومات مهمة، يُوصى باستخدام ترجمة بشرية احترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة تنشأ عن استخدام هذه الترجمة.