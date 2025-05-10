<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e46691923dca7cb2f11d32b1d9d558e0",
  "translation_date": "2025-05-09T11:47:51+00:00",
  "source_file": "md/01.Introduction/03/Kaito_Inference.md",
  "language_code": "bn"
}
-->
## Kaito দিয়ে ইনফারেন্স

[Kaito](https://github.com/Azure/kaito) হলো একটি অপারেটর যা Kubernetes ক্লাস্টারে AI/ML ইনফারেন্স মডেল ডিপ্লয়মেন্ট স্বয়ংক্রিয় করে।

Kaito-এর মূল পার্থক্যগুলো বেশিরভাগ প্রচলিত মডেল ডিপ্লয়মেন্ট পদ্ধতির তুলনায়, যা ভার্চুয়াল মেশিন অবকাঠামোর উপর নির্মিত:

- মডেল ফাইলগুলো কন্টেইনার ইমেজের মাধ্যমে পরিচালনা করা হয়। মডেল লাইব্রেরি ব্যবহার করে ইনফারেন্স কল করার জন্য একটি HTTP সার্ভার প্রদান করা হয়।
- GPU হার্ডওয়্যারের সাথে মানিয়ে নেওয়ার জন্য ডিপ্লয়মেন্ট প্যারামিটার টিউনিং এড়ানো হয়, পূর্বনির্ধারিত কনফিগারেশন সরবরাহ করে।
- মডেল প্রয়োজন অনুযায়ী GPU নোড স্বয়ংক্রিয়ভাবে প্রোভিশন করা হয়।
- লাইসেন্স অনুমতি দিলে বড় মডেল ইমেজগুলো Microsoft Container Registry (MCR) তে হোস্ট করা হয়।

Kaito ব্যবহার করে, Kubernetes-এ বড় AI ইনফারেন্স মডেল অনবোর্ড করার ওয়ার্কফ্লো অনেক সহজ হয়।

## আর্কিটেকচার

Kaito ক্লাসিক Kubernetes Custom Resource Definition(CRD)/controller ডিজাইন প্যাটার্ন অনুসরণ করে। ইউজার একটি `workspace` কাস্টম রিসোর্স পরিচালনা করেন যা GPU প্রয়োজনীয়তা এবং ইনফারেন্স স্পেসিফিকেশন বর্ণনা করে। Kaito কন্ট্রোলারগুলো `workspace` কাস্টম রিসোর্স রিকনসাইল করে ডিপ্লয়মেন্ট স্বয়ংক্রিয় করবে।
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

উপরের চিত্রে Kaito আর্কিটেকচারের ওভারভিউ দেখানো হয়েছে। এর প্রধান উপাদানগুলো হলো:

- **Workspace controller**: এটি `workspace` কাস্টম রিসোর্স রিকনসাইল করে, নোড অটো প্রোভিশনিং ট্রিগার করার জন্য `machine` (নীচে ব্যাখ্যা করা হয়েছে) কাস্টম রিসোর্স তৈরি করে, এবং মডেলের পূর্বনির্ধারিত কনফিগারেশনের উপর ভিত্তি করে ইনফারেন্স ওয়ার্কলোড (`deployment` বা `statefulset`) তৈরি করে।
- **Node provisioner controller**: এই কন্ট্রোলারের নাম [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner)-এ *gpu-provisioner*। এটি [Karpenter](https://sigs.k8s.io/karpenter) থেকে আগত `machine` CRD ব্যবহার করে workspace controller-এর সাথে ইন্টারঅ্যাক্ট করে। এটি Azure Kubernetes Service (AKS) API-এর সাথে ইন্টিগ্রেট করে AKS ক্লাস্টারে নতুন GPU নোড যোগ করে।
> Note: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) একটি ওপেন সোর্স উপাদান। যদি অন্য কন্ট্রোলারগুলো [Karpenter-core](https://sigs.k8s.io/karpenter) API সমর্থন করে, তাহলে সেগুলো দিয়ে প্রতিস্থাপন করা যেতে পারে।

## ইনস্টলেশন

ইনস্টলেশন নির্দেশিকা দেখতে [এখানে](https://github.com/Azure/kaito/blob/main/docs/installation.md) ক্লিক করুন।

## দ্রুত শুরু ইনফারেন্স Phi-3
[Sample Code Inference Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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

ওয়ার্কস্পেসের স্ট্যাটাস ট্র্যাক করতে নিচের কমান্ডটি চালান। যখন WORKSPACEREADY কলামটি `True` হবে, তখন মডেল সফলভাবে ডিপ্লয় হয়েছে।

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

এরপর, ইনফারেন্স সার্ভিসের ক্লাস্টার আইপি খুঁজে বের করে একটি অস্থায়ী `curl` পড ব্যবহার করে ক্লাস্টারের সার্ভিস এন্ডপয়েন্ট পরীক্ষা করা যেতে পারে।

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## দ্রুত শুরু ইনফারেন্স Phi-3 অ্যাডাপ্টারসহ

Kaito ইনস্টল করার পর, নিচের কমান্ডগুলো চালিয়ে ইনফারেন্স সার্ভিস শুরু করতে পারেন।

[Sample Code Inference Phi-3 with Adapters](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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

ওয়ার্কস্পেসের স্ট্যাটাস ট্র্যাক করতে নিচের কমান্ডটি চালান। যখন WORKSPACEREADY কলামটি `True` হবে, তখন মডেল সফলভাবে ডিপ্লয় হয়েছে।

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

এরপর, ইনফারেন্স সার্ভিসের ক্লাস্টার আইপি খুঁজে বের করে একটি অস্থায়ী `curl` পড ব্যবহার করে ক্লাস্টারের সার্ভিস এন্ডপয়েন্ট পরীক্ষা করা যেতে পারে।

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**অস্বীকারোক্তি**:  
এই ডকুমেন্টটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে দয়া করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ভুল বা অসঙ্গতি থাকতে পারে। মূল ডকুমেন্টটি তার স্বাভাবিক ভাষায় কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদের পরামর্শ দেওয়া হয়। এই অনুবাদ ব্যবহারের ফলে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।