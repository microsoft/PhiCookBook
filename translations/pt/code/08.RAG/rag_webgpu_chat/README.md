<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4aac6b8a5dcbbe9a32b47be30340cac2",
  "translation_date": "2025-07-16T17:16:20+00:00",
  "source_file": "code/08.RAG/rag_webgpu_chat/README.md",
  "language_code": "pt"
}
-->
Phi-3-mini WebGPU RAG Chatbot

## Demonstração para apresentar WebGPU e o Padrão RAG
O Padrão RAG com o modelo Phi-3 Onnx Hospedado utiliza a abordagem de Geração Aumentada por Recuperação, combinando o poder dos modelos Phi-3 com o alojamento ONNX para implementações de IA eficientes. Este padrão é fundamental para o ajuste fino de modelos para tarefas específicas de domínio, oferecendo uma combinação de qualidade, custo-benefício e compreensão de contexto longo. Faz parte do conjunto Azure AI, que disponibiliza uma vasta seleção de modelos fáceis de encontrar, experimentar e usar, respondendo às necessidades de personalização de várias indústrias. Os modelos Phi-3, incluindo Phi-3-mini, Phi-3-small e Phi-3-medium, estão disponíveis no Catálogo de Modelos Azure AI e podem ser ajustados e implementados de forma autónoma ou através de plataformas como HuggingFace e ONNX, demonstrando o compromisso da Microsoft com soluções de IA acessíveis e eficientes.

## O que é WebGPU
WebGPU é uma API moderna de gráficos web concebida para fornecer acesso eficiente à unidade de processamento gráfico (GPU) de um dispositivo diretamente a partir dos navegadores web. Destina-se a ser o sucessor do WebGL, oferecendo várias melhorias importantes:

1. **Compatibilidade com GPUs Modernas**: O WebGPU foi criado para funcionar perfeitamente com arquiteturas de GPU contemporâneas, aproveitando APIs do sistema como Vulkan, Metal e Direct3D 12.
2. **Desempenho Aprimorado**: Suporta computações gerais na GPU e operações mais rápidas, tornando-o adequado tanto para renderização gráfica como para tarefas de aprendizagem automática.
3. **Funcionalidades Avançadas**: O WebGPU permite acesso a capacidades mais avançadas da GPU, possibilitando cargas de trabalho gráficas e computacionais mais complexas e dinâmicas.
4. **Redução da Carga no JavaScript**: Ao transferir mais tarefas para a GPU, o WebGPU reduz significativamente a carga no JavaScript, resultando em melhor desempenho e experiências mais fluidas.

Atualmente, o WebGPU é suportado em navegadores como o Google Chrome, com trabalhos em curso para expandir o suporte a outras plataformas.

### 03.WebGPU
Ambiente Requerido:

**Navegadores suportados:**  
- Google Chrome 113+  
- Microsoft Edge 113+  
- Safari 18 (macOS 15)  
- Firefox Nightly.

### Ativar WebGPU:

- No Chrome/Microsoft Edge

Ative a flag `chrome://flags/#enable-unsafe-webgpu`.

#### Abra o Seu Navegador:
Inicie o Google Chrome ou Microsoft Edge.

#### Aceda à Página de Flags:
Na barra de endereços, escreva `chrome://flags` e pressione Enter.

#### Procure a Flag:
Na caixa de pesquisa no topo da página, escreva 'enable-unsafe-webgpu'

#### Ative a Flag:
Encontre a flag #enable-unsafe-webgpu na lista de resultados.

Clique no menu suspenso ao lado e selecione Ativado.

#### Reinicie o Seu Navegador:

Após ativar a flag, será necessário reiniciar o navegador para que as alterações tenham efeito. Clique no botão Reiniciar que aparece na parte inferior da página.

- No Linux, inicie o navegador com `--enable-features=Vulkan`.
- O Safari 18 (macOS 15) tem o WebGPU ativado por defeito.
- No Firefox Nightly, escreva about:config na barra de endereços e defina `dom.webgpu.enabled` para true.

### Configurar GPU para Microsoft Edge

Aqui estão os passos para configurar uma GPU de alto desempenho para o Microsoft Edge no Windows:

- **Abra as Definições:** Clique no menu Iniciar e selecione Definições.
- **Definições do Sistema:** Vá a Sistema e depois a Ecrã.
- **Definições de Gráficos:** Desça até ao fim e clique em Definições de gráficos.
- **Escolha a App:** Em “Escolha uma aplicação para definir preferência,” selecione Aplicação de ambiente de trabalho e depois Procurar.
- **Selecione o Edge:** Navegue até à pasta de instalação do Edge (normalmente `C:\Program Files (x86)\Microsoft\Edge\Application`) e selecione `msedge.exe`.
- **Defina a Preferência:** Clique em Opções, escolha Alto desempenho e depois clique em Guardar.  
Isto garantirá que o Microsoft Edge utiliza a sua GPU de alto desempenho para melhor desempenho.  
- **Reinicie** o seu computador para que estas definições tenham efeito.

### Abra o Seu Codespace:
Navegue até ao seu repositório no GitHub.  
Clique no botão Code e selecione Abrir com Codespaces.

Se ainda não tiver um Codespace, pode criar um clicando em Novo codespace.

**Nota** Instalar o Ambiente Node no seu codespace  
Executar uma demo npm a partir de um GitHub Codespace é uma ótima forma de testar e desenvolver o seu projeto. Aqui está um guia passo a passo para o ajudar a começar:

### Configure o Seu Ambiente:
Assim que o seu Codespace estiver aberto, certifique-se de que tem o Node.js e o npm instalados. Pode verificar isto executando:  
```
node -v
```  
```
npm -v
```

Se não estiverem instalados, pode instalá-los usando:  
```
sudo apt-get update
```  
```
sudo apt-get install nodejs npm
```

### Navegue até ao Diretório do Seu Projeto:
Use o terminal para navegar até ao diretório onde o seu projeto npm está localizado:  
```
cd path/to/your/project
```

### Instale as Dependências:
Execute o seguinte comando para instalar todas as dependências necessárias listadas no seu ficheiro package.json:  

```
npm install
```

### Execute a Demo:
Depois de instaladas as dependências, pode executar o seu script de demonstração. Normalmente, este está especificado na secção scripts do seu package.json. Por exemplo, se o seu script de demo se chamar start, pode executar:  

```
npm run build
```  
```
npm run dev
```

### Aceda à Demo:
Se a sua demo envolver um servidor web, os Codespaces fornecerão uma URL para aceder a ela. Procure uma notificação ou verifique o separador Ports para encontrar a URL.

**Nota:** O modelo precisa de ser armazenado em cache no navegador, por isso pode demorar algum tempo a carregar.

### Demonstração RAG
Carregue o ficheiro markdown `intro_rag.md` para completar a solução RAG. Se estiver a usar codespaces, pode descarregar o ficheiro localizado em `01.InferencePhi3/docs/`

### Selecione o Seu Ficheiro:
Clique no botão que diz “Choose File” para escolher o documento que pretende carregar.

### Carregue o Documento:
Depois de selecionar o seu ficheiro, clique no botão “Upload” para carregar o seu documento para RAG (Geração Aumentada por Recuperação).

### Inicie a Sua Conversa:
Assim que o documento estiver carregado, pode iniciar uma sessão de chat usando RAG com base no conteúdo do seu documento.

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações erradas decorrentes da utilização desta tradução.