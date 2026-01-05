<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aca91084bc440431571e00bf30d96ab8",
  "translation_date": "2026-01-05T02:24:04+00:00",
  "source_file": "md/01.Introduction/03/Kaito_Inference.md",
  "language_code": "ne"
}
-->
## Kaito सँग अनुमान 

[Kaito](https://github.com/Azure/kaito) एक operator हो जसले Kubernetes क्लस्टरमा AI/ML अनुमान मोडेल तैनाती स्वचालित गर्दछ।

Kaitoसँग निम्न प्रमुख भिन्नताहरू छन् जुन अधिकांश मुख्यधाराका मोडेल तैनाती विधिहरू (जुन भर्चुअल मेसिन पूर्वाधारमा निर्माण गरिएका छन्) सँग तुलना गर्दा:

- Container images प्रयोग गरेर मोडेल फाइलहरू व्यवस्थापन गर्दछ। मोडेल लाइब्रेरी प्रयोग गरेर अनुमान कलहरू सञ्चालन गर्न एक HTTP सर्भर प्रदान गरिन्छ।
- प्रिसेट कन्फिगरेसनहरू प्रदान गरेर GPU हार्डवेयरसँग मेल खाने गरी deployment प्यारामिटरहरू ट्यून गर्नुबाट जोगिन्छ।
- मोडेलको आवश्यकताहरूका आधारमा GPU नोडहरू स्वचालित रूपमा प्राविजन गर्छ।
- लाइसेन्सले अनुमति दिएमा ठूलो मोडेल इमेजहरू सार्वजनिक Microsoft Container Registry (MCR) मा होस्ट गर्छ।

Kaito प्रयोग गर्दा Kubernetes मा ठूला AI अनुमान मोडेलहरूलाई अनबोर्ड गर्ने कार्यप्रवाह धेरै हदसम्म सरल हुन्छ।

## आर्किटेक्चर

Kaito ले पारम्परिक Kubernetes Custom Resource Definition(CRD)/controller डिजाइन ढाँचालाई अनुसरण गर्छ। प्रयोगकर्ताले GPU आवश्यकता र अनुमान विनिर्देश वर्णन गर्ने `workspace` custom resource व्यवस्थापन गर्छ। Kaito controllerहरूले `workspace` custom resource लाई reconcile गरेर तैनाती स्वचालित गर्नेछन्।

<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/website/static/img/ragarch.png" width=80% title="KAITO RAGEngine आर्किटेक्चर" alt="KAITO RAGEngine आर्किटेक्चर">
</div>

माथिको चित्रले Kaito को आर्किटेक्चर अवलोकन प्रस्तुत गर्छ। यसको मुख्य कम्पोनेन्टहरू समावेश छन्:

- **Workspace controller**: यसले `workspace` custom resource लाई reconcile गर्छ, नोड स्वचालित प्राविजन ट्रिगर गर्न `machine` (तल्लोमा व्याख्या गरिएको) custom resources सिर्जना गर्छ, र मोडेल प्रिसेट कन्फिगरेसनहरूका आधारमा अनुमान वर्कलोड (`deployment` वा `statefulset`) सिर्जना गर्छ।
- **Node provisioner controller**: उक्त controller को नाम [gpu-provisioner helm चार्ट](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) मा *gpu-provisioner* हो। यसले workspace controller सँग अन्तरक्रिया गर्न Karpenter बाट उत्पन्न भएको `machine` CRD प्रयोग गर्छ। यसले नयाँ GPU नोडहरू AKS क्लस्टरमा थप्न Azure Kubernetes Service(AKS) APIs सँग एकीकृत गर्छ। 
> नोट: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) एक open sourced कम्पोनेन्ट हो। यदि अन्य controller हरूले [Karpenter-core](https://sigs.k8s.io/karpenter) APIs समर्थन गर्छन् भने यसलाई प्रतिस्थापन गर्न सकिन्छ।

## स्थापना

कृपया स्थापना मार्गनिर्देशन [यहाँ](https://github.com/Azure/kaito/blob/main/docs/installation.md) हेर्नुहोस्।

## छिटो सुरु: Phi-3 अनुमान
[Phi-3 अनुमानको नमूना कोड](https://github.com/Azure/kaito/tree/main/examples/inference)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # समायोजन आउटपुट ACR पथ
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3.yaml
```

The workspace status can be tracked by running the following command. When the WORKSPACEREADY column becomes `True`, the model has been deployed successfully.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

Next, one can find the inference service's cluster ip and use a temporal `curl` pod to test the service endpoint in the cluster.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## एडाप्टरहरूसँग Phi-3 अनुमान छिटो सुरु

Kaito इन्स्टल गरेपछि, अनुमान सेवा सुरु गर्न तपाईँले तलका आदेशहरू प्रयास गर्न सक्नुहुन्छ।

[एडाप्टरहरूसँग Phi-3 अनुमानको नमूना कोड](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # ट्युनिङ आउटपुट ACR मार्ग
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3_with_adapters.yaml
```

The workspace status can be tracked by running the following command. When the WORKSPACEREADY column becomes `True`, the model has been deployed successfully.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

Next, one can find the inference service's cluster ip and use a temporal `curl` pod to test the service endpoint in the cluster.

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
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताको लागि प्रयास गर्छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा असत्यताहरू हुन सक्छन्। मूल दस्तावेजलाई यसको मूल भाषामा नै अधिकारिक स्रोत मानिनु पर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->