<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "faa063cfc6d50047bbfdb58a90d520ad",
  "translation_date": "2025-04-04T12:45:59+00:00",
  "source_file": "md\\02.Application\\01.TextAndChat\\Phi3\\WebGPUWithPhi35Readme.md",
  "language_code": "mo"
}
-->
# Phi-3.5-Instruct WebGPU RAG Chatbot

## Demo da apresentação do WebGPU e do padrão RAG

O padrão RAG com o modelo Phi-3.5 hospedado em ONNX utiliza a abordagem de Geração com Recuperação Incrementada, combinando a capacidade dos modelos Phi-3.5 com a hospedagem ONNX para implantações de IA eficientes. Esse padrão é essencial para ajustar modelos a tarefas específicas de domínio, oferecendo uma combinação de qualidade, custo-benefício e compreensão de contextos longos. Faz parte do conjunto de ferramentas do Azure AI, que disponibiliza uma ampla variedade de modelos fáceis de encontrar, experimentar e usar, atendendo às necessidades de personalização de diferentes indústrias.

## O que é WebGPU 
WebGPU é uma API moderna de gráficos para web projetada para oferecer acesso eficiente à unidade de processamento gráfico (GPU) de um dispositivo diretamente dos navegadores. Ela foi desenvolvida como sucessora do WebGL, trazendo várias melhorias importantes:

1. **Compatibilidade com GPUs Modernas**: O WebGPU foi criado para funcionar perfeitamente com arquiteturas de GPU contemporâneas, utilizando APIs do sistema como Vulkan, Metal e Direct3D 12.
2. **Desempenho Melhorado**: Suporta cálculos gerais em GPU e operações mais rápidas, tornando-o adequado tanto para renderização gráfica quanto para tarefas de aprendizado de máquina.
3. **Recursos Avançados**: O WebGPU oferece acesso a capacidades mais avançadas de GPU, permitindo cargas de trabalho gráficas e computacionais mais complexas e dinâmicas.
4. **Menor Carga no JavaScript**: Ao transferir mais tarefas para a GPU, o WebGPU reduz significativamente a carga no JavaScript, resultando em melhor desempenho e experiências mais suaves.

Atualmente, o WebGPU é compatível com navegadores como Google Chrome, com esforços em andamento para expandir o suporte a outras plataformas.

### 03.WebGPU
Ambiente necessário:

**Navegadores compatíveis:** 
- Google Chrome 113+
- Microsoft Edge 113+
- Safari 18 (macOS 15)
- Firefox Nightly.

### Ativar o WebGPU:

- No Chrome/Microsoft Edge 

Ative a flag `chrome://flags/#enable-unsafe-webgpu`.

#### Abra seu navegador:
Inicie o Google Chrome ou Microsoft Edge.

#### Acesse a página de flags:
Na barra de endereço, digite `chrome://flags` e pressione Enter.

#### Pesquise pela flag:
Na caixa de busca no topo da página, digite 'enable-unsafe-webgpu'.

#### Ative a flag:
Localize a flag #enable-unsafe-webgpu na lista de resultados.

Clique no menu suspenso ao lado dela e selecione Enabled.

#### Reinicie o navegador:

Após ativar a flag, será necessário reiniciar o navegador para que as mudanças entrem em vigor. Clique no botão Relaunch que aparece na parte inferior da página.

- Para Linux, inicie o navegador com `--enable-features=Vulkan`.
- Safari 18 (macOS 15) tem o WebGPU ativado por padrão.
- No Firefox Nightly, digite about:config na barra de endereço e `set dom.webgpu.enabled to true`.

### Configurando GPU para Microsoft Edge 

Veja os passos para configurar uma GPU de alto desempenho para o Microsoft Edge no Windows:

- **Abra Configurações:** Clique no menu Iniciar e selecione Configurações.
- **Configurações do Sistema:** Vá para Sistema e depois para Tela.
- **Configurações de Gráficos:** Role para baixo e clique em Configurações de gráficos.
- **Escolher Aplicativo:** Em “Escolha um aplicativo para definir a preferência,” selecione Aplicativo da área de trabalho e depois Procurar.
- **Selecione o Edge:** Navegue até a pasta de instalação do Edge (geralmente `C:\Program Files (x86)\Microsoft\Edge\Application`) e selecione `msedge.exe`.
- **Defina a Preferência:** Clique em Opções, escolha Alto desempenho e depois clique em Salvar.
Isso garantirá que o Microsoft Edge utilize sua GPU de alto desempenho para um desempenho melhor. 
- **Reinicie** sua máquina para que essas configurações entrem em vigor.

### Exemplos: Por favor [clique neste link](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

It seems like "mo" might refer to a specific language or dialect, but I need clarification on what "mo" stands for. Could you please specify the language or provide additional context?