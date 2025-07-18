<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "80a853c08e4ee25ef9b4bfcedd8990da",
  "translation_date": "2025-07-16T23:10:22+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md",
  "language_code": "es"
}
-->
# Evaluar el modelo Phi-3 / Phi-3.5 afinado en Azure AI Foundry centrado en los Principios de IA Responsable de Microsoft

Este ejemplo de extremo a extremo (E2E) se basa en la guía "[Evaluate Fine-tuned Phi-3 / 3.5 Models in Azure AI Foundry Focusing on Microsoft's Responsible AI](https://techcommunity.microsoft.com/blog/educatordeveloperblog/evaluate-fine-tuned-phi-3--3-5-models-in-azure-ai-studio-focusing-on-microsofts-/4227850?WT.mc_id=aiml-137032-kinfeylo)" de la Comunidad Técnica de Microsoft.

## Visión general

### ¿Cómo puedes evaluar la seguridad y el rendimiento de un modelo Phi-3 / Phi-3.5 afinado en Azure AI Foundry?

Afinar un modelo puede a veces generar respuestas no deseadas o imprevistas. Para garantizar que el modelo siga siendo seguro y eficaz, es importante evaluar su potencial para generar contenido dañino y su capacidad para producir respuestas precisas, relevantes y coherentes. En este tutorial, aprenderás a evaluar la seguridad y el rendimiento de un modelo Phi-3 / Phi-3.5 afinado e integrado con Prompt flow en Azure AI Foundry.

Aquí tienes el proceso de evaluación de Azure AI Foundry.

![Arquitectura del tutorial.](../../../../../../translated_images/architecture.10bec55250f5d6a4e1438bb31c5c70309908e21e7ada24a621bbfdd8d0f834f4.es.png)

*Fuente de la imagen: [Evaluación de aplicaciones de IA generativa](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> Para obtener información más detallada y explorar recursos adicionales sobre Phi-3 / Phi-3.5, visita el [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723).

### Requisitos previos

- [Python](https://www.python.org/downloads)
- [Suscripción a Azure](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- Modelo Phi-3 / Phi-3.5 afinado

### Tabla de contenidos

1. [**Escenario 1: Introducción a la evaluación con Prompt flow de Azure AI Foundry**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Introducción a la evaluación de seguridad](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Introducción a la evaluación de rendimiento](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [**Escenario 2: Evaluación del modelo Phi-3 / Phi-3.5 en Azure AI Foundry**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Antes de comenzar](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Desplegar Azure OpenAI para evaluar el modelo Phi-3 / Phi-3.5](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Evaluar el modelo Phi-3 / Phi-3.5 afinado usando la evaluación con Prompt flow de Azure AI Foundry](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [¡Felicidades!](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## **Escenario 1: Introducción a la evaluación con Prompt flow de Azure AI Foundry**

### Introducción a la evaluación de seguridad

Para garantizar que tu modelo de IA sea ético y seguro, es fundamental evaluarlo conforme a los Principios de IA Responsable de Microsoft. En Azure AI Foundry, las evaluaciones de seguridad te permiten analizar la vulnerabilidad de tu modelo a ataques de jailbreak y su potencial para generar contenido dañino, lo cual está directamente alineado con estos principios.

![Evaluación de seguridad.](../../../../../../translated_images/safety-evaluation.083586ec88dfa9500d3d25faf0720fd99cbf07c8c4b559dda5e70c84a0e2c1aa.es.png)

*Fuente de la imagen: [Evaluación de aplicaciones de IA generativa](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Principios de IA Responsable de Microsoft

Antes de comenzar con los pasos técnicos, es esencial comprender los Principios de IA Responsable de Microsoft, un marco ético diseñado para guiar el desarrollo, despliegue y operación responsables de sistemas de IA. Estos principios orientan el diseño, desarrollo y despliegue responsable de sistemas de IA, asegurando que las tecnologías de IA se construyan de manera justa, transparente e inclusiva. Estos principios son la base para evaluar la seguridad de los modelos de IA.

Los Principios de IA Responsable de Microsoft incluyen:

- **Equidad e Inclusión**: Los sistemas de IA deben tratar a todas las personas de manera justa y evitar afectar de forma diferente a grupos similares. Por ejemplo, cuando los sistemas de IA ofrecen recomendaciones sobre tratamientos médicos, solicitudes de préstamos o empleo, deben hacer las mismas recomendaciones a quienes tengan síntomas, circunstancias financieras o cualificaciones profesionales similares.

- **Confiabilidad y Seguridad**: Para generar confianza, es fundamental que los sistemas de IA funcionen de manera confiable, segura y consistente. Estos sistemas deben operar según lo diseñado originalmente, responder de forma segura a condiciones imprevistas y resistir manipulaciones dañinas. Su comportamiento y la variedad de condiciones que pueden manejar reflejan el rango de situaciones que los desarrolladores anticiparon durante el diseño y las pruebas.

- **Transparencia**: Cuando los sistemas de IA ayudan a tomar decisiones que impactan significativamente la vida de las personas, es crucial que estas entiendan cómo se tomaron dichas decisiones. Por ejemplo, un banco podría usar un sistema de IA para decidir si una persona es crediticia. Una empresa podría usar un sistema de IA para determinar los candidatos más calificados para contratar.

- **Privacidad y Seguridad**: A medida que la IA se vuelve más común, proteger la privacidad y asegurar la información personal y empresarial se vuelve más importante y complejo. Con la IA, la privacidad y la seguridad de los datos requieren especial atención porque el acceso a los datos es esencial para que los sistemas de IA hagan predicciones y decisiones precisas e informadas sobre las personas.

- **Responsabilidad**: Las personas que diseñan y despliegan sistemas de IA deben ser responsables del funcionamiento de sus sistemas. Las organizaciones deben basarse en estándares de la industria para desarrollar normas de responsabilidad. Estas normas pueden asegurar que los sistemas de IA no sean la autoridad final en decisiones que afectan la vida de las personas y que los humanos mantengan un control significativo sobre sistemas de IA altamente autónomos.

![Centro de llenado.](../../../../../../translated_images/responsibleai2.c07ef430113fad8c72329615ecf51a4e3df31043fb0d918f868525e7a9747b98.es.png)

*Fuente de la imagen: [¿Qué es IA Responsable?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> Para aprender más sobre los Principios de IA Responsable de Microsoft, visita [¿Qué es IA Responsable?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723).

#### Métricas de seguridad

En este tutorial, evaluarás la seguridad del modelo Phi-3 afinado usando las métricas de seguridad de Azure AI Foundry. Estas métricas te ayudan a valorar el potencial del modelo para generar contenido dañino y su vulnerabilidad a ataques de jailbreak. Las métricas de seguridad incluyen:

- **Contenido relacionado con autolesiones**: Evalúa si el modelo tiende a producir contenido relacionado con autolesiones.
- **Contenido odioso e injusto**: Evalúa si el modelo tiende a generar contenido odioso o injusto.
- **Contenido violento**: Evalúa si el modelo tiende a producir contenido violento.
- **Contenido sexual**: Evalúa si el modelo tiende a generar contenido sexual inapropiado.

Evaluar estos aspectos asegura que el modelo de IA no produzca contenido dañino u ofensivo, alineándose con los valores sociales y las normativas vigentes.

![Evaluar basado en seguridad.](../../../../../../translated_images/evaluate-based-on-safety.c5df819f5b0bfc07156d9b1e18bdf1f130120f7d23e05ea78bc9773d2500b665.es.png)

### Introducción a la evaluación de rendimiento

Para garantizar que tu modelo de IA funcione como se espera, es importante evaluar su rendimiento mediante métricas específicas. En Azure AI Foundry, las evaluaciones de rendimiento te permiten medir la efectividad de tu modelo para generar respuestas precisas, relevantes y coherentes.

![Evaluación de seguridad.](../../../../../../translated_images/performance-evaluation.48b3e7e01a098740c7babf1904fa4acca46c5bd7ea8c826832989c776c0e01ca.es.png)

*Fuente de la imagen: [Evaluación de aplicaciones de IA generativa](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Métricas de rendimiento

En este tutorial, evaluarás el rendimiento del modelo Phi-3 / Phi-3.5 afinado usando las métricas de rendimiento de Azure AI Foundry. Estas métricas te ayudan a valorar la efectividad del modelo para generar respuestas precisas, relevantes y coherentes. Las métricas de rendimiento incluyen:

- **Fundamentación**: Evalúa qué tan bien las respuestas generadas se alinean con la información de la fuente de entrada.
- **Relevancia**: Evalúa la pertinencia de las respuestas generadas respecto a las preguntas planteadas.
- **Coherencia**: Evalúa qué tan fluido es el texto generado, si se lee de forma natural y se asemeja al lenguaje humano.
- **Fluidez**: Evalúa la competencia lingüística del texto generado.
- **Similitud con GPT**: Compara la respuesta generada con la verdad de referencia para medir similitud.
- **Puntuación F1**: Calcula la proporción de palabras compartidas entre la respuesta generada y los datos fuente.

Estas métricas te ayudan a evaluar la efectividad del modelo para generar respuestas precisas, relevantes y coherentes.

![Evaluar basado en rendimiento.](../../../../../../translated_images/evaluate-based-on-performance.3e801c647c7554e820ceb3f7f148014fe0572c05dbdadb1af7205e1588fb0358.es.png)

## **Escenario 2: Evaluación del modelo Phi-3 / Phi-3.5 en Azure AI Foundry**

### Antes de comenzar

Este tutorial es una continuación de las publicaciones anteriores, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" y "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)." En estas publicaciones, recorrimos el proceso de afinado de un modelo Phi-3 / Phi-3.5 en Azure AI Foundry y su integración con Prompt flow.

En este tutorial, desplegarás un modelo Azure OpenAI como evaluador en Azure AI Foundry y lo usarás para evaluar tu modelo Phi-3 / Phi-3.5 afinado.

Antes de comenzar este tutorial, asegúrate de contar con los siguientes requisitos previos, tal como se describió en los tutoriales anteriores:

1. Un conjunto de datos preparado para evaluar el modelo Phi-3 / Phi-3.5 afinado.
1. Un modelo Phi-3 / Phi-3.5 que haya sido afinado y desplegado en Azure Machine Learning.
1. Un Prompt flow integrado con tu modelo Phi-3 / Phi-3.5 afinado en Azure AI Foundry.

> [!NOTE]
> Usarás el archivo *test_data.jsonl*, ubicado en la carpeta data del conjunto de datos **ULTRACHAT_200k** descargado en las publicaciones anteriores, como conjunto de datos para evaluar el modelo Phi-3 / Phi-3.5 afinado.

#### Integrar el modelo personalizado Phi-3 / Phi-3.5 con Prompt flow en Azure AI Foundry (enfoque basado en código)
> [!NOTE]
> Si seguiste el enfoque low-code descrito en "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)", puedes omitir este ejercicio y continuar con el siguiente.
> Sin embargo, si seguiste el enfoque code-first descrito en "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" para ajustar y desplegar tu modelo Phi-3 / Phi-3.5, el proceso para conectar tu modelo con Prompt flow es un poco diferente. Aprenderás este proceso en este ejercicio.
Para continuar, necesitas integrar tu modelo ajustado Phi-3 / Phi-3.5 en Prompt flow dentro de Azure AI Foundry.

#### Crear Azure AI Foundry Hub

Debes crear un Hub antes de crear el Proyecto. Un Hub funciona como un Grupo de Recursos, permitiéndote organizar y gestionar múltiples Proyectos dentro de Azure AI Foundry.

1. Inicia sesión en [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Selecciona **All hubs** en la pestaña lateral izquierda.

1. Selecciona **+ New hub** en el menú de navegación.

    ![Create hub.](../../../../../../translated_images/create-hub.5be78fb1e21ffbf1aa9ecc232c2c95d337386f3cd0f361ca80c4475dc8aa2c7b.es.png)

1. Realiza las siguientes tareas:

    - Ingresa el **Hub name**. Debe ser un valor único.
    - Selecciona tu **Subscription** de Azure.
    - Selecciona el **Resource group** que usarás (crea uno nuevo si es necesario).
    - Selecciona la **Location** que deseas usar.
    - Selecciona **Connect Azure AI Services** para usar (crea uno nuevo si es necesario).
    - Selecciona **Connect Azure AI Search** para **Skip connecting**.

    ![Fill hub.](../../../../../../translated_images/fill-hub.baaa108495c71e3449667210a8ec5a0f3206bf2724ebacaa69cb09d3b12f29d3.es.png)

1. Selecciona **Next**.

#### Crear Proyecto en Azure AI Foundry

1. En el Hub que creaste, selecciona **All projects** en la pestaña lateral izquierda.

1. Selecciona **+ New project** en el menú de navegación.

    ![Select new project.](../../../../../../translated_images/select-new-project.cd31c0404088d7a32ee9018978b607dfb773956b15a88606f45579d3bc23c155.es.png)

1. Ingresa el **Project name**. Debe ser un valor único.

    ![Create project.](../../../../../../translated_images/create-project.ca3b71298b90e42049ce8f6f452313bde644c309331fd728fcacd8954a20e26d.es.png)

1. Selecciona **Create a project**.

#### Añadir una conexión personalizada para el modelo ajustado Phi-3 / Phi-3.5

Para integrar tu modelo personalizado Phi-3 / Phi-3.5 con Prompt flow, necesitas guardar el endpoint y la clave del modelo en una conexión personalizada. Esta configuración asegura el acceso a tu modelo personalizado en Prompt flow.

#### Configurar la clave api y el URI del endpoint del modelo ajustado Phi-3 / Phi-3.5

1. Visita [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Navega al espacio de trabajo de Azure Machine Learning que creaste.

1. Selecciona **Endpoints** en la pestaña lateral izquierda.

    ![Select endpoints.](../../../../../../translated_images/select-endpoints.ee7387ecd68bd18d35cd7f235f930ebe99841a8c8c9dea2f608b7f43508576dd.es.png)

1. Selecciona el endpoint que creaste.

    ![Select endpoints.](../../../../../../translated_images/select-endpoint-created.9f63af5e4cf98b2ec92358f15ad36d69820e627c048f14c7ec3750fdbce3558b.es.png)

1. Selecciona **Consume** en el menú de navegación.

1. Copia tu **REST endpoint** y tu **Primary key**.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/copy-endpoint-key.0650c3786bd646ab0b5a80833917b7b8f32ee011c09af0459f3830dc25b00760.es.png)

#### Añadir la Conexión Personalizada

1. Visita [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Navega al proyecto de Azure AI Foundry que creaste.

1. En el proyecto que creaste, selecciona **Settings** en la pestaña lateral izquierda.

1. Selecciona **+ New connection**.

    ![Select new connection.](../../../../../../translated_images/select-new-connection.fa0f35743758a74b6c5dca5f37ca22939163f5c89eac47d1fd0a8c663bd5904a.es.png)

1. Selecciona **Custom keys** en el menú de navegación.

    ![Select custom keys.](../../../../../../translated_images/select-custom-keys.5a3c6b25580a9b67df43e8c5519124268b987d8cb77d6e5fe5631f116714bd47.es.png)

1. Realiza las siguientes tareas:

    - Selecciona **+ Add key value pairs**.
    - Para el nombre de la clave, ingresa **endpoint** y pega el endpoint que copiaste de Azure ML Studio en el campo de valor.
    - Selecciona **+ Add key value pairs** nuevamente.
    - Para el nombre de la clave, ingresa **key** y pega la clave que copiaste de Azure ML Studio en el campo de valor.
    - Después de agregar las claves, selecciona **is secret** para evitar que la clave sea expuesta.

    ![Add connection.](../../../../../../translated_images/add-connection.ac7f5faf8b10b0dfe6679422f479f88cc47c33cbf24568da138ab19fbb17dc4b.es.png)

1. Selecciona **Add connection**.

#### Crear Prompt flow

Has añadido una conexión personalizada en Azure AI Foundry. Ahora, vamos a crear un Prompt flow siguiendo los pasos a continuación. Luego, conectarás este Prompt flow a la conexión personalizada para usar el modelo ajustado dentro del Prompt flow.

1. Navega al proyecto de Azure AI Foundry que creaste.

1. Selecciona **Prompt flow** en la pestaña lateral izquierda.

1. Selecciona **+ Create** en el menú de navegación.

    ![Select Promptflow.](../../../../../../translated_images/select-promptflow.18ff2e61ab9173eb94fbf771819d7ddf21e9c239f2689cb2684d4d3c739deb75.es.png)

1. Selecciona **Chat flow** en el menú de navegación.

    ![Select chat flow.](../../../../../../translated_images/select-flow-type.28375125ec9996d33a7d73eb77e59354e1b70fd246009e30bdd40db17143ec83.es.png)

1. Ingresa el **Folder name** que usarás.

    ![Select chat flow.](../../../../../../translated_images/enter-name.02ddf8fb840ad4305ba88e0a804a5198ddd8720ebccb420d65ba13dcd481591f.es.png)

1. Selecciona **Create**.

#### Configurar Prompt flow para chatear con tu modelo personalizado Phi-3 / Phi-3.5

Necesitas integrar el modelo ajustado Phi-3 / Phi-3.5 en un Prompt flow. Sin embargo, el Prompt flow existente no está diseñado para este propósito. Por lo tanto, debes rediseñar el Prompt flow para habilitar la integración del modelo personalizado.

1. En el Prompt flow, realiza las siguientes tareas para reconstruir el flujo existente:

    - Selecciona **Raw file mode**.
    - Elimina todo el código existente en el archivo *flow.dag.yml*.
    - Añade el siguiente código en *flow.dag.yml*.

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

    - Selecciona **Save**.

    ![Select raw file mode.](../../../../../../translated_images/select-raw-file-mode.06c1eca581ce4f5344b4801da9d695b3c1ea7019479754e566d2df495e868664.es.png)

1. Añade el siguiente código en *integrate_with_promptflow.py* para usar el modelo personalizado Phi-3 / Phi-3.5 en Prompt flow.

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

    ![Paste prompt flow code.](../../../../../../translated_images/paste-promptflow-code.cd6d95b101c0ec2818291eeeb2aa744d0e01320308a1fa6348ac7f51bec93de9.es.png)

> [!NOTE]
> Para más información detallada sobre cómo usar Prompt flow en Azure AI Foundry, puedes consultar [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Selecciona **Chat input**, **Chat output** para habilitar el chat con tu modelo.

    ![Select Input Output.](../../../../../../translated_images/select-input-output.c187fc58f25fbfc339811bdd5a2285589fef803aded96b8c58b40131f0663571.es.png)

1. Ahora estás listo para chatear con tu modelo personalizado Phi-3 / Phi-3.5. En el siguiente ejercicio, aprenderás cómo iniciar Prompt flow y usarlo para chatear con tu modelo ajustado Phi-3 / Phi-3.5.

> [!NOTE]
>
> El flujo reconstruido debería verse como en la imagen a continuación:
>
> ![Flow example](../../../../../../translated_images/graph-example.82fd1bcdd3fc545bcc81d64cb6542972ae593588ab94564c8c25edf06fae27fc.es.png)
>

#### Iniciar Prompt flow

1. Selecciona **Start compute sessions** para iniciar Prompt flow.

    ![Start compute session.](../../../../../../translated_images/start-compute-session.9acd8cbbd2c43df160358b6be6cad3e069a9c22271fd8b40addc847aeca83b44.es.png)

1. Selecciona **Validate and parse input** para renovar los parámetros.

    ![Validate input.](../../../../../../translated_images/validate-input.c1adb9543c6495be3c94da090ce7c61a77cc8baf0718552e3d6e41b87eb96a41.es.png)

1. Selecciona el **Value** de la **connection** a la conexión personalizada que creaste. Por ejemplo, *connection*.

    ![Connection.](../../../../../../translated_images/select-connection.1f2b59222bcaafefe7ac3726aaa2a7fdb04a5b969cd09f009acfe8b1e841efb6.es.png)

#### Chatear con tu modelo personalizado Phi-3 / Phi-3.5

1. Selecciona **Chat**.

    ![Select chat.](../../../../../../translated_images/select-chat.0406bd9687d0c49d8bf2b8145f603ed5616b71ba82a0eadde189275b88e50a3f.es.png)

1. Aquí tienes un ejemplo de los resultados: ahora puedes chatear con tu modelo personalizado Phi-3 / Phi-3.5. Se recomienda hacer preguntas basadas en los datos usados para el ajuste fino.

    ![Chat with prompt flow.](../../../../../../translated_images/chat-with-promptflow.1cf8cea112359ada4628ea1d3d9f563f3e6df2c01cf917bade1a5eb9d197493a.es.png)

### Desplegar Azure OpenAI para evaluar el modelo Phi-3 / Phi-3.5

Para evaluar el modelo Phi-3 / Phi-3.5 en Azure AI Foundry, necesitas desplegar un modelo Azure OpenAI. Este modelo se usará para evaluar el rendimiento del modelo Phi-3 / Phi-3.5.

#### Desplegar Azure OpenAI

1. Inicia sesión en [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Navega al proyecto de Azure AI Foundry que creaste.

    ![Select Project.](../../../../../../translated_images/select-project-created.5221e0e403e2c9d6a17c809ad9aee8de593cd48717f157cc3eb2b29a37aa02ae.es.png)

1. En el proyecto que creaste, selecciona **Deployments** en la pestaña lateral izquierda.

1. Selecciona **+ Deploy model** en el menú de navegación.

1. Selecciona **Deploy base model**.

    ![Select Deployments.](../../../../../../translated_images/deploy-openai-model.95d812346b25834b05b20fe43c20130da7eae1e485ad60bb8e46bbc85a6c613a.es.png)

1. Selecciona el modelo Azure OpenAI que deseas usar. Por ejemplo, **gpt-4o**.

    ![Select Azure OpenAI model you'd like to use.](../../../../../../translated_images/select-openai-model.959496d7e311546d66ec145dc4e0bf0cc806e6e5469b17e776788d6f5ba7a221.es.png)

1. Selecciona **Confirm**.

### Evaluar el modelo ajustado Phi-3 / Phi-3.5 usando la evaluación de Prompt flow de Azure AI Foundry

### Iniciar una nueva evaluación

1. Visita [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Navega al proyecto de Azure AI Foundry que creaste.

    ![Select Project.](../../../../../../translated_images/select-project-created.5221e0e403e2c9d6a17c809ad9aee8de593cd48717f157cc3eb2b29a37aa02ae.es.png)

1. En el proyecto que creaste, selecciona **Evaluation** en la pestaña lateral izquierda.

1. Selecciona **+ New evaluation** en el menú de navegación.

    ![Select evaluation.](../../../../../../translated_images/select-evaluation.2846ad7aaaca7f4f2cd3f728b640e64eeb639dc5dcb52f2d651099576b894848.es.png)

1. Selecciona la evaluación **Prompt flow**.

    ![Select Prompt flow evaluation.](../../../../../../translated_images/promptflow-evaluation.cb9758cc19b4760f7a1ddda46bf47281cac59f2b1043f6a775a73977875f29a6.es.png)

1. Realiza las siguientes tareas:

    - Ingresa el nombre de la evaluación. Debe ser un valor único.
    - Selecciona **Question and answer without context** como tipo de tarea. Esto es porque el conjunto de datos **ULTRACHAT_200k** usado en este tutorial no contiene contexto.
    - Selecciona el prompt flow que deseas evaluar.

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting1.4aa08259ff7a536e2e0e3011ff583f7164532d954a5ede4434fe9985cf51047e.es.png)

1. Selecciona **Next**.

1. Realiza las siguientes tareas:

    - Selecciona **Add your dataset** para subir el conjunto de datos. Por ejemplo, puedes subir el archivo de prueba, como *test_data.json1*, que se incluye al descargar el conjunto de datos **ULTRACHAT_200k**.
    - Selecciona la **Dataset column** adecuada que coincida con tu conjunto de datos. Por ejemplo, si usas el conjunto de datos **ULTRACHAT_200k**, selecciona **${data.prompt}** como columna del conjunto de datos.

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting2.07036831ba58d64ee622f9ee9b1c70f71b51cf39c3749dcd294414048c5b7e39.es.png)

1. Selecciona **Next**.

1. Realiza las siguientes tareas para configurar las métricas de rendimiento y calidad:

    - Selecciona las métricas de rendimiento y calidad que deseas usar.
    - Selecciona el modelo Azure OpenAI que creaste para la evaluación. Por ejemplo, selecciona **gpt-4o**.

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting3-1.d1ae69e3bf80914e68a0ad38486ca2d6c3ee5a30f4275f98fd3bc510c8d8f6d2.es.png)

1. Realiza las siguientes tareas para configurar las métricas de riesgo y seguridad:

    - Selecciona las métricas de riesgo y seguridad que deseas usar.
    - Selecciona el umbral para calcular la tasa de defectos que deseas usar. Por ejemplo, selecciona **Medium**.
    - Para **question**, selecciona **Data source** a **{$data.prompt}**.
    - Para **answer**, selecciona **Data source** a **{$run.outputs.answer}**.
    - Para **ground_truth**, selecciona **Data source** a **{$data.message}**.

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting3-2.d53bd075c60a45a2fab8ffb7e4dc28e8e544d2a093fbc9f63449a03984df98d9.es.png)

1. Selecciona **Next**.

1. Selecciona **Submit** para iniciar la evaluación.

1. La evaluación tomará un tiempo en completarse. Puedes monitorear el progreso en la pestaña **Evaluation**.

### Revisar los resultados de la evaluación
> [!NOTE]
> Los resultados que se presentan a continuación tienen como objetivo ilustrar el proceso de evaluación. En este tutorial, hemos utilizado un modelo ajustado con un conjunto de datos relativamente pequeño, lo que puede conducir a resultados subóptimos. Los resultados reales pueden variar significativamente según el tamaño, la calidad y la diversidad del conjunto de datos utilizado, así como la configuración específica del modelo.
Una vez que la evaluación esté completa, puedes revisar los resultados tanto de los indicadores de rendimiento como de seguridad.

1. Métricas de rendimiento y calidad:

    - evalúa la efectividad del modelo para generar respuestas coherentes, fluidas y relevantes.

    ![Evaluation result.](../../../../../../translated_images/evaluation-result-gpu.85f48b42dfb7425434ec49685cff41376de3954fdab20f2a82c726f9fd690617.es.png)

1. Métricas de riesgo y seguridad:

    - Asegúrate de que las salidas del modelo sean seguras y estén alineadas con los Principios de IA Responsable, evitando cualquier contenido dañino u ofensivo.

    ![Evaluation result.](../../../../../../translated_images/evaluation-result-gpu-2.1b74e336118f4fd0589153bf7fb6269cd10aaeb10c1456bc76a06b93b2be15e6.es.png)

1. Puedes desplazarte hacia abajo para ver el **resultado detallado de las métricas**.

    ![Evaluation result.](../../../../../../translated_images/detailed-metrics-result.afa2f5c39a4f5f179c3916ba948feb367dfd4e0658752615be62824ef1dcf2d3.es.png)

1. Al evaluar tu modelo personalizado Phi-3 / Phi-3.5 con ambas métricas, de rendimiento y seguridad, puedes confirmar que el modelo no solo es efectivo, sino que también cumple con las prácticas de IA responsable, preparándolo para su implementación en el mundo real.

## ¡Felicidades!

### Has completado este tutorial

Has evaluado con éxito el modelo Phi-3 afinado e integrado con Prompt flow en Azure AI Foundry. Este es un paso importante para garantizar que tus modelos de IA no solo tengan un buen desempeño, sino que también cumplan con los principios de IA Responsable de Microsoft, ayudándote a construir aplicaciones de IA confiables y seguras.

![Architecture.](../../../../../../translated_images/architecture.10bec55250f5d6a4e1438bb31c5c70309908e21e7ada24a621bbfdd8d0f834f4.es.png)

## Limpieza de recursos de Azure

Limpia tus recursos de Azure para evitar cargos adicionales en tu cuenta. Ve al portal de Azure y elimina los siguientes recursos:

- El recurso de Azure Machine learning.
- El endpoint del modelo de Azure Machine learning.
- El recurso del proyecto Azure AI Foundry.
- El recurso de Prompt flow de Azure AI Foundry.

### Próximos pasos

#### Documentación

- [Evalúa sistemas de IA usando el panel de IA Responsable](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [Métricas de evaluación y monitoreo para IA generativa](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Documentación de Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Documentación de Prompt flow](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### Contenido de capacitación

- [Introducción al enfoque de IA Responsable de Microsoft](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Introducción a Azure AI Foundry](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### Referencias

- [¿Qué es la IA Responsable?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [Anuncio de nuevas herramientas en Azure AI para ayudarte a crear aplicaciones de IA generativa más seguras y confiables](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [Evaluación de aplicaciones de IA generativa](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

**Aviso legal**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.