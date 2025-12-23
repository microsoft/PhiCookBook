<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e46691923dca7cb2f11d32b1d9d558e0",
  "translation_date": "2025-12-22T01:11:10+00:00",
  "source_file": "md/01.Introduction/03/Kaito_Inference.md",
  "language_code": "pcm"
}
-->
## Inference wit Kaito 

[Kaito](https://github.com/Azure/kaito) na operator wey dey automate AI/ML inference model deployment for Kubernetes cluster.

Kaito get the following key differences compared to most of the mainstream model deployment methodologies wey dem build on top of virtual machine infrastructures:

- Manage model files using container images. One HTTP server dey wey fit perform inference calls using the model library.
- No need to dey tune deployment parameters to fit GPU hardware because preset configurations don already dey.
- Auto-provision GPU nodes based on model requirements.
- Host large model images for the public Microsoft Container Registry (MCR) if the license allow am.

With Kaito, the workflow to onboard large AI inference models for Kubernetes don become much simpler.


## Architecture

Kaito dey follow the classic Kubernetes Custom Resource Definition(CRD)/controller design pattern. User dey manage a `workspace` custom resource wey describe the GPU requirements and the inference specification. Kaito controllers go automate the deployment by reconciling the `workspace` custom resource.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Kaito architekcha" alt="Kaito architekcha">
</div>

Di figure wey dey above show Kaito architecture overview. E major components be:

- **Workspace controller**: E dey reconcile the `workspace` custom resource, e go create `machine` (explained below) custom resources to trigger node auto provisioning, and e go create the inference workload (`deployment` or `statefulset`) based on the model preset configurations.
- **Node provisioner controller**: Di controller name na *gpu-provisioner* for [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). E dey use the `machine` CRD wey come from [Karpenter](https://sigs.k8s.io/karpenter) to interact with the workspace controller. E dey integrate with Azure Kubernetes Service(AKS) APIs to add new GPU nodes to the AKS cluster. 
> Note: The [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) na open sourced component. E fit replace am with other controllers if dem support [Karpenter-core](https://sigs.k8s.io/karpenter) APIs.

## Installation

Abeg check the installation guidance [here](https://github.com/Azure/kaito/blob/main/docs/installation.md).

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Tuning di ACR output path
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3.yaml
```

You fit track the workspace status by running the following command. When the WORKSPACEREADY column become `True`, the model don deploy successfully.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

Next, you fit find the inference service's cluster ip and use one temporary `curl` pod to test the service endpoint inside the cluster.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Quick start Inference Phi-3 wit adapters

After you install Kaito, you fit try the following commands to start an inference service.

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Tune di output ACR path
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3_with_adapters.yaml
```

You fit track the workspace status by running the following command. When the WORKSPACEREADY column become `True`, the model don deploy successfully.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

Next, you fit find the inference service's cluster ip and use one temporary `curl` pod to test the service endpoint inside the cluster.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Disclaimer:

Dis document na AI translation service wey dem call Co-op Translator do. Even though we dey try make everything correct, abeg sabi say automatic translation fit get mistakes or no too correct. Di original document for im original language na di official one. If na important matter, make you use professional human translator. We no go responsible for any misunderstanding or wrong interpretation wey fit happen because of this translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->