<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aca91084bc440431571e00bf30d96ab8",
  "translation_date": "2026-01-05T01:43:43+00:00",
  "source_file": "md/01.Introduction/03/Kaito_Inference.md",
  "language_code": "hi"
}
-->
## Kaito के साथ इन्फ़ेरेंस 

[Kaito](https://github.com/Azure/kaito) Kubernetes क्लस्टर में AI/ML इन्फ़ेरेंस मॉडल तैनाती को स्वचालित करने वाला एक ऑपरेटर है।

Kaito के पास वर्चुअल मशीन इन्फ्रास्ट्रक्चर पर बने अधिकांश प्रमुख मॉडल तैनाती विधियों की तुलना में निम्नलिखित मुख्य भिन्नताएँ हैं:

- मॉडल फ़ाइलों का प्रबंधन कंटेनर इमेजेज़ का उपयोग करके करता है। मॉडल लाइब्रेरी का उपयोग करके इन्फ़ेरेंस कॉल करने के लिए एक http सर्वर प्रदान किया जाता है।
- प्रिसेट कॉन्फ़िगरेशन प्रदान करके GPU हार्डवेयर के अनुरूप तैनाती पैरामीटर को समायोजित करने से बचाता है।
- मॉडल आवश्यकताओं के आधार पर GPU नोड्स को स्वचालित रूप से प्रोविज़न करता है।
- यदि लाइसेंस अनुमति देता है तो बड़े मॉडल इमेजेज़ को सार्वजनिक Microsoft Container Registry (MCR) में होस्ट करता है।

Kaito का उपयोग करके, Kubernetes में बड़े AI इन्फ़ेरेंस मॉडलों को ऑनबोर्ड करने का कार्यप्रवाह काफी सरल हो जाता है।


## आर्किटेक्चर

Kaito क्लासिक Kubernetes Custom Resource Definition(CRD)/controller डिज़ाइन पैटर्न का पालन करता है। उपयोगकर्ता एक `workspace` कस्टम रिसोर्स का प्रबंधन करता है जो GPU आवश्यकताओं और इन्फ़ेरेंस विनिर्देश को दर्शाता है। Kaito कंट्रोलर `workspace` कस्टम रिसोर्स को मेल बैठाकर तैनाती को स्वचालित करेंगे।

<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/website/static/img/ragarch.png" width=80% title="KAITO RAGEngine आर्किटेक्चर" alt="KAITO RAGEngine आर्किटेक्चर">
</div>

ऊपर का चित्र Kaito आर्किटेक्चर का अवलोकन प्रस्तुत करता है। इसके प्रमुख घटक निम्न हैं:

- **Workspace controller**: यह `workspace` कस्टम रिसोर्स को मेल बैठाता है, नोड ऑटो प्रोविज़निंग ट्रिगर करने के लिए `machine` (नीचे समझाया गया) कस्टम रिसोर्स बनाता है, और मॉडल प्रीसेट कॉन्फ़िगरेशन के आधार पर इन्फ़ेरेंस वर्कलोड (`deployment` या `statefulset`) बनाता है।
- **Node provisioner controller**: कंट्रोलर का नाम [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) में *gpu-provisioner* है। यह workspace कंट्रोलर के साथ इंटरैक्ट करने के लिए [Karpenter](https://sigs.k8s.io/karpenter) से उत्पन्न `machine` CRD का उपयोग करता है। यह Azure Kubernetes Service(AKS) APIs के साथ एकीकृत होकर AKS क्लस्टर में नए GPU नोड्स जोड़ता है। 
> नोट: यह [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) एक ओपन-सोर्स कंपोनेंट है। यदि अन्य कंट्रोलर [Karpenter-core](https://sigs.k8s.io/karpenter) APIs का समर्थन करते हैं तो इसे प्रतिस्थापित किया जा सकता है।

## इंस्टॉलेशन

कृपया इंस्टॉलेशन मार्गदर्शन [यहाँ](https://github.com/Azure/kaito/blob/main/docs/installation.md) देखें।

## क्विक स्टार्ट: इनफ़ेरेंस Phi-3
[इनफ़ेरेंस Phi-3 का नमूना कोड](https://github.com/Azure/kaito/tree/main/examples/inference)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # ट्यूनिंग आउटपुट ACR पथ
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3.yaml
```

वर्कस्पेस की स्थिति को निम्नलिखित कमांड चलाकर ट्रैक किया जा सकता है। जब WORKSPACEREADY कॉलम `True` हो जाता है, तब मॉडल सफलतापूर्वक तैनात हो चुका है।

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

अगला, कोई इन्फ़ेरेंस सर्विस का क्लस्टर ip ढूंढ सकता है और क्लस्टर में सेवा एंडपॉइंट का परीक्षण करने के लिए एक अस्थायी `curl` पोड का उपयोग कर सकता है।

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## एडाप्टर्स के साथ क्विक स्टार्ट: इनफ़ेरेंस Phi-3

Kaito इंस्टॉल करने के बाद, कोई निम्नलिखित कमांड्स आज़मा कर एक इन्फ़ेरेंस सर्विस शुरू कर सकता है।

[एडाप्टर्स के साथ इनफ़ेरेंस Phi-3 का नमूना कोड](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # ट्यूनिंग आउटपुट ACR पथ
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3_with_adapters.yaml
```

वर्कस्पेस की स्थिति को निम्नलिखित कमांड चलाकर ट्रैक किया जा सकता है। जब WORKSPACEREADY कॉलम `True` हो जाता है, तब मॉडल सफलतापूर्वक तैनात हो चुका है।

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

अगला, कोई इन्फ़ेरेंस सर्विस का क्लस्टर ip ढूंढ सकता है और क्लस्टर में सेवा एंडपॉइंट का परीक्षण करने के लिए एक अस्थायी `curl` पोड का उपयोग कर सकता है।

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
अस्वीकरण:
यह दस्तावेज़ एआई अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या असंगतताएँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में अधिकृत स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->