<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a1c62bf7d86d6186bf8d3917196a92a0",
  "translation_date": "2025-05-09T20:41:24+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Kaito.md",
  "language_code": "fi"
}
-->
## Hienosäätö Kaiton avulla

[Kaito](https://github.com/Azure/kaito) on operaattori, joka automatisoi AI/ML-päätelmallimallien käyttöönoton Kubernetes-klusterissa.

Kaitolla on seuraavat keskeiset erot verrattuna useimpiin virtuaalikoneinfrastruktuurien päälle rakennettuihin yleisiin mallin käyttöönoton menetelmiin:

- Mallitiedostojen hallinta konttikuvien avulla. HTTP-palvelin tarjoaa mahdollisuuden tehdä päätelmäkutsuja mallikirjaston avulla.
- Välttää käyttöönottoasetusten säätämisen GPU-laitteistolle esiasetettujen konfiguraatioiden avulla.
- GPU-solmujen automaattinen provisiointi mallin vaatimusten mukaan.
- Suurten mallikuvien isännöinti julkisessa Microsoft Container Registryssä (MCR), jos lisenssi sallii.

Kaiton avulla suurten AI-päätelmallien käyttöönoton työnkulku Kubernetesissa yksinkertaistuu merkittävästi.


## Arkkitehtuuri

Kaito noudattaa klassista Kubernetesin Custom Resource Definition (CRD) / controller -suunnittelumallia. Käyttäjä hallinnoi `workspace`-erikoisresurssia, joka kuvaa GPU-vaatimukset ja päätelmän spesifikaation. Kaiton kontrollerit automatisoivat käyttöönoton sovittamalla `workspace`-erikoisresurssin.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

Yllä oleva kuva esittää Kaiton arkkitehtuurin yleiskuvan. Sen tärkeimmät osat ovat:

- **Workspace controller**: Se sovittaa `workspace`-erikoisresurssin, luo `machine` (selitetty alla) erikoisresursseja solmujen automaattista provisiointia varten, ja luo päätelmäkuorman (`deployment` tai `statefulset`) mallin esiasetusten perusteella.
- **Node provisioner controller**: Kontrollerin nimi on *gpu-provisioner* [gpu-provisioner helm chartissa](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Se käyttää `machine` CRD:tä, joka on peräisin [Karpenteristä](https://sigs.k8s.io/karpenter) kommunikoidakseen workspace-kontrollerin kanssa. Se integroituu Azure Kubernetes Service (AKS) -rajapintoihin lisätäkseen uusia GPU-solmuja AKS-klusteriin.  
> Huom: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) on avoimen lähdekoodin komponentti. Sen voi korvata muilla kontrollerilla, jos ne tukevat [Karpenter-core](https://sigs.k8s.io/karpenter) -rajapintoja.

## Yleiskatsausvideo  
[Katsotaan Kaito-demo](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)

## Asennus

Tarkista asennusohjeet [täältä](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Pikakäynnistys

Kaiton asentamisen jälkeen voi kokeilla seuraavia komentoja käynnistääkseen hienosäätöpalvelun.

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

Workspace-tilaa voi seurata ajamalla seuraavan komennon. Kun WORKSPACEREADY-sarake näyttää `True`, malli on otettu käyttöön onnistuneesti.

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

Seuraavaksi voi hakea päätelmäpalvelun klusteri-IP:n ja käyttää väliaikaista `curl`-podia testatakseen palvelupistettä klusterissa.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulee pitää virallisena lähteenä. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.