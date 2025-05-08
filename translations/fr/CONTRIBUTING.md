<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f71f15fee9a73ecfcd4fd40efbe3070",
  "translation_date": "2025-05-07T12:58:14+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "fr"
}
-->
# Contribution

Ce projet accueille les contributions et suggestions. La plupart des contributions nécessitent que vous acceptiez un
Accord de Licence de Contributeur (CLA) déclarant que vous avez le droit, et que vous accordez effectivement, les
droits d’utilisation de votre contribution. Pour plus de détails, consultez [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com)

Lorsque vous soumettez une pull request, un bot CLA déterminera automatiquement si vous devez fournir
un CLA et annotera la PR en conséquence (par exemple, vérification du statut, commentaire). Suivez simplement les instructions
du bot. Vous n’aurez à le faire qu’une seule fois pour tous les dépôts utilisant notre CLA.

## Code de conduite

Ce projet a adopté le [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
Pour plus d’informations, consultez la [FAQ du Code de conduite](https://opensource.microsoft.com/codeofconduct/faq/) ou contactez [opencode@microsoft.com](mailto:opencode@microsoft.com) pour toute question ou commentaire supplémentaire.

## Précautions pour la création de tickets

Merci de ne pas ouvrir de tickets GitHub pour des questions de support général, car la liste GitHub doit être utilisée pour les demandes de fonctionnalités et les rapports de bugs. Cela nous permet de suivre plus facilement les problèmes ou bugs réels liés au code et de séparer la discussion générale du code lui-même.

## Comment contribuer

### Directives pour les Pull Requests

Lors de la soumission d’une pull request (PR) dans le dépôt Phi-3 CookBook, veuillez suivre les directives suivantes :

- **Fork du dépôt** : Toujours forker le dépôt dans votre propre compte avant de faire vos modifications.

- **Pull requests séparées (PR)** :
  - Soumettez chaque type de modification dans une PR distincte. Par exemple, les corrections de bugs et les mises à jour de documentation doivent être soumises dans des PR séparées.
  - Les corrections de fautes de frappe et les petites mises à jour de documentation peuvent être combinées dans une seule PR lorsque cela est approprié.

- **Gérer les conflits de fusion** : Si votre pull request affiche des conflits de fusion, mettez à jour votre branche locale `main` pour qu’elle reflète le dépôt principal avant de faire vos modifications.

- **Soumissions de traduction** : Lors de la soumission d’une PR de traduction, assurez-vous que le dossier de traduction inclut les traductions de tous les fichiers présents dans le dossier original.

### Directives de traduction

> [!IMPORTANT]
>
> Lors de la traduction des textes dans ce dépôt, n’utilisez pas de traduction automatique. Ne proposez vos services que pour des langues que vous maîtrisez.

Si vous maîtrisez une langue autre que l’anglais, vous pouvez aider à traduire le contenu. Suivez ces étapes pour garantir que vos contributions de traduction soient bien intégrées, en respectant les directives suivantes :

- **Créer un dossier de traduction** : Rendez-vous dans le dossier de la section concernée et créez un dossier de traduction pour la langue à laquelle vous contribuez. Par exemple :
  - Pour la section introduction : `PhiCookBook/md/01.Introduce/translations/<language_code>/`
  - Pour la section démarrage rapide : `PhiCookBook/md/02.QuickStart/translations/<language_code>/`
  - Continuez ce schéma pour les autres sections (03.Inference, 04.Finetuning, etc.)

- **Mettre à jour les chemins relatifs** : Lors de la traduction, ajustez la structure des dossiers en ajoutant `../../` au début des chemins relatifs dans les fichiers markdown afin que les liens fonctionnent correctement. Par exemple, remplacez :
  - `(../../imgs/01/phi3aisafety.png)` par `(../../../../imgs/01/phi3aisafety.png)`

- **Organiser vos traductions** : Chaque fichier traduit doit être placé dans le dossier de traduction de la section correspondante. Par exemple, si vous traduisez la section introduction en espagnol, créez le dossier comme suit :
  - `PhiCookBook/md/01.Introduce/translations/es/`

- **Soumettre une PR complète** : Assurez-vous que tous les fichiers traduits d’une section soient inclus dans une seule PR. Nous n’acceptons pas les traductions partielles pour une section. Lors de la soumission d’une PR de traduction, vérifiez que le dossier de traduction contient les traductions de tous les fichiers du dossier original.

### Directives de rédaction

Pour garantir la cohérence de tous les documents, veuillez suivre les directives suivantes :

- **Formatage des URL** : Entourez toutes les URL de crochets suivis de parenthèses, sans espaces supplémentaires autour ou à l’intérieur. Par exemple : `[example](https://www.microsoft.com)`.

- **Liens relatifs** : Utilisez `./` pour les liens relatifs pointant vers des fichiers ou dossiers dans le répertoire courant, et `../` pour ceux situés dans un répertoire parent. Par exemple : `[example](../../path/to/file)` ou `[example](../../../path/to/file)`.

- **Locales non spécifiques à un pays** : Veillez à ce que vos liens n’incluent pas de locales spécifiques à un pays. Par exemple, évitez `/en-us/` ou `/en/`.

- **Stockage des images** : Stockez toutes les images dans le dossier `./imgs`.

- **Noms d’images descriptifs** : Donnez aux images des noms descriptifs en utilisant des caractères anglais, des chiffres et des tirets. Par exemple : `example-image.jpg`.

## Workflows GitHub

Lorsque vous soumettez une pull request, les workflows suivants seront déclenchés pour valider les modifications. Suivez les instructions ci-dessous pour vous assurer que votre pull request passe les vérifications :

- [Vérifier les chemins relatifs cassés](../..)
- [Vérifier que les URL ne contiennent pas de locale](../..)

### Vérifier les chemins relatifs cassés

Ce workflow vérifie que tous les chemins relatifs dans vos fichiers sont corrects.

1. Pour vérifier que vos liens fonctionnent correctement, effectuez les opérations suivantes dans VS Code :
    - Survolez un lien dans vos fichiers.
    - Appuyez sur **Ctrl + clic** pour naviguer vers le lien.
    - Si un lien ne fonctionne pas localement, cela déclenchera le workflow et il ne fonctionnera pas non plus sur GitHub.

1. Pour corriger ce problème, effectuez les opérations suivantes en utilisant les suggestions de chemin proposées par VS Code :
    - Tapez `./` ou `../`.
    - VS Code vous proposera des options basées sur ce que vous avez tapé.
    - Suivez le chemin en cliquant sur le fichier ou dossier désiré pour vous assurer que le chemin est correct.

Une fois le chemin relatif corrigé, sauvegardez et poussez vos modifications.

### Vérifier que les URL ne contiennent pas de locale

Ce workflow vérifie qu’aucune URL web ne contient une locale spécifique à un pays. Comme ce dépôt est accessible mondialement, il est important que les URL ne contiennent pas la locale de votre pays.

1. Pour vérifier que vos URL ne contiennent pas de locales pays, effectuez les opérations suivantes :

    - Recherchez des textes comme `/en-us/`, `/en/`, ou toute autre locale de langue dans les URL.
    - Si ces éléments ne sont pas présents dans vos URL, vous passerez la vérification.

1. Pour corriger ce problème, effectuez les opérations suivantes :
    - Ouvrez le fichier indiqué par le workflow.
    - Supprimez la locale pays des URL.

Une fois la locale pays supprimée, sauvegardez et poussez vos modifications.

### Vérifier les URL cassées

Ce workflow vérifie que toutes les URL web dans vos fichiers fonctionnent et renvoient un code de statut 200.

1. Pour vérifier que vos URL fonctionnent correctement, effectuez les opérations suivantes :
    - Vérifiez le statut des URL dans vos fichiers.

2. Pour corriger les URL cassées, effectuez les opérations suivantes :
    - Ouvrez le fichier contenant l’URL cassée.
    - Mettez à jour l’URL avec la bonne adresse.

Une fois les URL corrigées, sauvegardez et poussez vos modifications.

> [!NOTE]
>
> Il peut arriver que la vérification des URL échoue même si le lien est accessible. Cela peut être dû à plusieurs raisons, notamment :
>
> - **Restrictions réseau :** Les serveurs GitHub Actions peuvent avoir des restrictions réseau empêchant l’accès à certaines URL.
> - **Problèmes de délai d’attente :** Les URL qui mettent trop de temps à répondre peuvent déclencher une erreur de timeout dans le workflow.
> - **Problèmes temporaires de serveur :** Des interruptions ou maintenances temporaires peuvent rendre une URL indisponible lors de la validation.

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçons d'assurer l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle humaine est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.