<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "80a853c08e4ee25ef9b4bfcedd8990da",
  "translation_date": "2025-07-16T23:17:13+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md",
  "language_code": "zh"
}
-->
# 在 Azure AI Foundry 中评估微调后的 Phi-3 / Phi-3.5 模型，聚焦微软的负责任 AI 原则

本端到端（E2E）示例基于微软技术社区的指南《[在 Azure AI Foundry 中评估微调后的 Phi-3 / 3.5 模型，聚焦微软的负责任 AI](https://techcommunity.microsoft.com/blog/educatordeveloperblog/evaluate-fine-tuned-phi-3--3-5-models-in-azure-ai-studio-focusing-on-microsofts-/4227850?WT.mc_id=aiml-137032-kinfeylo)》。

## 概述

### 如何在 Azure AI Foundry 中评估微调后的 Phi-3 / Phi-3.5 模型的安全性和性能？

模型微调有时可能导致意外或不理想的响应。为了确保模型保持安全且有效，评估模型生成有害内容的潜力以及其产生准确、相关且连贯回答的能力非常重要。在本教程中，您将学习如何评估集成了 Prompt flow 的微调 Phi-3 / Phi-3.5 模型在 Azure AI Foundry 中的安全性和性能。

以下是 Azure AI Foundry 的评估流程。

![教程架构。](../../../../../../translated_images/architecture.10bec55250f5d6a4e1438bb31c5c70309908e21e7ada24a621bbfdd8d0f834f4.zh.png)

*图片来源：[生成式 AI 应用评估](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> 如需更详细的信息及探索更多关于 Phi-3 / Phi-3.5 的资源，请访问 [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723)。

### 先决条件

- [Python](https://www.python.org/downloads)
- [Azure 订阅](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- 微调后的 Phi-3 / Phi-3.5 模型

### 目录

1. [**场景 1：Azure AI Foundry 的 Prompt flow 评估介绍**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [安全性评估介绍](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [性能评估介绍](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [**场景 2：在 Azure AI Foundry 中评估 Phi-3 / Phi-3.5 模型**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [开始之前](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [部署 Azure OpenAI 以评估 Phi-3 / Phi-3.5 模型](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [使用 Azure AI Foundry 的 Prompt flow 评估微调后的 Phi-3 / Phi-3.5 模型](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [恭喜！](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## **场景 1：Azure AI Foundry 的 Prompt flow 评估介绍**

### 安全性评估介绍

为了确保您的 AI 模型符合伦理且安全，评估其是否符合微软的负责任 AI 原则至关重要。在 Azure AI Foundry 中，安全性评估可以帮助您检测模型是否容易被绕过限制（jailbreak 攻击）以及其生成有害内容的潜力，这与这些原则直接相关。

![安全性评估。](../../../../../../translated_images/safety-evaluation.083586ec88dfa9500d3d25faf0720fd99cbf07c8c4b559dda5e70c84a0e2c1aa.zh.png)

*图片来源：[生成式 AI 应用评估](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### 微软的负责任 AI 原则

在开始技术步骤之前，理解微软的负责任 AI 原则非常重要。这是一套伦理框架，旨在指导 AI 系统的负责任开发、部署和运营。这些原则指导 AI 系统的设计、开发和部署，确保 AI 技术以公平、透明和包容的方式构建。这些原则是评估 AI 模型安全性的基础。

微软的负责任 AI 原则包括：

- **公平与包容**：AI 系统应公平对待所有人，避免对处境相似的群体产生不同影响。例如，当 AI 系统为医疗治疗、贷款申请或就业提供建议时，应对所有具有相似症状、财务状况或专业资格的人给出相同的建议。

- **可靠性与安全性**：为了建立信任，AI 系统必须可靠、安全且一致地运行。这些系统应能按设计正常工作，安全应对意外情况，并抵御有害操控。它们的行为及能处理的各种情况反映了开发者在设计和测试阶段预见的情境范围。

- **透明度**：当 AI 系统帮助做出对人们生活有重大影响的决策时，确保人们理解这些决策的依据至关重要。例如，银行可能使用 AI 系统判断一个人的信用状况，公司可能用 AI 系统筛选最合适的候选人。

- **隐私与安全**：随着 AI 的普及，保护隐私和保障个人及企业信息安全变得更加重要且复杂。AI 需要访问数据以做出准确且有依据的预测和决策，因此隐私和数据安全需特别关注。

- **问责制**：设计和部署 AI 系统的人必须对系统的运行负责。组织应借鉴行业标准制定问责规范，确保 AI 系统不会成为影响人们生活决策的最终权威，并确保人类对高度自主的 AI 系统保持有效控制。

![填充中心。](../
> [!NOTE]  
> 如果你按照“[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)”中描述的低代码方法操作，可以跳过本练习，直接进行下一个。  
> 但是，如果你是按照“[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)”中描述的代码优先方法来微调并部署你的 Phi-3 / Phi-3.5 模型，那么将模型连接到 Prompt flow 的流程会有所不同。你将在本练习中学习这一过程。
要继续操作，您需要将微调后的 Phi-3 / Phi-3.5 模型集成到 Azure AI Foundry 的 Prompt flow 中。

#### 创建 Azure AI Foundry Hub

在创建项目之前，您需要先创建一个 Hub。Hub 类似于资源组，方便您在 Azure AI Foundry 中组织和管理多个项目。

1. 登录 [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723)。

1. 从左侧标签中选择 **All hubs**。

1. 从导航菜单中选择 **+ New hub**。

    ![Create hub.](../../../../../../translated_images/create-hub.5be78fb1e21ffbf1aa9ecc232c2c95d337386f3cd0f361ca80c4475dc8aa2c7b.zh.png)

1. 执行以下操作：

    - 输入 **Hub name**，必须是唯一值。
    - 选择您的 Azure **Subscription**。
    - 选择要使用的 **Resource group**（如有需要可新建）。
    - 选择您想使用的 **Location**。
    - 选择要连接的 **Connect Azure AI Services**（如有需要可新建）。
    - 选择 **Connect Azure AI Search** 并选择 **Skip connecting**。

    ![Fill hub.](../../../../../../translated_images/fill-hub.baaa108495c71e3449667210a8ec5a0f3206bf2724ebacaa69cb09d3b12f29d3.zh.png)

1. 选择 **Next**。

#### 创建 Azure AI Foundry 项目

1. 在您创建的 Hub 中，从左侧标签选择 **All projects**。

1. 从导航菜单选择 **+ New project**。

    ![Select new project.](../../../../../../translated_images/select-new-project.cd31c0404088d7a32ee9018978b607dfb773956b15a88606f45579d3bc23c155.zh.png)

1. 输入 **Project name**，必须是唯一值。

    ![Create project.](../../../../../../translated_images/create-project.ca3b71298b90e42049ce8f6f452313bde644c309331fd728fcacd8954a20e26d.zh.png)

1. 选择 **Create a project**。

#### 为微调后的 Phi-3 / Phi-3.5 模型添加自定义连接

要将您的自定义 Phi-3 / Phi-3.5 模型集成到 Prompt flow 中，您需要将模型的端点和密钥保存到自定义连接中。这样可以确保 Prompt flow 能访问您的自定义模型。

#### 设置微调后的 Phi-3 / Phi-3.5 模型的 api key 和 endpoint uri

1. 访问 [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)。

1. 进入您创建的 Azure 机器学习工作区。

1. 从左侧标签选择 **Endpoints**。

    ![Select endpoints.](../../../../../../translated_images/select-endpoints.ee7387ecd68bd18d35cd7f235f930ebe99841a8c8c9dea2f608b7f43508576dd.zh.png)

1. 选择您创建的端点。

    ![Select endpoints.](../../../../../../translated_images/select-endpoint-created.9f63af5e4cf98b2ec92358f15ad36d69820e627c048f14c7ec3750fdbce3558b.zh.png)

1. 从导航菜单选择 **Consume**。

1. 复制您的 **REST endpoint** 和 **Primary key**。

    ![Copy api key and endpoint uri.](../../../../../../translated_images/copy-endpoint-key.0650c3786bd646ab0b5a80833917b7b8f32ee011c09af0459f3830dc25b00760.zh.png)

#### 添加自定义连接

1. 访问 [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723)。

1. 进入您创建的 Azure AI Foundry 项目。

1. 在项目中，从左侧标签选择 **Settings**。

1. 选择 **+ New connection**。

    ![Select new connection.](../../../../../../translated_images/select-new-connection.fa0f35743758a74b6c5dca5f37ca22939163f5c89eac47d1fd0a8c663bd5904a.zh.png)

1. 从导航菜单选择 **Custom keys**。

    ![Select custom keys.](../../../../../../translated_images/select-custom-keys.5a3c6b25580a9b67df43e8c5519124268b987d8cb77d6e5fe5631f116714bd47.zh.png)

1. 执行以下操作：

    - 选择 **+ Add key value pairs**。
    - 键名输入 **endpoint**，将从 Azure ML Studio 复制的端点粘贴到值字段。
    - 再次选择 **+ Add key value pairs**。
    - 键名输入 **key**，将从 Azure ML Studio 复制的密钥粘贴到值字段。
    - 添加完密钥后，选择 **is secret** 以防止密钥泄露。

    ![Add connection.](../../../../../../translated_images/add-connection.ac7f5faf8b10b0dfe6679422f479f88cc47c33cbf24568da138ab19fbb17dc4b.zh.png)

1. 选择 **Add connection**。

#### 创建 Prompt flow

您已在 Azure AI Foundry 中添加了自定义连接。接下来，按照以下步骤创建一个 Prompt flow，然后将其连接到自定义连接，以便在 Prompt flow 中使用微调模型。

1. 进入您创建的 Azure AI Foundry 项目。

1. 从左侧标签选择 **Prompt flow**。

1. 从导航菜单选择 **+ Create**。

    ![Select Promptflow.](../../../../../../translated_images/select-promptflow.18ff2e61ab9173eb94fbf771819d7ddf21e9c239f2689cb2684d4d3c739deb75.zh.png)

1. 从导航菜单选择 **Chat flow**。

    ![Select chat flow.](../../../../../../translated_images/select-flow-type.28375125ec9996d33a7d73eb77e59354e1b70fd246009e30bdd40db17143ec83.zh.png)

1. 输入要使用的 **Folder name**。

    ![Select chat flow.](../../../../../../translated_images/enter-name.02ddf8fb840ad4305ba88e0a804a5198ddd8720ebccb420d65ba13dcd481591f.zh.png)

1. 选择 **Create**。

#### 设置 Prompt flow 以与您的自定义 Phi-3 / Phi-3.5 模型聊天

您需要将微调后的 Phi-3 / Phi-3.5 模型集成到 Prompt flow 中。但现有的 Prompt flow 并非为此设计，因此您必须重新设计 Prompt flow 来实现自定义模型的集成。

1. 在 Prompt flow 中，执行以下操作以重建现有流程：

    - 选择 **Raw file mode**。
    - 删除 *flow.dag.yml* 文件中所有现有代码。
    - 将以下代码添加到 *flow.dag.yml*。

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

    - 选择 **Save**。

    ![Select raw file mode.](../../../../../../translated_images/select-raw-file-mode.06c1eca581ce4f5344b4801da9d695b3c1ea7019479754e566d2df495e868664.zh.png)

1. 将以下代码添加到 *integrate_with_promptflow.py*，以便在 Prompt flow 中使用自定义 Phi-3 / Phi-3.5 模型。

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

    ![Paste prompt flow code.](../../../../../../translated_images/paste-promptflow-code.cd6d95b101c0ec2818291eeeb2aa744d0e01320308a1fa6348ac7f51bec93de9.zh.png)

> [!NOTE]
> 
> 有关在 Azure AI Foundry 中使用 Prompt flow 的详细信息，请参阅 [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow)。

1. 选择 **Chat input** 和 **Chat output**，以启用与模型的聊天功能。

    ![Select Input Output.](../../../../../../translated_images/select-input-output.c187fc58f25fbfc339811bdd5a2285589fef803aded96b8c58b40131f0663571.zh.png)

1. 现在，您已准备好与自定义 Phi-3 / Phi-3.5 模型聊天。下一练习中，您将学习如何启动 Prompt flow 并使用它与微调模型对话。

> [!NOTE]
>
> 重建后的流程应如下图所示：
>
> ![Flow example](../../../../../../translated_images/graph-example.82fd1bcdd3fc545bcc81d64cb6542972ae593588ab94564c8c25edf06fae27fc.zh.png)
>

#### 启动 Prompt flow

1. 选择 **Start compute sessions** 启动 Prompt flow。

    ![Start compute session.](../../../../../../translated_images/start-compute-session.9acd8cbbd2c43df160358b6be6cad3e069a9c22271fd8b40addc847aeca83b44.zh.png)

1. 选择 **Validate and parse input** 以更新参数。

    ![Validate input.](../../../../../../translated_images/validate-input.c1adb9543c6495be3c94da090ce7c61a77cc8baf0718552e3d6e41b87eb96a41.zh.png)

1. 选择 **connection** 的 **Value**，即您创建的自定义连接，例如 *connection*。

    ![Connection.](../../../../../../translated_images/select-connection.1f2b59222bcaafefe7ac3726aaa2a7fdb04a5b969cd09f009acfe8b1e841efb6.zh.png)

#### 与您的自定义 Phi-3 / Phi-3.5 模型聊天

1. 选择 **Chat**。

    ![Select chat.](../../../../../../translated_images/select-chat.0406bd9687d0c49d8bf2b8145f603ed5616b71ba82a0eadde189275b88e50a3f.zh.png)

1. 以下是示例结果：现在您可以与自定义 Phi-3 / Phi-3.5 模型聊天。建议基于用于微调的数据提问。

    ![Chat with prompt flow.](../../../../../../translated_images/chat-with-promptflow.1cf8cea112359ada4628ea1d3d9f563f3e6df2c01cf917bade1a5eb9d197493a.zh.png)

### 部署 Azure OpenAI 以评估 Phi-3 / Phi-3.5 模型

要在 Azure AI Foundry 中评估 Phi-3 / Phi-3.5 模型，您需要部署一个 Azure OpenAI 模型。该模型将用于评估 Phi-3 / Phi-3.5 模型的性能。

#### 部署 Azure OpenAI

1. 登录 [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723)。

1. 进入您创建的 Azure AI Foundry 项目。

    ![Select Project.](../../../../../../translated_images/select-project-created.5221e0e403e2c9d6a17c809ad9aee8de593cd48717f157cc3eb2b29a37aa02ae.zh.png)

1. 在项目中，从左侧标签选择 **Deployments**。

1. 从导航菜单选择 **+ Deploy model**。

1. 选择 **Deploy base model**。

    ![Select Deployments.](../../../../../../translated_images/deploy-openai-model.95d812346b25834b05b20fe43c20130da7eae1e485ad60bb8e46bbc85a6c613a.zh.png)

1. 选择您想使用的 Azure OpenAI 模型，例如 **gpt-4o**。

    ![Select Azure OpenAI model you'd like to use.](../../../../../../translated_images/select-openai-model.959496d7e311546d66ec145dc4e0bf0cc806e6e5469b17e776788d6f5ba7a221.zh.png)

1. 选择 **Confirm**。

### 使用 Azure AI Foundry 的 Prompt flow 评估微调后的 Phi-3 / Phi-3.5 模型

### 开始新的评估

1. 访问 [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723)。

1. 进入您创建的 Azure AI Foundry 项目。

    ![Select Project.](../../../../../../translated_images/select-project-created.5221e0e403e2c9d6a17c809ad9aee8de593cd48717f157cc3eb2b29a37aa02ae.zh.png)

1. 在项目中，从左侧标签选择 **Evaluation**。

1. 从导航菜单选择 **+ New evaluation**。

    ![Select evaluation.](../../../../../../translated_images/select-evaluation.2846ad7aaaca7f4f2cd3f728b640e64eeb639dc5dcb52f2d651099576b894848.zh.png)

1. 选择 **Prompt flow** 评估。

    ![Select Prompt flow evaluation.](../../../../../../translated_images/promptflow-evaluation.cb9758cc19b4760f7a1ddda46bf47281cac59f2b1043f6a775a73977875f29a6.zh.png)

1. 执行以下操作：

    - 输入评估名称，必须唯一。
    - 选择任务类型为 **Question and answer without context**，因为本教程使用的 **ULTRACHAT_200k** 数据集不包含上下文。
    - 选择您想评估的 prompt flow。

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting1.4aa08259ff7a536e2e0e3011ff583f7164532d954a5ede4434fe9985cf51047e.zh.png)

1. 选择 **Next**。

1. 执行以下操作：

    - 选择 **Add your dataset** 上传数据集。例如，您可以上传测试数据集文件，如下载的 **ULTRACHAT_200k** 数据集中的 *test_data.json1*。
    - 选择与数据集匹配的 **Dataset column**。例如，使用 **ULTRACHAT_200k** 数据集时，选择 **${data.prompt}** 作为数据列。

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting2.07036831ba58d64ee622f9ee9b1c70f71b51cf39c3749dcd294414048c5b7e39.zh.png)

1. 选择 **Next**。

1. 配置性能和质量指标：

    - 选择您想使用的性能和质量指标。
    - 选择用于评估的 Azure OpenAI 模型，例如 **gpt-4o**。

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting3-1.d1ae69e3bf80914e68a0ad38486ca2d6c3ee5a30f4275f98fd3bc510c8d8f6d2.zh.png)

1. 配置风险和安全指标：

    - 选择您想使用的风险和安全指标。
    - 选择用于计算缺陷率的阈值，例如选择 **Medium**。
    - 对于 **question**，选择数据源为 **{$data.prompt}**。
    - 对于 **answer**，选择数据源为 **{$run.outputs.answer}**。
    - 对于 **ground_truth**，选择数据源为 **{$data.message}**。

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting3-2.d53bd075c60a45a2fab8ffb7e4dc28e8e544d2a093fbc9f63449a03984df98d9.zh.png)

1. 选择 **Next**。

1. 选择 **Submit** 开始评估。

1. 评估需要一些时间完成，您可以在 **Evaluation** 标签中监控进度。

### 查看评估结果
> [!NOTE]
> 下面展示的结果旨在说明评估过程。在本教程中，我们使用了一个在相对较小的数据集上微调的模型，因此结果可能不够理想。实际结果可能会因所用数据集的规模、质量和多样性，以及模型的具体配置而有较大差异。
评估完成后，您可以查看性能和安全指标的结果。

1. 性能和质量指标：

    - 评估模型生成连贯、流畅且相关响应的效果。

    ![Evaluation result.](../../../../../../translated_images/evaluation-result-gpu.85f48b42dfb7425434ec49685cff41376de3954fdab20f2a82c726f9fd690617.zh.png)

1. 风险和安全指标：

    - 确保模型输出安全，符合 Responsible AI Principles，避免任何有害或冒犯性内容。

    ![Evaluation result.](../../../../../../translated_images/evaluation-result-gpu-2.1b74e336118f4fd0589153bf7fb6269cd10aaeb10c1456bc76a06b93b2be15e6.zh.png)

1. 您可以向下滚动查看**详细指标结果**。

    ![Evaluation result.](../../../../../../translated_images/detailed-metrics-result.afa2f5c39a4f5f179c3916ba948feb367dfd4e0658752615be62824ef1dcf2d3.zh.png)

1. 通过对自定义的 Phi-3 / Phi-3.5 模型进行性能和安全指标的评估，您可以确认模型不仅有效，而且遵循负责任的 AI 实践，准备好投入实际应用。

## 恭喜！

### 您已完成本教程

您已成功评估了集成了 Prompt flow 的微调 Phi-3 模型，这是确保您的 AI 模型不仅表现优异，还遵守微软 Responsible AI 原则的重要步骤，帮助您构建值得信赖且可靠的 AI 应用。

![Architecture.](../../../../../../translated_images/architecture.10bec55250f5d6a4e1438bb31c5c70309908e21e7ada24a621bbfdd8d0f834f4.zh.png)

## 清理 Azure 资源

请清理您的 Azure 资源，以避免产生额外费用。登录 Azure 门户，删除以下资源：

- Azure 机器学习资源。
- Azure 机器学习模型端点。
- Azure AI Foundry 项目资源。
- Azure AI Foundry Prompt flow 资源。

### 后续步骤

#### 文档

- [使用 Responsible AI 仪表板评估 AI 系统](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [生成式 AI 的评估和监控指标](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Azure AI Foundry 文档](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Prompt flow 文档](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### 培训内容

- [微软 Responsible AI 方法介绍](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Azure AI Foundry 介绍](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### 参考资料

- [什么是 Responsible AI？](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [宣布 Azure AI 新工具，助您构建更安全、更可信的生成式 AI 应用](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [生成式 AI 应用的评估](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

**免责声明**：  
本文件使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始文件的母语版本应被视为权威来源。对于重要信息，建议使用专业人工翻译。对于因使用本翻译而产生的任何误解或误释，我们不承担任何责任。