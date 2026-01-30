## Kaito के साथ अनुमान

[Kaito](https://github.com/Azure/kaito) एक ऑपरेटर है जो Kubernetes क्लस्टर में AI/ML अनुमान मॉडल तैनाती को स्वचालित करता है।

Kaito के पास अधिकांश मुख्यधारा के मॉडल तैनाती विधियों की तुलना में जो वर्चुअल मशीन इन्फ्रास्ट्रक्चर पर निर्मित हैं, निम्नलिखित प्रमुख अंतर हैं:

- मॉडल फ़ाइलों को कंटेनर छवियों का उपयोग करके प्रबंधित करें। मॉडल पुस्तकालय का उपयोग करके अनुमान कॉल करने के लिए एक http सर्वर प्रदान किया गया है।
- GPU हार्डवेयर के अनुरूप तैनाती पैरामीटर ट्यूनिंग से बचने के लिए पूर्व निर्धारित कॉन्फ़िगरेशन प्रदान करें।
- मॉडल आवश्यकताओं के अनुसार GPU नोड्स का स्वचालित प्रावधान करें।
- यदि लाइसेंस अनुमति देता है, तो बड़े मॉडल छवियों को सार्वजनिक Microsoft कंटेनर रजिस्ट्री (MCR) में होस्ट करें।

Kaito का उपयोग करके, Kubernetes में बड़े AI अनुमान मॉडल को शामिल करने का कार्यप्रवाह काफी सरल हो जाता है।

## वास्तुकला

Kaito पारंपरिक Kubernetes कस्टम रिसोर्स डेफिनिशन (CRD)/कंट्रोलर डिज़ाइन पैटर्न का अनुसरण करता है। उपयोगकर्ता एक `workspace` कस्टम रिसोर्स का प्रबंधन करता है जो GPU आवश्यकताओं और अनुमान विनिर्देश का वर्णन करता है। Kaito कंट्रोलर `workspace` कस्टम रिसोर्स को समेकित करके तैनाती को स्वचालित करेंगे।

<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/website/static/img/ragarch.png" width=80% title="KAITO RAGEngine architecture" alt="KAITO RAGEngine architecture">
</div>

ऊपर दिया गया चित्र Kaito वास्तुकला का अवलोकन प्रस्तुत करता है। इसके मुख्य घटक निम्नलिखित हैं:

- **Workspace कंट्रोलर**: यह `workspace` कस्टम रिसोर्स को समेकित करता है, नोड ऑटो प्रावधान को ट्रिगर करने के लिए `machine` (नीचे समझाया गया) कस्टम रिसोर्स बनाता है, और मॉडल पूर्व निर्धारित कॉन्फ़िगरेशनों के आधार पर अनुमान वर्कलोड (`deployment` या `statefulset`) बनाता है।
- **Node प्राविजनर कंट्रोलर**: इस कंट्रोलर का नाम [gpu-provisioner helm चार्ट](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) में *gpu-provisioner* है। यह [Karpenter](https://sigs.k8s.io/karpenter) से उत्पन्न `machine` CRD का उपयोग करता है ताकि workspace कंट्रोलर के साथ संपर्क कर सके। यह Azure Kubernetes Service (AKS) API के साथ एकीकृत होकर AKS क्लस्टर में नए GPU नोड जोड़ता है।
> नोट: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) एक खुले स्रोत का घटक है। इसे दूसरे कंट्रोलरों से बदला जा सकता है यदि वे [Karpenter-core](https://sigs.k8s.io/karpenter) API का समर्थन करते हैं।

## स्थापना

कृपया स्थापना मार्गदर्शन के लिए [यहाँ](https://github.com/Azure/kaito/blob/main/docs/installation.md) देखें।

## त्वरित प्रारंभ अनुमान Phi-3
[नमूना कोड अनुमान Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # आउटपुट ACR पथ को ट्यून करना
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3.yaml
```

कार्यस्थान की स्थिति को निम्नलिखित कमांड चलाकर ट्रैक किया जा सकता है। जब WORKSPACEREADY कॉलम `True` हो जाता है, तो मॉडल सफलतापूर्वक तैनात हो चुका होता है।

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

इसके बाद, कोई भी अनुमान सेवा के क्लस्टर आईपी को ढूंढ सकता है और क्लस्टर में सेवा अंत बिंदु का परीक्षण करने के लिए एक अस्थायी `curl` पोड का उपयोग कर सकता है।

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## त्वरित प्रारंभ अनुमान Phi-3 एडाप्टर के साथ

Kaito स्थापित करने के बाद, कोई निम्नलिखित कमांड आज़मा सकता है ताकि एक अनुमान सेवा शुरू की जा सके।

[नमूना कोड अनुमान Phi-3 एडाप्टर के साथ](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # आउटपुट ACR पथ को ट्यून करना
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3_with_adapters.yaml
```

कार्यस्थान की स्थिति को निम्नलिखित कमांड चलाकर ट्रैक किया जा सकता है। जब WORKSPACEREADY कॉलम `True` हो जाता है, तो मॉडल सफलतापूर्वक तैनात हो चुका होता है।

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

इसके बाद, कोई भी अनुमान सेवा के क्लस्टर आईपी को ढूंढ सकता है और क्लस्टर में सेवा अंत बिंदु का परीक्षण करने के लिए एक अस्थायी `curl` पोड का उपयोग कर सकता है।

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या गलतियाँ हो सकती हैं। मूल भाषा में दस्तावेज़ ही आधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->