<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bcf5dd7031db0031abdb9dd0c05ba118",
  "translation_date": "2025-07-16T20:55:37+00:00",
  "source_file": "md/01.Introduction/03/Local_Server_Inference.md",
  "language_code": "mo"
}
-->
# **在本地伺服器上推論 Phi-3**

我們可以將 Phi-3 部署在本地伺服器上。使用者可以選擇 [Ollama](https://ollama.com) 或 [LM Studio](https://llamaedge.com) 解決方案，或者自行撰寫程式碼。你可以透過 [Semantic Kernel](https://github.com/microsoft/semantic-kernel?WT.mc_id=aiml-138114-kinfeylo) 或 [Langchain](https://www.langchain.com/) 連接 Phi-3 的本地服務，來構建 Copilot 應用程式。

## **使用 Semantic Kernel 存取 Phi-3-mini**

在 Copilot 應用程式中，我們透過 Semantic Kernel / LangChain 建立應用程式。這類應用框架通常相容於 Azure OpenAI Service / OpenAI 模型，也能支援 Hugging Face 上的開源模型及本地模型。如果想用 Semantic Kernel 存取 Phi-3-mini 該怎麼做？以 .NET 為例，我們可以將它與 Semantic Kernel 中的 Hugging Face Connector 結合。預設情況下，它會對應 Hugging Face 上的模型 ID（首次使用時，模型會從 Hugging Face 下載，耗時較長）。你也可以連接到已建置的本地服務。兩者相比，我們建議使用後者，因為它擁有更高的自主性，尤其適合企業應用。

![sk](../../../../../translated_images/mo/sk.d03785c25edc6d44.png)

從圖中可見，透過 Semantic Kernel 存取本地服務能輕鬆連接自建的 Phi-3-mini 模型伺服器。以下是執行結果

![skrun](../../../../../translated_images/mo/skrun.5aafc1e7197dca20.png)

***範例程式碼*** https://github.com/kinfey/Phi3MiniSamples/tree/main/semantickernel

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋負責。