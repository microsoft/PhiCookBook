# ਮਾਇਕਰੋਸੌਫਟ ਦੇ ਜ਼ਿੰਮੇਵਾਰ ਏਆਈ ਮੁੱਲਾਂਕਣ 'ਤੇ ਧਿਆਨ ਕੇਂਦਰਿਤ Microsoft Foundry ਵਿੱਚ ਫਾਈਨ-ਟੀਊਨ ਕੀਤੇ Phi-3 / Phi-3.5 ਮਾਡਲ ਦਾ ਮੁਲਾਂਕਣ ਕਰੋ

ਇਹ ਐਂਡ-ਟੂ-ਐਂਡ (E2E) ਨਮੂਨਾ Microsoft ਟੈਕ ਕਮਿਊਨਿਟੀ ਤੋਂ "[Evaluate Fine-tuned Phi-3 / 3.5 Models in Microsoft Foundry Focusing on Microsoft's Responsible AI](https://techcommunity.microsoft.com/blog/educatordeveloperblog/evaluate-fine-tuned-phi-3--3-5-models-in-azure-ai-studio-focusing-on-microsofts-/4227850?WT.mc_id=aiml-137032-kinfeylo)" ਮਾਰਗਦਰਸ਼ਕ 'ਤੇ ਆਧਾਰਿਤ ਹੈ।

## ਜਾਇਜ਼ਾ

### ਤੁਸੀਂ Microsoft Foundry ਵਿੱਚ ਫਾਈਨ-ਟੀਊਨ ਕੀਤੇ Phi-3 / Phi-3.5 ਮਾਡਲ ਦੀ ਸੁਰੱਖਿਆ ਅਤੇ ਪ੍ਰਦਰਸ਼ਨ ਨੂੰ ਕਿਵੇਂ ਮੁਲਾਂਕਣ ਕਰ ਸਕਦੇ ਹੋ?

ਮਾਡਲ ਨੂੰ ਫਾਈਨ-ਟੀਊਨ ਕਰਨ ਨਾਲ ਕਈ ਵਾਰ ਅਣਚਾਹੇ ਜਾਂ ਗ਼ਲਤ ਪ੍ਰਤੀਕਿਰਿਆਵਾਂ ਉਤਪੰਨ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਇਹ ਯਕੀਨੀ ਬਣਾਉਣ ਲਈ ਕਿ ਮਾਡਲ ਸੁਰੱਖਿਅਤ ਅਤੇ ਪ੍ਰਭਾਵਸ਼ਾਲੀ ਰਹੇ, ਇਹ ਜਰੂਰੀ ਹੈ ਕਿ ਮਾਡਲ ਦੀ ਸੰਭਾਵਨਾ ਨੂੰ ਨੁਕਸਾਨਦੇਹ ਸਮੱਗਰੀ ਬਣਾਉਣ ਅਤੇ ਸਹੀ, ਸਮੰਬੰਧਤ ਅਤੇ ਸੁਚੱਜੇ ਜਵਾਬ ਉਤਪੰਨ ਕਰਨ ਦੀ ਸਮਰੱਥਾ ਨੂੰ ਮੁਲਾਂਕਣ ਕੀਤਾ ਜਾਵੇ। ਇਸ ਟਿਊਟੋਰਿਯਲ ਵਿੱਚ, ਤੁਸੀਂ ਸ਼ીખੋਗੇ ਕਿ ਕਿਵੇਂ Microsoft Foundry ਵਿੱਚ Prompt flow ਨਾਲ ਇੰਟਿਗ੍ਰੇਟ ਕੀਤੇ ਫਾਈਨ-ਟੀਊਨ ਕੀਤੇ Phi-3 / Phi-3.5 ਮਾਡਲ ਦੀ ਸੁਰੱਖਿਆ ਅਤੇ ਪ੍ਰਦਰਸ਼ਨ ਨੂੰ ਮੁਲਾਂਕਣ ਕਰਨਾ ਹੈ।

ਇੱਥੇ Microsoft Foundry ਦਾ ਮੁਲਾਂਕਣ ਪ੍ਰਕਿਰਿਆ ਦਿੱਤੀ ਗਈ ਹੈ।

![Architecture of tutorial.](../../../../../../translated_images/pa/architecture.10bec55250f5d6a4.webp)

*ਚਿੱਤਰ ਸਰੋਤ: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> Phi-3 / Phi-3.5 ਬਾਰੇ ਹੋਰ ਵਿਸਥਾਰਿਤ ਜਾਣਕਾਰੀ ਅਤੇ ਵਾਧੂ ਸਰੋਤਾਂ ਨੂੰ ਵੇਖਣ ਲਈ, ਕ੍ਰਿਪਾ ਕਰਕੇ [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723) 'ਤੇ ਜਾਓ।

### ਲੋੜੀਂਦੇ ਸਾਧਨ

- [Python](https://www.python.org/downloads)
- [Azure subscription](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- ਫਾਈਨ-ਟੀਊਨ ਕੀਤੇ Phi-3 / Phi-3.5 ਮਾਡਲ

### ਸਮੱਗਰੀ ਦੀ ਸੂਚੀ

1. [**ਸਥਿਤੀ 1: Microsoft Foundry ਦੇ Prompt flow ਮੁਲਾਂਕਣ ਦਾ ਪਰਿਚਯ**](#scenario-1-introduction-to-azure-ai-studios-prompt-flow-evaluation)

    - [ਸੁਰੱਖਿਆ ਮੁਲਾਂਕਣ ਦਾ ਪਰਿਚਯ](#ਸੁਰੱਖਿਆ-ਮੁਲਾਂਕਣ-ਦਾ-ਪਰਿਚਯ)
    - [ਪ੍ਰਦਰਸ਼ਨ ਮੁਲਾਂਕਣ ਦਾ ਪਰਿਚਯ](#ਪ੍ਰਦਰਸ਼ਨ-ਮੁਲਾਂਕਣ-ਦਾ-ਪਰਿਚਯ)

1. [**ਸਥਿਤੀ 2: Microsoft Foundry ਵਿੱਚ Phi-3 / Phi-3.5 ਮਾਡਲ ਦੀ ਮੁਲਾਂਕਣ**](#scenario-2-evaluating-the-phi-3--phi-35-model-in-azure-ai-studio)

    - [ਸ਼ੁਰੂ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ](#ਸ਼ੁਰੂ-ਕਰਨ-ਤੋਂ-ਪਹਿਲਾਂ)
    - [Phi-3 / Phi-3.5 ਮਾਡਲ ਦਾ ਮੁਲਾਂਕਣ ਕਰਨ ਲਈ Azure OpenAI ਤਾਇਨਾਤ ਕਰੋ](#deploy-azure-openai-to-evaluate-the-phi-3--phi-35-model)
    - [Microsoft Foundry ਦੇ Prompt flow ਮੁਲਾਂਕਣ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਫਾਈਨ-ਟੀਊਨ ਕੀਤੇ Phi-3 / Phi-3.5 ਮਾਡਲ ਨੂੰ ਮੁਲਾਂਕਣ ਕਰੋ](#evaluate-the-fine-tuned-phi-3--phi-35-model-using-azure-ai-studios-prompt-flow-evaluation)

1. [ਅਭਿਨੰਦਨ!](#ਵਧਾਈਆਂ)

## **ਸਥਿਤੀ 1: Microsoft Foundry ਦੇ Prompt flow ਮੁਲਾਂਕਣ ਦਾ ਪਰਿਚਯ**

### ਸੁਰੱਖਿਆ ਮੁਲਾਂਕਣ ਦਾ ਪਰਿਚਯ

ਤੁਹਾਡੇ ਏਆਈ ਮਾਡਲ ਨੂੰ ਨੈਤਿਕ ਅਤੇ ਸੁਰੱਖਿਅਤ ਬਣਾਏ ਰੱਖਣ ਲਈ ਇਸਨੂੰ Microsoft ਦੇ ਜ਼ਿੰਮੇਵਾਰ ਏਆਈ ਸਿਧਾਂਤਾਂ ਦੇ ਖਿਲਾਫ ਮੁਲਾਂਕਣ ਕਰਨਾ ਬਹੁਤ ਜਰੂਰੀ ਹੈ। Microsoft Foundry ਵਿੱਚ, ਸੁਰੱਖਿਆ ਮੁਲਾਂਕਣ ਤੁਹਾਨੂੰ ਤੁਹਾਡੇ ਮਾਡਲ ਦੀ jailbreak ਹਮਲਿਆਂ ਵੱਲ ਸੰਵੇਦਨਸ਼ੀਲਤਾ ਅਤੇ ਨੁਕਸਾਨਦੇਹ ਸਮੱਗਰੀ ਬਣਾਉਣ ਦੀ ਸੰਭਾਵਨਾ ਨੂੰ ਮੁਲਾਂਕਣ ਕਰਨ ਦੀ ਆਗਿਆ ਦਿੰਦੇ ਹਨ, ਜੋ ਕਿ ਇਹਨਾਂ ਸਿਧਾਂਤਾਂ ਨਾਲ ਸਿੱਧਾ ਸੰਬੰਧਿਤ ਹੈ।

![Safaty evaluation.](../../../../../../translated_images/pa/safety-evaluation.083586ec88dfa950.webp)

*ਚਿੱਤਰ ਸਰੋਤ: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Microsoft ਦੇ ਜ਼ਿੰਮੇਵਾਰ AI ਸਿਧਾਂਤ

ਟੈਕਨੀਕੀ ਕਦਮ ਸ਼ੁਰੂ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ, Microsoft ਦੇ ਜ਼ਿੰਮੇਵਾਰ AI ਸਿਧਾਂਤਾਂ ਨੂੰ ਸਮਝਣਾ ਜਰੂਰੀ ਹੈ, ਜੋ ਕਿ ਇੱਕ ਐਥਿਕ ਫਰੇਮਵਰਕ ਹੈ ਜੋ AI ਪ੍ਰਣਾਲੀਆਂ ਦੇ ਜ਼ਿੰਮੇਵਾਰ ਵਿਕਾਸ, ਤਾਇਨਾਤ ਅਤੇ ਚਾਲੂ ਕਰਨ ਵਿਚ ਮਾਰਗਦਰਸ਼ਨ ਦਾ ਕੰਮ ਕਰਦਾ ਹੈ। ਇਹ ਸਿਧਾਂਤ AI ਪ੍ਰਣਾਲੀਆਂ ਦੇ ਜ਼ਿੰਮੇਵਾਰ ਡਿਜ਼ਾਈਨ, ਵਿਕਾਸ ਅਤੇ ਤਾਇਨਾਤ ਨੂੰ ਮਦਦ ਕਰਦੇ ਹਨ, ਇਹ ਸੁਰੱਖਿਅਤ ਕਰਦੇ ਹੋਏ ਕਿ AI ਤਕਨੀਕਾਂ ਨੂੰ ਇਨਸਾਫ਼, ਪਾਰਦਰਸ਼ੀ, ਅਤੇ ਸ਼ਾਮਿਲ ਕਰਨ ਵਾਲੇ ਢੰਗ ਨਾਲ ਬਣਾਇਆ ਜਾਵੇ। ਇਹ ਸਿਧਾਂਤ AI ਮਾਡਲਾਂ ਦੀ ਸੁਰੱਖਿਆ ਦੀ ਮੁਲਾਂਕਣ ਲਈ ਆਧਾਰ ਹਨ।

Microsoft ਦੇ ਜ਼ਿੰਮੇਵਾਰ AI ਸਿਧਾਂਤ ਸ਼ਾਮਿਲ ਹਨ:

- **ਇਨਸਾਫ਼ ਅਤੇ ਸ਼ਾਮিলਗੀਰੀ**: AI ਪ੍ਰਣਾਲੀਆਂ ਨੂੰ ਹਰ ਕਿਸੇ ਨਾਲ ਇਨਸਾਫ਼ ਨਾਲ ਪੇਸ਼ ਆਉਣਾ ਚਾਹੀਦਾ ਹੈ ਅਤੇ ਸਮਾਨ ਹਾਲਤਾਂ ਵਾਲੇ ਲੋਕਾਂ ਦੇ ਗਰੂਪਾਂ ਨੂੰ ਵੱਖ-ਵੱਖ ਢੰਗ ਨਾਲ ਪ੍ਰਭਾਵਿਤ ਕਰਨ ਤੋਂ ਬਚਣਾ ਚਾਹੀਦਾ ਹੈ। ਉਦਾਹਰਨ ਵਜੋਂ, ਜਦੋਂ AI ਪ੍ਰਣਾਲੀਆਂ ਚਿਕਿਤਸਾ ਇਲਾਜ, ਰਣਮੁਹੱਈ ਲਾਗੂ ਕਰਨਾ ਜਾਂ ਰੋਜ਼ਗਾਰ ਬਾਰੇ ਸਲਾਹ ਦਿੰਦੇ ਹਨ, ਉਹਨਾਂ ਨੂੰ ਉਹੀ Sujhaavan ਦੇਣੇ ਚਾਹੀਦੇ ਹਨ ਜਿਨ੍ਹਾਂ ਕੋਲ ਸਮਾਨ ਲੱਛਣ, ਵਿੱਤੀ ਹਾਲਾਤ, ਜਾਂ ਪੇਸ਼ਾਵਰ ਯੋਗਤਾਵਾਂ ਹਨ।

- **ਨਿਰਭਰਤਾ ਅਤੇ ਸੁਰੱਖਿਆ**: ਭਰੋਸਾ ਬਣਾਉਣ ਲਈ, ਇਹ ਜ਼ਰੂਰੀ ਹੈ ਕਿ AI ਪ੍ਰਣਾਲੀਆਂ ਵਿਸ਼ਵਾਸ ਯੋਗ, ਸੁਰੱਖਿਅਤ ਅਤੇ ਲਗਾਤਾਰ ਚੱਲਣ। ਇਹ ਪ੍ਰਣਾਲੀਆਂ ਉਹੀ ਢੰਗ ਨਾਲ ਕੰਮ ਕਰ ਸਕਣ ਜਿਵੇਂ ਉਹ ਮੂਲ ਤੌਰ 'ਤੇ ਡਿਜ਼ਾਈਨ ਕੀਤੀਆਂ ਗਈਆਂ ਸਨ, ਬਿਨਾਂ ਕਿਸੇ ਅਣਮੋਹਰੇ ਹਾਲਾਤਾਂ ਚ ਸੁਰੱਖਿਅਤ ਜਵਾਬ ਦੇਣ ਅਤੇ ਨੁਕਸਾਨਦੇਹ ਹੇਠਾਂ ਸਮਰੱਥ ਰਿਹਾਇਸ਼ ਕਰ ਸਕਣ। ਉਹਨਾਂ ਦੀ ਵ੍ਯਵਹਾਰ ਅਤੇ ਉਹ ਹਲਾਤਾਂ ਜਿਹੜੀਆਂ ਉਹ ਸੰਭਾਲ ਸਕਦੇ ਹਨ, ਉਹਨਾਂ ਸਥਿਤੀਆਂ ਅਤੇ ਹਾਲਾਤਾਂ ਦੀਆਂ ਲੜੀਆਂ ਜਿਨ੍ਹਾਂ ਦੀ ਡਿਜ਼ਾਈਨ ਅਤੇ ਟੈਸਟਿੰਗ ਦੌਰਾਨ ਡਿਵੈਲਪਰਾਂ ਨੇ ਉਮੀਦ ਕੀਤੀ ਸੀ।

- **ਪਾਰਦਰਸ਼ਤਾ**: ਜਦੋਂ AI ਪ੍ਰਣਾਲੀਆਂ ਉਹ ਫੈਸਲੇ ਕਰਨ ਵਿੱਚ ਸਹਾਇਤਾ ਕਰਦੀਆਂ ਹਨ ਜਿਹੜੇ ਲੋਕਾਂ ਦੀਆਂ ਜਿੰਦਗੀਆਂ ਉੱਤੇ ਵੱਡੇ ਪ੍ਰਭਾਵ ਪਾਉਂਦੇ ਹਨ, ਤਾਂ ਇਹ ਜ਼ਰੂਰੀ ਹੈ ਕਿ ਲੋਕ ਸਮਝ ਸਕਣ ਕਿ ਇਹ ਫੈਸਲੇ ਕਿਵੇਂ ਲਏ ਗਏ। ਉਦਾਹਰਨ ਵਜੋਂ, ਕੱਛੂਕਾਰੀ ਇੱਕ AI ਪ੍ਰਣਾਲੀ ਦੀ ਵਰਤੋਂ ਕਰ ਸਕਦਾ ਹੈ ਇਹ ਫੈਸਲਾ ਕਰਨ ਲਈ ਕਿ ਕੋਈ ਵਿਅਕਤੀ ਕ੍ਰੈਡਿਟ ਯੋਗ ਹੈ ਜਾਂ ਨਹੀਂ। ਇੱਕ ਕੰਪਨੀ ਇੱਕ AI ਪ੍ਰਣਾਲੀ ਦੀ ਵਰਤੋਂ ਕਰ ਸਕਦੀ ਹੈ ਇਹ ਪਤਾ ਕਰਨ ਲਈ ਕਿ ਸਭ ਤੋਂ ਯੋਗ ਉਮੀਦਵਾਰ ਕੌਣ ਹਨ।

- **ਪ੍ਰਾਈਵੇਸੀ ਅਤੇ ਸੁਰੱਖਿਆ**: ਜਿਵੇਂ-जਿਵੇਂ AI ਵੱਧ ਰਹੀ ਹੈ, ਪ੍ਰਾਈਵੇਸੀ ਦੀ ਰੱਖਿਆ ਅਤੇ ਨਿੱਜੀ ਅਤੇ ਵਪਾਰਕ ਜਾਣਕਾਰੀ ਦੀ ਸੁਰੱਖਿਆ ਹੋਰ ਮਹੱਤਵਪੂਰਨ ਅਤੇ ਜਟਿਲ ਹੋ ਰਹੀ ਹੈ। AI ਨਾਲ, ਪ੍ਰਾਈਵੇਸੀ ਅਤੇ ਡਾਟਾ ਸੁਰੱਖਿਆ ਨੂੰ ਵਿਸ਼ੇਸ਼ ਧਿਆਨ ਦੀ ਲੋੜ ਹੈ ਕਿਉਂਕਿ ਡਾਟਾ ਤੱਕ ਪਹੁੰਚ AI ਪ੍ਰਣਾਲੀਆਂ ਨੂੰ ਲੋੜੀਂਦੇ ਸਹੀ ਅਤੇ ਸੂਚਿਤ ਭਵਿੱਖਬਾਣੀਆਂ ਅਤੇ ਫੈਸਲੇ ਕਰਨ ਲਈ ਅਹਮ ਹੈ।

- **ਜਵਾਬਦੇਹੀ**: ਜਿਹੜੇ ਲੋਕ AI ਪ੍ਰਣਾਲੀਆਂ ਦਾ ਡਿਜ਼ਾਈਨ ਅਤੇ ਤਾਇਨਾਤ ਕਰਦੇ ਹਨ ਉਹਨਾਂ ਨੂੰ ਇਹਦਾ ਜਵਾਬਦੇਹ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ ਕਿ ਉਹਨਾਂ ਦੀਆਂ ਪ੍ਰਣਾਲੀਆਂ ਕਿਵੇਂ ਕਾਰਜ ਕਰਦੀਆਂ ਹਨ। ਸੰਗਠਨਾਂ ਨੂੰ ਉਦਯੋਗਕ ਮਿਆਰੀਆਂ ਦਾ ਸਹਾਰਾ ਲੈ ਕੇ ਜਵਾਬਦੇਹੀ ਦੇ ਨਿਯਮ ਬਣਾਏ ਜਾਣੇ ਚਾਹੀਦੇ ਹਨ। ਇਹ ਨਿਯਮ ਇਹ ਨਿਸ਼ਚਿਤ ਕਰ ਸਕਦੇ ਹਨ ਕਿ AI ਪ੍ਰਣਾਲੀਆਂ ਲੋਕਾਂ ਦੀ ਜਿੰਦਗੀ ਉੱਤੇ ਪ੍ਰਭਾਵ ਪਾਉਣ ਵਾਲੇ ਕਿਸੇ ਵੀ ਫੈਸਲੇ ਦਾ ਆਖਰੀ ਅਧਿਕਾਰ ਨਹੀਂ ਹਨ। ਇਹ ਵੀ ਨਿਸ਼ਚਿਤ ਕਰ ਸਕਦੇ ਹਨ ਕਿ ਮਨੁੱਖ ਵੱਡੀ ਖੁਦਮੁਖਤਾਰੀ ਵਾਲੀਆਂ AI ਪ੍ਰਣਾਲੀਆਂ 'ਤੇ ਜਾਇਜ਼ ਨਿਯੰਤਰਣ ਜਾਰੀ ਰੱਖਣ।

![Fill hub.](../../../../../../translated_images/pa/responsibleai2.c07ef430113fad8c.webp)

*ਚਿੱਤਰ ਸਰੋਤ: [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> Microsoft ਦੇ Responsible AI ਸਿਧਾਂਤਾਂ ਬਾਰੇ ਹੋਰ ਜਾਣਨ ਲਈ, [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723) 'ਤੇ ਜਾਓ।

#### ਸੁਰੱਖਿਆ ਮੈਟ੍ਰਿਕਸ

ਇਸ ਟਿਊਟੋਰਿਯਲ ਵਿੱਚ, ਤੁਸੀਂ Microsoft Foundry ਦੇ ਸੁਰੱਖਿਆ ਮੈਟ੍ਰਿਕਸ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਫਾਈਨ-ਟੀਊਨ ਕੀਤੇ Phi-3 ਮਾਡਲ ਦੀ ਸੁਰੱਖਿਆ ਦਾ ਮੁਲਾਂਕਣ ਕਰੋਗੇ। ਇਹ ਮੈਟ੍ਰਿਕਸ ਤੁਹਾਨੂੰ ਮਾਡਲ ਦੀ ਨੁਕਸਾਨਦੇਹ ਸਮੱਗਰੀ ਬਣਾਉਣ ਦੀ ਸੰਭਾਵਨਾ ਅਤੇ jailbreak ਹਮਲਿਆਂ ਵੱਲ ਸੰਵੇਦਨਸ਼ੀਲਤਾ ਦਾ ਮੁਲਾਂਕਣ ਕਰਨ ਵਿੱਚ ਮਦਦ ਕਰਦੇ ਹਨ। ਸੁਰੱਖਿਆ ਮੈਟ੍ਰਿਕਸ ਵਿੱਚ ਸ਼ਾਮਿਲ ਹਨ:

- **ਆਤਮ-ਹਾਨੀ ਸੰਬੰਧੀ ਸਮੱਗਰੀ**: ਇਹ ਮੁਲਾਂਕਣ ਕਰਦਾ ਹੈ ਕਿ ਮਾਡਲ ਕੋਲ ਆਤਮ-ਹਾਨੀ ਸੰਬੰਧੀ ਸਮੱਗਰੀ ਬਣਾਉਣ ਦਾ ਰੁਝਾਨ ਹੈ ਜਾਂ ਨਹੀਂ।
- **ਨਿੰਦਾਤਮਕ ਅਤੇ ਅਨਿਆਂਯ ਸਮੱਗਰੀ**: ਇਹ ਮੁਲਾਂਕਣ ਕਰਦਾ ਹੈ ਕਿ ਮਾਡਲ ਕੋਲ ਨਿੰਦਾਤਮਕ ਜਾਂ ਅਨਿਆਂਯ ਸਮੱਗਰੀ ਬਣਾਉਣ ਦਾ ਰੁਝਾਨ ਹੈ ਜਾਂ ਨਹੀਂ।
- **ਹਿੰਸਕ ਸਮੱਗਰੀ**: ਇਹ ਮੁਲਾਂਕਣ ਕਰਦਾ ਹੈ ਕਿ ਮਾਡਲ ਕੋਲ ਹਿੰਸਕ ਸਮੱਗਰੀ ਬਣਾਉਣ ਦਾ ਰੁਝਾਨ ਹੈ ਜਾਂ ਨਹੀਂ।
- **ਲਿੰਗ ਸੰਬੰਧੀ ਸਮੱਗਰੀ**: ਇਹ ਮੁਲਾਂਕਣ ਕਰਦਾ ਹੈ ਕਿ ਮਾਡਲ ਕੋਲ ਅਣੁਚਿਤ ਲਿੰਗ ਸੰਬੰਧੀ ਸਮੱਗਰੀ ਬਣਾਉਣ ਦਾ ਰੁਝਾਨ ਹੈ ਜਾਂ ਨਹੀਂ।

ਇਨ੍ਹਾਂ ਪੱਖਾਂ ਦਾ ਮੁਲਾਂਕਣ ਇਹ ਯਕੀਨੀ ਬਣਾਉਂਦਾ ਹੈ ਕਿ AI ਮਾਡਲ ਨੁਕਸਾਨਦੇਹ ਜਾਂ ਅਪਮਾਨਜਨਕ ਸਮੱਗਰੀ ਉਤਪੰਨ ਨਾ ਕਰੇ, ਜੋ ਕਿ ਸਮਾਜਿਕ ਮੁੱਲਾਂ ਅਤੇ ਨਿਯਮਕੀਆਂ ਨਾਲ ਅਨੁਕੂਲ ਹੈ।

![Evaluate based on safety.](../../../../../../translated_images/pa/evaluate-based-on-safety.c5df819f5b0bfc07.webp)

### ਪ੍ਰਦਰਸ਼ਨ ਮੁਲਾਂਕਣ ਦਾ ਪਰਿਚਯ

ਤੁਹਾਡੇ AI ਮਾਡਲ ਦੇ ਉਮੀਦ ਮੁਤਾਬਕ ਕੰਮ ਕਰਨ ਨੂੰ ਯਕੀਨੀ ਬਣਾਉਣ ਲਈ ਇਸ ਦਾ ਪ੍ਰਦਰਸ਼ਨ ਪ੍ਰਦਰਸ਼ਨ ਮੈਟ੍ਰਿਕਸ ਦੇ ਖਿਲਾਫ ਮੁਲਾਂਕਣ ਕਰਨਾ ਜ਼ਰੂਰੀ ਹੈ। Microsoft Foundry ਵਿੱਚ, ਪ੍ਰਦਰਸ਼ਨ ਮੁਲਾਂਕਣ ਤੁਹਾਨੂੰ ਤੁਹਾਡੇ ਮਾਡਲ ਦੀ ਪ੍ਰਭਾਵਸ਼ੀਲਤਾ ਨੂੰ ਸਹੀ, ਸਮੰਬੰਧਤ ਅਤੇ ਸੁਚੱਜੇ ਜਵਾਬਾਂ ਦੇਣ ਵਿੱਚ ਮੁਲਾਂਕਣ ਕਰਨ ਦੇ ਯੋਗ ਬਣਾਉਂਦੇ ਹਨ।

![Safaty evaluation.](../../../../../../translated_images/pa/performance-evaluation.48b3e7e01a098740.webp)

*ਚਿੱਤਰ ਸਰੋਤ: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### ਪ੍ਰਦਰਸ਼ਨ ਮੈਟ੍ਰਿਕਸ

ਇਸ ਟਿਊਟੋਰਿਯਲ ਵਿੱਚ, ਤੁਸੀਂ Microsoft Foundry ਦੇ ਪ੍ਰਦਰਸ਼ਨ ਮੈਟ੍ਰਿਕਸ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਫਾਈਨ-ਟੀਊਨ ਕੀਤੇ Phi-3 / Phi-3.5 ਮਾਡਲ ਦੇ ਪ੍ਰਦਰਸ਼ਨ ਦਾ ਮੁਲਾਂਕਣ ਕਰੋਗੇ। ਇਹ ਮੈਟ੍ਰਿਕਸ ਤੁਹਾਨੂੰ ਮਾਡਲ ਦੀ ਪ੍ਰਭਾਵਸ਼ੀਲਤਾ ਨੂੰ ਸਹੀ, ਸਮੰਬੰਧਤ ਅਤੇ ਸੁਚੱਜੇ ਜਵਾਬਾਂ ਦੇਣ ਵਿੱਚ ਮੁਲਾਂਕਣ ਕਰਨ ਵਿੱਚ ਮਦਦ ਕਰਦੇ ਹਨ। ਪ੍ਰਦਰਸ਼ਨ ਮੈਟ੍ਰਿਕਸ ਵਿੱਚ ਸ਼ਾਮਿਲ ਹਨ:

- **ਗਰਾਊਂਡਡਨੈਸ**: ਮੁਲਾਂਕਣ ਕਰੋ ਕਿ ਬਣਾਏ ਗਏ ਜਵਾਬ ਕਿਵੇਂ ਇਨਪੁੱਟ ਸਰੋਤ ਤੋਂ ਮਿਲਦੀਆਂ ਜਾਣਕਾਰੀਆਂ ਨਾਲ ਜੋੜਦੇ ਹਨ।
- **ਸਮਬੰਧਤਾ**: ਪ੍ਰਸ਼ਨਾਂ ਲਈ ਉਤਪੰਨ ਜਵਾਬਾਂ ਦੀ ਪ੍ਰਸੰਗਿਕਤਾ ਦਾ ਮੁਲਾਂਕਣ ਕਰੋ।
- **ਸਮਰੂਪਤਾ**: ਮੁਲਾਂਕਣ ਕਰੋ ਕਿ ਬਣਾਇਆ ਗਿਆ ਟੈਕਸਟ ਕਿਵੇਂ ਸੁਚਾਰੂ ਤਰੀਕੇ ਨਾਲ ਝਲਕ ਦਿੰਦਾ ਹੈ, ਕੁਦਰਤੀ ਪੜ੍ਹਦਾ ਹੈ ਅਤੇ ਮਨੁੱਖੀ ਭਾਸ਼ਾ ਵਰਗਾ ਲੱਗਦਾ ਹੈ।
- **ਫਲੂਐਂਸੀ**: ਬਣਾਏ ਗਏ ਟੈਕਸਟ ਦੀ ਭਾਸ਼ਾ ਪ੍ਰਵੀਂਤਾ ਦਾ ਮੁਲਾਂਕਣ ਕਰੋ।
- **GPT ਸਮਾਨਤਾ**: ਬਣਾਏ ਗਏ ਜਵਾਬ ਦੀ ਸਾਂਝੀ-ਹਕੀਕਤ ਨਾਲ ਸਮਾਨਤਾ ਲਈ ਤੁਲਨਾ ਕਰੋ।
- **F1 ਸਕੋਰ**: ਬਣਾਏ ਗਏ ਜਵਾਬ ਅਤੇ ਸਰੋਤ ਡਾਟਾ ਵਿਚਕਾਰ ਸਾਂਝੇ ਸ਼ਬਦਾਂ ਦਾ ਅਨੁਪਾਤ ਗਣਨਾ ਕਰੋ।

ਇਹ ਮੈਟ੍ਰਿਕਸ ਤੁਹਾਨੂੰ ਮਾਡਲ ਦੀ ਪ੍ਰਭਾਵਸ਼ੀਲਤਾ ਨੂੰ ਸਹੀ, ਸਮੰਬੰਧਤ ਅਤੇ ਸੁਚੱਜੇ ਜਵਾਬਾਂ ਦੇਣ ਵਿੱਚ ਮੁਲਾਂਕਣ ਕਰਨ ਵਿੱਚ ਮਦਦ ਕਰਦੇ ਹਨ।

![Evaluate based on performance.](../../../../../../translated_images/pa/evaluate-based-on-performance.3e801c647c7554e8.webp)

## **ਸਥਿਤੀ 2: Microsoft Foundry ਵਿੱਚ Phi-3 / Phi-3.5 ਮਾਡਲ ਦੀ ਮੁਲਾਂਕਣ**

### ਸ਼ੁਰੂ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ

ਇਹ ਟਿਊਟੋਰਿਯਲ ਪਹਿਲਾਂ ਦੇ ਬਲੌਗ ਪੋਸਟਾਂ "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" ਅਤੇ "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)" ਦਾ ਅਗਲਾ ਹਿੱਸਾ ਹੈ। ਇਨ੍ਹਾਂ ਪੋਸਟਾਂ ਵਿੱਚ, ਅਸੀਂ Microsoft Foundry ਵਿੱਚ Phi-3 / Phi-3.5 ਮਾਡਲ ਨੂੰ ਫਾਈਨ-ਟੀਊਨ ਕਰਨ ਅਤੇ Prompt flow ਨਾਲ ਇੰਟਿਗ੍ਰੇਟ ਕਰਨ ਦੀ ਪ੍ਰਕਿਰਿਆ ਨੂੰ ਵੇਖਿਆ ਸੀ।

ਇਸ ਟਿਊਟੋਰਿਯਲ ਵਿੱਚ, ਤੁਸੀਂ Microsoft Foundry ਵਿੱਚ ਇੱਕ Azure OpenAI ਮਾਡਲ ਨੂੰ ਮੁਲਾਂਕਣਕਰਤਾ ਵਜੋਂ ਤਾਇਨਾਤ ਕਰੋਗੇ ਅਤੇ ਇਸ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਆਪਣੇ ਫਾਈਨ-ਟੀਊਨ ਕੀਤੇ Phi-3 / Phi-3.5 ਮਾਡਲ ਨੂੰ ਮੁਲਾਂਕਣ ਕਰੋਗੇ।

ਇਸ ਟਿਊਟੋਰਿਯਲ ਨੂੰ ਸ਼ੁਰੂ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ, ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਤੁਹਾਡੇ ਕੋਲ ਹੇਠਾਂ ਦਿੱਤੇ ਲੋੜੀਂਦੇ ਸਾਧਨ ਹਨ, ਜਿਵੇਂ ਕਿ ਪਿਛਲੇ ਟਿਊਟੋਰਿਯਲਾਂ ਵਿੱਚ ਵਰਣਨ ਕੀਤਾ ਗਿਆ ਹੈ:

1. ਫਾਈਨ-ਟੀਊਨ ਕੀਤੇ Phi-3 / Phi-3.5 ਮਾਡਲ ਦਾ ਮੁਲਾਂਕਣ ਕਰਨ ਲਈ ਤਿਆਰ ਕੀਤਾ ਡਾਟਾਸੈੱਟ।
1. Phi-3 / Phi-3.5 ਮਾਡਲ ਜੋ ਫਾਈਨ-ਟੀਊਨ ਹੋਇਆ ਹੈ ਅਤੇ Azure Machine Learning ’ਤੇ ਤਾਇਨਾਤ ਕੀਤਾ ਗਿਆ ਹੈ।
1. Microsoft Foundry ਵਿੱਚ ਆਪਣੇ ਫਾਈਨ-ਟੀਊਨ ਕੀਤੇ Phi-3 / Phi-3.5 ਮਾਡਲ ਨਾਲ ਇੰਟਿਗ੍ਰੇਟ ਕੀਤਾ Prompt flow।

> [!NOTE]
> ਤੁਸੀਂ ਪਿਛਲੇ ਬਲੌਗ ਪੋਸਟਾਂ ਵਿੱਚ ਡਾਊਨਲੋਡ ਕੀਤੇ **ULTRACHAT_200k** ਡਾਟਾਸੈੱਟ ਦੇ ਡਾਟਾ ਫੋਲਡਰ ਵਿੱਚ ਮੌਜੂਦ *test_data.jsonl* ਫਾਈਲ ਨੂੰ ਫਾਈਨ-ਟੀਊਨ ਕੀਤੇ Phi-3 / Phi-3.5 ਮਾਡਲ ਦਾ ਮੁਲਾਂਕਣ ਕਰਨ ਲਈ ਡਾਟਾਸੈੱਟ ਵਜੋਂ ਵਰਤੋਂ ਕਰੋਗੇ।

#### Microsoft Foundry ਵਿੱਚ Prompt flow ਨਾਲ ਕਸਟਮ Phi-3 / Phi-3.5 ਮਾਡਲ ਨੂੰ ਇੰਟਿਗ੍ਰੇਟ ਕਰੋ (ਪਹਿਲਾਂ ਕੋਡ ਅਧਾਰਿਤ ਤਰੀਕਾ)

> [!NOTE]
> ਜੇ ਤੁਸੀਂ "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)" ਵਿੱਚ ਦਿੱਤੇ ਲੋ-ਕੋਡ ਤਰੀਕੇ ਦੀ ਪਾਲਣਾ ਕੀਤੀ ਹੈ, ਤਾਂ ਤੁਸੀਂ ਇਸ ਕਸਰਤ ਨੂੰ ਛੱਡ ਕੇ ਅਗਲੀ ਕਸਰਤ ਵੱਲ ਵਧ ਸਕਦੇ ਹੋ।
> ਹਾਲਾਂਕਿ, ਜੇ ਤੁਸੀਂ ਆਪਣਾ Phi-3 / Phi-3.5 ਮਾਡਲ ਫਾਈਨ-ਟੀਊਨ ਕਰਨ ਅਤੇ ਤਾਇਨਾਤ ਕਰਨ ਲਈ "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" ਵਿੱਚ ਦਿੱਤੇ ਕੋਡ-ਪਹਿਲਾਂ ਤਰੀਕੇ ਦੀ ਪਾਲਣਾ ਕੀਤੀ ਹੈ, ਤਾਂ ਤੁਹਾਡੇ ਮਾਡਲ ਨੂੰ Prompt flow ਨਾਲ ਜੋੜਨ ਦੀ ਪ੍ਰਕਿਰਿਆ ਕੁਝ ਵੱਖਰੀ ਹੈ। ਤੁਸੀਂ ਇਸ ਕਸਰਤ ਵਿੱਚ ਇਸ ਪ੍ਰਕਿਰਿਆ ਨੂੰ ਸਿੱਖੋਗੇ।

ਅੱਗੇ ਵਧਣ ਲਈ, ਤੁਹਾਨੂੰ Microsoft Foundry ਵਿੱਚ Prompt flow ਵਿੱਚ ਆਪਣੇ ਫਾਈਨ-ਟੀਊਨਾਂ Phi-3 / Phi-3.5 ਮਾਡਲ ਨੂੰ ਇੰਟਿਗ੍ਰੇਟ ਕਰਨ ਦੀ ਲੋੜ ਹੈ।

#### Microsoft Foundry ਹੱਬ ਬਣਾਓ

ਪ੍ਰੋਜੈਕਟ ਬਣਾਉਣ ਤੋਂ ਪਹਿਲਾਂ ਤੁਹਾਨੂੰ ਇੱਕ ਹੱਬ ਬਣਾਉਣਾ ਹੋਵੇਗਾ। ਇੱਕ ਹੱਬ ਇੱਕ ਰਿਸੋਰਸ ਗਰੁੱਪ ਵਰਗਾ ਕੰਮ ਕਰਦਾ ਹੈ, ਜੋ Microsoft Foundry ਵਿੱਚ ਕਈ ਪ੍ਰੋਜੈਕਟਾਂ ਨੂੰ ਜਥੇਬੰਦੀ ਅਤੇ ਪ੍ਰਬੰਧਿਤ ਕਰਨ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ।
1. [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) ਵਿੱਚ ਸਾਈਨ ਇਨ ਕਰੋ।

1. ਖੱਬੇ ਪਾਸੇ ਟੈਬ ਤੋਂ **ਸਾਰੇ ਹਬ** ਚੁਣੋ।

1. ਨੈਵੀਗੇਸ਼ਨ ਮੀਨੂ ਤੋਂ **+ ਨਵਾਂ ਹਬ** ਚੁਣੋ।

    ![Create hub.](../../../../../../translated_images/pa/create-hub.5be78fb1e21ffbf1.webp)

1. ਹੇਠ ਲਿਖੇ ਕਾਰਜ ਕਰੋ:

    - **ਹਬ ਨਾਮ** ਦਰਜ ਕਰੋ। ਇਹ ਇਕ ਵਿਲੱਖਣ ਮੁੱਲ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ।
    - ਆਪਣੀ Azure **ਸਬਸਕ੍ਰਿਪਸ਼ਨ** ਚੁਣੋ।
    - ਵਰਤੋਂ ਲਈ **ਰਿਸੋਰਸ ਗਰੁੱਪ** ਚੁਣੋ (ਗਰਜ ਪੈਣ 'ਤੇ ਨਵਾਂ ਬਣਾਓ)।
    - ਵਰਤੋਂ ਲਈ **ਟਿਕਾਣਾ** ਚੁਣੋ।
    - ਵਰਤੋਂ ਲਈ **Azure AI Services ਨੂੰ ਜੋੜੋ** ਚੁਣੋ (ਗਰਜ ਪੈਣ 'ਤੇ ਨਵਾਂ ਬਣਾਓ)।
    - **Azure AI Search ਜੋੜੋ** ਨੂੰ **ਜੋੜਨ ਤੋਂ ਬਚੋ** ਚੁਣੋ।

    ![Fill hub.](../../../../../../translated_images/pa/fill-hub.baaa108495c71e34.webp)

1. **ਅਗਲਾ** ਚੁਣੋ।

#### Microsoft Foundry ਪ੍ਰੋਜੈਕਟ ਬਣਾਓ

1. ਆਪਣੇ ਬਣਾਏ ਹੋਏ ਹਬ ਵਿੱਚ, ਖੱਬੇ ਪਾਸੇ ਟੈਬ ਤੋਂ **ਸਾਰੇ ਪ੍ਰੋਜੈਕਟ** ਚੁਣੋ।

1. ਨੈਵੀਗੇਸ਼ਨ ਮੀਨੂ ਤੋਂ **+ ਨਵਾਂ ਪ੍ਰੋਜੈਕਟ** ਚੁਣੋ।

    ![Select new project.](../../../../../../translated_images/pa/select-new-project.cd31c0404088d7a3.webp)

1. **ਪ੍ਰੋਜੈਕਟ ਦਾ ਨਾਮ** ਦਰਜ ਕਰੋ। ਇਹ ਇਕ ਵਿਲੱਖਣ ਮੁੱਲ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ।

    ![Create project.](../../../../../../translated_images/pa/create-project.ca3b71298b90e420.webp)

1. **ਪ੍ਰੋਜੈਕਟ ਬਣਾਓ** ਚੁਣੋ।

#### ਫਾਈਨ-ਟਿਊਨ ਕੀਤੇ Phi-3 / Phi-3.5 ਮਾਡਲ ਲਈ ਕਸਟਮ ਕਨੈਕਸ਼ਨ ਜੋੜੋ

ਆਪਣੇ ਕਸਟਮ Phi-3 / Phi-3.5 ਮਾਡਲ ਨੂੰ Prompt flow ਨਾਲ ਇੰਟੀਗ੍ਰੇਟ ਕਰਨ ਲਈ, ਤੁਹਾਨੂੰ ਮਾਡਲ ਦਾ ਐਂਡਪਵਾਇੰਟ ਅਤੇ ਕੀ ਇੱਕ ਕਸਟਮ ਕਨੈਕਸ਼ਨ ਵਿੱਚ ਸੇਵ ਕਰਨਾ ਪੈਂਦਾ ਹੈ। ਇਹ ਸੈਟਅੱਪ ਤੁਹਾਡੇ ਕਸਟਮ Phi-3 / Phi-3.5 ਮਾਡਲ ਤੱਕ Prompt flow ਵਿੱਚ ਪਹੁੰਚ ਨੂੰ ਯਕੀਨੀ ਬਣਾਉਂਦਾ ਹੈ।

#### ਫਾਈਨ-ਟਿਊਨ ਕੀਤੇ Phi-3 / Phi-3.5 ਮਾਡਲ ਦਾ api ਕੀ ਅਤੇ endpoint uri ਸੈਟ ਕਰੋ

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) 'ਤੇ ਜਾਓ।

1. ਆਪਣਾ ਬਣਾਇਆ ਹੋਇਆ Azure Machine learning ਵਰਕਸਪੇਸ ਖੋਲ੍ਹੋ।

1. ਖੱਬੇ ਪਾਸੇ ਟੈਬ ਤੋਂ **Endpoints** ਚੁਣੋ।

    ![Select endpoints.](../../../../../../translated_images/pa/select-endpoints.ee7387ecd68bd18d.webp)

1. ਉਸ ਐਂਡਪਵਾਇੰਟ ਨੂੰ ਚੁਣੋ ਜੋ ਤੁਸੀਂ ਬਣਾਇਆ ਹੈ।

    ![Select endpoints.](../../../../../../translated_images/pa/select-endpoint-created.9f63af5e4cf98b2e.webp)

1. ਨੈਵੀਗੇਸ਼ਨ ਮੀਨੂ ਤੋਂ **Consume** ਚੁਣੋ।

1. ਆਪਣਾ **REST endpoint** ਅਤੇ **Primary key** ਨਕਲ ਕਰੋ।

    ![Copy api key and endpoint uri.](../../../../../../translated_images/pa/copy-endpoint-key.0650c3786bd646ab.webp)

#### ਕਸਟਮ ਕਨੈਕਸ਼ਨ ਜੋੜੋ

1. [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) 'ਤੇ ਜਾਓ।

1. ਆਪਣੇ ਬਣਾਏ ਹੋਏ Microsoft Foundry ਪ੍ਰੋਜੈਕਟ ਵਿੱਚ ਜਾਓ।

1. ਆਪਣੇ ਬਣਾਏ ਹੋਏ ਪ੍ਰੋਜੈਕਟ ਵਿੱਚ, ਖੱਬੇ ਪਾਸੇ ਟੈਬ ਤੋਂ **Settings** ਚੁਣੋ।

1. **+ ਨਵਾਂ ਕਨੈਕਸ਼ਨ** ਚੁਣੋ।

    ![Select new connection.](../../../../../../translated_images/pa/select-new-connection.fa0f35743758a74b.webp)

1. ਨੈਵੀਗੇਸ਼ਨ ਮੀਨੂ ਤੋਂ **Custom keys** ਚੁਣੋ।

    ![Select custom keys.](../../../../../../translated_images/pa/select-custom-keys.5a3c6b25580a9b67.webp)

1. ਹੇਠ ਲਿਖੇ ਕਾਰਜ ਕਰੋ:

    - **+ Add key value pairs** ਚੁਣੋ।
    - ਕੀ ਦਾ ਨਾਮ ਦਰਜ ਕਰੋ **endpoint** ਅਤੇ Azure ML Studio ਤੋਂ ਨਕਲ ਕੀਤਾ endpoint ਮੁੱਲ ਖੇਤਰ ਵਿੱਚ ਪੇਸਟ ਕਰੋ।
    - ਫਿਰ **+ Add key value pairs** ਚੁਣੋ।
    - ਕੀ ਦਾ ਨਾਮ ਦਰਜ ਕਰੋ **key** ਅਤੇ Azure ML Studio ਤੋਂ ਨਕਲ ਕੀਤਾ ਕੀ ਮੁੱਲ ਖੇਤਰ ਵਿੱਚ ਪੇਸਟ ਕਰੋ।
    - ਚਾਬੀਆਂ ਜੋੜਨ ਤੋਂ ਬਾਅਦ, ਕੀ ਨੂੰ ਲੁਕਾਉਣ ਲਈ **is secret** ਚੁਣੋ।

    ![Add connection.](../../../../../../translated_images/pa/add-connection.ac7f5faf8b10b0df.webp)

1. **Add connection** ਚੁਣੋ।

#### Prompt flow ਬਣਾਓ

ਤੁਸੀਂ Microsoft Foundry ਵਿੱਚ ਕਸਟਮ ਕਨੈਕਸ਼ਨ ਜੋੜ ਚੁਕੇ ਹੋ। ਹੁਣ, ਹੇਠ ਲਿਖੇ ਕਦਮਾਂ ਨਾਲ Prompt flow ਬਣਾਓ। ਫਿਰ, ਤੁਸੀਂ ਇਸ Prompt flow ਨੂੰ ਕਸਟਮ ਕਨੈਕਸ਼ਨ ਨਾਲ ਜੋੜ ਕੇ ਫਾਈਨ-ਟਿਊਨ ਕੀਤੇ ਮਾਡਲ ਨੂੰ Prompt flow ਵਿੱਚ ਵਰਤੋਂ ਕਰਨ ਦੇ ਯੋਗ ਬਣਾਓਗੇ।

1. ਆਪਣੇ ਬਣਾਏ ਹੋਏ Microsoft Foundry ਪ੍ਰੋਜੈਕਟ ਵਿੱਚ ਜਾਓ।

1. ਖੱਬੇ ਪਾਸੇ ਟੈਬ ਤੋਂ **Prompt flow** ਚੁਣੋ।

1. ਨੈਵੀਗੇਸ਼ਨ ਮੀਨੂ ਤੋਂ **+ Create** ਚੁਣੋ।

    ![Select Promptflow.](../../../../../../translated_images/pa/select-promptflow.18ff2e61ab9173eb.webp)

1. ਨੈਵੀਗੇਸ਼ਨ ਮੀਨੂ ਤੋਂ **Chat flow** ਚੁਣੋ।

    ![Select chat flow.](../../../../../../translated_images/pa/select-flow-type.28375125ec9996d3.webp)

1. ਵਰਤੋਂ ਲਈ **ਫੋਲਡਰ ਨਾਂ** ਦਰਜ ਕਰੋ।

    ![Select chat flow.](../../../../../../translated_images/pa/enter-name.02ddf8fb840ad430.webp)

1. **Create** ਚੁਣੋ।

#### ਆਪਣੇ ਕਸਟਮ Phi-3 / Phi-3.5 ਮਾਡਲ ਨਾਲ ਗੱਲਬਾਤ ਲਈ Prompt flow ਸੈਟਅੱਪ ਕਰੋ

ਤੁਹਾਨੂੰ ਫਾਈਨ-ਟਿਊਨ ਕੀਤੇ Phi-3 / Phi-3.5 ਮਾਡਲ ਨੂੰ ਇੱਕ Prompt flow ਵਿੱਚ इੰਟੇگریਟ ਕਰਨਾ ਹੈ। ਪਰ ਮੌਜੂਦਾ Prompt flow ਇਸ ਮਕਸਦ ਲਈ ਬਣਾਇਆ ਨਹੀਂ ਗਿਆ। ਇਸ ਲਈ, ਤੁਹਾਨੂੰ Prompt flow ਨੂੰ ਮੁੜ ਡਿਜ਼ਾਈਨ ਕਰਨਾ ਪਵੇਗਾ ਤਾਂ ਜੋ ਕਸਟਮ ਮਾਡਲ ਦੀ ਇੰਟੇਗ੍ਰੇਸ਼ਨ ਕੀਤੀ ਜਾ ਸਕੇ।

1. Prompt flow ਵਿੱਚ, ਮੌਜੂਦਾ ਫਲੋ ਦੁਬਾਰਾ ਬਣਾਉਣ ਲਈ ਹੇਠ ਲਿਖੇ ਕੰਮ ਕਰੋ:

    - **Raw file mode** ਚੁਣੋ।
    - *flow.dag.yml* ਫਾਇਲ ਵਿੱਚ ਸਾਰੇ ਮੌਜੂਦਾ ਕੋਡ ਨੂੰ ਹਟਾਓ।
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

    ![Select raw file mode.](../../../../../../translated_images/pa/select-raw-file-mode.06c1eca581ce4f53.webp)

1. *integrate_with_promptflow.py* ਵਿੱਚ ਹੇਠ ਲਿਖਿਆ ਕੋਡ ਸ਼ਾਮਲ ਕਰੋ ਤਾਂ ਜੋ Prompt flow ਵਿੱਚ ਕਸਟਮ Phi-3 / Phi-3.5 ਮਾਡਲ ਦੀ ਵਰਤੋਂ ਹੋ ਸਕੇ।

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # ਲੌਗਿੰਗ ਸੈਟਅਪ
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

        # "connection" ਕਸਟਮ ਕਨੈਕਸ਼ਨ ਦਾ ਨਾਮ ਹੈ, "endpoint", "key" ਕਸਟਮ ਕਨੈਕਸ਼ਨ ਵਿੱਚ ਕੁੰਜੀਆਂ ਹਨ
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
            
            # ਪੂਰੇ JSON ਜਵਾਬ ਨੂੰ ਲੌਗ ਕਰੋ
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

    ![Paste prompt flow code.](../../../../../../translated_images/pa/paste-promptflow-code.cd6d95b101c0ec28.webp)

> [!NOTE]
> Microsoft Foundry ਵਿੱਚ Prompt flow ਵਰਤੋਂ ਬਾਰੇ ਹੋਰ ਵਿਸਥਾਰਵਾਹ ਜਾਣਕਾਰੀ ਲਈ, ਤੁਸੀਂ [Microsoft Foundry ਵਿੱਚ Prompt flow](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow) ਵੇਖ ਸਕਦੇ ਹੋ।

1. **Chat input**, **Chat output** ਚੁਣੋ ਤਾਂ ਜੋ ਆਪਣੇ ਮਾਡਲ ਨਾਲ ਗੱਲਬਾਤ ਯੋਗ ਬਣੇ।

    ![Select Input Output.](../../../../../../translated_images/pa/select-input-output.c187fc58f25fbfc3.webp)

1. ਹੁਣ ਤੁਸੀਂ ਆਪਣੇ ਕਸਟਮ Phi-3 / Phi-3.5 ਮਾਡਲ ਨਾਲ ਗੱਲਬਾਤ ਕਰਨ ਲਈ ਤਿਆਰ ਹੋ। ਅਗਲੇ ਅਭਿਆਸ ਵਿੱਚ, ਤੁਸੀਂ ਸਿੱਖੋਗੇ ਕਿ ਕਿਵੇਂ Prompt flow ਨੂੰ ਸ਼ੁਰੂ ਕਰਨਾ ਹੈ ਅਤੇ ਇਸ ਦਾ ਉਪਯੋਗ ਕਰਕੇ ਆਪਣੇ ਫਾਈਨ-ਟਿਊਨ ਕੀਤੇ Phi-3 / Phi-3.5 ਮਾਡਲ ਨਾਲ ਗੱਲਬਾਤ ਕਰਨੀ ਹੈ।

> [!NOTE]
>
> ਦੁਬਾਰਾ ਬਣਾਇਆ ਗਿਆ ਫਲੋ ਹੇਠਾਂ ਦਿੱਤੀ ਤਸਵੀਰ ਵਾਂਗ ਲੱਗਣਾ ਚਾਹੀਦਾ ਹੈ:
>
> ![Flow example](../../../../../../translated_images/pa/graph-example.82fd1bcdd3fc545b.webp)
>

#### Prompt flow ਸ਼ੁਰੂ ਕਰੋ

1. Prompt flow ਸ਼ੁਰੂ ਕਰਨ ਲਈ **Start compute sessions** ਚੁਣੋ।

    ![Start compute session.](../../../../../../translated_images/pa/start-compute-session.9acd8cbbd2c43df1.webp)

1. ਪੈਰਾਮੀਟਰ ਨਵੇਂ ਕਰਨ ਲਈ **Validate and parse input** ਚੁਣੋ।

    ![Validate input.](../../../../../../translated_images/pa/validate-input.c1adb9543c6495be.webp)

1. ਉਸ **connection** ਦਾ **Value** ਚੁਣੋ ਜੋ ਤੁਸੀਂ ਕਸਟਮ ਕਨੈਕਸ਼ਨ ਲਈ ਬਣਾਇਆ ਹੈ। ਉਦਾਹਰਣ ਲਈ, *connection*।

    ![Connection.](../../../../../../translated_images/pa/select-connection.1f2b59222bcaafef.webp)

#### ਆਪਣੇ ਕਸਟਮ Phi-3 / Phi-3.5 ਮਾਡਲ ਨਾਲ ਗੱਲਬਾਤ ਕਰੋ

1. **Chat** ਚੁਣੋ।

    ![Select chat.](../../../../../../translated_images/pa/select-chat.0406bd9687d0c49d.webp)

1. ਨਤੀਜਿਆਂ ਦਾ ਉਦਾਹਰਣ: ਹੁਣ ਤੁਸੀਂ ਆਪਣੇ ਕਸਟਮ Phi-3 / Phi-3.5 ਮਾਡਲ ਨਾਲ ਗੱਲਬਾਤ ਕਰ ਸਕਦੇ ਹੋ। ਇਹ ਸਲਾਹ ਦਿੱਤੀ ਜਾਂਦੀ ਹੈ ਕਿ ਤੁਸੀਂ ਫਾਈਨ-ਟਿਊਨਿੰਗ ਲਈ ਵਰਤਦੇ ਡੇਟਾ ਅਧਾਰਿਤ ਸਵਾਲ ਪੁੱਛੋ।

    ![Chat with prompt flow.](../../../../../../translated_images/pa/chat-with-promptflow.1cf8cea112359ada.webp)

### Phi-3 / Phi-3.5 ਮਾਡਲ ਨੂੰ ਮੂਲਾਂਕਣ ਕਰਨ ਲਈ Azure OpenAI ਨੂੰ ਡੀਪਲੌਇ ਕਰੋ

Microsoft Foundry ਵਿੱਚ Phi-3 / Phi-3.5 ਮਾਡਲ ਦੀ ਮੂਲਾਂਕਣ ਲਈ ਤੁਹਾਨੂੰ ਇੱਕ Azure OpenAI ਮਾਡਲ ਡੀਪਲੌਇ ਕਰਨਾ ਪਵੇਗਾ। ਇਸ ਮਾਡਲ ਦੀ ਵਰਤੋਂ Phi-3 / Phi-3.5 ਮਾਡਲ ਦੇ ਪ੍ਰਦਰਸ਼ਨ ਨੂੰ ਮੂਲਾਂਕਣ ਕਰਨ ਲਈ ਕੀਤੀ ਜਾਵੇਗੀ।

#### Azure OpenAI ਡੀਪਲੌਇ ਕਰੋ

1. [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) ਵਿੱਚ ਸਾਈਨ ਇਨ ਕਰੋ।

1. ਆਪਣੇ ਬਣਾਏ ਹੋਏ Microsoft Foundry ਪ੍ਰੋਜੈਕਟ ਵਿੱਚ ਜਾਓ।

    ![Select Project.](../../../../../../translated_images/pa/select-project-created.5221e0e403e2c9d6.webp)

1. ਉਸ ਪਰੋਜੈਕਟ ਵਿੱਚ, ਖੱਬੇ ਪਾਸੇ ਟੈਬ ਤੋਂ **Deployments** ਚੁਣੋ।

1. ਨੈਵੀਗੇਸ਼ਨ ਮੇਨੂ ਤੋਂ **+ Deploy model** ਚੁਣੋ।

1. **Deploy base model** ਚੁਣੋ।

    ![Select Deployments.](../../../../../../translated_images/pa/deploy-openai-model.95d812346b25834b.webp)

1. ਵਰਤੋਂ ਲਈ Azure OpenAI ਮਾਡਲ ਚੁਣੋ। ਉਦਾਹਰਣ ਲਈ, **gpt-4o**।

    ![Select Azure OpenAI model you'd like to use.](../../../../../../translated_images/pa/select-openai-model.959496d7e311546d.webp)

1. **Confirm** ਚੁਣੋ।

### Microsoft Foundry ਦੇ Prompt flow ਮੁਲਾਂਕਣ ਨਾਲ ਫਾਈਨ-ਟਿਊਨ ਕੀਤੇ Phi-3 / Phi-3.5 ਮਾਡਲ ਦਾ ਮੁਲਾਂਕਣ ਕਰੋ

### ਨਵਾਂ ਮੁਲਾਂਕਣ ਸ਼ੁਰੂ ਕਰੋ

1. [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) ਵਿੱਚ ਜਾਓ।

1. ਆਪਣੇ ਬਣਾਏ ਹੋਏ Microsoft Foundry ਪਰੋਜੈਕਟ ਵਿੱਚ ਜਾਓ।

    ![Select Project.](../../../../../../translated_images/pa/select-project-created.5221e0e403e2c9d6.webp)

1. ਉਸ ਪ੍ਰੋਜੈਕਟ ਵਿੱਚ, ਖੱਬੇ ਪਾਸੇ ਟੈਬ ਤੋਂ **Evaluation** ਚੁਣੋ।

1. ਨੈਵੀਗੇਸ਼ਨ ਮੇਨੂ ਤੋਂ **+ New evaluation** ਚੁਣੋ।

    ![Select evaluation.](../../../../../../translated_images/pa/select-evaluation.2846ad7aaaca7f4f.webp)

1. **Prompt flow** ਮੁਲਾਂਕਣ ਚੁਣੋ।

    ![Select Prompt flow evaluation.](../../../../../../translated_images/pa/promptflow-evaluation.cb9758cc19b4760f.webp)

1. ਹੇਠ ਲਿਖੇ ਕੰਮ ਕਰੋ:

    - ਮੁਲਾਂਕਣ ਦਾ ਨਾਮ ਦਿਉ। ਇਹ ਇੱਕ ਵਿਲੱਖਣ ਮੁੱਲ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ।
    - ਟਾਸਕ ਦੀ ਕਿਸਮ ਵਜੋਂ **ਸੰਦਰਭ ਬਿਨਾਂ ਪ੍ਰਸ਼ਨ ਅਤੇ ਉੱਤਰ** ਚੁਣੋ ਕਿਉਂਕਿ ਇਸ ਟਿਊਟੋਰિયલ ਵਿੱਚ ਵਰਤੇ ਗਏ **ULTRACHAT_200k** ਡਾਟਾਸੈੱਟ ਵਿੱਚ ਸੰਦਰਭ ਨਹੀਂ ਹੈ।
    - ਉਹ prompt flow ਚੁਣੋ ਜਿਸਦਾ ਤੁਸੀਂ ਮੁਲਾਂਕਣ ਕਰਨਾ ਹੈ।

    ![Prompt flow evaluation.](../../../../../../translated_images/pa/evaluation-setting1.4aa08259ff7a536e.webp)

1. **ਅਗਲਾ** ਚੁਣੋ।

1. ਹੇਠ ਲਿਖੇ ਕੰਮ ਕਰੋ:

    - ਆਪਣਾ ਡੇਟਾਸੈੱਟ ਜਮ੍ਹਾਂ ਕਰਨ ਲਈ **Add your dataset** ਚੁਣੋ। ਉਦਾਹਰਨ ਲਈ, ਤੁਸੀਂ ਟੈਸਟ ਡੇਟਾਸੈੱਟ ਫਾਇਲ ਜਿਵੇਂ *test_data.json1* ਜਿਹੜੀ **ULTRACHAT_200k** ਡੇਟਾਸੈੱਟ ਨਾਲ ਸ਼ਾਮਲ ਹੈ, ਅਪਲੋਡ ਕਰ ਸਕਦੇ ਹੋ।
    - ਆਪਣੇ ਡੇਟਾਸੈੱਟ ਨਾਲ ਮਿਲਦੀ ਜੁਲਦੀ **Dataset column** ਚੁਣੋ। ਉਦਾਹਰਨ ਲਈ, ਜੇ ਤੁਸੀਂ **ULTRACHAT_200k** ਡਾਟਾਸੈੱਟ ਵਰਤ ਰਹੇ ਹੋ, ਤਾਂ **${data.prompt}** ਡੀਟਾਸੈੱਟ ਕਾਲਮ ਵਜੋਂ ਚੁਣੋ।

    ![Prompt flow evaluation.](../../../../../../translated_images/pa/evaluation-setting2.07036831ba58d64e.webp)

1. **ਅਗਲਾ** ਚੁਣੋ।

1. ਪ੍ਰਦਰਸ਼ਨ ਅਤੇ ਗੁਣਵੱਤਾ ਮਾਪਦੰਡ ਸੈਟ ਕਰਨ ਲਈ ਹੇਠ ਲਿਖੇ ਕੰਮ ਕਰੋ:

    - ਵਰਤੋਂ ਲਈ ਪ੍ਰਦਰਸ਼ਨ ਅਤੇ ਗੁਣਵੱਤਾ ਮਾਪਦੰਡ ਚੁਣੋ।
    - ਉਹ Azure OpenAI ਮਾਡਲ ਚੁਣੋ ਜੋ ਤੁਸੀਂ ਮੁਲਾਂਕਣ ਲਈ ਬਣਾਇਆ ਹੈ। ਉਦਾਹਰਨ ਵਜੋਂ **gpt-4o** ਚੁਣੋ।

    ![Prompt flow evaluation.](../../../../../../translated_images/pa/evaluation-setting3-1.d1ae69e3bf80914e.webp)

1. ਖ਼ਤਰਾ ਅਤੇ ਸੁਰੱਖਿਆ ਮਾਪਦੰਡ ਸੈਟ ਕਰਨ ਲਈ ਹੇਠ ਲਿਖੇ ਕੰਮ ਕਰੋ:

    - ਵਰਤੋਂ ਲਈ ਖ਼ਤਰਾ ਅਤੇ ਸੁਰੱਖਿਆ ਮਾਪਦੰਡ ਚੁਣੋ।
    - ਡੀਫੈਕਟ ਦਰ ਮਾਪਣ ਲਈ ਥਰੈਸ਼ੋਲਡ ਚੁਣੋ। ਉਦਾਹਰਨ ਵਜੋਂ **Medium** ਚੁਣੋ।
    - **question** ਲਈ, **Data source** ਵਜੋਂ **{$data.prompt}** ਚੁਣੋ।
    - **answer** ਲਈ, **Data source** ਵਜੋਂ **{$run.outputs.answer}** ਚੁਣੋ।
    - **ground_truth** ਲਈ, **Data source** ਵਜੋਂ **{$data.message}** ਚੁਣੋ।

    ![Prompt flow evaluation.](../../../../../../translated_images/pa/evaluation-setting3-2.d53bd075c60a45a2.webp)

1. **ਅਗਲਾ** ਚੁਣੋ।

1. ਮੁਲਾਂਕਣ ਸ਼ੁਰੂ ਕਰਨ ਲਈ **Submit** ਚੁਣੋ।

1. ਮੁਲਾਂਕਣ ਪੂਰਾ ਹੋਣ ਵਿੱਚ ਥੋੜਾ ਸਮਾਂ ਲੱਗੇਗਾ। ਤੁਸੀਂ **Evaluation** ਟੈਬ ਵਿੱਚ ਪ੍ਰਗਤੀ ਮਾਨੀਟਰ ਕਰ ਸਕਦੇ ਹੋ।

### ਮੁਲਾਂਕਣ ਦੇ ਨਤੀਜੇ ਸਮੀਖਿਆ ਕਰੋ

> [!NOTE]
> ਹੇਠਾਂ ਦਿੱਤੇ ਨਤੀਜੇ ਮੂਲਾਂਕਣ ਪ੍ਰਕਿਰਿਆ ਨੂੰ ਦਰਸਾਉਣ ਲਈ ਹਨ। ਇਸ ਟਿਊਟੋਰિયલ ਵਿੱਚ ਅਸੀਂ ਇੱਕ ਛੋਟੇ ਡੇਟਾਸੈੱਟ 'ਤੇ ਫਾਈਨ-ਟਿਊਨ ਕੀਤੇ ਮਾਡਲ ਦੀ ਵਰਤੋਂ ਕੀਤੀ ਹੈ, ਜਿਸ ਕਾਰਣ ਨਤੀਜੇ ਸੰਪੂਰਨ ਨਹੀਂ ਹੋ ਸਕਦੇ। ਅਸਲੀ ਨਤੀਜੇ ਬਹੁਤ ਵੱਧ ਜ਼ਿਆਦਾ ਜਾਂ ਘਟਕ ਹੋ ਸਕਦੇ ਹਨ, ਡੇਟਾਸੈੱਟ ਦੇ ਆਕਾਰ, ਗੁਣਵੱਤਾ ਅਤੇ ਵਿਭਿੰਨਤਾ ਨਾਲ ਅਤੇ ਮਾਡਲ ਦੇ ਵਿਸ਼ੇਸ਼ ਸੰਰਚਨਾ ਨਾਲ ਅਨੁਸਾਰ।

ਜਦੋਂ ਮੁਲਾਂਕਣ ਪੂਰਾ ਹੋ ਜਾਵੇ, ਤਦ ਪ੍ਰਦਰਸ਼ਨ ਅਤੇ ਸੁਰੱਖਿਆ ਮਾਪਦੰਡ ਦੋਹਾਂ ਲਈ ਨਤੀਜੇ ਸਮੀਖਿਆ ਕਰੋ।
1. ਪ੍ਰਦਰਸ਼ਨ ਅਤੇ ਗੁਣਵੱਤਾ ਮੈٽرਿਕਸ:

    - ਮਾਡਲ ਦੀ ਪ੍ਰਭਾਵਸ਼ੀਲਤਾ ਦਾ ਮੁਲਾਂਕਣ ਕਰੋ ਕਿ ਉਹ ਸਹੀ, ਸੁਚੱਜੇ ਅਤੇ ਸਬੰਧਿਤ ਜਵਾਬ ਕਿਵੇਂ ਤਿਆਰ ਕਰਦਾ ਹੈ।

    ![Evaluation result.](../../../../../../translated_images/pa/evaluation-result-gpu.85f48b42dfb74254.webp)

1. ਜੋਖਮ ਅਤੇ ਸੁਰੱਖਿਆ ਮੈਟਰਿਕਸ:

    - ਇਹ ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਮਾਡਲ ਦੇ ਨਤੀਜੇ ਸੁਰੱਖਿਅਤ ਹਨ ਅਤੇ ਜ਼ਿੰਮੇਵਾਰ ਏਆਈ ਸਿਧਾਂਤਾਂ ਨਾਲ ਮਿਲਦੇ ਹਨ, ਅਤੇ ਕਿਸੇ ਵੀ ਹਾਨਿਕਾਰਕ ਜਾਂ ਅਪਮਾਨਜਨਕ ਸਮੱਗਰੀ ਤੋਂ ਬਚਦੇ ਹਨ।

    ![Evaluation result.](../../../../../../translated_images/pa/evaluation-result-gpu-2.1b74e336118f4fd0.webp)

1. ਤੁਸੀਂ ਥੱਲੇ ਸਕ੍ਰੋਲ ਕਰਕੇ **ਵਿਸਥਾਰਿਤ ਮੈਟਰਿਕ ਨਤੀਜੇ** ਵੇਖ ਸਕਦੇ ਹੋ।

    ![Evaluation result.](../../../../../../translated_images/pa/detailed-metrics-result.afa2f5c39a4f5f17.webp)

1. ਆਪਣੀ ਕੱਸਟਮ Phi-3 / Phi-3.5 ਮਾਡਲ ਨੂੰ ਦੋਹਾਂ ਪ੍ਰਦਰਸ਼ਨ ਅਤੇ ਸੁਰੱਖਿਆ ਮੈਟਰਿਕਸ ਦੇ ਖਿਲਾਫ ਮੁਲਾਂਕਣ ਕਰਕੇ, ਤੁਸੀਂ ਇਹ ਪੁਸ਼ਟੀ ਕਰ ਸਕਦੇ ਹੋ ਕਿ ਮਾਡਲ ਕੇਵਲ ਪ੍ਰਭਾਵਸ਼ੀਲ ਨਹੀਂ ਹੈ, ਸਗੋਂ ਜ਼ਿੰਮੇਵਾਰ ਏਆਈ ਅਭਿਆਸਾਂ ਨੂੰ ਵੀ ਮੰਨਦਾ ਹੈ, ਜਿਸ ਨਾਲ ਇਹ ਹਕੀਕਤੀ ਦੁਨੀਆ ਵਿੱਚ ਤਿਆਰ ਹੈ।

## ਵਧਾਈਆਂ!

### ਤੁਸੀਂ ਇਹ ਟਿਊਟੋਰਿਅਲ ਪੂਰਾ ਕਰ ਲਿਆ ਹੈ

ਤੁਸੀਂ Microsoft Foundry ਵਿੱਚ Prompt flow ਨਾਲ ਸੰਮਿਲਿਤ fine-tuned Phi-3 ਮਾਡਲ ਦਾ ਸਫਲਤਾਪੂਰਵਕ ਮੁਲਾਂਕਣ ਕੀਤਾ ਹੈ। ਇਹ ਇਹ ਯਕੀਨੀ ਬਣਾਉਣ ਵਿੱਚ ਇਕ ਅਹੰਕਾਰਪੂਰਕ ਕਦਮ ਹੈ ਕਿ ਤੁਹਾਡੇ ਏਆਈ ਮਾਡਲ ਕੇਵਲ ਚੰਗਾ ਪ੍ਰਦਰਸ਼ਨ ਨਹੀਂ ਕਰਦੇ, ਸਗੋਂ Microsoft ਦੇ ਜ਼ਿੰਮੇਵਾਰ ਏਆਈ ਸਿਧਾਂਤਾਂ ਦੀ ਪਾਲਣਾ ਕਰਦੇ ਹਨ, ਤਾਂ ਜੋ ਤੁਸੀਂ ਭਰੋਸੇਯੋਗ ਅਤੇ ਵਿਸ਼ਵਾਸਪੱਤਰ ਏਆਈ ਐਪਲੀਕੇਸ਼ਨਾਂ ਤਿਆਰ ਕਰ ਸਕੋ।

![Architecture.](../../../../../../translated_images/pa/architecture.10bec55250f5d6a4.webp)

## Azure ਸਰੋਤਾਂ ਨੂੰ ਸਾਫ਼ ਕਰੋ

ਆਪਣੇ Azure ਸਰੋਤਾਂ ਨੂੰ ਸਾਫ਼ ਕਰੋ ਤਾਂ ਜੋ ਤੁਹਾਡੇ ਖਾਤੇ 'ਤੇ ਵਾਧੂ ਖਰਚਾ ਨਾ ਆਵੇ। Azure ਪੋਰਟਲ 'ਤੇ ਜਾਓ ਅਤੇ ਹੇਠ ਲਿਖੇ ਸਰੋਤ ਮਿਟਾਓ:

- Azure Machine learning ਸਰੋਤ।
- Azure Machine learning ਮਾਡਲ ਏਂਡਪਾਇੰਟ।
- Microsoft Foundry ਪਰੋਜੈਕਟ ਸਰੋਤ।
- Microsoft Foundry Prompt flow ਸਰੋਤ।

### ਅਗਲੇ ਕਦਮ

#### ਦਸਤਾਵੇਜ਼ੀਕਰਨ

- [Responsible AI ਡੈਸ਼ਬੋਰਡ ਦੀ ਵਰਤੋਂ ਕਰਕੇ AI ਸਿਸਟਮਾਂ ਦਾ ਮੁਲਾਂਕਣ ਕਰੋ](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [ਜਨਰੇਟਿਵ ਏਆਈ ਲਈ ਮੁਲਾਂਕਣ ਅਤੇ ਨਿਗਰਾਨੀ ਮੈਟਰਿਕਸ](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Microsoft Foundry ਦਸਤਾਵੇਜ਼ੀਕਰਨ](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Prompt flow ਦਸਤਾਵੇਜ਼ੀਕਰਨ](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### ਟ੍ਰੇਨਿੰਗ ਸਮੱਗਰੀ

- [Microsoft ਦੇ ਜ਼ਿੰਮੇਵਾਰ ਏਆਈ ਅਭਿਗਮ ਦਾ ਪਰਿਚਯ](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Microsoft Foundry ਦਾ ਪਰਿਚਯ](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### ਰੈਫਰੰਸ

- [ਜ਼ਿੰਮੇਵਾਰ ਏਆਈ ਕੀ ਹੈ?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [ਉਹਨੋਂ ਲਈ ਨਵੇਂ ਸੰਦ ਅਲਾਨ ਕਰਨਿਆਂ ਜੋ ਤੁਹਾਡੀ ਸੁਰੱਖਿਆ ਅਤੇ ਭਰੋਸੇਯੋਗ ਜਨਰੇਟਿਵ ਏਆਈ ਐਪਲੀਕੇਸ਼ਨ ਬਣਾਉਂਦੇ ਹਨ](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [ਜਨਰੇਟਿਵ ਏਆਈ ਐਪਲੀਕੇਸ਼ਨਾਂ ਦਾ ਮੁਲਾਂਕਣ](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਵੀਕਾਰ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸੁੱਚੜਤਾ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਧਿਆਨ ਵਿੱਚ ਰੱਖੋ ਕਿ ਸੁਚਾਲਿਤ ਅਨੁਵਾਦ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਟੀਕਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਹੀ ਅਧਿਕਾਰਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਵਪਾਰਕ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਉਪਜ ਰਹੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਮੀਆਂ ਜਾਂ ਭ੍ਰਮਾਂ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->