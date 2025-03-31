<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e4e010400c2918557b36bb932a14004c",
  "translation_date": "2025-03-27T15:37:16+00:00",
  "source_file": "md\\03.FineTuning\\FineTuning_vs_RAG.md",
  "language_code": "fr"
}
-->
## Ajustement fin vs RAG

## Génération augmentée par récupération

RAG combine la récupération de données et la génération de texte. Les données structurées et non structurées de l'entreprise sont stockées dans une base de données vectorielle. Lorsqu'on recherche un contenu pertinent, un résumé et des informations connexes sont identifiés pour former un contexte, puis la capacité de complétion de texte de LLM/SLM est utilisée pour générer du contenu.

## Processus RAG
![FinetuningvsRAG](../../../../translated_images/rag.36e7cb856f120334d577fde60c6a5d7c5eecae255dac387669303d30b4b3efa4.fr.png)

## Ajustement fin
L'ajustement fin repose sur l'amélioration d'un modèle existant. Il n'est pas nécessaire de repartir de zéro avec l'algorithme du modèle, mais il faut accumuler des données de manière continue. Si vous souhaitez des terminologies plus précises et une expression linguistique adaptée aux applications industrielles, l'ajustement fin est une meilleure option. Cependant, si vos données changent fréquemment, l'ajustement fin peut devenir complexe.

## Comment choisir
Si notre réponse nécessite l'intégration de données externes, RAG est le meilleur choix.

Si vous devez produire des connaissances industrielles stables et précises, l'ajustement fin sera une bonne option. RAG privilégie la récupération de contenu pertinent, mais il peut parfois manquer de nuances spécialisées.

L'ajustement fin nécessite un ensemble de données de haute qualité, et si les données sont limitées à une petite plage, la différence sera minime. RAG est plus flexible.  
L'ajustement fin est une boîte noire, une sorte de métaphysique, et il est difficile de comprendre son mécanisme interne. En revanche, RAG facilite l'identification de la source des données, permettant ainsi de mieux corriger les hallucinations ou les erreurs de contenu et d'offrir une meilleure transparence.

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.