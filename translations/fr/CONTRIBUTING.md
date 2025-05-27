<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "90d0d072cf26ccc1f271a580d3e45d70",
  "translation_date": "2025-05-27T02:39:50+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "fr"
}
-->
# Contribuer

Ce projet accepte les contributions et suggestions. La plupart des contributions nécessitent que vous acceptiez un  
Contrat de Licence de Contributeur (CLA) déclarant que vous avez le droit, et que vous accordez effectivement,  
les droits d’utilisation de votre contribution. Pour plus de détails, consultez [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com)

Lorsque vous soumettez une pull request, un bot CLA déterminera automatiquement si vous devez fournir  
un CLA et annotera la PR en conséquence (par exemple, vérification de statut, commentaire). Suivez simplement les instructions  
du bot. Vous n’aurez à le faire qu’une seule fois pour tous les dépôts utilisant notre CLA.

## Code de Conduite

Ce projet a adopté le [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).  
Pour plus d’informations, consultez la [FAQ sur le Code de Conduite](https://opensource.microsoft.com/codeofconduct/faq/) ou contactez [opencode@microsoft.com](mailto:opencode@microsoft.com) pour toute question ou remarque supplémentaire.

## Précautions pour la création d’issues

Merci de ne pas ouvrir d’issues GitHub pour des questions générales de support, car la liste GitHub doit être utilisée pour les demandes de fonctionnalités et les rapports de bugs.  
Cela nous permet de mieux suivre les problèmes ou bugs réels liés au code et de séparer la discussion générale du code lui-même.

## Comment Contribuer

### Directives pour les Pull Requests

Lorsque vous soumettez une pull request (PR) au dépôt Phi-3 CookBook, veuillez suivre les directives suivantes :

- **Forker le dépôt** : Toujours forker le dépôt sur votre propre compte avant d’apporter vos modifications.

- **Pull requests séparées (PR)** :  
  - Soumettez chaque type de modification dans une PR distincte. Par exemple, les corrections de bugs et les mises à jour de documentation doivent être soumises dans des PR séparées.  
  - Les corrections de fautes de frappe et les petites mises à jour de documentation peuvent être combinées dans une seule PR lorsque cela est approprié.

- **Gérer les conflits de fusion** : Si votre pull request présente des conflits de fusion, mettez à jour votre branche locale `main` pour qu’elle reflète le dépôt principal avant d’apporter vos modifications.

- **Soumissions de traduction** : Lors de la soumission d’une PR de traduction, assurez-vous que le dossier de traduction contient les traductions pour tous les fichiers du dossier original.

### Directives de rédaction

Pour assurer la cohérence de tous les documents, merci de suivre les directives suivantes :

- **Formatage des URL** : Entourez toutes les URL de crochets suivis de parenthèses, sans espaces supplémentaires autour ou à l’intérieur. Par exemple : `[example](https://www.microsoft.com)`.

- **Liens relatifs** : Utilisez `./` pour les liens relatifs pointant vers des fichiers ou dossiers dans le répertoire courant, et `../` pour ceux dans un répertoire parent. Par exemple : `[example](../../path/to/file)` ou `[example](../../../path/to/file)`.

- **Locales non spécifiques à un pays** : Assurez-vous que vos liens n’incluent pas de locales spécifiques à un pays. Par exemple, évitez `/en-us/` ou `/en/`.

- **Stockage des images** : Stockez toutes les images dans le dossier `./imgs`.

- **Noms descriptifs pour les images** : Nommez les images de manière descriptive en utilisant des caractères anglais, des chiffres et des tirets. Par exemple : `example-image.jpg`.

## Workflows GitHub

Lorsque vous soumettez une pull request, les workflows suivants sont déclenchés pour valider les modifications. Suivez les instructions ci-dessous pour vous assurer que votre pull request passe les vérifications du workflow :

- [Check Broken Relative Paths](../..)  
- [Check URLs Don't Have Locale](../..)

### Check Broken Relative Paths

Ce workflow vérifie que tous les chemins relatifs dans vos fichiers sont corrects.

1. Pour vous assurer que vos liens fonctionnent correctement, effectuez les tâches suivantes dans VS Code :  
    - Survolez un lien dans vos fichiers.  
    - Appuyez sur **Ctrl + Clic** pour naviguer vers le lien.  
    - Si vous cliquez sur un lien qui ne fonctionne pas localement, cela déclenchera le workflow et ne fonctionnera pas sur GitHub.

1. Pour corriger ce problème, effectuez les tâches suivantes en utilisant les suggestions de chemin proposées par VS Code :  
    - Tapez `./` ou `../`.  
    - VS Code vous proposera des options en fonction de ce que vous avez tapé.  
    - Suivez le chemin en cliquant sur le fichier ou dossier souhaité pour vérifier que votre chemin est correct.

Une fois le chemin relatif correct ajouté, enregistrez et poussez vos modifications.

### Check URLs Don't Have Locale

Ce workflow vérifie qu’aucune URL web ne contient une locale spécifique à un pays. Comme ce dépôt est accessible globalement, il est important que les URL ne contiennent pas la locale de votre pays.

1. Pour vérifier que vos URL ne contiennent pas de locales pays, effectuez les tâches suivantes :

    - Cherchez des textes comme `/en-us/`, `/en/`, ou toute autre locale linguistique dans les URL.  
    - Si ces éléments ne sont pas présents dans vos URL, vous passerez cette vérification.

1. Pour corriger ce problème, effectuez les tâches suivantes :  
    - Ouvrez le fichier dont le chemin est indiqué par le workflow.  
    - Supprimez la locale pays des URL.

Une fois la locale pays supprimée, enregistrez et poussez vos modifications.

### Check Broken Urls

Ce workflow vérifie que toutes les URL web dans vos fichiers fonctionnent et renvoient un code de statut 200.

1. Pour vérifier que vos URL fonctionnent correctement, effectuez les tâches suivantes :  
    - Vérifiez le statut des URL dans vos fichiers.

2. Pour corriger les URL cassées, effectuez les tâches suivantes :  
    - Ouvrez le fichier contenant l’URL cassée.  
    - Mettez à jour l’URL avec la bonne adresse.

Une fois les URL corrigées, enregistrez et poussez vos modifications.

> [!NOTE]  
>  
> Il peut arriver que la vérification des URL échoue même si le lien est accessible. Cela peut être dû à plusieurs raisons, notamment :  
>  
> - **Restrictions réseau :** Les serveurs GitHub actions peuvent avoir des restrictions réseau empêchant l’accès à certaines URL.  
> - **Problèmes de délai d’attente :** Les URL qui mettent trop de temps à répondre peuvent déclencher une erreur de timeout dans le workflow.  
> - **Problèmes temporaires de serveur :** Des interruptions occasionnelles ou des maintenances peuvent rendre une URL temporairement indisponible lors de la validation.

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçons d'assurer l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l'utilisation de cette traduction.