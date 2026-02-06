## Kaito দিয়ে অনুমান

[Kaito](https://github.com/Azure/kaito) একটি অপারেটর যা Kubernetes ক্লাস্টারে AI/ML অনুমান মডেল ডিপ্লয়মেন্ট স্বয়ংক্রিয় করে।

Kaito এর প্রধান পার্থক্যগুলি নিম্নরূপ, যা বেশিরভাগ প্রচলিত মডেল ডিপ্লয়মেন্ট পদ্ধতির সাথে যা ভার্চুয়াল মেশিন অবকাঠামোর উপর নির্মিত:

- কনটেইনার ইমেজ ব্যবহার করে মডেল ফাইলগুলি পরিচালনা করা। মডেল লাইব্রেরি ব্যবহার করে অনুমান কল সম্পাদনের জন্য একটি HTTP সার্ভার প্রদান করা হয়।
- GPU হার্ডওয়্যারের সাথে মানিয়ে নেওয়ার জন্য ডিপ্লয়মেন্ট প্যারামিটার টিউনিং এড়ানো পূর্বনির্ধারিত কনফিগারেশন প্রদান করে।
- মডেল প্রয়োজনীয়তা অনুযায়ী স্বয়ংক্রিয়ভাবে GPU নোড প্রদান।
- লাইসেন্স অনুমতি দিলে পাবলিক Microsoft Container Registry (MCR) তে বড় মডেল ইমেজ হোস্ট করা।

Kaito ব্যবহার করে, Kubernetes এ বড় AI অনুমান মডেল অনবোর্ডিংয়ের ওয়ার্কফ্লো উল্লেখযোগ্যভাবে সহজ করা হয়েছে।

## আর্কিটেকচার

Kaito ঐতিহ্যবাহী Kubernetes কাস্টম রিসোর্স ডেফিনিশন (CRD)/controller ডিজাইন প্যাটার্ন অনুসরণ করে। ব্যবহারকারী একটি `workspace` কাস্টম রিসোর্স পরিচালনা করেন যেটি GPU প্রয়োজনীয়তা এবং অনুমান স্পেসিফিকেশন বর্ণনা করে। Kaito কন্ট্রোলারগুলি `workspace` কাস্টম রিসোর্স রিকনসাইল করে ডিপ্লয়মেন্ট স্বয়ংক্রিয় করবে।

<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/website/static/img/ragarch.png" width=80% title="KAITO RAGEngine architecture" alt="KAITO RAGEngine architecture">
</div>

উপরের চিত্রটি Kaito আর্কিটেকচার ওভারভিউ উপস্থাপন করে। এর প্রধান উপাদানগুলি হলো:

- **Workspace controller**: এটি `workspace` কাস্টম রিসোর্স রিকনসাইল করে, নোড স্বয়ংক্রিয়ভাবে প্রদান করার জন্য `machine` (নীচে ব্যাখ্যা করা হয়েছে) কাস্টম রিসোর্স তৈরি করে এবং মডেল পূর্বনির্ধারিত কনফিগারেশনের ভিত্তিতে অনুমান ওয়ার্কলোড (`deployment` বা `statefulset`) তৈরি করে।
- **Node provisioner controller**: কন্ট্রোলারের নাম [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) এ *gpu-provisioner*। এটি [Karpenter](https://sigs.k8s.io/karpenter) থেকে আগত `machine` CRD ব্যবহার করে workspace controller এর সাথে ইন্টারঅ্যাক্ট করে। এটি Azure Kubernetes Service (AKS) API এর সাথে ইন্টিগ্রেট করে AKS ক্লাস্টারে নতুন GPU নোড যুক্ত করে।
> Note: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) একটি ওপেন সোর্স উপাদান। যদি অন্য কোনো কন্ট্রোলার [Karpenter-core](https://sigs.k8s.io/karpenter) API সমর্থন করে তবে এটি দিয়ে প্রতিস্থাপন করা যেতে পারে।

## ইনস্টলেশন

অনুগ্রহ করে ইনস্টলেশন নির্দেশিকা [এখানে](https://github.com/Azure/kaito/blob/main/docs/installation.md) দেখুন।

## দ্রুত শুরু অনুমান Phi-3
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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # আউটপুট ACR পাথ টিউনিং
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3.yaml
```

নিম্নলিখিত কমান্ড চালিয়ে workspace স্ট্যাটাস ট্র্যাক করা যেতে পারে। যখন WORKSPACEREADY কলাম `True` হবে, তখন মডেল সফলভাবে ডিপ্লয় হয়েছে।

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

পরবর্তী ধাপে, অনুমান সার্ভিসের ক্লাস্টার আইপি খুঁজে বের করা যাবে এবং ক্লাস্টারের সার্ভিস এন্ডপয়েন্ট পরীক্ষা করার জন্য একটি অস্থায়ী `curl` পড ব্যবহার করা যাবে।

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## অ্যাডাপ্টার সহ দ্রুত শুরু অনুমান Phi-3

Kaito ইনস্টল করার পরে, নিম্নলিখিত কমান্ডগুলি চালিয়ে অনুমান সার্ভিস শুরু করার চেষ্টা করতে পারেন।

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # আউটপুট ACR পথ টিউন করা হচ্ছে
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3_with_adapters.yaml
```

নিম্নলিখিত কমান্ড চালিয়ে workspace স্ট্যাটাস ট্র্যাক করা যায়। যখন WORKSPACEREADY কলাম `True` হবে, তখন মডেল সফলভাবে ডিপ্লয় হয়েছে।

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

পরবর্তী ধাপে, অনুমান সার্ভিসের ক্লাস্টার আইপি খুঁজে বের করুন এবং ক্লাস্টারের সার্ভিস এন্ডপয়েন্ট পরীক্ষা করার জন্য একটি অস্থায়ী `curl` পড ব্যবহার করুন।

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**বাকস্বত্ব অ্যাপডেট**:
এই নথিটি এআই অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে স্বয়ংক্রিয় অনুবাদে ভুল বা অসঙ্গতি থাকতে পারে। মূল নথি তার নিজস্ব ভাষায়ই কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানসম্পন্ন মানুষের অনুবাদ নেওয়া সুপারিশ করা হয়। এই অনুবাদের ব্যবহারে উদ্ভূত কোন ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা কোনো দায়বদ্ধতা গ্রহণ করি না।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->