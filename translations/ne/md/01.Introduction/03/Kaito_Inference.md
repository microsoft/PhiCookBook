<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e46691923dca7cb2f11d32b1d9d558e0",
  "translation_date": "2025-07-16T20:49:24+00:00",
  "source_file": "md/01.Introduction/03/Kaito_Inference.md",
  "language_code": "ne"
}
-->
## Kaito सँग इन्फरेन्स

[Kaito](https://github.com/Azure/kaito) एक अपरेटर हो जसले Kubernetes क्लस्टरमा AI/ML इन्फरेन्स मोडेल डिप्लोयमेन्टलाई स्वचालित बनाउँछ।

Kaito का मुख्य फरकहरू प्रायः भर्चुअल मेशिन इन्फ्रास्ट्रक्चरमा आधारित अधिकांश मोडेल डिप्लोयमेन्ट विधिहरूको तुलनामा यसप्रकार छन्:

- मोडेल फाइलहरू कन्टेनर इमेजहरू प्रयोग गरेर व्यवस्थापन गर्नु। मोडेल लाइब्रेरी प्रयोग गरी इन्फरेन्स कलहरू गर्न HTTP सर्भर प्रदान गरिन्छ।
- GPU हार्डवेयरमा फिट हुन डिप्लोयमेन्ट प्यारामिटरहरू ट्यून नगरी पूर्वनिर्धारित कन्फिगरेसनहरू उपलब्ध गराउनु।
- मोडेल आवश्यकताहरू अनुसार GPU नोडहरू स्वचालित रूपमा प्रावधान गर्नु।
- लाइसेन्स अनुमति भएमा ठूलो मोडेल इमेजहरू सार्वजनिक Microsoft Container Registry (MCR) मा होस्ट गर्नु।

Kaito प्रयोग गरेर, Kubernetes मा ठूलो AI इन्फरेन्स मोडेलहरू अनबोर्ड गर्ने कार्यप्रवाह धेरै सरल हुन्छ।


## वास्तुकला

Kaito ले क्लासिक Kubernetes Custom Resource Definition(CRD)/controller डिजाइन ढाँचा अनुसरण गर्छ। प्रयोगकर्ताले GPU आवश्यकताहरू र इन्फरेन्स विशिष्टता वर्णन गर्ने `workspace` कस्टम रिसोर्स व्यवस्थापन गर्छ। Kaito कन्ट्रोलरहरूले `workspace` कस्टम रिसोर्सलाई मिलाएर डिप्लोयमेन्ट स्वचालित बनाउँछन्।
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

माथिको चित्रले Kaito वास्तुकलाको अवलोकन प्रस्तुत गर्दछ। यसको मुख्य कम्पोनेन्टहरू यसप्रकार छन्:

- **Workspace controller**: यसले `workspace` कस्टम रिसोर्सलाई मिलाउँछ, नोड स्वचालित प्रावधान गर्न `machine` (तल व्याख्या गरिएको) कस्टम रिसोर्सहरू सिर्जना गर्छ, र मोडेल पूर्वनिर्धारित कन्फिगरेसनहरूका आधारमा इन्फरेन्स वर्कलोड (`deployment` वा `statefulset`) सिर्जना गर्छ।
- **Node provisioner controller**: यस कन्ट्रोलरको नाम [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) मा *gpu-provisioner* हो। यसले [Karpenter](https://sigs.k8s.io/karpenter) बाट उत्पन्न `machine` CRD प्रयोग गरेर workspace controller सँग अन्तरक्रिया गर्छ। यसले Azure Kubernetes Service(AKS) API हरूसँग एकीकृत भएर AKS क्लस्टरमा नयाँ GPU नोडहरू थप्छ। 
> Note: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) एक खुला स्रोत कम्पोनेन्ट हो। यदि अन्य कन्ट्रोलरहरूले [Karpenter-core](https://sigs.k8s.io/karpenter) API हरू समर्थन गर्छन् भने यसलाई प्रतिस्थापन गर्न सकिन्छ।

## स्थापना

कृपया स्थापना निर्देशनहरू [यहाँ](https://github.com/Azure/kaito/blob/main/docs/installation.md) हेर्नुहोस्।

## छिटो सुरु इन्फरेन्स Phi-3
[नमूना कोड इन्फरेन्स Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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

workspace स्थिति तलको कमाण्ड चलाएर ट्र्याक गर्न सकिन्छ। जब WORKSPACEREADY स्तम्भ `True` हुन्छ, मोडेल सफलतापूर्वक डिप्लोय गरिएको हुन्छ।

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

अर्को, इन्फरेन्स सेवाको क्लस्टर IP पत्ता लगाएर क्लस्टर भित्र अस्थायी `curl` पोड प्रयोग गरी सेवा अन्तबिन्दु परीक्षण गर्न सकिन्छ।

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## छिटो सुरु इन्फरेन्स Phi-3 एडाप्टरहरूसँग

Kaito स्थापना गरेपछि, तलका कमाण्डहरू चलाएर इन्फरेन्स सेवा सुरु गर्न सकिन्छ।

[नमूना कोड इन्फरेन्स Phi-3 एडाप्टरहरूसँग](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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

workspace स्थिति तलको कमाण्ड चलाएर ट्र्याक गर्न सकिन्छ। जब WORKSPACEREADY स्तम्भ `True` हुन्छ, मोडेल सफलतापूर्वक डिप्लोय गरिएको हुन्छ।

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

अर्को, इन्फरेन्स सेवाको क्लस्टर IP पत्ता लगाएर क्लस्टर भित्र अस्थायी `curl` पोड प्रयोग गरी सेवा अन्तबिन्दु परीक्षण गर्न सकिन्छ।

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**अस्वीकरण**:  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताका लागि प्रयासरत छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुन सक्छ। मूल दस्तावेज यसको मूल भाषामा नै अधिकारिक स्रोत मानिनु पर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार छैनौं।