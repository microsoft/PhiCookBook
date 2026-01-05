<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aca91084bc440431571e00bf30d96ab8",
  "translation_date": "2026-01-05T09:29:05+00:00",
  "source_file": "md/01.Introduction/03/Kaito_Inference.md",
  "language_code": "hu"
}
-->
## Inference a Kaitóval

A [Kaito](https://github.com/Azure/kaito) egy olyan operátor, amely automatizálja az AI/ML inferencia modellek telepítését egy Kubernetes klaszterben.

A Kaito a következő főbb különbségekkel rendelkezik a legtöbb, virtuális gép infrastruktúrákra épülő mainstream modelltelepítési módszerhez képest:

- A modellfájlokat konténer képek segítségével kezeli. Egy http szerver áll rendelkezésre, amely az inferencia hívásokat a modellkönyvtár használatával végzi.
- Elkerüli a GPU hardverhez való illeszkedő telepítési paraméterek hangolását előre beállított konfigurációk biztosításával.
- Automatikusan biztosít GPU node-okat a modell igényei alapján.
- Nagy modell képeket helyez el a nyilvános Microsoft Container Registry-ben (MCR), ha a licenc engedi.

A Kaitóval az AI inferencia modellek Kubernetes-be történő bekerülési folyamata nagymértékben egyszerűsödik.

## Architektúra

A Kaito követi a klasszikus Kubernetes Custom Resource Definition(CRD)/controller tervezési mintát. A felhasználó egy `workspace` egyedi erőforrást kezel, amely leírja a GPU követelményeket és az inferencia specifikációt. A Kaito kontroller automatikusan elvégzi a telepítést a `workspace` egyedi erőforrás összehangolásával.

<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/website/static/img/ragarch.png" width=80% title="KAITO RAGEngine architektúra" alt="KAITO RAGEngine architektúra">
</div>

A fenti ábra a Kaito architektúra áttekintését mutatja. Fő összetevői:

- **Workspace kontroller**: Összehangolja a `workspace` egyedi erőforrást, létrehozza a `machine` (lentebb magyarázva) egyedi erőforrásokat a node automatikus biztosításának elindítására, és a modell előre beállított konfigurációi alapján létrehozza az inferencia munkaterhelést (`deployment` vagy `statefulset`).
- **Node biztosító kontroller**: A kontroller neve *gpu-provisioner* a [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) alatt. A `machine` CRD-t használja, amely a [Karpenter](https://sigs.k8s.io/karpenter)-től származik, hogy kommunikáljon a workspace kontrollerrel. Integrálódik az Azure Kubernetes Service (AKS) API-kkal, hogy új GPU node-okat adjon az AKS klaszterhez.
> Megjegyzés: A [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) nyílt forráskódú komponens. Más kontrollerek is helyettesíthetik, ha támogatják a [Karpenter-core](https://sigs.k8s.io/karpenter) API-kat.

## Telepítés

Kérjük, tekintse meg a telepítési útmutatót [itt](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Gyors indítás Inference Phi-3
[Phi-3 példa kód](https://github.com/Azure/kaito/tree/main/examples/inference)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # ACR kimeneti út hangolása
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3.yaml
```

A workspace állapotát az alábbi paranccsal lehet nyomon követni. Amikor a WORKSPACEREADY oszlop `True` értéket vesz fel, a modell sikeresen telepítve lett.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

Ezután meg lehet találni az inferencia szolgáltatás klaszter IP-címét, és egy ideiglenes `curl` pod használatával tesztelni lehet a szolgáltatás végpontját a klaszterben.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Gyors indítás Inference Phi-3 adapterekkel

A Kaito telepítése után az alábbi parancsokkal elindítható egy inferencia szolgáltatás.

[Phi-3 példa kód adapterekkel](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Kimenő ACR útvonal hangolása
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3_with_adapters.yaml
```

A workspace állapotát az alábbi paranccsal lehet nyomon követni. Amikor a WORKSPACEREADY oszlop `True` értéket vesz fel, a modell sikeresen telepítve lett.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

Ezután meg lehet találni az inferencia szolgáltatás klaszter IP-címét, és egy ideiglenes `curl` pod használatával tesztelni lehet a szolgáltatás végpontját a klaszterben.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Jelen dokumentumot az AI fordítószolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével fordítottuk. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások tartalmazhatnak hibákat vagy pontatlanságokat. Az eredeti dokumentum anyanyelvű változata tekintendő hiteles forrásnak. Fontos információk esetén szakmai emberi fordítást javasolt igénybe venni. Nem vállalunk felelősséget a fordítás használatából eredő bármilyen félreértésért vagy félreértelmezésért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->