<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a1c62bf7d86d6186bf8d3917196a92a0",
  "translation_date": "2025-05-09T20:42:18+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Kaito.md",
  "language_code": "tl"
}
-->
## Fine-Tuning gamit ang Kaito

Ang [Kaito](https://github.com/Azure/kaito) ay isang operator na nag-a-automate ng deployment ng AI/ML inference model sa isang Kubernetes cluster.

Ang Kaito ay may mga sumusunod na pangunahing pagkakaiba kumpara sa karamihan ng mga karaniwang pamamaraan ng model deployment na nakabase sa virtual machine infrastructures:

- Pinamamahalaan ang mga model file gamit ang container images. Mayroong http server na ibinibigay para magsagawa ng inference calls gamit ang model library.
- Hindi na kailangang i-tune ang deployment parameters para umangkop sa GPU hardware dahil may preset configurations na.
- Awtomatikong nagpo-provision ng GPU nodes base sa pangangailangan ng model.
- Nagho-host ng malalaking model images sa public Microsoft Container Registry (MCR) kung pinapayagan ng lisensya.

Gamit ang Kaito, mas pinasimple ang workflow ng pag-onboard ng malalaking AI inference models sa Kubernetes.

## Arkitektura

Sinusunod ng Kaito ang klasikong Kubernetes Custom Resource Definition(CRD)/controller design pattern. Pinamamahalaan ng user ang isang `workspace` custom resource na naglalarawan ng GPU requirements at inference specification. Ina-automate ng Kaito controllers ang deployment sa pamamagitan ng pag-reconcile ng `workspace` custom resource.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

Ipinapakita ng larawan sa itaas ang overview ng arkitektura ng Kaito. Ang mga pangunahing bahagi nito ay:

- **Workspace controller**: Ire-reconcile nito ang `workspace` custom resource, gagawa ng `machine` (ipinaliwanag sa ibaba) custom resources para i-trigger ang node auto provisioning, at gagawa ng inference workload (`deployment` o `statefulset`) base sa preset configurations ng model.
- **Node provisioner controller**: Ang pangalan ng controller ay *gpu-provisioner* sa [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Ginagamit nito ang `machine` CRD na nagmula sa [Karpenter](https://sigs.k8s.io/karpenter) para makipag-ugnayan sa workspace controller. Nakikipag-integrate ito sa Azure Kubernetes Service(AKS) APIs para magdagdag ng bagong GPU nodes sa AKS cluster.
> Note: Ang [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) ay isang open sourced na component. Maaari itong palitan ng ibang controllers kung sinusuportahan nila ang [Karpenter-core](https://sigs.k8s.io/karpenter) APIs.

## Overview video  
[Panoorin ang Kaito Demo](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)

## Pag-install

Pakitingnan ang gabay sa pag-install [dito](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Mabilis na pagsisimula

Pagkatapos ma-install ang Kaito, maaaring subukan ang mga sumusunod na utos para magsimula ng fine-tuning service.

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

Maaaring subaybayan ang status ng workspace gamit ang sumusunod na utos. Kapag ang WORKSPACEREADY na kolum ay naging `True`, matagumpay nang na-deploy ang model.

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

Susunod, maaaring hanapin ang cluster ip ng inference service at gamitin ang pansamantalang `curl` pod para subukan ang service endpoint sa cluster.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa kanyang sariling wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.