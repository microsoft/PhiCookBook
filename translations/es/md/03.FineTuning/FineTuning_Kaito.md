<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a1c62bf7d86d6186bf8d3917196a92a0",
  "translation_date": "2025-03-27T13:50:43+00:00",
  "source_file": "md\\03.FineTuning\\FineTuning_Kaito.md",
  "language_code": "es"
}
-->
## Ajuste fino con Kaito

[Kaito](https://github.com/Azure/kaito) es un operador que automatiza el despliegue de modelos de inferencia de IA/ML en un clúster de Kubernetes.

Kaito tiene las siguientes diferencias clave en comparación con la mayoría de las metodologías de despliegue de modelos convencionales basadas en infraestructuras de máquinas virtuales:

- Gestiona los archivos de modelos utilizando imágenes de contenedor. Se proporciona un servidor HTTP para realizar llamadas de inferencia utilizando la biblioteca del modelo.
- Evita ajustar parámetros de despliegue para adaptarse al hardware de GPU proporcionando configuraciones preestablecidas.
- Aprovisiona automáticamente nodos GPU según los requisitos del modelo.
- Aloja imágenes de modelos grandes en el Registro de Contenedores Público de Microsoft (MCR) si la licencia lo permite.

Con Kaito, el flujo de trabajo para integrar grandes modelos de inferencia de IA en Kubernetes se simplifica considerablemente.

## Arquitectura

Kaito sigue el clásico patrón de diseño de Definición de Recursos Personalizados (CRD)/controlador de Kubernetes. El usuario gestiona un recurso personalizado `workspace` que describe los requisitos de GPU y las especificaciones de inferencia. Los controladores de Kaito automatizan el despliegue reconciliando el recurso personalizado `workspace`.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Arquitectura de Kaito" alt="Arquitectura de Kaito">
</div>

La figura anterior presenta una visión general de la arquitectura de Kaito. Sus principales componentes son:

- **Controlador de espacio de trabajo**: Reconcila el recurso personalizado `workspace`, crea recursos personalizados `machine` (explicados más adelante) para activar el aprovisionamiento automático de nodos y genera la carga de trabajo de inferencia (`deployment` o `statefulset`) según las configuraciones preestablecidas del modelo.
- **Controlador de aprovisionamiento de nodos**: El nombre del controlador es *gpu-provisioner* en el [helm chart de gpu-provisioner](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Utiliza el CRD `machine` originado de [Karpenter](https://sigs.k8s.io/karpenter) para interactuar con el controlador de espacio de trabajo. Se integra con las APIs de Azure Kubernetes Service (AKS) para agregar nuevos nodos GPU al clúster de AKS.  
> Nota: El [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) es un componente de código abierto. Puede ser reemplazado por otros controladores si admiten las APIs de [Karpenter-core](https://sigs.k8s.io/karpenter).

## Video de resumen 
[Mira la demostración de Kaito](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)
## Instalación

Por favor, consulta la guía de instalación [aquí](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Inicio rápido

Después de instalar Kaito, se pueden ejecutar los siguientes comandos para iniciar un servicio de ajuste fino.

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

El estado del espacio de trabajo puede ser monitoreado ejecutando el siguiente comando. Cuando la columna WORKSPACEREADY cambie a `True`, el modelo se habrá desplegado exitosamente.

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

A continuación, se puede encontrar la IP del clúster del servicio de inferencia y utilizar un pod temporal de `curl` para probar el punto de acceso del servicio dentro del clúster.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de ningún malentendido o interpretación errónea que surja del uso de esta traducción.