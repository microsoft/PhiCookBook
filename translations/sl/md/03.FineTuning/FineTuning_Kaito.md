<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a1c62bf7d86d6186bf8d3917196a92a0",
  "translation_date": "2025-07-17T06:26:03+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Kaito.md",
  "language_code": "sl"
}
-->
## Fine-tuning s Kaito

[Kaito](https://github.com/Azure/kaito) je operator, ki avtomatizira uvajanje AI/ML modelov za inferenco v Kubernetes gruči.

Kaito se v primerjavi z večino običajnih metod uvajanja modelov, ki temeljijo na infrastrukturi virtualnih strojev, razlikuje po naslednjih ključnih značilnostih:

- Upravljanje datotek modelov z uporabo slik kontejnerjev. Na voljo je http strežnik za izvajanje inferenčnih klicev z uporabo knjižnice modelov.
- Izogibanje nastavljanju parametrov uvajanja za prilagoditev GPU strojni opremi z zagotavljanjem vnaprej nastavljenih konfiguracij.
- Samodejno zagotavljanje GPU vozlišč glede na zahteve modela.
- Gostovanje velikih slik modelov v javnem Microsoft Container Registry (MCR), če to dovoljuje licenca.

Z uporabo Kaitoa je postopek uvajanja velikih AI inferenčnih modelov v Kubernetesu precej poenostavljen.

## Arhitektura

Kaito sledi klasičnemu vzorcu zasnove Kubernetes Custom Resource Definition (CRD)/controller. Uporabnik upravlja s `workspace` custom resource, ki opisuje zahteve po GPU in specifikacijo inferenčnega modela. Kaito kontrolerji avtomatizirajo uvajanje z usklajevanjem `workspace` custom resource.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

Zgornja slika prikazuje pregled arhitekture Kaitoa. Njegove glavne komponente so:

- **Workspace controller**: Usklajuje `workspace` custom resource, ustvarja `machine` (pojasnjeno spodaj) custom resource za sprožitev samodejnega zagotavljanja vozlišč in ustvarja inferenčno delovno obremenitev (`deployment` ali `statefulset`) na podlagi vnaprej nastavljenih konfiguracij modela.
- **Node provisioner controller**: Ime kontrolerja je *gpu-provisioner* v [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Uporablja `machine` CRD, ki izvira iz [Karpenter](https://sigs.k8s.io/karpenter), za interakcijo z workspace controllerjem. Integrira se z Azure Kubernetes Service (AKS) API-ji za dodajanje novih GPU vozlišč v AKS gruči.
> Opomba: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) je odprtokomponenta. Lahko ga nadomestijo drugi kontrolerji, če podpirajo [Karpenter-core](https://sigs.k8s.io/karpenter) API-je.

## Pregledni video  
[Oglejte si Kaito demo](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)

## Namestitev

Prosimo, preverite navodila za namestitev [tukaj](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Hitri začetek

Po namestitvi Kaitoa lahko poskusite naslednje ukaze za zagon fine-tuning storitve.

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

Status workspace lahko spremljate z izvajanjem naslednjega ukaza. Ko stolpec WORKSPACEREADY postane `True`, je model uspešno nameščen.

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

Nato lahko poiščete IP naslov inferenčne storitve v gruči in uporabite začasni `curl` pod za testiranje končne točke storitve v gruči.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za avtomatski prevod AI [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za pomembne informacije priporočamo strokovni človeški prevod. Za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.