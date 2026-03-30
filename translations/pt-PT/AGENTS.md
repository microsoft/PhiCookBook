# AGENTS.md

## Visão Geral do Projeto

O PhiCookBook é um repositório abrangente de cookbooks que contém exemplos práticos, tutoriais e documentação para trabalhar com a família Phi de Modelos Pequenos de Linguagem (SLMs) da Microsoft. O repositório demonstra vários casos de uso, incluindo inferência, fine-tuning, quantização, implementações RAG e aplicações multimodais em diferentes plataformas e frameworks.

**Tecnologias Principais:**
- **Linguagens:** Python, C#/.NET, JavaScript/Node.js
- **Frameworks:** ONNX Runtime, PyTorch, Transformers, MLX, OpenVINO, Semantic Kernel
- **Plataformas:** Microsoft Foundry, GitHub Models, Hugging Face, Ollama
- **Tipos de Modelo:** Phi-3, Phi-3.5, Phi-4 (variantes de texto, visão, multimodal, raciocínio)

**Estrutura do Repositório:**
- `/code/` - Exemplos de código funcional e implementações de amostra
- `/md/` - Documentação detalhada, tutoriais e guias práticos  
- `/translations/` - Traduções multilíngues (mais de 50 idiomas via workflow automatizado)
- `/.devcontainer/` - Configuração do ambiente de desenvolvimento (Python 3.12 com Ollama)

## Configuração do Ambiente de Desenvolvimento

### Utilizando GitHub Codespaces ou Contêineres de Desenvolvimento (Recomendado)

1. Abrir no GitHub Codespaces (mais rápido):
   - Clique no badge "Open in GitHub Codespaces" no README
   - O contêiner configura automaticamente com Python 3.12 e Ollama com Phi-3

2. Abrir no VS Code Dev Containers:
   - Use o badge "Open in Dev Containers" do README
   - O contêiner requer pelo menos 16GB de memória do host

### Configuração Local

**Pré-requisitos:**
- Python 3.12 ou superior
- .NET 8.0 SDK (para exemplos em C#)
- Node.js 18+ e npm (para exemplos em JavaScript)
- 16GB de RAM recomendados no mínimo

**Instalação:**
```bash
git clone https://github.com/microsoft/PhiCookBook.git
cd PhiCookBook
```

**Para Exemplos em Python:**
Navegue até os diretórios específicos dos exemplos e instale as dependências:
```bash
cd code/<example-directory>
pip install -r requirements.txt  # se o ficheiro requirements.txt existir
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
npm run dev  # Iniciar servidor de desenvolvimento
npm run build  # Construir para produção
```

## Organização do Repositório

### Exemplos de Código (`/code/`)

- **01.Introduce/** - Introduções básicas e amostras de primeiros passos
- **03.Finetuning/** e **04.Finetuning/** - Exemplos de fine-tuning com vários métodos
- **03.Inference/** - Exemplos de inferência em diferentes hardwares (AIPC, MLX)
- **06.E2E/** - Exemplos de aplicações end-to-end
- **07.Lab/** - Implementações laboratoriais/experimentais
- **08.RAG/** - Exemplos de Recuperação-Augmentada de Geração (RAG)
- **09.UpdateSamples/** - Amostras mais recentes atualizadas

### Documentação (`/md/`)

- **01.Introduction/** - Guias introdutórios, configuração do ambiente, guias de plataforma
- **02.Application/** - Exemplos de aplicações organizados por tipo (Texto, Código, Visão, Áudio, etc.)
- **02.QuickStart/** - Guias rápidos para Microsoft Foundry e GitHub Models
- **03.FineTuning/** - Documentação e tutoriais de fine-tuning
- **04.HOL/** - Laboratórios práticos (inclui exemplos .NET)

### Formatos de Ficheiro

- **Jupyter Notebooks (`.ipynb`)** - Tutoriais interativos em Python marcados com 📓 no README
- **Scripts Python (`.py`)** - Exemplos independentes em Python
- **Projetos C# (`.csproj`, `.sln`)** - Aplicações e exemplos .NET
- **JavaScript (`.js`, `package.json`)** - Exemplos web e Node.js
- **Markdown (`.md`)** - Documentação e guias

## Trabalho com Exemplos

### Executar Jupyter Notebooks

A maioria dos exemplos é fornecida como Jupyter notebooks:
```bash
pip install jupyter notebook
jupyter notebook  # Abre a interface do navegador
# Navegue até ao ficheiro .ipynb desejado
```

### Executar Scripts Python

```bash
cd code/<example-directory>
pip install -r requirements.txt
python <script-name>.py
```

### Executar Exemplos .NET

```bash
cd md/04.HOL/dotnet/src/<project-name>
dotnet run
```

Ou construir a solução completa:
```bash
cd md/04.HOL/dotnet/src
dotnet run --project <project-name>
```

### Executar Exemplos JavaScript/Web

```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Desenvolvimento com recarregamento a quente
```

## Testes

Este repositório contém código de exemplo e tutoriais em vez de um projeto de software tradicional com testes unitários. A validação é normalmente feita por:

1. **Executar os exemplos** - Cada exemplo deve correr sem erros
2. **Verificar as saídas** - Confirmar que as respostas do modelo são apropriadas
3. **Seguir os tutoriais** - Os guias passo a passo devem funcionar conforme documentado

**Abordagem comum de validação:**
- Testar a execução dos exemplos no ambiente alvo
- Verificar se as dependências são instaladas corretamente
- Confirmar que os modelos são descarregados/carregados com sucesso
- Confirmar que o comportamento esperado corresponde à documentação

## Estilo de Código e Convenções

### Diretrizes Gerais

- Os exemplos devem ser claros, bem comentados e educativos
- Seguir convenções específicas da linguagem (PEP 8 para Python, standards C# para .NET)
- Manter os exemplos focados em demonstrar capacidades específicas dos modelos Phi
- Incluir comentários que expliquem conceitos-chave e parâmetros específicos dos modelos

### Padrões de Documentação

**Formatação de URLs:**
- Usar o formato `[text](../../url)` sem espaços adicionais
- Links relativos: usar `./` para diretório atual, `../` para diretório pai
- Evitar locais específicos de país em URLs (não usar `/en-us/`, `/en/`)

**Imagens:**
- Guardar todas as imagens na diretoria `/imgs/`
- Usar nomes descritivos com caracteres latinos, números e traços
- Exemplo: `phi-3-architecture.png`

**Ficheiros Markdown:**
- Referenciar exemplos funcionais reais no diretório `/code/`
- Manter documentação sincronizada com as alterações do código
- Usar o emoji 📓 para marcar links de Jupyter notebook no README

### Organização de Ficheiros

- Exemplos de código em `/code/` organizados por tópico/funcionalidade
- Documentação em `/md/` espelha a estrutura do código quando aplicável
- Manter ficheiros relacionados (notebooks, scripts, configs) juntos em subdiretórios

## Diretrizes para Pull Requests

### Antes de Submeter

1. **Fazer fork do repositório** para sua conta
2. **Separar PRs por tipo:**
   - Correções de bugs num PR
   - Atualizações de documentação noutra
   - Novos exemplos em PRs separados
   - Correções de erros tipográficos podem ser combinadas

3. **Gerir conflitos de merge:**
   - Atualizar a branch `main` local antes de fazer alterações
   - Sincronizar frequentemente com o upstream

4. **PRs de tradução:**
   - Devem incluir traduções para TODOS os ficheiros na pasta
   - Manter a estrutura consistente com o idioma original

### Verificações Obrigatórias

Os PRs executam automaticamente workflows do GitHub para validar:

1. **Validação de caminhos relativos** - Todos os links internos devem funcionar
   - Testar links localmente: Ctrl+Click no VS Code
   - Usar sugestões de caminho do VS Code (`./` ou `../`)

2. **Verificação de língua em URL** - URLs web não devem conter locais de país
   - Remover `/en-us/`, `/en/` ou outros códigos de idioma
   - Usar URLs internacionais genéricos

3. **Verificação de URLs inválidas** - Todas as URLs devem retornar status 200
   - Confirmar que os links são acessíveis antes da submissão
   - Nota: Algumas falhas podem dever-se a restrições de rede

### Formato do Título do PR

```
[component] Brief description
```

Exemplos:
- `[docs] Adicionar tutorial de inferência Phi-4`
- `[code] Corrigir exemplo de integração ONNX Runtime`
- `[translation] Adicionar tradução japonesa para guias introdutórios`

## Padrões Comuns de Desenvolvimento

### Trabalhar com Modelos Phi

**Carregamento de Modelo:**
- Exemplos usam vários frameworks: Transformers, ONNX Runtime, MLX, OpenVINO
- Modelos são normalmente descarregados do Hugging Face, Azure ou GitHub Models
- Verificar compatibilidade do modelo com o hardware (CPU, GPU, NPU)

**Padrões de Inferência:**
- Geração de texto: A maioria dos exemplos usa variantes chat/instruct
- Visão: Phi-3-vision e Phi-4-multimodal para compreensão de imagens
- Áudio: Phi-4-multimodal suporta entradas áudio
- Raciocínio: Variantes Phi-4-reasoning para tarefas avançadas de raciocínio

### Notas Específicas da Plataforma

**Microsoft Foundry:**
- Requer subscrição Azure e chaves API
- Ver `/md/02.QuickStart/AzureAIFoundry_QuickStart.md`

**GitHub Models:**
- Plano gratuito disponível para testes
- Ver `/md/02.QuickStart/GitHubModel_QuickStart.md`

**Inferência Local:**
- ONNX Runtime: Multiplataforma, inferência otimizada
- Ollama: Gestão fácil de modelos locais (pré-configurado no contêiner)
- Apple MLX: Otimizado para Apple Silicon

## Resolução de Problemas

### Problemas Comuns

**Problemas de Memória:**
- Modelos Phi requerem muita RAM (especialmente variantes visão/multimodal)
- Use modelos quantizados para ambientes com recursos limitados
- Ver `/md/01.Introduction/04/QuantifyingPhi.md`

**Conflitos de Dependências:**
- Exemplos Python podem ter requisitos específicos de versões
- Usar ambientes virtuais para cada exemplo
- Ver ficheiros individuais `requirements.txt`

**Falhas de Download de Modelo:**
- Modelos grandes podem falhar por timeout em conexões lentas
- Considere usar ambientes na nuvem (Codespaces, Azure)
- Ver cache Hugging Face: `~/.cache/huggingface/`

**Problemas em Projetos .NET:**
- Garantir instalação do .NET 8.0 SDK
- Usar `dotnet restore` antes de construir
- Alguns projetos têm configurações específicas para CUDA (Debug_Cuda)

**Exemplos JavaScript/Web:**
- Usar Node.js 18+ para compatibilidade
- Limpar `node_modules` e reinstalar se houver problemas
- Ver consola do navegador para problemas de compatibilidade WebGPU

### Obter Ajuda

- **Discord:** Junte-se ao Microsoft Foundry Community Discord
- **GitHub Issues:** Reportar bugs e problemas no repositório
- **GitHub Discussions:** Perguntar e partilhar conhecimento

## Contexto Adicional

### IA Responsável

Todo uso dos modelos Phi deve seguir os princípios de IA Responsável da Microsoft:
- Justiça, fiabilidade, segurança
- Privacidade e segurança  
- Inclusividade, transparência, responsabilidade
- Usar Azure AI Content Safety para aplicações em produção
- Ver `/md/01.Introduction/01/01.AISafety.md`

### Traduções

- Suporte a mais de 50 idiomas via GitHub Action automatizada
- Traduções em `/translations/`
- Mantidas pelo workflow co-op-translator
- Não editar manualmente ficheiros traduzidos (gerados automaticamente)

### Contribuição

- Seguir diretrizes em `CONTRIBUTING.md`
- Aceitar o Acordo de Licença de Contribuinte (CLA)
- Cumprir o Código de Conduta de Código Aberto da Microsoft
- Manter segurança e credenciais fora dos commits

### Suporte Multilíngue

Este é um repositório poliglota com exemplos em:
- **Python** - Workflows ML/IA, Jupyter notebooks, fine-tuning
- **C#/.NET** - Aplicações empresariais, integração ONNX Runtime
- **JavaScript** - IA web, inferência no browser com WebGPU

Escolha a linguagem que melhor se adequa ao seu caso de uso e alvo de implementação.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações erradas decorrentes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->