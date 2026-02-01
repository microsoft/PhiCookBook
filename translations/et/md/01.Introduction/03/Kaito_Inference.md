## Järeldus Kaito abil

[Kaito](https://github.com/Azure/kaito) on operaator, mis automatiseerib AI/ML järeldusmudelite juurutamist Kubernetes klastris.

Kaitol on järgmised peamised eristavad omadused võrreldes enamiku virtuaalmasina infrastruktuuride põhiste tavaliste mudelijuurutuse meetoditega:

- Halda mudelifaile konteineripiltide abil. Mudeli teegi kasutamiseks päringute tegemiseks on pakutud http-server.
- Vältida juurutusparameetrite häälestamist GPU riistvarale sobitamiseks, pakkudes eelmääratud konfiguratsioone.
- Sätestada GPU sõlmed automaatselt vastavalt mudeli nõudmistele.
- Majutada suuri mudelipilte avalikus Microsoft Container Registrys (MCR), kui litsents seda lubab.

Kaitot kasutades on suurte AI järeldusmudelite sisseseadmine Kubernetes keskkonnas märkimisväärselt lihtsustatud.

## Arhitektuur

Kaito järgib klassikalist Kubernetes Custom Resource Definition (CRD)/kontrolleri disainimustrit. Kasutaja haldab `workspace` kohandatud ressurssi, mis kirjeldab GPU nõudeid ja järelduse spetsifikatsiooni. Kaito kontrollerid automatiseerivad juurutuse, kooskõlastades `workspace` kohandatud ressurssi.

<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/website/static/img/ragarch.png" width=80% title="KAITO RAGEngine arhitektuur" alt="KAITO RAGEngine arhitektuur">
</div>

Ülaltoodud joonis esitab Kaito arhitektuuri ülevaate. Selle peamised komponendid koosnevad:

- **Workspace kontroller**: Kooskõlastab `workspace` kohandatud ressurssi, loob `machine` (allpool kirjeldatud) kohandatud ressursid sõlmede automaatseks provisioninguks ning loob järeldustöökoormuse (`deployment` või `statefulset`) mudeli eelmääratud konfiguratsioonide alusel.
- **Sõlme provisioning kontroller**: Kontrolleri nimi on *gpu-provisioner* [gpu-provisioner helm chartis](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). See kasutab `machine` CRD-d, mis pärineb [Karpenterilt](https://sigs.k8s.io/karpenter), et suhelda workspace kontrolleriga. See integreerub Azure Kubernetes Service(AKS) API-dega, et lisada uusi GPU sõlmi AKS klastrisse.
> Märkus: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) on avatud lähtekoodiga komponent. Selle võib asendada mõne teise kontrolleriga juhul, kui need toetavad [Karpenter-core](https://sigs.k8s.io/karpenter) API-sid.

## Paigaldamine

Palun vaadake paigaldusjuhendit [siit](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Kiirkäivitus Inference Phi-3
[Näidiskood Inference Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Väljundi ACR tee häälestamine
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3.yaml
```

Workspace olekut saab jälgida järgmise käsu abil. Kui WORKSPACEREADY veerg näitab `True`, on mudel edukalt juurutatud.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

Edasi saab leida järeldusteenuse klastrisisese IP ning kasutada ajutist `curl` podi teenuse lõpp-punkti testimiseks klastris.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Kiirkäivitus Inference Phi-3 koos adapteritega

Pärast Kaito paigaldamist saab proovida järgmisi käske, et käivitada järeldusteenus.

[Näidiskood Inference Phi-3 koos adapteritega](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Väljundi ACR tee häälestamine
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3_with_adapters.yaml
```

Workspace olekut saab jälgida järgmise käsu abil. Kui WORKSPACEREADY veerg näitab `True`, on mudel edukalt juurutatud.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

Edasi saab leida järeldusteenuse klastrisisese IP ning kasutada ajutist `curl` podi teenuse lõpp-punkti testimiseks klastris.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastutusest loobumine**:  
See dokument on tõlgitud kasutades tehisintellekti tõlke teenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi püüame tagada täpsust, palun arvestage, et automatiseeritud tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste ega valesti tõlgenduste eest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->