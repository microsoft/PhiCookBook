## Inferencia con Kaito 

[Kaito](https://github.com/Azure/kaito) es un operador que automatiza el despliegue de modelos de inferencia AI/ML en un clúster de Kubernetes.

Kaito tiene las siguientes diferencias clave en comparación con la mayoría de las metodologías de despliegue de modelos populares construidas sobre infraestructuras de máquinas virtuales:

- Gestiona los archivos del modelo usando imágenes de contenedor. Se proporciona un servidor http para realizar llamadas de inferencia usando la biblioteca del modelo.
- Evita ajustar parámetros de despliegue para adaptarse al hardware GPU proporcionando configuraciones preestablecidas.
- Provisión automática de nodos GPU basada en los requerimientos del modelo.
- Aloja imágenes de modelos grandes en el Microsoft Container Registry (MCR) público si la licencia lo permite.

Usando Kaito, el flujo de trabajo para incorporar grandes modelos de inferencia AI en Kubernetes se simplifica en gran medida.

## Arquitectura

Kaito sigue el patrón clásico de diseño Custom Resource Definition (CRD)/controlador de Kubernetes. El usuario gestiona un recurso personalizado `workspace` que describe los requerimientos GPU y la especificación de inferencia. Los controladores de Kaito automatizarán el despliegue reconciliando el recurso personalizado `workspace`.

<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/website/static/img/ragarch.png" width=80% title="Arquitectura KAITO RAGEngine" alt="Arquitectura KAITO RAGEngine">
</div>

La figura anterior presenta la visión general de la arquitectura de Kaito. Sus componentes principales consisten en:

- **Controlador Workspace**: Reconciliará el recurso personalizado `workspace`, crea recursos personalizados `machine` (explicados abajo) para activar la provisión automática de nodos y crea la carga de trabajo de inferencia (`deployment` o `statefulset`) basada en las configuraciones preestablecidas del modelo.
- **Controlador de provisión de nodos**: El nombre del controlador es *gpu-provisioner* en el [helm chart gpu-provisioner](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Usa el CRD `machine` originado de [Karpenter](https://sigs.k8s.io/karpenter) para interactuar con el controlador workspace. Se integra con las APIs de Azure Kubernetes Service (AKS) para añadir nuevos nodos GPU al clúster AKS.
> Nota: El [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) es un componente de código abierto. Puede ser reemplazado por otros controladores si soportan las APIs [Karpenter-core](https://sigs.k8s.io/karpenter).

## Instalación

Por favor, revise la guía de instalación [aquí](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Inicio rápido Inferencia Phi-3
[Código de ejemplo Inferencia Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Ajustando la ruta ACR de salida
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3.yaml
```

El estado del workspace puede ser monitoreado ejecutando el siguiente comando. Cuando la columna WORKSPACEREADY sea `True`, el modelo ha sido desplegado exitosamente.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

Luego, puede encontrarse la IP de clúster del servicio de inferencia y usar un pod temporal `curl` para probar el endpoint del servicio dentro del clúster.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Inicio rápido Inferencia Phi-3 con adaptadores

Después de instalar Kaito, puede intentar los siguientes comandos para iniciar un servicio de inferencia.

[Código de ejemplo Inferencia Phi-3 con Adaptadores](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Ajustando la ruta ACR de salida
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3_with_adapters.yaml
```

El estado del workspace puede ser monitoreado ejecutando el siguiente comando. Cuando la columna WORKSPACEREADY sea `True`, el modelo ha sido desplegado exitosamente.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

Luego, puede encontrarse la IP de clúster del servicio de inferencia y usar un pod temporal `curl` para probar el endpoint del servicio dentro del clúster.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Si bien nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por un humano. No nos hacemos responsables por malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->