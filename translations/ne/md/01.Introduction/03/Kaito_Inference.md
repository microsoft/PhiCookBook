<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e46691923dca7cb2f11d32b1d9d558e0",
  "translation_date": "2025-05-09T11:49:09+00:00",
  "source_file": "md/01.Introduction/03/Kaito_Inference.md",
  "language_code": "ne"
}
-->
## Kaito सँग inference

[Kaito](https://github.com/Azure/kaito) एउटा operator हो जसले Kubernetes cluster भित्र AI/ML inference मोडेल deployment लाई स्वचालित गर्छ।

Kaito का मुख्य फरकहरू जुन धेरै मुख्यधाराका मोडेल deployment विधिहरू भन्दा फरक छन् जुन प्रायः virtual machine infrastructures मा आधारित हुन्छन्:

- मोडेल फाइलहरू container images मार्फत व्यवस्थापन गर्छ। मोडेल लाइब्रेरी प्रयोग गरेर inference कल गर्न HTTP server उपलब्ध गराउँछ।
- GPU hardware अनुसार deployment parameters मिलाउन tuning गर्न आवश्यक पर्दैन किनकि preset configurations उपलब्ध छन्।
- मोडेल आवश्यकताहरू अनुसार GPU nodes स्वचालित रूपमा provision गर्छ।
- यदि license अनुमति दिन्छ भने ठूलो मोडेल images सार्वजनिक Microsoft Container Registry (MCR) मा होस्ट गर्छ।

Kaito प्रयोग गर्दा Kubernetes मा ठूलो AI inference मोडेलहरू onboarding को workflow धेरै सरल हुन्छ।


## वास्तुकला

Kaito ले पारम्परिक Kubernetes Custom Resource Definition(CRD)/controller डिजाइन ढाँचा अनुसरण गर्छ। प्रयोगकर्ताले `workspace` custom resource व्यवस्थापन गर्छ जसले GPU आवश्यकताहरू र inference specification वर्णन गर्छ। Kaito controllers ले `workspace` custom resource reconcile गरेर deployment स्वचालित बनाउँछन्।
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

माथिको चित्रले Kaito वास्तुकला को अवलोकन देखाउँछ। यसको मुख्य घटकहरू:

- **Workspace controller**: यसले `workspace` custom resource reconcile गर्छ, node auto provisioning ट्रिगर गर्न `machine` (तल व्याख्या गरिएको) custom resources सिर्जना गर्छ, र मोडेल preset configurations अनुसार inference workload (`deployment` वा `statefulset`) सिर्जना गर्छ।
- **Node provisioner controller**: यो controller को नाम [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) मा *gpu-provisioner* हो। यो [Karpenter](https://sigs.k8s.io/karpenter) बाट आएको `machine` CRD प्रयोग गरेर workspace controller सँग अन्तरक्रिया गर्छ। यो Azure Kubernetes Service(AKS) APIs सँग मिलेर AKS cluster मा नयाँ GPU nodes थप्छ। 
> Note: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) खुला स्रोत component हो। यदि अन्य controllers ले [Karpenter-core](https://sigs.k8s.io/karpenter) APIs समर्थन गर्छन् भने यसलाई प्रतिस्थापन गर्न सकिन्छ।

## स्थापना

कृपया स्थापना निर्देशिका [यहाँ](https://github.com/Azure/kaito/blob/main/docs/installation.md) हेर्नुहोस्।

## छिटो सुरुवात Inference Phi-3
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

workspace को स्थिति तलको आदेश चलाएर ट्र्याक गर्न सकिन्छ। WORKSPACEREADY स्तम्भ `True` हुँदा मोडेल सफलतापूर्वक deploy भइसकेको हुन्छ।

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

पछि, inference सेवा को cluster ip पत्ता लगाएर cluster भित्र सेवा endpoint परीक्षण गर्न अस्थायी `curl` pod प्रयोग गर्न सकिन्छ।

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## छिटो सुरुवात Inference Phi-3 with adapters

Kaito स्थापना पछि, निम्न आदेशहरू चलाएर inference सेवा सुरु गर्न सकिन्छ।

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

workspace को स्थिति तलको आदेश चलाएर ट्र्याक गर्न सकिन्छ। WORKSPACEREADY स्तम्भ `True` हुँदा मोडेल सफलतापूर्वक deploy भइसकेको हुन्छ।

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

पछि, inference सेवा को cluster ip पत्ता लगाएर cluster भित्र सेवा endpoint परीक्षण गर्न अस्थायी `curl` pod प्रयोग गर्न सकिन्छ।

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**अस्वीकरण**:  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताका लागि प्रयासरत छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुन सक्दछ। मूल दस्तावेज यसको मूल भाषामा नै अधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्याको लागि हामी जिम्मेवार छैनौं।