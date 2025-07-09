<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8ec74e4a49934dad78bc52dcb898359c",
  "translation_date": "2025-07-09T20:13:19+00:00",
  "source_file": "code/07.Lab/RAG_with_PromptFlow_and_AISearch/README.md",
  "language_code": "my"
}
-->
## RAG နှင့် PromptFlow နှင့် AISearch

ဤဥပမာတွင် Phi3 ကို SLM အဖြစ်၊ AI Search ကို vectorDB အဖြစ်နှင့် Prompt Flow ကို low-code orchestrator အဖြစ် အသုံးပြု၍ Retrieval Augmented Generation (RAG) အက်ပလီကေးရှင်းတစ်ခုကို တည်ဆောက်မည်ဖြစ်သည်။

## လက္ခဏာများ

- Docker အသုံးပြု၍ လွယ်ကူစွာ တပ်ဆင်နိုင်ခြင်း။
- AI workflow များကို ကိုင်တွယ်နိုင်သော တိုးချဲ့နိုင်သော ဖွဲ့စည်းပုံ။
- Prompt Flow ကို အသုံးပြုသည့် low code နည်းလမ်း။

## မတိုင်မီ လိုအပ်ချက်များ

စတင်မလုပ်မီ အောက်ပါလိုအပ်ချက်များကို ဖြည့်ဆည်းထားကြောင်း သေချာပါစေ-

- သင့်ဒေသတွင် Docker တပ်ဆင်ထားရှိခြင်း။
- container resource များ ဖန်တီးခြင်းနှင့် စီမံခန့်ခွဲခြင်းအတွက် ခွင့်ပြုချက်ရှိသော Azure အကောင့်။
- Azure AI Studio နှင့် Azure AI Search အကောင့်များ။
- သင့် index ဖန်တီးရန် embedding model တစ်ခု (Azure OpenAI embedding သို့မဟုတ် catalog မှ OS model တစ်ခုဖြစ်နိုင်သည်)။
- သင့်ဒေသတွင် Python 3.8 သို့မဟုတ် နောက်ဆုံးထွက် ဗားရှင်းတပ်ဆင်ထားခြင်း။
- Azure Container Registry (သို့မဟုတ် သင့်ရွေးချယ်သည့် registry တစ်ခု)။

## တပ်ဆင်ခြင်း

1. flow.yaml ဖိုင်ကို အသုံးပြု၍ သင့် Azure AI Studio Project တွင် flow အသစ်တစ်ခု ဖန်တီးပါ။
2. Azure AI model catalog မှ Phi3 Model တစ်ခု တပ်ဆင်ပြီး သင့် project နှင့် ချိတ်ဆက်ပါ။ [Deploy Phi-3 as a Model as a Service](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. သင့်ရွေးချယ်သည့် စာရွက်စာတမ်းတစ်ခုကို အသုံးပြု၍ Azure AI Search တွင် vector index တစ်ခု ဖန်တီးပါ။ [Create a vector index on Azure AI Search](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. managed endpoint တစ်ခုတွင် flow ကို တပ်ဆင်ပြီး prompt-flow-frontend.py ဖိုင်တွင် အသုံးပြုပါ။ [Deploy a flow on an online endpoint](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. repository ကို clone လုပ်ပါ-

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. Docker image ကို တည်ဆောက်ပါ-

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. Docker image ကို Azure Container Registry သို့ တင်ပါ-

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## အသုံးပြုနည်း

1. Docker container ကို run ပါ-

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. သင့် browser တွင် `http://localhost:8501` မှာ အက်ပလီကေးရှင်းကို ဝင်ကြည့်နိုင်ပါသည်။

## ဆက်သွယ်ရန်

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

အပြည့်အစုံ ဆောင်းပါး- [RAG with Phi-3-Medium as a Model as a Service from Azure Model Catalog](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**အကြောင်းကြားချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်ခြင်းသည် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် မေတ္တာရပ်ခံအပ်ပါသည်။ မူရင်းစာတမ်းကို မိမိဘာသာစကားဖြင့်သာ တရားဝင်အချက်အလက်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်မှ ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုရာမှ ဖြစ်ပေါ်လာနိုင်သည့် နားလည်မှုမှားယွင်းမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။