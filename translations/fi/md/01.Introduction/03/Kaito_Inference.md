<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e46691923dca7cb2f11d32b1d9d558e0",
  "translation_date": "2025-07-16T20:51:30+00:00",
  "source_file": "md/01.Introduction/03/Kaito_Inference.md",
  "language_code": "fi"
}
-->
## Päättely Kaito:n kanssa

[Kaito](https://github.com/Azure/kaito) on operaattori, joka automatisoi AI/ML-päättelymallien käyttöönoton Kubernetes-klusterissa.

Kaito eroaa seuraavilla tavoilla useimmista virtuaalikoneinfrastruktuurien päälle rakennetuista mallien käyttöönoton menetelmistä:

- Mallitiedostojen hallinta konttikuvien avulla. HTTP-palvelin tarjoaa päättelykutsujen suorittamisen mallikirjastoa käyttäen.
- Välttää käyttöönoton parametrien säätämisen GPU-laitteistolle esiasetettujen konfiguraatioiden avulla.
- GPU-solmujen automaattinen provisiointi mallin vaatimusten perusteella.
- Suurten mallikuvien isännöinti julkisessa Microsoft Container Registryssä (MCR), jos lisenssi sen sallii.

Kaito:n avulla suurten AI-päättelymallien käyttöönoton työnkulku Kubernetesissa yksinkertaistuu merkittävästi.

## Arkkitehtuuri

Kaito noudattaa perinteistä Kubernetesin Custom Resource Definition (CRD) / controller -suunnittelumallia. Käyttäjä hallinnoi `workspace`-custom resourcea, joka kuvaa GPU-vaatimukset ja päättelymäärittelyn. Kaito-controllerit automatisoivat käyttöönoton sovittamalla `workspace`-custom resourcen tilan.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

Yllä oleva kuva esittää Kaito-arkkitehtuurin yleiskuvan. Sen pääkomponentit ovat:

- **Workspace controller**: Sovittaa `workspace`-custom resourcen tilan, luo `machine` (selitetty alla) custom resourcet solmujen automaattista provisiointia varten ja luo päättelytyönkuorman (`deployment` tai `statefulset`) mallin esiasetettujen konfiguraatioiden perusteella.
- **Node provisioner controller**: Controllerin nimi on *gpu-provisioner* [gpu-provisioner helm chartissa](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Se käyttää [Karpenter](https://sigs.k8s.io/karpenter) -projektin `machine` CRD:tä kommunikoidakseen workspace-controllerin kanssa. Se integroituu Azure Kubernetes Service (AKS) -rajapintoihin lisätäkseen uusia GPU-solmuja AKS-klusteriin.
> Huom: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) on avoimen lähdekoodin komponentti. Sen voi korvata muilla controllereilla, jos ne tukevat [Karpenter-core](https://sigs.k8s.io/karpenter) -rajapintoja.

## Asennus

Katso asennusohjeet [täältä](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Nopeasti käyntiin Inference Phi-3:n kanssa
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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Tuning Output ACR Path
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3.yaml
```

Workspace-tilaa voi seurata ajamalla seuraavan komennon. Kun WORKSPACEREADY-sarake muuttuu arvoksi `True`, malli on otettu käyttöön onnistuneesti.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

Seuraavaksi voi hakea päättelypalvelun klusterin IP-osoitteen ja käyttää väliaikaista `curl`-podia testatakseen palvelun päätepistettä klusterissa.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Nopeasti käyntiin Inference Phi-3 adaptereiden kanssa

Kaito:n asennuksen jälkeen voi kokeilla seuraavia komentoja käynnistääkseen päättelypalvelun.

[Esimerkkikoodi Inference Phi-3 adaptereiden kanssa](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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

Workspace-tilaa voi seurata ajamalla seuraavan komennon. Kun WORKSPACEREADY-sarake muuttuu arvoksi `True`, malli on otettu käyttöön onnistuneesti.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

Seuraavaksi voi hakea päättelypalvelun klusterin IP-osoitteen ja käyttää väliaikaista `curl`-podia testatakseen palvelun päätepistettä klusterissa.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.