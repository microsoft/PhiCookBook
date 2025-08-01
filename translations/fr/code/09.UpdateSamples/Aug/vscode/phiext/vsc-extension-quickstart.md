<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "62b2632720dd39ef391d6b60b9b4bfb8",
  "translation_date": "2025-07-16T17:33:33+00:00",
  "source_file": "code/09.UpdateSamples/Aug/vscode/phiext/vsc-extension-quickstart.md",
  "language_code": "fr"
}
-->
# Bienvenue dans votre extension VS Code

## Contenu du dossier

* Ce dossier contient tous les fichiers nécessaires à votre extension.
* `package.json` - c’est le fichier manifeste dans lequel vous déclarez votre extension et votre commande.
  * Le plugin d’exemple enregistre une commande et définit son titre ainsi que son nom. Avec ces informations, VS Code peut afficher la commande dans la palette de commandes. Il n’a pas encore besoin de charger le plugin.
* `src/extension.ts` - c’est le fichier principal où vous fournirez l’implémentation de votre commande.
  * Le fichier exporte une fonction, `activate`, qui est appelée la toute première fois que votre extension est activée (dans ce cas en exécutant la commande). À l’intérieur de la fonction `activate`, nous appelons `registerCommand`.
  * Nous passons la fonction contenant l’implémentation de la commande en second paramètre à `registerCommand`.

## Configuration

* installez les extensions recommandées (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner, et dbaeumer.vscode-eslint)

## Démarrez immédiatement

* Appuyez sur `F5` pour ouvrir une nouvelle fenêtre avec votre extension chargée.
* Exécutez votre commande depuis la palette de commandes en appuyant sur (`Ctrl+Shift+P` ou `Cmd+Shift+P` sur Mac) et en tapant `Hello World`.
* Placez des points d’arrêt dans votre code dans `src/extension.ts` pour déboguer votre extension.
* Trouvez la sortie de votre extension dans la console de débogage.

## Apportez des modifications

* Vous pouvez relancer l’extension depuis la barre d’outils de débogage après avoir modifié le code dans `src/extension.ts`.
* Vous pouvez aussi recharger (`Ctrl+R` ou `Cmd+R` sur Mac) la fenêtre VS Code avec votre extension pour appliquer vos modifications.

## Explorez l’API

* Vous pouvez ouvrir l’ensemble complet de notre API en ouvrant le fichier `node_modules/@types/vscode/index.d.ts`.

## Exécutez les tests

* Installez [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* Lancez la tâche "watch" via la commande **Tasks: Run Task**. Assurez-vous qu’elle tourne, sinon les tests risquent de ne pas être détectés.
* Ouvrez la vue Testing depuis la barre d’activités et cliquez sur le bouton "Run Test", ou utilisez le raccourci `Ctrl/Cmd + ; A`
* Consultez le résultat des tests dans la vue Test Results.
* Modifiez `src/test/extension.test.ts` ou créez de nouveaux fichiers de test dans le dossier `test`.
  * Le test runner fourni ne prendra en compte que les fichiers correspondant au motif de nom `**.test.ts`.
  * Vous pouvez créer des dossiers dans le dossier `test` pour organiser vos tests comme vous le souhaitez.

## Allez plus loin

* Réduisez la taille de l’extension et améliorez le temps de démarrage en [regroupant votre extension](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* [Publiez votre extension](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) sur la marketplace des extensions VS Code.
* Automatisez les builds en configurant [l’intégration continue](https://code.visualstudio.com/api/working-with-extensions/continuous-integration).

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.