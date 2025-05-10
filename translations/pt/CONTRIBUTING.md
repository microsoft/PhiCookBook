<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f71f15fee9a73ecfcd4fd40efbe3070",
  "translation_date": "2025-05-09T03:27:38+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "pt"
}
-->
# Contribuindo

Este projeto aceita contribuições e sugestões. A maioria das contribuições exige que você concorde com um Acordo de Licença de Contribuidor (CLA) declarando que você tem o direito e realmente concede a nós os direitos de usar sua contribuição. Para mais detalhes, visite [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com)

Ao enviar um pull request, um bot de CLA determinará automaticamente se você precisa fornecer um CLA e marcará o PR adequadamente (por exemplo, verificação de status, comentário). Basta seguir as instruções fornecidas pelo bot. Você precisará fazer isso apenas uma vez para todos os repositórios que usam nosso CLA.

## Código de Conduta

Este projeto adotou o [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).  
Para mais informações, leia o [FAQ do Código de Conduta](https://opensource.microsoft.com/codeofconduct/faq/) ou entre em contato com [opencode@microsoft.com](mailto:opencode@microsoft.com) para dúvidas ou comentários adicionais.

## Cuidados ao criar issues

Por favor, não abra issues no GitHub para dúvidas gerais de suporte, pois a lista do GitHub deve ser usada para solicitações de funcionalidades e relatórios de bugs. Dessa forma, podemos acompanhar mais facilmente problemas reais ou bugs no código e manter a discussão geral separada do código em si.

## Como Contribuir

### Diretrizes para Pull Requests

Ao enviar um pull request (PR) para o repositório Phi-3 CookBook, siga as diretrizes abaixo:

- **Faça um fork do repositório**: Sempre faça um fork do repositório para sua própria conta antes de fazer suas modificações.

- **Pull requests separados**:
  - Envie cada tipo de alteração em um pull request separado. Por exemplo, correções de bugs e atualizações de documentação devem ser enviadas em PRs distintos.
  - Correções de erros de digitação e pequenas atualizações de documentação podem ser combinadas em um único PR quando apropriado.

- **Resolver conflitos de merge**: Se seu pull request apresentar conflitos de merge, atualize sua branch local `main` para espelhar o repositório principal antes de fazer suas modificações.

- **Envio de traduções**: Ao enviar um PR de tradução, certifique-se de que a pasta de tradução inclua traduções para todos os arquivos da pasta original.

### Diretrizes de Tradução

> [!IMPORTANT]
>
> Ao traduzir textos neste repositório, não utilize tradução automática. Só se voluntarie para traduções em idiomas nos quais você seja proficiente.

Se você domina um idioma que não seja o inglês, pode ajudar traduzindo o conteúdo. Siga estes passos para garantir que suas contribuições sejam integradas corretamente, usando as seguintes diretrizes:

- **Crie a pasta de tradução**: Navegue até a pasta da seção apropriada e crie uma pasta de tradução para o idioma que você está contribuindo. Por exemplo:
  - Para a seção de introdução: `PhiCookBook/md/01.Introduce/translations/<language_code>/`
  - Para a seção de início rápido: `PhiCookBook/md/02.QuickStart/translations/<language_code>/`
  - Continue esse padrão para outras seções (03.Inference, 04.Finetuning, etc.)

- **Atualize os caminhos relativos**: Ao traduzir, ajuste a estrutura de pastas adicionando `../../` no início dos caminhos relativos dentro dos arquivos markdown para garantir que os links funcionem corretamente. Por exemplo, altere:
  - De `(../../imgs/01/phi3aisafety.png)` para `(../../../../imgs/01/phi3aisafety.png)`

- **Organize suas traduções**: Cada arquivo traduzido deve ser colocado na pasta de tradução correspondente à seção. Por exemplo, se você estiver traduzindo a seção de introdução para o espanhol, crie a seguinte estrutura:
  - `PhiCookBook/md/01.Introduce/translations/es/`

- **Envie um PR completo**: Garanta que todos os arquivos traduzidos de uma seção estejam incluídos em um único PR. Não aceitamos traduções parciais de uma seção. Ao enviar um PR de tradução, certifique-se de que a pasta de tradução contenha todas as traduções dos arquivos da pasta original.

### Diretrizes de Escrita

Para garantir consistência em todos os documentos, utilize as seguintes orientações:

- **Formatação de URLs**: Envolva todas as URLs entre colchetes seguidos de parênteses, sem espaços extras ao redor ou dentro deles. Por exemplo: `[example](https://www.microsoft.com)`.

- **Links relativos**: Use `./` para links relativos que apontam para arquivos ou pastas no diretório atual, e `../` para aqueles em diretórios superiores. Por exemplo: `[example](../../path/to/file)` ou `[example](../../../path/to/file)`.

- **Locales não específicos de país**: Certifique-se de que seus links não incluam locais específicos de país. Por exemplo, evite `/en-us/` ou `/en/`.

- **Armazenamento de imagens**: Armazene todas as imagens na pasta `./imgs`.

- **Nomes descritivos para imagens**: Nomeie as imagens de forma descritiva usando caracteres em inglês, números e traços. Por exemplo: `example-image.jpg`.

## Workflows do GitHub

Ao enviar um pull request, os seguintes workflows serão acionados para validar as alterações. Siga as instruções abaixo para garantir que seu pull request passe nas verificações dos workflows:

- [Check Broken Relative Paths](../..)  
- [Check URLs Don't Have Locale](../..)

### Check Broken Relative Paths

Este workflow garante que todos os caminhos relativos em seus arquivos estejam corretos.

1. Para garantir que seus links estejam funcionando corretamente, faça o seguinte usando o VS Code:
    - Passe o mouse sobre qualquer link nos seus arquivos.
    - Pressione **Ctrl + Clique** para navegar até o link.
    - Se o link não funcionar localmente, isso acionará o workflow e o link não funcionará no GitHub.

1. Para corrigir esse problema, faça o seguinte usando as sugestões de caminho fornecidas pelo VS Code:
    - Digite `./` ou `../`.
    - O VS Code irá sugerir opções com base no que você digitou.
    - Siga o caminho clicando no arquivo ou pasta desejada para garantir que o caminho esteja correto.

Depois de adicionar o caminho relativo correto, salve e envie suas alterações.

### Check URLs Don't Have Locale

Este workflow garante que qualquer URL web não contenha um local específico de país. Como este repositório é acessível globalmente, é importante garantir que as URLs não contenham o local do seu país.

1. Para verificar se suas URLs não possuem locais específicos, faça o seguinte:

    - Verifique se há textos como `/en-us/`, `/en/` ou qualquer outro local de idioma nas URLs.
    - Se esses não estiverem presentes em suas URLs, você passará nesta verificação.

1. Para corrigir esse problema, faça o seguinte:
    - Abra o arquivo destacado pelo workflow.
    - Remova o local do país das URLs.

Depois de remover o local do país, salve e envie suas alterações.

### Check Broken Urls

Este workflow garante que qualquer URL web em seus arquivos esteja funcionando e retorne código de status 200.

1. Para verificar se suas URLs estão funcionando corretamente, faça o seguinte:
    - Verifique o status das URLs em seus arquivos.

2. Para corrigir URLs quebradas, faça o seguinte:
    - Abra o arquivo que contém a URL quebrada.
    - Atualize a URL para a correta.

Depois de corrigir as URLs, salve e envie suas alterações.

> [!NOTE]
>
> Pode haver casos em que a verificação de URL falhe mesmo que o link esteja acessível. Isso pode ocorrer por vários motivos, incluindo:
>
> - **Restrições de rede:** os servidores de ações do GitHub podem ter restrições de rede que impedem o acesso a certas URLs.
> - **Problemas de timeout:** URLs que demoram muito para responder podem gerar erro de timeout no workflow.
> - **Problemas temporários no servidor:** interrupções ocasionais ou manutenção do servidor podem tornar uma URL temporariamente indisponível durante a validação.

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.