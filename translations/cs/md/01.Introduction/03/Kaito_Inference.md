<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e46691923dca7cb2f11d32b1d9d558e0",
  "translation_date": "2025-05-09T11:58:39+00:00",
  "source_file": "md/01.Introduction/03/Kaito_Inference.md",
  "language_code": "cs"
}
-->
## Inference with Kaito 

[Kaito](https://github.com/Azure/kaito) es un operador que automatiza el despliegue de modelos de inferencia AI/ML en un clúster de Kubernetes.

Kaito presenta las siguientes diferencias clave en comparación con la mayoría de las metodologías convencionales de despliegue de modelos basadas en infraestructuras de máquinas virtuales:

- Gestiona los archivos del modelo usando imágenes de contenedor. Se proporciona un servidor http para realizar llamadas de inferencia usando la biblioteca del modelo.
- Evita ajustar parámetros de despliegue para adaptarse al hardware GPU proporcionando configuraciones predefinidas.
- Provisión automática de nodos GPU según los requerimientos del modelo.
- Aloja imágenes de modelos grandes en el Microsoft Container Registry (MCR) público si la licencia lo permite.

Con Kaito, el flujo de trabajo para incorporar grandes modelos de inferencia AI en Kubernetes se simplifica considerablemente.


## Arquitectura

Kaito sigue el patrón clásico de diseño Kubernetes Custom Resource Definition (CRD)/controlador. El usuario gestiona un recurso personalizado `workspace` que describe los requerimientos de GPU y la especificación de inferencia. Los controladores de Kaito automatizan el despliegue reconciliando el recurso personalizado `workspace`.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

La figura anterior presenta una visión general de la arquitectura de Kaito. Sus componentes principales son:

- **Controlador de workspace**: Reconciliará el recurso personalizado `workspace`, creará recursos personalizados `machine` (explicados más adelante) para activar la provisión automática de nodos, y creará la carga de trabajo de inferencia (`deployment` o `statefulset`) basada en las configuraciones predefinidas del modelo.
- **Controlador de provisión de nodos**: El nombre del controlador es *gpu-provisioner* en el [chart helm gpu-provisioner](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Utiliza el CRD `machine` originado de [Karpenter](https://sigs.k8s.io/karpenter) para interactuar con el controlador de workspace. Se integra con las APIs de Azure Kubernetes Service (AKS) para añadir nuevos nodos GPU al clúster AKS. 
> Nota: El componente de código abierto [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) puede ser reemplazado por otros controladores si soportan las APIs de [Karpenter-core](https://sigs.k8s.io/karpenter).

## Instalación

Por favor, consulta la guía de instalación [aquí](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Inicio rápido Inference Phi-3
[Código de ejemplo Inference Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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

El estado del workspace puede ser monitoreado ejecutando el siguiente comando. Cuando la columna WORKSPACEREADY sea `True`, el modelo se ha desplegado con éxito.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

A continuación, se puede obtener la IP del servicio de inferencia en el clúster y usar un pod temporal con `curl` para probar el endpoint del servicio dentro del clúster.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Inicio rápido Inference Phi-3 con adaptadores

Después de instalar Kaito, se pueden probar los siguientes comandos para iniciar un servicio de inferencia.

[Código de ejemplo Inference Phi-3 con adaptadores](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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

El estado del workspace puede ser monitoreado ejecutando el siguiente comando. Cuando la columna WORKSPACEREADY sea `True`, el modelo se ha desplegado con éxito.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

A continuación, se puede obtener la IP del servicio de inferencia en el clúster y usar un pod temporal con `curl` para probar el endpoint del servicio dentro del clúster.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.