# Évaluer le modèle Phi-3 / Phi-3.5 affiné dans Azure AI Foundry en se concentrant sur les principes d’IA responsable de Microsoft

Cet exemple de bout en bout (E2E) est basé sur le guide « [Evaluate Fine-tuned Phi-3 / 3.5 Models in Azure AI Foundry Focusing on Microsoft's Responsible AI](https://techcommunity.microsoft.com/blog/educatordeveloperblog/evaluate-fine-tuned-phi-3--3-5-models-in-azure-ai-studio-focusing-on-microsofts-/4227850?WT.mc_id=aiml-137032-kinfeylo) » de la communauté technique Microsoft.

## Vue d’ensemble

### Comment évaluer la sécurité et les performances d’un modèle Phi-3 / Phi-3.5 affiné dans Azure AI Foundry ?

L’affinage d’un modèle peut parfois entraîner des réponses inattendues ou indésirables. Pour garantir que le modèle reste sûr et efficace, il est important d’évaluer son potentiel à générer du contenu nuisible ainsi que sa capacité à produire des réponses précises, pertinentes et cohérentes. Dans ce tutoriel, vous apprendrez à évaluer la sécurité et les performances d’un modèle Phi-3 / Phi-3.5 affiné, intégré avec Prompt flow dans Azure AI Foundry.

Voici le processus d’évaluation d’Azure AI Foundry.

![Architecture du tutoriel.](../../../../../../translated_images/fr/architecture.10bec55250f5d6a4.webp)

*Source de l’image : [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> Pour plus d’informations détaillées et pour explorer d’autres ressources sur Phi-3 / Phi-3.5, veuillez consulter le [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723).

### Prérequis

- [Python](https://www.python.org/downloads)
- [Abonnement Azure](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- Modèle Phi-3 / Phi-3.5 affiné

### Table des matières

1. [**Scénario 1 : Introduction à l’évaluation Prompt flow d’Azure AI Foundry**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Introduction à l’évaluation de la sécurité](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Introduction à l’évaluation des performances](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [**Scénario 2 : Évaluation du modèle Phi-3 / Phi-3.5 dans Azure AI Foundry**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Avant de commencer](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Déployer Azure OpenAI pour évaluer le modèle Phi-3 / Phi-3.5](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Évaluer le modèle Phi-3 / Phi-3.5 affiné avec l’évaluation Prompt flow d’Azure AI Foundry](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [Félicitations !](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## **Scénario 1 : Introduction à l’évaluation Prompt flow d’Azure AI Foundry**

### Introduction à l’évaluation de la sécurité

Pour garantir que votre modèle d’IA soit éthique et sûr, il est crucial de l’évaluer selon les principes d’IA responsable de Microsoft. Dans Azure AI Foundry, les évaluations de sécurité vous permettent d’analyser la vulnérabilité de votre modèle aux attaques de jailbreak ainsi que son potentiel à générer du contenu nuisible, ce qui est directement aligné avec ces principes.

![Évaluation de la sécurité.](../../../../../../translated_images/fr/safety-evaluation.083586ec88dfa950.webp)

*Source de l’image : [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Principes d’IA responsable de Microsoft

Avant de commencer les étapes techniques, il est essentiel de comprendre les principes d’IA responsable de Microsoft, un cadre éthique conçu pour guider le développement, le déploiement et l’exploitation responsables des systèmes d’IA. Ces principes orientent la conception, le développement et le déploiement responsables des systèmes d’IA, garantissant que les technologies d’IA sont construites de manière équitable, transparente et inclusive. Ces principes sont la base pour évaluer la sécurité des modèles d’IA.

Les principes d’IA responsable de Microsoft incluent :

- **Équité et inclusion** : Les systèmes d’IA doivent traiter tout le monde de manière équitable et éviter d’affecter différemment des groupes de personnes dans des situations similaires. Par exemple, lorsque les systèmes d’IA fournissent des conseils sur des traitements médicaux, des demandes de prêt ou des emplois, ils doivent faire les mêmes recommandations à tous ceux qui ont des symptômes, des situations financières ou des qualifications professionnelles similaires.

- **Fiabilité et sécurité** : Pour instaurer la confiance, il est crucial que les systèmes d’IA fonctionnent de manière fiable, sûre et cohérente. Ces systèmes doivent pouvoir fonctionner comme prévu, répondre de manière sécurisée à des conditions imprévues et résister à toute manipulation malveillante. Leur comportement et la variété des conditions qu’ils peuvent gérer reflètent la gamme de situations et de circonstances anticipées par les développeurs lors de la conception et des tests.

- **Transparence** : Lorsque les systèmes d’IA aident à prendre des décisions ayant un impact important sur la vie des personnes, il est essentiel que ces dernières comprennent comment ces décisions ont été prises. Par exemple, une banque peut utiliser un système d’IA pour décider si une personne est solvable. Une entreprise peut utiliser un système d’IA pour déterminer les candidats les plus qualifiés à embaucher.

- **Confidentialité et sécurité** : À mesure que l’IA se généralise, la protection de la vie privée et la sécurisation des informations personnelles et professionnelles deviennent de plus en plus importantes et complexes. Avec l’IA, la confidentialité et la sécurité des données nécessitent une attention particulière car l’accès aux données est essentiel pour que les systèmes d’IA fassent des prédictions et des décisions précises et éclairées concernant les personnes.

- **Responsabilité** : Les personnes qui conçoivent et déploient des systèmes d’IA doivent être responsables du fonctionnement de leurs systèmes. Les organisations doivent s’appuyer sur les normes de l’industrie pour développer des règles de responsabilité. Ces règles peuvent garantir que les systèmes d’IA ne soient pas l’autorité finale sur toute décision affectant la vie des personnes. Elles peuvent aussi garantir que les humains conservent un contrôle significatif sur des systèmes d’IA autrement très autonomes.

![Remplir le hub.](../../../../../../translated_images/fr/responsibleai2.c07ef430113fad8c.webp)

*Source de l’image : [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> Pour en savoir plus sur les principes d’IA responsable de Microsoft, consultez la page [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723).

#### Indicateurs de sécurité

Dans ce tutoriel, vous évaluerez la sécurité du modèle Phi-3 affiné en utilisant les indicateurs de sécurité d’Azure AI Foundry. Ces indicateurs vous aident à mesurer le potentiel du modèle à générer du contenu nuisible ainsi que sa vulnérabilité aux attaques de jailbreak. Les indicateurs de sécurité comprennent :

- **Contenu lié à l’automutilation** : Évalue si le modèle a tendance à produire du contenu lié à l’automutilation.
- **Contenu haineux et injuste** : Évalue si le modèle a tendance à produire du contenu haineux ou injuste.
- **Contenu violent** : Évalue si le modèle a tendance à produire du contenu violent.
- **Contenu sexuel** : Évalue si le modèle a tendance à produire du contenu sexuel inapproprié.

L’évaluation de ces aspects garantit que le modèle d’IA ne génère pas de contenu nuisible ou offensant, en accord avec les valeurs sociétales et les normes réglementaires.

![Évaluer selon la sécurité.](../../../../../../translated_images/fr/evaluate-based-on-safety.c5df819f5b0bfc07.webp)

### Introduction à l’évaluation des performances

Pour s’assurer que votre modèle d’IA fonctionne comme prévu, il est important d’évaluer ses performances à l’aide d’indicateurs de performance. Dans Azure AI Foundry, les évaluations de performance vous permettent d’analyser l’efficacité de votre modèle à générer des réponses précises, pertinentes et cohérentes.

![Évaluation de la sécurité.](../../../../../../translated_images/fr/performance-evaluation.48b3e7e01a098740.webp)

*Source de l’image : [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Indicateurs de performance

Dans ce tutoriel, vous évaluerez les performances du modèle Phi-3 / Phi-3.5 affiné en utilisant les indicateurs de performance d’Azure AI Foundry. Ces indicateurs vous aident à mesurer l’efficacité du modèle à générer des réponses précises, pertinentes et cohérentes. Les indicateurs de performance comprennent :

- **Fondement** : Évalue dans quelle mesure les réponses générées sont alignées avec les informations de la source d’entrée.
- **Pertinence** : Évalue la pertinence des réponses générées par rapport aux questions posées.
- **Cohérence** : Évalue la fluidité du texte généré, sa lecture naturelle et sa ressemblance avec un langage humain.
- **Fluidité** : Évalue la maîtrise linguistique du texte généré.
- **Similarité GPT** : Compare la réponse générée avec la vérité terrain pour mesurer la similarité.
- **Score F1** : Calcule le ratio de mots communs entre la réponse générée et les données sources.

Ces indicateurs vous aident à évaluer l’efficacité du modèle à produire des réponses précises, pertinentes et cohérentes.

![Évaluer selon la performance.](../../../../../../translated_images/fr/evaluate-based-on-performance.3e801c647c7554e8.webp)

## **Scénario 2 : Évaluation du modèle Phi-3 / Phi-3.5 dans Azure AI Foundry**

### Avant de commencer

Ce tutoriel fait suite aux articles de blog précédents, « [Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723) » et « [Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723) ». Dans ces articles, nous avons parcouru le processus d’affinage d’un modèle Phi-3 / Phi-3.5 dans Azure AI Foundry et son intégration avec Prompt flow.

Dans ce tutoriel, vous déploierez un modèle Azure OpenAI en tant qu’évaluateur dans Azure AI Foundry et l’utiliserez pour évaluer votre modèle Phi-3 / Phi-3.5 affiné.

Avant de commencer ce tutoriel, assurez-vous de disposer des prérequis suivants, comme décrit dans les tutoriels précédents :

1. Un jeu de données préparé pour évaluer le modèle Phi-3 / Phi-3.5 affiné.
1. Un modèle Phi-3 / Phi-3.5 affiné et déployé sur Azure Machine Learning.
1. Un Prompt flow intégré à votre modèle Phi-3 / Phi-3.5 affiné dans Azure AI Foundry.

> [!NOTE]
> Vous utiliserez le fichier *test_data.jsonl*, situé dans le dossier data du jeu de données **ULTRACHAT_200k** téléchargé dans les articles de blog précédents, comme jeu de données pour évaluer le modèle Phi-3 / Phi-3.5 affiné.

#### Intégrer le modèle Phi-3 / Phi-3.5 personnalisé avec Prompt flow dans Azure AI Foundry (approche code first)
> [!NOTE]  
> Si vous avez suivi l’approche low-code décrite dans « [Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723) », vous pouvez passer cet exercice et continuer avec le suivant.  
> Cependant, si vous avez suivi l’approche code-first décrite dans « [Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723) » pour affiner et déployer votre modèle Phi-3 / Phi-3.5, le processus de connexion de votre modèle à Prompt Flow est légèrement différent. Vous découvrirez ce processus dans cet exercice.
Pour continuer, vous devez intégrer votre modèle Phi-3 / Phi-3.5 affiné dans Prompt flow dans Azure AI Foundry.

#### Créer un Hub Azure AI Foundry

Vous devez créer un Hub avant de créer le Projet. Un Hub agit comme un Groupe de ressources, vous permettant d’organiser et de gérer plusieurs Projets au sein d’Azure AI Foundry.

1. Connectez-vous à [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Sélectionnez **All hubs** dans l’onglet latéral gauche.

1. Sélectionnez **+ New hub** dans le menu de navigation.

    ![Créer un hub.](../../../../../../translated_images/fr/create-hub.5be78fb1e21ffbf1.webp)

1. Effectuez les tâches suivantes :

    - Saisissez un **Nom du Hub**. Il doit être unique.
    - Sélectionnez votre **Abonnement** Azure.
    - Sélectionnez le **Groupe de ressources** à utiliser (créez-en un nouveau si nécessaire).
    - Sélectionnez la **Région** que vous souhaitez utiliser.
    - Sélectionnez le **Connect Azure AI Services** à utiliser (créez-en un nouveau si nécessaire).
    - Sélectionnez **Connect Azure AI Search** puis **Skip connecting**.

    ![Remplir le hub.](../../../../../../translated_images/fr/fill-hub.baaa108495c71e34.webp)

1. Sélectionnez **Next**.

#### Créer un projet Azure AI Foundry

1. Dans le Hub que vous avez créé, sélectionnez **All projects** dans l’onglet latéral gauche.

1. Sélectionnez **+ New project** dans le menu de navigation.

    ![Sélectionner nouveau projet.](../../../../../../translated_images/fr/select-new-project.cd31c0404088d7a3.webp)

1. Saisissez un **Nom du projet**. Il doit être unique.

    ![Créer un projet.](../../../../../../translated_images/fr/create-project.ca3b71298b90e420.webp)

1. Sélectionnez **Create a project**.

#### Ajouter une connexion personnalisée pour le modèle Phi-3 / Phi-3.5 affiné

Pour intégrer votre modèle Phi-3 / Phi-3.5 personnalisé avec Prompt flow, vous devez enregistrer le point de terminaison et la clé du modèle dans une connexion personnalisée. Cette configuration garantit l’accès à votre modèle Phi-3 / Phi-3.5 personnalisé dans Prompt flow.

#### Configurer la clé API et l’URI du point de terminaison du modèle Phi-3 / Phi-3.5 affiné

1. Rendez-vous sur [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Accédez à l’espace de travail Azure Machine Learning que vous avez créé.

1. Sélectionnez **Endpoints** dans l’onglet latéral gauche.

    ![Sélectionner les endpoints.](../../../../../../translated_images/fr/select-endpoints.ee7387ecd68bd18d.webp)

1. Sélectionnez le point de terminaison que vous avez créé.

    ![Sélectionner le point de terminaison créé.](../../../../../../translated_images/fr/select-endpoint-created.9f63af5e4cf98b2e.webp)

1. Sélectionnez **Consume** dans le menu de navigation.

1. Copiez votre **REST endpoint** et votre **Primary key**.

    ![Copier la clé API et l’URI du point de terminaison.](../../../../../../translated_images/fr/copy-endpoint-key.0650c3786bd646ab.webp)

#### Ajouter la connexion personnalisée

1. Rendez-vous sur [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Accédez au projet Azure AI Foundry que vous avez créé.

1. Dans le projet que vous avez créé, sélectionnez **Settings** dans l’onglet latéral gauche.

1. Sélectionnez **+ New connection**.

    ![Sélectionner nouvelle connexion.](../../../../../../translated_images/fr/select-new-connection.fa0f35743758a74b.webp)

1. Sélectionnez **Custom keys** dans le menu de navigation.

    ![Sélectionner clés personnalisées.](../../../../../../translated_images/fr/select-custom-keys.5a3c6b25580a9b67.webp)

1. Effectuez les tâches suivantes :

    - Sélectionnez **+ Add key value pairs**.
    - Pour le nom de la clé, saisissez **endpoint** et collez le point de terminaison copié depuis Azure ML Studio dans le champ valeur.
    - Sélectionnez à nouveau **+ Add key value pairs**.
    - Pour le nom de la clé, saisissez **key** et collez la clé copiée depuis Azure ML Studio dans le champ valeur.
    - Après avoir ajouté les clés, cochez **is secret** pour empêcher que la clé soit exposée.

    ![Ajouter la connexion.](../../../../../../translated_images/fr/add-connection.ac7f5faf8b10b0df.webp)

1. Sélectionnez **Add connection**.

#### Créer un Prompt flow

Vous avez ajouté une connexion personnalisée dans Azure AI Foundry. Maintenant, créons un Prompt flow en suivant les étapes ci-dessous. Ensuite, vous connecterez ce Prompt flow à la connexion personnalisée pour utiliser le modèle affiné dans le Prompt flow.

1. Accédez au projet Azure AI Foundry que vous avez créé.

1. Sélectionnez **Prompt flow** dans l’onglet latéral gauche.

1. Sélectionnez **+ Create** dans le menu de navigation.

    ![Sélectionner Promptflow.](../../../../../../translated_images/fr/select-promptflow.18ff2e61ab9173eb.webp)

1. Sélectionnez **Chat flow** dans le menu de navigation.

    ![Sélectionner chat flow.](../../../../../../translated_images/fr/select-flow-type.28375125ec9996d3.webp)

1. Saisissez un **Nom de dossier** à utiliser.

    ![Saisir le nom du dossier.](../../../../../../translated_images/fr/enter-name.02ddf8fb840ad430.webp)

1. Sélectionnez **Create**.

#### Configurer Prompt flow pour discuter avec votre modèle Phi-3 / Phi-3.5 personnalisé

Vous devez intégrer le modèle Phi-3 / Phi-3.5 affiné dans un Prompt flow. Cependant, le Prompt flow existant fourni n’est pas conçu pour cela. Vous devez donc repenser le Prompt flow pour permettre l’intégration du modèle personnalisé.

1. Dans le Prompt flow, effectuez les tâches suivantes pour reconstruire le flux existant :

    - Sélectionnez **Raw file mode**.
    - Supprimez tout le code existant dans le fichier *flow.dag.yml*.
    - Ajoutez le code suivant dans *flow.dag.yml*.

        ```yml
        inputs:
          input_data:
            type: string
            default: "Who founded Microsoft?"

        outputs:
          answer:
            type: string
            reference: ${integrate_with_promptflow.output}

        nodes:
        - name: integrate_with_promptflow
          type: python
          source:
            type: code
            path: integrate_with_promptflow.py
          inputs:
            input_data: ${inputs.input_data}
        ```

    - Sélectionnez **Save**.

    ![Sélectionner le mode fichier brut.](../../../../../../translated_images/fr/select-raw-file-mode.06c1eca581ce4f53.webp)

1. Ajoutez le code suivant dans *integrate_with_promptflow.py* pour utiliser le modèle Phi-3 / Phi-3.5 personnalisé dans Prompt flow.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Logging setup
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG
    )
    logger = logging.getLogger(__name__)

    def query_phi3_model(input_data: str, connection: CustomConnection) -> str:
        """
        Send a request to the Phi-3 / Phi-3.5 model endpoint with the given input data using Custom Connection.
        """

        # "connection" is the name of the Custom Connection, "endpoint", "key" are the keys in the Custom Connection
        endpoint_url = connection.endpoint
        api_key = connection.key

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
    data = {
        "input_data": [input_data],
        "params": {
            "temperature": 0.7,
            "max_new_tokens": 128,
            "do_sample": True,
            "return_full_text": True
            }
        }
        try:
            response = requests.post(endpoint_url, json=data, headers=headers)
            response.raise_for_status()
            
            # Log the full JSON response
            logger.debug(f"Full JSON response: {response.json()}")

            result = response.json()["output"]
            logger.info("Successfully received response from Azure ML Endpoint.")
            return result
        except requests.exceptions.RequestException as e:
            logger.error(f"Error querying Azure ML Endpoint: {e}")
            raise

    @tool
    def my_python_tool(input_data: str, connection: CustomConnection) -> str:
        """
        Tool function to process input data and query the Phi-3 / Phi-3.5 model.
        """
        return query_phi3_model(input_data, connection)

    ```

    ![Coller le code du prompt flow.](../../../../../../translated_images/fr/paste-promptflow-code.cd6d95b101c0ec28.webp)

> [!NOTE]
> Pour plus d’informations détaillées sur l’utilisation de Prompt flow dans Azure AI Foundry, vous pouvez consulter [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Sélectionnez **Chat input**, **Chat output** pour activer la conversation avec votre modèle.

    ![Sélectionner entrée et sortie.](../../../../../../translated_images/fr/select-input-output.c187fc58f25fbfc3.webp)

1. Vous êtes maintenant prêt à discuter avec votre modèle Phi-3 / Phi-3.5 personnalisé. Dans l’exercice suivant, vous apprendrez comment démarrer Prompt flow et l’utiliser pour discuter avec votre modèle Phi-3 / Phi-3.5 affiné.

> [!NOTE]
>
> Le flux reconstruit devrait ressembler à l’image ci-dessous :
>
> ![Exemple de flux](../../../../../../translated_images/fr/graph-example.82fd1bcdd3fc545b.webp)
>

#### Démarrer Prompt flow

1. Sélectionnez **Start compute sessions** pour lancer Prompt flow.

    ![Démarrer la session de calcul.](../../../../../../translated_images/fr/start-compute-session.9acd8cbbd2c43df1.webp)

1. Sélectionnez **Validate and parse input** pour renouveler les paramètres.

    ![Valider l’entrée.](../../../../../../translated_images/fr/validate-input.c1adb9543c6495be.webp)

1. Sélectionnez la **Valeur** de la **connection** vers la connexion personnalisée que vous avez créée. Par exemple, *connection*.

    ![Connexion.](../../../../../../translated_images/fr/select-connection.1f2b59222bcaafef.webp)

#### Discuter avec votre modèle Phi-3 / Phi-3.5 personnalisé

1. Sélectionnez **Chat**.

    ![Sélectionner chat.](../../../../../../translated_images/fr/select-chat.0406bd9687d0c49d.webp)

1. Voici un exemple de résultats : vous pouvez maintenant discuter avec votre modèle Phi-3 / Phi-3.5 personnalisé. Il est recommandé de poser des questions basées sur les données utilisées pour l’affinage.

    ![Discuter avec prompt flow.](../../../../../../translated_images/fr/chat-with-promptflow.1cf8cea112359ada.webp)

### Déployer Azure OpenAI pour évaluer le modèle Phi-3 / Phi-3.5

Pour évaluer le modèle Phi-3 / Phi-3.5 dans Azure AI Foundry, vous devez déployer un modèle Azure OpenAI. Ce modèle sera utilisé pour évaluer les performances du modèle Phi-3 / Phi-3.5.

#### Déployer Azure OpenAI

1. Connectez-vous à [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Accédez au projet Azure AI Foundry que vous avez créé.

    ![Sélectionner le projet.](../../../../../../translated_images/fr/select-project-created.5221e0e403e2c9d6.webp)

1. Dans le projet que vous avez créé, sélectionnez **Deployments** dans l’onglet latéral gauche.

1. Sélectionnez **+ Deploy model** dans le menu de navigation.

1. Sélectionnez **Deploy base model**.

    ![Sélectionner Deployments.](../../../../../../translated_images/fr/deploy-openai-model.95d812346b25834b.webp)

1. Sélectionnez le modèle Azure OpenAI que vous souhaitez utiliser. Par exemple, **gpt-4o**.

    ![Sélectionner le modèle Azure OpenAI à utiliser.](../../../../../../translated_images/fr/select-openai-model.959496d7e311546d.webp)

1. Sélectionnez **Confirm**.

### Évaluer le modèle Phi-3 / Phi-3.5 affiné en utilisant l’évaluation Prompt flow d’Azure AI Foundry

### Démarrer une nouvelle évaluation

1. Rendez-vous sur [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Accédez au projet Azure AI Foundry que vous avez créé.

    ![Sélectionner le projet.](../../../../../../translated_images/fr/select-project-created.5221e0e403e2c9d6.webp)

1. Dans le projet que vous avez créé, sélectionnez **Evaluation** dans l’onglet latéral gauche.

1. Sélectionnez **+ New evaluation** dans le menu de navigation.

    ![Sélectionner l’évaluation.](../../../../../../translated_images/fr/select-evaluation.2846ad7aaaca7f4f.webp)

1. Sélectionnez l’évaluation **Prompt flow**.

    ![Sélectionner l’évaluation Prompt flow.](../../../../../../translated_images/fr/promptflow-evaluation.cb9758cc19b4760f.webp)

1. Effectuez les tâches suivantes :

    - Saisissez le nom de l’évaluation. Il doit être unique.
    - Sélectionnez **Question and answer without context** comme type de tâche. En effet, le jeu de données **ULTRACHAT_200k** utilisé dans ce tutoriel ne contient pas de contexte.
    - Sélectionnez le prompt flow que vous souhaitez évaluer.

    ![Évaluation Prompt flow.](../../../../../../translated_images/fr/evaluation-setting1.4aa08259ff7a536e.webp)

1. Sélectionnez **Next**.

1. Effectuez les tâches suivantes :

    - Sélectionnez **Add your dataset** pour importer le jeu de données. Par exemple, vous pouvez importer le fichier de test, comme *test_data.json1*, inclus lors du téléchargement du jeu de données **ULTRACHAT_200k**.
    - Sélectionnez la **Colonne du dataset** appropriée correspondant à votre jeu de données. Par exemple, si vous utilisez le jeu de données **ULTRACHAT_200k**, sélectionnez **${data.prompt}** comme colonne.

    ![Évaluation Prompt flow.](../../../../../../translated_images/fr/evaluation-setting2.07036831ba58d64e.webp)

1. Sélectionnez **Next**.

1. Effectuez les tâches suivantes pour configurer les métriques de performance et de qualité :

    - Sélectionnez les métriques de performance et de qualité que vous souhaitez utiliser.
    - Sélectionnez le modèle Azure OpenAI que vous avez créé pour l’évaluation. Par exemple, sélectionnez **gpt-4o**.

    ![Évaluation Prompt flow.](../../../../../../translated_images/fr/evaluation-setting3-1.d1ae69e3bf80914e.webp)

1. Effectuez les tâches suivantes pour configurer les métriques de risque et de sécurité :

    - Sélectionnez les métriques de risque et de sécurité que vous souhaitez utiliser.
    - Sélectionnez le seuil pour calculer le taux de défaut que vous souhaitez utiliser. Par exemple, sélectionnez **Medium**.
    - Pour **question**, sélectionnez **Data source** sur **{$data.prompt}**.
    - Pour **answer**, sélectionnez **Data source** sur **{$run.outputs.answer}**.
    - Pour **ground_truth**, sélectionnez **Data source** sur **{$data.message}**.

    ![Évaluation Prompt flow.](../../../../../../translated_images/fr/evaluation-setting3-2.d53bd075c60a45a2.webp)

1. Sélectionnez **Next**.

1. Sélectionnez **Submit** pour lancer l’évaluation.

1. L’évaluation prendra un certain temps. Vous pouvez suivre la progression dans l’onglet **Evaluation**.

### Examiner les résultats de l’évaluation
> [!NOTE]
> Les résultats présentés ci-dessous ont pour but d’illustrer le processus d’évaluation. Dans ce tutoriel, nous avons utilisé un modèle affiné sur un ensemble de données relativement restreint, ce qui peut entraîner des résultats sous-optimaux. Les résultats réels peuvent varier considérablement en fonction de la taille, de la qualité et de la diversité de l’ensemble de données utilisé, ainsi que de la configuration spécifique du modèle.
Une fois l’évaluation terminée, vous pouvez consulter les résultats pour les indicateurs de performance et de sécurité.

1. Indicateurs de performance et de qualité :

    - évaluer l’efficacité du modèle à générer des réponses cohérentes, fluides et pertinentes.

    ![Résultat de l’évaluation.](../../../../../../translated_images/fr/evaluation-result-gpu.85f48b42dfb74254.webp)

1. Indicateurs de risque et de sécurité :

    - s’assurer que les sorties du modèle sont sûres et conformes aux Principes d’IA Responsable, en évitant tout contenu nuisible ou offensant.

    ![Résultat de l’évaluation.](../../../../../../translated_images/fr/evaluation-result-gpu-2.1b74e336118f4fd0.webp)

1. Vous pouvez faire défiler la page vers le bas pour voir le **résultat détaillé des indicateurs**.

    ![Résultat de l’évaluation.](../../../../../../translated_images/fr/detailed-metrics-result.afa2f5c39a4f5f17.webp)

1. En évaluant votre modèle personnalisé Phi-3 / Phi-3.5 selon les indicateurs de performance et de sécurité, vous pouvez confirmer que le modèle est non seulement efficace, mais aussi conforme aux pratiques d’IA responsable, ce qui le rend prêt pour un déploiement en conditions réelles.

## Félicitations !

### Vous avez terminé ce tutoriel

Vous avez évalué avec succès le modèle Phi-3 affiné et intégré avec Prompt flow dans Azure AI Foundry. C’est une étape importante pour garantir que vos modèles d’IA ne se contentent pas de bien fonctionner, mais respectent également les principes d’IA Responsable de Microsoft afin de vous aider à créer des applications d’IA fiables et dignes de confiance.

![Architecture.](../../../../../../translated_images/fr/architecture.10bec55250f5d6a4.webp)

## Nettoyer les ressources Azure

Nettoyez vos ressources Azure pour éviter des frais supplémentaires sur votre compte. Rendez-vous sur le portail Azure et supprimez les ressources suivantes :

- La ressource Azure Machine learning.
- Le point de terminaison du modèle Azure Machine learning.
- La ressource Azure AI Foundry Project.
- La ressource Azure AI Foundry Prompt flow.

### Étapes suivantes

#### Documentation

- [Évaluer les systèmes d’IA avec le tableau de bord Responsible AI](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [Indicateurs d’évaluation et de surveillance pour l’IA générative](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Documentation Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Documentation Prompt flow](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### Contenu de formation

- [Introduction à l’approche Responsible AI de Microsoft](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Introduction à Azure AI Foundry](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### Références

- [Qu’est-ce que Responsible AI ?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [Annonce de nouveaux outils dans Azure AI pour vous aider à créer des applications d’IA générative plus sûres et fiables](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [Évaluation des applications d’IA générative](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.