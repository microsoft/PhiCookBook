<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aca91084bc440431571e00bf30d96ab8",
  "translation_date": "2026-01-04T07:18:39+00:00",
  "source_file": "md/01.Introduction/03/Kaito_Inference.md",
  "language_code": "ar"
}
-->
## الاستدلال مع Kaito 

[Kaito](https://github.com/Azure/kaito) هو مُشغّل يقوم بأتمتة نشر نماذج الاستدلال للذكاء الاصطناعي/التعلّم الآلي في عنقود Kubernetes.

Kaito يمتاز بالاختلافات الرئيسية التالية مقارنةً بمعظم منهجيات نشر النماذج السائدة المبنية على بنى تحتية من نوع الآلة الافتراضية:

- إدارة ملفات النموذج باستخدام صور الحاويات. يتم توفير خادم HTTP لتنفيذ استدعاءات الاستدلال باستخدام مكتبة النموذج.
- تجنّب ضبط معلمات النشر لتناسب أجهزة GPU من خلال توفير إعدادات مُسبقة.
- يتم توفير عُقد GPU تلقائيًا بناءً على متطلبات النموذج.
- استضافة صور النماذج الكبيرة في Microsoft Container Registry العامة (MCR) إذا سمحت الرخصة.

باستخدام Kaito، يتم تبسيط سير عمل إدخال نماذج الاستدلال الكبيرة للذكاء الاصطناعي في Kubernetes بشكل كبير.


## المعمارية

يتبع Kaito نمط التصميم الكلاسيكي لتعريف المورد المخصص (Custom Resource Definition(CRD))/وحدة التحكم في Kubernetes. يدير المستخدم موردًا مخصصًا `workspace` يصف متطلبات GPU ومواصفات الاستدلال. ستقوم وحدات التحكم في Kaito بأتمتة النشر من خلال مزامنة مورد `workspace` المخصص.

<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/website/static/img/ragarch.png" width=80% title="معمارية محرك KAITO RAG" alt="معمارية محرك KAITO RAG">
</div>

يعرض الشكل أعلاه لمحة عامة عن معمارية Kaito. تتكون مكوناته الرئيسية من:

- **وحدة تحكم Workspace**: تقوم بمزامنة مورد `workspace` المخصص، وتُنشئ موارد مخصصة `machine` (موضّح أدناه) لبدء توفير العقد تلقائيًا، وتُنشئ عبء عمل الاستدلال (`deployment` أو `statefulset`) بناءً على إعدادات النموذج المسبقة.
- **متحكم توفير العقد**: اسم المتحكم هو *gpu-provisioner* في [مخطط Helm الخاص بـ gpu-provisioner](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). يستخدم CRD `machine` المنشأ من [Karpenter](https://sigs.k8s.io/karpenter) للتفاعل مع وحدة تحكم الـ workspace. يتكامل مع واجهات برمجة تطبيقات Azure Kubernetes Service(AKS) لإضافة عُقد GPU جديدة إلى عنقود AKS. 
> ملاحظة: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) هو مكوّن مفتوح المصدر. يمكن استبداله بوحدات تحكم أخرى إذا كانت تدعم واجهات برمجة تطبيقات [Karpenter-core](https://sigs.k8s.io/karpenter).

## التثبيت

يرجى مراجعة إرشادات التثبيت [هنا](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## بداية سريعة: استدلال Phi-3
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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # مسار إخراج ضبط ACR
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3.yaml
```

يمكن تتبع حالة الـ `workspace` عن طريق تشغيل الأمر التالي. عندما يصبح عمود WORKSPACEREADY بقيمة `True`، يكون النموذج قد تم نشره بنجاح.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

بعد ذلك، يمكن العثور على عنوان IP الخاص بخدمة الاستدلال في العنقود واستخدام بود `curl` مؤقت لاختبار نقطة النهاية للخدمة داخل العنقود.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## بداية سريعة: استدلال Phi-3 مع المحولات

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # مسار ACR لإخراج الضبط
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3_with_adapters.yaml
```

يمكن تتبع حالة الـ `workspace` عن طريق تشغيل الأمر التالي. عندما يصبح عمود WORKSPACEREADY بقيمة `True`، يكون النموذج قد تم نشره بنجاح.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

بعد ذلك، يمكن العثور على عنوان IP الخاص بخدمة الاستدلال في العنقود واستخدام بود `curl` مؤقت لاختبار نقطة النهاية للخدمة داخل العنقود.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
إخلاء المسؤولية:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية Co-op Translator (https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر المرجعي والمعتمد. بالنسبة للمعلومات الحرجة، يُنصح بالاستعانة بترجمة بشرية احترافية. لا نتحمل مسؤولية أي سوء فهم أو تفسير خاطئ ينشأ عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->