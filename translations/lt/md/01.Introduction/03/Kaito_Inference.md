<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e46691923dca7cb2f11d32b1d9d558e0",
  "translation_date": "2025-09-12T14:56:09+00:00",
  "source_file": "md/01.Introduction/03/Kaito_Inference.md",
  "language_code": "lt"
}
-->
## Inference su Kaito

[Kaito](https://github.com/Azure/kaito) yra operatorius, kuris automatizuoja AI/ML modelių įdiegimą Kubernetes klasteryje.

Kaito turi šiuos pagrindinius skirtumus, palyginti su dauguma tradicinių modelių diegimo metodų, pagrįstų virtualių mašinų infrastruktūra:

- Modelių failai valdomi naudojant konteinerių atvaizdus. Pateikiamas HTTP serveris, leidžiantis atlikti inferencijos užklausas naudojant modelių biblioteką.
- Vengiama derinti diegimo parametrus, kad jie atitiktų GPU aparatinę įrangą, pateikiant iš anksto nustatytas konfigūracijas.
- Automatiškai priskiriami GPU mazgai pagal modelio reikalavimus.
- Dideli modelių atvaizdai talpinami viešajame Microsoft Container Registry (MCR), jei tai leidžia licencija.

Naudojant Kaito, didelių AI inferencijos modelių įdiegimo procesas Kubernetes klasteryje yra žymiai supaprastintas.

## Architektūra

Kaito naudoja klasikinį Kubernetes Custom Resource Definition (CRD) / valdiklio dizaino modelį. Vartotojas valdo `workspace` pasirinktą resursą, kuris aprašo GPU reikalavimus ir inferencijos specifikaciją. Kaito valdikliai automatizuoja diegimą, suderindami `workspace` pasirinktą resursą.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Kaito architektūra" alt="Kaito architektūra">
</div>

Aukščiau pateiktame paveikslėlyje parodyta Kaito architektūros apžvalga. Pagrindiniai komponentai yra:

- **Workspace valdiklis**: Jis suderina `workspace` pasirinktą resursą, sukuria `machine` (paaiškinta žemiau) pasirinktus resursus, kad inicijuotų mazgų automatinį priskyrimą, ir sukuria inferencijos darbo krūvį (`deployment` arba `statefulset`) pagal modelio iš anksto nustatytas konfigūracijas.
- **Mazgų priskyrimo valdiklis**: Šio valdiklio pavadinimas yra *gpu-provisioner* [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Jis naudoja `machine` CRD, kilusį iš [Karpenter](https://sigs.k8s.io/karpenter), kad sąveikautų su workspace valdikliu. Jis integruojasi su Azure Kubernetes Service (AKS) API, kad pridėtų naujus GPU mazgus į AKS klasterį. 
> Pastaba: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) yra atvirojo kodo komponentas. Jį galima pakeisti kitais valdikliais, jei jie palaiko [Karpenter-core](https://sigs.k8s.io/karpenter) API.

## Diegimas

Prašome peržiūrėti diegimo instrukcijas [čia](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Greitas startas: Inferencija Phi-3
[Pavyzdinis kodas inferencijai Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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

Workspace būseną galima stebėti vykdant šią komandą. Kai WORKSPACEREADY stulpelis tampa `True`, modelis sėkmingai įdiegtas.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

Tada galima rasti inferencijos paslaugos klasterio IP ir naudoti laikiną `curl` podą, kad būtų galima išbandyti paslaugos galinį tašką klasteryje.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Greitas startas: Inferencija Phi-3 su adapteriais

Įdiegus Kaito, galima išbandyti šias komandas, kad pradėtumėte inferencijos paslaugą.

[Pavyzdinis kodas inferencijai Phi-3 su adapteriais](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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

Workspace būseną galima stebėti vykdant šią komandą. Kai WORKSPACEREADY stulpelis tampa `True`, modelis sėkmingai įdiegtas.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

Tada galima rasti inferencijos paslaugos klasterio IP ir naudoti laikiną `curl` podą, kad būtų galima išbandyti paslaugos galinį tašką klasteryje.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors stengiamės užtikrinti tikslumą, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.