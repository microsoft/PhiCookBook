## Inferenca s Kaito

[Kaito](https://github.com/Azure/kaito) je operator, ki avtomatizira namestitev AI/ML modela za inferenco v Kubernetes gruči.

Kaito se od večine glavnih metodologij za nameščanje modelov, ki so zgrajene na infrastrukturi navideznih strojev, razlikuje po naslednjih ključnih točkah:

- Upravljanje datotek modela z uporabo vsebniških slik. Na voljo je http strežnik za izvajanje inferenčnih klicev z uporabo knjižnice modela.
- Izogibanje nastavljanju parametrov nameščanja za prilagoditev GPU strojni opremi z zagotavljanjem vnaprej nastavljenih konfiguracij.
- Samodejno zagotavljanje GPU vozlišč glede na zahteve modela.
- Gostovanje velikih slik modelov v javnem Microsoft Container Registry (MCR), če to dovoljuje licenca.

Z uporabo Kaitoa je potek uvajanja velikih AI inferenčnih modelov v Kubernetesu močno poenostavljen.


## Arhitektura

Kaito sledi klasičnemu Kubernetes vzorcu za Custom Resource Definition (CRD)/kontroler. Uporabnik upravlja z lastnim virom `workspace`, ki opisuje zahteve po GPU in specifikacijo inferenc. Kaito kontrolerji avtomatizirajo nameščanje z usklajevanjem lastnega vira `workspace`.

<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/website/static/img/ragarch.png" width=80% title="KAITO RAGEngine arhitektura" alt="KAITO RAGEngine arhitektura">
</div>

Zgornja slika prikazuje pregled arhitekture Kaitoa. Njene glavne sestavine so:

- **Workspace kontroler**: Usklajuje lastni vir `workspace`, ustvarja lastne vire `machine` (razložene spodaj) za sprožitev samodejnega zagotavljanja vozlišč in ustvarja inferenčno delovno obremenitev (`deployment` ali `statefulset`) na podlagi vnaprej nastavljenih konfiguracij modela.
- **Node provisioner kontroler**: Ime kontrolerja je *gpu-provisioner* v [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Uporablja `machine` CRD, ki izvira iz [Karpenter](https://sigs.k8s.io/karpenter), za interakcijo s kontrolerjem workspace. Integrira se z Azure Kubernetes Service (AKS) API-ji za dodajanje novih GPU vozlišč v AKS gručo.
> Opomba: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) je odprtokodna komponenta. Lahko ga nadomestijo drugi kontrolerji, če podpirajo [Karpenter-core](https://sigs.k8s.io/karpenter) API-je.

## Namestitev

Za navodila za namestitev si oglejte [tukaj](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Hitri začetek Inferenca Phi-3
[Vzorec kode Inferenca Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Prilagajanje poti izhoda ACR
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3.yaml
```

Stanje workspace-a lahko spremljate z izvajanjem naslednjega ukaza. Ko stolpec WORKSPACEREADY postane `True`, je bil model uspešno nameščen.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

Nato lahko poiščete klasterski IP inferenčne storitve in s pomočjo začasnega `curl` poda preizkusite končno točko storitve v gruči.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Hitri začetek Inferenca Phi-3 z adapterji

Po namestitvi Kaitoa lahko poskusite naslednje ukaze za zagon inferenčne storitve.

[Vzorec kode Inferenca Phi-3 z adapterji](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Nastavitev izhodne poti ACR
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3_with_adapters.yaml
```

Stanje workspace-a lahko spremljate z izvajanjem naslednjega ukaza. Ko stolpec WORKSPACEREADY postane `True`, je bil model uspešno nameščen.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

Nato lahko poiščete klasterski IP inferenčne storitve in s pomočjo začasnega `curl` poda preizkusite končno točko storitve v gruči.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Opozorilo**:
Ta dokument je bil preveden z uporabo storitve za avtomatski prevod AI [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku se šteje za avtoritativni vir. Za kritične informacije priporočamo strokovni človeški prevod. Nismo odgovorni za morebitne nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->