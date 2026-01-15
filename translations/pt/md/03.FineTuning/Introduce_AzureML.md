<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7fe541373802e33568e94e13226d463c",
  "translation_date": "2025-07-17T09:40:08+00:00",
  "source_file": "md/03.FineTuning/Introduce_AzureML.md",
  "language_code": "pt"
}
-->
# **Introdução ao Azure Machine Learning Service**

[Azure Machine Learning](https://ml.azure.com?WT.mc_id=aiml-138114-kinfeylo) é um serviço na cloud para acelerar e gerir o ciclo de vida de projetos de machine learning (ML).

Profissionais de ML, cientistas de dados e engenheiros podem usá-lo no seu dia a dia para:

- Treinar e implementar modelos.
- Gerir operações de machine learning (MLOps).
- Pode criar um modelo no Azure Machine Learning ou usar um modelo criado numa plataforma open-source, como PyTorch, TensorFlow ou scikit-learn.
- As ferramentas de MLOps ajudam a monitorizar, re-treinar e reimplementar modelos.

## Para quem é o Azure Machine Learning?

**Cientistas de Dados e Engenheiros de ML**

Podem usar ferramentas para acelerar e automatizar os seus fluxos de trabalho diários.  
O Azure ML oferece funcionalidades para justiça, explicabilidade, rastreio e auditabilidade.

**Desenvolvedores de Aplicações:**  
Podem integrar modelos em aplicações ou serviços de forma simples.

**Desenvolvedores de Plataforma**

Têm acesso a um conjunto robusto de ferramentas suportadas por APIs duráveis do Azure Resource Manager.  
Estas ferramentas permitem construir ferramentas avançadas de ML.

**Empresas**

Ao trabalhar na cloud Microsoft Azure, as empresas beneficiam de segurança familiar e controlo de acesso baseado em funções.  
Podem configurar projetos para controlar o acesso a dados protegidos e operações específicas.

## Produtividade para toda a equipa  
Os projetos de ML frequentemente requerem uma equipa com competências variadas para construir e manter.

O Azure ML oferece ferramentas que permitem:  
- Colaborar com a equipa através de notebooks partilhados, recursos de computação, computação serverless, dados e ambientes.  
- Desenvolver modelos com justiça, explicabilidade, rastreio e auditabilidade para cumprir requisitos de linhagem e conformidade de auditoria.  
- Implementar modelos de ML rápida e facilmente em escala, e gerir e governar eficientemente com MLOps.  
- Executar cargas de trabalho de machine learning em qualquer lugar com governação, segurança e conformidade integradas.

## Ferramentas da plataforma compatíveis entre si

Qualquer membro da equipa de ML pode usar as suas ferramentas preferidas para realizar o trabalho.  
Quer esteja a executar experiências rápidas, ajuste de hiperparâmetros, construir pipelines ou gerir inferências, pode usar interfaces familiares, incluindo:  
- Azure Machine Learning Studio  
- Python SDK (v2)  
- Azure CLI (v2)  
- Azure Resource Manager REST APIs

À medida que refina modelos e colabora durante o ciclo de desenvolvimento, pode partilhar e encontrar ativos, recursos e métricas na interface do Azure Machine Learning studio.

## **LLM/SLM no Azure ML**

O Azure ML adicionou muitas funções relacionadas com LLM/SLM, combinando LLMOps e SLMOps para criar uma plataforma tecnológica de inteligência artificial generativa a nível empresarial.

### **Catálogo de Modelos**

Os utilizadores empresariais podem implementar diferentes modelos conforme diferentes cenários de negócio através do Catálogo de Modelos, e fornecer serviços como Modelo como Serviço para que desenvolvedores ou utilizadores empresariais acedam.

![models](../../../../translated_images/pt/models.e6c7ff50a51806fd.webp)

O Catálogo de Modelos no Azure Machine Learning studio é o centro para descobrir e usar uma vasta gama de modelos que permitem construir aplicações de IA Generativa. O catálogo inclui centenas de modelos de fornecedores como Azure OpenAI service, Mistral, Meta, Cohere, Nvidia, Hugging Face, incluindo modelos treinados pela Microsoft. Modelos de fornecedores que não sejam a Microsoft são Produtos Não Microsoft, conforme definido nos Termos de Produto da Microsoft, e sujeitos aos termos fornecidos com o modelo.

### **Pipeline de Trabalho**

O núcleo de um pipeline de machine learning é dividir uma tarefa completa de machine learning num fluxo de trabalho com múltiplas etapas. Cada etapa é um componente gerível que pode ser desenvolvido, otimizado, configurado e automatizado individualmente. As etapas estão ligadas por interfaces bem definidas. O serviço de pipeline do Azure Machine Learning orquestra automaticamente todas as dependências entre as etapas do pipeline.

No fine-tuning de SLM / LLM, podemos gerir os nossos dados, treino e processos de geração através do Pipeline.

![finetuning](../../../../translated_images/pt/finetuning.6559da198851fa52.webp)

### **Prompt flow**

Vantagens de usar o Azure Machine Learning prompt flow  
O Azure Machine Learning prompt flow oferece várias vantagens que ajudam os utilizadores a passar da ideação à experimentação e, finalmente, a aplicações LLM prontas para produção:

**Agilidade na engenharia de prompts**

Experiência interativa de autoria: o Azure Machine Learning prompt flow fornece uma representação visual da estrutura do fluxo, permitindo aos utilizadores compreender e navegar facilmente nos seus projetos. Também oferece uma experiência de codificação semelhante a notebooks para desenvolvimento e depuração eficientes do fluxo.  
Variantes para ajuste de prompts: os utilizadores podem criar e comparar múltiplas variantes de prompts, facilitando um processo iterativo de refinamento.

Avaliação: fluxos de avaliação incorporados permitem aos utilizadores avaliar a qualidade e eficácia dos seus prompts e fluxos.

Recursos abrangentes: o Azure Machine Learning prompt flow inclui uma biblioteca de ferramentas, exemplos e modelos incorporados que servem como ponto de partida para o desenvolvimento, inspirando criatividade e acelerando o processo.

**Prontidão empresarial para aplicações baseadas em LLM**

Colaboração: o Azure Machine Learning prompt flow suporta colaboração em equipa, permitindo que vários utilizadores trabalhem juntos em projetos de engenharia de prompts, partilhem conhecimento e mantenham controlo de versões.

Plataforma tudo-em-um: o Azure Machine Learning prompt flow simplifica todo o processo de engenharia de prompts, desde o desenvolvimento e avaliação até à implementação e monitorização. Os utilizadores podem implementar facilmente os seus fluxos como endpoints do Azure Machine Learning e monitorizar o seu desempenho em tempo real, garantindo operação ótima e melhoria contínua.

Soluções de Prontidão Empresarial do Azure Machine Learning: o prompt flow aproveita as robustas soluções de prontidão empresarial do Azure Machine Learning, fornecendo uma base segura, escalável e fiável para o desenvolvimento, experimentação e implementação de fluxos.

Com o Azure Machine Learning prompt flow, os utilizadores podem libertar a sua agilidade na engenharia de prompts, colaborar eficazmente e tirar partido de soluções de nível empresarial para o desenvolvimento e implementação bem-sucedidos de aplicações baseadas em LLM.

Combinando o poder computacional, dados e diferentes componentes do Azure ML, os desenvolvedores empresariais podem construir facilmente as suas próprias aplicações de inteligência artificial.

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.