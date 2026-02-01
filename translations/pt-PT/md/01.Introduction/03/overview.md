No contexto do Phi-3-mini, inferência refere-se ao processo de usar o modelo para fazer previsões ou gerar resultados com base nos dados de entrada. Deixe-me fornecer mais detalhes sobre o Phi-3-mini e as suas capacidades de inferência.

O Phi-3-mini faz parte da série Phi-3 de modelos lançados pela Microsoft. Estes modelos foram concebidos para redefinir o que é possível com Pequenos Modelos de Linguagem (SLMs).

Aqui estão alguns pontos-chave sobre o Phi-3-mini e as suas capacidades de inferência:

## **Visão Geral do Phi-3-mini:**
- O Phi-3-mini tem um tamanho de parâmetro de 3,8 mil milhões.
- Pode ser executado não só em dispositivos de computação tradicionais, mas também em dispositivos edge, como dispositivos móveis e dispositivos IoT.
- O lançamento do Phi-3-mini permite que indivíduos e empresas implementem SLMs em diferentes dispositivos de hardware, especialmente em ambientes com recursos limitados.
- Abrange vários formatos de modelo, incluindo o formato tradicional PyTorch, a versão quantizada do formato gguf e a versão quantizada baseada em ONNX.

## **Acesso ao Phi-3-mini:**
Para aceder ao Phi-3-mini, pode usar o [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) numa aplicação Copilot. O Semantic Kernel é geralmente compatível com o Azure OpenAI Service, modelos open-source no Hugging Face e modelos locais.  
Também pode usar o [Ollama](https://ollama.com) ou o [LlamaEdge](https://llamaedge.com) para chamar modelos quantizados. O Ollama permite que utilizadores individuais chamem diferentes modelos quantizados, enquanto o LlamaEdge oferece disponibilidade multiplataforma para modelos GGUF.

## **Modelos Quantizados:**
Muitos utilizadores preferem usar modelos quantizados para inferência local. Por exemplo, pode executar diretamente o Ollama run Phi-3 ou configurá-lo offline usando um Modelfile. O Modelfile especifica o caminho do ficheiro GGUF e o formato do prompt.

## **Possibilidades da IA Generativa:**
Combinar SLMs como o Phi-3-mini abre novas possibilidades para a IA generativa. A inferência é apenas o primeiro passo; estes modelos podem ser usados para várias tarefas em cenários com recursos limitados, restrições de latência e custos controlados.

## **Desbloquear a IA Generativa com Phi-3-mini: Um Guia para Inferência e Implementação**  
Aprenda a usar o Semantic Kernel, Ollama/LlamaEdge e ONNX Runtime para aceder e inferir modelos Phi-3-mini, e explore as possibilidades da IA generativa em vários cenários de aplicação.

**Funcionalidades**  
Inferência do modelo phi3-mini em:

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)  
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)  
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)  
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)  
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)  

Em resumo, o Phi-3-mini permite aos programadores explorar diferentes formatos de modelo e tirar partido da IA generativa em vários cenários de aplicação.

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, por favor tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações erradas decorrentes da utilização desta tradução.