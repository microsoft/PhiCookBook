<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aca91084bc440431571e00bf30d96ab8",
  "translation_date": "2026-01-05T01:58:48+00:00",
  "source_file": "md/01.Introduction/03/Kaito_Inference.md",
  "language_code": "bn"
}
-->
## Kaito দিয়ে ইনফারেন্স 

[Kaito](https://github.com/Azure/kaito) হল একটি অপারেটর যা Kubernetes ক্লাস্টারে AI/ML ইনফারেন্স মডেল ডিপ্লয়মেন্ট অটোমেট করে।

Kaito-এর নিম্নলিখিত মূল পার্থক্যগুলো আছে, যা সাধারণত ভিন্ন ভার্চুয়াল মেশিন ভিত্তিক ইन्फ্রাস্ট্রাকচারের উপরে নির্মিত বেশিরভাগ মডেল ডিপ্লয়মেন্ট পদ্ধতির তুলনায় ভিন্ন:

- কন্টেইনার ইমেজ ব্যবহার করে মডেল ফাইলগুলো পরিচালনা করে। মডেল লাইব্রেরি ব্যবহার করে ইনফারেন্স কল করার জন্য একটি HTTP সার্ভার প্রদান করা হয়।
- প্রিসেট কনফিগারেশন সরবরাহ করে GPU হার্ডওয়্যারের সাথে খাপ খাওয়ানোর জন্য ডিপ্লয়মেন্ট প্যারামিটার টিউন করা এড়ায়।
- মডেলের চাহিদা অনুযায়ী GPU নোডগুলো স্বয়ংক্রিয়ভাবে প্রোভিশন করে।
- লাইসেন্স অনুমতি দিলে বড় মডেল ইমেজগুলোকে public Microsoft Container Registry (MCR)-এ হোস্ট করে।

Kaito ব্যবহার করে Kubernetes-এ বড় AI ইনফারেন্স মডেল অনবোর্ড করার ওয়ার্কফ্লো ব্যাপকভাবে সরলীকৃত হয়।


## আর্কিটেকচার

Kaito প্রচলিত Kubernetes Custom Resource Definition(CRD)/controller ডিজাইন প্যাটার্ন অনুসরণ করে। ব্যবহারকারী একটি `workspace` কাস্টম রিসোর্স পরিচালনা করে যা GPU প্রয়োজনীয়তা এবং ইনফারেন্স স্পেসিফিকেশন বর্ণনা করে। Kaito কন্ট্রোলারগুলো `workspace` কাস্টম রিসোর্সকে সমন্বয় করে ডিপ্লয়মেন্ট অটোমেট করবে।

<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/website/static/img/ragarch.png" width=80% title="KAITO RAGEngine আর্কিটেকচার" alt="KAITO RAGEngine আর্কিটেকচার">
</div>

উপরের চিত্র Kaito আর্কিটেকচারের ওভারভিউ উপস্থাপন করে। এর প্রধান উপাদানগুলো নিম্নরূপ:

- **Workspace controller**: এটি `workspace` কাস্টম রিসোর্সকে সমন্বয় করে, নোড অটো-প্রোভিশনিং ট্রিগার করার জন্য `machine` (নীচে ব্যাখ্যা করা হয়েছে) কাস্টম রিসোর্স তৈরি করে, এবং মডেল প্রিসেট কনফিগারেশনের ওপর ভিত্তি করে ইনফারেন্স ওয়ার্কলোড (`deployment` বা `statefulset`) তৈরি করে।
- **Node provisioner controller**: কন্ট্রোলারটির নাম [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner)-এ *gpu-provisioner*। এটি [Karpenter](https://sigs.k8s.io/karpenter)-থেকে উদ্ভূত `machine` CRD ব্যবহার করে workspace কন্ট্রোলারের সাথে ইন্টারঅ্যাক্ট করে। এটি Azure Kubernetes Service(AKS) APIs-এর সাথে ইন্টিগ্রেট করে AKS ক্লাস্টারে নতুন GPU নোড যোগ করে। 
> নোট: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) একটি ওপেন সোর্স উপাদান। যদি অন্যান্য কন্ট্রোলারগুলো [Karpenter-core](https://sigs.k8s.io/karpenter) APIs সাপোর্ট করে, তাহলে এটিকে প্রতিস্থাপন করা যেতে পারে।

## ইনস্টলেশন

ইনস্টলেশন নির্দেশিকা অনুগ্রহ করে [এখানে](https://github.com/Azure/kaito/blob/main/docs/installation.md) দেখুন।

## দ্রুত শুরু Inference Phi-3
[নমুনা কোড — Inference Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # আউটপুট ACR পাথ টিউন করা
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3.yaml
```

workspace স্ট্যাটাসটি নিম্নলিখিত কমান্ড চালিয়ে ট্র্যাক করা যেতে পারে। যখন WORKSPACEREADY কলামটি `True` হয়ে যায়, তখন মডেল সফলভাবে ডিপ্লয় হয়েছে।

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

পরবর্তী, কেউ ইনফারেন্স সার্ভিসের ক্লাস্টার IP খুঁজে পেয়ে ক্লাস্টারে সার্ভিস এন্ডপয়েন্ট পরীক্ষা করার জন্য একটি অস্থায়ী `curl` পড ব্যবহার করতে পারে।

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## দ্রুত শুরু Inference Phi-3 অ্যাডাপ্টারসহ

Kaito ইন্সটল করার পরে, নিম্নলিখিত কমান্ডগুলো ব্যবহার করে ইনফারেন্স সার্ভিস শুরু করতে পারেন।

[নমুনা কোড — Inference Phi-3 (অ্যাডাপ্টারসহ)](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # আউটপুট ACR পাথ টিউনিং
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3_with_adapters.yaml
```

workspace স্ট্যাটাসটি নিম্নলিখিত কমান্ড চালিয়ে ট্র্যাক করা যেতে পারে। যখন WORKSPACEREADY কলামটি `True` হয়ে যায়, তখন মডেল সফলভাবে ডিপ্লয় হয়েছে।

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

পরবর্তী, কেউ ইনফারেন্স সার্ভিসের ক্লাস্টার IP খুঁজে পেয়ে ক্লাস্টারে সার্ভিস এন্ডপয়েন্ট পরীক্ষা করার জন্য একটি অস্থায়ী `curl` পড ব্যবহার করতে পারে।

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
অস্বীকৃতি:
এই নথিটি কৃত্রিম বুদ্ধিমত্তা অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। যদিও আমরা যথার্থতার চেষ্টা করি, দয়া করে মনে রাখুন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল ভাষায় থাকা নথিকেই কর্তৃত্বপ্রাপ্ত উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের ক্ষেত্রে পেশাদার মানব অনুবাদের পরামর্শ দেওয়া হয়। এই অনুবাদ ব্যবহারের ফলে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->