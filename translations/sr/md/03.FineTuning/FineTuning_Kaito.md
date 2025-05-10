<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a1c62bf7d86d6186bf8d3917196a92a0",
  "translation_date": "2025-05-09T20:43:25+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Kaito.md",
  "language_code": "sr"
}
-->
## Fino podešavanje sa Kaitom

[Kaito](https://github.com/Azure/kaito) je operator koji automatizuje implementaciju AI/ML modela za inferencu u Kubernetes klasteru.

Kaito ima sledeće ključne razlike u odnosu na većinu glavnih metoda za implementaciju modela zasnovanih na virtuelnim mašinama:

- Upravljanje fajlovima modela korišćenjem kontejnerskih slika. HTTP server je dostupan za izvođenje inferencijskih poziva koristeći biblioteku modela.
- Izbegavanje podešavanja parametara implementacije za prilagođavanje GPU hardveru kroz unapred definisane konfiguracije.
- Automatsko obezbeđivanje GPU čvorova u zavisnosti od zahteva modela.
- Hostovanje velikih model slika u javnom Microsoft Container Registry (MCR) ukoliko licenca dozvoljava.

Korišćenjem Kaitoa, proces uključivanja velikih AI modela za inferencu u Kubernetes znatno je pojednostavljen.

## Arhitektura

Kaito prati klasični Kubernetes dizajn obrazac Custom Resource Definition (CRD)/kontroler. Korisnik upravlja `workspace` prilagođenim resursom koji opisuje zahteve za GPU i specifikaciju inferencije. Kaito kontroleri automatizuju implementaciju usklađivanjem `workspace` prilagođenog resursa.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

Gornja slika prikazuje pregled arhitekture Kaitoa. Njeni glavni delovi su:

- **Workspace controller**: Usklađuje `workspace` prilagođeni resurs, kreira `machine` (objašnjeno dole) prilagođene resurse za pokretanje automatskog obezbeđivanja čvorova i kreira inferencijski workload (`deployment` ili `statefulset`) na osnovu unapred definisanih konfiguracija modela.
- **Node provisioner controller**: Kontroler se zove *gpu-provisioner* u [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Koristi `machine` CRD koji potiče od [Karpenter](https://sigs.k8s.io/karpenter) da bi komunicirao sa workspace kontrolerom. Integrisan je sa Azure Kubernetes Service (AKS) API-jima za dodavanje novih GPU čvorova u AKS klaster.
> Napomena: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) je open source komponenta. Može biti zamenjen drugim kontrolerima ukoliko podržavaju [Karpenter-core](https://sigs.k8s.io/karpenter) API-je.

## Pregled video zapisa  
[Pogledajte Kaito demo](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)

## Instalacija

Molimo proverite uputstvo za instalaciju [ovde](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Brzi početak

Nakon instalacije Kaitoa, možete probati sledeće komande za pokretanje servisa za fino podešavanje.

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

Status workspace-a može se pratiti pokretanjem sledeće komande. Kada kolona WORKSPACEREADY postane `True`, model je uspešno implementiran.

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

Zatim, možete pronaći cluster IP inferencijskog servisa i koristiti privremeni `curl` pod za testiranje krajnje tačke servisa unutar klastera.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korišćenjem AI servisa za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo tačnosti, imajte na umu da automatski prevodi mogu sadržati greške ili netačnosti. Originalni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prevod. Nismo odgovorni za bilo kakve nesporazume ili pogrešna tumačenja nastala korišćenjem ovog prevoda.