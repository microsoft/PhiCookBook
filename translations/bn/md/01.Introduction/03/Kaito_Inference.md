<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e46691923dca7cb2f11d32b1d9d558e0",
  "translation_date": "2025-07-16T20:49:00+00:00",
  "source_file": "md/01.Introduction/03/Kaito_Inference.md",
  "language_code": "bn"
}
-->
## Kaito দিয়ে ইনফারেন্স

[Kaito](https://github.com/Azure/kaito) একটি অপারেটর যা Kubernetes ক্লাস্টারে AI/ML ইনফারেন্স মডেল ডিপ্লয়মেন্ট স্বয়ংক্রিয় করে।

Kaito-এর প্রধান কিছু বৈশিষ্ট্য যা বেশিরভাগ প্রচলিত মডেল ডিপ্লয়মেন্ট পদ্ধতির থেকে আলাদা, যেগুলো ভার্চুয়াল মেশিন ইনফ্রাস্ট্রাকচারের ওপর ভিত্তি করে তৈরি:

- মডেল ফাইলগুলো কন্টেইনার ইমেজ ব্যবহার করে পরিচালনা করা হয়। মডেল লাইব্রেরি ব্যবহার করে ইনফারেন্স কল করার জন্য একটি HTTP সার্ভার প্রদান করা হয়।
- GPU হার্ডওয়্যারের সাথে খাপ খাওয়ানোর জন্য ডিপ্লয়মেন্ট প্যারামিটার টিউন করার প্রয়োজন হয় না, কারণ প্রিসেট কনফিগারেশন দেওয়া আছে।
- মডেল প্রয়োজন অনুযায়ী GPU নোড স্বয়ংক্রিয়ভাবে প্রোভিশন করা হয়।
- লাইসেন্স অনুমতি থাকলে বড় মডেল ইমেজগুলো পাবলিক Microsoft Container Registry (MCR)-তে হোস্ট করা হয়।

Kaito ব্যবহার করে Kubernetes-এ বড় AI ইনফারেন্স মডেল অনবোর্ড করার কাজ অনেক সহজ হয়ে যায়।

## আর্কিটেকচার

Kaito ক্লাসিক Kubernetes Custom Resource Definition (CRD)/controller ডিজাইন প্যাটার্ন অনুসরণ করে। ব্যবহারকারী একটি `workspace` কাস্টম রিসোর্স পরিচালনা করেন যা GPU প্রয়োজনীয়তা এবং ইনফারেন্স স্পেসিফিকেশন বর্ণনা করে। Kaito কন্ট্রোলারগুলো `workspace` কাস্টম রিসোর্সের সাথে সামঞ্জস্য রেখে ডিপ্লয়মেন্ট স্বয়ংক্রিয়ভাবে সম্পন্ন করে।

<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

উপরের চিত্রে Kaito আর্কিটেকচারের সারাংশ দেখানো হয়েছে। এর প্রধান উপাদানগুলো হলো:

- **Workspace controller**: এটি `workspace` কাস্টম রিসোর্সের সাথে সামঞ্জস্য রেখে কাজ করে, নোড স্বয়ংক্রিয় প্রোভিশনিং শুরু করার জন্য `machine` (নিচে ব্যাখ্যা করা হয়েছে) কাস্টম রিসোর্স তৈরি করে, এবং মডেলের প্রিসেট কনফিগারেশন অনুযায়ী ইনফারেন্স ওয়ার্কলোড (`deployment` বা `statefulset`) তৈরি করে।
- **Node provisioner controller**: এই কন্ট্রোলারের নাম [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner)-এ *gpu-provisioner*। এটি [Karpenter](https://sigs.k8s.io/karpenter) থেকে উদ্ভূত `machine` CRD ব্যবহার করে workspace controller-এর সাথে ইন্টারঅ্যাক্ট করে। এটি Azure Kubernetes Service (AKS) API-এর সাথে সংযুক্ত হয়ে AKS ক্লাস্টারে নতুন GPU নোড যোগ করে।
> Note: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) একটি ওপেন সোর্স কম্পোনেন্ট। যদি অন্য কোনো কন্ট্রোলার [Karpenter-core](https://sigs.k8s.io/karpenter) API সমর্থন করে, তবে সেটি দিয়ে প্রতিস্থাপন করা যেতে পারে।

## ইনস্টলেশন

ইনস্টলেশন নির্দেশিকা দেখতে [এখানে](https://github.com/Azure/kaito/blob/main/docs/installation.md) দেখুন।

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

ওয়ার্কস্পেসের স্ট্যাটাস নিচের কমান্ড চালিয়ে ট্র্যাক করা যায়। যখন WORKSPACEREADY কলাম `True` হবে, তখন মডেল সফলভাবে ডিপ্লয় হয়েছে।

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

এরপর, ইনফারেন্স সার্ভিসের ক্লাস্টার আইপি খুঁজে বের করে একটি অস্থায়ী `curl` পড ব্যবহার করে ক্লাস্টারের সার্ভিস এন্ডপয়েন্ট পরীক্ষা করা যায়।

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## অ্যাডাপ্টারসহ দ্রুত শুরু ইনফারেন্স Phi-3

Kaito ইনস্টল করার পর, নিচের কমান্ডগুলো চালিয়ে ইনফারেন্স সার্ভিস শুরু করা যেতে পারে।

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

ওয়ার্কস্পেসের স্ট্যাটাস নিচের কমান্ড চালিয়ে ট্র্যাক করা যায়। যখন WORKSPACEREADY কলাম `True` হবে, তখন মডেল সফলভাবে ডিপ্লয় হয়েছে।

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

এরপর, ইনফারেন্স সার্ভিসের ক্লাস্টার আইপি খুঁজে বের করে একটি অস্থায়ী `curl` পড ব্যবহার করে ক্লাস্টারের সার্ভিস এন্ডপয়েন্ট পরীক্ষা করা যায়।

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার নিজস্ব ভাষায়ই কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ গ্রহণ করার পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহারে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।