<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "212531c5722978740dcfb73e3995cbba",
  "translation_date": "2025-04-03T05:59:05+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "fr"
}
-->
# Contribuer

Ce projet accueille volontiers les contributions et suggestions. La plupart des contributions nécessitent que vous acceptiez un Accord de Licence de Contributeur (CLA) déclarant que vous avez le droit, et que vous accordez effectivement, les droits nécessaires pour utiliser votre contribution. Pour plus de détails, visitez [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com).

Lorsque vous soumettez une pull request, un bot CLA déterminera automatiquement si vous devez fournir un CLA et annotera la PR en conséquence (par exemple, vérification de statut, commentaire). Suivez simplement les instructions fournies par le bot. Vous n'aurez besoin de le faire qu'une seule fois pour tous les dépôts utilisant notre CLA.

## Code de conduite

Ce projet a adopté le [Code de conduite Open Source de Microsoft](https://opensource.microsoft.com/codeofconduct/). Pour plus d'informations, consultez la [FAQ sur le code de conduite](https://opensource.microsoft.com/codeofconduct/faq/) ou contactez [opencode@microsoft.com](mailto:opencode@microsoft.com) pour toute question ou commentaire supplémentaire.

## Précautions lors de la création de problèmes

Veuillez ne pas ouvrir de problèmes GitHub pour des questions générales de support, car la liste GitHub doit être utilisée pour les demandes de fonctionnalités et les rapports de bugs. Cela nous permet de mieux suivre les problèmes ou bugs réels liés au code et de séparer les discussions générales du code lui-même.

## Comment contribuer

### Directives pour les pull requests

Lorsque vous soumettez une pull request (PR) au dépôt Phi-3 CookBook, veuillez suivre les directives suivantes :

- **Forker le dépôt** : Forkez toujours le dépôt sur votre propre compte avant de faire vos modifications.

- **Séparer les pull requests (PR)** :
  - Soumettez chaque type de changement dans une pull request distincte. Par exemple, les corrections de bugs et les mises à jour de documentation doivent être soumises dans des PR séparées.
  - Les corrections de fautes de frappe et les mises à jour mineures de documentation peuvent être combinées dans une seule PR si cela est approprié.

- **Gérer les conflits de fusion** : Si votre pull request présente des conflits de fusion, mettez à jour votre branche locale `main` pour refléter le dépôt principal avant de faire vos modifications.

- **Soumissions de traductions** : Lors de la soumission d'une PR de traduction, assurez-vous que le dossier de traduction inclut les traductions de tous les fichiers du dossier original.

### Directives pour les traductions

> [!IMPORTANT]
>
> Lors de la traduction de texte dans ce dépôt, n'utilisez pas de traduction automatique. Contribuez uniquement dans les langues où vous êtes compétent.

Si vous maîtrisez une langue autre que l'anglais, vous pouvez aider à traduire le contenu. Suivez ces étapes pour que vos contributions de traduction soient correctement intégrées, en respectant les directives suivantes :

- **Créer un dossier de traduction** : Accédez au dossier de la section appropriée et créez un dossier de traduction pour la langue que vous contribuez. Par exemple :
  - Pour la section introduction : `PhiCookBook/md/01.Introduce/translations/<language_code>/`
  - Pour la section démarrage rapide : `PhiCookBook/md/02.QuickStart/translations/<language_code>/`
  - Continuez ce modèle pour les autres sections (03.Inference, 04.Finetuning, etc.)

- **Mettre à jour les chemins relatifs** : Lors de la traduction, ajustez la structure des dossiers en ajoutant `../../` au début des chemins relatifs dans les fichiers markdown pour garantir que les liens fonctionnent correctement. Par exemple, modifiez comme suit :
  - Changez `(../../imgs/01/phi3aisafety.png)` en `(../../../../imgs/01/phi3aisafety.png)`

- **Organiser vos traductions** : Chaque fichier traduit doit être placé dans le dossier de traduction correspondant à la section. Par exemple, si vous traduisez la section introduction en espagnol, vous créeriez comme suit :
  - `PhiCookBook/md/01.Introduce/translations/es/`

- **Soumettre une PR complète** : Assurez-vous que tous les fichiers traduits pour une section sont inclus dans une seule PR. Nous n'acceptons pas les traductions partielles pour une section. Lors de la soumission d'une PR de traduction, vérifiez que le dossier de traduction inclut les traductions de tous les fichiers du dossier original.

### Directives de rédaction

Pour garantir la cohérence dans tous les documents, veuillez utiliser les directives suivantes :

- **Formatage des URL** : Encadrez toutes les URL entre crochets suivis de parenthèses, sans espaces supplémentaires autour ou à l'intérieur. Par exemple : `[example](https://www.microsoft.com)`.

- **Liens relatifs** : Utilisez `./` pour les liens relatifs pointant vers des fichiers ou dossiers dans le répertoire actuel, et `../` pour ceux dans un répertoire parent. Par exemple : `[example](../../path/to/file)` ou `[example](../../../path/to/file)`.

- **Locales non spécifiques à un pays** : Assurez-vous que vos liens ne contiennent pas de locales spécifiques à un pays. Par exemple, évitez `/en-us/` ou `/en/`.

- **Stockage des images** : Stockez toutes les images dans le dossier `./imgs`.

- **Noms descriptifs pour les images** : Nommez les images de manière descriptive en utilisant des caractères anglais, des chiffres et des tirets. Par exemple : `example-image.jpg`.

## Workflows GitHub

Lorsque vous soumettez une pull request, les workflows suivants seront déclenchés pour valider les modifications. Suivez les instructions ci-dessous pour garantir que votre pull request passe les vérifications des workflows :

- [Vérifier les chemins relatifs cassés](../..)
- [Vérifier que les URL n'ont pas de locale](../..)

### Vérifier les chemins relatifs cassés

Ce workflow garantit que tous les chemins relatifs dans vos fichiers sont corrects.

1. Pour vous assurer que vos liens fonctionnent correctement, effectuez les tâches suivantes en utilisant VS Code :
    - Passez la souris sur n'importe quel lien dans vos fichiers.
    - Appuyez sur **Ctrl + Clic** pour naviguer vers le lien.
    - Si vous cliquez sur un lien et qu'il ne fonctionne pas localement, cela déclenchera le workflow et ne fonctionnera pas sur GitHub.

1. Pour résoudre ce problème, effectuez les tâches suivantes en utilisant les suggestions de chemin fournies par VS Code :
    - Tapez `./` ou `../`.
    - VS Code vous proposera de choisir parmi les options disponibles en fonction de ce que vous avez tapé.
    - Suivez le chemin en cliquant sur le fichier ou dossier souhaité pour garantir que votre chemin est correct.

Une fois que vous avez ajouté le chemin relatif correct, enregistrez et poussez vos modifications.

### Vérifier que les URL n'ont pas de locale

Ce workflow garantit que toute URL web n'inclut pas de locale spécifique à un pays. Comme ce dépôt est accessible globalement, il est important de s'assurer que les URL ne contiennent pas la locale de votre pays.

1. Pour vérifier que vos URL n'ont pas de locales de pays, effectuez les tâches suivantes :

    - Vérifiez les textes comme `/en-us/`, `/en/`, ou toute autre locale de langue dans les URL.
    - Si elles ne sont pas présentes dans vos URL, vous passerez cette vérification.

1. Pour résoudre ce problème, effectuez les tâches suivantes :
    - Ouvrez le chemin du fichier mis en évidence par le workflow.
    - Supprimez la locale de pays des URL.

Une fois que vous avez supprimé la locale de pays, enregistrez et poussez vos modifications.

### Vérifier les URL cassées

Ce workflow garantit que toute URL web dans vos fichiers fonctionne et retourne un code de statut 200.

1. Pour vérifier que vos URL fonctionnent correctement, effectuez les tâches suivantes :
    - Vérifiez le statut des URL dans vos fichiers.

2. Pour corriger toute URL cassée, effectuez les tâches suivantes :
    - Ouvrez le fichier contenant l'URL cassée.
    - Mettez à jour l'URL avec la correcte.

Une fois que vous avez corrigé les URL, enregistrez et poussez vos modifications.

> [!NOTE]
>
> Il peut arriver que la vérification des URL échoue même si le lien est accessible. Cela peut se produire pour plusieurs raisons, notamment :
>
> - **Restrictions réseau** : Les serveurs des actions GitHub peuvent avoir des restrictions réseau empêchant l'accès à certaines URL.
> - **Problèmes de délai d'attente** : Les URL qui prennent trop de temps à répondre peuvent déclencher une erreur de délai d'attente dans le workflow.
> - **Problèmes temporaires de serveur** : Les temps d'arrêt occasionnels ou la maintenance des serveurs peuvent rendre une URL temporairement inaccessible pendant la validation.

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.