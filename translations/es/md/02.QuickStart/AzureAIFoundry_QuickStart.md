<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3a1e48b628022485aac989c9f733e792",
  "translation_date": "2025-03-27T13:19:19+00:00",
  "source_file": "md\\02.QuickStart\\AzureAIFoundry_QuickStart.md",
  "language_code": "es"
}
-->
# **Uso de Phi-3 en Azure AI Foundry**

Con el desarrollo de la IA Generativa, buscamos utilizar una plataforma unificada para gestionar diferentes LLM y SLM, integrar datos empresariales, realizar operaciones de ajuste fino/RAG, y evaluar diversos negocios empresariales tras integrar LLM y SLM, entre otros, para que las aplicaciones inteligentes de IA generativa se implementen de manera más eficiente. [Azure AI Foundry](https://ai.azure.com) es una plataforma de aplicaciones empresariales de IA generativa.

![aistudo](../../../../translated_images/aifoundry_home.ffa4fe13d11f26171097f8666a1db96ac0979ffa1adde80374c60d1136c7e1de.es.png)

Con Azure AI Foundry, puedes evaluar las respuestas de los modelos de lenguaje grande (LLM) y orquestar componentes de aplicación de prompts con prompt flow para mejorar el rendimiento. La plataforma facilita la escalabilidad para transformar pruebas de concepto en implementaciones completas de producción con facilidad. El monitoreo continuo y la optimización garantizan el éxito a largo plazo.

Podemos desplegar rápidamente el modelo Phi-3 en Azure AI Foundry a través de pasos sencillos y luego utilizar Azure AI Foundry para realizar tareas relacionadas con Phi-3 como Playground/Chat, ajuste fino, evaluación y más.

## **1. Preparación**

Si ya tienes [Azure Developer CLI](https://learn.microsoft.com/azure/developer/azure-developer-cli/overview?WT.mc_id=aiml-138114-kinfeylo) instalado en tu máquina, usar esta plantilla es tan fácil como ejecutar este comando en un nuevo directorio.

## Creación Manual

Crear un proyecto y un hub en Microsoft Azure AI Foundry es una excelente manera de organizar y gestionar tu trabajo de IA. Aquí tienes una guía paso a paso para comenzar:

### Creación de un Proyecto en Azure AI Foundry

1. **Ir a Azure AI Foundry**: Inicia sesión en el portal de Azure AI Foundry.
2. **Crear un Proyecto**:
   - Si estás en un proyecto, selecciona "Azure AI Foundry" en la parte superior izquierda de la página para ir a la página de inicio.
   - Selecciona "+ Crear proyecto".
   - Ingresa un nombre para el proyecto.
   - Si tienes un hub, se seleccionará por defecto. Si tienes acceso a más de un hub, puedes elegir uno diferente en el menú desplegable. Si deseas crear un nuevo hub, selecciona "Crear nuevo hub" e ingresa un nombre.
   - Selecciona "Crear".

### Creación de un Hub en Azure AI Foundry

1. **Ir a Azure AI Foundry**: Inicia sesión con tu cuenta de Azure.
2. **Crear un Hub**:
   - Selecciona el Centro de gestión desde el menú lateral.
   - Selecciona "Todos los recursos", luego la flecha hacia abajo junto a "+ Nuevo proyecto" y selecciona "+ Nuevo hub".
   - En el cuadro de diálogo "Crear un nuevo hub", ingresa un nombre para tu hub (por ejemplo, contoso-hub) y modifica los demás campos según sea necesario.
   - Selecciona "Siguiente", revisa la información y luego selecciona "Crear".

Para instrucciones más detalladas, puedes consultar la [documentación oficial de Microsoft](https://learn.microsoft.com/azure/ai-studio/how-to/create-projects).

Tras una creación exitosa, puedes acceder al estudio que creaste a través de [ai.azure.com](https://ai.azure.com/)

En un AI Foundry pueden existir múltiples proyectos. Crea un proyecto en AI Foundry para prepararte.

Crea Azure AI Foundry [QuickStarts](https://learn.microsoft.com/azure/ai-studio/quickstarts/get-started-code)

## **2. Desplegar un modelo Phi en Azure AI Foundry**

Haz clic en la opción Explorar del proyecto para entrar al Catálogo de Modelos y selecciona Phi-3.

Selecciona Phi-3-mini-4k-instruct.

Haz clic en 'Desplegar' para implementar el modelo Phi-3-mini-4k-instruct.

> [!NOTE]
>
> Puedes seleccionar la potencia de cómputo al desplegar.

## **3. Playground Chat Phi en Azure AI Foundry**

Ve a la página de despliegue, selecciona Playground y chatea con Phi-3 en Azure AI Foundry.

## **4. Desplegar el modelo desde Azure AI Foundry**

Para desplegar un modelo desde el Catálogo de Modelos de Azure, puedes seguir estos pasos:

- Inicia sesión en Azure AI Foundry.
- Elige el modelo que deseas desplegar desde el catálogo de modelos de Azure AI Foundry.
- En la página de Detalles del modelo, selecciona Desplegar y luego selecciona API sin servidor con Azure AI Content Safety.
- Selecciona el proyecto en el que deseas desplegar tus modelos. Para usar la oferta de API sin servidor, tu espacio de trabajo debe pertenecer a la región East US 2 o Sweden Central. Puedes personalizar el nombre del despliegue.
- En el asistente de despliegue, selecciona Precios y términos para conocer los costos y condiciones de uso.
- Selecciona Desplegar. Espera hasta que el despliegue esté listo y seas redirigido a la página de Despliegues.
- Selecciona Abrir en playground para comenzar a interactuar con el modelo.
- Puedes regresar a la página de Despliegues, seleccionar el despliegue y anotar la URL del objetivo del endpoint y la Clave Secreta, que puedes usar para llamar al despliegue y generar completaciones.
- Siempre puedes encontrar los detalles del endpoint, URL y claves de acceso navegando a la pestaña Build y seleccionando Despliegues en la sección de Componentes.

> [!NOTE]
> Ten en cuenta que tu cuenta debe tener permisos de rol de Desarrollador de Azure AI en el Grupo de Recursos para realizar estos pasos.

## **5. Usar la API de Phi en Azure AI Foundry**

Puedes acceder a https://{Tu nombre de proyecto}.region.inference.ml.azure.com/swagger.json a través de una solicitud GET en Postman y combinarlo con la Clave para conocer las interfaces disponibles.

Puedes obtener fácilmente los parámetros de solicitud, así como los parámetros de respuesta.

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.