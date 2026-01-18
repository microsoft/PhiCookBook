<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f61c383bbf0c3dac97e43f833c258731",
  "translation_date": "2025-07-17T02:35:35+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md",
  "language_code": "sk"
}
-->
# MLflow

[MLflow](https://mlflow.org/) je open-source platforma navrhnutá na správu celého životného cyklu strojového učenia.

![MLFlow](../../../../../../translated_images/sk/MlFlowmlops.ed16f47809d74d9a.webp)

MLFlow sa používa na správu životného cyklu ML, vrátane experimentovania, reprodukovateľnosti, nasadenia a centrálneho registra modelov. MLflow momentálne ponúka štyri komponenty.

- **MLflow Tracking:** Zaznamenávanie a dotazovanie experimentov, kódu, konfigurácie dát a výsledkov.
- **MLflow Projects:** Zabalenie dátovej vedy do formátu, ktorý umožňuje reprodukciu spustení na akejkoľvek platforme.
- **Mlflow Models:** Nasadenie modelov strojového učenia v rôznych prostrediach pre servovanie.
- **Model Registry:** Ukladanie, anotovanie a správa modelov v centrálnej databáze.

Obsahuje funkcie na sledovanie experimentov, balenie kódu do reprodukovateľných spustení a zdieľanie a nasadzovanie modelov. MLFlow je integrovaný v Databricks a podporuje rôzne ML knižnice, čím je nezávislý na konkrétnej knižnici. Môže byť použitý s akoukoľvek knižnicou strojového učenia a v ľubovoľnom programovacom jazyku, keďže poskytuje REST API a CLI pre pohodlné použitie.

![MLFlow](../../../../../../translated_images/sk/MLflow2.5a22eb718f6311d1.webp)

Hlavné vlastnosti MLFlow zahŕňajú:

- **Sledovanie experimentov:** Zaznamenávanie a porovnávanie parametrov a výsledkov.
- **Správa modelov:** Nasadenie modelov na rôzne platformy pre servovanie a inferenciu.
- **Model Registry:** Spolupráca na správe životného cyklu MLflow modelov, vrátane verzovania a anotácií.
- **Projects:** Zabalenie ML kódu na zdieľanie alebo produkčné použitie.

MLFlow tiež podporuje MLOps cyklus, ktorý zahŕňa prípravu dát, registráciu a správu modelov, balenie modelov na spustenie, nasadenie služieb a monitorovanie modelov. Cieľom je zjednodušiť prechod od prototypu k produkčnému workflow, najmä v cloudových a edge prostrediach.

## E2E scenár – Vytvorenie wrappera a použitie Phi-3 ako MLFlow modelu

V tomto E2E príklade ukážeme dva rôzne prístupy na vytvorenie wrappera okolo malého jazykového modelu Phi-3 (SLM) a následné spustenie ako MLFlow modelu buď lokálne, alebo v cloude, napríklad v Azure Machine Learning workspace.

![MLFlow](../../../../../../translated_images/sk/MlFlow1.fd745e47dbd3fecf.webp)

| Projekt | Popis | Umiestnenie |
| ------------ | ----------- | -------- |
| Transformer Pipeline | Transformer Pipeline je najjednoduchšia možnosť, ako vytvoriť wrapper, ak chcete použiť HuggingFace model s experimentálnou podporou transformerov v MLFlow. | [**TransformerPipeline.ipynb**](../../../../../../code/06.E2E/E2E_Phi-3-MLflow_TransformerPipeline.ipynb) |
| Custom Python Wrapper | V čase písania transformer pipeline nepodporovala generovanie MLFlow wrappera pre HuggingFace modely v ONNX formáte, ani s experimentálnym balíkom optimum Python. V takýchto prípadoch môžete vytvoriť vlastný Python wrapper pre MLFlow model. | [**CustomPythonWrapper.ipynb**](../../../../../../code/06.E2E/E2E_Phi-3-MLflow_CustomPythonWrapper.ipynb) |

## Projekt: Transformer Pipeline

1. Budete potrebovať príslušné Python balíky z MLFlow a HuggingFace:

    ``` Python
    import mlflow
    import transformers
    ```

2. Ďalej by ste mali inicializovať transformer pipeline odkazom na cieľový Phi-3 model v HuggingFace registri. Ako je vidieť z modelovej karty _Phi-3-mini-4k-instruct_, jeho úlohou je „Text Generation“:

    ``` Python
    pipeline = transformers.pipeline(
        task = "text-generation",
        model = "microsoft/Phi-3-mini-4k-instruct"
    )
    ```

3. Teraz môžete uložiť transformer pipeline Phi-3 modelu do MLFlow formátu a poskytnúť ďalšie detaily, ako cieľovú cestu pre artefakty, špecifické nastavenia modelu a typ inference API:

    ``` Python
    model_info = mlflow.transformers.log_model(
        transformers_model = pipeline,
        artifact_path = "phi3-mlflow-model",
        model_config = model_config,
        task = "llm/v1/chat"
    )
    ```

## Projekt: Custom Python Wrapper

1. Môžeme tu využiť Microsoftov [ONNX Runtime generate() API](https://github.com/microsoft/onnxruntime-genai) pre inferenciu ONNX modelu a kódovanie/dekódovanie tokenov. Pre cieľový výpočtový zdroj si vyberiete balík _onnxruntime_genai_, v tomto príklade je cieľom CPU:

    ``` Python
    import mlflow
    from mlflow.models import infer_signature
    import onnxruntime_genai as og
    ```

1. Naša vlastná trieda implementuje dve metódy: _load_context()_ na inicializáciu **ONNX modelu** Phi-3 Mini 4K Instruct, **parametrov generátora** a **tokenizéra**; a _predict()_ na generovanie výstupných tokenov pre zadaný prompt:

    ``` Python
    class Phi3Model(mlflow.pyfunc.PythonModel):
        def load_context(self, context):
            # Retrieving model from the artifacts
            model_path = context.artifacts["phi3-mini-onnx"]
            model_options = {
                 "max_length": 300,
                 "temperature": 0.2,         
            }
        
            # Defining the model
            self.phi3_model = og.Model(model_path)
            self.params = og.GeneratorParams(self.phi3_model)
            self.params.set_search_options(**model_options)
            
            # Defining the tokenizer
            self.tokenizer = og.Tokenizer(self.phi3_model)
    
        def predict(self, context, model_input):
            # Retrieving prompt from the input
            prompt = model_input["prompt"][0]
            self.params.input_ids = self.tokenizer.encode(prompt)
    
            # Generating the model's response
            response = self.phi3_model.generate(self.params)
    
            return self.tokenizer.decode(response[0][len(self.params.input_ids):])
    ```

1. Teraz môžete použiť funkciu _mlflow.pyfunc.log_model()_ na vytvorenie vlastného Python wrappera (vo formáte pickle) pre Phi-3 model spolu s originálnym ONNX modelom a potrebnými závislosťami:

    ``` Python
    model_info = mlflow.pyfunc.log_model(
        artifact_path = artifact_path,
        python_model = Phi3Model(),
        artifacts = {
            "phi3-mini-onnx": "cpu_and_mobile/cpu-int4-rtn-block-32-acc-level-4",
        },
        input_example = input_example,
        signature = infer_signature(input_example, ["Run"]),
        extra_pip_requirements = ["torch", "onnxruntime_genai", "numpy"],
    )
    ```

## Signatúry generovaných MLFlow modelov

1. V kroku 3 projektu Transformer Pipeline sme nastavili úlohu MLFlow modelu na „_llm/v1/chat_“. Takýto parameter generuje API wrapper modelu, kompatibilný s OpenAI Chat API, ako je uvedené nižšie:

    ``` Python
    {inputs: 
      ['messages': Array({content: string (required), name: string (optional), role: string (required)}) (required), 'temperature': double (optional), 'max_tokens': long (optional), 'stop': Array(string) (optional), 'n': long (optional), 'stream': boolean (optional)],
    outputs: 
      ['id': string (required), 'object': string (required), 'created': long (required), 'model': string (required), 'choices': Array({finish_reason: string (required), index: long (required), message: {content: string (required), name: string (optional), role: string (required)} (required)}) (required), 'usage': {completion_tokens: long (required), prompt_tokens: long (required), total_tokens: long (required)} (required)],
    params: 
      None}
    ```

1. Výsledkom je, že môžete odoslať prompt v nasledujúcom formáte:

    ``` Python
    messages = [{"role": "user", "content": "What is the capital of Spain?"}]
    ```

1. Potom použite post-processing kompatibilný s OpenAI API, napríklad _response[0][‘choices’][0][‘message’][‘content’]_, na úpravu výstupu do takejto podoby:

    ``` JSON
    Question: What is the capital of Spain?
    
    Answer: The capital of Spain is Madrid. It is the largest city in Spain and serves as the political, economic, and cultural center of the country. Madrid is located in the center of the Iberian Peninsula and is known for its rich history, art, and architecture, including the Royal Palace, the Prado Museum, and the Plaza Mayor.
    
    Usage: {'prompt_tokens': 11, 'completion_tokens': 73, 'total_tokens': 84}
    ```

1. V kroku 3 projektu Custom Python Wrapper umožňujeme MLFlow balíku vygenerovať signatúru modelu z daného príkladu vstupu. Signatúra nášho MLFlow wrappera bude vyzerať takto:

    ``` Python
    {inputs: 
      ['prompt': string (required)],
    outputs: 
      [string (required)],
    params: 
      None}
    ```

1. Takže náš prompt by mal obsahovať kľúč "prompt" v slovníku, podobne ako toto:

    ``` Python
    {"prompt": "<|system|>You are a stand-up comedian.<|end|><|user|>Tell me a joke about atom<|end|><|assistant|>",}
    ```

1. Výstup modelu bude potom poskytnutý vo formáte reťazca:

    ``` JSON
    Alright, here's a little atom-related joke for you!
    
    Why don't electrons ever play hide and seek with protons?
    
    Because good luck finding them when they're always "sharing" their electrons!
    
    Remember, this is all in good fun, and we're just having a little atomic-level humor!
    ```

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.