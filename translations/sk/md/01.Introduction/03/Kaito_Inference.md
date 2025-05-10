<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e46691923dca7cb2f11d32b1d9d558e0",
  "translation_date": "2025-05-09T11:59:06+00:00",
  "source_file": "md/01.Introduction/03/Kaito_Inference.md",
  "language_code": "sk"
}
-->
## Inference s Kaitom

[Kaito](https://github.com/Azure/kaito) je operator, ktorý automatizuje nasadenie AI/ML inference modelov v Kubernetes klastri.

Kaito má oproti väčšine bežných metód nasadenia modelov postavených na infraštruktúre virtuálnych strojov tieto hlavné odlišnosti:

- Správa modelových súborov pomocou kontajnerových obrazov. Poskytuje HTTP server na vykonávanie inference volaní pomocou knižnice modelov.
- Vyhýba sa ladení parametrov nasadenia pre GPU hardvér vďaka prednastaveným konfiguráciám.
- Automaticky zabezpečuje GPU uzly podľa požiadaviek modelu.
- Hostuje veľké modelové obrazy v verejnom Microsoft Container Registry (MCR), ak to licencia umožňuje.

Použitím Kaitoa je pracovný postup pridávania veľkých AI inference modelov v Kubernetes výrazne zjednodušený.

## Architektúra

Kaito nasleduje klasický Kubernetes Custom Resource Definition (CRD)/controller dizajnový vzor. Používateľ spravuje vlastný zdroj `workspace`, ktorý popisuje požiadavky na GPU a špecifikáciu inferencie. Kaito controllery automatizujú nasadenie tým, že zosúladia vlastný zdroj `workspace`.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

Na obrázku vyššie je prehľad architektúry Kaitoa. Jeho hlavné komponenty zahŕňajú:

- **Workspace controller**: Zosúlaďuje vlastný zdroj `workspace`, vytvára vlastné zdroje `machine` (vysvetlené nižšie) na spustenie automatického zabezpečenia uzlov a vytvára inference workload (`deployment` alebo `statefulset`) na základe prednastavených konfigurácií modelu.
- **Node provisioner controller**: Controller sa volá *gpu-provisioner* v [gpu-provisioner helm charte](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Používa `machine` CRD pochádzajúci z [Karpenter](https://sigs.k8s.io/karpenter) na komunikáciu s workspace controllerom. Integruje sa s Azure Kubernetes Service (AKS) API na pridávanie nových GPU uzlov do AKS klastra.
> Note: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) je open source komponent. Môže byť nahradený inými controllermi, ak podporujú [Karpenter-core](https://sigs.k8s.io/karpenter) API.

## Inštalácia

Inštalačný návod nájdete [tu](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Rýchly štart Inference Phi-3
[Ukážkový kód Inference Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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

Stav workspace je možné sledovať spustením nasledujúceho príkazu. Keď sa v stĺpci WORKSPACEREADY zobrazí `True`, model bol úspešne nasadený.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

Ďalej je možné nájsť cluster IP inference služby a použiť dočasný `curl` pod na otestovanie endpointu služby v klastri.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Rýchly štart Inference Phi-3 s adaptérmi

Po inštalácii Kaitoa môžete vyskúšať nasledujúce príkazy na spustenie inference služby.

[Ukážkový kód Inference Phi-3 s adaptérmi](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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

Stav workspace je možné sledovať spustením nasledujúceho príkazu. Keď sa v stĺpci WORKSPACEREADY zobrazí `True`, model bol úspešne nasadený.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

Ďalej je možné nájsť cluster IP inference služby a použiť dočasný `curl` pod na otestovanie endpointu služby v klastri.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, majte na pamäti, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre dôležité informácie sa odporúča profesionálny ľudský preklad. Nezodpovedáme za žiadne nedorozumenia alebo nesprávne výklady vyplývajúce z použitia tohto prekladu.