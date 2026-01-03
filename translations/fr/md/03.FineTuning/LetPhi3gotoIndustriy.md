<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "743d7e9cb9c4e8ea642d77bee657a7fa",
  "translation_date": "2025-07-17T09:50:50+00:00",
  "source_file": "md/03.FineTuning/LetPhi3gotoIndustriy.md",
  "language_code": "fr"
}
-->
# **Faites de Phi-3 un expert de l'industrie**

Pour intégrer le modèle Phi-3 dans un secteur industriel, il est nécessaire d’ajouter des données métier spécifiques à ce secteur au modèle Phi-3. Nous avons deux options différentes : la première est le RAG (Retrieval Augmented Generation) et la seconde est le Fine Tuning.

## **RAG vs Fine-Tuning**

### **Retrieval Augmented Generation**

Le RAG combine la récupération de données et la génération de texte. Les données structurées et non structurées de l’entreprise sont stockées dans une base de données vectorielle. Lorsqu’on recherche un contenu pertinent, un résumé et un contenu associés sont extraits pour former un contexte, puis la capacité de complétion textuelle du LLM/SLM est utilisée pour générer du contenu.

### **Fine-tuning**

Le fine-tuning consiste à améliorer un modèle existant. Il ne nécessite pas de repartir de l’algorithme du modèle, mais il faut accumuler continuellement des données. Si vous souhaitez une terminologie et une expression linguistique plus précises dans les applications industrielles, le fine-tuning est un meilleur choix. En revanche, si vos données évoluent fréquemment, le fine-tuning peut devenir complexe.

### **Comment choisir**

1. Si notre réponse nécessite l’introduction de données externes, le RAG est le meilleur choix.

2. Si vous avez besoin d’une sortie stable et précise des connaissances industrielles, le fine-tuning sera une bonne option. Le RAG privilégie la récupération de contenu pertinent mais peut ne pas toujours saisir les nuances spécialisées.

3. Le fine-tuning requiert un jeu de données de haute qualité, et s’il s’agit d’un petit volume de données, cela ne fera pas une grande différence. Le RAG est plus flexible.

4. Le fine-tuning est une boîte noire, une sorte de métaphysique, et il est difficile de comprendre son mécanisme interne. En revanche, le RAG facilite la traçabilité des sources de données, ce qui permet de corriger efficacement les hallucinations ou erreurs de contenu et offre une meilleure transparence.

### **Scénarios**

1. Les secteurs verticaux nécessitant un vocabulaire et des expressions professionnelles spécifiques, ***le Fine-tuning*** sera le meilleur choix.

2. Pour un système de questions-réponses impliquant la synthèse de différents points de connaissance, ***le RAG*** sera le meilleur choix.

3. La combinaison d’un flux métier automatisé, ***RAG + Fine-tuning*** est la meilleure option.

## **Comment utiliser le RAG**

![rag](../../../../translated_images/rag.2014adc59e6f6007.fr.png)

Une base de données vectorielle est un ensemble de données stockées sous forme mathématique. Les bases vectorielles facilitent la mémorisation des entrées précédentes par les modèles d’apprentissage automatique, permettant ainsi d’utiliser l’apprentissage automatique pour des cas d’usage tels que la recherche, les recommandations et la génération de texte. Les données peuvent être identifiées sur la base de mesures de similarité plutôt que de correspondances exactes, ce qui permet aux modèles informatiques de comprendre le contexte des données.

La base de données vectorielle est la clé pour réaliser le RAG. Nous pouvons convertir les données en stockage vectoriel via des modèles vectoriels tels que text-embedding-3, jina-ai-embedding, etc.

En savoir plus sur la création d’une application RAG [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?WT.mc_id=aiml-138114-kinfeylo)

## **Comment utiliser le Fine-tuning**

Les algorithmes couramment utilisés en Fine-tuning sont Lora et QLora. Comment choisir ?
- [En savoir plus avec ce notebook d’exemple](../../../../code/04.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Exemple de script Python FineTuning](../../../../code/04.Finetuning/FineTrainingScript.py)

### **Lora et QLora**

![lora](../../../../translated_images/qlora.e6446c988ee04ca0.fr.png)

LoRA (Low-Rank Adaptation) et QLoRA (Quantized Low-Rank Adaptation) sont deux techniques utilisées pour affiner les grands modèles de langage (LLM) via le Parameter Efficient Fine Tuning (PEFT). Les techniques PEFT sont conçues pour entraîner les modèles de manière plus efficace que les méthodes traditionnelles.  
LoRA est une technique de fine-tuning autonome qui réduit l’empreinte mémoire en appliquant une approximation de faible rang à la matrice de mise à jour des poids. Elle offre des temps d’entraînement rapides tout en maintenant des performances proches des méthodes traditionnelles de fine-tuning.

QLoRA est une version étendue de LoRA qui intègre des techniques de quantification pour réduire encore plus l’utilisation mémoire. QLoRA quantifie la précision des paramètres de poids du LLM pré-entraîné à une précision 4 bits, ce qui est plus économe en mémoire que LoRA. Cependant, l’entraînement avec QLoRA est environ 30 % plus lent que celui avec LoRA en raison des étapes supplémentaires de quantification et de déquantification.

QLoRA utilise LoRA comme accessoire pour corriger les erreurs introduites lors de la quantification. QLoRA permet le fine-tuning de modèles massifs avec des milliards de paramètres sur des GPU relativement petits et disponibles. Par exemple, QLoRA peut affiner un modèle de 70 milliards de paramètres nécessitant 36 GPU avec seulement 2...

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.