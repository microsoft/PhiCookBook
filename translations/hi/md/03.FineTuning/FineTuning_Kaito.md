<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a1c62bf7d86d6186bf8d3917196a92a0",
  "translation_date": "2025-05-08T05:23:17+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Kaito.md",
  "language_code": "hi"
}
-->
## Kaito के साथ फाइन-ट्यूनिंग

[Kaito](https://github.com/Azure/kaito) एक ऑपरेटर है जो Kubernetes क्लस्टर में AI/ML इन्फरेंस मॉडल डिप्लॉयमेंट को स्वचालित करता है।

Kaito के पास अधिकांश मुख्यधारा के मॉडल डिप्लॉयमेंट विधियों की तुलना में कुछ प्रमुख अंतर हैं, जो वर्चुअल मशीन इन्फ्रास्ट्रक्चर पर आधारित हैं:

- मॉडल फाइलों को कंटेनर इमेजेज के माध्यम से प्रबंधित करना। मॉडल लाइब्रेरी का उपयोग करके इन्फरेंस कॉल करने के लिए एक HTTP सर्वर प्रदान किया जाता है।
- GPU हार्डवेयर के अनुसार डिप्लॉयमेंट पैरामीटर को ट्यून करने से बचने के लिए प्रीसेट कॉन्फ़िगरेशन प्रदान करना।
- मॉडल आवश्यकताओं के आधार पर GPU नोड्स का ऑटो-प्रावधान।
- यदि लाइसेंस अनुमति देता है, तो बड़े मॉडल इमेजेज को सार्वजनिक Microsoft Container Registry (MCR) में होस्ट करना।

Kaito का उपयोग करके, Kubernetes में बड़े AI इन्फरेंस मॉडल को ऑनबोर्ड करने का कार्यप्रवाह काफी सरल हो जाता है।

## आर्किटेक्चर

Kaito पारंपरिक Kubernetes Custom Resource Definition (CRD)/controller डिज़ाइन पैटर्न का पालन करता है। उपयोगकर्ता एक `workspace` कस्टम रिसोर्स को प्रबंधित करता है जो GPU आवश्यकताओं और इन्फरेंस विनिर्देशन का वर्णन करता है। Kaito कंट्रोलर `workspace` कस्टम रिसोर्स को मेल करके डिप्लॉयमेंट को स्वचालित करेगा।
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

ऊपर दिया गया चित्र Kaito आर्किटेक्चर का अवलोकन प्रस्तुत करता है। इसके मुख्य घटक निम्नलिखित हैं:

- **Workspace controller**: यह `workspace` कस्टम रिसोर्स को मेल करता है, नोड ऑटो प्राविजनिंग को ट्रिगर करने के लिए `machine` (नीचे समझाया गया) कस्टम रिसोर्स बनाता है, और मॉडल प्रीसेट कॉन्फ़िगरेशन के आधार पर इन्फरेंस वर्कलोड (`deployment` या `statefulset`) बनाता है।
- **Node provisioner controller**: इस कंट्रोलर का नाम [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) में *gpu-provisioner* है। यह [Karpenter](https://sigs.k8s.io/karpenter) से उत्पन्न `machine` CRD का उपयोग करके workspace controller के साथ इंटरैक्ट करता है। यह Azure Kubernetes Service (AKS) APIs के साथ इंटीग्रेट होकर AKS क्लस्टर में नए GPU नोड्स जोड़ता है।  
> Note: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) एक ओपन सोर्स कंपोनेंट है। इसे अन्य कंट्रोलर्स से बदला जा सकता है यदि वे [Karpenter-core](https://sigs.k8s.io/karpenter) APIs का समर्थन करते हों।

## अवलोकन वीडियो  
[Kaito डेमो देखें](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)

## इंस्टॉलेशन

इंस्टॉलेशन मार्गदर्शन के लिए कृपया [यहाँ](https://github.com/Azure/kaito/blob/main/docs/installation.md) देखें।

## त्वरित शुरुआत

Kaito इंस्टॉल करने के बाद, फाइन-ट्यूनिंग सेवा शुरू करने के लिए निम्नलिखित कमांड आज़माए जा सकते हैं।

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

वर्कस्पेस की स्थिति को ट्रैक करने के लिए निम्नलिखित कमांड चलाएं। जब WORKSPACEREADY कॉलम `True` हो जाता है, तो मॉडल सफलतापूर्वक डिप्लॉय हो चुका होता है।

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

इसके बाद, इन्फरेंस सेवा के क्लस्टर IP को खोजा जा सकता है और क्लस्टर में सेवा एंडपॉइंट का परीक्षण करने के लिए एक अस्थायी `curl` पॉड का उपयोग किया जा सकता है।

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान रखें कि स्वचालित अनुवादों में त्रुटियाँ या गलतियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही अधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।