## Kaito peenhäälestamine

[Kaito](https://github.com/Azure/kaito) on operaator, mis automatiseerib AI/ML mudelite inferentsi juurutamise Kubernetes'i klastris.

Kaito eristub peamistest virtuaalmasinate infrastruktuuril põhinevatest mudelite juurutamise meetoditest järgmiselt:

- Mudelifailide haldamine konteinerpiltide abil. Mudeliraamatukogu kasutamiseks on saadaval HTTP-server inferentsikõnede tegemiseks.
- Vältida juurutusparameetrite häälestamist GPU riistvara jaoks, pakkudes eelkonfigureeritud seadistusi.
- GPU sõlmede automaatne lisamine vastavalt mudeli nõuetele.
- Suurte mudelipiltide majutamine avalikus Microsoft Container Registry (MCR) registris, kui litsents seda lubab.

Kaito abil on suurte AI inferentsimudelite Kubernetes'i klastrisse integreerimise töövoog oluliselt lihtsustatud.

## Arhitektuur

Kaito järgib klassikalist Kubernetes'i kohandatud ressursi määratluse (CRD)/kontrolleri disainimustrit. Kasutaja haldab `workspace` kohandatud ressurssi, mis kirjeldab GPU nõudeid ja inferentsi spetsifikatsiooni. Kaito kontrollerid automatiseerivad juurutamise, viies `workspace` kohandatud ressursi vastavusse.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito arhitektuur" alt="Kaito arhitektuur">
</div>

Ülaltoodud joonis esitab Kaito arhitektuuri ülevaate. Selle peamised komponendid on:

- **Workspace kontroller**: See viib `workspace` kohandatud ressursi vastavusse, loob `machine` (selgitatud allpool) kohandatud ressursid sõlmede automaatseks lisamiseks ja loob inferentsi töökoormuse (`deployment` või `statefulset`) mudeli eelkonfiguratsioonide põhjal.
- **Sõlmede lisamise kontroller**: Selle kontrolleri nimi on *gpu-provisioner* [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) raames. See kasutab `machine` CRD-d, mis pärineb [Karpenter](https://sigs.k8s.io/karpenter) projektist, et suhelda workspace kontrolleriga. See integreerub Azure Kubernetes Service (AKS) API-dega, et lisada uusi GPU sõlmi AKS klastrisse.  
> Märkus: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) on avatud lähtekoodiga komponent. Seda saab asendada teiste kontrolleritega, kui need toetavad [Karpenter-core](https://sigs.k8s.io/karpenter) API-sid.

## Ülevaatevideo 
[Vaata Kaito demo](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)

## Paigaldamine

Paigaldusjuhiseid leiate [siit](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Kiire alustamine

Pärast Kaito paigaldamist saab proovida järgmisi käske, et käivitada peenhäälestamise teenus.

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

Workspace'i olekut saab jälgida, käivitades järgmise käsu. Kui WORKSPACEREADY veerg muutub väärtuseks `True`, on mudel edukalt juurutatud.

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

Seejärel saab leida inferentsiteenuse klastri IP-aadressi ja kasutada ajutist `curl` pod-i teenuse lõpp-punkti testimiseks klastris.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.