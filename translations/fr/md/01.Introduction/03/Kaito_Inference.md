<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e46691923dca7cb2f11d32b1d9d558e0",
  "translation_date": "2025-03-27T07:28:41+00:00",
  "source_file": "md\\01.Introduction\\03\\Kaito_Inference.md",
  "language_code": "fr"
}
-->
## Inférence avec Kaito 

[Kaito](https://github.com/Azure/kaito) est un opérateur qui automatise le déploiement des modèles d'inférence AI/ML dans un cluster Kubernetes.

Kaito se distingue des méthodologies de déploiement de modèles les plus courantes basées sur des infrastructures de machines virtuelles grâce aux points suivants :

- Gestion des fichiers de modèles à l'aide d'images de conteneurs. Un serveur HTTP est fourni pour effectuer des appels d'inférence en utilisant la bibliothèque de modèles.
- Évite d'ajuster les paramètres de déploiement pour s'adapter au matériel GPU en fournissant des configurations prédéfinies.
- Provisionnement automatique des nœuds GPU en fonction des exigences du modèle.
- Hébergement des images de modèles volumineux dans le registre public Microsoft Container Registry (MCR) si la licence le permet.

Avec Kaito, le processus d'intégration de grands modèles d'inférence AI dans Kubernetes est grandement simplifié.


## Architecture

Kaito suit le modèle classique de conception de définition de ressources personnalisées (CRD)/contrôleur de Kubernetes. L'utilisateur gère une ressource personnalisée `workspace` qui décrit les exigences GPU et les spécifications d'inférence. Les contrôleurs Kaito automatisent le déploiement en réconciliant la ressource personnalisée `workspace`.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Architecture de Kaito" alt="Architecture de Kaito">
</div>

La figure ci-dessus présente une vue d'ensemble de l'architecture de Kaito. Ses principaux composants comprennent :

- **Contrôleur de workspace** : Il réconcilie la ressource personnalisée `workspace`, crée des ressources personnalisées `machine` (expliquées ci-dessous) pour déclencher le provisionnement automatique des nœuds, et crée la charge de travail d'inférence (`deployment` ou `statefulset`) en fonction des configurations prédéfinies du modèle.
- **Contrôleur de provisionnement de nœuds** : Le nom du contrôleur est *gpu-provisioner* dans le [chart helm gpu-provisioner](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Il utilise le CRD `machine` provenant de [Karpenter](https://sigs.k8s.io/karpenter) pour interagir avec le contrôleur de workspace. Il s'intègre aux APIs d'Azure Kubernetes Service (AKS) pour ajouter de nouveaux nœuds GPU au cluster AKS.  
> Note : Le [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) est un composant open source. Il peut être remplacé par d'autres contrôleurs s'ils prennent en charge les APIs [Karpenter-core](https://sigs.k8s.io/karpenter).

## Installation

Veuillez consulter les instructions d'installation [ici](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Démarrage rapide : Inférence Phi-3
[Exemple de code pour l'inférence Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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

Le statut du workspace peut être suivi en exécutant la commande suivante. Lorsque la colonne WORKSPACEREADY devient `True`, le modèle a été déployé avec succès.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

Ensuite, on peut trouver l'ip du service d'inférence dans le cluster et utiliser un pod `curl` temporaire pour tester le point de terminaison du service dans le cluster.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Démarrage rapide : Inférence Phi-3 avec adaptateurs

Après avoir installé Kaito, on peut essayer les commandes suivantes pour démarrer un service d'inférence.

[Exemple de code pour l'inférence Phi-3 avec adaptateurs](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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

Le statut du workspace peut être suivi en exécutant la commande suivante. Lorsque la colonne WORKSPACEREADY devient `True`, le modèle a été déployé avec succès.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

Ensuite, on peut trouver l'ip du service d'inférence dans le cluster et utiliser un pod `curl` temporaire pour tester le point de terminaison du service dans le cluster.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Clause de non-responsabilité** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions de garantir l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de faire appel à une traduction professionnelle réalisée par un humain. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.