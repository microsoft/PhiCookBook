<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aca91084bc440431571e00bf30d96ab8",
  "translation_date": "2026-01-05T16:53:49+00:00",
  "source_file": "md/01.Introduction/03/Kaito_Inference.md",
  "language_code": "ne"
}
-->
## Kaito सँग inference

[Kaito](https://github.com/Azure/kaito) एउटा अपरेटर हो जसले Kubernetes क्लस्टरमा AI/ML inference मोडेल डिप्लॉयमेन्टलाई स्वचालित गर्दछ।

Kaito सँग भर्चुअल मेसिन पूर्वाधारहरूको माथि निर्मित अधिकांश मुख्यधाराको मोडेल डिप्लॉयमेन्ट विधिहरूको तुलनामा निम्न मुख्य भिन्नताहरू छन्:

- मोडेल फाइलहरू कन्टेनर इमेजहरू प्रयोग गरेर व्यवस्थापन गर्नुहोस्। मोडेल पुस्तकालय प्रयोग गरी inference कलहरू प्रदर्शन गर्न HTTP सर्भर प्रदान गरिएको छ।
- GPU हार्डवेयर अनुकूल बनाउन डिप्लॉयमेन्ट प्यारामिटरहरू ट्युनिङ नगर्न पूर्वनिर्धारित कन्फिगरेसनहरू प्रदान गरिन्छ।
- मोडेल आवश्यकताहरूका आधारमा GPU नोडहरू स्वचालित रूपमा प्रावधान गर्नुहोस्।
- लाइसेन्सले अनुमति दिएमा सार्वजनिक Microsoft Container Registry (MCR) मा ठूलो मोडेल इमेजहरू होस्ट गर्नुहोस्।

Kaito प्रयोग गरेर, Kubernetes मा ठूलो AI inference मोडेलहरू अनबोर्ड गर्ने कार्यप्रवाह ठूलो मात्रामा सरल पारिन्छ।


## वास्तुकला

Kaito ले क्लासिक Kubernetes Custom Resource Definition(CRD)/controller डिजाइन ढाँचा अनुसरण गर्दछ। प्रयोगकर्ताले GPU आवश्यकताहरू र inference विशिष्टता वर्णन गर्ने `workspace` कस्टम स्रोत व्यवस्थापन गर्दछ। Kaito कन्ट्रोलरहरूले `workspace` कस्टम स्रोतलाई मेल खाने गरी डिप्लॉयमेन्ट स्वचालित बनाउँछन्।

<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/website/static/img/ragarch.png" width=80% title="KAITO RAGEngine architecture" alt="KAITO RAGEngine architecture">
</div>

माथिको चित्रले Kaito वास्तुकलाको अवलोकन प्रस्तुत गर्दछ। यसको मुख्य भागहरू समावेश छन्:

- **Workspace controller**: यसले `workspace` कस्टम स्रोतलाई मेल खुवाउँछ, ग्राफमा उल्लेख गरिएका `machine` (तल व्याख्या गरिएको) कस्टम स्रोतहरू सिर्जना गर्दछ जसले नोड स्वचालित प्रावधान गर्ने ट्रिगर गर्छ र मोडेल पूर्वनिर्धारित कन्फिगरेसनहरू आधारित inference कार्यभार (`deployment` वा `statefulset`) सिर्जना गर्दछ।
- **Node provisioner controller**: यो कन्ट्रोलरको नाम [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) मा *gpu-provisioner* हो। यसले workspace controller सँग अन्तरक्रिया गर्न Karpenter बाट उत्पन्न `machine` CRD प्रयोग गर्दछ। यसले Azure Kubernetes Service(AKS) API हरू संग एकीकृत गरी AKS क्लस्टरमा नयाँ GPU नोडहरू थप्छ। 
> नोट: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) एउटा खुला स्रोत कम्पोनेन्ट हो। यो अन्य कन्ट्रोलरहरूले यदि [Karpenter-core](https://sigs.k8s.io/karpenter) API हरू समर्थन गर्छ भने प्रतिस्थापन गर्न सकिन्छ।

## स्थापना

कृपया [यहाँ](https://github.com/Azure/kaito/blob/main/docs/installation.md) स्थापना निर्देशन जाँच गर्नुहोस्।

## छिटो सुरुवात Inference Phi-3
[नमूना कोड Inference Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # आउटपुट ACR पाथ ट्यून गर्दै
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3.yaml
```

workspace स्थिति तलको कमाण्ड चलाएर ट्र्याक गर्न सकिन्छ। जब WORKSPACEREADY स्तम्भ `True` हुन्छ, मोडेल सफलतापूर्वक डिप्लॉय गरिएको छ।

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

अर्को, inference सेवा को क्लस्टर IP खोज्न र क्लस्टरमा अस्थायी `curl` पोड प्रयोग गरी सेवा इन्डपोइन्ट परीक्षण गर्न सकिन्छ।

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## adapters सहित छिटो सुरुवात Inference Phi-3

Kaito स्थापना गरेपछि, inference सेवा सुरु गर्न निम्न कमाण्डहरू प्रयास गर्न सकिन्छ।

[नमूना कोड Inference Phi-3 with Adapters](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # उत्पादन ACR मार्ग ट्यून गर्दै
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3_with_adapters.yaml
```

workspace स्थिति तलको कमाण्ड चलाएर ट्र्याक गर्न सकिन्छ। जब WORKSPACEREADY स्तम्भ `True` हुन्छ, मोडेल सफलतापूर्वक डिप्लॉय गरिएको छ।

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

अर्को, inference सेवा को क्लस्टर IP खोज्न र क्लस्टरमा अस्थायी `curl` पोड प्रयोग गरी सेवा इन्डपोइन्ट परीक्षण गर्न सकिन्छ।

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
यस कागजातलाई AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी सटीकता सुनिश्चित गर्न प्रयासरत छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा असत्यताहरू हुन सक्छन्। मूल कागजात यसको स्वदेशी भाषामा अधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीको लागि पेशेवर मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्याको लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->