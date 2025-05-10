<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f71f15fee9a73ecfcd4fd40efbe3070",
  "translation_date": "2025-05-09T03:27:53+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "br"
}
-->
# Contributing

Este projeto aceita contribuições e sugestões. A maioria das contribuições exige que você concorde com um Contributor License Agreement (CLA) declarando que você tem o direito e realmente concede a nós os direitos de usar sua contribuição. Para mais detalhes, visite [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com)

Ao enviar um pull request, um bot de CLA determinará automaticamente se você precisa fornecer um CLA e marcará o PR adequadamente (por exemplo, verificação de status, comentário). Basta seguir as instruções fornecidas pelo bot. Você precisará fazer isso apenas uma vez para todos os repositórios que usam nosso CLA.

## Code of Conduct

Este projeto adotou o [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). Para mais informações, leia o [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) ou entre em contato com [opencode@microsoft.com](mailto:opencode@microsoft.com) para dúvidas ou comentários adicionais.

## Cautions for creating issues

Por favor, não abra issues no GitHub para dúvidas gerais de suporte, pois a lista do GitHub deve ser usada para solicitações de funcionalidades e relatórios de bugs. Assim, podemos acompanhar mais facilmente problemas ou bugs reais do código e manter a discussão geral separada do código propriamente dito.

## How to Contribute

### Pull Requests Guidelines

Ao enviar um pull request (PR) para o repositório Phi-3 CookBook, siga as diretrizes abaixo:

- **Fork do Repositório**: Sempre faça um fork do repositório para sua própria conta antes de fazer suas modificações.

- **Pull requests separados (PR)**:
  - Envie cada tipo de alteração em seu próprio pull request. Por exemplo, correções de bugs e atualizações de documentação devem ser enviadas em PRs separados.
  - Correções de erros de digitação e pequenas atualizações de documentação podem ser combinadas em um único PR quando apropriado.

- **Resolver conflitos de merge**: Se seu pull request apresentar conflitos de merge, atualize sua branch local `main` para refletir o repositório principal antes de fazer suas modificações.

- **Envio de traduções**: Ao enviar um PR de tradução, certifique-se de que a pasta de tradução inclua as traduções de todos os arquivos da pasta original.

### Translation Guidelines

> [!IMPORTANT]
>
> Ao traduzir textos neste repositório, não use tradução automática. Só se voluntarie para traduções em idiomas que você domina.

Se você domina um idioma que não seja inglês, pode ajudar a traduzir o conteúdo. Para garantir que suas contribuições de tradução sejam integradas corretamente, siga as diretrizes abaixo:

- **Crie a pasta de tradução**: Navegue até a pasta da seção apropriada e crie uma pasta de tradução para o idioma ao qual você está contribuindo. Por exemplo:
  - Para a seção de introdução: `PhiCookBook/md/01.Introduce/translations/<language_code>/`
  - Para a seção de início rápido: `PhiCookBook/md/02.QuickStart/translations/<language_code>/`
  - Continue esse padrão para outras seções (03.Inference, 04.Finetuning, etc.)

- **Atualize os caminhos relativos**: Ao traduzir, ajuste a estrutura das pastas adicionando `../../` no início dos caminhos relativos dentro dos arquivos markdown para garantir que os links funcionem corretamente. Por exemplo, altere:
  - `(../../imgs/01/phi3aisafety.png)` para `(../../../../imgs/01/phi3aisafety.png)`

- **Organize suas traduções**: Cada arquivo traduzido deve ser colocado na pasta de tradução correspondente à seção. Por exemplo, se estiver traduzindo a seção de introdução para espanhol, você criaria:
  - `PhiCookBook/md/01.Introduce/translations/es/`

- **Envie um PR completo**: Certifique-se de que todos os arquivos traduzidos para uma seção estejam incluídos em um único PR. Não aceitamos traduções parciais para uma seção. Ao enviar um PR de tradução, garanta que a pasta de tradução contenha as traduções de todos os arquivos da pasta original.

### Writing Guidelines

Para garantir consistência em todos os documentos, siga as diretrizes abaixo:

- **Formatação de URLs**: Envolva todas as URLs em colchetes seguidos de parênteses, sem espaços extras ao redor ou dentro deles. Por exemplo: `[example](https://www.microsoft.com)`.

- **Links relativos**: Use `./` para links relativos que apontam para arquivos ou pastas no diretório atual, e `../` para aqueles em um diretório pai. Por exemplo: `[example](../../path/to/file)` ou `[example](../../../path/to/file)`.

- **Não usar localidades específicas de país**: Certifique-se de que seus links não incluam localidades específicas de país. Por exemplo, evite `/en-us/` ou `/en/`.

- **Armazenamento de imagens**: Armazene todas as imagens na pasta `./imgs`.

- **Nomes descritivos para imagens**: Nomeie as imagens de forma descritiva usando caracteres em inglês, números e hífens. Por exemplo: `example-image.jpg`.

## GitHub Workflows

Ao enviar um pull request, os seguintes workflows serão acionados para validar as alterações. Siga as instruções abaixo para garantir que seu pull request passe nas verificações:

- [Check Broken Relative Paths](../..)
- [Check URLs Don't Have Locale](../..)

### Check Broken Relative Paths

Este workflow garante que todos os caminhos relativos em seus arquivos estejam corretos.

1. Para garantir que seus links funcionem corretamente, execute as seguintes tarefas usando o VS Code:
    - Passe o cursor sobre qualquer link em seus arquivos.
    - Pressione **Ctrl + Clique** para navegar até o link.
    - Se você clicar em um link e ele não funcionar localmente, isso acionará o workflow e não funcionará no GitHub.

1. Para corrigir esse problema, execute as tarefas abaixo usando as sugestões de caminho fornecidas pelo VS Code:
    - Digite `./` ou `../`.
    - O VS Code irá sugerir opções com base no que você digitou.
    - Siga o caminho clicando no arquivo ou pasta desejada para garantir que o caminho está correto.

Depois de adicionar o caminho relativo correto, salve e envie suas alterações.

### Check URLs Don't Have Locale

Este workflow garante que qualquer URL web não inclua uma localidade específica de país. Como este repositório é acessível globalmente, é importante garantir que as URLs não contenham a localidade do seu país.

1. Para verificar se suas URLs não têm localidades de país, execute as seguintes tarefas:

    - Verifique se há textos como `/en-us/`, `/en/`, ou qualquer outra localidade de idioma nas URLs.
    - Se não houver essas localidades nas URLs, você passará nesta verificação.

1. Para corrigir esse problema, execute as seguintes tarefas:
    - Abra o arquivo destacado pelo workflow.
    - Remova a localidade do país das URLs.

Depois de remover a localidade do país, salve e envie suas alterações.

### Check Broken Urls

Este workflow garante que qualquer URL web em seus arquivos esteja funcionando e retornando o código de status 200.

1. Para verificar se suas URLs estão funcionando corretamente, execute as seguintes tarefas:
    - Verifique o status das URLs em seus arquivos.

2. Para corrigir URLs quebradas, execute as seguintes tarefas:
    - Abra o arquivo que contém a URL quebrada.
    - Atualize a URL para a correta.

Depois de corrigir as URLs, salve e envie suas alterações.

> [!NOTE]
>
> Pode haver casos em que a verificação de URL falhe mesmo que o link esteja acessível. Isso pode ocorrer por vários motivos, incluindo:
>
> - **Restrições de rede:** Os servidores do GitHub Actions podem ter restrições de rede que impedem o acesso a certas URLs.
> - **Problemas de timeout:** URLs que demoram muito para responder podem gerar erro de timeout no workflow.
> - **Problemas temporários no servidor:** Eventuais indisponibilidades ou manutenção do servidor podem tornar uma URL temporariamente inacessível durante a validação.

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.