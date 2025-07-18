<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e46691923dca7cb2f11d32b1d9d558e0",
  "translation_date": "2025-07-16T20:54:04+00:00",
  "source_file": "md/01.Introduction/03/Kaito_Inference.md",
  "language_code": "sl"
}
-->
## Inferenca s Kaito

[Kaito](https://github.com/Azure/kaito) je operator, ki avtomatizira uvajanje AI/ML modelov za inferenco v Kubernetes gruči.

Kaito se razlikuje od večine običajnih metod uvajanja modelov, ki temeljijo na infrastrukturi virtualnih strojev, na naslednje ključne načine:

- Upravljanje datotek modelov z uporabo slik kontejnerjev. Na voljo je http strežnik za izvajanje inferenčnih klicev z uporabo knjižnice modelov.
- Izogibanje nastavljanju parametrov uvajanja za prilagoditev GPU strojni opremi z vnaprej določenimi konfiguracijami.
- Samodejno zagotavljanje GPU vozlišč glede na zahteve modela.
- Gostovanje velikih slik modelov v javnem Microsoft Container Registry (MCR), če to dovoljuje licenca.

Z uporabo Kaitoa je postopek uvajanja velikih AI inferenčnih modelov v Kubernetesu precej poenostavljen.

## Arhitektura

Kaito sledi klasičnemu vzorcu zasnove Kubernetes Custom Resource Definition (CRD)/controller. Uporabnik upravlja s prilagojenim virom `workspace`, ki opisuje zahteve po GPU in specifikacijo inferenčnega modela. Kaito kontrolerji avtomatizirajo uvajanje z usklajevanjem prilagojenega vira `workspace`.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Kaito arhitektura" alt="Kaito arhitektura">
</div>

Zgornja slika prikazuje pregled arhitekture Kaitoa. Njegove glavne komponente so:

- **Workspace controller**: Usklajuje prilagojeni vir `workspace`, ustvarja prilagojene vire `machine` (pojasnjeno spodaj) za sprožitev samodejnega zagotavljanja vozlišč in ustvarja inferenčno delovno obremenitev (`deployment` ali `statefulset`) na podlagi vnaprej določenih konfiguracij modela.
- **Node provisioner controller**: Ime kontrolerja je *gpu-provisioner* v [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Uporablja `machine` CRD, ki izvira iz [Karpenter](https://sigs.k8s.io/karpenter), za interakcijo z workspace kontrolerjem. Integrira se z Azure Kubernetes Service (AKS) API-ji za dodajanje novih GPU vozlišč v AKS gruči.
> Opomba: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) je odprtokodna komponenta. Lahko jo nadomestijo drugi kontrolerji, če podpirajo [Karpenter-core](https://sigs.k8s.io/karpenter) API-je.

## Namestitev

Prosimo, preverite navodila za namestitev [tukaj](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Hiter začetek Inferenca Phi-3
[Primer kode Inferenca Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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

Status delovnega prostora lahko spremljate z izvajanjem naslednjega ukaza. Ko stolpec WORKSPACEREADY postane `True`, je model uspešno nameščen.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

Nato lahko poiščete IP gruče inferenčne storitve in uporabite začasni `curl` pod za testiranje končne točke storitve v gruči.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Hiter začetek Inferenca Phi-3 z adapterji

Po namestitvi Kaitoa lahko poskusite naslednje ukaze za zagon inferenčne storitve.

[Primer kode Inferenca Phi-3 z adapterji](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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

Status delovnega prostora lahko spremljate z izvajanjem naslednjega ukaza. Ko stolpec WORKSPACEREADY postane `True`, je model uspešno nameščen.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

Nato lahko poiščete IP gruče inferenčne storitve in uporabite začasni `curl` pod za testiranje končne točke storitve v gruči.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za avtomatski prevod AI [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za pomembne informacije priporočamo strokovni človeški prevod. Za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.