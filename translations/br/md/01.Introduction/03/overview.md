<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1ff728038c4f554b660a36b76cbdd6e",
  "translation_date": "2025-05-09T12:23:43+00:00",
  "source_file": "md/01.Introduction/03/overview.md",
  "language_code": "br"
}
-->
No contexto do Phi-3-mini, inferência refere-se ao processo de usar o modelo para fazer previsões ou gerar resultados com base nos dados de entrada. Vou fornecer mais detalhes sobre o Phi-3-mini e suas capacidades de inferência.

O Phi-3-mini faz parte da série Phi-3 de modelos lançados pela Microsoft. Esses modelos foram projetados para redefinir o que é possível com Small Language Models (SLMs).

Aqui estão alguns pontos-chave sobre o Phi-3-mini e suas capacidades de inferência:

## **Visão geral do Phi-3-mini:**
- O Phi-3-mini possui um tamanho de parâmetro de 3,8 bilhões.
- Ele pode ser executado não apenas em dispositivos computacionais tradicionais, mas também em dispositivos de borda, como dispositivos móveis e IoT.
- O lançamento do Phi-3-mini permite que indivíduos e empresas implantem SLMs em diferentes dispositivos de hardware, especialmente em ambientes com recursos limitados.
- Abrange vários formatos de modelo, incluindo o formato tradicional PyTorch, a versão quantizada do formato gguf e a versão quantizada baseada em ONNX.

## **Acessando o Phi-3-mini:**
Para acessar o Phi-3-mini, você pode usar o [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) em uma aplicação Copilot. O Semantic Kernel é geralmente compatível com Azure OpenAI Service, modelos open-source no Hugging Face e modelos locais.  
Você também pode usar [Ollama](https://ollama.com) ou [LlamaEdge](https://llamaedge.com) para chamar modelos quantizados. O Ollama permite que usuários individuais chamem diferentes modelos quantizados, enquanto o LlamaEdge oferece disponibilidade multiplataforma para modelos GGUF.

## **Modelos Quantizados:**
Muitos usuários preferem usar modelos quantizados para inferência local. Por exemplo, você pode executar diretamente o Ollama run Phi-3 ou configurá-lo offline usando um Modelfile. O Modelfile especifica o caminho do arquivo GGUF e o formato do prompt.

## **Possibilidades de IA Generativa:**
Combinar SLMs como o Phi-3-mini abre novas possibilidades para IA generativa. A inferência é apenas o primeiro passo; esses modelos podem ser usados para várias tarefas em cenários com recursos limitados, restrição de latência e custos controlados.

## **Desbloqueando IA Generativa com Phi-3-mini: Um Guia para Inferência e Implantação**  
Aprenda a usar Semantic Kernel, Ollama/LlamaEdge e ONNX Runtime para acessar e inferir modelos Phi-3-mini, e explore as possibilidades da IA generativa em diversos cenários de aplicação.

**Recursos**  
Inferência do modelo phi3-mini em:

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)  
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)  
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)  
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)  
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)

Em resumo, o Phi-3-mini permite que desenvolvedores explorem diferentes formatos de modelo e aproveitem a IA generativa em diversos cenários de aplicação.

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.