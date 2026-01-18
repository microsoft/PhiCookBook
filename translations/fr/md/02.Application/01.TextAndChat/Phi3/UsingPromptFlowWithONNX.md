<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "92e7dac1e5af0dd7c94170fdaf6860fe",
  "translation_date": "2025-07-17T02:56:23+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md",
  "language_code": "fr"
}
-->
# Utilisation du GPU Windows pour créer une solution Prompt flow avec Phi-3.5-Instruct ONNX

Le document suivant est un exemple montrant comment utiliser PromptFlow avec ONNX (Open Neural Network Exchange) pour développer des applications IA basées sur les modèles Phi-3.

PromptFlow est une suite d’outils de développement conçue pour simplifier le cycle complet de création d’applications IA basées sur des LLM (Large Language Model), de l’idéation et du prototypage jusqu’aux tests et à l’évaluation.

En intégrant PromptFlow avec ONNX, les développeurs peuvent :

- Optimiser les performances du modèle : tirer parti d’ONNX pour une inférence et un déploiement efficaces.
- Simplifier le développement : utiliser PromptFlow pour gérer le flux de travail et automatiser les tâches répétitives.
- Améliorer la collaboration : faciliter le travail d’équipe grâce à un environnement de développement unifié.

**Prompt flow** est une suite d’outils de développement conçue pour fluidifier le cycle complet de création d’applications IA basées sur des LLM, de l’idéation, du prototypage, des tests, de l’évaluation jusqu’au déploiement en production et à la surveillance. Il rend l’ingénierie des prompts beaucoup plus simple et vous permet de créer des applications LLM de qualité production.

Prompt flow peut se connecter à OpenAI, Azure OpenAI Service, ainsi qu’à des modèles personnalisables (Huggingface, LLM/SLM locaux). Nous espérons déployer le modèle ONNX quantifié de Phi-3.5 dans des applications locales. Prompt flow peut nous aider à mieux planifier notre activité et à réaliser des solutions locales basées sur Phi-3.5. Dans cet exemple, nous allons combiner la bibliothèque ONNX Runtime GenAI pour compléter la solution Prompt flow basée sur un GPU Windows.

## **Installation**

### **ONNX Runtime GenAI pour GPU Windows**

Lisez ce guide pour configurer ONNX Runtime GenAI pour GPU Windows [cliquez ici](./ORTWindowGPUGuideline.md)

### **Configurer Prompt flow dans VSCode**

1. Installez l’extension Prompt flow pour VS Code

![pfvscode](../../../../../../translated_images/fr/pfvscode.eff93dfc66a42cbe.webp)

2. Après avoir installé l’extension Prompt flow pour VS Code, cliquez sur l’extension, puis choisissez **Installation dependencies** et suivez ce guide pour installer le SDK Prompt flow dans votre environnement

![pfsetup](../../../../../../translated_images/fr/pfsetup.b46e93096f5a254f.webp)

3. Téléchargez le [Code d’exemple](../../../../../../code/09.UpdateSamples/Aug/pf/onnx_inference_pf) et ouvrez cet exemple avec VS Code

![pfsample](../../../../../../translated_images/fr/pfsample.8d89e70584ffe7c4.webp)

4. Ouvrez **flow.dag.yaml** pour sélectionner votre environnement Python

![pfdag](../../../../../../translated_images/fr/pfdag.264a77f7366458ff.webp)

   Ouvrez **chat_phi3_ort.py** pour modifier l’emplacement de votre modèle Phi-3.5-instruct ONNX

![pfphi](../../../../../../translated_images/fr/pfphi.72da81d74244b45f.webp)

5. Lancez votre prompt flow pour tester

Ouvrez **flow.dag.yaml** et cliquez sur l’éditeur visuel

![pfv](../../../../../../translated_images/fr/pfv.ba8a81f34b20f603.webp)

Après avoir cliqué, lancez-le pour tester

![pfflow](../../../../../../translated_images/fr/pfflow.4e1135a089b1ce1b.webp)

1. Vous pouvez exécuter un batch dans le terminal pour vérifier plus de résultats


```bash

pf run create --file batch_run.yaml --stream --name 'Your eval qa name'    

```

Vous pouvez consulter les résultats dans votre navigateur par défaut


![pfresult](../../../../../../translated_images/fr/pfresult.c22c826f8062d7cb.webp)

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle humaine est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.