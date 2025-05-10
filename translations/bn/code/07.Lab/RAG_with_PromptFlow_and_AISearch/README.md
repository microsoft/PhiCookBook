<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8ec74e4a49934dad78bc52dcb898359c",
  "translation_date": "2025-05-09T05:11:12+00:00",
  "source_file": "code/07.Lab/RAG_with_PromptFlow_and_AISearch/README.md",
  "language_code": "bn"
}
-->
## RAG with PromptFlow and AISearch

এই উদাহরণে, আমরা Phi3 কে SLM হিসেবে, AI Search কে vectorDB হিসেবে এবং Prompt Flow কে low-code orchestrator হিসেবে ব্যবহার করে একটি Retrieval Augmented Generation (RAG) অ্যাপ্লিকেশন তৈরি করব।

## বৈশিষ্ট্যসমূহ

- Docker ব্যবহার করে সহজ ডিপ্লয়মেন্ট।
- AI ওয়ার্কফ্লো পরিচালনার জন্য স্কেলেবল আর্কিটেকচার।
- Prompt Flow ব্যবহার করে কম কোডের পদ্ধতি।

## প্রয়োজনীয়তা

শুরু করার আগে, নিশ্চিত করুন যে আপনি নিম্নলিখিত শর্তগুলো পূরণ করেছেন:

- আপনার লোকাল মেশিনে Docker ইনস্টল করা আছে।
- Azure অ্যাকাউন্ট যার মাধ্যমে কন্টেইনার রিসোর্স তৈরি ও পরিচালনার অনুমতি রয়েছে।
- Azure AI Studio এবং Azure AI Search ইনস্ট্যান্স।
- আপনার ইনডেক্স তৈরি করার জন্য একটি embedding মডেল (এটি হতে পারে Azure OpenAI embedding অথবা ক্যাটালগ থেকে একটি OS মডেল)।
- আপনার লোকাল মেশিনে Python 3.8 বা তার পরবর্তী ভার্সন ইনস্টল করা আছে।
- একটি Azure Container Registry (অথবা আপনার পছন্দের অন্য কোনো রেজিস্ট্রি)।

## ইনস্টলেশন

1. আপনার Azure AI Studio প্রজেক্টে flow.yaml ফাইল ব্যবহার করে একটি নতুন ফ্লো তৈরি করুন।
2. Azure AI মডেল ক্যাটালগ থেকে একটি Phi3 মডেল ডিপ্লয় করুন এবং আপনার প্রজেক্টের সাথে সংযোগ তৈরি করুন। [Deploy Phi-3 as a Model as a Service](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. Azure AI Search এ আপনার পছন্দের কোনো ডকুমেন্ট ব্যবহার করে ভেক্টর ইনডেক্স তৈরি করুন। [Create a vector index on Azure AI Search](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. ম্যানেজড এন্ডপয়েন্টে ফ্লো ডিপ্লয় করুন এবং prompt-flow-frontend.py ফাইলে এটি ব্যবহার করুন। [Deploy a flow on an online endpoint](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. রিপোজিটরি ক্লোন করুন:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. Docker ইমেজ তৈরি করুন:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. Docker ইমেজ Azure Container Registry তে পুশ করুন:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## ব্যবহার

1. Docker কন্টেইনার চালান:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. ব্রাউজারে `http://localhost:8501` এ অ্যাপ্লিকেশন অ্যাক্সেস করুন।

## যোগাযোগ

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

সম্পূর্ণ আর্টিকেল: [RAG with Phi-3-Medium as a Model as a Service from Azure Model Catalog](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**অস্বীকারোক্তি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথি তার নিজস্ব ভাষায়ই সর্বোত্তম এবং কর্তৃপক্ষের উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ গ্রহণ করার পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহার থেকে উদ্ভূত কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়বদ্ধ নই।