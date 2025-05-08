<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e46691923dca7cb2f11d32b1d9d558e0",
  "translation_date": "2025-05-08T05:59:10+00:00",
  "source_file": "md/01.Introduction/03/Kaito_Inference.md",
  "language_code": "hi"
}
-->
## Kaito के साथ Inference

[Kaito](https://github.com/Azure/kaito) एक ऑपरेटर है जो Kubernetes क्लस्टर में AI/ML inference मॉडल डिप्लॉयमेंट को स्वचालित करता है।

Kaito के पास वर्चुअल मशीन इन्फ्रास्ट्रक्चर पर आधारित अधिकांश मुख्यधारा के मॉडल डिप्लॉयमेंट तरीकों की तुलना में निम्नलिखित प्रमुख विशेषताएं हैं:

- कंटेनर इमेजेज़ का उपयोग करके मॉडल फाइलों का प्रबंधन। मॉडल लाइब्रेरी का उपयोग करके inference कॉल करने के लिए एक http सर्वर प्रदान किया जाता है।
- GPU हार्डवेयर के अनुसार डिप्लॉयमेंट पैरामीटर ट्यूनिंग से बचने के लिए प्रीसेट कॉन्फ़िगरेशन प्रदान करना।
- मॉडल आवश्यकताओं के आधार पर GPU नोड्स का ऑटो-प्रावधान।
- यदि लाइसेंस अनुमति देता है, तो बड़े मॉडल इमेजेस को सार्वजनिक Microsoft Container Registry (MCR) में होस्ट करना।

Kaito का उपयोग करके, Kubernetes में बड़े AI inference मॉडल को ऑनबोर्ड करने का वर्कफ़्लो काफी सरल हो जाता है।

## आर्किटेक्चर

Kaito क्लासिक Kubernetes Custom Resource Definition(CRD)/controller डिज़ाइन पैटर्न का पालन करता है। उपयोगकर्ता एक `workspace` कस्टम रिसोर्स का प्रबंधन करता है जो GPU आवश्यकताओं और inference विनिर्देश को वर्णित करता है। Kaito कंट्रोलर्स `workspace` कस्टम रिसोर्स को reconcile करके डिप्लॉयमेंट को स्वचालित करेंगे।
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

ऊपर दिया गया चित्र Kaito आर्किटेक्चर का अवलोकन प्रस्तुत करता है। इसके मुख्य घटक हैं:

- **Workspace controller**: यह `workspace` कस्टम रिसोर्स को reconcile करता है, नोड ऑटो प्राविजनिंग को ट्रिगर करने के लिए `machine` (नीचे समझाया गया) कस्टम रिसोर्स बनाता है, और मॉडल प्रीसेट कॉन्फ़िगरेशन के आधार पर inference वर्कलोड (`deployment` या `statefulset`) बनाता है।
- **Node provisioner controller**: इस कंट्रोलर का नाम [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) में *gpu-provisioner* है। यह [Karpenter](https://sigs.k8s.io/karpenter) से उत्पन्न `machine` CRD का उपयोग करके workspace controller के साथ इंटरैक्ट करता है। यह Azure Kubernetes Service(AKS) APIs के साथ एकीकृत होकर AKS क्लस्टर में नए GPU नोड्स जोड़ता है।
> Note: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) एक ओपन सोर्स कंपोनेंट है। इसे अन्य कंट्रोलर्स से बदला जा सकता है यदि वे [Karpenter-core](https://sigs.k8s.io/karpenter) APIs का समर्थन करते हैं।

## इंस्टॉलेशन

कृपया इंस्टॉलेशन निर्देश [यहाँ](https://github.com/Azure/kaito/blob/main/docs/installation.md) देखें।

## Quick start Inference Phi-3
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

वर्कस्पेस की स्थिति को निम्नलिखित कमांड चलाकर ट्रैक किया जा सकता है। जब WORKSPACEREADY कॉलम `True` हो जाता है, तो मॉडल सफलतापूर्वक डिप्लॉय हो चुका होता है।

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

इसके बाद, आप inference सेवा का क्लस्टर IP पा सकते हैं और क्लस्टर में सेवा एन्डपॉइंट का परीक्षण करने के लिए एक अस्थायी `curl` पॉड का उपयोग कर सकते हैं।

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Quick start Inference Phi-3 with adapters

Kaito इंस्टॉल करने के बाद, आप निम्नलिखित कमांड्स का उपयोग करके inference सेवा शुरू कर सकते हैं।

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

वर्कस्पेस की स्थिति को निम्नलिखित कमांड चलाकर ट्रैक किया जा सकता है। जब WORKSPACEREADY कॉलम `True` हो जाता है, तो मॉडल सफलतापूर्वक डिप्लॉय हो चुका होता है।

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

इसके बाद, आप inference सेवा का क्लस्टर IP पा सकते हैं और क्लस्टर में सेवा एन्डपॉइंट का परीक्षण करने के लिए एक अस्थायी `curl` पॉड का उपयोग कर सकते हैं।

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। हम सटीकता के लिए प्रयासरत हैं, लेकिन कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या गलतियाँ हो सकती हैं। मूल दस्तावेज़ उसकी मूल भाषा में प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।