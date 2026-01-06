<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aca91084bc440431571e00bf30d96ab8",
  "translation_date": "2026-01-05T09:35:32+00:00",
  "source_file": "md/01.Introduction/03/Kaito_Inference.md",
  "language_code": "cs"
}
-->
## Inference s Kaitem

[Kaito](https://github.com/Azure/kaito) je operator, který automatizuje nasazení modelů AI/ML pro inferenci v Kubernetes clusteru.

Kaito má následující klíčové odlišnosti oproti většině mainstream metodologií nasazení modelů postavených na infrastruktuře virtuálních strojů:

- Správa souborů modelu pomocí kontejnerových image. Poskytuje HTTP server pro provádění inferenčních volání pomocí modelové knihovny.
- Vyhýbá se ladění parametrů nasazení pro přizpůsobení GPU hardwaru díky přednastaveným konfiguracím.
- Automaticky zajišťuje GPU uzly na základě požadavků modelu.
- Hostuje velké modelové image v veřejném Microsoft Container Registry (MCR), pokud to licence umožňuje.

Pomocí Kaitoa je workflow zavedení velkých AI inferenčních modelů v Kubernetes výrazně zjednodušeno.

## Architektura

Kaito vychází z klasického designového vzoru Kubernetes Custom Resource Definition (CRD)/controller. Uživatel spravuje vlastní zdroj `workspace`, který popisuje požadavky na GPU a specifikaci inferencí. Kaito controllery automatizují nasazení rekoncilací `workspace` custom resource.

<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/website/static/img/ragarch.png" width=80% title="KAITO RAGEngine architecture" alt="KAITO RAGEngine architecture">
</div>

Výše uvedený obrázek představuje přehled architektury Kaitoa. Její hlavní komponenty jsou:

- **Workspace controller**: Spravuje vlastní zdroj `workspace`, vytváří vlastní zdroje `machine` (vysvětleno níže) pro spuštění automatického zajištění uzlů a vytváří inferenční zátěž (`deployment` nebo `statefulset`) na základě přednastavených konfigurací modelů.
- **Node provisioner controller**: Kontroler jménem *gpu-provisioner* z [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Používá `machine` CRD původně ze [Karpenter](https://sigs.k8s.io/karpenter) pro komunikaci s workspace controllerem. Integruje se s Azure Kubernetes Service (AKS) API pro přidávání nových GPU uzlů do AKS clusteru.
> Poznámka: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) je open source komponenta. Může být nahrazena jinými controllery, pokud podporují [Karpenter-core](https://sigs.k8s.io/karpenter) API.

## Instalace

Pokyny k instalaci naleznete [zde](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Rychlý start Inference Phi-3
[Ukázkový kód Inference Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Ladění výstupní cesty ACR
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3.yaml
```

Status workspace lze sledovat spuštěním následujícího příkazu. Když se sloupec WORKSPACEREADY změní na `True`, model byl úspěšně nasazen.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

Dále lze najít cluster IP inferenční služby a použít dočasný `curl` pod k otestování koncového bodu služby v clusteru.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Rychlý start Inference Phi-3 s adaptéry

Po instalaci Kaitoa lze vyzkoušet následující příkazy pro spuštění inferenční služby.

[Ukázkový kód Inference Phi-3 s adaptéry](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Ladění výstupní cesty ACR
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3_with_adapters.yaml
```

Status workspace lze sledovat spuštěním následujícího příkazu. Když se sloupec WORKSPACEREADY změní na `True`, model byl úspěšně nasazen.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

Dále lze najít cluster IP inferenční služby a použít dočasný `curl` pod k otestování koncového bodu služby v clusteru.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o vyloučení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoliv usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za závazný zdroj. Pro zásadní informace se doporučuje profesionální lidský překlad. Nejsme odpovědni za jakékoli nedorozumění nebo mylné výklady vyplývající z použití tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->