<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e46691923dca7cb2f11d32b1d9d558e0",
  "translation_date": "2025-07-16T20:49:52+00:00",
  "source_file": "md/01.Introduction/03/Kaito_Inference.md",
  "language_code": "pt"
}
-->
## Inferência com Kaito

[Kaito](https://github.com/Azure/kaito) é um operador que automatiza a implementação de modelos de inferência AI/ML num cluster Kubernetes.

O Kaito apresenta as seguintes diferenças chave em comparação com a maioria das metodologias convencionais de implementação de modelos baseadas em infraestruturas de máquinas virtuais:

- Gerir ficheiros de modelos usando imagens de containers. É fornecido um servidor http para realizar chamadas de inferência usando a biblioteca do modelo.
- Evitar a configuração manual dos parâmetros de implementação para adaptar ao hardware GPU, fornecendo configurações pré-definidas.
- Auto-provisionar nós GPU com base nos requisitos do modelo.
- Hospedar imagens de modelos grandes no Microsoft Container Registry (MCR) público, se a licença permitir.

Com o Kaito, o fluxo de trabalho para integrar grandes modelos de inferência AI no Kubernetes é bastante simplificado.

## Arquitetura

O Kaito segue o padrão clássico de design Kubernetes Custom Resource Definition (CRD)/controller. O utilizador gere um recurso personalizado `workspace` que descreve os requisitos de GPU e a especificação de inferência. Os controladores do Kaito automatizam a implementação reconciliando o recurso personalizado `workspace`.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Arquitetura do Kaito" alt="Arquitetura do Kaito">
</div>

A figura acima apresenta uma visão geral da arquitetura do Kaito. Os seus principais componentes consistem em:

- **Controlador Workspace**: Reconciliia o recurso personalizado `workspace`, cria recursos personalizados `machine` (explicados abaixo) para desencadear o auto-provisionamento de nós, e cria a carga de trabalho de inferência (`deployment` ou `statefulset`) com base nas configurações pré-definidas do modelo.
- **Controlador de provisionamento de nós**: O nome do controlador é *gpu-provisioner* no [chart helm gpu-provisioner](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Utiliza o CRD `machine` originado do [Karpenter](https://sigs.k8s.io/karpenter) para interagir com o controlador workspace. Integra-se com as APIs do Azure Kubernetes Service (AKS) para adicionar novos nós GPU ao cluster AKS.
> Nota: O [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) é um componente open source. Pode ser substituído por outros controladores se estes suportarem as APIs [Karpenter-core](https://sigs.k8s.io/karpenter).

## Instalação

Por favor, consulte as instruções de instalação [aqui](https://github.com/Azure/kaito/blob/main/docs/installation.md).

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

O estado do workspace pode ser acompanhado executando o seguinte comando. Quando a coluna WORKSPACEREADY ficar `True`, o modelo foi implementado com sucesso.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

De seguida, pode-se encontrar o IP do serviço de inferência no cluster e usar um pod temporário `curl` para testar o endpoint do serviço no cluster.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Início rápido Inferência Phi-3 com adaptadores

Após instalar o Kaito, pode-se experimentar os seguintes comandos para iniciar um serviço de inferência.

[Código de Exemplo Inferência Phi-3 com Adaptadores](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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

O estado do workspace pode ser acompanhado executando o seguinte comando. Quando a coluna WORKSPACEREADY ficar `True`, o modelo foi implementado com sucesso.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

De seguida, pode-se encontrar o IP do serviço de inferência no cluster e usar um pod temporário `curl` para testar o endpoint do serviço no cluster.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, por favor tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.