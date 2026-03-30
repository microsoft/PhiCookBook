# AGENTS.md

## Visão Geral do Projeto

PhiCookBook é um repositório abrangente de receitas contendo exemplos práticos, tutoriais e documentação para trabalhar com a família Phi de Pequenos Modelos de Linguagem (SLMs) da Microsoft. O repositório demonstra vários casos de uso, incluindo inferência, fine-tuning, quantização, implementações RAG e aplicações multimodais em diferentes plataformas e frameworks.

**Principais Tecnologias:**
- **Linguagens:** Python, C#/.NET, JavaScript/Node.js
- **Frameworks:** ONNX Runtime, PyTorch, Transformers, MLX, OpenVINO, Semantic Kernel
- **Plataformas:** Microsoft Foundry, GitHub Models, Hugging Face, Ollama
- **Tipos de Modelos:** Phi-3, Phi-3.5, Phi-4 (variantes texto, visão, multimodal, raciocínio)

**Estrutura do Repositório:**
- `/code/` - Exemplos de código práticos e implementações de amostra
- `/md/` - Documentação detalhada, tutoriais e guias passo a passo  
- `/translations/` - Traduções multilíngues (50+ idiomas via fluxo automatizado)
- `/.devcontainer/` - Configuração do container de desenvolvimento (Python 3.12 com Ollama)

## Configuração do Ambiente de Desenvolvimento

### Usando GitHub Codespaces ou Dev Containers (Recomendado)

1. Abrir no GitHub Codespaces (mais rápido):
   - Clique no badge "Open in GitHub Codespaces" no README
   - O container é auto-configurado com Python 3.12 e Ollama com Phi-3

2. Abrir no VS Code Dev Containers:
   - Use o badge "Open in Dev Containers" do README
   - O container requer no mínimo 16GB de memória no host

### Configuração Local

**Pré-requisitos:**
- Python 3.12 ou superior
- SDK .NET 8.0 (para exemplos em C#)
- Node.js 18+ e npm (para exemplos em JavaScript)
- Recomenda-se mínimo de 16GB de RAM

**Instalação:**
```bash
git clone https://github.com/microsoft/PhiCookBook.git
cd PhiCookBook
```

**Para Exemplos Python:**
Navegue para os diretórios dos exemplos específicos e instale as dependências:
```bash
cd code/<example-directory>
pip install -r requirements.txt  # se o requirements.txt existir
```

**Para Exemplos .NET:**
```bash
cd md/04.HOL/dotnet/src
dotnet restore LabsPhi.sln
dotnet build LabsPhi.sln
```

**Para Exemplos JavaScript/Web:**
```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Iniciar servidor de desenvolvimento
npm run build  # Compilar para produção
```

## Organização do Repositório

### Exemplos de Código (`/code/`)

- **01.Introduce/** - Introduções básicas e amostras iniciais
- **03.Finetuning/** e **04.Finetuning/** - Exemplos de fine-tuning com vários métodos
- **03.Inference/** - Exemplos de inferência em diferentes hardwares (AIPC, MLX)
- **06.E2E/** - Exemplos de aplicações ponta a ponta
- **07.Lab/** - Implementações laboratoriais/experimentais
- **08.RAG/** - Amostras de Geração Aprimorada por Recuperação
- **09.UpdateSamples/** - Amostras atualizadas recentemente

### Documentação (`/md/`)

- **01.Introduction/** - Guias de introdução, configuração de ambiente, guias de plataforma
- **02.Application/** - Amostras de aplicações organizadas por tipo (Texto, Código, Visão, Áudio, etc.)
- **02.QuickStart/** - Guias rápidos para Microsoft Foundry e GitHub Models
- **03.FineTuning/** - Documentação e tutoriais de fine-tuning
- **04.HOL/** - Laboratórios práticos (inclui exemplos em .NET)

### Formatos de Arquivo

- **Jupyter Notebooks (`.ipynb`)** - Tutoriais interativos em Python marcados com 📓 no README
- **Scripts Python (`.py`)** - Exemplos Python independentes
- **Projetos C# (`.csproj`, `.sln`)** - Aplicações e amostras .NET
- **JavaScript (`.js`, `package.json`)** - Exemplos para Web e Node.js
- **Markdown (`.md`)** - Documentação e guias

## Trabalhando com Exemplos

### Executando Jupyter Notebooks

A maioria dos exemplos é fornecida como notebooks Jupyter:
```bash
pip install jupyter notebook
jupyter notebook  # Abre a interface do navegador
# Navegue até o arquivo .ipynb desejado
```

### Executando Scripts Python

```bash
cd code/<example-directory>
pip install -r requirements.txt
python <script-name>.py
```

### Executando Exemplos .NET

```bash
cd md/04.HOL/dotnet/src/<project-name>
dotnet run
```

Ou construa a solução inteira:
```bash
cd md/04.HOL/dotnet/src
dotnet run --project <project-name>
```

### Executando Exemplos JavaScript/Web

```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Desenvolvimento com recarga rápida
```

## Testes

Este repositório contém código de exemplo e tutoriais em vez de um projeto de software tradicional com testes unitários. A validação é normalmente feita por:

1. **Executar os exemplos** - Cada exemplo deve rodar sem erros
2. **Verificar as saídas** - Confirmar que as respostas do modelo são apropriadas
3. **Seguir os tutoriais** - Os guias passo a passo devem funcionar conforme documentado

**Abordagem comum de validação:**
- Testar execução dos exemplos no ambiente alvo
- Verificar instalação correta das dependências
- Confirmar download/carregamento do modelo com sucesso
- Confirmar comportamento esperado conforme documentação

## Estilo e Convenções de Código

### Diretrizes Gerais

- Exemplos devem ser claros, bem comentados e educacionais
- Siga as convenções específicas de cada linguagem (PEP 8 para Python, padrões C# para .NET)
- Mantenha os exemplos focados em demonstrar capacidades específicas dos modelos Phi
- Inclua comentários explicando conceitos chave e parâmetros específicos do modelo

### Padrões de Documentação

**Formatação de URL:**
- Use formato `[texto](../../url)` sem espaços extras
- Links relativos: use `./` para diretório atual, `../` para pai
- Não use locais de idioma específicos em URLs (evite `/en-us/`, `/en/`)

**Imagens:**
- Armazene todas as imagens em `/imgs/`
- Use nomes descritivos com caracteres em inglês, números e traços
- Exemplo: `phi-3-architecture.png`

**Arquivos Markdown:**
- Faça referência a exemplos reais no diretório `/code/`
- Mantenha documentação sincronizada com mudanças no código
- Use emoji 📓 para marcar links de notebooks Jupyter no README

### Organização dos Arquivos

- Exemplos de código em `/code/` organizados por tópico/recurso
- Documentação em `/md/` espelha estrutura do código quando aplicável
- Mantenha arquivos relacionados (notebooks, scripts, configs) juntos nos subdiretórios

## Diretrizes para Pull Requests

### Antes de Enviar

1. **Faça um fork do repositório** para sua conta
2. **Separe PRs por tipo:**
   - Correções de bugs em um PR
   - Atualizações de documentação em outro
   - Novos exemplos em PRs separados
   - Correções de erros ortográficos podem ser combinadas

3. **Resolver conflitos de merge:**
   - Atualize sua branch `main` local antes de fazer mudanças
   - Sincronize com o upstream frequentemente

4. **PRs de tradução:**
   - Devem incluir traduções para TODOS os arquivos na pasta
   - Mantenha estrutura consistente com o idioma original

### Verificações Requeridas

PRs executam automaticamente workflows do GitHub para validar:

1. **Validação de caminhos relativos** - Todos os links internos devem funcionar
   - Teste links localmente: Ctrl+Click no VS Code
   - Use sugestões de caminho do VS Code (`./` ou `../`)

2. **Checagem de localidade em URL** - URLs web não devem conter locais regionais
   - Remova `/en-us/`, `/en/` ou outros códigos de idioma
   - Use URLs internacionais genéricas

3. **Checagem de URLs quebradas** - Todas as URLs devem retornar status 200
   - Verifique links acessíveis antes de enviar
   - Atenção: Alguns erros podem ser devido a restrições de rede

### Formato do Título do PR

```
[component] Brief description
```

Exemplos:
- `[docs] Adicionar tutorial de inferência Phi-4`
- `[code] Corrigir exemplo de integração ONNX Runtime`
- `[translation] Adicionar tradução para japonês nos guias de introdução`

## Padrões Comuns de Desenvolvimento

### Trabalhando com Modelos Phi

**Carregamento de Modelos:**
- Exemplos usam vários frameworks: Transformers, ONNX Runtime, MLX, OpenVINO
- Modelos são normalmente baixados do Hugging Face, Azure ou GitHub Models
- Verifique a compatibilidade do modelo com seu hardware (CPU, GPU, NPU)

**Padrões de Inferência:**
- Geração de texto: A maioria dos exemplos usa variantes de chat/instruct
- Visão: Phi-3-vision e Phi-4-multimodal para entendimento de imagens
- Áudio: Phi-4-multimodal suporta entradas de áudio
- Raciocínio: Variantes Phi-4-reasoning para tarefas avançadas de raciocínio

### Notas Específicas da Plataforma

**Microsoft Foundry:**
- Requer assinatura Azure e chaves de API
- Veja `/md/02.QuickStart/AzureAIFoundry_QuickStart.md`

**GitHub Models:**
- Camada gratuita disponível para testes
- Veja `/md/02.QuickStart/GitHubModel_QuickStart.md`

**Inferência Local:**
- ONNX Runtime: Inferência cross-platform otimizada
- Ollama: Gerenciamento fácil de modelos locais (pré-configurado no container dev)
- Apple MLX: Otimizado para Apple Silicon

## Solução de Problemas

### Problemas Comuns

**Problemas de Memória:**
- Modelos Phi requerem RAM significativa (especialmente variantes visão/multimodal)
- Use modelos quantizados para ambientes com poucos recursos
- Veja `/md/01.Introduction/04/QuantifyingPhi.md`

**Conflitos de Dependência:**
- Exemplos Python podem ter requisitos específicos de versão
- Use ambientes virtuais para cada exemplo
- Verifique arquivos `requirements.txt` individuais

**Falhas no Download de Modelos:**
- Modelos grandes podem expirar em conexões lentas
- Considere usar ambientes em nuvem (Codespaces, Azure)
- Verifique cache do Hugging Face: `~/.cache/huggingface/`

**Problemas em Projetos .NET:**
- Certifique-se de que o SDK .NET 8.0 está instalado
- Use `dotnet restore` antes de compilar
- Alguns projetos têm configurações específicas para CUDA (Debug_Cuda)

**Exemplos JavaScript/Web:**
- Use Node.js 18+ para compatibilidade
- Limpe `node_modules` e reinstale se surgirem problemas
- Verifique console do navegador para problemas de compatibilidade com WebGPU

### Obtenção de Ajuda

- **Discord:** Participe do Discord da Comunidade Microsoft Foundry
- **Issues no GitHub:** Reporte bugs e problemas no repositório
- **Discussões no GitHub:** Faça perguntas e compartilhe conhecimento

## Contexto Adicional

### IA Responsável

Todo uso de modelos Phi deve seguir os princípios de IA Responsável da Microsoft:
- Justiça, confiabilidade, segurança
- Privacidade e segurança  
- Inclusividade, transparência, responsabilidade
- Use Azure AI Content Safety para aplicações em produção
- Veja `/md/01.Introduction/01/01.AISafety.md`

### Traduções

- Suporte para 50+ idiomas via GitHub Action automatizado
- Traduções no diretório `/translations/`
- Mantidas pelo fluxo co-op-translator
- Não edite arquivos traduzidos manualmente (gerados automaticamente)

### Contribuindo

- Siga as diretrizes em `CONTRIBUTING.md`
- Concorde com o Acordo de Licença de Contribuidor (CLA)
- Siga o Código de Conduta de Código Aberto da Microsoft
- Mantenha segurança e credenciais fora dos commits

### Suporte Multilíngue

Este é um repositório poliglota com exemplos em:
- **Python** - Fluxos ML/IA, notebooks Jupyter, fine-tuning
- **C#/.NET** - Aplicações empresariais, integração ONNX Runtime
- **JavaScript** - IA baseada na web, inferência no navegador com WebGPU

Escolha a linguagem que melhor se adequa ao seu caso de uso e alvo de implantação.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos empenhemos pela precisão, por favor, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional feita por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->