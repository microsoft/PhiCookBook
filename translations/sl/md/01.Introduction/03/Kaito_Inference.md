<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e46691923dca7cb2f11d32b1d9d558e0",
  "translation_date": "2025-05-09T12:01:19+00:00",
  "source_file": "md/01.Introduction/03/Kaito_Inference.md",
  "language_code": "sl"
}
-->
## Inference with Kaito 

[Kaito](https://github.com/Azure/kaito) je operator, ki avtomatizira uvajanje AI/ML inferenčnih modelov v Kubernetes gruči.

Kaito ima naslednje ključne prednosti v primerjavi z večino običajnih metod uvajanja modelov, ki temeljijo na virtualnih strojih:

- Upravljanje datotek modela z uporabo container slik. Na voljo je http strežnik za izvajanje inferenčnih klicev z uporabo knjižnice modelov.
- Izogibanje nastavljanju parametrov uvajanja za prilagoditev GPU strojni opremi s prednastavljenimi konfiguracijami.
- Samodejna priprava GPU vozlišč glede na zahteve modela.
- Gostovanje velikih slik modelov v javnem Microsoft Container Registry (MCR), če to dovoljuje licenca.

Z uporabo Kaito je potek vključevanja velikih AI inferenčnih modelov v Kubernetes močno poenostavljen.


## Arhitektura

Kaito sledi klasičnemu Kubernetes Custom Resource Definition (CRD)/controller vzorcu. Uporabnik upravlja s `workspace` custom resource, ki opisuje zahteve po GPU in specifikacijo inferenc. Kaito kontrolerji avtomatizirajo uvajanje z usklajevanjem tega `workspace` custom resource.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

Zgornja slika prikazuje pregled arhitekture Kaito. Njeni glavni sestavni deli so:

- **Workspace controller**: Usmerja usklajevanje `workspace` custom resource, ustvarja `machine` (pojasnjeno spodaj) custom resource za sprožitev samodejne priprave vozlišč in ustvarja inferenčno delovno obremenitev (`deployment` ali `statefulset`) glede na prednastavitve modela.
- **Node provisioner controller**: Ime kontrolerja je *gpu-provisioner* v [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Uporablja `machine` CRD, ki izvira iz [Karpenter](https://sigs.k8s.io/karpenter), za interakcijo z workspace controllerjem. Povezuje se z Azure Kubernetes Service (AKS) API-ji za dodajanje novih GPU vozlišč v AKS gruči.
> Note: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) je odprtokodna komponenta. Lahko jo nadomestijo drugi kontrolerji, če podpirajo [Karpenter-core](https://sigs.k8s.io/karpenter) API-je.

## Namestitev

Prosimo, preverite navodila za namestitev [tukaj](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Hiter začetek Inference Phi-3
[Primer kode Inference Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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

Status workspace lahko spremljate z izvajanjem naslednjega ukaza. Ko stolpec WORKSPACEREADY postane `True`, je model uspešno nameščen.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

Nato lahko poiščete cluster IP inferenčne storitve in uporabite začasen `curl` pod za testiranje končne točke storitve znotraj gruče.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Hiter začetek Inference Phi-3 z adapterji

Po namestitvi Kaito lahko poskusite naslednje ukaze za zagon inferenčne storitve.

[Primer kode Inference Phi-3 z adapterji](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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

Status workspace lahko spremljate z izvajanjem naslednjega ukaza. Ko stolpec WORKSPACEREADY postane `True`, je model uspešno nameščen.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

Nato lahko poiščete cluster IP inferenčne storitve in uporabite začasen `curl` pod za testiranje končne točke storitve znotraj gruče.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Opozorilo**:  
Ta dokument je bil preveden z uporabo storitve za avtomatski prevod AI [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za pomembne informacije priporočamo strokovni človeški prevod. Nismo odgovorni za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.