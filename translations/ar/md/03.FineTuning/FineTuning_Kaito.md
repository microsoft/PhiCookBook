<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a1c62bf7d86d6186bf8d3917196a92a0",
  "translation_date": "2025-03-27T13:53:41+00:00",
  "source_file": "md\\03.FineTuning\\FineTuning_Kaito.md",
  "language_code": "ar"
}
-->
## تحسين الأداء باستخدام Kaito

[Kaito](https://github.com/Azure/kaito) هو مشغل يقوم بأتمتة نشر نماذج الاستدلال للذكاء الاصطناعي/تعلم الآلة في مجموعة Kubernetes.

يتميز Kaito بعدة فروقات رئيسية مقارنة بمعظم منهجيات نشر النماذج الشائعة المبنية على بنية تحتية تعتمد على الأجهزة الافتراضية:

- إدارة ملفات النماذج باستخدام صور الحاويات. يتم توفير خادم HTTP لإجراء مكالمات الاستدلال باستخدام مكتبة النماذج.
- تجنب ضبط معلمات النشر لتناسب أجهزة GPU من خلال توفير إعدادات مسبقة.
- توفير عقد GPU تلقائيًا بناءً على متطلبات النماذج.
- استضافة صور النماذج الكبيرة في سجل الحاويات العام الخاص بـ Microsoft (MCR) إذا سمحت الرخصة بذلك.

باستخدام Kaito، يتم تبسيط سير العمل لتضمين نماذج استدلال الذكاء الاصطناعي الكبيرة في Kubernetes بشكل كبير.

## الهندسة المعمارية

يتبع Kaito نمط تصميم Kubernetes الكلاسيكي باستخدام تعريف الموارد المخصصة (CRD) والمتحكم. يقوم المستخدم بإدارة مورد مخصص `workspace` يصف متطلبات GPU ومواصفات الاستدلال. سيقوم متحكمو Kaito بأتمتة عملية النشر من خلال مطابقة المورد المخصص `workspace`.

<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

الصورة أعلاه تعرض نظرة عامة على هندسة Kaito. تتكون مكوناته الرئيسية من:

- **متحكم مساحة العمل**: يقوم بمطابقة المورد المخصص `workspace`، وإنشاء موارد مخصصة `machine` (موضحة أدناه) لتفعيل توفير العقد تلقائيًا، وإنشاء عبء العمل للاستدلال (`deployment` أو `statefulset`) بناءً على إعدادات النماذج المسبقة.
- **متحكم توفير العقد**: يُعرف اسم هذا المتحكم بـ *gpu-provisioner* في [مخطط gpu-provisioner الخاص بـ helm](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). يستخدم CRD `machine` المأخوذ من [Karpenter](https://sigs.k8s.io/karpenter) للتفاعل مع متحكم مساحة العمل. يتكامل مع واجهات برمجة التطبيقات الخاصة بـ Azure Kubernetes Service (AKS) لإضافة عقد GPU جديدة إلى مجموعة AKS.  
> ملاحظة: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) هو مكون مفتوح المصدر. يمكن استبداله بمتَحكمين آخرين إذا كانوا يدعمون واجهات برمجة التطبيقات الخاصة بـ [Karpenter-core](https://sigs.k8s.io/karpenter).

## فيديو تعريفي
[شاهد عرض Kaito](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)

## التثبيت

يرجى مراجعة إرشادات التثبيت [هنا](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## البدء السريع

بعد تثبيت Kaito، يمكن تجربة الأوامر التالية لبدء خدمة تحسين الأداء.

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

يمكن تتبع حالة مساحة العمل عن طريق تشغيل الأمر التالي. عندما تصبح قيمة العمود WORKSPACEREADY هي `True`، فهذا يعني أن النموذج قد تم نشره بنجاح.

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

بعد ذلك، يمكن العثور على عنوان IP الخاص بخدمة الاستدلال واستخدام بود `curl` مؤقت لاختبار نقطة النهاية للخدمة داخل المجموعة.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**إخلاء المسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يُرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو معلومات غير دقيقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق. للحصول على معلومات حساسة، يُوصى بالترجمة البشرية الاحترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة ناتجة عن استخدام هذه الترجمة.