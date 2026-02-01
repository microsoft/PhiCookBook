## Pagsusuri gamit ang Kaito

Ang [Kaito](https://github.com/Azure/kaito) ay isang operator na nag-automate ng AI/ML inference model deployment sa isang Kubernetes cluster.

Ang Kaito ay may mga sumusunod na pangunahing pagkakaiba kumpara sa karamihan ng mga karaniwang metodolohiyang deployment ng modelo na binuo sa ibabaw ng virtual machine infrastructures:

- Pamahalaan ang mga modelong file gamit ang container images. Mayroong isang http server na ibinibigay para magsagawa ng inference calls gamit ang model library.
- Iwasan ang pag-tune ng deployment parameters para umangkop sa GPU hardware sa pamamagitan ng pagbibigay ng mga preset configurations.
- Auto-provision ng mga GPU nodes base sa mga kinakailangan ng modelo.
- I-host ang malalaking model images sa pampublikong Microsoft Container Registry (MCR) kung pinapayagan ng lisensya.

Gamit ang Kaito, ang workflow ng pag-onboard ng malalaking AI inference models sa Kubernetes ay malaki ang pinasimple.

## Arkitektura

Sinusunod ng Kaito ang klasikong Kubernetes Custom Resource Definition (CRD)/controller design pattern. Pinamamahalaan ng user ang isang `workspace` custom resource na naglalarawan ng mga kinakailangan sa GPU at ang inferensyang espesipikasyon. Awtomatikong gagawin ng Kaito controllers ang deployment sa pamamagitan ng pag-reconcile ng `workspace` custom resource.

<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/website/static/img/ragarch.png" width=80% title="KAITO RAGEngine architecture" alt="KAITO RAGEngine architecture">
</div>

Ipinapakita ng larawang nasa itaas ang pangkalahatang arkitektura ng Kaito. Ang mga pangunahing bahagi nito ay binubuo ng:

- **Workspace controller**: Pinag-uugnay nito ang `workspace` custom resource, lumilikha ng mga `machine` (ipinaliwanag sa ibaba) custom resources upang mag-trigger ng node auto provisioning, at lumilikha ng inference workload (`deployment` o `statefulset`) base sa mga preset na configuration ng modelo.
- **Node provisioner controller**: Ang pangalan ng controller na ito ay *gpu-provisioner* sa [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Ginagamit nito ang `machine` CRD na pinagmulan mula sa [Karpenter](https://sigs.k8s.io/karpenter) upang makipag-ugnayan sa workspace controller. Nakikipag-integrate ito sa Azure Kubernetes Service (AKS) APIs para magdagdag ng mga bagong GPU nodes sa AKS cluster.
> Tandaan: Ang [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) ay isang open sourced na bahagi. Maaari itong palitan ng ibang controllers kung sinusuportahan nila ang [Karpenter-core](https://sigs.k8s.io/karpenter) APIs.

## Pag-install

Mangyaring tingnan ang gabay sa pag-install [dito](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Mabilisang Simula sa Pagsusuri ng Phi-3
[Sample Code Pagsusuri ng Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Pag-aayos ng Output ACR Path
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3.yaml
```

Maaaring subaybayan ang status ng workspace sa pamamagitan ng pagpapatakbo ng sumusunod na utos. Kapag ang WORKSPACEREADY column ay naging `True`, matagumpay nang na-deploy ang modelo.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

Susunod, maaari mong hanapin ang cluster ip ng inference service at gamitin ang isang panandaliang `curl` pod para subukan ang service endpoint sa cluster.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Mabilisang Simula sa Pagsusuri ng Phi-3 gamit ang mga adapters

Pagkatapos i-install ang Kaito, maaaring subukan ang mga sumusunod na utos upang simulan ang isang inference service.

[Sample Code Pagsusuri ng Phi-3 gamit ang Adapters](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Pag-aayos ng Output ACR Path
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3_with_adapters.yaml
```

Maaaring subaybayan ang status ng workspace sa pamamagitan ng pagpapatakbo ng sumusunod na utos. Kapag ang WORKSPACEREADY column ay naging `True`, matagumpay nang na-deploy ang modelo.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

Susunod, maaari mong hanapin ang cluster ip ng inference service at gamitin ang isang panandaliang `curl` pod para subukan ang service endpoint sa cluster.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtataya**:
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagaman nagsusumikap kami para sa katumpakan, pakiusap na tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi eksaktong impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pinakamaaasahang sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaintindihan o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->