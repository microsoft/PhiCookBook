<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "05e69691c294289d217150bec390a5fb",
  "translation_date": "2025-04-04T18:50:42+00:00",
  "source_file": "md\\03.FineTuning\\FineTuning_Kaito.md",
  "language_code": "hi"
}
-->
## Kaito के साथ फाइन-ट्यूनिंग

[Kaito](https://github.com/Azure/kaito) एक ऑपरेटर है जो Kubernetes क्लस्टर में AI/ML इंफरेंस मॉडल को डिप्लॉय करने को ऑटोमेट करता है।

Kaito के पास मुख्यधारा के मॉडल डिप्लॉयमेंट तरीकों की तुलना में निम्नलिखित प्रमुख अंतर हैं, जो वर्चुअल मशीन इंफ्रास्ट्रक्चर पर आधारित होते हैं:

- कंटेनर इमेज का उपयोग करके मॉडल फाइल्स को प्रबंधित करें। मॉडल लाइब्रेरी का उपयोग करके इंफरेंस कॉल्स करने के लिए एक HTTP सर्वर प्रदान किया जाता है।
- GPU हार्डवेयर के अनुसार डिप्लॉयमेंट पैरामीटर्स को ट्यून करने से बचें, क्योंकि प्रीसेट कॉन्फ़िगरेशन उपलब्ध हैं।
- मॉडल की आवश्यकताओं के आधार पर GPU नोड्स को ऑटो-प्रोविजन करें।
- यदि लाइसेंस अनुमति देता है, तो बड़े मॉडल इमेज को सार्वजनिक Microsoft Container Registry (MCR) में होस्ट करें।

Kaito का उपयोग करके Kubernetes में बड़े AI इंफरेंस मॉडल को ऑनबोर्ड करने का वर्कफ़्लो काफी सरल हो जाता है।

## आर्किटेक्चर

Kaito क्लासिक Kubernetes Custom Resource Definition(CRD)/कंट्रोलर डिज़ाइन पैटर्न का अनुसरण करता है। उपयोगकर्ता एक `workspace` कस्टम रिसोर्स प्रबंधित करते हैं, जो GPU आवश्यकताओं और इंफरेंस स्पेसिफिकेशन का वर्णन करता है। Kaito कंट्रोलर `workspace` कस्टम रिसोर्स को समेटकर डिप्लॉयमेंट को ऑटोमेट कर देते हैं।
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

ऊपर दिए गए चित्र में Kaito आर्किटेक्चर का ओवरव्यू प्रस्तुत किया गया है। इसके मुख्य घटक निम्नलिखित हैं:

- **वर्कस्पेस कंट्रोलर**: यह `workspace` कस्टम रिसोर्स को समेटता है, `machine` (नीचे समझाया गया है) कस्टम रिसोर्स बनाता है ताकि नोड ऑटो-प्रोविजनिंग ट्रिगर हो सके, और मॉडल प्रीसेट कॉन्फ़िगरेशन के आधार पर इंफरेंस वर्कलोड (`deployment` या `statefulset`) बनाता है।
- **नोड प्रोविजनर कंट्रोलर**: इस कंट्रोलर का नाम [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) में *gpu-provisioner* है। यह [Karpenter](https://sigs.k8s.io/karpenter) से उत्पन्न `machine` CRD का उपयोग वर्कस्पेस कंट्रोलर के साथ बातचीत करने के लिए करता है। यह Azure Kubernetes Service(AKS) APIs के साथ इंटीग्रेट करता है ताकि AKS क्लस्टर में नए GPU नोड्स जोड़े जा सकें।  
> नोट: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) एक ओपन सोर्स्ड घटक है। इसे अन्य कंट्रोलर्स द्वारा प्रतिस्थापित किया जा सकता है यदि वे [Karpenter-core](https://sigs.k8s.io/karpenter) APIs को सपोर्ट करते हैं।

## ओवरव्यू वीडियो
[Kaito डेमो देखें](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)
## इंस्टॉलेशन

कृपया इंस्टॉलेशन गाइडेंस [यहां](https://github.com/Azure/kaito/blob/main/docs/installation.md) देखें।

## त्वरित शुरुआत

Kaito इंस्टॉल करने के बाद, निम्नलिखित कमांड्स का उपयोग करके एक फाइन-ट्यूनिंग सर्विस शुरू की जा सकती है।

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

वर्कस्पेस की स्थिति को निम्नलिखित कमांड चलाकर ट्रैक किया जा सकता है। जब WORKSPACEREADY कॉलम `True` हो जाए, तो मॉडल सफलतापूर्वक डिप्लॉय हो चुका है।

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

इसके बाद, क्लस्टर के इंफरेंस सर्विस का क्लस्टर IP ढूंढा जा सकता है और एक अस्थायी `curl` pod का उपयोग करके क्लस्टर में सर्विस एन्डपॉइंट का परीक्षण किया जा सकता है।

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता सुनिश्चित करने का प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियां या गलतियां हो सकती हैं। मूल भाषा में लिखा गया मूल दस्तावेज़ ही आधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।