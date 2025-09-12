<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a1c62bf7d86d6186bf8d3917196a92a0",
  "translation_date": "2025-09-12T14:39:08+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Kaito.md",
  "language_code": "lt"
}
-->
## Modelio pritaikymas su Kaito

[Kaito](https://github.com/Azure/kaito) yra operatorius, kuris automatizuoja AI/ML modelių įdiegimą Kubernetes klasteryje.

Kaito turi šiuos pagrindinius privalumus, palyginti su dauguma tradicinių modelių diegimo metodų, sukurtų virtualių mašinų infrastruktūrose:

- Modelio failų valdymas naudojant konteinerių atvaizdus. Teikiamas HTTP serveris, skirtas atlikti modelio bibliotekos užklausas.
- Vengia derinti diegimo parametrus, kad atitiktų GPU aparatinę įrangą, pateikdamas iš anksto nustatytas konfigūracijas.
- Automatiškai priskiria GPU mazgus pagal modelio reikalavimus.
- Talpina didelius modelio atvaizdus viešame Microsoft Container Registry (MCR), jei tai leidžia licencija.

Naudojant Kaito, didelių AI modelių įdiegimo procesas Kubernetes klasteryje tampa gerokai paprastesnis.

## Architektūra

Kaito naudoja klasikinį Kubernetes Custom Resource Definition (CRD) / valdiklio dizaino modelį. Vartotojas valdo `workspace` (darbo aplinkos) išteklių, kuris aprašo GPU reikalavimus ir užklausų specifikaciją. Kaito valdikliai automatizuoja diegimą, suderindami `workspace` išteklių.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito architektūra" alt="Kaito architektūra">
</div>

Aukščiau pateikta schema parodo Kaito architektūros apžvalgą. Pagrindiniai komponentai yra:

- **Workspace valdiklis**: Jis suderina `workspace` išteklių, sukuria `machine` (paaiškinta žemiau) išteklius, kad inicijuotų mazgų automatinį priskyrimą, ir sukuria užklausų darbo krūvį (`deployment` arba `statefulset`) pagal modelio iš anksto nustatytas konfigūracijas.
- **Mazgų priskyrimo valdiklis**: Šio valdiklio pavadinimas yra *gpu-provisioner* [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Jis naudoja `machine` CRD, kilusį iš [Karpenter](https://sigs.k8s.io/karpenter), kad sąveikautų su workspace valdikliu. Jis integruojasi su Azure Kubernetes Service (AKS) API, kad pridėtų naujus GPU mazgus į AKS klasterį.  
> Pastaba: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) yra atvirojo kodo komponentas. Jį galima pakeisti kitais valdikliais, jei jie palaiko [Karpenter-core](https://sigs.k8s.io/karpenter) API.

## Apžvalgos vaizdo įrašas 
[Žiūrėti Kaito demonstraciją](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)

## Įdiegimas

Įdiegimo instrukcijas rasite [čia](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Greitas startas

Įdiegus Kaito, galima išbandyti šias komandas, kad pradėtumėte modelio pritaikymo paslaugą.

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

Darbo aplinkos būseną galima stebėti vykdant šią komandą. Kai WORKSPACEREADY stulpelis tampa `True`, modelis sėkmingai įdiegtas.

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

Toliau galima rasti užklausų paslaugos klasterio IP ir naudoti laikiną `curl` podą, kad patikrintumėte paslaugos galinį tašką klasteryje.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Dėl svarbios informacijos rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius naudojant šį vertimą.