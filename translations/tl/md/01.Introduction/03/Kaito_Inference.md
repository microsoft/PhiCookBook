<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e46691923dca7cb2f11d32b1d9d558e0",
  "translation_date": "2025-05-09T11:57:24+00:00",
  "source_file": "md/01.Introduction/03/Kaito_Inference.md",
  "language_code": "tl"
}
-->
## Inference gamit ang Kaito

Ang [Kaito](https://github.com/Azure/kaito) ay isang operator na nag-a-automate ng AI/ML inference model deployment sa isang Kubernetes cluster.

May mga sumusunod na pangunahing pagkakaiba ang Kaito kumpara sa karamihan ng mga karaniwang pamamaraan ng model deployment na nakabase sa virtual machine infrastructures:

- Pinamamahalaan ang mga model file gamit ang container images. Mayroong http server para magsagawa ng inference calls gamit ang model library.
- Hindi na kailangang i-tune ang deployment parameters para umangkop sa GPU hardware dahil may preset configurations na.
- Awtomatikong nagpo-provision ng GPU nodes base sa pangangailangan ng modelo.
- Puwedeng i-host ang malalaking model images sa public Microsoft Container Registry (MCR) kung pinapayagan ng lisensya.

Gamit ang Kaito, ang proseso ng pag-onboard ng malalaking AI inference models sa Kubernetes ay mas pinasimple.

## Arkitektura

Sinusunod ng Kaito ang klasikong Kubernetes Custom Resource Definition(CRD)/controller design pattern. Ang user ang nagma-manage ng `workspace` custom resource na naglalarawan ng GPU requirements at inference specification. Ang mga Kaito controllers ang mag-a-automate ng deployment sa pamamagitan ng pag-reconcile ng `workspace` custom resource.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

Ipinapakita sa larawan sa itaas ang overview ng Kaito arkitektura. Ang mga pangunahing bahagi nito ay:

- **Workspace controller**: Ito ang nagre-reconcile ng `workspace` custom resource, lumilikha ng `machine` (ipinaliwanag sa ibaba) custom resources para i-trigger ang node auto provisioning, at lumilikha ng inference workload (`deployment` o `statefulset`) base sa preset configurations ng modelo.
- **Node provisioner controller**: Ang pangalan ng controller ay *gpu-provisioner* sa [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Ginagamit nito ang `machine` CRD mula sa [Karpenter](https://sigs.k8s.io/karpenter) para makipag-ugnayan sa workspace controller. Nakikipag-integrate ito sa Azure Kubernetes Service(AKS) APIs para magdagdag ng bagong GPU nodes sa AKS cluster. 
> Note: Ang [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) ay isang open sourced na component. Puwedeng palitan ito ng ibang controllers kung sinusuportahan nila ang [Karpenter-core](https://sigs.k8s.io/karpenter) APIs.

## Pag-install

Pakitingnan ang gabay sa pag-install [dito](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Mabilis na pagsisimula sa Inference Phi-3
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

Masusubaybayan ang status ng workspace sa pamamagitan ng pagpapatakbo ng sumusunod na utos. Kapag ang WORKSPACEREADY column ay naging `True`, matagumpay na na-deploy ang modelo.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

Sunod, puwedeng hanapin ang cluster ip ng inference service at gumamit ng pansamantalang `curl` pod para subukan ang service endpoint sa cluster.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Mabilis na pagsisimula sa Inference Phi-3 gamit ang adapters

Pagkatapos ma-install ang Kaito, puwedeng subukan ang mga sumusunod na utos para magsimula ng inference service.

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

Masusubaybayan ang status ng workspace sa pamamagitan ng pagpapatakbo ng sumusunod na utos. Kapag ang WORKSPACEREADY column ay naging `True`, matagumpay na na-deploy ang modelo.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

Sunod, puwedeng hanapin ang cluster ip ng inference service at gumamit ng pansamantalang `curl` pod para subukan ang service endpoint sa cluster.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagaman nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong salin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa kanyang sariling wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.