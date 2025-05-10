<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e46691923dca7cb2f11d32b1d9d558e0",
  "translation_date": "2025-05-09T11:50:14+00:00",
  "source_file": "md/01.Introduction/03/Kaito_Inference.md",
  "language_code": "pt"
}
-->
## Inferência com Kaito 

[Kaito](https://github.com/Azure/kaito) é um operador que automatiza a implantação de modelos de inferência AI/ML em um cluster Kubernetes.

O Kaito apresenta as seguintes diferenças principais em comparação com a maioria das metodologias tradicionais de implantação de modelos baseadas em infraestruturas de máquinas virtuais:

- Gerencia arquivos de modelo usando imagens de container. Um servidor http é fornecido para realizar chamadas de inferência utilizando a biblioteca do modelo.
- Evita a necessidade de ajustar parâmetros de implantação para se adequar ao hardware GPU, oferecendo configurações pré-definidas.
- Faz o provisionamento automático de nós GPU conforme os requisitos do modelo.
- Hospeda grandes imagens de modelos no Microsoft Container Registry (MCR) público, caso a licença permita.

Com o Kaito, o fluxo de trabalho para integrar grandes modelos de inferência AI no Kubernetes fica muito mais simples.


## Arquitetura

O Kaito segue o padrão clássico de design Kubernetes Custom Resource Definition (CRD)/controller. O usuário gerencia um recurso customizado `workspace` que descreve os requisitos de GPU e a especificação da inferência. Os controllers do Kaito automatizam a implantação reconciliando o recurso customizado `workspace`.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Arquitetura do Kaito" alt="Arquitetura do Kaito">
</div>

A figura acima apresenta uma visão geral da arquitetura do Kaito. Seus principais componentes são:

- **Workspace controller**: Reconciliam o recurso customizado `workspace`, cria recursos customizados `machine` (explicados abaixo) para disparar o provisionamento automático de nós e cria a carga de trabalho de inferência (`deployment` ou `statefulset`) com base nas configurações pré-definidas do modelo.
- **Node provisioner controller**: O nome do controller é *gpu-provisioner* no [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Ele usa o CRD `machine` originado do [Karpenter](https://sigs.k8s.io/karpenter) para interagir com o workspace controller. Integra-se com as APIs do Azure Kubernetes Service (AKS) para adicionar novos nós GPU ao cluster AKS.
> Note: O [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) é um componente open source. Pode ser substituído por outros controllers caso suportem as APIs [Karpenter-core](https://sigs.k8s.io/karpenter).

## Instalação

Por favor, consulte as orientações de instalação [aqui](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Início rápido Inferência Phi-3
[Código de Exemplo Inferência Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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

O status do workspace pode ser acompanhado executando o comando abaixo. Quando a coluna WORKSPACEREADY estiver `True`, o modelo foi implantado com sucesso.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

Em seguida, é possível localizar o IP do serviço de inferência no cluster e usar um pod temporário `curl` para testar o endpoint do serviço dentro do cluster.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Início rápido Inferência Phi-3 com adapters

Após instalar o Kaito, você pode executar os comandos a seguir para iniciar um serviço de inferência.

[Código de Exemplo Inferência Phi-3 com Adapters](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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

O status do workspace pode ser acompanhado executando o comando abaixo. Quando a coluna WORKSPACEREADY estiver `True`, o modelo foi implantado com sucesso.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

Em seguida, é possível localizar o IP do serviço de inferência no cluster e usar um pod temporário `curl` para testar o endpoint do serviço dentro do cluster.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.