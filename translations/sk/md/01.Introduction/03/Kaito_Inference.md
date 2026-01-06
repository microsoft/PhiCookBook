<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aca91084bc440431571e00bf30d96ab8",
  "translation_date": "2026-01-05T09:48:00+00:00",
  "source_file": "md/01.Introduction/03/Kaito_Inference.md",
  "language_code": "sk"
}
-->
## Inference s Kaito

[Kaito](https://github.com/Azure/kaito) je operátor, ktorý automatizuje nasadenie AI/ML inference modelov v Kubernetes klastri.

Kaito má nasledujúce kľúčové odlišnosti v porovnaní s väčšinou bežných metód nasadenia modelov postavených na infraštruktúrach virtuálnych strojov:

- Správa modelových súborov pomocou kontajnerových obrazov. Poskytuje HTTP server na vykonávanie inference volaní s využitím knižnice modelu.
- Vyhýbanie sa ladeniu parametrov nasadenia podľa GPU hardvéru prostredníctvom prednastavených konfigurácií.
- Automatické zabezpečenie GPU uzlov na základe požiadaviek modelu.
- Hostovanie veľkých modelových obrazov v verejnom Microsoft Container Registry (MCR), ak to licencia povoľuje.

Použitím Kaito je pracovný postup nahrávania veľkých AI inference modelov v Kubernetes výrazne zjednodušený.

## Architektúra

Kaito nasleduje klasický Kubernetes vzor návrhu Custom Resource Definition(CRD)/controller. Používateľ spravuje vlastný zdroj `workspace`, ktorý popisuje požiadavky na GPU a špecifikáciu inference. Kaito kontroléry automatizujú nasadenie zosúladzovaním vlastného zdroja `workspace`.

<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/website/static/img/ragarch.png" width=80% title="KAITO RAGEngine architecture" alt="KAITO RAGEngine architecture">
</div>

Vyššie uvedený obrázok prezentuje prehľad architektúry Kaito. Jej hlavné komponenty tvoria:

- **Workspace kontrolér**: zosúlaďuje vlastný zdroj `workspace`, vytvára vlastné zdroje `machine` (popísané nižšie) na vyvolanie automatického zabezpečenia uzlov a vytvára inference záťaž (`deployment` alebo `statefulset`) na základe predvolených konfigurácií modelu.
- **Node provisioner kontrolér**: Kontrolér sa nazýva *gpu-provisioner* v [gpu-provisioner helm charte](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Používa CRD `machine` pochádzajúci z [Karpenter](https://sigs.k8s.io/karpenter), aby komunikoval s workspace kontrolérom. Integruje sa s Azure Kubernetes Service (AKS) API na pridávanie nových GPU uzlov do AKS klastra.
> Poznámka: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) je open-source komponent. Môže byť nahradený inými kontrolérmi, ak podporujú [Karpenter-core](https://sigs.k8s.io/karpenter) API.

## Inštalácia

Prosím, skontrolujte návod na inštaláciu [tu](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Rýchly štart Inference Phi-3
[Vzorový kód Inference Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Ladenie výstupnej cesty ACR
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3.yaml
```

Stav workspace je možné sledovať spustením nasledujúceho príkazu. Keď stĺpec WORKSPACEREADY nadobudne hodnotu `True`, model bol úspešne nasadený.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

Ďalej je možné nájsť cluster IP inference služby a použiť dočasný `curl` pod na otestovanie koncového bodu služby v klastri.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Rýchly štart Inference Phi-3 s adaptérmi

Po inštalácii Kaito je možné skúsiť nasledujúce príkazy na spustenie inference služby.

[Vzorový kód Inference Phi-3 s adaptérmi](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Ladenie výstupnej cesty ACR
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3_with_adapters.yaml
```

Stav workspace je možné sledovať spustením nasledujúceho príkazu. Keď stĺpec WORKSPACEREADY nadobudne hodnotu `True`, model bol úspešne nasadený.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

Ďalej je možné nájsť cluster IP inference služby a použiť dočasný `curl` pod na otestovanie koncového bodu služby v klastri.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zrieknutie sa zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, majte prosím na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Za akékoľvek nedorozumenia alebo nesprávne výklady vyplývajúce z použitia tohto prekladu nenesieme zodpovednosť.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->