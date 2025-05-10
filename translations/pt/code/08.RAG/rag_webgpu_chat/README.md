<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4aac6b8a5dcbbe9a32b47be30340cac2",
  "translation_date": "2025-05-09T05:16:47+00:00",
  "source_file": "code/08.RAG/rag_webgpu_chat/README.md",
  "language_code": "pt"
}
-->
Phi-3-mini WebGPU RAG Chatbot

## Demonstração para apresentar WebGPU e o padrão RAG
O padrão RAG com o modelo Phi-3 Onnx hospedado utiliza a abordagem de Geração Aumentada por Recuperação, combinando o poder dos modelos Phi-3 com hospedagem ONNX para implantações de IA eficientes. Esse padrão é fundamental para o ajuste fino de modelos para tarefas específicas de domínio, oferecendo uma combinação de qualidade, custo-benefício e compreensão de contexto longo. Faz parte da suíte Azure AI, que oferece uma ampla seleção de modelos fáceis de encontrar, testar e usar, atendendo às necessidades de personalização de vários setores. Os modelos Phi-3, incluindo Phi-3-mini, Phi-3-small e Phi-3-medium, estão disponíveis no Azure AI Model Catalog e podem ser ajustados e implantados de forma autogerenciada ou por meio de plataformas como HuggingFace e ONNX, demonstrando o compromisso da Microsoft com soluções de IA acessíveis e eficientes.

## O que é WebGPU
WebGPU é uma API gráfica web moderna projetada para fornecer acesso eficiente à unidade de processamento gráfico (GPU) de um dispositivo diretamente dos navegadores. Destina-se a ser o sucessor do WebGL, oferecendo várias melhorias importantes:

1. **Compatibilidade com GPUs modernas**: WebGPU foi criado para funcionar perfeitamente com arquiteturas contemporâneas de GPU, aproveitando APIs do sistema como Vulkan, Metal e Direct3D 12.
2. **Desempenho aprimorado**: Suporta computações gerais na GPU e operações mais rápidas, tornando-o adequado tanto para renderização gráfica quanto para tarefas de aprendizado de máquina.
3. **Recursos avançados**: WebGPU oferece acesso a capacidades mais avançadas da GPU, permitindo cargas de trabalho gráficas e computacionais mais complexas e dinâmicas.
4. **Redução da carga do JavaScript**: Ao descarregar mais tarefas para a GPU, WebGPU reduz significativamente a carga sobre o JavaScript, resultando em melhor desempenho e experiências mais fluidas.

WebGPU é atualmente suportado em navegadores como Google Chrome, com trabalho em andamento para expandir o suporte a outras plataformas.

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

#### Acesse a página de flags:
Na barra de endereços, digite `chrome://flags` e pressione Enter.

#### Procure pela flag:
Na caixa de pesquisa no topo da página, digite 'enable-unsafe-webgpu'

#### Ative a flag:
Encontre a flag #enable-unsafe-webgpu na lista de resultados.

Clique no menu suspenso ao lado e selecione Enabled.

#### Reinicie seu navegador:

Após ativar a flag, será necessário reiniciar o navegador para que as mudanças tenham efeito. Clique no botão Relaunch que aparece na parte inferior da página.

- No Linux, inicie o navegador com `--enable-features=Vulkan`.
- Safari 18 (macOS 15) já vem com WebGPU ativado por padrão.
- No Firefox Nightly, entre em about:config na barra de endereços e `set dom.webgpu.enabled to true`.

### Configurando a GPU para Microsoft Edge

Aqui estão os passos para configurar uma GPU de alto desempenho para o Microsoft Edge no Windows:

- **Abra as Configurações:** Clique no menu Iniciar e selecione Configurações.
- **Configurações do Sistema:** Vá para Sistema e depois Exibir.
- **Configurações de Gráficos:** Role para baixo e clique em Configurações de gráficos.
- **Escolha o App:** Em “Escolha um app para definir preferência,” selecione App para área de trabalho e depois Procurar.
- **Selecione o Edge:** Navegue até a pasta de instalação do Edge (normalmente `C:\Program Files (x86)\Microsoft\Edge\Application`) e selecione `msedge.exe`.
- **Defina a preferência:** Clique em Opções, escolha Alto desempenho e depois clique em Salvar.
Isso garantirá que o Microsoft Edge use sua GPU de alto desempenho para melhor desempenho.
- **Reinicie** sua máquina para que as configurações tenham efeito.

### Abra seu Codespace:
Navegue até seu repositório no GitHub.
Clique no botão Code e selecione Open with Codespaces.

Se você ainda não tem um Codespace, pode criar um clicando em New codespace.

**Nota** Instalando o ambiente Node no seu codespace
Executar um demo npm a partir de um GitHub Codespace é uma ótima forma de testar e desenvolver seu projeto. Aqui está um guia passo a passo para começar:

### Configure seu ambiente:
Com seu Codespace aberto, certifique-se de que Node.js e npm estão instalados. Você pode verificar executando:
```
node -v
```
```
npm -v
```

Se não estiverem instalados, você pode instalá-los usando:
```
sudo apt-get update
```
```
sudo apt-get install nodejs npm
```

### Navegue até o diretório do seu projeto:
Use o terminal para navegar até o diretório onde seu projeto npm está localizado:
```
cd path/to/your/project
```

### Instale as dependências:
Execute o seguinte comando para instalar todas as dependências necessárias listadas no seu arquivo package.json:

```
npm install
```

### Execute o demo:
Depois que as dependências estiverem instaladas, você pode executar seu script de demo. Normalmente, ele está especificado na seção scripts do seu package.json. Por exemplo, se o script de demo se chama start, você pode executar:

```
npm run build
```
```
npm run dev
```

### Acesse o demo:
Se seu demo envolver um servidor web, os Codespaces fornecerão uma URL para acessá-lo. Procure por uma notificação ou verifique a aba Ports para encontrar a URL.

**Nota:** O modelo precisa estar em cache no navegador, então pode levar algum tempo para carregar.

### Demonstração RAG
Faça upload do arquivo markdown `intro_rag.md` to complete the RAG solution. If using codespaces you can download the file located in `01.InferencePhi3/docs/`

### Selecione seu arquivo:
Clique no botão “Choose File” para escolher o documento que deseja enviar.

### Faça o upload do documento:
Após selecionar seu arquivo, clique no botão “Upload” para carregar seu documento para o RAG (Geração Aumentada por Recuperação).

### Inicie seu chat:
Depois que o documento for carregado, você pode iniciar uma sessão de chat usando RAG baseada no conteúdo do seu documento.

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.