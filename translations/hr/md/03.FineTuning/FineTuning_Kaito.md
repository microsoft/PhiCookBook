<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a1c62bf7d86d6186bf8d3917196a92a0",
  "translation_date": "2025-05-09T20:43:33+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Kaito.md",
  "language_code": "hr"
}
-->
## Fine-Tuning s Kaitom

[Kaito](https://github.com/Azure/kaito) je operator koji automatizira implementaciju AI/ML modela za inferenciju u Kubernetes klasteru.

Kaito se razlikuje od većine glavnih metodologija za implementaciju modela baziranih na virtualnim mašinama po sljedećem:

- Upravljanje datotekama modela pomoću kontejnerskih slika. HTTP server je dostupan za izvođenje inferencijskih poziva koristeći biblioteku modela.
- Izbjegavanje podešavanja parametara implementacije za prilagodbu GPU hardveru pružanjem unaprijed definiranih konfiguracija.
- Automatsko osiguravanje GPU čvorova na temelju zahtjeva modela.
- Hostanje velikih slika modela u javnom Microsoft Container Registry (MCR) ako licenca to dopušta.

Korištenjem Kaitoa, proces uvođenja velikih AI modela za inferenciju u Kubernetes znatno je pojednostavljen.


## Arhitektura

Kaito prati klasični Kubernetes Custom Resource Definition (CRD)/controller dizajn obrazac. Korisnik upravlja `workspace` prilagođenim resursom koji opisuje zahtjeve za GPU i specifikaciju inferencije. Kaito kontroleri automatiziraju implementaciju usklađivanjem `workspace` prilagođenog resursa.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

Gornja slika prikazuje pregled arhitekture Kaitoa. Njegove glavne komponente su:

- **Workspace controller**: Usklađuje `workspace` prilagođeni resurs, kreira `machine` (objašnjeno u nastavku) prilagođene resurse za pokretanje automatskog osiguravanja čvorova i kreira inferencijski workload (`deployment` ili `statefulset`) na temelju unaprijed definiranih konfiguracija modela.
- **Node provisioner controller**: Kontroler se zove *gpu-provisioner* u [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Koristi `machine` CRD koji potječe iz [Karpenter](https://sigs.k8s.io/karpenter) za interakciju s workspace controllerom. Integrira se s Azure Kubernetes Service (AKS) API-jima za dodavanje novih GPU čvorova u AKS klaster. 
> Note: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) je open source komponenta. Može se zamijeniti drugim kontrolerima ako podržavaju [Karpenter-core](https://sigs.k8s.io/karpenter) API-je.

## Pregledni video  
[Pogledajte Kaito Demo](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)
## Instalacija

Molimo provjerite upute za instalaciju [ovdje](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Brzi početak

Nakon instalacije Kaitoa, možete isprobati sljedeće naredbe za pokretanje fine-tuning servisa.

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

Status workspacea možete pratiti izvođenjem sljedeće naredbe. Kada stupac WORKSPACEREADY postane `True`, model je uspješno implementiran.

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

Zatim možete pronaći cluster IP inferencijskog servisa i koristiti privremeni `curl` pod za testiranje servisne točke u klasteru.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Odricanje od odgovornosti**:  
Ovaj dokument preveden je pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.