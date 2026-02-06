## Päättely Kaiton kanssa

[Kaito](https://github.com/Azure/kaito) on operaattori, joka automatisoi AI/ML päättelymallien käyttöönoton Kubernetes-klusterissa.

Kaitolla on seuraavat keskeiset erot verrattuna useimpiin yleisiin mallien käyttöönoton menetelmiin, jotka perustuvat virtuaalikoneinfrastruktuureihin:

- Mallitiedostojen hallinta konttien kuvien avulla. HTTP-palvelin on käytettävissä päättelykutsujen tekemiseen mallikirjastoa hyödyntäen.
- Välttää käyttöönoton parametrien säätämisen GPU-laitteistolle tarjoamalla valmiita kokoonpanoja.
- GPU-solmujen automaattinen provisiointi mallin vaatimusten perusteella.
- Suurten mallikuvien isännöinti julkisessa Microsoft Container Registryssä (MCR), mikäli lisenssi sallii.

Kaiton avulla suurten AI-päättelymallien käyttöönoton työnkulku Kubernetesissa on merkittävästi yksinkertaistettu.


## Arkkitehtuuri

Kaito noudattaa klassista Kubernetes Custom Resource Definition (CRD) / controller -suunnittelumallia. Käyttäjä hallinnoi `workspace`-erikoisresurssia, joka kuvaa GPU-vaatimukset ja päättelymäärityksen. Kaiton kontrollerit automatisoivat käyttöönoton sovittamalla `workspace`-erikoisresurssin.

<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/website/static/img/ragarch.png" width=80% title="KAITO RAGEngine architecture" alt="KAITO RAGEngine architecture">
</div>

Yllä oleva kuva esittää Kaiton arkkitehtuurin yleiskatsauksen. Sen keskeiset osat ovat:

- **Workspace controller**: Se sovittaa `workspace`-erikoisresurssin, luo `machine` (selitetty alla) -erikoisresursseja noden automaattista provisiointia varten sekä luo päättelytyökuorman (`deployment` tai `statefulset`) mallin valmiisiin asetuksiin perustuen.
- **Node provisioner controller**: Kontrollerin nimi on *gpu-provisioner* [gpu-provisioner helm chartissa](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Se käyttää `machine` CRD:tä, joka on peräisin [Karpenteriltä](https://sigs.k8s.io/karpenter) ja toimii yhdessä workspace-kontrollerin kanssa. Se integroituu Azure Kubernetes Servicen (AKS) API:hin lisätäkseen uusia GPU-nodeja AKS-klusteriin.
> Huomautus: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) on avoimen lähdekoodin komponentti. Sen voi korvata muilla kontrollerilla, jos ne tukevat [Karpenter-core](https://sigs.k8s.io/karpenter) API:a.

## Asennus

Tarkista asennusohjeet [tästä](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Nopeasti käyntiin Inference Phi-3
[Esimerkkikoodi Inference Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Säädetään ulostulon ACR-polku
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3.yaml
```

Workspace-tilaa voi seurata suorittamalla seuraavan komennon. Kun WORKSPACEREADY-sarake muuttuu `True`:ksi, malli on otettu käyttöön onnistuneesti.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

Seuraavaksi voi löytää päättelypalvelun klusterin IP-osoitteen ja käyttää tilapäistä `curl`-podia palvelun päätepisteen testaamiseen klusterissa.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Nopeasti käyntiin Inference Phi-3 adaptereilla

Kaiton asennuksen jälkeen voi kokeilla seuraavia komentoja käynnistääkseen päättelypalvelun.

[Esimerkkikoodi Inference Phi-3 adaptereilla](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Säätö Output ACR -polku
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3_with_adapters.yaml
```

Workspace-tilaa voi seurata suorittamalla seuraavan komennon. Kun WORKSPACEREADY-sarake muuttuu `True`:ksi, malli on otettu käyttöön onnistuneesti.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

Seuraavaksi voi löytää päättelypalvelun klusterin IP-osoitteen ja käyttää tilapäistä `curl`-podia palvelun päätepisteen testaamiseen klusterissa.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty tekoälypohjaisella käännöspalvelulla [Co-op Translator](https://github.com/Azure/co-op-translator). Pyrimme tarkkuuteen, mutta huomioithan, että automaattikäännöksissä voi esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulisi pitää luotettavana lähteenä. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tästä käännöksestä mahdollisesti aiheutuvista väärinkäsityksistä tai virhetulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->