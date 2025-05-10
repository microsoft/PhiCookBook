<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "80a853c08e4ee25ef9b4bfcedd8990da",
  "translation_date": "2025-05-09T16:14:56+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md",
  "language_code": "pa"
}
-->
# ਮਾਈਕ੍ਰੋਸਾਫਟ ਦੇ ਜ਼ਿੰਮੇਵਾਰ AI ਸਿਧਾਂਤਾਂ 'ਤੇ ਧਿਆਨ ਕੇਂਦਰਿਤ ਕਰਦਿਆਂ Azure AI Foundry ਵਿੱਚ Fine-tuned Phi-3 / Phi-3.5 ਮਾਡਲ ਦੀ ਮੁਲਾਂਕਣ ਕਰੋ

ਇਹ ਐਂਡ-ਟੂ-ਐਂਡ (E2E) ਨਮੂਨਾ Microsoft Tech Community ਦੇ "[Evaluate Fine-tuned Phi-3 / 3.5 Models in Azure AI Foundry Focusing on Microsoft's Responsible AI](https://techcommunity.microsoft.com/blog/educatordeveloperblog/evaluate-fine-tuned-phi-3--3-5-models-in-azure-ai-studio-focusing-on-microsofts-/4227850?WT.mc_id=aiml-137032-kinfeylo)" ਗਾਈਡ 'ਤੇ ਆਧਾਰਿਤ ਹੈ।

## ਓਵਰਵਿਊ

### ਤੁਸੀਂ Azure AI Foundry ਵਿੱਚ Fine-tuned Phi-3 / Phi-3.5 ਮਾਡਲ ਦੀ ਸੁਰੱਖਿਆ ਅਤੇ ਪ੍ਰਦਰਸ਼ਨ ਨੂੰ ਕਿਵੇਂ ਮੁਲਾਂਕਣ ਕਰ ਸਕਦੇ ਹੋ?

ਮਾਡਲ ਨੂੰ ਫਾਈਨ-ਟਿਊਨ ਕਰਨਾ ਕਈ ਵਾਰ ਅਣਚਾਹੇ ਜਾਂ ਅਣਕਾਮਯਾਬ ਜਵਾਬਾਂ ਦਾ ਕਾਰਨ ਬਣ ਸਕਦਾ ਹੈ। ਇਹ ਯਕੀਨੀ ਬਣਾਉਣ ਲਈ ਕਿ ਮਾਡਲ ਸੁਰੱਖਿਅਤ ਅਤੇ ਪ੍ਰਭਾਵਸ਼ালী ਰਹੇ, ਇਸ ਦੀ ਸਮਰੱਥਾ ਦਾ ਮੁਲਾਂਕਣ ਕਰਨਾ ਜਰੂਰੀ ਹੈ ਕਿ ਇਹ ਨੁਕਸਾਨਦਾਇਕ ਸਮੱਗਰੀ ਬਣਾਉਣ ਦੀ ਸੰਭਾਵਨਾ ਰੱਖਦਾ ਹੈ ਜਾਂ ਨਹੀਂ ਅਤੇ ਇਹ ਸਹੀ, ਸਬੰਧਤ ਅਤੇ ਸੁਚੱਜੇ ਜਵਾਬ ਦੇ ਸਕਦਾ ਹੈ। ਇਸ ਟਿਊਟੋਰਿਅਲ ਵਿੱਚ, ਤੁਸੀਂ ਸਿੱਖੋਗੇ ਕਿ Azure AI Foundry ਵਿੱਚ Prompt flow ਨਾਲ ਇੰਟਿਗ੍ਰੇਟ ਕੀਤੇ Fine-tuned Phi-3 / Phi-3.5 ਮਾਡਲ ਦੀ ਸੁਰੱਖਿਆ ਅਤੇ ਪ੍ਰਦਰਸ਼ਨ ਨੂੰ ਕਿਵੇਂ ਮੁਲਾਂਕਣ ਕਰਨਾ ਹੈ।

ਇੱਥੇ Azure AI Foundry ਦਾ ਮੁਲਾਂਕਣ ਪ੍ਰਕਿਰਿਆ ਦਿੱਤੀ ਗਈ ਹੈ।

![Architecture of tutorial.](../../../../../../translated_images/architecture.99df2035c1c1a82e7f7d3aa3368e5940e46d27d35abd498166e55094298fce81.pa.png)

*ਚਿੱਤਰ ਸਰੋਤ: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> Phi-3 / Phi-3.5 ਬਾਰੇ ਹੋਰ ਵਿਸਥਾਰਿਤ ਜਾਣਕਾਰੀ ਅਤੇ ਵਾਧੂ ਸਰੋਤਾਂ ਲਈ, ਕਿਰਪਾ ਕਰਕੇ [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723) ਵੇਖੋ।

### ਲੋੜੀਂਦੀਆਂ ਚੀਜ਼ਾਂ

- [Python](https://www.python.org/downloads)
- [Azure subscription](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- Fine-tuned Phi-3 / Phi-3.5 ਮਾਡਲ

### ਸਮੱਗਰੀ ਦੀ ਸੂਚੀ

1. [**ਸਕੈਨਾਰੀਓ 1: Azure AI Foundry ਦੇ Prompt flow ਮੁਲਾਂਕਣ ਦਾ ਪਰਿਚਯ**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [ਸੁਰੱਖਿਆ ਮੁਲਾਂਕਣ ਦਾ ਪਰਿਚਯ](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [ਪ੍ਰਦਰਸ਼ਨ ਮੁਲਾਂਕਣ ਦਾ ਪਰਿਚਯ](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [**ਸਕੈਨਾਰੀਓ 2: Azure AI Foundry ਵਿੱਚ Phi-3 / Phi-3.5 ਮਾਡਲ ਦਾ ਮੁਲਾਂਕਣ**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [ਸ਼ੁਰੂ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Phi-3 / Phi-3.5 ਮਾਡਲ ਦਾ ਮੁਲਾਂਕਣ ਕਰਨ ਲਈ Azure OpenAI ਨੂੰ ਡਿਪਲੌਏ ਕਰੋ](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Azure AI Foundry ਦੇ Prompt flow ਮੁਲਾਂਕਣ ਨਾਲ Fine-tuned Phi-3 / Phi-3.5 ਮਾਡਲ ਦਾ ਮੁਲਾਂਕਣ ਕਰੋ](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [ਮੁਬਾਰਕਾਂ!](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## **ਸਕੈਨਾਰੀਓ 1: Azure AI Foundry ਦੇ Prompt flow ਮੁਲਾਂਕਣ ਦਾ ਪਰਿਚਯ**

### ਸੁਰੱਖਿਆ ਮੁਲਾਂਕਣ ਦਾ ਪਰਿਚਯ

ਇਹ ਯਕੀਨੀ ਬਣਾਉਣ ਲਈ ਕਿ ਤੁਹਾਡਾ AI ਮਾਡਲ ਨੈਤਿਕ ਅਤੇ ਸੁਰੱਖਿਅਤ ਹੈ, ਇਹ ਜਰੂਰੀ ਹੈ ਕਿ ਤੁਸੀਂ ਇਸਨੂੰ Microsoft ਦੇ ਜ਼ਿੰਮੇਵਾਰ AI ਸਿਧਾਂਤਾਂ ਦੇ ਖਿਲਾਫ ਮੁਲਾਂਕਣ ਕਰੋ। Azure AI Foundry ਵਿੱਚ, ਸੁਰੱਖਿਆ ਮੁਲਾਂਕਣ ਤੁਹਾਨੂੰ ਮਾਡਲ ਦੀ jailbreak ਹਮਲਿਆਂ ਵੱਲ ਸੰਵੇਦਨਸ਼ੀਲਤਾ ਅਤੇ ਨੁਕਸਾਨਦਾਇਕ ਸਮੱਗਰੀ ਬਣਾਉਣ ਦੀ ਸੰਭਾਵਨਾ ਦਾ ਮੁਲਾਂਕਣ ਕਰਨ ਦਿੰਦੇ ਹਨ, ਜੋ ਸਿੱਧੇ ਤੌਰ 'ਤੇ ਇਨ੍ਹਾਂ ਸਿਧਾਂਤਾਂ ਨਾਲ ਮੇਲ ਖਾਂਦੇ ਹਨ।

![Safaty evaluation.](../../../../../../translated_images/safety-evaluation.91fdef98588aadf56e8043d04cd78d24aac1472d6c121a6289f60d50d1f33d42.pa.png)

*ਚਿੱਤਰ ਸਰੋਤ: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Microsoft ਦੇ ਜ਼ਿੰਮੇਵਾਰ AI ਸਿਧਾਂਤ

ਤਕਨੀਕੀ ਕਦਮ ਸ਼ੁਰੂ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ, Microsoft ਦੇ ਜ਼ਿੰਮੇਵਾਰ AI ਸਿਧਾਂਤਾਂ ਨੂੰ ਸਮਝਣਾ ਜਰੂਰੀ ਹੈ, ਜੋ ਕਿ AI ਸਿਸਟਮਾਂ ਦੀ ਜ਼ਿੰਮੇਵਾਰ ਵਿਕਾਸ, ਤਾਇਨਾਤੀ ਅਤੇ ਚਲਾਉਣ ਲਈ ਇੱਕ ਨੈਤਿਕ ਢਾਂਚਾ ਹੈ। ਇਹ ਸਿਧਾਂਤ AI ਸਿਸਟਮਾਂ ਦੇ ਜ਼ਿੰਮੇਵਾਰ ਡਿਜ਼ਾਈਨ, ਵਿਕਾਸ ਅਤੇ ਤਾਇਨਾਤੀ ਨੂੰ ਮਦਦ ਕਰਦੇ ਹਨ, ਇਹ ਯਕੀਨੀ ਬਣਾਉਂਦੇ ਹਨ ਕਿ AI ਤਕਨੀਕਾਂ ਇਨਸਾਫ਼, ਪਾਰਦਰਸ਼ੀ ਅਤੇ ਸ਼ਾਮਿਲ ਕਰਦੀਆਂ ਹਨ। ਇਹ ਸਿਧਾਂਤ AI ਮਾਡਲਾਂ ਦੀ ਸੁਰੱਖਿਆ ਮੁਲਾਂਕਣ ਲਈ ਬੁਨਿਆਦ ਹਨ।

Microsoft ਦੇ ਜ਼ਿੰਮੇਵਾਰ AI ਸਿਧਾਂਤ ਵਿੱਚ ਸ਼ਾਮਲ ਹਨ:

- **ਇਨਸਾਫ਼ ਅਤੇ ਸ਼ਾਮਿਲਤਾ**: AI ਸਿਸਟਮਾਂ ਨੂੰ ਹਰ ਕਿਸੇ ਨਾਲ ਇਨਸਾਫ਼ ਨਾਲ ਪੇਸ਼ ਆਉਣਾ ਚਾਹੀਦਾ ਹੈ ਅਤੇ ਸਮਾਨ ਹਾਲਾਤ ਵਾਲੇ ਸਮੂਹਾਂ ਨੂੰ ਵੱਖ-ਵੱਖ ਤਰੀਕਿਆਂ ਨਾਲ ਪ੍ਰਭਾਵਿਤ ਨਹੀਂ ਕਰਨਾ ਚਾਹੀਦਾ। ਉਦਾਹਰਨ ਵਜੋਂ, ਜਦੋਂ AI ਸਿਸਟਮ ਮੈਡੀਕਲ ਇਲਾਜ, ਲੋਨ ਅਰਜ਼ੀਆਂ ਜਾਂ ਨੌਕਰੀ ਲਈ ਮਦਦ ਕਰਦੇ ਹਨ, ਤਾਂ ਉਹ ਉਹਨਾਂ ਸਭ ਨੂੰ ਇੱਕੋ ਜਿਹੇ ਸੁਝਾਅ ਦੇਣ ਜੋੜੇ ਜੋ ਸਮਾਨ ਲੱਛਣ, ਵਿੱਤੀ ਹਾਲਾਤ ਜਾਂ ਪੇਸ਼ੇਵਰ ਯੋਗਤਾਵਾਂ ਰੱਖਦੇ ਹਨ।

- **ਭਰੋਸੇਯੋਗਤਾ ਅਤੇ ਸੁਰੱਖਿਆ**: ਭਰੋਸਾ ਬਣਾਉਣ ਲਈ, ਇਹ ਜਰੂਰੀ ਹੈ ਕਿ AI ਸਿਸਟਮ ਭਰੋਸੇਯੋਗ, ਸੁਰੱਖਿਅਤ ਅਤੇ ਲਗਾਤਾਰ ਕੰਮ ਕਰਨ। ਇਹ ਸਿਸਟਮ ਉਸ ਤਰੀਕੇ ਨਾਲ ਕੰਮ ਕਰਨ ਜੋ ਉਹ ਪਹਿਲਾਂ ਬਣਾਏ ਗਏ ਸਨ, ਅਣਪੇਸ਼ਕਸ਼ਿਤ ਹਾਲਾਤਾਂ ਵਿੱਚ ਸੁਰੱਖਿਅਤ ਜਵਾਬ ਦੇਣ ਅਤੇ ਨੁਕਸਾਨਦਾਇਕ ਚਾਲਾਂ ਤੋਂ ਬਚਣ ਯੋਗ ਹੋਣ। ਉਹ ਕਿਸ ਤਰ੍ਹਾਂ ਵਰਤਦੇ ਹਨ ਅਤੇ ਕਿਹੜੇ ਹਾਲਾਤ ਸੰਭਾਲ ਸਕਦੇ ਹਨ, ਇਹ ਵਿਕਾਸਕਾਰਾਂ ਨੇ ਡਿਜ਼ਾਈਨ ਅਤੇ ਟੈਸਟਿੰਗ ਦੌਰਾਨ ਸੋਚੇ ਹੋਏ ਹਾਲਾਤਾਂ ਨੂੰ ਦਰਸਾਉਂਦਾ ਹੈ।

- **ਪਾਰਦਰਸ਼ਤਾ**: ਜਦੋਂ AI ਸਿਸਟਮ ਲੋਕਾਂ ਦੀ ਜ਼ਿੰਦਗੀ 'ਤੇ ਵੱਡੇ ਪ੍ਰਭਾਵ ਵਾਲੇ ਫੈਸਲੇ ਕਰਨ ਵਿੱਚ ਮਦਦ ਕਰਦੇ ਹਨ, ਤਾਂ ਲੋਕਾਂ ਲਈ ਇਹ ਸਮਝਣਾ ਜਰੂਰੀ ਹੁੰਦਾ ਹੈ ਕਿ ਇਹ ਫੈਸਲੇ ਕਿਵੇਂ ਲਏ ਗਏ। ਉਦਾਹਰਨ ਵਜੋਂ, ਇੱਕ ਬੈਂਕ AI ਸਿਸਟਮ ਦੀ ਵਰਤੋਂ ਕਰ ਸਕਦੀ ਹੈ ਇਹ ਨਿਰਣੇ ਲਈ ਕਿ ਕੋਈ ਵਿਅਕਤੀ ਕਰਜ਼ਾ ਲਾਇਕ ਹੈ ਜਾਂ ਨਹੀਂ। ਇੱਕ ਕੰਪਨੀ AI ਸਿਸਟਮ ਦੀ ਵਰਤੋਂ ਕਰ ਸਕਦੀ ਹੈ ਸਭ ਤੋਂ ਯੋਗ ਉਮੀਦਵਾਰਾਂ ਦੀ ਚੋਣ ਕਰਨ ਲਈ।

- **ਪ੍ਰਾਈਵੇਸੀ ਅਤੇ ਸੁਰੱਖਿਆ**: ਜਿਵੇਂ AI ਵਧਦਾ ਜਾ ਰਿਹਾ ਹੈ, ਪ੍ਰਾਈਵੇਸੀ ਦੀ ਰੱਖਿਆ ਅਤੇ ਨਿੱਜੀ ਅਤੇ ਵਪਾਰਕ ਜਾਣਕਾਰੀ ਦੀ ਸੁਰੱਖਿਆ ਹੋਰ ਜ਼ਰੂਰੀ ਅਤੇ ਜਟਿਲ ਹੋ ਰਹੀ ਹੈ। AI ਨਾਲ, ਪ੍ਰਾਈਵੇਸੀ ਅਤੇ ਡਾਟਾ ਸੁਰੱਖਿਆ 'ਤੇ ਖਾਸ ਧਿਆਨ ਦੇਣਾ ਲਾਜ਼ਮੀ ਹੈ ਕਿਉਂਕਿ ਡਾਟਾ ਤੱਕ ਪਹੁੰਚ AI ਸਿਸਟਮਾਂ ਨੂੰ ਲੋਕਾਂ ਬਾਰੇ ਸਹੀ ਅਤੇ ਜਾਣੂ ਅੰਦਾਜ਼ੇ ਅਤੇ ਫੈਸਲੇ ਕਰਨ ਲਈ ਲੋੜੀਂਦੀ ਹੈ।

- **ਜਵਾਬਦੇਹੀ**: ਜਿਹੜੇ ਲੋਕ AI ਸਿਸਟਮ ਡਿਜ਼ਾਈਨ ਅਤੇ ਤਾਇਨਾਤ ਕਰਦੇ ਹਨ, ਉਹਨਾਂ ਨੂੰ ਆਪਣੇ ਸਿਸਟਮਾਂ ਦੇ ਕੰਮ ਕਰਨ ਲਈ ਜਵਾਬਦੇਹ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ। ਸੰਸਥਾਵਾਂ ਨੂੰ ਉਦਯੋਗ ਮਿਆਰਾਂ ਨੂੰ ਧਿਆਨ ਵਿੱਚ ਰੱਖ ਕੇ ਜਵਾਬਦੇਹੀ ਦੇ ਨਿਯਮ ਬਣਾਉਣੇ ਚਾਹੀਦੇ ਹਨ। ਇਹ ਨਿਯਮ ਇਹ ਯਕੀਨੀ ਬਣਾਉਂਦੇ ਹਨ ਕਿ AI ਸਿਸਟਮ ਲੋਕਾਂ ਦੀ ਜ਼ਿੰਦਗੀ 'ਤੇ ਪ੍ਰਭਾਵ ਪਾਉਣ ਵਾਲੇ ਕਿਸੇ ਵੀ ਫੈਸਲੇ ਦਾ ਆਖਰੀ ਅਧਿਕਾਰੀ ਨਾ ਹੋਣ। ਇਹ ਇਹ ਵੀ ਯਕੀਨੀ ਬਣਾਉਂਦੇ ਹਨ ਕਿ ਮਨੁੱਖੀ ਹੱਥਾਂ ਕੋਲ ਅਜੇ ਵੀ ਉਹਨਾਂ ਬਹੁਤ ਜ਼ਿਆਦਾ ਖੁਦਮੁਖਤਿਆਰ AI ਸਿਸਟਮਾਂ 'ਤੇ ਮਾਇਨੇਦਾਰ ਨਿਯੰਤਰਣ ਹੋਵੇ।

![Fill hub.](../../../../../../translated_images/responsibleai2.93a32c6cd88ec3e57ec73a8c81717cd74ba27d2cd6d500097c82d79ac49726d7.pa.png)

*ਚਿੱਤਰ ਸਰੋਤ: [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> Microsoft ਦੇ ਜ਼ਿੰਮੇਵਾਰ AI ਸਿਧਾਂਤਾਂ ਬਾਰੇ ਹੋਰ ਜਾਣਨ ਲਈ, ਕਿਰਪਾ ਕਰਕੇ [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723) ਵੇਖੋ।

#### ਸੁਰੱਖਿਆ ਮੈਟਰਿਕਸ

ਇਸ ਟਿਊਟੋਰਿਅਲ ਵਿੱਚ, ਤੁਸੀਂ Azure AI Foundry ਦੇ ਸੁਰੱਖਿਆ ਮੈਟਰਿਕਸ ਦੀ ਵਰਤੋਂ ਕਰਕੇ Fine-tuned Phi-3 ਮਾਡਲ ਦੀ ਸੁਰੱਖਿਆ ਦਾ ਮੁਲਾਂਕਣ ਕਰੋਗੇ। ਇਹ ਮੈਟਰਿਕਸ ਤੁਹਾਨੂੰ ਮਾਡਲ ਦੀ ਨੁਕਸਾਨਦਾਇਕ ਸਮੱਗਰੀ ਬਣਾਉਣ ਦੀ ਸੰਭਾਵਨਾ ਅਤੇ jailbreak ਹਮਲਿਆਂ ਵੱਲ ਇਸ ਦੀ ਸੰਵੇਦਨਸ਼ੀਲਤਾ ਦਾ ਮੁਲਾਂਕਣ ਕਰਨ ਵਿੱਚ ਮਦਦ ਕਰਦੇ ਹਨ। ਸੁਰੱਖਿਆ ਮੈਟਰਿਕਸ ਵਿੱਚ ਸ਼ਾਮਲ ਹਨ:

- **ਆਤਮ-ਹਾਨੀ ਨਾਲ ਸੰਬੰਧਿਤ ਸਮੱਗਰੀ**: ਮੁਲਾਂਕਣ ਕਰਦਾ ਹੈ ਕਿ ਮਾਡਲ ਵਿੱਚ ਆਤਮ-ਹਾਨੀ ਨਾਲ ਸੰਬੰਧਿਤ ਸਮੱਗਰੀ ਬਣਾਉਣ ਦੀ ਰੁਝਾਨ ਹੈ ਜਾਂ ਨਹੀਂ।
- **ਘਿਣਾਵਣੀ ਅਤੇ ਅਨਿਆਇਕ ਸਮੱਗਰੀ**: ਮੁਲਾਂਕਣ ਕਰਦਾ ਹੈ ਕਿ ਮਾਡਲ ਵਿੱਚ ਘਿਣਾਵਣੀ ਜਾਂ ਅਨਿਆਇਕ ਸਮੱਗਰੀ ਬਣਾਉਣ ਦੀ ਰੁਝਾਨ ਹੈ ਜਾਂ ਨਹੀਂ।
- **ਹਿੰਸਕ ਸਮੱਗਰੀ**: ਮੁਲਾਂਕਣ ਕਰਦਾ ਹੈ ਕਿ ਮਾਡਲ ਵਿੱਚ ਹਿੰਸਕ ਸਮੱਗਰੀ ਬਣਾਉਣ ਦੀ ਰੁਝਾਨ ਹੈ ਜਾਂ ਨਹੀਂ।
- **ਯੌਨ ਸਮੱਗਰੀ**: ਮੁਲਾਂਕਣ ਕਰਦਾ ਹੈ ਕਿ ਮਾਡਲ ਵਿੱਚ ਅਣਚਾਹੀ ਯੌਨ ਸਮੱਗਰੀ ਬਣਾਉਣ ਦੀ ਰੁਝਾਨ ਹੈ ਜਾਂ ਨਹੀਂ।

ਇਨ੍ਹਾਂ ਪੱਖਾਂ ਦਾ ਮੁਲਾਂਕਣ ਇਹ ਯਕੀਨੀ ਬਣਾਉਂਦਾ ਹੈ ਕਿ AI ਮਾਡਲ ਨੁਕਸਾਨਦਾਇਕ ਜਾਂ ਆਪਤੀਜਨਕ ਸਮੱਗਰੀ ਨਹੀਂ ਬਣਾਉਂਦਾ, ਜੋ ਸਮਾਜਿਕ ਮੁੱਲਾਂ ਅਤੇ ਨਿਯਮਾਂ ਦੇ ਅਨੁਕੂਲ ਹੈ।

![Evaluate based on safety.](../../../../../../translated_images/evaluate-based-on-safety.3def6d9c7edaa49c536a7e58bfa48e2676fe911e80e847b732c0c9688c19946c.pa.png)

### ਪ੍ਰਦਰਸ਼ਨ ਮੁਲਾਂਕਣ ਦਾ ਪਰਿਚਯ

ਇਹ ਯਕੀਨੀ ਬਣਾਉਣ ਲਈ ਕਿ ਤੁਹਾਡਾ AI ਮਾਡਲ ਉਮੀਦ ਮੁਤਾਬਕ ਕੰਮ ਕਰ ਰਿਹਾ ਹੈ, ਇਹ ਜਰੂਰੀ ਹੈ ਕਿ ਤੁਸੀਂ ਇਸਦਾ ਪ੍ਰਦਰਸ਼ਨ ਪ੍ਰਦਰਸ਼ਨ ਮੈਟਰਿਕਸ ਦੇ ਖਿਲਾਫ ਮੁਲਾਂਕਣ ਕਰੋ। Azure AI Foundry ਵਿੱਚ, ਪ੍ਰਦਰਸ਼ਨ ਮੁਲਾਂਕਣ ਤੁਹਾਨੂੰ ਮਾਡਲ ਦੀ ਪ੍ਰਭਾਵਸ਼ੀਲਤਾ ਦਾ ਮੁਲਾਂਕਣ ਕਰਨ ਦਿੰਦਾ ਹੈ ਕਿ ਇਹ ਸਹੀ, ਸਬੰਧਤ ਅਤੇ ਸੁਚੱਜੇ ਜਵਾਬ ਕਿੰਨੇ ਚੰਗੇ ਤਰੀਕੇ ਨਾਲ ਪੈਦਾ ਕਰਦਾ ਹੈ।

![Safaty evaluation.](../../../../../../translated_images/performance-evaluation.692eccfdea40b8a399040a6304cfee03667b5a9a0636a7152565d806427ff6be.pa.png)

*ਚਿੱਤਰ ਸਰੋਤ: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### ਪ੍ਰਦਰਸ਼ਨ ਮੈਟਰਿਕਸ

ਇਸ ਟਿਊਟੋਰਿਅਲ ਵਿੱਚ, ਤੁਸੀਂ Azure AI Foundry ਦੇ ਪ੍ਰਦਰਸ਼ਨ ਮੈਟਰਿਕਸ ਦੀ ਵਰਤੋਂ ਕਰਕੇ Fine-tuned Phi-3 / Phi-3.5 ਮਾਡਲ ਦਾ ਪ੍ਰਦਰਸ਼ਨ ਮੁਲਾਂਕਣ ਕਰੋਗੇ। ਇਹ ਮੈਟਰਿਕਸ ਤੁਹਾਨੂੰ ਮਾਡਲ ਦੀ ਪ੍ਰਭਾਵਸ਼ੀਲਤਾ ਦਾ ਮੁਲਾਂਕਣ ਕਰਨ ਵਿੱਚ ਮਦਦ ਕਰਦੇ ਹਨ ਕਿ ਇਹ ਸਹੀ, ਸਬੰਧਤ ਅਤੇ ਸੁਚੱਜੇ ਜਵਾਬ ਕਿੰਨੇ ਚੰਗੇ ਤਰੀਕੇ ਨਾਲ ਪੈਦਾ ਕਰਦਾ ਹੈ। ਪ੍ਰਦਰਸ਼ਨ ਮੈਟਰਿਕਸ ਵਿੱਚ ਸ਼ਾਮਲ ਹਨ:

- **Groundedness**: ਮੁਲਾਂਕਣ ਕਰਦਾ ਹੈ ਕਿ ਪੈਦਾ ਕੀਤੇ ਜਵਾਬ ਇਨਪੁਟ ਸਰੋਤ ਦੀ ਜਾਣਕਾਰੀ ਨਾਲ ਕਿੰਨੇ ਮੇਲ ਖਾਂਦੇ ਹਨ।
- **Relevance**: ਮੁਲਾਂਕਣ ਕਰਦਾ ਹੈ ਕਿ ਜਵਾਬ ਦਿੱਤੇ ਗਏ ਸਵਾਲਾਂ ਨਾਲ ਕਿੰਨੇ ਸਬੰਧਤ ਹਨ।
- **Coherence**: ਮੁਲਾਂਕਣ ਕਰਦਾ ਹੈ ਕਿ ਪੈਦਾ ਕੀਤਾ ਲਿਖਤ ਕਿਵੇਂ ਸੁਚੱਜਾ, ਕੁਦਰਤੀ ਅਤੇ ਮਨੁੱਖੀ ਬੋਲਚਾਲ ਵਰਗਾ ਹੈ।
- **Fluency**: ਮੁਲਾਂਕਣ ਕਰਦਾ ਹੈ ਕਿ ਪੈਦਾ ਕੀਤਾ ਲਿਖਤ ਭਾਸ਼ਾ ਦੱਖਲ ਵਿੱਚ ਕਿੰਨਾ ਪ੍ਰਵੀਂਨ ਹੈ।
- **GPT Similarity**: ਪੈਦਾ ਕੀਤੇ ਜਵਾਬ ਦੀ ਮੂਲ ਸੱਚਾਈ ਨਾਲ ਮਿਲਾਪ ਦੀ ਤੁਲਨਾ ਕਰਦਾ ਹੈ।
- **F1 Score**: ਪੈਦਾ ਕੀਤੇ ਜਵਾਬ ਅਤੇ ਸਰੋਤ ਡਾਟਾ ਵਿੱਚ ਸਾਂਝੇ ਸ਼ਬਦਾਂ ਦਾ ਅਨੁਪਾਤ ਕੈਲਕੁਲੇਟ ਕਰਦਾ ਹੈ।

ਇਹ ਮੈਟਰਿਕਸ ਤੁਹਾਨੂੰ ਮਾਡਲ ਦੀ ਪ੍ਰਭਾਵਸ਼ੀਲਤਾ ਦਾ ਮੁਲਾਂਕਣ ਕਰਨ ਵਿੱਚ ਮਦਦ ਕਰਦੇ ਹਨ ਕਿ ਇਹ ਸਹੀ, ਸਬੰਧਤ ਅਤੇ ਸੁਚੱਜੇ ਜਵਾਬ ਪੈਦਾ ਕਰਦਾ ਹੈ।

![Evaluate based on performance.](../../../../../../translated_images/evaluate-based-on-performance.16c477bfd4e547f34dd803492ce032fbdb3376a5dbd236042233e21e5b7f7f6a.pa.png)

## **ਸਕੈਨਾਰੀਓ 2: Azure AI Foundry ਵਿੱਚ Phi-3 / Phi-3.5 ਮਾਡਲ ਦਾ ਮੁਲਾਂਕਣ**

### ਸ਼ੁਰੂ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ

ਇਹ ਟਿਊਟੋਰਿਅਲ ਪਹਿਲਾਂ ਦੇ ਬਲੌਗ ਪੋਸਟਾਂ "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" ਅਤੇ "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)" ਦਾ ਜਾਰੀ ਹੈ। ਇਨ੍ਹਾਂ ਪੋਸਟਾਂ ਵਿੱਚ, ਅਸੀਂ Azure AI Foundry ਵਿੱਚ Phi-3 / Phi-3.5 ਮਾਡਲ ਨੂੰ ਫਾਈਨ-ਟਿਊਨ ਕਰਨ ਅਤੇ Prompt flow ਨਾਲ ਇੰਟਿਗ੍ਰੇਟ ਕਰਨ ਦੀ ਪ੍ਰਕਿਰਿਆ ਦਿਖਾਈ।

ਇਸ ਟਿਊਟੋਰਿਅਲ ਵਿੱਚ, ਤੁਸੀਂ Azure AI Foundry ਵਿੱਚ ਇੱਕ Azure OpenAI ਮਾਡਲ ਨੂੰ ਮੁਲਾਂ
![Fill hub.](../../../../../../translated_images/fill-hub.bb8b648703e968da13d123e40a6fc76f2193f6c6b432d24036d2aa9e823ee813.pa.png)

1. **Next** ਚੁਣੋ।

#### Azure AI Foundry ਪ੍ਰੋਜੈਕਟ ਬਣਾਓ

1. ਜਿਸ Hub ਨੂੰ ਤੁਸੀਂ ਬਣਾਇਆ ਹੈ, ਉਸ ਵਿੱਚ ਖੱਬੇ ਪਾਸੇ ਟੈਬ ਤੋਂ **All projects** ਚੁਣੋ।

1. ਨੈਵੀਗੇਸ਼ਨ ਮੀਨੂ ਤੋਂ **+ New project** ਚੁਣੋ।

    ![Select new project.](../../../../../../translated_images/select-new-project.1b9270456fbb8d598938036c6bd26247ea39c8b9ad76be16c81df57d54ce78ed.pa.png)

1. **Project name** ਦਰਜ ਕਰੋ। ਇਹ ਇਕ ਵਿਲੱਖਣ ਮੁੱਲ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ।

    ![Create project.](../../../../../../translated_images/create-project.8378d7842c49702498ba20f0553cbe91ff516275c8514ec865799669f9becbff.pa.png)

1. **Create a project** ਚੁਣੋ।

#### ਫਾਈਨ-ਟਿਊਨ ਕੀਤੇ Phi-3 / Phi-3.5 ਮਾਡਲ ਲਈ ਕਸਟਮ ਕਨੈਕਸ਼ਨ ਸ਼ਾਮਲ ਕਰੋ

ਆਪਣੇ ਕਸਟਮ Phi-3 / Phi-3.5 ਮਾਡਲ ਨੂੰ Prompt flow ਨਾਲ ਜੋੜਨ ਲਈ, ਤੁਹਾਨੂੰ ਮਾਡਲ ਦੇ endpoint ਅਤੇ key ਨੂੰ ਇੱਕ ਕਸਟਮ ਕਨੈਕਸ਼ਨ ਵਿੱਚ ਸੇਵ ਕਰਨਾ ਪਵੇਗਾ। ਇਹ ਸੈਟਅਪ ਤੁਹਾਡੇ ਕਸਟਮ ਮਾਡਲ ਤੱਕ Prompt flow ਵਿੱਚ ਪਹੁੰਚ ਨੂੰ ਯਕੀਨੀ ਬਣਾਉਂਦਾ ਹੈ।

#### ਫਾਈਨ-ਟਿਊਨ ਕੀਤੇ Phi-3 / Phi-3.5 ਮਾਡਲ ਦਾ api key ਅਤੇ endpoint uri ਸੈਟ ਕਰੋ

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) 'ਤੇ ਜਾਓ।

1. ਉਸ Azure Machine learning ਵਰਕਸਪੇਸ ਤੇ ਜਾਓ ਜੋ ਤੁਸੀਂ ਬਣਾਇਆ ਹੈ।

1. ਖੱਬੇ ਪਾਸੇ ਟੈਬ ਤੋਂ **Endpoints** ਚੁਣੋ।

    ![Select endpoints.](../../../../../../translated_images/select-endpoints.fc2852aa73fdb1531682b599c0b1f5b39a842f0a60fec7c8e941b3070ec6c463.pa.png)

1. ਬਣਾਇਆ ਗਿਆ endpoint ਚੁਣੋ।

    ![Select endpoints.](../../../../../../translated_images/select-endpoint-created.e1cd34ec8ae5a3eca599be7c894b0738e243317960138984b32d8a3fe20f4380.pa.png)

1. ਨੈਵੀਗੇਸ਼ਨ ਮੀਨੂ ਤੋਂ **Consume** ਚੁਣੋ।

1. ਆਪਣਾ **REST endpoint** ਅਤੇ **Primary key** ਕਾਪੀ ਕਰੋ।

    ![Copy api key and endpoint uri.](../../../../../../translated_images/copy-endpoint-key.f74d8aab513b5f540d2a219198fc5b7a3e64213497491bedb17f4bd039f16054.pa.png)

#### ਕਸਟਮ ਕਨੈਕਸ਼ਨ ਸ਼ਾਮਲ ਕਰੋ

1. [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) 'ਤੇ ਜਾਓ।

1. ਉਸ Azure AI Foundry ਪ੍ਰੋਜੈਕਟ ਵਿੱਚ ਜਾਓ ਜੋ ਤੁਸੀਂ ਬਣਾਇਆ ਹੈ।

1. ਪ੍ਰੋਜੈਕਟ ਵਿੱਚ, ਖੱਬੇ ਪਾਸੇ ਟੈਬ ਤੋਂ **Settings** ਚੁਣੋ।

1. **+ New connection** ਚੁਣੋ।

    ![Select new connection.](../../../../../../translated_images/select-new-connection.7ac97b4db6dc44c3d4f01a38b22fff11c3e88f75bcbf4d26999048a61a8729b2.pa.png)

1. ਨੈਵੀਗੇਸ਼ਨ ਮੀਨੂ ਤੋਂ **Custom keys** ਚੁਣੋ।

    ![Select custom keys.](../../../../../../translated_images/select-custom-keys.b2e452da9ea19401c4b7c63fe2ec95a3a38fd13ae3e9fca37d431f0b7780d4da.pa.png)

1. ਹੇਠ ਲਿਖੇ ਕੰਮ ਕਰੋ:

    - **+ Add key value pairs** ਚੁਣੋ।
    - key ਨਾਮ ਵਜੋਂ **endpoint** ਦਰਜ ਕਰੋ ਅਤੇ Azure ML Studio ਤੋਂ ਕਾਪੀ ਕੀਤਾ endpoint value ਖੇਤਰ ਵਿੱਚ ਪੇਸਟ ਕਰੋ।
    - ਫਿਰ ਇੱਕ ਵਾਰ ਫਿਰ **+ Add key value pairs** ਚੁਣੋ।
    - key ਨਾਮ ਵਜੋਂ **key** ਦਰਜ ਕਰੋ ਅਤੇ Azure ML Studio ਤੋਂ ਕਾਪੀ ਕੀਤਾ key value ਖੇਤਰ ਵਿੱਚ ਪੇਸਟ ਕਰੋ।
    - keys ਸ਼ਾਮਲ ਕਰਨ ਤੋਂ ਬਾਅਦ, key ਨੂੰ ਖੁਲਾਸਾ ਹੋਣ ਤੋਂ ਬਚਾਉਣ ਲਈ **is secret** ਚੁਣੋ।

    ![Add connection.](../../../../../../translated_images/add-connection.645b0c3ecf4a21f97a16ffafc9f25fedbb75a823cec5fc9dd778c3ab6130b4f0.pa.png)

1. **Add connection** ਚੁਣੋ।

#### Prompt flow ਬਣਾਓ

ਤੁਸੀਂ Azure AI Foundry ਵਿੱਚ ਇੱਕ ਕਸਟਮ ਕਨੈਕਸ਼ਨ ਸ਼ਾਮਲ ਕਰ ਦਿੱਤਾ ਹੈ। ਹੁਣ, ਹੇਠ ਲਿਖੇ ਕਦਮਾਂ ਨਾਲ ਇੱਕ Prompt flow ਬਣਾਓ। ਫਿਰ, ਇਸ Prompt flow ਨੂੰ ਕਸਟਮ ਕਨੈਕਸ਼ਨ ਨਾਲ ਜੋੜ ਕੇ ਫਾਈਨ-ਟਿਊਨ ਕੀਤੇ ਮਾਡਲ ਨੂੰ Prompt flow ਵਿੱਚ ਵਰਤੋਂ ਲਈ ਕਨੈਕਟ ਕਰੋਗੇ।

1. ਉਸ Azure AI Foundry ਪ੍ਰੋਜੈਕਟ ਵਿੱਚ ਜਾਓ ਜੋ ਤੁਸੀਂ ਬਣਾਇਆ ਹੈ।

1. ਖੱਬੇ ਪਾਸੇ ਟੈਬ ਤੋਂ **Prompt flow** ਚੁਣੋ।

1. ਨੈਵੀਗੇਸ਼ਨ ਮੀਨੂ ਤੋਂ **+ Create** ਚੁਣੋ।

    ![Select Promptflow.](../../../../../../translated_images/select-promptflow.4d42246677cc7ba65feb3e2be4479620a2b1e6637a66847dc1047ca89cd02780.pa.png)

1. ਨੈਵੀਗੇਸ਼ਨ ਮੀਨੂ ਤੋਂ **Chat flow** ਚੁਣੋ।

    ![Select chat flow.](../../../../../../translated_images/select-flow-type.e818b610f36e93c5c9741911d7b95232164f01486cbb39a29d748c322bd62038.pa.png)

1. ਵਰਤਣ ਲਈ **Folder name** ਦਰਜ ਕਰੋ।

    ![Select chat flow.](../../../../../../translated_images/enter-name.628d4a5d69122cfae9d66e9bccf0f2f38c595e90e456a3837c713aadeff6aa52.pa.png)

1. **Create** ਚੁਣੋ।

#### ਆਪਣੇ ਕਸਟਮ Phi-3 / Phi-3.5 ਮਾਡਲ ਨਾਲ ਗੱਲਬਾਤ ਲਈ Prompt flow ਸੈਟਅਪ ਕਰੋ

ਤੁਹਾਨੂੰ ਫਾਈਨ-ਟਿਊਨ ਕੀਤੇ Phi-3 / Phi-3.5 ਮਾਡਲ ਨੂੰ Prompt flow ਵਿੱਚ ਸ਼ਾਮਲ ਕਰਨਾ ਹੈ। ਮੌਜੂਦਾ ਦਿੱਤਾ ਗਿਆ Prompt flow ਇਸ ਮਕਸਦ ਲਈ ਬਣਾਇਆ ਨਹੀਂ ਗਿਆ। ਇਸ ਲਈ, ਤੁਹਾਨੂੰ Prompt flow ਨੂੰ ਮੁੜ ਡਿਜ਼ਾਈਨ ਕਰਨਾ ਪਵੇਗਾ ਤਾਂ ਜੋ ਕਸਟਮ ਮਾਡਲ ਨਾਲ ਇੰਟਿਗ੍ਰੇਸ਼ਨ ਹੋ ਸਕੇ।

1. Prompt flow ਵਿੱਚ, ਮੌਜੂਦਾ flow ਨੂੰ ਮੁੜ ਬਣਾਉਣ ਲਈ ਹੇਠ ਲਿਖੇ ਕੰਮ ਕਰੋ:

    - **Raw file mode** ਚੁਣੋ।
    - *flow.dag.yml* ਫਾਇਲ ਵਿੱਚ ਸਾਰੇ ਮੌਜੂਦਾ ਕੋਡ ਨੂੰ ਮਿਟਾ ਦਿਓ।
    - *flow.dag.yml* ਵਿੱਚ ਹੇਠ ਲਿਖਿਆ ਕੋਡ ਸ਼ਾਮਲ ਕਰੋ।

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

    - **Save** ਚੁਣੋ।

    ![Select raw file mode.](../../../../../../translated_images/select-raw-file-mode.e665df3117bf5411acf4d93bc8ecc405a984120c0ca7b944fe700601fdbac66f.pa.png)

1. *integrate_with_promptflow.py* ਵਿੱਚ ਹੇਠ ਲਿਖਿਆ ਕੋਡ ਸ਼ਾਮਲ ਕਰੋ ਤਾਂ ਜੋ Prompt flow ਵਿੱਚ ਕਸਟਮ Phi-3 / Phi-3.5 ਮਾਡਲ ਵਰਤਿਆ ਜਾ ਸਕੇ।

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

    ![Paste prompt flow code.](../../../../../../translated_images/paste-promptflow-code.8547c46c57a5354667f91578d7bca9cc2d0f5e1c4dadd59efa1ca18d6376e7a8.pa.png)

> [!NOTE]
> Azure AI Foundry ਵਿੱਚ Prompt flow ਵਰਤੋਂ ਬਾਰੇ ਵਧੇਰੇ ਜਾਣਕਾਰੀ ਲਈ, ਤੁਸੀਂ [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow) ਨੂੰ ਦੇਖ ਸਕਦੇ ਹੋ।

1. **Chat input**, **Chat output** ਚੁਣੋ ਤਾਂ ਜੋ ਮਾਡਲ ਨਾਲ ਗੱਲਬਾਤ ਯੋਗ ਹੋ ਜਾਵੇ।

    ![Select Input Output.](../../../../../../translated_images/select-input-output.4d094b2da9e817e0ef7b9fd5339d929b50364b430ecc476a39c885ae9e4dcb35.pa.png)

1. ਹੁਣ ਤੁਸੀਂ ਆਪਣੇ ਕਸਟਮ Phi-3 / Phi-3.5 ਮਾਡਲ ਨਾਲ ਗੱਲਬਾਤ ਕਰਨ ਲਈ ਤਿਆਰ ਹੋ। ਅਗਲੇ ਅਭਿਆਸ ਵਿੱਚ, ਤੁਸੀਂ ਸਿੱਖੋਗੇ ਕਿ Prompt flow ਕਿਵੇਂ ਸ਼ੁਰੂ ਕਰਨਾ ਹੈ ਅਤੇ ਇਸਨੂੰ ਆਪਣੇ ਫਾਈਨ-ਟਿਊਨ ਕੀਤੇ ਮਾਡਲ ਨਾਲ ਗੱਲਬਾਤ ਲਈ ਕਿਵੇਂ ਵਰਤਣਾ ਹੈ।

> [!NOTE]
>
> ਮੁੜ ਬਣਾਇਆ ਗਿਆ flow ਹੇਠਾਂ ਦਿੱਤੀ ਤਸਵੀਰ ਵਰਗਾ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ:
>
> ![Flow example](../../../../../../translated_images/graph-example.55ee258e205e3b686250c5fc480ffe8956eb9f4887f7b11e94a6720e0d032733.pa.png)
>

#### Prompt flow ਸ਼ੁਰੂ ਕਰੋ

1. Prompt flow ਸ਼ੁਰੂ ਕਰਨ ਲਈ **Start compute sessions** ਚੁਣੋ।

    ![Start compute session.](../../../../../../translated_images/start-compute-session.e7eb268344e2040fdee7b46a175d2fbd19477e0ab122ef563113828d03b03946.pa.png)

1. ਪੈਰਾਮੀਟਰ ਨਵੀਨਤਮ ਕਰਨ ਲਈ **Validate and parse input** ਚੁਣੋ।

    ![Validate input.](../../../../../../translated_images/validate-input.dffb16c78fc266e52d55582791d67a54d631c166a61d7ca57a258e00c2e14150.pa.png)

1. ਆਪਣੇ ਬਣਾਏ ਕਸਟਮ ਕਨੈਕਸ਼ਨ ਦੀ **connection** ਦੀ **Value** ਚੁਣੋ। ਉਦਾਹਰਨ ਵਜੋਂ, *connection*।

    ![Connection.](../../../../../../translated_images/select-connection.5c7a570da52e12219d21fef02800b152d124722619f56064b172a84721603b52.pa.png)

#### ਆਪਣੇ ਕਸਟਮ Phi-3 / Phi-3.5 ਮਾਡਲ ਨਾਲ ਗੱਲਬਾਤ ਕਰੋ

1. **Chat** ਚੁਣੋ।

    ![Select chat.](../../../../../../translated_images/select-chat.c255a13f678aa46d9601c54a81aa2e0d58c9e01a8c6ec7d86598438d8e19214d.pa.png)

1. ਨਤੀਜਿਆਂ ਦਾ ਉਦਾਹਰਨ: ਹੁਣ ਤੁਸੀਂ ਆਪਣੇ ਕਸਟਮ Phi-3 / Phi-3.5 ਮਾਡਲ ਨਾਲ ਗੱਲਬਾਤ ਕਰ ਸਕਦੇ ਹੋ। ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ ਕਿ ਤੁਸੀਂ ਫਾਈਨ-ਟਿਊਨਿੰਗ ਲਈ ਵਰਤੇ ਡਾਟਾ ਦੇ ਆਧਾਰ 'ਤੇ ਸਵਾਲ ਪੁੱਛੋ।

    ![Chat with prompt flow.](../../../../../../translated_images/chat-with-promptflow.6da5e838c71f428b6d8aea9a0c655568354ae82babcdc87cd0f0d4edeee9d930.pa.png)

### Phi-3 / Phi-3.5 ਮਾਡਲ ਦਾ ਮੁਲਾਂਕਣ ਕਰਨ ਲਈ Azure OpenAI ਡਿਪਲੋਇ ਕਰੋ

Phi-3 / Phi-3.5 ਮਾਡਲ ਦਾ Azure AI Foundry ਵਿੱਚ ਮੁਲਾਂਕਣ ਕਰਨ ਲਈ, ਤੁਹਾਨੂੰ ਇੱਕ Azure OpenAI ਮਾਡਲ ਡਿਪਲੋਇ ਕਰਨਾ ਪਵੇਗਾ। ਇਹ ਮਾਡਲ Phi-3 / Phi-3.5 ਮਾਡਲ ਦੀ ਕਾਰਗੁਜ਼ਾਰੀ ਦਾ ਮੁਲਾਂਕਣ ਕਰਨ ਲਈ ਵਰਤਿਆ ਜਾਵੇਗਾ।

#### Azure OpenAI ਡਿਪਲੋਇ ਕਰੋ

1. [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) ਵਿੱਚ ਸਾਈਨ ਇਨ ਕਰੋ।

1. ਉਸ Azure AI Foundry ਪ੍ਰੋਜੈਕਟ ਵਿੱਚ ਜਾਓ ਜੋ ਤੁਸੀਂ ਬਣਾਇਆ ਹੈ।

    ![Select Project.](../../../../../../translated_images/select-project-created.84d119464c1bb0a8f5f9ab58012fa88304b0e3b0d6ddda444617424b2bb0d22e.pa.png)

1. ਪ੍ਰੋਜੈਕਟ ਵਿੱਚ, ਖੱਬੇ ਪਾਸੇ ਟੈਬ ਤੋਂ **Deployments** ਚੁਣੋ।

1. ਨੈਵੀਗੇਸ਼ਨ ਮੀਨੂ ਤੋਂ **+ Deploy model** ਚੁਣੋ।

1. **Deploy base model** ਚੁਣੋ।

    ![Select Deployments.](../../../../../../translated_images/deploy-openai-model.91e6d9f9934e0e0c63116bd81a7628ea5ab37617f3e3b23a998a37c7f5aaba8b.pa.png)

1. ਜਿਸ Azure OpenAI ਮਾਡਲ ਨੂੰ ਤੁਸੀਂ ਵਰਤਣਾ ਚਾਹੁੰਦੇ ਹੋ, ਉਹ ਚੁਣੋ। ਉਦਾਹਰਨ ਵਜੋਂ, **gpt-4o**।

    ![Select Azure OpenAI model you'd like to use.](../../../../../../translated_images/select-openai-model.c0f0e8d4afe80525745b4e67b52ae0d23550da9130bc8d1aea8160be0e261399.pa.png)

1. **Confirm** ਚੁਣੋ।

### Azure AI Foundry ਦੇ Prompt flow ਮੁਲਾਂਕਣ ਨਾਲ ਫਾਈਨ-ਟਿਊਨ ਕੀਤੇ Phi-3 / Phi-3.5 ਮਾਡਲ ਦਾ ਮੁਲਾਂਕਣ ਕਰੋ

### ਨਵਾਂ ਮੁਲਾਂਕਣ ਸ਼ੁਰੂ ਕਰੋ

1. [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) 'ਤੇ ਜਾਓ।

1. ਉਸ Azure AI Foundry ਪ੍ਰੋਜੈਕਟ ਵਿੱਚ ਜਾਓ ਜੋ ਤੁਸੀਂ ਬਣਾਇਆ ਹੈ।

    ![Select Project.](../../../../../../translated_images/select-project-created.84d119464c1bb0a8f5f9ab58012fa88304b0e3b0d6ddda444617424b2bb0d22e.pa.png)

1. ਪ੍ਰੋਜੈਕਟ ਵਿੱਚ, ਖੱਬੇ ਪਾਸੇ ਟੈਬ ਤੋਂ **Evaluation** ਚੁਣੋ।

1. ਨੈਵੀਗੇਸ਼ਨ ਮੀਨੂ ਤੋਂ **+ New evaluation** ਚੁਣੋ।
![Select evaluation.](../../../../../../translated_images/select-evaluation.00ce489c57544e735170ae63682b293c3f5e362ded9d62b602ff0cf8e957287c.pa.png)

1. **Prompt flow** ਮੁਲਾਂਕਣ ਚੁਣੋ।

    ![Select Prompt flow evaluation.](../../../../../../translated_images/promptflow-evaluation.350729f9e70f59110aa0b425adcdf00b2d5382066144ac1cdf265fa1884808b2.pa.png)

1. ਹੇਠਾਂ ਦਿੱਤੇ ਕੰਮ ਕਰੋ:

    - ਮੁਲਾਂਕਣ ਦਾ ਨਾਮ ਦਿਓ। ਇਹ ਇਕ ਵਿਲੱਖਣ ਮੁੱਲ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ।
    - ਟਾਸਕ ਕਿਸਮ ਵਜੋਂ **Question and answer without context** ਚੁਣੋ। ਕਿਉਂਕਿ ਇਸ ਟਿਊਟੋਰਿਯਲ ਵਿੱਚ ਵਰਤੇ ਗਏ **UlTRACHAT_200k** ਡੇਟਾਸੈੱਟ ਵਿੱਚ ਸੰਦਰਭ ਨਹੀਂ ਹੁੰਦਾ।
    - ਉਹ prompt flow ਚੁਣੋ ਜਿਸਦੀ ਤੁਸੀਂ ਮੁਲਾਂਕਣ ਕਰਨਾ ਚਾਹੁੰਦੇ ਹੋ।

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting1.772ca4e86a27e9c37d627e36c84c07b363a5d5229724f15596599d6b0f1d4ca1.pa.png)

1. **Next** ਚੁਣੋ।

1. ਹੇਠਾਂ ਦਿੱਤੇ ਕੰਮ ਕਰੋ:

    - ਡੇਟਾਸੈੱਟ ਅਪਲੋਡ ਕਰਨ ਲਈ **Add your dataset** ਚੁਣੋ। ਉਦਾਹਰਨ ਵਜੋਂ, ਤੁਸੀਂ ਟੈਸਟ ਡੇਟਾਸੈੱਟ ਫਾਈਲ ਜਿਵੇਂ *test_data.json1* ਅਪਲੋਡ ਕਰ ਸਕਦੇ ਹੋ, ਜੋ ਕਿ **ULTRACHAT_200k** ਡੇਟਾਸੈੱਟ ਡਾਊਨਲੋਡ ਕਰਦੇ ਸਮੇਂ ਸ਼ਾਮਲ ਹੁੰਦੀ ਹੈ।
    - ਆਪਣੇ ਡੇਟਾਸੈੱਟ ਨਾਲ ਮਿਲਦਾ ਜੁਲਦਾ **Dataset column** ਚੁਣੋ। ਉਦਾਹਰਨ ਵਜੋਂ, ਜੇ ਤੁਸੀਂ **ULTRACHAT_200k** ਡੇਟਾਸੈੱਟ ਵਰਤ ਰਹੇ ਹੋ, ਤਾਂ **${data.prompt}** ਕਾਲਮ ਚੁਣੋ।

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting2.074e573f2ab245d37b12a9057b8fef349a552962f1ec3b23fd09734d4d653752.pa.png)

1. **Next** ਚੁਣੋ।

1. ਪ੍ਰਦਰਸ਼ਨ ਅਤੇ ਗੁਣਵੱਤਾ ਮੈਟਰਿਕਸ ਸੈੱਟ ਕਰਨ ਲਈ ਹੇਠਾਂ ਦਿੱਤੇ ਕੰਮ ਕਰੋ:

    - ਉਹ ਪ੍ਰਦਰਸ਼ਨ ਅਤੇ ਗੁਣਵੱਤਾ ਮੈਟਰਿਕਸ ਚੁਣੋ ਜੋ ਤੁਸੀਂ ਵਰਤਣਾ ਚਾਹੁੰਦੇ ਹੋ।
    - ਮੁਲਾਂਕਣ ਲਈ ਬਣਾਇਆ ਗਿਆ Azure OpenAI ਮਾਡਲ ਚੁਣੋ। ਉਦਾਹਰਨ ਵਜੋਂ, **gpt-4o** ਚੁਣੋ।

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting3-1.7e26ae563c1312db5d1d21f8f44652243627f487df036ba27fe58d181102300d.pa.png)

1. ਖਤਰਾ ਅਤੇ ਸੁਰੱਖਿਆ ਮੈਟਰਿਕਸ ਸੈੱਟ ਕਰਨ ਲਈ ਹੇਠਾਂ ਦਿੱਤੇ ਕੰਮ ਕਰੋ:

    - ਉਹ ਖਤਰਾ ਅਤੇ ਸੁਰੱਖਿਆ ਮੈਟਰਿਕਸ ਚੁਣੋ ਜੋ ਤੁਸੀਂ ਵਰਤਣਾ ਚਾਹੁੰਦੇ ਹੋ।
    - ਖ਼ਰਾਬੀ ਦਰ ਗਿਣਤੀ ਲਈ ਥ੍ਰੇਸ਼ਹੋਲਡ ਚੁਣੋ। ਉਦਾਹਰਨ ਵਜੋਂ, **Medium** ਚੁਣੋ।
    - **question** ਲਈ, **Data source** ਨੂੰ **{$data.prompt}** ਤੇ ਸੈੱਟ ਕਰੋ।
    - **answer** ਲਈ, **Data source** ਨੂੰ **{$run.outputs.answer}** ਤੇ ਸੈੱਟ ਕਰੋ।
    - **ground_truth** ਲਈ, **Data source** ਨੂੰ **{$data.message}** ਤੇ ਸੈੱਟ ਕਰੋ।

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting3-2.185148a456f1edb7d0db874f765dc6bc34fec7e1b00833be81b0428af6d18233.pa.png)

1. **Next** ਚੁਣੋ।

1. ਮੁਲਾਂਕਣ ਸ਼ੁਰੂ ਕਰਨ ਲਈ **Submit** ਚੁਣੋ।

1. ਮੁਲਾਂਕਣ ਪੂਰਾ ਹੋਣ ਵਿੱਚ ਕੁਝ ਸਮਾਂ ਲੱਗੇਗਾ। ਤੁਸੀਂ ਪ੍ਰਗਤੀ ਨੂੰ **Evaluation** ਟੈਬ ਵਿੱਚ ਦੇਖ ਸਕਦੇ ਹੋ।

### ਮੁਲਾਂਕਣ ਨਤੀਜੇ ਸਮੀਖਿਆ ਕਰੋ

> [!NOTE]
> ਹੇਠਾਂ ਦਿੱਤੇ ਨਤੀਜੇ ਸਿਰਫ਼ ਮੁਲਾਂਕਣ ਪ੍ਰਕਿਰਿਆ ਨੂੰ ਦਰਸਾਉਣ ਲਈ ਹਨ। ਇਸ ਟਿਊਟੋਰਿਯਲ ਵਿੱਚ, ਅਸੀਂ ਇੱਕ ਛੋਟੇ ਡੇਟਾਸੈੱਟ ‘ਤੇ ਫਾਈਨ-ਟਿਊਨ ਕੀਤਾ ਮਾਡਲ ਵਰਤਿਆ ਹੈ, ਜਿਸ ਕਰਕੇ ਨਤੀਜੇ ਕਦੇ ਕਦੇ ਵਧੀਆ ਨਹੀਂ ਹੁੰਦੇ। ਅਸਲ ਨਤੀਜੇ ਡੇਟਾਸੈੱਟ ਦੇ ਆਕਾਰ, ਗੁਣਵੱਤਾ, ਵਿਭਿੰਨਤਾ ਅਤੇ ਮਾਡਲ ਦੀ ਵਿਸ਼ੇਸ਼ ਸੈਟਿੰਗ ਉੱਤੇ ਬਹੁਤ ਅਸਰ ਕਰਦੇ ਹਨ।

ਮੁਲਾਂਕਣ ਪੂਰਾ ਹੋਣ ‘ਤੇ, ਤੁਸੀਂ ਪ੍ਰਦਰਸ਼ਨ ਅਤੇ ਸੁਰੱਖਿਆ ਮੈਟਰਿਕਸ ਦੋਹਾਂ ਦੇ ਨਤੀਜੇ ਵੇਖ ਸਕਦੇ ਹੋ।

1. ਪ੍ਰਦਰਸ਼ਨ ਅਤੇ ਗੁਣਵੱਤਾ ਮੈਟਰਿਕਸ:

    - ਮਾਡਲ ਦੀ ਸਮਝਦਾਰੀ, ਸੁਚੱਜੇ ਅਤੇ ਸਬੰਧਿਤ ਜਵਾਬ ਬਣਾਉਣ ਦੀ ਸਮਰੱਥਾ ਦਾ ਮੁਲਾਂਕਣ ਕਰੋ।

    ![Evaluation result.](../../../../../../translated_images/evaluation-result-gpu.8e9decea0f5dd1250948982514bcde94bb2debba2b686be5e633f1aad093921f.pa.png)

1. ਖਤਰਾ ਅਤੇ ਸੁਰੱਖਿਆ ਮੈਟਰਿਕਸ:

    - ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਮਾਡਲ ਦੇ ਨਤੀਜੇ ਸੁਰੱਖਿਅਤ ਹਨ ਅਤੇ Responsible AI Principles ਨਾਲ ਮੇਲ ਖਾਂਦੇ ਹਨ, ਜਿਹੜੇ ਕਿਸੇ ਵੀ ਨੁਕਸਾਨਦਾਇਕ ਜਾਂ ਅਪਮਾਨਜਨਕ ਸਮੱਗਰੀ ਤੋਂ ਬਚਾਉਂਦੇ ਹਨ।

    ![Evaluation result.](../../../../../../translated_images/evaluation-result-gpu-2.180e37b9669f3d31aade247bd38b87b15a2ef93b69a1633c4e4072946aadaa26.pa.png)

1. ਤੁਸੀਂ ਹੇਠਾਂ ਸਕ੍ਰੋਲ ਕਰਕੇ **Detailed metrics result** ਵੀ ਵੇਖ ਸਕਦੇ ਹੋ।

    ![Evaluation result.](../../../../../../translated_images/detailed-metrics-result.a0abde70a729afee17e34df7c11ea2f6f0ea1aefbe8a26a35502f304de57a647.pa.png)

1. ਆਪਣੇ ਕਸਟਮ Phi-3 / Phi-3.5 ਮਾਡਲ ਦਾ ਪ੍ਰਦਰਸ਼ਨ ਅਤੇ ਸੁਰੱਖਿਆ ਮੈਟਰਿਕਸ ਨਾਲ ਮੁਲਾਂਕਣ ਕਰਕੇ, ਤੁਸੀਂ ਪੱਕਾ ਕਰ ਸਕਦੇ ਹੋ ਕਿ ਮਾਡਲ ਨਾ ਸਿਰਫ਼ ਪ੍ਰਭਾਵਸ਼ਾਲੀ ਹੈ, ਬਲਕਿ Responsible AI ਅਮਲਾਂ ਦਾ ਪਾਲਣ ਵੀ ਕਰਦਾ ਹੈ, ਜਿਸ ਨਾਲ ਇਹ ਅਸਲੀ ਦੁਨੀਆ ਵਿੱਚ ਵਰਤੋਂ ਲਈ ਤਿਆਰ ਹੁੰਦਾ ਹੈ।

## ਵਧਾਈਆਂ!

### ਤੁਸੀਂ ਇਹ ਟਿਊਟੋਰਿਯਲ ਪੂਰਾ ਕਰ ਲਿਆ ਹੈ

ਤੁਸੀਂ Azure AI Foundry ਵਿੱਚ Prompt flow ਨਾਲ ਇੰਟਿਗ੍ਰੇਟ ਕੀਤਾ ਫਾਈਨ-ਟਿਊਨ ਕੀਤਾ Phi-3 ਮਾਡਲ ਸਫਲਤਾਪੂਰਵਕ ਮੁਲਾਂਕਣ ਕੀਤਾ ਹੈ। ਇਹ ਤੁਹਾਡੇ AI ਮਾਡਲਾਂ ਨੂੰ ਨਾ ਸਿਰਫ਼ ਚੰਗਾ ਪ੍ਰਦਰਸ਼ਨ ਕਰਨ ਲਈ, ਸਗੋਂ Microsoft ਦੇ Responsible AI ਨੀਤੀਆਂ ਦਾ ਪਾਲਣ ਕਰਨ ਲਈ ਇੱਕ ਮਹੱਤਵਪੂਰਨ ਕਦਮ ਹੈ, ਜੋ ਤੁਹਾਨੂੰ ਭਰੋਸੇਮੰਦ ਅਤੇ ਵਿਸ਼ਵਾਸਯੋਗ AI ਐਪਲੀਕੇਸ਼ਨ ਬਣਾਉਣ ਵਿੱਚ ਮਦਦ ਕਰਦਾ ਹੈ।

![Architecture.](../../../../../../translated_images/architecture.99df2035c1c1a82e7f7d3aa3368e5940e46d27d35abd498166e55094298fce81.pa.png)

## Azure ਸਰੋਤ ਸਾਫ਼ ਕਰੋ

ਆਪਣੇ ਖਾਤੇ 'ਤੇ ਵਾਧੂ ਖਰਚਿਆਂ ਤੋਂ ਬਚਣ ਲਈ Azure ਸਰੋਤ ਸਾਫ਼ ਕਰੋ। Azure ਪੋਰਟਲ 'ਤੇ ਜਾ ਕੇ ਹੇਠਾਂ ਦਿੱਤੇ ਸਰੋਤ ਹਟਾਓ:

- Azure Machine learning ਸਰੋਤ।
- Azure Machine learning ਮਾਡਲ ਐਂਡਪਾਇੰਟ।
- Azure AI Foundry ਪ੍ਰੋਜੈਕਟ ਸਰੋਤ।
- Azure AI Foundry Prompt flow ਸਰੋਤ।

### ਅਗਲੇ ਕਦਮ

#### ਦਸਤਾਵੇਜ਼ੀਕਰਨ

- [Assess AI systems by using the Responsible AI dashboard](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [Evaluation and monitoring metrics for generative AI](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Azure AI Foundry documentation](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Prompt flow documentation](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### ਟ੍ਰੇਨਿੰਗ ਸਮੱਗਰੀ

- [Introduction to Microsoft's Responsible AI Approach](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Introduction to Azure AI Foundry](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### ਸੰਦਰਭ

- [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [Announcing new tools in Azure AI to help you build more secure and trustworthy generative AI applications](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

**ਅਸਵੀਕਾਰੋक्ति**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਅਤ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਥਿਰਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਇਸਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜ਼ਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੇ ਇਸਤੇਮਾਲ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।