<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9481b07dda8f9715a5d1ff43fb27568b",
  "translation_date": "2025-07-16T20:13:09+00:00",
  "source_file": "md/01.Introduction/03/Android_Inference.md",
  "language_code": "br"
}
-->
# **Inferência Phi-3 no Android**

Vamos explorar como você pode realizar inferência com o Phi-3-mini em dispositivos Android. O Phi-3-mini é uma nova série de modelos da Microsoft que permite a implantação de Grandes Modelos de Linguagem (LLMs) em dispositivos de borda e dispositivos IoT.

## Semantic Kernel e Inferência

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) é um framework de aplicação que permite criar aplicativos compatíveis com o Azure OpenAI Service, modelos OpenAI e até mesmo modelos locais. Se você é novo no Semantic Kernel, sugerimos que confira o [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo).

### Para acessar o Phi-3-mini usando o Semantic Kernel

Você pode combiná-lo com o Hugging Face Connector no Semantic Kernel. Consulte este [Código de Exemplo](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo).

Por padrão, ele corresponde ao ID do modelo no Hugging Face. No entanto, você também pode se conectar a um servidor de modelo Phi-3-mini construído localmente.

### Chamando modelos quantizados com Ollama ou LlamaEdge

Muitos usuários preferem usar modelos quantizados para rodar modelos localmente. [Ollama](https://ollama.com/) e [LlamaEdge](https://llamaedge.com) permitem que usuários individuais chamem diferentes modelos quantizados:

#### Ollama

Você pode executar diretamente `ollama run Phi-3` ou configurá-lo offline criando um `Modelfile` com o caminho para seu arquivo `.gguf`.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Código de Exemplo](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

Se você quiser usar arquivos `.gguf` na nuvem e em dispositivos de borda simultaneamente, o LlamaEdge é uma ótima opção. Você pode consultar este [código de exemplo](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) para começar.

### Instalar e rodar em celulares Android

1. **Baixe o app MLC Chat** (Gratuito) para celulares Android.  
2. Baixe o arquivo APK (148MB) e instale no seu dispositivo.  
3. Abra o app MLC Chat. Você verá uma lista de modelos de IA, incluindo o Phi-3-mini.

Em resumo, o Phi-3-mini abre possibilidades empolgantes para IA generativa em dispositivos de borda, e você pode começar a explorar suas capacidades no Android.

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.