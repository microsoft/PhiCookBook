## Izvođenje zaključaka s Kaitom

[Kaito](https://github.com/Azure/kaito) je operator koji automatizira implementaciju AI/ML modela za izvođenje zaključaka u Kubernetes klasteru.

Kaito ima sljedeće ključne razlike u odnosu na većinu glavnih metoda implementacije modela baziranih na virtualnim strojevima:

- Upravljanje datotekama modela pomoću kontejnerskih slika. HTTP poslužitelj je osiguran za izvođenje poziva za zaključivanje koristeći knjižnicu modela.
- Izbjegava podešavanje parametara implementacije kako bi se prilagodilo GPU hardveru pružajući unaprijed postavljene konfiguracije.
- Automatsko osiguravanje GPU čvorova prema zahtjevima modela.
- Hostiranje velikih slika modela u javnom Microsoft Container Registryu (MCR) ako licenca to dopušta.

Korištenjem Kaitoa, tijek rada uvoza velikih AI modela za izvođenje zaključaka u Kubernetesu je uvelike pojednostavljen.

## Arhitektura

Kaito slijedi klasični Kubernetes obrazac dizajna Custom Resource Definition (CRD)/kontroler. Korisnik upravlja prilagođenim resursom `workspace` koji opisuje zahtjeve za GPU i specifikaciju izvođenja zaključaka. Kaito kontroleri automatiziraju implementaciju usklađivanjem prilagođenog resursa `workspace`.

<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/website/static/img/ragarch.png" width=80% title="KAITO RAGEngine architecture" alt="KAITO RAGEngine architecture">
</div>

Gornja slika prikazuje pregled arhitekture Kaitoa. Njegove glavne komponente sastojale su se od:

- **Workspace kontroler**: Usuglašava prilagođeni resurs `workspace`, kreira prilagođene resurse `machine` (objašnjeno u nastavku) za pokretanje automatskog osiguravanja čvorova te kreira radno opterećenje za zaključivanje (`deployment` ili `statefulset`) na temelju unaprijed postavljenih konfiguracija modela.
- **Node provisioner kontroler**: Kontroler se zove *gpu-provisioner* u [gpu-provisioner helm chartu](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Koristi `machine` CRD koji potječe od [Karpentera](https://sigs.k8s.io/karpenter) za interakciju s workspace kontrolerom. Integrira se s Azure Kubernetes Service (AKS) API-jima kako bi dodao nove GPU čvorove u AKS klaster. 
> Napomena: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) je open source komponenta. Može se zamijeniti drugim kontrolerima ako podržavaju [Karpenter-core](https://sigs.k8s.io/karpenter) API-je.

## Instalacija

Molimo pogledajte upute za instalaciju [ovdje](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Brzi početak Izvođenja zaključaka Phi-3
[Primjer koda za Izvođenje zaključaka Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Podešavanje izlazne ACR staze
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3.yaml
```

Status workspacea može se pratiti pokretanjem sljedeće naredbe. Kada stupac WORKSPACEREADY postane `True`, model je uspješno implementiran.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

Zatim se može pronaći klasterska IP adresa servisa za izvođenje zaključaka i upotrijebiti privremeni `curl` pod za testiranje servisa u klasteru.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Brzi početak Izvođenja zaključaka Phi-3 s adapterima

Nakon instalacije Kaitoa, može se isprobati sljedeće naredbe za pokretanje servisa za izvođenje zaključaka.

[Primjer koda za Izvođenje zaključaka Phi-3 s adapterima](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Podešavanje izlaznog ACR puta
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3_with_adapters.yaml
```

Status workspacea može se pratiti pokretanjem sljedeće naredbe. Kada stupac WORKSPACEREADY postane `True`, model je uspješno implementiran.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

Zatim se može pronaći klasterska IP adresa servisa za izvođenje zaključaka i upotrijebiti privremeni `curl` pod za testiranje servisa u klasteru.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Odricanje od odgovornosti**:
Ovaj dokument je preveden pomoću AI usluge za prijevod [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo biti precizni, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku smatra se službenim i autoritativnim izvorom. Za važne informacije preporučuje se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazume ili pogrešna tumačenja nastala korištenjem ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->