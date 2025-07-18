<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e46691923dca7cb2f11d32b1d9d558e0",
  "translation_date": "2025-07-16T20:53:54+00:00",
  "source_file": "md/01.Introduction/03/Kaito_Inference.md",
  "language_code": "hr"
}
-->
## Inference s Kaitom

[Kaito](https://github.com/Azure/kaito) je operator koji automatizira implementaciju AI/ML inference modela u Kubernetes klasteru.

Kaito se razlikuje od većine uobičajenih metoda implementacije modela temeljenih na virtualnim strojevima po sljedećem:

- Upravljanje datotekama modela putem kontejnerskih slika. HTTP server je dostupan za izvođenje inference poziva koristeći biblioteku modela.
- Izbjegavanje podešavanja parametara implementacije za prilagodbu GPU hardveru kroz unaprijed postavljene konfiguracije.
- Automatsko osiguravanje GPU čvorova prema zahtjevima modela.
- Hostanje velikih model slika u javnom Microsoft Container Registryju (MCR) ako licenca to dopušta.

Korištenjem Kaitoa, proces uvođenja velikih AI inference modela u Kubernetes znatno je pojednostavljen.

## Arhitektura

Kaito slijedi klasični Kubernetes Custom Resource Definition (CRD)/controller dizajn obrazac. Korisnik upravlja `workspace` prilagođenim resursom koji opisuje GPU zahtjeve i specifikaciju inference. Kaito kontroleri automatiziraju implementaciju usklađivanjem `workspace` prilagođenog resursa.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

Gornja slika prikazuje pregled Kaito arhitekture. Njeni glavni dijelovi su:

- **Workspace controller**: Usklađuje `workspace` prilagođeni resurs, kreira `machine` (objašnjeno dolje) prilagođene resurse za pokretanje automatskog osiguravanja čvorova i kreira inference workload (`deployment` ili `statefulset`) na temelju unaprijed postavljenih konfiguracija modela.
- **Node provisioner controller**: Kontroler se zove *gpu-provisioner* u [gpu-provisioner helm chartu](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Koristi `machine` CRD koji potječe iz [Karpentera](https://sigs.k8s.io/karpenter) za interakciju s workspace kontrolerom. Integrira se s Azure Kubernetes Service (AKS) API-jima za dodavanje novih GPU čvorova u AKS klaster.
> Napomena: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) je open source komponenta. Može se zamijeniti drugim kontrolerima ako podržavaju [Karpenter-core](https://sigs.k8s.io/karpenter) API-je.

## Instalacija

Molimo provjerite upute za instalaciju [ovdje](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Brzi početak Inference Phi-3
[Primjer koda Inference Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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

Status workspacea može se pratiti pokretanjem sljedeće naredbe. Kada stupac WORKSPACEREADY postane `True`, model je uspješno implementiran.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

Zatim se može pronaći cluster IP inference servisa i koristiti privremeni `curl` pod za testiranje endpointa servisa unutar klastera.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Brzi početak Inference Phi-3 s adapterima

Nakon instalacije Kaitoa, moguće je isprobati sljedeće naredbe za pokretanje inference servisa.

[Primjer koda Inference Phi-3 s adapterima](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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

Status workspacea može se pratiti pokretanjem sljedeće naredbe. Kada stupac WORKSPACEREADY postane `True`, model je uspješno implementiran.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

Zatim se može pronaći cluster IP inference servisa i koristiti privremeni `curl` pod za testiranje endpointa servisa unutar klastera.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati službenim i autoritativnim izvorom. Za važne informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazuma ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.