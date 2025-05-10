<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b62864faf628eb07f5231d4885555198",
  "translation_date": "2025-05-09T18:56:50+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md",
  "language_code": "pt"
}
-->
# Phi-3.5-Instruct WebGPU RAG Chatbot

## Demonstração para apresentar WebGPU e o padrão RAG

O padrão RAG com o modelo Phi-3.5 Onnx hospedado utiliza a abordagem Retrieval-Augmented Generation, combinando o poder dos modelos Phi-3.5 com o hosting ONNX para implantações de IA eficientes. Esse padrão é fundamental para o fine-tuning de modelos para tarefas específicas de domínio, oferecendo uma combinação de qualidade, custo-benefício e compreensão de contexto longo. Faz parte do conjunto Azure AI, que oferece uma ampla seleção de modelos fáceis de encontrar, testar e usar, atendendo às necessidades de personalização de diversos setores.

## O que é WebGPU  
WebGPU é uma API moderna de gráficos web projetada para fornecer acesso eficiente à unidade de processamento gráfico (GPU) de um dispositivo diretamente dos navegadores. É a sucessora do WebGL, oferecendo várias melhorias importantes:

1. **Compatibilidade com GPUs modernas**: WebGPU foi criado para funcionar perfeitamente com arquiteturas de GPU contemporâneas, aproveitando APIs do sistema como Vulkan, Metal e Direct3D 12.
2. **Desempenho aprimorado**: Suporta computações gerais na GPU e operações mais rápidas, tornando-o adequado tanto para renderização gráfica quanto para tarefas de aprendizado de máquina.
3. **Recursos avançados**: WebGPU oferece acesso a capacidades mais avançadas da GPU, permitindo gráficos e cargas computacionais mais complexas e dinâmicas.
4. **Redução da carga do JavaScript**: Ao transferir mais tarefas para a GPU, o WebGPU reduz significativamente a carga no JavaScript, resultando em melhor desempenho e experiências mais fluidas.

Atualmente, o WebGPU é suportado em navegadores como Google Chrome, com trabalho em andamento para ampliar o suporte para outras plataformas.

### 03.WebGPU  
Ambiente necessário:

**Navegadores suportados:**  
- Google Chrome 113+  
- Microsoft Edge 113+  
- Safari 18 (macOS 15)  
- Firefox Nightly.

### Ativar WebGPU:

- No Chrome/Microsoft Edge  

Ative a flag `chrome://flags/#enable-unsafe-webgpu`.

#### Abra seu navegador:  
Inicie o Google Chrome ou Microsoft Edge.

#### Acesse a página de Flags:  
Na barra de endereços, digite `chrome://flags` e pressione Enter.

#### Procure pela flag:  
Na caixa de busca no topo da página, digite 'enable-unsafe-webgpu'

#### Ative a flag:  
Encontre a flag #enable-unsafe-webgpu na lista de resultados.

Clique no menu suspenso ao lado e selecione Enabled.

#### Reinicie seu navegador:  

Após ativar a flag, será necessário reiniciar o navegador para que as alterações tenham efeito. Clique no botão Relaunch que aparecerá na parte inferior da página.

- No Linux, inicie o navegador com `--enable-features=Vulkan`.  
- Safari 18 (macOS 15) já vem com WebGPU ativado por padrão.  
- No Firefox Nightly, digite about:config na barra de endereços e `set dom.webgpu.enabled to true`.

### Configurando a GPU para Microsoft Edge  

Aqui estão os passos para configurar uma GPU de alto desempenho para o Microsoft Edge no Windows:

- **Abra as Configurações:** Clique no menu Iniciar e selecione Configurações.  
- **Configurações do sistema:** Vá em Sistema e depois em Tela.  
- **Configurações de gráficos:** Role para baixo e clique em Configurações de gráficos.  
- **Escolha o app:** Em “Escolha um aplicativo para definir preferência”, selecione Aplicativo de área de trabalho e depois Procurar.  
- **Selecione o Edge:** Navegue até a pasta de instalação do Edge (geralmente `C:\Program Files (x86)\Microsoft\Edge\Application`) e selecione `msedge.exe`.  
- **Defina a preferência:** Clique em Opções, escolha Alto desempenho e depois clique em Salvar.  
Isso garantirá que o Microsoft Edge use sua GPU de alto desempenho para melhor performance.  
- **Reinicie** sua máquina para que as configurações tenham efeito.

### Exemplos : Por favor, [clique neste link](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, por favor, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.