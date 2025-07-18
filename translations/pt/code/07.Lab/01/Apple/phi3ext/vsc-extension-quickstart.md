<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "62b2632720dd39ef391d6b60b9b4bfb8",
  "translation_date": "2025-07-16T17:00:46+00:00",
  "source_file": "code/07.Lab/01/Apple/phi3ext/vsc-extension-quickstart.md",
  "language_code": "pt"
}
-->
# Bem-vindo à sua Extensão VS Code

## O que está na pasta

* Esta pasta contém todos os ficheiros necessários para a sua extensão.
* `package.json` - este é o ficheiro manifesto onde declara a sua extensão e comando.
  * O plugin de exemplo regista um comando e define o seu título e nome do comando. Com esta informação, o VS Code pode mostrar o comando na paleta de comandos. Ainda não é necessário carregar o plugin.
* `src/extension.ts` - este é o ficheiro principal onde irá implementar o seu comando.
  * O ficheiro exporta uma função, `activate`, que é chamada na primeira vez que a sua extensão é ativada (neste caso, ao executar o comando). Dentro da função `activate` chamamos `registerCommand`.
  * Passamos a função que contém a implementação do comando como segundo parâmetro para `registerCommand`.

## Configuração

* instale as extensões recomendadas (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner, e dbaeumer.vscode-eslint)

## Comece a usar imediatamente

* Prima `F5` para abrir uma nova janela com a sua extensão carregada.
* Execute o seu comando a partir da paleta de comandos pressionando (`Ctrl+Shift+P` ou `Cmd+Shift+P` no Mac) e escrevendo `Hello World`.
* Defina pontos de interrupção no seu código dentro de `src/extension.ts` para depurar a sua extensão.
* Encontre a saída da sua extensão na consola de depuração.

## Faça alterações

* Pode relançar a extensão a partir da barra de ferramentas de depuração depois de alterar o código em `src/extension.ts`.
* Também pode recarregar (`Ctrl+R` ou `Cmd+R` no Mac) a janela do VS Code com a sua extensão para carregar as suas alterações.

## Explore a API

* Pode abrir o conjunto completo da nossa API ao abrir o ficheiro `node_modules/@types/vscode/index.d.ts`.

## Executar testes

* Instale o [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* Execute a tarefa "watch" através do comando **Tasks: Run Task**. Certifique-se de que está a correr, caso contrário os testes podem não ser encontrados.
* Abra a vista de Testes na barra de atividades e clique no botão "Run Test", ou use o atalho `Ctrl/Cmd + ; A`
* Veja a saída do resultado do teste na vista Test Results.
* Faça alterações em `src/test/extension.test.ts` ou crie novos ficheiros de teste dentro da pasta `test`.
  * O test runner fornecido só considera ficheiros que correspondam ao padrão de nome `**.test.ts`.
  * Pode criar pastas dentro da pasta `test` para organizar os seus testes da forma que desejar.

## Vá mais longe

* Reduza o tamanho da extensão e melhore o tempo de arranque [empacotando a sua extensão](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* [Publique a sua extensão](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) no marketplace de extensões do VS Code.
* Automatize builds configurando [Integração Contínua](https://code.visualstudio.com/api/working-with-extensions/continuous-integration).

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos por garantir a precisão, por favor tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações erradas decorrentes da utilização desta tradução.