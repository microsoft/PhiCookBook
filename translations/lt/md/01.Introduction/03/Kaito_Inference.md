<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aca91084bc440431571e00bf30d96ab8",
  "translation_date": "2026-01-05T16:09:29+00:00",
  "source_file": "md/01.Introduction/03/Kaito_Inference.md",
  "language_code": "lt"
}
-->
## Išvados su Kaito

[Kaito](https://github.com/Azure/kaito) yra operatorius, kuris automatizuoja AI/ML išvados modelių diegimą Kubernetes klasteryje.

Kaito turi šiuos pagrindinius skirtumus, palyginti su dauguma pagrindinių modelių diegimo metodų, sukurtų ant virtualių mašinų infrastruktūrų:

- Valdo modelio failus naudodamas konteinerių vaizdus. HTTP serveris suteikiamas išvados kvietimams atlikti naudojant modelio biblioteką.
- Vengia diegimo parametrų derinimo GPU aparatūrai, teikdamas iš anksto nustatytas konfigūracijas.
- Automatiškai priskiria GPU mazgus pagal modelio reikalavimus.
- Talpina didelius modelių vaizdus viešajame Microsoft Container Registry (MCR), jei licencija tai leidžia.

Naudojant Kaito, didelių AI išvados modelių įkėlimo į Kubernetes procesas yra žymiai supaprastintas.

## Architektūra

Kaito laikosi klasikinio Kubernetes Custom Resource Definition (CRD)/valdiklio dizaino modelio. Vartotojas valdo `workspace` papildomą išteklių objektą, kuris aprašo GPU reikalavimus ir išvados specifikaciją. Kaito valdikliai automatiškai diegia, suderindami `workspace` papildomą išteklių objektą.

<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/website/static/img/ragarch.png" width=80% title="KAITO RAGEngine architektūra" alt="KAITO RAGEngine architektūra">
</div>

Aukščiau pateiktame paveikslėlyje matomas Kaito architektūros apžvalga. Jos pagrindiniai komponentai yra:

- **Workspace valdiklis**: Jis suderina `workspace` papildomą išteklių objektą, sukuria `machine` (paaiškinta žemiau) papildomus išteklius naujų mazgų automatinio priskyrimo paleidimui ir sukuria išvados apkrovą (`deployment` arba `statefulset`), remdamasis modelio iš anksto nustatytomis konfigūracijomis.
- **Mazgų priskyrimo valdiklis**: Valdiklio pavadinimas yra *gpu-provisioner* [gpu-provisioner helm charte](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Jis naudoja `machine` CRD, kilusį iš [Karpenter](https://sigs.k8s.io/karpenter), bendrauti su workspace valdikliu. Jis integruojasi su Azure Kubernetes Service (AKS) API, kad pridėtų naujus GPU mazgus AKS klasteriui.
> Pastaba: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) yra atviro kodo komponentas. Jis gali būti pakeistas kitais valdikliais, jei palaiko [Karpenter-core](https://sigs.k8s.io/karpenter) API.

## Diegimas

Prašome patikrinti diegimo gaires [čia](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Greitas paleidimas Išvado Phi-3
[Pavyzdinis kodas Išvada Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Derinamas išvesties ACR kelias
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3.yaml
```

`workspace` būseną galima sekti vykdant šią komandą. Kai WORKSPACEREADY stulpelis tampa `True`, modelis sėkmingai įdiegtas.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

Toliau, galima rasti išvados paslaugos klasterio IP ir naudoti laikinuosius `curl` pod’ą paslaugos galui teste atlikti klastryje.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Greitas paleidimas Išvada Phi-3 su adapteriais

Įdiegus Kaito, galima išbandyti šias komandas, kad paleisti išvados paslaugą.

[Pavyzdinis kodas Išvada Phi-3 su adapteriais](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Išvesties ACR kelio derinimas
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3_with_adapters.yaml
```

`workspace` būseną galima sekti vykdant šią komandą. Kai WORKSPACEREADY stulpelis tampa `True`, modelis sėkmingai įdiegtas.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

Toliau galima rasti išvados paslaugos klasterio IP ir naudoti laikinuosius `curl` pod’ą paslaugos galui teste atlikti klastryje.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors stengiamės užtikrinti tikslumą, prašome atkreipti dėmesį, kad automatizuoti vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas gimtąja kalba turėtų būti laikomas tikruoju šaltiniu. Kritinei informacijai rekomenduojamas profesionalus žmogaus vertimas. Mes neatsakome už bet kokius nesusipratimus ar neteisingus aiškinimus, kilusius dėl šio vertimo naudojimo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->