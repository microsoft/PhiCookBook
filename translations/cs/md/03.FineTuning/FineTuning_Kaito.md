## Doladění s Kaito

[Kaito](https://github.com/Azure/kaito) je operator, který automatizuje nasazení AI/ML inferenčních modelů v Kubernetes clusteru.

Kaito se od většiny běžných metod nasazení modelů postavených na infrastruktuře virtuálních strojů liší těmito klíčovými vlastnostmi:

- Správa modelových souborů pomocí kontejnerových image. K dispozici je HTTP server pro provádění inferenčních volání pomocí modelové knihovny.
- Nepotřebujete ladit parametry nasazení podle GPU hardwaru díky přednastaveným konfiguracím.
- Automatické zajištění GPU uzlů podle požadavků modelu.
- Hostování velkých modelových image v veřejném Microsoft Container Registry (MCR), pokud to licence umožňuje.

Díky Kaito je proces zavádění velkých AI inferenčních modelů v Kubernetes výrazně jednodušší.

## Architektura

Kaito vychází z klasického návrhového vzoru Kubernetes Custom Resource Definition (CRD)/controller. Uživatel spravuje vlastní zdroj `workspace`, který popisuje požadavky na GPU a specifikaci inferencí. Kaito controllery automatizují nasazení tím, že synchronizují stav `workspace` custom resource.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

Výše uvedený obrázek ukazuje přehled architektury Kaito. Její hlavní komponenty jsou:

- **Workspace controller**: Synchronizuje `workspace` custom resource, vytváří `machine` (viz níže) custom resources pro spuštění automatického zajištění uzlů a vytváří inferenční workload (`deployment` nebo `statefulset`) na základě přednastavených konfigurací modelu.
- **Node provisioner controller**: Tento controller se jmenuje *gpu-provisioner* v [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Používá `machine` CRD pocházející z [Karpenter](https://sigs.k8s.io/karpenter) pro komunikaci s workspace controllerem. Integruje se s Azure Kubernetes Service (AKS) API pro přidání nových GPU uzlů do AKS clusteru.
> Poznámka: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) je open source komponenta. Může být nahrazena jinými controllery, pokud podporují [Karpenter-core](https://sigs.k8s.io/karpenter) API.

## Přehledové video  
[Sledujte Kaito Demo](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)

## Instalace

Pokyny k instalaci najdete [zde](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Rychlý start

Po instalaci Kaito můžete vyzkoušet následující příkazy pro spuštění služby doladění.

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

Stav workspace lze sledovat pomocí následujícího příkazu. Jakmile se ve sloupci WORKSPACEREADY objeví hodnota `True`, model byl úspěšně nasazen.

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

Dále můžete zjistit cluster IP inferenční služby a použít dočasný `curl` pod pro otestování koncového bodu služby v clusteru.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.