<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "92e7dac1e5af0dd7c94170fdaf6860fe",
  "translation_date": "2025-05-07T13:58:50+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md",
  "language_code": "fr"
}
-->
# Utiliser le GPU Windows pour créer une solution Prompt flow avec Phi-3.5-Instruct ONNX

Le document suivant est un exemple montrant comment utiliser PromptFlow avec ONNX (Open Neural Network Exchange) pour développer des applications d’IA basées sur les modèles Phi-3.

PromptFlow est une suite d’outils de développement conçue pour simplifier le cycle complet de création d’applications IA basées sur les LLM (Large Language Model), de l’idéation et du prototypage jusqu’aux tests et à l’évaluation.

En intégrant PromptFlow avec ONNX, les développeurs peuvent :

- Optimiser les performances du modèle : tirer parti d’ONNX pour une inférence et un déploiement efficaces.
- Simplifier le développement : utiliser PromptFlow pour gérer le workflow et automatiser les tâches répétitives.
- Favoriser la collaboration : faciliter une meilleure collaboration entre les membres de l’équipe grâce à un environnement de développement unifié.

**Prompt flow** est une suite d’outils de développement conçue pour fluidifier le cycle complet de création d’applications IA basées sur les LLM, de l’idéation, du prototypage, des tests et de l’évaluation jusqu’au déploiement en production et à la surveillance. Il rend l’ingénierie des prompts beaucoup plus simple et vous permet de créer des applications LLM de qualité production.

Prompt flow peut se connecter à OpenAI, Azure OpenAI Service, ainsi qu’à des modèles personnalisables (Huggingface, LLM/SLM locaux). Nous espérons déployer le modèle ONNX quantifié de Phi-3.5 dans des applications locales. Prompt flow peut nous aider à mieux planifier notre activité et à réaliser des solutions locales basées sur Phi-3.5. Dans cet exemple, nous allons combiner la bibliothèque ONNX Runtime GenAI pour compléter la solution Prompt flow basée sur un GPU Windows.

## **Installation**

### **ONNX Runtime GenAI pour GPU Windows**

Lisez cette documentation pour configurer ONNX Runtime GenAI pour GPU Windows [cliquer ici](./ORTWindowGPUGuideline.md)

### **Configurer Prompt flow dans VSCode**

1. Installer l’extension Prompt flow pour VS Code

![pfvscode](../../../../../../translated_images/pfvscode.eff93dfc66a42cbef699fc16fa48f3ed3a23361875a3362037d026896395a00d.fr.png)

2. Après avoir installé l’extension Prompt flow pour VS Code, cliquez sur l’extension, puis choisissez **Installation dependencies** et suivez ce guide pour installer le SDK Prompt flow dans votre environnement

![pfsetup](../../../../../../translated_images/pfsetup.b46e93096f5a254f74e8b74ce2be7047ce963ef573d755ec897eb1b78cb9c954.fr.png)

3. Téléchargez le [code d’exemple](../../../../../../code/09.UpdateSamples/Aug/pf/onnx_inference_pf) et ouvrez cet exemple avec VS Code

![pfsample](../../../../../../translated_images/pfsample.8d89e70584ffe7c4dba182513e3148a989e552c3b8e4948567a6b806b5ae1845.fr.png)

4. Ouvrez **flow.dag.yaml** pour sélectionner votre environnement Python

![pfdag](../../../../../../translated_images/pfdag.264a77f7366458ff850a76ae949226391ea382856d543ef9da4b92096aff7e4b.fr.png)

   Ouvrez **chat_phi3_ort.py** pour modifier l’emplacement de votre modèle Phi-3.5-instruct ONNX

![pfphi](../../../../../../translated_images/pfphi.72da81d74244b45fc78cdfeeb8c7fbd9e7cd610bf2f96814dbade6a4a2dfad7e.fr.png)

5. Lancez votre prompt flow pour tester

Ouvrez **flow.dag.yaml** et cliquez sur l’éditeur visuel

![pfv](../../../../../../translated_images/pfv.ba8a81f34b20f603cccee3fe91e94113792ed6f5af28f76ab08e1a0b3e77b33b.fr.png)

Après avoir cliqué, exécutez-le pour tester

![pfflow](../../../../../../translated_images/pfflow.4e1135a089b1ce1b6348b59edefdb6333e5729b54c8e57f9039b7f9463e68fbd.fr.png)

1. Vous pouvez exécuter un batch dans le terminal pour obtenir plus de résultats


```bash

pf run create --file batch_run.yaml --stream --name 'Your eval qa name'    

```

Vous pouvez consulter les résultats dans votre navigateur par défaut


![pfresult](../../../../../../translated_images/pfresult.c22c826f8062d7cbe871cff35db4a013dcfefc13fafe5da6710a8549a96a4ceb.fr.png)

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçons d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.