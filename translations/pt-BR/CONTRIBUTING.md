# Contribuindo

Este projeto aceita contribuições e sugestões. A maioria das contribuições exige que você concorde com um Acordo de Licença de Contribuidor (CLA) declarando que você tem o direito e realmente concede a nós os direitos de usar sua contribuição. Para mais detalhes, visite [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com)

Quando você enviar um pull request, um bot de CLA determinará automaticamente se você precisa fornecer um CLA e marcará o PR adequadamente (por exemplo, verificação de status, comentário). Basta seguir as instruções fornecidas pelo bot. Você precisará fazer isso apenas uma vez para todos os repositórios que usam nosso CLA.

## Código de Conduta

Este projeto adotou o [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).  
Para mais informações, leia o [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) ou entre em contato pelo e-mail [opencode@microsoft.com](mailto:opencode@microsoft.com) para dúvidas ou comentários adicionais.

## Cuidados ao criar issues

Por favor, não abra issues no GitHub para dúvidas gerais de suporte, pois a lista do GitHub deve ser usada para solicitações de funcionalidades e relatórios de bugs. Assim, podemos acompanhar mais facilmente problemas reais ou bugs no código e manter a discussão geral separada do código em si.

## Como Contribuir

### Diretrizes para Pull Requests

Ao enviar um pull request (PR) para o repositório Phi-3 CookBook, siga as diretrizes abaixo:

- **Faça um fork do repositório**: Sempre faça um fork do repositório para sua própria conta antes de fazer suas modificações.

- **Pull requests separados (PR)**:
  - Envie cada tipo de alteração em um pull request separado. Por exemplo, correções de bugs e atualizações de documentação devem ser enviadas em PRs distintos.
  - Correções de erros de digitação e pequenas atualizações de documentação podem ser combinadas em um único PR quando apropriado.

- **Resolver conflitos de merge**: Se seu pull request apresentar conflitos de merge, atualize sua branch `main` local para refletir o repositório principal antes de fazer suas modificações.

- **Envio de traduções**: Ao enviar um PR de tradução, certifique-se de que a pasta de tradução inclua traduções para todos os arquivos da pasta original.

### Diretrizes de Escrita

Para garantir consistência em todos os documentos, siga as diretrizes abaixo:

- **Formatação de URLs**: Envolva todas as URLs entre colchetes seguidos de parênteses, sem espaços extras ao redor ou dentro deles. Por exemplo: `[example](https://www.microsoft.com)`.

- **Links relativos**: Use `./` para links relativos que apontam para arquivos ou pastas no diretório atual, e `../` para aqueles em um diretório pai. Por exemplo: `[example](../../path/to/file)` ou `[example](../../../path/to/file)`.

- **Locales não específicos de país**: Certifique-se de que seus links não incluam locales específicos de país. Por exemplo, evite `/en-us/` ou `/en/`.

- **Armazenamento de imagens**: Armazene todas as imagens na pasta `./imgs`.

- **Nomes descritivos para imagens**: Nomeie as imagens de forma descritiva usando caracteres em inglês, números e traços. Por exemplo: `example-image.jpg`.

## Workflows do GitHub

Quando você enviar um pull request, os seguintes workflows serão acionados para validar as alterações. Siga as instruções abaixo para garantir que seu pull request passe nas verificações do workflow:

- [Verificar caminhos relativos quebrados](../..)  
- [Verificar URLs sem locale](../..)

### Verificar caminhos relativos quebrados

Este workflow garante que todos os caminhos relativos em seus arquivos estejam corretos.

1. Para garantir que seus links funcionem corretamente, execute as seguintes tarefas usando o VS Code:  
    - Passe o mouse sobre qualquer link em seus arquivos.  
    - Pressione **Ctrl + Clique** para navegar até o link.  
    - Se você clicar em um link e ele não funcionar localmente, isso acionará o workflow e o link não funcionará no GitHub.

1. Para corrigir esse problema, execute as seguintes tarefas usando as sugestões de caminho fornecidas pelo VS Code:  
    - Digite `./` ou `../`.  
    - O VS Code irá sugerir opções disponíveis com base no que você digitou.  
    - Siga o caminho clicando no arquivo ou pasta desejada para garantir que o caminho esteja correto.

Depois de adicionar o caminho relativo correto, salve e envie suas alterações.

### Verificar URLs sem locale

Este workflow garante que qualquer URL web não inclua um locale específico de país. Como este repositório é acessível globalmente, é importante garantir que as URLs não contenham o locale do seu país.

1. Para verificar se suas URLs não possuem locales de país, execute as seguintes tarefas:

    - Verifique se há textos como `/en-us/`, `/en/` ou qualquer outro locale de idioma nas URLs.  
    - Se esses textos não estiverem presentes nas suas URLs, você passará nesta verificação.

1. Para corrigir esse problema, execute as seguintes tarefas:  
    - Abra o arquivo indicado pelo workflow.  
    - Remova o locale do país das URLs.

Depois de remover o locale do país, salve e envie suas alterações.

### Verificar URLs quebradas

Este workflow garante que qualquer URL web em seus arquivos esteja funcionando e retornando código de status 200.

1. Para verificar se suas URLs estão funcionando corretamente, execute as seguintes tarefas:  
    - Verifique o status das URLs em seus arquivos.

2. Para corrigir URLs quebradas, execute as seguintes tarefas:  
    - Abra o arquivo que contém a URL quebrada.  
    - Atualize a URL para a correta.

Depois de corrigir as URLs, salve e envie suas alterações.

> [!NOTE]  
>  
> Pode haver casos em que a verificação de URL falhe mesmo que o link esteja acessível. Isso pode acontecer por vários motivos, incluindo:  
>  
> - **Restrições de rede:** Os servidores do GitHub Actions podem ter restrições de rede que impedem o acesso a certas URLs.  
> - **Problemas de timeout:** URLs que demoram muito para responder podem causar erro de timeout no workflow.  
> - **Problemas temporários no servidor:** Eventuais quedas ou manutenções no servidor podem tornar uma URL temporariamente indisponível durante a validação.

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.