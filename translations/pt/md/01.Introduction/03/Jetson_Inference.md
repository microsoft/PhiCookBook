<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "be4101a30d98e95a71d42c276e8bcd37",
  "translation_date": "2025-07-16T20:41:42+00:00",
  "source_file": "md/01.Introduction/03/Jetson_Inference.md",
  "language_code": "pt"
}
-->
# **Inferência Phi-3 no Nvidia Jetson**

Nvidia Jetson é uma série de placas de computação embutidas da Nvidia. Os modelos Jetson TK1, TX1 e TX2 possuem um processador Tegra (ou SoC) da Nvidia que integra uma unidade central de processamento (CPU) com arquitetura ARM. O Jetson é um sistema de baixo consumo energético, projetado para acelerar aplicações de machine learning. A Nvidia Jetson é utilizada por desenvolvedores profissionais para criar produtos inovadores de IA em diversos setores, assim como por estudantes e entusiastas para aprendizagem prática de IA e desenvolvimento de projetos incríveis. O SLM é implementado em dispositivos edge como o Jetson, o que permite uma melhor aplicação de cenários industriais de IA generativa.

## Implementação no NVIDIA Jetson:
Desenvolvedores que trabalham com robótica autónoma e dispositivos embutidos podem tirar proveito do Phi-3 Mini. O tamanho relativamente pequeno do Phi-3 torna-o ideal para implementação em edge. Os parâmetros foram cuidadosamente ajustados durante o treino, garantindo alta precisão nas respostas.

### Otimização TensorRT-LLM:
A biblioteca [TensorRT-LLM da NVIDIA](https://github.com/NVIDIA/TensorRT-LLM?WT.mc_id=aiml-138114-kinfeylo) otimiza a inferência de grandes modelos de linguagem. Suporta a janela de contexto longa do Phi-3 Mini, melhorando tanto o throughput como a latência. As otimizações incluem técnicas como LongRoPE, FP8 e inflight batching.

### Disponibilidade e Implementação:
Os desenvolvedores podem explorar o Phi-3 Mini com a janela de contexto de 128K em [NVIDIA AI](https://www.nvidia.com/en-us/ai-data-science/generative-ai/). Está empacotado como um NVIDIA NIM, um microserviço com uma API padrão que pode ser implementado em qualquer lugar. Além disso, as [implementações TensorRT-LLM no GitHub](https://github.com/NVIDIA/TensorRT-LLM).

## **1. Preparação**

a. Jetson Orin NX / Jetson NX

b. JetPack 5.1.2+

c. Cuda 11.8

d. Python 3.8+

## **2. Executar Phi-3 no Jetson**

Podemos escolher [Ollama](https://ollama.com) ou [LlamaEdge](https://llamaedge.com)

Se quiser usar gguf na cloud e em dispositivos edge ao mesmo tempo, o LlamaEdge pode ser entendido como WasmEdge (WasmEdge é um runtime WebAssembly leve, de alto desempenho e escalável, adequado para aplicações cloud native, edge e descentralizadas. Suporta aplicações serverless, funções embutidas, microserviços, smart contracts e dispositivos IoT). Pode implementar o modelo quantitativo gguf em dispositivos edge e na cloud através do LlamaEdge.

![llamaedge](../../../../../translated_images/pt/llamaedge.e9d6ff96dff11cf7.webp)

Aqui estão os passos para usar

1. Instalar e descarregar as bibliotecas e ficheiros relacionados

```bash

curl -sSf https://raw.githubusercontent.com/WasmEdge/WasmEdge/master/utils/install.sh | bash -s -- --plugin wasi_nn-ggml

curl -LO https://github.com/LlamaEdge/LlamaEdge/releases/latest/download/llama-api-server.wasm

curl -LO https://github.com/LlamaEdge/chatbot-ui/releases/latest/download/chatbot-ui.tar.gz

tar xzf chatbot-ui.tar.gz

```

**Nota**: llama-api-server.wasm e chatbot-ui precisam estar no mesmo diretório

2. Executar os scripts no terminal

```bash

wasmedge --dir .:. --nn-preload default:GGML:AUTO:{Your gguf path} llama-api-server.wasm -p phi-3-chat

```

Aqui está o resultado da execução

![llamaedgerun](../../../../../translated_images/pt/llamaedgerun.bed921516c9a821c.webp)

***Código de exemplo*** [Phi-3 mini WASM Notebook Sample](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm)

Em resumo, o Phi-3 Mini representa um avanço significativo na modelação de linguagem, combinando eficiência, consciência de contexto e o poder de otimização da NVIDIA. Quer esteja a construir robôs ou aplicações edge, o Phi-3 Mini é uma ferramenta poderosa a ter em conta.

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.