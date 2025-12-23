<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a1c62bf7d86d6186bf8d3917196a92a0",
  "translation_date": "2025-12-21T18:38:11+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Kaito.md",
  "language_code": "pcm"
}
-->
## Fine-Tuning wit Kaito 

[Kaito](https://github.com/Azure/kaito) na operator wey dey automate di AI/ML inference model deployment for Kubernetes cluster.

Kaito get dis key differences compared to most mainstream model deployment methodologies wey dem build on top of virtual machine infrastructures:

- Manage model files using container images. A http server dey provided to perform inference calls using di model library.
- No need to tune deployment parameters to fit GPU hardware because preset configurations dey provided.
- E dey auto-provision GPU nodes based on wetin di model need.
- Host large model images in the public Microsoft Container Registry (MCR) if di license allow am.

With Kaito, di workflow for onboarding large AI inference models inside Kubernetes don become much simpler.


## Architecture

Kaito dey follow di classic Kubernetes Custom Resource Definition(CRD)/controller design pattern. User manages a `workspace` custom resource wey dey describe di GPU requirements and di inference specification. Kaito controllers go automate di deployment by reconciling di `workspace` custom resource.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

Di picture wey dey above show di Kaito architecture overview. Di main components na:

- **Workspace controller**: E dey reconcile di `workspace` custom resource, e dey create `machine` (explained below) custom resources to trigger node auto provisioning, and e dey create di inference workload (`deployment` or `statefulset`) based on di model preset configurations.
- **Node provisioner controller**: Di controller name na *gpu-provisioner* for [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). E dey use di `machine` CRD wey originate from [Karpenter](https://sigs.k8s.io/karpenter) to interact with di workspace controller. E dey integrate with Azure Kubernetes Service(AKS) APIs to add new GPU nodes to di AKS cluster. 
> Note: The [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) is an open sourced component. You fit replace am with other controllers if dem support [Karpenter-core](https://sigs.k8s.io/karpenter) APIs.

## Overview video 
[Watch di Kaito Demo](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)
## Installation

Abeg check di installation guidance [here](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Quick start

After you install Kaito, you fit try di following commands to start fine-tuning service.

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Tunin di ACR output path
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/fine-tuning/kaito_workspace_tuning_phi_3.yaml
```

You fit track di workspace status by running di following command. When di WORKSPACEREADY column become `True`, di model don deploy successfully.

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

Next, you fit find di inference service's cluster ip and use one temporary `curl` pod to test di service endpoint inside di cluster.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Disclaimer:
Dis dokument don translate with AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even though we dey try make am correct, abeg note say automated translations fit get errors or inaccuracies. Di original dokument for im original language suppose be di authority. If na important information, make professional human translator check am. We no dey responsible for any misunderstanding or wrong interpretation wey fit happen from this translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->