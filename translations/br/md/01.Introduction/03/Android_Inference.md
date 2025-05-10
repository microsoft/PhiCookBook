<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9481b07dda8f9715a5d1ff43fb27568b",
  "translation_date": "2025-05-09T10:44:12+00:00",
  "source_file": "md/01.Introduction/03/Android_Inference.md",
  "language_code": "br"
}
-->
# **Inferência Phi-3 no Android**

Vamos ver como realizar inferência com Phi-3-mini em dispositivos Android. Phi-3-mini é uma nova série de modelos da Microsoft que permite a implantação de Large Language Models (LLMs) em dispositivos de borda e IoT.

## Semantic Kernel e Inferência

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) é um framework de aplicação que permite criar apps compatíveis com Azure OpenAI Service, modelos OpenAI e até modelos locais. Se você é novo no Semantic Kernel, sugerimos dar uma olhada no [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo).

### Para acessar Phi-3-mini usando Semantic Kernel

Você pode combiná-lo com o Hugging Face Connector no Semantic Kernel. Consulte este [Exemplo de Código](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo).

Por padrão, ele usa o ID do modelo no Hugging Face. No entanto, você também pode conectar-se a um servidor de modelo Phi-3-mini construído localmente.

### Chamando modelos quantizados com Ollama ou LlamaEdge

Muitos usuários preferem usar modelos quantizados para rodar localmente. [Ollama](https://ollama.com/) e [LlamaEdge](https://llamaedge.com) permitem que usuários individuais chamem diferentes modelos quantizados:

#### Ollama

Você pode rodar diretamente `ollama run Phi-3` ou configurá-lo offline criando um `Modelfile` com o caminho para seu arquivo `.gguf`.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Exemplo de Código](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

Se quiser usar arquivos `.gguf` na nuvem e em dispositivos de borda ao mesmo tempo, LlamaEdge é uma ótima opção. Você pode consultar este [exemplo de código](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) para começar.

### Instalar e rodar em celulares Android

1. **Baixe o app MLC Chat** (Gratuito) para celulares Android.  
2. Baixe o arquivo APK (148MB) e instale no seu dispositivo.  
3. Abra o app MLC Chat. Você verá uma lista de modelos de IA, incluindo Phi-3-mini.

Em resumo, Phi-3-mini abre possibilidades empolgantes para IA generativa em dispositivos de borda, e você pode começar a explorar suas capacidades no Android.

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.