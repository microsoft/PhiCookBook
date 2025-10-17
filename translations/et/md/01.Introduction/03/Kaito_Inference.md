<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e46691923dca7cb2f11d32b1d9d558e0",
  "translation_date": "2025-10-11T12:21:23+00:00",
  "source_file": "md/01.Introduction/03/Kaito_Inference.md",
  "language_code": "et"
}
-->
## Järeldused Kaito abil

[Kaito](https://github.com/Azure/kaito) on operaator, mis automatiseerib AI/ML järeldusmudelite juurutamise Kubernetes'i klastris.

Kaitol on järgmised peamised erinevused võrreldes enamiku peavoolu mudelite juurutamise meetoditega, mis põhinevad virtuaalmasinate infrastruktuuridel:

- Halda mudelifailid konteinerpiltide abil. HTTP-server on saadaval, et teha järelduskõnesid mudelibraariaga.
- Väldi juurutusparameetrite häälestamist GPU riistvara jaoks, pakkudes eelseadistatud konfiguratsioone.
- GPU sõlmede automaatne ettevalmistamine mudeli nõuete alusel.
- Suurte mudelipiltide majutamine avalikus Microsoft Container Registry (MCR), kui litsents seda lubab.

Kaito abil on suurte AI järeldusmudelite Kubernetes'i klastrisse integreerimise töövoog oluliselt lihtsustatud.

## Arhitektuur

Kaito järgib klassikalist Kubernetes Custom Resource Definition (CRD)/kontrolleri disainimustrit. Kasutaja haldab `workspace` kohandatud ressurssi, mis kirjeldab GPU nõudeid ja järelduse spetsifikatsiooni. Kaito kontrollerid automatiseerivad juurutamise, viies kokku `workspace` kohandatud ressursi.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Kaito arhitektuur" alt="Kaito arhitektuur">
</div>

Ülaltoodud joonis esitab Kaito arhitektuuri ülevaate. Selle peamised komponendid koosnevad järgmistest:

- **Workspace kontroller**: See viib kokku `workspace` kohandatud ressursi, loob `machine` (selgitatud allpool) kohandatud ressursid, et käivitada sõlmede automaatne ettevalmistamine, ja loob järelduskoormuse (`deployment` või `statefulset`) mudeli eelseadistatud konfiguratsioonide alusel.
- **Sõlmede ettevalmistaja kontroller**: Kontrolleri nimi on *gpu-provisioner* [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) raames. See kasutab `machine` CRD-d, mis pärineb [Karpenter](https://sigs.k8s.io/karpenter)-ist, et suhelda workspace kontrolleriga. See integreerub Azure Kubernetes Service (AKS) API-dega, et lisada uusi GPU sõlmi AKS klastrisse. 
> Märkus: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) on avatud lähtekoodiga komponent. Seda saab asendada teiste kontrolleritega, kui need toetavad [Karpenter-core](https://sigs.k8s.io/karpenter) API-sid.

## Paigaldamine

Paigaldusjuhiseid leiate [siit](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Kiire algus: Järeldus Phi-3
[Phi-3 järelduse näidiskood](https://github.com/Azure/kaito/tree/main/examples/inference)

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

Workspace'i olekut saab jälgida, käivitades järgmise käsu. Kui veerg WORKSPACEREADY muutub väärtuseks `True`, on mudel edukalt juurutatud.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

Seejärel saab leida järeldusteenuse klastri IP ja kasutada ajutist `curl` pod-i teenuse lõpp-punkti testimiseks klastris.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Kiire algus: Järeldus Phi-3 adapteritega

Pärast Kaito paigaldamist saab proovida järgmisi käske, et käivitada järeldusteenus.

[Phi-3 järelduse näidiskood adapteritega](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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

Workspace'i olekut saab jälgida, käivitades järgmise käsu. Kui veerg WORKSPACEREADY muutub väärtuseks `True`, on mudel edukalt juurutatud.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

Seejärel saab leida järeldusteenuse klastri IP ja kasutada ajutist `curl` pod-i teenuse lõpp-punkti testimiseks klastris.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.