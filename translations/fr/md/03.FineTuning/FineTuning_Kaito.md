<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a1c62bf7d86d6186bf8d3917196a92a0",
  "translation_date": "2025-05-07T13:38:05+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Kaito.md",
  "language_code": "fr"
}
-->
## Affinage avec Kaito 

[Kaito](https://github.com/Azure/kaito) est un opérateur qui automatise le déploiement des modèles d'inférence IA/ML dans un cluster Kubernetes.

Kaito se distingue des principales méthodes de déploiement de modèles basées sur des infrastructures de machines virtuelles par les points clés suivants :

- Gestion des fichiers modèles via des images conteneurs. Un serveur http est fourni pour effectuer des appels d'inférence en utilisant la bibliothèque de modèles.
- Évite d'ajuster les paramètres de déploiement pour correspondre au matériel GPU en proposant des configurations prédéfinies.
- Provisionnement automatique des nœuds GPU selon les besoins du modèle.
- Hébergement des images de modèles volumineux dans le Microsoft Container Registry (MCR) public, si la licence le permet.

Avec Kaito, le processus d’intégration de modèles d’inférence IA volumineux dans Kubernetes est grandement simplifié.


## Architecture

Kaito suit le modèle classique de conception Kubernetes Custom Resource Definition (CRD) / contrôleur. L’utilisateur gère une ressource personnalisée `workspace` qui décrit les besoins GPU et la spécification d’inférence. Les contrôleurs Kaito automatisent le déploiement en conciliant la ressource personnalisée `workspace`.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Architecture de Kaito">
</div>

La figure ci-dessus présente une vue d’ensemble de l’architecture Kaito. Ses principaux composants sont :

- **Contrôleur Workspace** : Il concilie la ressource personnalisée `workspace`, crée des ressources personnalisées `machine` (expliquées ci-dessous) pour déclencher le provisionnement automatique des nœuds, et crée la charge de travail d’inférence (`deployment` ou `statefulset`) selon les configurations prédéfinies du modèle.
- **Contrôleur de provisionnement de nœuds** : Ce contrôleur s’appelle *gpu-provisioner* dans le [chart helm gpu-provisioner](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Il utilise le CRD `machine` issu de [Karpenter](https://sigs.k8s.io/karpenter) pour interagir avec le contrôleur workspace. Il s’intègre aux API Azure Kubernetes Service (AKS) pour ajouter de nouveaux nœuds GPU au cluster AKS.
> Note : Le [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) est un composant open source. Il peut être remplacé par d’autres contrôleurs s’ils supportent les API [Karpenter-core](https://sigs.k8s.io/karpenter).

## Vidéo de présentation 
[Regarder la démo de Kaito](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)

## Installation

Veuillez consulter les instructions d’installation [ici](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Démarrage rapide

Après avoir installé Kaito, vous pouvez essayer les commandes suivantes pour lancer un service d’affinage.

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

L’état du workspace peut être suivi avec la commande suivante. Lorsque la colonne WORKSPACEREADY devient `True`, le modèle est déployé avec succès.

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

Ensuite, vous pouvez récupérer l’IP du service d’inférence dans le cluster et utiliser un pod temporaire `curl` pour tester le point de terminaison du service dans le cluster.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant foi. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle humaine. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.