# **Inferência Phi-3 no Android**

Vamos explorar como pode realizar inferência com o Phi-3-mini em dispositivos Android. O Phi-3-mini é uma nova série de modelos da Microsoft que permite a implementação de Large Language Models (LLMs) em dispositivos edge e dispositivos IoT.

## Semantic Kernel e Inferência

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) é um framework de aplicação que permite criar aplicações compatíveis com o Azure OpenAI Service, modelos OpenAI e até modelos locais. Se é novo no Semantic Kernel, sugerimos que consulte o [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo).

### Para Aceder ao Phi-3-mini Usando o Semantic Kernel

Pode combiná-lo com o Hugging Face Connector no Semantic Kernel. Consulte este [Exemplo de Código](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo).

Por defeito, corresponde ao ID do modelo no Hugging Face. No entanto, também pode ligar-se a um servidor de modelo Phi-3-mini construído localmente.

### Chamar Modelos Quantizados com Ollama ou LlamaEdge

Muitos utilizadores preferem usar modelos quantizados para executar modelos localmente. [Ollama](https://ollama.com/) e [LlamaEdge](https://llamaedge.com) permitem que utilizadores individuais chamem diferentes modelos quantizados:

#### Ollama

Pode executar diretamente `ollama run Phi-3` ou configurá-lo offline criando um `Modelfile` com o caminho para o seu ficheiro `.gguf`.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Exemplo de Código](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

Se quiser usar ficheiros `.gguf` na cloud e em dispositivos edge simultaneamente, o LlamaEdge é uma excelente opção. Pode consultar este [exemplo de código](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) para começar.

### Instalar e Executar em Telemóveis Android

1. **Descarregue a app MLC Chat** (Grátis) para telemóveis Android.  
2. Descarregue o ficheiro APK (148MB) e instale-o no seu dispositivo.  
3. Abra a app MLC Chat. Vai ver uma lista de modelos de IA, incluindo o Phi-3-mini.

Em resumo, o Phi-3-mini abre possibilidades entusiasmantes para IA generativa em dispositivos edge, e pode começar a explorar as suas capacidades no Android.

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações erradas decorrentes da utilização desta tradução.