<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e46691923dca7cb2f11d32b1d9d558e0",
  "translation_date": "2025-05-09T11:57:00+00:00",
  "source_file": "md/01.Introduction/03/Kaito_Inference.md",
  "language_code": "ms"
}
-->
## Inference with Kaito 

[Kaito](https://github.com/Azure/kaito) هو أوبريتور يقوم بأتمتة نشر نماذج الاستدلال AI/ML في عنقود Kubernetes.

يمتاز Kaito بالميزات التالية مقارنة بمعظم طرق نشر النماذج التقليدية المبنية على بنى الأجهزة الافتراضية:

- إدارة ملفات النماذج باستخدام صور الحاويات. يتم توفير خادم http لتنفيذ استدعاءات الاستدلال باستخدام مكتبة النموذج.
- تجنب تعديل معلمات النشر لتناسب أجهزة GPU من خلال توفير إعدادات مسبقة.
- توفير عقد GPU تلقائيًا بناءً على متطلبات النموذج.
- استضافة صور النماذج الكبيرة في سجل الحاويات العام لمايكروسوفت (MCR) إذا سمحت الرخصة.

باستخدام Kaito، يتم تبسيط سير العمل الخاص بإضافة نماذج استدلال AI كبيرة في Kubernetes بشكل كبير.


## Architecture

يتبع Kaito نمط التصميم الكلاسيكي لتعريف الموارد المخصصة (CRD)/المتحكم في Kubernetes. يدير المستخدم موردًا مخصصًا `workspace` يصف متطلبات GPU ومواصفات الاستدلال. يقوم متحكم Kaito بأتمتة النشر عن طريق التوفيق بين مورد `workspace` المخصص.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

الشكل أعلاه يعرض نظرة عامة على بنية Kaito. مكوناته الرئيسية تتضمن:

- **Workspace controller**: يقوم بتوفيق مورد `workspace` المخصص، ينشئ موارد مخصصة `machine` (مشروحة أدناه) لتحفيز التوفير التلقائي للعقد، وينشئ عبء عمل الاستدلال (`deployment` أو `statefulset`) بناءً على إعدادات النموذج المسبقة.
- **Node provisioner controller**: اسم المتحكم هو *gpu-provisioner* في [مخطط helm الخاص بـ gpu-provisioner](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). يستخدم CRD `machine` القادم من [Karpenter](https://sigs.k8s.io/karpenter) للتفاعل مع متحكم workspace. يتكامل مع واجهات برمجة تطبيقات Azure Kubernetes Service (AKS) لإضافة عقد GPU جديدة إلى عنقود AKS. 
> ملاحظة: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) هو مكون مفتوح المصدر. يمكن استبداله بمتحكمات أخرى إذا دعمت واجهات برمجة تطبيقات [Karpenter-core](https://sigs.k8s.io/karpenter).

## Installation

يرجى مراجعة إرشادات التثبيت [هنا](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Quick start Inference Phi-3
[رمز العينة Inference Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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

يمكن تتبع حالة workspace بتشغيل الأمر التالي. عندما يصبح عمود WORKSPACEREADY على `True`، يكون النموذج قد تم نشره بنجاح.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

بعد ذلك، يمكن العثور على IP العنقود الخاص بخدمة الاستدلال واستخدام بود `curl` مؤقت لاختبار نقطة نهاية الخدمة داخل العنقود.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Quick start Inference Phi-3 with adapters

بعد تثبيت Kaito، يمكن تجربة الأوامر التالية لبدء خدمة استدلال.

[رمز العينة Inference Phi-3 مع Adapters](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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

يمكن تتبع حالة workspace بتشغيل الأمر التالي. عندما يصبح عمود WORKSPACEREADY على `True`، يكون النموذج قد تم نشره بنجاح.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

بعد ذلك، يمكن العثور على IP العنقود الخاص بخدمة الاستدلال واستخدام بود `curl` مؤقت لاختبار نقطة نهاية الخدمة داخل العنقود.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau tafsiran yang timbul daripada penggunaan terjemahan ini.