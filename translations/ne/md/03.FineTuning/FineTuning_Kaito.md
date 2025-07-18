<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a1c62bf7d86d6186bf8d3917196a92a0",
  "translation_date": "2025-07-17T06:20:53+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Kaito.md",
  "language_code": "ne"
}
-->
## Kaito सँग फाइन-ट्यूनिङ

[Kaito](https://github.com/Azure/kaito) एक अपरेटर हो जसले Kubernetes क्लस्टरमा AI/ML इन्फरेन्स मोडेल डिप्लोयमेन्टलाई स्वचालित बनाउँछ।

Kaito सँग भर्चुअल मेशिन इन्फ्रास्ट्रक्चरमा आधारित अधिकांश मुख्यधाराका मोडेल डिप्लोयमेन्ट विधिहरूको तुलनामा निम्न मुख्य भिन्नताहरू छन्:

- मोडेल फाइलहरू कन्टेनर इमेजहरू प्रयोग गरेर व्यवस्थापन गर्नुहोस्। मोडेल लाइब्रेरी प्रयोग गरेर इन्फरेन्स कलहरू गर्न http सर्भर प्रदान गरिएको छ।
- GPU हार्डवेयरमा फिट हुन डिप्लोयमेन्ट प्यारामिटरहरू ट्यून नगर्न पूर्वनिर्धारित कन्फिगरेसनहरू उपलब्ध गराउनुहोस्।
- मोडेल आवश्यकताहरूको आधारमा GPU नोडहरू स्वचालित रूपमा प्रावधान गर्नुहोस्।
- लाइसेन्स अनुमति भएमा ठूलो मोडेल इमेजहरू सार्वजनिक Microsoft Container Registry (MCR) मा होस्ट गर्नुहोस्।

Kaito प्रयोग गरेर, Kubernetes मा ठूलो AI इन्फरेन्स मोडेलहरू अनबोर्ड गर्ने कार्यप्रवाह धेरै सरल हुन्छ।


## वास्तुकला

Kaito ले क्लासिक Kubernetes Custom Resource Definition(CRD)/controller डिजाइन ढाँचा अनुसरण गर्छ। प्रयोगकर्ताले GPU आवश्यकताहरू र इन्फरेन्स विशिष्टता वर्णन गर्ने `workspace` कस्टम रिसोर्स व्यवस्थापन गर्छ। Kaito कन्ट्रोलरहरूले `workspace` कस्टम रिसोर्सलाई मेल खाने गरी डिप्लोयमेन्ट स्वचालित बनाउँछन्।
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

माथिको चित्रले Kaito वास्तुकलाको अवलोकन प्रस्तुत गर्दछ। यसको मुख्य कम्पोनेन्टहरू समावेश छन्:

- **Workspace controller**: यसले `workspace` कस्टम रिसोर्सलाई मेल खाने काम गर्छ, नोड स्वचालित प्रावधान गर्न `machine` (तल व्याख्या गरिएको) कस्टम रिसोर्सहरू सिर्जना गर्छ, र मोडेल पूर्वनिर्धारित कन्फिगरेसनहरूका आधारमा इन्फरेन्स वर्कलोड (`deployment` वा `statefulset`) सिर्जना गर्छ।
- **Node provisioner controller**: यस कन्ट्रोलरको नाम [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) मा *gpu-provisioner* हो। यसले [Karpenter](https://sigs.k8s.io/karpenter) बाट उत्पन्न `machine` CRD प्रयोग गरेर workspace controller सँग अन्तरक्रिया गर्छ। यसले Azure Kubernetes Service(AKS) API हरूसँग एकीकृत भएर AKS क्लस्टरमा नयाँ GPU नोडहरू थप्छ। 
> Note: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) एक खुला स्रोत कम्पोनेन्ट हो। यदि अन्य कन्ट्रोलरहरूले [Karpenter-core](https://sigs.k8s.io/karpenter) API हरू समर्थन गर्छन् भने तिनीहरूले यसलाई प्रतिस्थापन गर्न सक्छन्।

## अवलोकन भिडियो  
[Kaito डेमो हेर्नुहोस्](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)

## स्थापना

कृपया स्थापना निर्देशनहरू [यहाँ](https://github.com/Azure/kaito/blob/main/docs/installation.md) जाँच गर्नुहोस्।

## छिटो सुरु

Kaito स्थापना गरेपछि, फाइन-ट्यूनिङ सेवा सुरु गर्न तलका आदेशहरू प्रयास गर्न सकिन्छ।

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

workspace स्थिति तलको आदेश चलाएर ट्र्याक गर्न सकिन्छ। जब WORKSPACEREADY स्तम्भ `True` हुन्छ, मोडेल सफलतापूर्वक डिप्लोय गरिएको हुन्छ।

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

अर्को, इन्फरेन्स सेवाको क्लस्टर IP पत्ता लगाएर क्लस्टर भित्र अस्थायी `curl` पोड प्रयोग गरी सेवा अन्तबिन्दु परीक्षण गर्न सकिन्छ।

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**अस्वीकरण**:  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताका लागि प्रयासरत छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुनसक्छ। मूल दस्तावेज यसको मूल भाषामा नै अधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार छैनौं।