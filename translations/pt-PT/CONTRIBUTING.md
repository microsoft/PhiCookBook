# Contribuir

Este projeto aceita contribuições e sugestões. A maioria das contribuições exige que concorde com um Acordo de Licença de Contribuidor (CLA) declarando que tem o direito e efetivamente concede-nos os direitos para usar a sua contribuição. Para mais detalhes, visite [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com)

Quando submeter um pull request, um bot de CLA irá automaticamente determinar se precisa de fornecer um CLA e marcar o PR adequadamente (por exemplo, verificação de estado, comentário). Basta seguir as instruções fornecidas pelo bot. Só precisará de fazer isto uma vez para todos os repositórios que usam o nosso CLA.

## Código de Conduta

Este projeto adotou o [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).  
Para mais informações, leia as [Perguntas Frequentes sobre o Código de Conduta](https://opensource.microsoft.com/codeofconduct/faq/) ou contacte [opencode@microsoft.com](mailto:opencode@microsoft.com) para quaisquer questões ou comentários adicionais.

## Cuidados ao criar issues

Por favor, não abra issues no GitHub para questões gerais de suporte, pois a lista do GitHub deve ser usada para pedidos de funcionalidades e relatórios de bugs. Desta forma, podemos acompanhar mais facilmente problemas ou erros reais no código e manter a discussão geral separada do código propriamente dito.

## Como Contribuir

### Diretrizes para Pull Requests

Ao submeter um pull request (PR) para o repositório Phi-3 CookBook, por favor siga as seguintes diretrizes:

- **Fork do Repositório**: Faça sempre um fork do repositório para a sua própria conta antes de fazer as suas modificações.

- **Pull requests separados (PR)**:
  - Submeta cada tipo de alteração num pull request separado. Por exemplo, correções de bugs e atualizações de documentação devem ser submetidas em PRs distintos.
  - Correções de erros tipográficos e pequenas atualizações de documentação podem ser combinadas num único PR quando apropriado.

- **Resolver conflitos de merge**: Se o seu pull request apresentar conflitos de merge, atualize a sua branch local `main` para refletir o repositório principal antes de fazer as suas modificações.

- **Submissões de traduções**: Ao submeter um PR de tradução, assegure-se de que a pasta de tradução inclui traduções para todos os ficheiros da pasta original.

### Diretrizes de Escrita

Para garantir consistência em todos os documentos, por favor use as seguintes diretrizes:

- **Formatação de URLs**: Envolva todas as URLs entre colchetes seguidos de parênteses, sem espaços extras à volta ou dentro deles. Por exemplo: `[exemplo](https://www.microsoft.com)`.

- **Links relativos**: Use `./` para links relativos que apontam para ficheiros ou pastas no diretório atual, e `../` para os que apontam para um diretório pai. Por exemplo: `[exemplo](../../caminho/para/ficheiro)` ou `[exemplo](../../../caminho/para/ficheiro)`.

- **Locales não específicos de país**: Certifique-se de que os seus links não incluem locales específicos de país. Por exemplo, evite `/en-us/` ou `/en/`.

- **Armazenamento de imagens**: Guarde todas as imagens na pasta `./imgs`.

- **Nomes descritivos para imagens**: Nomeie as imagens de forma descritiva usando caracteres em inglês, números e hífens. Por exemplo: `exemplo-imagem.jpg`.

## Workflows do GitHub

Quando submeter um pull request, os seguintes workflows serão acionados para validar as alterações. Siga as instruções abaixo para garantir que o seu pull request passa nas verificações do workflow:

- [Verificar Caminhos Relativos Quebrados](../..)
- [Verificar URLs Sem Locale](../..)

### Verificar Caminhos Relativos Quebrados

Este workflow garante que todos os caminhos relativos nos seus ficheiros estão corretos.

1. Para garantir que os seus links funcionam corretamente, execute as seguintes tarefas usando o VS Code:
    - Passe o cursor sobre qualquer link nos seus ficheiros.
    - Pressione **Ctrl + Clique** para navegar até ao link.
    - Se clicar num link e este não funcionar localmente, irá disparar o workflow e não funcionará no GitHub.

1. Para corrigir este problema, execute as seguintes tarefas usando as sugestões de caminho fornecidas pelo VS Code:
    - Digite `./` ou `../`.
    - O VS Code irá sugerir opções disponíveis com base no que digitou.
    - Siga o caminho clicando no ficheiro ou pasta desejada para garantir que o caminho está correto.

Depois de adicionar o caminho relativo correto, guarde e envie as suas alterações.

### Verificar URLs Sem Locale

Este workflow garante que qualquer URL web não inclui um locale específico de país. Como este repositório é acessível globalmente, é importante garantir que as URLs não contenham o locale do seu país.

1. Para verificar que as suas URLs não têm locales de país, execute as seguintes tarefas:

    - Verifique se há texto como `/en-us/`, `/en/` ou qualquer outro locale de idioma nas URLs.
    - Se estes não estiverem presentes nas suas URLs, então passará nesta verificação.

1. Para corrigir este problema, execute as seguintes tarefas:
    - Abra o caminho do ficheiro destacado pelo workflow.
    - Remova o locale do país das URLs.

Depois de remover o locale do país, guarde e envie as suas alterações.

### Verificar URLs Quebradas

Este workflow garante que qualquer URL web nos seus ficheiros está a funcionar e retorna o código de estado 200.

1. Para verificar que as suas URLs estão a funcionar corretamente, execute as seguintes tarefas:
    - Verifique o estado das URLs nos seus ficheiros.

2. Para corrigir quaisquer URLs quebradas, execute as seguintes tarefas:
    - Abra o ficheiro que contém a URL quebrada.
    - Atualize a URL para a correta.

Depois de corrigir as URLs, guarde e envie as suas alterações.

> [!NOTE]
>
> Pode haver casos em que a verificação da URL falhe mesmo que o link esteja acessível. Isto pode acontecer por várias razões, incluindo:
>
> - **Restrições de rede:** Os servidores das ações do GitHub podem ter restrições de rede que impedem o acesso a certas URLs.
> - **Problemas de timeout:** URLs que demoram demasiado a responder podem disparar um erro de timeout no workflow.
> - **Problemas temporários do servidor:** Eventuais períodos de indisponibilidade ou manutenção do servidor podem tornar uma URL temporariamente inacessível durante a validação.

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.