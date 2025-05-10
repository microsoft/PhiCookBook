<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e46691923dca7cb2f11d32b1d9d558e0",
  "translation_date": "2025-05-09T12:00:31+00:00",
  "source_file": "md/01.Introduction/03/Kaito_Inference.md",
  "language_code": "sr"
}
-->
## Inference sa Kaito

[Kaito](https://github.com/Azure/kaito) je operator koji automatizuje postavljanje AI/ML inference modela u Kubernetes klasteru.

Kaito se razlikuje od većine uobičajenih metoda za postavljanje modela koje se baziraju na virtuelnim mašinama na sledeće načine:

- Upravljanje fajlovima modela putem container imidža. HTTP server je obezbeđen za izvođenje inference poziva koristeći model biblioteku.
- Izbegavanje podešavanja parametara postavljanja u skladu sa GPU hardverom kroz unapred definisane konfiguracije.
- Automatsko obezbeđivanje GPU nodova prema zahtevima modela.
- Hostovanje velikih model imidža u javnom Microsoft Container Registry (MCR), ukoliko licenca to dozvoljava.

Korišćenjem Kaito-a, proces integracije velikih AI inference modela u Kubernetes je znatno pojednostavljen.


## Arhitektura

Kaito prati klasični Kubernetes Custom Resource Definition (CRD)/kontrolerski dizajn. Korisnik upravlja `workspace` custom resursom koji opisuje GPU zahteve i specifikaciju inference-a. Kaito kontroleri automatizuju postavljanje usklađivanjem sa `workspace` custom resursom.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

Gornja slika prikazuje pregled arhitekture Kaito-a. Njeni glavni delovi su:

- **Workspace controller**: Usklađuje `workspace` custom resurs, kreira `machine` (objašnjeno dole) custom resurse za pokretanje automatskog obezbeđivanja nodova, i kreira inference workload (`deployment` ili `statefulset`) bazirano na unapred definisanim konfiguracijama modela.
- **Node provisioner controller**: Kontroler se zove *gpu-provisioner* u [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Koristi `machine` CRD koji potiče iz [Karpenter](https://sigs.k8s.io/karpenter) da komunicira sa workspace kontrolerom. Integrisan je sa Azure Kubernetes Service (AKS) API-jima za dodavanje novih GPU nodova u AKS klaster. 
> Napomena: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) je open source komponenta. Može biti zamenjen drugim kontrolerima ako podržavaju [Karpenter-core](https://sigs.k8s.io/karpenter) API-je.

## Instalacija

Molimo pogledajte uputstvo za instalaciju [ovde](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Brzi početak Inference Phi-3
[Primer koda Inference Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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

Status workspace-a može se pratiti pokretanjem sledeće komande. Kada kolona WORKSPACEREADY postane `True`, model je uspešno postavljen.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

Zatim, može se pronaći cluster ip inference servisa i koristiti privremeni `curl` pod za testiranje servisa unutar klastera.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Brzi početak Inference Phi-3 sa adapterima

Nakon instalacije Kaito-a, može se probati sledeće komande za pokretanje inference servisa.

[Primer koda Inference Phi-3 sa adapterima](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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

Status workspace-a može se pratiti pokretanjem sledeće komande. Kada kolona WORKSPACEREADY postane `True`, model je uspešno postavljen.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

Zatim, može se pronaći cluster ip inference servisa i koristiti privremeni `curl` pod za testiranje servisa unutar klastera.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI преводилачке услуге [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да превод буде тачан, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која могу настати коришћењем овог превода.