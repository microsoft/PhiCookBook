<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bcf5dd7031db0031abdb9dd0c05ba118",
  "translation_date": "2025-07-16T20:54:46+00:00",
  "source_file": "md/01.Introduction/03/Local_Server_Inference.md",
  "language_code": "fr"
}
-->
# **Inférence Phi-3 sur serveur local**

Nous pouvons déployer Phi-3 sur un serveur local. Les utilisateurs peuvent choisir les solutions [Ollama](https://ollama.com) ou [LM Studio](https://llamaedge.com), ou bien écrire leur propre code. Vous pouvez connecter les services locaux de Phi-3 via [Semantic Kernel](https://github.com/microsoft/semantic-kernel?WT.mc_id=aiml-138114-kinfeylo) ou [Langchain](https://www.langchain.com/) pour créer des applications Copilot.

## **Utiliser Semantic Kernel pour accéder à Phi-3-mini**

Dans l’application Copilot, nous créons des applications via Semantic Kernel / LangChain. Ce type de framework applicatif est généralement compatible avec Azure OpenAI Service / modèles OpenAI, et peut aussi prendre en charge des modèles open source sur Hugging Face ainsi que des modèles locaux. Que faire si l’on souhaite utiliser Semantic Kernel pour accéder à Phi-3-mini ? En prenant .NET comme exemple, on peut le combiner avec le Hugging Face Connector dans Semantic Kernel. Par défaut, il correspond à l’id du modèle sur Hugging Face (la première utilisation télécharge le modèle depuis Hugging Face, ce qui prend du temps). Vous pouvez aussi vous connecter au service local que vous avez construit. Entre les deux, nous recommandons la seconde option car elle offre une plus grande autonomie, notamment pour les applications en entreprise.

![sk](../../../../../translated_images/fr/sk.d03785c25edc6d44.png)

D’après la figure, accéder aux services locaux via Semantic Kernel permet de se connecter facilement au serveur de modèle Phi-3-mini auto-hébergé. Voici le résultat d’exécution :

![skrun](../../../../../translated_images/fr/skrun.5aafc1e7197dca20.png)

***Exemple de code*** https://github.com/kinfey/Phi3MiniSamples/tree/main/semantickernel

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.