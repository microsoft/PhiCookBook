## الضبط الدقيق مع Kaito

[Kaito](https://github.com/Azure/kaito) هو أوبريتور يقوم بأتمتة نشر نماذج الاستدلال في الذكاء الاصطناعي/التعلم الآلي داخل عنقود Kubernetes.

يمتاز Kaito بالنقاط التالية مقارنة بمعظم طرق نشر النماذج الشائعة المبنية على بنى تحتية للآلات الافتراضية:

- إدارة ملفات النماذج باستخدام صور الحاويات. يتم توفير خادم http لتنفيذ استدعاءات الاستدلال باستخدام مكتبة النموذج.
- تجنب ضبط معلمات النشر لتناسب عتاد GPU من خلال توفير إعدادات مسبقة.
- توفير عقد GPU تلقائيًا بناءً على متطلبات النموذج.
- استضافة صور النماذج الكبيرة في سجل الحاويات العام لمايكروسوفت (MCR) إذا سمحت الرخصة بذلك.

باستخدام Kaito، يتم تبسيط سير العمل الخاص بإدخال نماذج استدلال الذكاء الاصطناعي الكبيرة في Kubernetes بشكل كبير.

## البنية المعمارية

يتبع Kaito نمط تصميم تعريف الموارد المخصصة (CRD) / المتحكم الكلاسيكي في Kubernetes. يدير المستخدم موردًا مخصصًا يسمى `workspace` يصف متطلبات GPU ومواصفات الاستدلال. يقوم متحكمو Kaito بأتمتة النشر من خلال التوفيق بين مورد `workspace` المخصص.

<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

الشكل أعلاه يعرض نظرة عامة على بنية Kaito. مكوناته الرئيسية تتضمن:

- **متحكم workspace**: يقوم بتوفيق مورد `workspace` المخصص، وينشئ موارد مخصصة `machine` (موضحة أدناه) لتحفيز توفير العقد تلقائيًا، وينشئ عبء عمل الاستدلال (`deployment` أو `statefulset`) بناءً على إعدادات النموذج المسبقة.
- **متحكم توفير العقد**: اسم المتحكم هو *gpu-provisioner* في [مخطط helm الخاص بـ gpu-provisioner](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). يستخدم CRD الخاص بـ `machine` المستمد من [Karpenter](https://sigs.k8s.io/karpenter) للتفاعل مع متحكم workspace. يتكامل مع واجهات برمجة تطبيقات Azure Kubernetes Service (AKS) لإضافة عقد GPU جديدة إلى عنقود AKS.
> ملاحظة: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) هو مكون مفتوح المصدر. يمكن استبداله بمتحكمات أخرى إذا كانت تدعم واجهات برمجة تطبيقات [Karpenter-core](https://sigs.k8s.io/karpenter).

## فيديو نظرة عامة  
[شاهد عرض Kaito التوضيحي](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)

## التثبيت

يرجى مراجعة إرشادات التثبيت [هنا](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## البداية السريعة

بعد تثبيت Kaito، يمكن تجربة الأوامر التالية لبدء خدمة الضبط الدقيق.

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

يمكن تتبع حالة workspace عبر تشغيل الأمر التالي. عندما تصبح قيمة عمود WORKSPACEREADY هي `True`، يكون النموذج قد تم نشره بنجاح.

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

بعد ذلك، يمكن العثور على عنوان IP الخاص بخدمة الاستدلال في العنقود واستخدام بود `curl` مؤقت لاختبار نقطة نهاية الخدمة داخل العنقود.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**إخلاء المسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق به. للمعلومات الهامة، يُنصح بالاعتماد على الترجمة البشرية المهنية. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.