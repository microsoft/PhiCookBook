<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a1c62bf7d86d6186bf8d3917196a92a0",
  "translation_date": "2025-05-09T20:42:10+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Kaito.md",
  "language_code": "ms"
}
-->
## Fine-Tuning with Kaito 

[Kaito](https://github.com/Azure/kaito) is an operator that automates the deployment of AI/ML inference models within a Kubernetes cluster.

Kaito offers several key advantages over most mainstream model deployment methods that rely on virtual machine infrastructures:

- Manage model files through container images. An HTTP server is provided to handle inference requests using the model library.
- Eliminate the need to adjust deployment parameters for GPU hardware by offering preset configurations.
- Automatically provision GPU nodes based on the model’s requirements.
- Host large model images in the public Microsoft Container Registry (MCR) if the license permits.

With Kaito, onboarding large AI inference models into Kubernetes becomes significantly simpler.


## Architecture

Kaito follows the traditional Kubernetes Custom Resource Definition (CRD)/controller design pattern. Users manage a `workspace` custom resource that specifies GPU requirements and inference details. Kaito controllers automate deployment by reconciling the `workspace` custom resource.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

The figure above shows an overview of Kaito’s architecture. Its main components include:

- **Workspace controller**: It reconciles the `workspace` custom resource, creates `machine` (explained below) custom resources to trigger node auto-provisioning, and creates the inference workload (`deployment` or `statefulset`) based on the model preset configurations.
- **Node provisioner controller**: This controller is called *gpu-provisioner* in the [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). It uses the `machine` CRD from [Karpenter](https://sigs.k8s.io/karpenter) to communicate with the workspace controller. It integrates with Azure Kubernetes Service (AKS) APIs to add new GPU nodes to the AKS cluster. 
> Note: The [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) is an open source component. It can be replaced by other controllers if they support [Karpenter-core](https://sigs.k8s.io/karpenter) APIs.

## Overview video 
[Watch the Kaito Demo](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)
## Installation

Please refer to the installation guide [here](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Quick start

After installing Kaito, you can run the following commands to start a fine-tuning service.

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

You can monitor the workspace status with the following command. When the WORKSPACEREADY column shows `True`, the model has been successfully deployed.

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

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.