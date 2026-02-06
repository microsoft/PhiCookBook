## Fine-Tuning gamit ang Kaito

Ang [Kaito](https://github.com/Azure/kaito) ay isang operator na nag-a-automate ng AI/ML inference model deployment sa isang Kubernetes cluster.

May mga sumusunod na pangunahing pagkakaiba ang Kaito kumpara sa karamihan ng mga karaniwang pamamaraan ng model deployment na nakabase sa virtual machine infrastructures:

- Pinamamahalaan ang mga model file gamit ang container images. Mayroong http server na ibinibigay para magsagawa ng inference calls gamit ang model library.
- Iniiwasan ang pag-tune ng deployment parameters para umangkop sa GPU hardware sa pamamagitan ng pagbibigay ng preset configurations.
- Awtomatikong nagpo-provision ng GPU nodes base sa pangangailangan ng modelo.
- Ina-host ang malalaking model images sa public Microsoft Container Registry (MCR) kung pinapayagan ng lisensya.

Sa paggamit ng Kaito, ang workflow ng pag-onboard ng malalaking AI inference models sa Kubernetes ay mas pinasimple.

## Arkitektura

Sinasunod ng Kaito ang klasikong Kubernetes Custom Resource Definition (CRD)/controller design pattern. Ang user ang nagma-manage ng `workspace` custom resource na naglalarawan ng mga pangangailangan sa GPU at ang inference specification. Awtomatikong ino-operate ng mga Kaito controllers ang deployment sa pamamagitan ng pag-reconcile ng `workspace` custom resource.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

Ipinapakita ng larawan sa itaas ang pangkalahatang arkitektura ng Kaito. Ang mga pangunahing bahagi nito ay:

- **Workspace controller**: Ina-reconcile nito ang `workspace` custom resource, lumilikha ng `machine` (ipinaliwanag sa ibaba) custom resources para mag-trigger ng node auto provisioning, at lumilikha ng inference workload (`deployment` o `statefulset`) base sa preset configurations ng modelo.
- **Node provisioner controller**: Ang pangalan ng controller ay *gpu-provisioner* sa [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Ginagamit nito ang `machine` CRD na nagmula sa [Karpenter](https://sigs.k8s.io/karpenter) para makipag-ugnayan sa workspace controller. Nakikipag-integrate ito sa Azure Kubernetes Service (AKS) APIs para magdagdag ng bagong GPU nodes sa AKS cluster.
> Note: Ang [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) ay isang open sourced na bahagi. Maaari itong palitan ng ibang controllers kung sinusuportahan nila ang [Karpenter-core](https://sigs.k8s.io/karpenter) APIs.

## Pangkalahatang video
[Panoorin ang Kaito Demo](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)

## Pag-install

Mangyaring tingnan ang gabay sa pag-install [dito](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Mabilis na pagsisimula

Pagkatapos ma-install ang Kaito, maaaring subukan ang mga sumusunod na utos para simulan ang fine-tuning service.

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

Maaaring subaybayan ang status ng workspace sa pamamagitan ng pagpapatakbo ng sumusunod na utos. Kapag ang WORKSPACEREADY na kolum ay naging `True`, matagumpay nang na-deploy ang modelo.

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

Sunod, maaaring hanapin ang cluster ip ng inference service at gumamit ng pansamantalang `curl` pod para subukan ang service endpoint sa cluster.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.