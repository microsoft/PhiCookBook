<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f61c383bbf0c3dac97e43f833c258731",
  "translation_date": "2025-07-17T02:34:12+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md",
  "language_code": "ms"
}
-->
# MLflow

[MLflow](https://mlflow.org/) adalah platform sumber terbuka yang direka untuk menguruskan kitar hayat pembelajaran mesin dari awal hingga akhir.

![MLFlow](../../../../../../translated_images/MlFlowmlops.ed16f47809d74d9ac0407bf43985ec022ad01f3d970083e465326951e43b2e01.ms.png)

MLFlow digunakan untuk menguruskan kitar hayat ML, termasuk eksperimen, kebolehulangan, penyebaran dan pendaftaran model pusat. ML flow kini menawarkan empat komponen.

- **MLflow Tracking:** Merekod dan menyemak eksperimen, kod, konfigurasi data dan keputusan.
- **MLflow Projects:** Membungkus kod sains data dalam format yang membolehkan pengulangan larian pada mana-mana platform.
- **Mlflow Models:** Menyebarkan model pembelajaran mesin dalam pelbagai persekitaran perkhidmatan.
- **Model Registry:** Menyimpan, memberi anotasi dan mengurus model dalam repositori pusat.

Ia merangkumi keupayaan untuk menjejak eksperimen, membungkus kod ke dalam larian yang boleh diulang, serta berkongsi dan menyebarkan model. MLFlow diintegrasikan ke dalam Databricks dan menyokong pelbagai perpustakaan ML, menjadikannya bebas perpustakaan. Ia boleh digunakan dengan mana-mana perpustakaan pembelajaran mesin dan dalam mana-mana bahasa pengaturcaraan, kerana ia menyediakan REST API dan CLI untuk kemudahan.

![MLFlow](../../../../../../translated_images/MLflow2.5a22eb718f6311d16f1a1952a047dc6b9e392649f1e0fc7bc3c3dcd65e3af07c.ms.png)

Ciri utama MLFlow termasuk:

- **Penjejakan Eksperimen:** Merekod dan membandingkan parameter dan keputusan.
- **Pengurusan Model:** Menyebarkan model ke pelbagai platform perkhidmatan dan inferens.
- **Model Registry:** Mengurus secara kolaboratif kitar hayat Model MLflow, termasuk versi dan anotasi.
- **Projects:** Membungkus kod ML untuk dikongsi atau digunakan dalam produksi.

MLFlow juga menyokong gelung MLOps, yang merangkumi penyediaan data, pendaftaran dan pengurusan model, pembungkusan model untuk pelaksanaan, penyebaran perkhidmatan, dan pemantauan model. Ia bertujuan untuk memudahkan proses peralihan dari prototaip ke aliran kerja produksi, terutamanya dalam persekitaran awan dan edge.

## Senario E2E - Membina pembalut dan menggunakan Phi-3 sebagai model MLFlow

Dalam contoh E2E ini, kami akan menunjukkan dua pendekatan berbeza untuk membina pembalut di sekitar model bahasa kecil Phi-3 (SLM) dan kemudian menjalankannya sebagai model MLFlow sama ada secara tempatan atau di awan, contohnya, dalam ruang kerja Azure Machine Learning.

![MLFlow](../../../../../../translated_images/MlFlow1.fd745e47dbd3fecfee254096d496cdf1cb3e1789184f9efcead9c2a96e5a979b.ms.png)

| Projek | Penerangan | Lokasi |
| ------------ | ----------- | -------- |
| Transformer Pipeline | Transformer Pipeline adalah pilihan paling mudah untuk membina pembalut jika anda ingin menggunakan model HuggingFace dengan rasa transformer eksperimen MLFlow. | [**TransformerPipeline.ipynb**](../../../../../../code/06.E2E/E2E_Phi-3-MLflow_TransformerPipeline.ipynb) |
| Custom Python Wrapper | Pada masa penulisan, pipeline transformer tidak menyokong penjanaan pembalut MLFlow untuk model HuggingFace dalam format ONNX, walaupun dengan pakej Python optimum eksperimen. Untuk kes seperti ini, anda boleh membina pembalut Python tersuai untuk mod MLFlow | [**CustomPythonWrapper.ipynb**](../../../../../../code/06.E2E/E2E_Phi-3-MLflow_CustomPythonWrapper.ipynb) |

## Projek: Transformer Pipeline

1. Anda memerlukan pakej Python yang berkaitan dari MLFlow dan HuggingFace:

    ``` Python
    import mlflow
    import transformers
    ```

2. Seterusnya, anda harus memulakan pipeline transformer dengan merujuk kepada model Phi-3 sasaran dalam daftar HuggingFace. Seperti yang dapat dilihat dari kad model _Phi-3-mini-4k-instruct_, tugasan model ini adalah jenis “Penjanaan Teks”:

    ``` Python
    pipeline = transformers.pipeline(
        task = "text-generation",
        model = "microsoft/Phi-3-mini-4k-instruct"
    )
    ```

3. Anda kini boleh menyimpan pipeline transformer model Phi-3 anda dalam format MLFlow dan memberikan butiran tambahan seperti laluan artifak sasaran, tetapan konfigurasi model tertentu dan jenis API inferens:

    ``` Python
    model_info = mlflow.transformers.log_model(
        transformers_model = pipeline,
        artifact_path = "phi3-mlflow-model",
        model_config = model_config,
        task = "llm/v1/chat"
    )
    ```

## Projek: Custom Python Wrapper

1. Di sini kita boleh menggunakan [ONNX Runtime generate() API](https://github.com/microsoft/onnxruntime-genai) Microsoft untuk inferens model ONNX dan pengekodan / penyahkodan token. Anda perlu memilih pakej _onnxruntime_genai_ untuk pengiraan sasaran anda, dengan contoh di bawah mensasarkan CPU:

    ``` Python
    import mlflow
    from mlflow.models import infer_signature
    import onnxruntime_genai as og
    ```

1. Kelas tersuai kami melaksanakan dua kaedah: _load_context()_ untuk memulakan **model ONNX** Phi-3 Mini 4K Instruct, **parameter penjana** dan **tokenizer**; dan _predict()_ untuk menjana token output bagi prompt yang diberikan:

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

1. Anda kini boleh menggunakan fungsi _mlflow.pyfunc.log_model()_ untuk menjana pembalut Python tersuai (dalam format pickle) untuk model Phi-3, bersama model ONNX asal dan kebergantungan yang diperlukan:

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

## Tandatangan model MLFlow yang dijana

1. Dalam langkah 3 projek Transformer Pipeline di atas, kami menetapkan tugasan model MLFlow kepada “_llm/v1/chat_”. Arahan sedemikian menjana pembalut API model, serasi dengan OpenAI Chat API seperti yang ditunjukkan di bawah:

    ``` Python
    {inputs: 
      ['messages': Array({content: string (required), name: string (optional), role: string (required)}) (required), 'temperature': double (optional), 'max_tokens': long (optional), 'stop': Array(string) (optional), 'n': long (optional), 'stream': boolean (optional)],
    outputs: 
      ['id': string (required), 'object': string (required), 'created': long (required), 'model': string (required), 'choices': Array({finish_reason: string (required), index: long (required), message: {content: string (required), name: string (optional), role: string (required)} (required)}) (required), 'usage': {completion_tokens: long (required), prompt_tokens: long (required), total_tokens: long (required)} (required)],
    params: 
      None}
    ```

1. Akibatnya, anda boleh menghantar prompt anda dalam format berikut:

    ``` Python
    messages = [{"role": "user", "content": "What is the capital of Spain?"}]
    ```

1. Kemudian, gunakan pemprosesan pasca yang serasi dengan OpenAI API, contohnya _response[0][‘choices’][0][‘message’][‘content’]_, untuk memperindah output anda menjadi seperti ini:

    ``` JSON
    Question: What is the capital of Spain?
    
    Answer: The capital of Spain is Madrid. It is the largest city in Spain and serves as the political, economic, and cultural center of the country. Madrid is located in the center of the Iberian Peninsula and is known for its rich history, art, and architecture, including the Royal Palace, the Prado Museum, and the Plaza Mayor.
    
    Usage: {'prompt_tokens': 11, 'completion_tokens': 73, 'total_tokens': 84}
    ```

1. Dalam langkah 3 projek Custom Python Wrapper di atas, kami membenarkan pakej MLFlow menjana tandatangan model daripada contoh input yang diberikan. Tandatangan pembalut MLFlow kami akan kelihatan seperti ini:

    ``` Python
    {inputs: 
      ['prompt': string (required)],
    outputs: 
      [string (required)],
    params: 
      None}
    ```

1. Jadi, prompt kami perlu mengandungi kunci kamus "prompt", serupa dengan ini:

    ``` Python
    {"prompt": "<|system|>You are a stand-up comedian.<|end|><|user|>Tell me a joke about atom<|end|><|assistant|>",}
    ```

1. Output model akan diberikan dalam format rentetan:

    ``` JSON
    Alright, here's a little atom-related joke for you!
    
    Why don't electrons ever play hide and seek with protons?
    
    Because good luck finding them when they're always "sharing" their electrons!
    
    Remember, this is all in good fun, and we're just having a little atomic-level humor!
    ```

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.