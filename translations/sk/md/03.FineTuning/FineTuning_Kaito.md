<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a1c62bf7d86d6186bf8d3917196a92a0",
  "translation_date": "2025-05-09T20:42:57+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Kaito.md",
  "language_code": "sk"
}
-->
## Doladenie pomocou Kaito

[Kaito](https://github.com/Azure/kaito) je operátor, ktorý automatizuje nasadenie AI/ML inference modelov v Kubernetes klastri.

Kaito má oproti väčšine bežných metód nasadzovania modelov postavených na infraštruktúre virtuálnych strojov tieto kľúčové odlišnosti:

- Spravuje modelové súbory pomocou kontajnerových obrazov. HTTP server je poskytovaný na vykonávanie inference volaní pomocou modelovej knižnice.
- Vyhýba sa ladenie parametrov nasadenia na mieru GPU hardvéru vďaka prednastaveným konfiguráciám.
- Automaticky zabezpečuje GPU uzly podľa požiadaviek modelu.
- Umožňuje hosťovanie veľkých modelových obrazov v verejnom Microsoft Container Registry (MCR), ak to licencia povoľuje.

Použitím Kaito je pracovný postup nasadzovania veľkých AI inference modelov v Kubernetes výrazne zjednodušený.

## Architektúra

Kaito nasleduje klasický návrhový vzor Kubernetes Custom Resource Definition (CRD)/controller. Používateľ spravuje `workspace` custom resource, ktorý popisuje požiadavky na GPU a špecifikáciu inferencie. Kaito controllery automatizujú nasadenie tým, že zosúladia stav `workspace` custom resource.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

Vyššie uvedený obrázok predstavuje prehľad architektúry Kaito. Jej hlavné komponenty zahŕňajú:

- **Workspace controller**: Zosúlaďuje `workspace` custom resource, vytvára `machine` (popísané nižšie) custom resources na spustenie automatického zabezpečenia uzlov a vytvára inference workload (`deployment` alebo `statefulset`) na základe prednastavení modelu.
- **Node provisioner controller**: Controller sa volá *gpu-provisioner* v [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Používa `machine` CRD pochádzajúci z [Karpenter](https://sigs.k8s.io/karpenter) na komunikáciu s workspace controllerom. Integruje sa s Azure Kubernetes Service (AKS) API na pridávanie nových GPU uzlov do AKS klastra.
> Poznámka: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) je open source komponent. Môže byť nahradený inými controllermi, ak podporujú [Karpenter-core](https://sigs.k8s.io/karpenter) API.

## Prehľadové video  
[Pozrite si Kaito Demo](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)

## Inštalácia

Prosím, skontrolujte inštalačný návod [tu](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Rýchly štart

Po inštalácii Kaito môžete vyskúšať nasledujúce príkazy na spustenie služby doladenia.

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

Stav workspace je možné sledovať spustením nasledujúceho príkazu. Keď sa v stĺpci WORKSPACEREADY zobrazí `True`, model bol úspešne nasadený.

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

Následne môžete zistiť cluster IP inferenčnej služby a použiť dočasný `curl` pod na otestovanie endpointu služby v klastri.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Zrieknutie sa zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne výklady vyplývajúce z použitia tohto prekladu.