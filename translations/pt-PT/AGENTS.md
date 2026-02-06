# AGENTS.md

## Visão Geral do Projeto

PhiCookBook é um repositório abrangente de receitas contendo exemplos práticos, tutoriais e documentação para trabalhar com a família Phi de Modelos de Linguagem Pequenos (SLMs) da Microsoft. O repositório demonstra vários casos de uso, incluindo inferência, ajuste fino, quantização, implementações RAG e aplicações multimodais em diferentes plataformas e frameworks.

**Principais Tecnologias:**
- **Linguagens:** Python, C#/.NET, JavaScript/Node.js
- **Frameworks:** ONNX Runtime, PyTorch, Transformers, MLX, OpenVINO, Semantic Kernel
- **Plataformas:** Azure AI Foundry, GitHub Models, Hugging Face, Ollama
- **Tipos de Modelos:** Phi-3, Phi-3.5, Phi-4 (texto, visão, multimodal, variantes de raciocínio)

**Estrutura do Repositório:**
- `/code/` - Exemplos de código prático e implementações de amostra
- `/md/` - Documentação detalhada, tutoriais e guias práticos  
- `/translations/` - Traduções multilíngues (50+ idiomas via fluxo de trabalho automatizado)
- `/.devcontainer/` - Configuração de contêiner de desenvolvimento (Python 3.12 com Ollama)

## Configuração do Ambiente de Desenvolvimento

### Usando GitHub Codespaces ou Contêineres de Desenvolvimento (Recomendado)

1. Abrir no GitHub Codespaces (mais rápido):
   - Clique no emblema "Open in GitHub Codespaces" no README
   - O contêiner é configurado automaticamente com Python 3.12 e Ollama com Phi-3

2. Abrir no VS Code Dev Containers:
   - Use o emblema "Open in Dev Containers" no README
   - O contêiner requer no mínimo 16GB de memória no host

### Configuração Local

**Pré-requisitos:**
- Python 3.12 ou superior
- .NET 8.0 SDK (para exemplos em C#)
- Node.js 18+ e npm (para exemplos em JavaScript)
- Recomendado no mínimo 16GB de RAM

**Instalação:**
```bash
git clone https://github.com/microsoft/PhiCookBook.git
cd PhiCookBook
```

**Para Exemplos em Python:**
Navegue até os diretórios de exemplo específicos e instale as dependências:
```bash
cd code/<example-directory>
pip install -r requirements.txt  # if requirements.txt exists
```

**Para Exemplos em .NET:**
```bash
cd md/04.HOL/dotnet/src
dotnet restore LabsPhi.sln
dotnet build LabsPhi.sln
```

**Para Exemplos em JavaScript/Web:**
```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Start development server
npm run build  # Build for production
```

## Organização do Repositório

### Exemplos de Código (`/code/`)

- **01.Introduce/** - Introduções básicas e exemplos iniciais
- **03.Finetuning/** e **04.Finetuning/** - Exemplos de ajuste fino com vários métodos
- **03.Inference/** - Exemplos de inferência em diferentes hardwares (AIPC, MLX)
- **06.E2E/** - Exemplos de aplicações de ponta a ponta
- **07.Lab/** - Implementações laboratoriais/experimentais
- **08.RAG/** - Exemplos de Geração com Recuperação de Dados
- **09.UpdateSamples/** - Exemplos atualizados mais recentes

### Documentação (`/md/`)

- **01.Introduction/** - Guias introdutórios, configuração de ambiente, guias de plataforma
- **02.Application/** - Exemplos de aplicação organizados por tipo (Texto, Código, Visão, Áudio, etc.)
- **02.QuickStart/** - Guias de início rápido para Azure AI Foundry e GitHub Models
- **03.FineTuning/** - Documentação e tutoriais de ajuste fino
- **04.HOL/** - Laboratórios práticos (inclui exemplos em .NET)

### Formatos de Arquivo

- **Jupyter Notebooks (`.ipynb`)** - Tutoriais interativos em Python marcados com 📓 no README
- **Scripts Python (`.py`)** - Exemplos independentes em Python
- **Projetos C# (`.csproj`, `.sln`)** - Aplicações e exemplos em .NET
- **JavaScript (`.js`, `package.json`)** - Exemplos baseados na web e Node.js
- **Markdown (`.md`)** - Documentação e guias

## Trabalhando com Exemplos

### Executando Jupyter Notebooks

A maioria dos exemplos é fornecida como notebooks Jupyter:
```bash
pip install jupyter notebook
jupyter notebook  # Opens browser interface
# Navigate to desired .ipynb file
```

### Executando Scripts Python

```bash
cd code/<example-directory>
pip install -r requirements.txt
python <script-name>.py
```

### Executando Exemplos em .NET

```bash
cd md/04.HOL/dotnet/src/<project-name>
dotnet run
```

Ou construa a solução inteira:
```bash
cd md/04.HOL/dotnet/src
dotnet run --project <project-name>
```

### Executando Exemplos em JavaScript/Web

```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Development with hot reload
```

## Testes

Este repositório contém código de exemplo e tutoriais, em vez de um projeto de software tradicional com testes unitários. A validação geralmente é feita por:

1. **Executar os exemplos** - Cada exemplo deve ser executado sem erros
2. **Verificar os resultados** - Certifique-se de que as respostas do modelo são apropriadas
3. **Seguir os tutoriais** - Os guias passo a passo devem funcionar conforme documentado

**Abordagem comum de validação:**
- Testar a execução dos exemplos no ambiente alvo
- Verificar se as dependências são instaladas corretamente
- Confirmar que os modelos são baixados/carregados com sucesso
- Garantir que o comportamento esperado corresponde à documentação

## Estilo de Código e Convenções

### Diretrizes Gerais

- Os exemplos devem ser claros, bem comentados e educativos
- Seguir convenções específicas da linguagem (PEP 8 para Python, padrões C# para .NET)
- Manter os exemplos focados em demonstrar capacidades específicas dos modelos Phi
- Incluir comentários explicando conceitos-chave e parâmetros específicos do modelo

### Padrões de Documentação

**Formatação de URLs:**
- Use o formato `[texto](../../url)` sem espaços extras
- Links relativos: Use `./` para o diretório atual, `../` para o pai
- Não use locais específicos de países em URLs (evite `/en-us/`, `/en/`)

**Imagens:**
- Armazene todas as imagens no diretório `/imgs/`
- Use nomes descritivos com caracteres em inglês, números e traços
- Exemplo: `phi-3-architecture.png`

**Arquivos Markdown:**
- Referencie exemplos reais de trabalho no diretório `/code/`
- Mantenha a documentação sincronizada com as alterações no código
- Use o emoji 📓 para marcar links de notebooks Jupyter no README

### Organização de Arquivos

- Exemplos de código em `/code/` organizados por tópico/funcionalidade
- Documentação em `/md/` espelha a estrutura do código quando aplicável
- Mantenha arquivos relacionados (notebooks, scripts, configurações) juntos em subdiretórios

## Diretrizes para Pull Requests

### Antes de Submeter

1. **Faça um fork do repositório** para sua conta
2. **Separe PRs por tipo:**
   - Correções de bugs em um PR
   - Atualizações de documentação em outro
   - Novos exemplos em PRs separados
   - Correções de erros de digitação podem ser combinadas

3. **Lidar com conflitos de mesclagem:**
   - Atualize sua branch `main` local antes de fazer alterações
   - Sincronize com o upstream frequentemente

4. **PRs de Tradução:**
   - Devem incluir traduções para TODOS os arquivos na pasta
   - Mantenha a estrutura consistente com o idioma original

### Verificações Necessárias

Os PRs executam automaticamente fluxos de trabalho do GitHub para validar:

1. **Validação de caminho relativo** - Todos os links internos devem funcionar
   - Teste os links localmente: Ctrl+Click no VS Code
   - Use sugestões de caminho do VS Code (`./` ou `../`)

2. **Verificação de local de URL** - URLs da web não devem conter locais de países
   - Remova `/en-us/`, `/en/` ou outros códigos de idioma
   - Use URLs internacionais genéricas

3. **Verificação de URL quebrada** - Todas as URLs devem retornar status 200
   - Verifique se os links são acessíveis antes de enviar
   - Nota: Algumas falhas podem ser devido a restrições de rede

### Formato do Título do PR

```
[component] Brief description
```

Exemplos:
- `[docs] Adicionar tutorial de inferência Phi-4`
- `[code] Corrigir exemplo de integração ONNX Runtime`
- `[translation] Adicionar tradução para japonês dos guias introdutórios`

## Padrões Comuns de Desenvolvimento

### Trabalhando com Modelos Phi

**Carregamento de Modelos:**
- Os exemplos usam vários frameworks: Transformers, ONNX Runtime, MLX, OpenVINO
- Os modelos geralmente são baixados do Hugging Face, Azure ou GitHub Models
- Verifique a compatibilidade do modelo com seu hardware (CPU, GPU, NPU)

**Padrões de Inferência:**
- Geração de texto: A maioria dos exemplos usa variantes de chat/instrução
- Visão: Phi-3-vision e Phi-4-multimodal para compreensão de imagens
- Áudio: Phi-4-multimodal suporta entradas de áudio
- Raciocínio: Variantes Phi-4-reasoning para tarefas avançadas de raciocínio

### Notas Específicas da Plataforma

**Azure AI Foundry:**
- Requer assinatura Azure e chaves de API
- Veja `/md/02.QuickStart/AzureAIFoundry_QuickStart.md`

**GitHub Models:**
- Nível gratuito disponível para testes
- Veja `/md/02.QuickStart/GitHubModel_QuickStart.md`

**Inferência Local:**
- ONNX Runtime: Inferência otimizada e multiplataforma
- Ollama: Gerenciamento fácil de modelos locais (pré-configurado no contêiner de desenvolvimento)
- Apple MLX: Otimizado para Apple Silicon

## Solução de Problemas

### Problemas Comuns

**Problemas de Memória:**
- Os modelos Phi exigem muita RAM (especialmente variantes de visão/multimodal)
- Use modelos quantizados para ambientes com recursos limitados
- Veja `/md/01.Introduction/04/QuantifyingPhi.md`

**Conflitos de Dependência:**
- Exemplos em Python podem ter requisitos específicos de versão
- Use ambientes virtuais para cada exemplo
- Verifique os arquivos `requirements.txt` individuais

**Falhas no Download de Modelos:**
- Modelos grandes podem expirar em conexões lentas
- Considere usar ambientes na nuvem (Codespaces, Azure)
- Verifique o cache do Hugging Face: `~/.cache/huggingface/`

**Problemas em Projetos .NET:**
- Certifique-se de que o SDK .NET 8.0 está instalado
- Use `dotnet restore` antes de construir
- Alguns projetos têm configurações específicas para CUDA (Debug_Cuda)

**Exemplos em JavaScript/Web:**
- Use Node.js 18+ para compatibilidade
- Limpe `node_modules` e reinstale se houver problemas
- Verifique o console do navegador para problemas de compatibilidade com WebGPU

### Obtendo Ajuda

- **Discord:** Participe da Comunidade Azure AI Foundry no Discord
- **GitHub Issues:** Relate bugs e problemas no repositório
- **GitHub Discussions:** Faça perguntas e compartilhe conhecimento

## Contexto Adicional

### IA Responsável

Todo uso de modelos Phi deve seguir os princípios de IA Responsável da Microsoft:
- Justiça, confiabilidade, segurança
- Privacidade e segurança  
- Inclusividade, transparência, responsabilidade
- Use Azure AI Content Safety para aplicações em produção
- Veja `/md/01.Introduction/01/01.AISafety.md`

### Traduções

- Suporte para mais de 50 idiomas via GitHub Action automatizado
- Traduções no diretório `/translations/`
- Mantido pelo fluxo de trabalho co-op-translator
- Não edite manualmente arquivos traduzidos (gerados automaticamente)

### Contribuindo

- Siga as diretrizes em `CONTRIBUTING.md`
- Concorde com o Acordo de Licença de Contribuidor (CLA)
- Adira ao Código de Conduta de Código Aberto da Microsoft
- Mantenha segurança e credenciais fora dos commits

### Suporte Multilíngue

Este é um repositório poliglota com exemplos em:
- **Python** - Fluxos de trabalho de ML/IA, notebooks Jupyter, ajuste fino
- **C#/.NET** - Aplicações empresariais, integração ONNX Runtime
- **JavaScript** - IA baseada na web, inferência no navegador com WebGPU

Escolha a linguagem que melhor se adapta ao seu caso de uso e alvo de implantação.

---

**Aviso**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se uma tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.