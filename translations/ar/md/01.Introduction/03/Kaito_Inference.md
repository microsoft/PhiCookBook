<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e46691923dca7cb2f11d32b1d9d558e0",
  "translation_date": "2025-07-16T20:47:21+00:00",
  "source_file": "md/01.Introduction/03/Kaito_Inference.md",
  "language_code": "ar"
}
-->
## الاستدلال مع Kaito

[Kaito](https://github.com/Azure/kaito) هو مشغل يقوم بأتمتة نشر نماذج الاستدلال في الذكاء الاصطناعي/التعلم الآلي داخل عنقود Kubernetes.

يمتاز Kaito بالميزات التالية مقارنة بمعظم طرق نشر النماذج الشائعة المبنية على بنى الآلات الافتراضية:

- إدارة ملفات النماذج باستخدام صور الحاويات. يتم توفير خادم http لإجراء استدعاءات الاستدلال باستخدام مكتبة النموذج.
- تجنب ضبط معلمات النشر لتناسب أجهزة GPU من خلال توفير إعدادات مسبقة.
- توفير عقد GPU تلقائيًا بناءً على متطلبات النموذج.
- استضافة صور النماذج الكبيرة في سجل الحاويات العام لمايكروسوفت (MCR) إذا سمحت الرخصة بذلك.

باستخدام Kaito، يتم تبسيط سير العمل الخاص بإدخال نماذج استدلال الذكاء الاصطناعي الكبيرة في Kubernetes بشكل كبير.

## البنية المعمارية

يتبع Kaito نمط تصميم تعريف الموارد المخصصة (CRD) / المتحكم الكلاسيكي في Kubernetes. يدير المستخدم موردًا مخصصًا يسمى `workspace` يصف متطلبات GPU ومواصفات الاستدلال. يقوم متحكمو Kaito بأتمتة النشر من خلال التوفيق بين مورد `workspace` المخصص.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

تعرض الصورة أعلاه نظرة عامة على بنية Kaito. وتتكون مكوناته الرئيسية من:

- **متحكم workspace**: يقوم بتوفيق مورد `workspace` المخصص، وينشئ موارد مخصصة `machine` (موضحة أدناه) لتحفيز توفير العقد تلقائيًا، وينشئ عبء عمل الاستدلال (`deployment` أو `statefulset`) بناءً على إعدادات النموذج المسبقة.
- **متحكم توفير العقد**: اسم المتحكم هو *gpu-provisioner* في [مخطط helm الخاص بـ gpu-provisioner](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). يستخدم CRD الخاص بـ `machine` المستمد من [Karpenter](https://sigs.k8s.io/karpenter) للتفاعل مع متحكم workspace. يتكامل مع واجهات برمجة تطبيقات Azure Kubernetes Service (AKS) لإضافة عقد GPU جديدة إلى عنقود AKS.
> ملاحظة: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) هو مكون مفتوح المصدر. يمكن استبداله بمتحكمات أخرى إذا كانت تدعم واجهات برمجة تطبيقات [Karpenter-core](https://sigs.k8s.io/karpenter).

## التثبيت

يرجى مراجعة إرشادات التثبيت [هنا](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## بدء سريع لاستدلال Phi-3
[كود عينة لاستدلال Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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

يمكن تتبع حالة workspace بتنفيذ الأمر التالي. عندما تصبح قيمة العمود WORKSPACEREADY `True`، يكون النموذج قد تم نشره بنجاح.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

بعد ذلك، يمكن العثور على عنوان IP الخاص بخدمة الاستدلال في العنقود واستخدام بود `curl` مؤقت لاختبار نقطة نهاية الخدمة داخل العنقود.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## بدء سريع لاستدلال Phi-3 مع المحولات

بعد تثبيت Kaito، يمكن تجربة الأوامر التالية لبدء خدمة استدلال.

[كود عينة لاستدلال Phi-3 مع المحولات](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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

يمكن تتبع حالة workspace بتنفيذ الأمر التالي. عندما تصبح قيمة العمود WORKSPACEREADY `True`، يكون النموذج قد تم نشره بنجاح.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

بعد ذلك، يمكن العثور على عنوان IP الخاص بخدمة الاستدلال في العنقود واستخدام بود `curl` مؤقت لاختبار نقطة نهاية الخدمة داخل العنقود.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**إخلاء المسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق به. للمعلومات الهامة، يُنصح بالاعتماد على الترجمة البشرية المهنية. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.