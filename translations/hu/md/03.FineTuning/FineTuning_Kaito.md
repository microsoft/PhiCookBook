<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a1c62bf7d86d6186bf8d3917196a92a0",
  "translation_date": "2025-07-17T06:24:37+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Kaito.md",
  "language_code": "hu"
}
-->
## Finomhangolás Kaitóval

[Kaito](https://github.com/Azure/kaito) egy operátor, amely automatizálja az AI/ML inferencia modellek telepítését Kubernetes klaszterben.

A Kaito a következő főbb különbségekkel rendelkezik a legtöbb, virtuális gép infrastruktúrákra épülő modelltelepítési módszerhez képest:

- A modellfájlokat konténerképek segítségével kezeli. Egy http szerver áll rendelkezésre az inferencia hívások végrehajtásához a modellkönyvtár használatával.
- Előre beállított konfigurációkat kínál, így nem kell a telepítési paramétereket a GPU hardverhez igazítani.
- Automatikusan biztosít GPU node-okat a modell igényei alapján.
- Nagy modellképeket tárolhat a nyilvános Microsoft Container Registry-ben (MCR), ha a licenc engedélyezi.

A Kaitóval az AI inferencia modellek Kubernetesbe való integrálása jelentősen leegyszerűsödik.

## Architektúra

A Kaito a klasszikus Kubernetes Custom Resource Definition (CRD)/controller tervezési mintát követi. A felhasználó egy `workspace` egyedi erőforrást kezel, amely leírja a GPU igényeket és az inferencia specifikációt. A Kaito kontrollerek automatikusan végrehajtják a telepítést a `workspace` egyedi erőforrás összehangolásával.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

A fenti ábra a Kaito architektúra áttekintését mutatja. Főbb komponensei:

- **Workspace controller**: Összehangolja a `workspace` egyedi erőforrást, létrehozza a `machine` (lentebb magyarázva) egyedi erőforrásokat a node automatikus biztosításának elindításához, és létrehozza az inferencia munkaterhelést (`deployment` vagy `statefulset`) a modell előre beállított konfigurációi alapján.
- **Node provisioner controller**: A kontroller neve *gpu-provisioner* a [gpu-provisioner helm chartban](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). A `machine` CRD-t használja, amely a [Karpenter](https://sigs.k8s.io/karpenter)-ből származik, hogy kommunikáljon a workspace controllerrel. Integrálódik az Azure Kubernetes Service (AKS) API-kkal, hogy új GPU node-okat adjon az AKS klaszterhez.
> Megjegyzés: A [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) egy nyílt forráskódú komponens. Más kontrollerek is használhatók helyette, ha támogatják a [Karpenter-core](https://sigs.k8s.io/karpenter) API-kat.

## Áttekintő videó  
[Nézd meg a Kaito demót](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)

## Telepítés

Kérjük, tekintsd meg a telepítési útmutatót [itt](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Gyors kezdés

A Kaito telepítése után az alábbi parancsokkal indítható el egy finomhangolási szolgáltatás.

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

A workspace állapotát az alábbi paranccsal lehet nyomon követni. Amikor a WORKSPACEREADY oszlop értéke `True` lesz, a modell sikeresen telepítve lett.

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

Ezután megkereshető az inferencia szolgáltatás klaszter IP címe, és egy ideiglenes `curl` pod segítségével tesztelhető a szolgáltatás végpontja a klaszteren belül.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.