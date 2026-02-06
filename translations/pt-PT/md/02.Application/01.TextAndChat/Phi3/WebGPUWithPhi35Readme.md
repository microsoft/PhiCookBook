# Phi-3.5-Instruct WebGPU RAG Chatbot

## Demonstração para apresentar WebGPU e o Padrão RAG

O Padrão RAG com o modelo Phi-3.5 Onnx Hosted utiliza a abordagem Retrieval-Augmented Generation, combinando o poder dos modelos Phi-3.5 com o hosting ONNX para implementações de IA eficientes. Este padrão é fundamental para o ajuste fino de modelos para tarefas específicas de domínio, oferecendo uma combinação de qualidade, custo-benefício e compreensão de contextos longos. Faz parte do conjunto Azure AI, que disponibiliza uma vasta seleção de modelos fáceis de encontrar, experimentar e usar, adaptando-se às necessidades de personalização de várias indústrias.

## O que é WebGPU  
WebGPU é uma API moderna de gráficos web concebida para fornecer acesso eficiente à unidade de processamento gráfico (GPU) de um dispositivo diretamente a partir dos navegadores web. Destina-se a ser o sucessor do WebGL, oferecendo várias melhorias importantes:

1. **Compatibilidade com GPUs modernas**: O WebGPU foi criado para funcionar perfeitamente com arquiteturas de GPU contemporâneas, aproveitando APIs do sistema como Vulkan, Metal e Direct3D 12.
2. **Desempenho melhorado**: Suporta computações gerais na GPU e operações mais rápidas, tornando-o adequado tanto para renderização gráfica como para tarefas de machine learning.
3. **Funcionalidades avançadas**: O WebGPU dá acesso a capacidades mais avançadas da GPU, permitindo cargas de trabalho gráficas e computacionais mais complexas e dinâmicas.
4. **Redução da carga no JavaScript**: Ao transferir mais tarefas para a GPU, o WebGPU reduz significativamente a carga de trabalho do JavaScript, resultando em melhor desempenho e experiências mais fluidas.

Atualmente, o WebGPU é suportado em navegadores como o Google Chrome, com trabalhos em curso para expandir o suporte a outras plataformas.

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

#### Abra o seu navegador:  
Inicie o Google Chrome ou Microsoft Edge.

#### Aceda à página de Flags:  
Na barra de endereços, escreva `chrome://flags` e pressione Enter.

#### Procure a flag:  
Na caixa de pesquisa no topo da página, escreva 'enable-unsafe-webgpu'.

#### Ative a flag:  
Encontre a flag #enable-unsafe-webgpu na lista de resultados.

Clique no menu suspenso ao lado e selecione Enabled.

#### Reinicie o navegador:  

Após ativar a flag, será necessário reiniciar o navegador para que as alterações tenham efeito. Clique no botão Relaunch que aparece na parte inferior da página.

- No Linux, inicie o navegador com `--enable-features=Vulkan`.  
- O Safari 18 (macOS 15) tem o WebGPU ativado por defeito.  
- No Firefox Nightly, escreva about:config na barra de endereços e defina dom.webgpu.enabled para true.

### Configurar GPU para Microsoft Edge  

Aqui estão os passos para configurar uma GPU de alto desempenho para o Microsoft Edge no Windows:

- **Abrir Definições:** Clique no menu Iniciar e selecione Definições.  
- **Definições do Sistema:** Vá a Sistema e depois a Ecrã.  
- **Definições de Gráficos:** Desça até ao fim e clique em Definições de gráficos.  
- **Escolher Aplicação:** Em “Escolher uma aplicação para definir preferência,” selecione Aplicação de ambiente de trabalho e depois Procurar.  
- **Selecionar Edge:** Navegue até à pasta de instalação do Edge (normalmente `C:\Program Files (x86)\Microsoft\Edge\Application`) e selecione `msedge.exe`.  
- **Definir Preferência:** Clique em Opções, escolha Alto desempenho e depois clique em Guardar.  
Isto garantirá que o Microsoft Edge utilize a sua GPU de alto desempenho para melhor desempenho.  
- **Reinicie** o seu computador para que estas definições tenham efeito.

### Exemplos : Por favor, [clique neste link](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.