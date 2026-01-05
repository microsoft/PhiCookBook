<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aca91084bc440431571e00bf30d96ab8",
  "translation_date": "2026-01-05T02:53:25+00:00",
  "source_file": "md/01.Introduction/03/Kaito_Inference.md",
  "language_code": "pt"
}
-->
## Inferência com Kaito 

[Kaito](https://github.com/Azure/kaito) é um operador que automatiza o deployment de modelos de inferência AI/ML num cluster Kubernetes.

Kaito apresenta as seguintes diferenças chave comparado com a maioria das metodologias de deployment de modelos mainstream construídas sobre infraestruturas de máquinas virtuais:

- Gerir ficheiros de modelo usando imagens de container. É fornecido um servidor HTTP para efectuar chamadas de inferência usando a biblioteca do modelo.
- Evitar a afinação de parâmetros de deployment para adaptar ao hardware GPU, fornecendo configurações predefinidas.
- Auto-provisionamento de nós GPU com base nos requisitos do modelo.
- Hospedar imagens de modelos grandes no Microsoft Container Registry (MCR) público se a licença permitir.

Usando o Kaito, o fluxo de trabalho de integração de grandes modelos de inferência AI no Kubernetes é amplamente simplificado.


## Arquitetura

Kaito segue o clássico padrão de design Custom Resource Definition(CRD)/controller do Kubernetes. O utilizador gere um recurso customizado `workspace` que descreve os requisitos de GPU e a especificação de inferência. Os controllers do Kaito irão automatizar o deployment reconciliando o recurso customizado `workspace`.

<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/website/static/img/ragarch.png" width=80% title="Arquitetura do KAITO RAGEngine" alt="Arquitetura do KAITO RAGEngine">
</div>

A figura acima apresenta a visão geral da arquitetura do Kaito. Os seus principais componentes consistem em:

- **Workspace controller**: Reconcila o recurso customizado `workspace`, cria recursos customizados `machine` (explicado abaixo) para desencadear o auto-provisionamento de nós, e cria a carga de trabalho de inferência (`deployment` ou `statefulset`) com base nas configurações predefinidas do modelo.
- **Node provisioner controller**: O nome do controller é *gpu-provisioner* no [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Utiliza o `machine` CRD originado do [Karpenter](https://sigs.k8s.io/karpenter) para interagir com o workspace controller. Integra-se com as APIs do Azure Kubernetes Service(AKS) para adicionar novos nós GPU ao cluster AKS. 
> Note: The [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) is an open sourced component. It can be replaced by other controllers if they support [Karpenter-core](https://sigs.k8s.io/karpenter) APIs.

## Instalação

Por favor verifique a orientação de instalação [here](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Início rápido Inferência Phi-3
[Sample Code Inference Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Caminho da saída ACR para afinação
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3.yaml
```

O estado do workspace pode ser acompanhado executando o seguinte comando. Quando a coluna WORKSPACEREADY se tornar `True`, o modelo foi deployado com sucesso.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

De seguida, pode encontrar o IP do cluster do serviço de inferência e usar um pod `curl` temporal para testar o endpoint do serviço no cluster.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Início rápido Inferência Phi-3 com adapters

Após instalar o Kaito, pode experimentar os seguintes comandos para iniciar um serviço de inferência.

[Sample Code Inference Phi-3 with Adapters](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Caminho ACR da Saída de Ajuste
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3_with_adapters.yaml
```

O estado do workspace pode ser acompanhado executando o seguinte comando. Quando a coluna WORKSPACEREADY se tornar `True`, o modelo foi deployado com sucesso.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

De seguida, pode encontrar o IP do cluster do serviço de inferência e usar um pod `curl` temporal para testar o endpoint do serviço no cluster.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Isenção de responsabilidade:
Este documento foi traduzido com recurso ao serviço de tradução por IA Co-op Translator (https://github.com/Azure/co-op-translator). Embora nos esforcemos por garantir a precisão, tenha em atenção que traduções automáticas podem conter erros ou imprecisões. O documento original, na sua língua nativa, deve ser considerado a fonte autoritativa. Para informação crítica, recomenda-se a tradução profissional por um tradutor humano. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->