<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aca91084bc440431571e00bf30d96ab8",
  "translation_date": "2026-01-05T14:53:18+00:00",
  "source_file": "md/01.Introduction/03/Kaito_Inference.md",
  "language_code": "pcm"
}
-->
## Inference wit Kaito 

[Kaito](https://github.com/Azure/kaito) na operator wey dey automate AI/ML inference model deployment for Kubernetes cluster.

Kaito get di following key differences compared to most of di main model deployment methods wey dem build on top of virtual machine infrastructure dem:

- Manage model files wit container images. Dem provide http server to run inference calls using di model library.
- No need to tune deployment parameters to fit GPU hardware, because dem get preset configurations ready.
- E dey auto-provision GPU nodes based on how model need am.
- E fit host big model images for public Microsoft Container Registry (MCR) if license allow am.

If you use Kaito, di work to bring big AI inference models enter Kubernetes go dey much simpler.


## Architecture

Kaito dey follow di classic Kubernetes Custom Resource Definition(CRD)/controller design pattern. User go manage `workspace` custom resource wey go describe GPU requirements and inference specification. Kaito controllers go automate deployment by matching up to di `workspace` custom resource.

<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/website/static/img/ragarch.png" width=80% title="KAITO RAGEngine architecture" alt="KAITO RAGEngine architecture">
</div>

Di picture wey dey above show Kaito architecture overview. Di main parts be:

- **Workspace controller**: E dey reconcile di `workspace` custom resource, e dey create `machine` (wey dem go explain below) custom resources to trigger node auto provisioning, and e dey create di inference workload (`deployment` or `statefulset`) based on di model preset configurations.
- **Node provisioner controller**: Di controller name na *gpu-provisioner* for [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). E dey use `machine` CRD wey come from [Karpenter](https://sigs.k8s.io/karpenter) to interact with di workspace controller. E dey work together wit Azure Kubernetes Service(AKS) APIs to add new GPU nodes enter di AKS cluster. 
> Note: Di [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) na open source component. You fit change am to other controllers if dem support [Karpenter-core](https://sigs.k8s.io/karpenter) APIs.

## Installation

Abeg check di installation guide [here](https://github.com/Azure/kaito/blob/main/docs/installation.md).

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Tuning Output ACR Path na so e be
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3.yaml
```

You fit track workspace status by running this command. When di WORKSPACEREADY column show `True`, e mean say di model don deploy well.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

After that, you fit find inference service cluster IP and use temporary `curl` pod to test di service endpoint inside di cluster.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Quick start Inference Phi-3 wit adapters

After you don install Kaito, you fit try these commands to start inference service.

[Sample Code Inference Phi-3 wit Adapters](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Tuning di Output ACR Path
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3_with_adapters.yaml
```

You fit track workspace status by running this command. When di WORKSPACEREADY column show `True`, e mean say di model don deploy well.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

After that, you fit find inference service cluster IP and use temporary `curl` pod to test di service endpoint inside di cluster.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document na translation wey AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator) help do. Even though we dey try make am correct, abeg make you sabi say automated translation fit get some mistakes or no too correct. Di original document wey e dey for im original language na di real correct one. If na serious gbege or important tin, e better make person wey sabi human translation help you translate am. We no go responsible if pesin no understand well or if yawa happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->