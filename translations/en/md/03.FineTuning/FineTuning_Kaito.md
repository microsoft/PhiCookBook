## Fine-Tuning with Kaito 

[Kaito](https://github.com/Azure/kaito) is an operator that automates the deployment of AI/ML inference models in a Kubernetes cluster.

Kaito offers the following key advantages compared to most mainstream model deployment methods built on virtual machine infrastructures:

- Manage model files through container images. An HTTP server is provided to handle inference requests using the model library.
- Eliminate the need to adjust deployment parameters for specific GPU hardware by offering preset configurations.
- Automatically provision GPU nodes based on model requirements.
- Host large model images in the public Microsoft Container Registry (MCR) if licensing permits.

With Kaito, the process of onboarding large AI inference models in Kubernetes is greatly simplified.

## Architecture

Kaito follows the classic Kubernetes Custom Resource Definition (CRD)/controller design pattern. Users manage a `workspace` custom resource that specifies GPU requirements and inference details. Kaito controllers automate deployment by reconciling the `workspace` custom resource.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

The diagram above shows an overview of Kaito’s architecture. Its main components include:

- **Workspace controller**: This reconciles the `workspace` custom resource, creates `machine` (explained below) custom resources to trigger node auto-provisioning, and creates the inference workload (`deployment` or `statefulset`) based on the model’s preset configurations.
- **Node provisioner controller**: Known as *gpu-provisioner* in the [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner), this controller uses the `machine` CRD from [Karpenter](https://sigs.k8s.io/karpenter) to interact with the workspace controller. It integrates with Azure Kubernetes Service (AKS) APIs to add new GPU nodes to the AKS cluster. 
> Note: The [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) is an open-source component. It can be replaced by other controllers if they support [Karpenter-core](https://sigs.k8s.io/karpenter) APIs.

## Overview video 
[Watch the Kaito Demo](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)

## Installation

Please refer to the installation guide [here](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Quick start

After installing Kaito, you can try the following commands to start a fine-tuning service.

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

You can monitor the workspace status by running the following command. When the WORKSPACEREADY column shows `True`, the model has been successfully deployed.

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

Next, find the inference service’s cluster IP and use a temporary `curl` pod to test the service endpoint within the cluster.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.