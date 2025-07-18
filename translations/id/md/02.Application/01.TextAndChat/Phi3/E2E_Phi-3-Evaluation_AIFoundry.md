<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "80a853c08e4ee25ef9b4bfcedd8990da",
  "translation_date": "2025-07-16T23:47:37+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md",
  "language_code": "id"
}
-->
# Evaluasi Model Fine-tuned Phi-3 / Phi-3.5 di Azure AI Foundry dengan Fokus pada Prinsip Responsible AI Microsoft

Contoh end-to-end (E2E) ini didasarkan pada panduan "[Evaluate Fine-tuned Phi-3 / 3.5 Models in Azure AI Foundry Focusing on Microsoft's Responsible AI](https://techcommunity.microsoft.com/blog/educatordeveloperblog/evaluate-fine-tuned-phi-3--3-5-models-in-azure-ai-studio-focusing-on-microsofts-/4227850?WT.mc_id=aiml-137032-kinfeylo)" dari Microsoft Tech Community.

## Ikhtisar

### Bagaimana cara mengevaluasi keamanan dan kinerja model fine-tuned Phi-3 / Phi-3.5 di Azure AI Foundry?

Fine-tuning model terkadang dapat menghasilkan respons yang tidak diinginkan atau tidak disengaja. Untuk memastikan model tetap aman dan efektif, penting untuk mengevaluasi potensi model dalam menghasilkan konten berbahaya serta kemampuannya menghasilkan respons yang akurat, relevan, dan koheren. Dalam tutorial ini, Anda akan belajar cara mengevaluasi keamanan dan kinerja model fine-tuned Phi-3 / Phi-3.5 yang terintegrasi dengan Prompt flow di Azure AI Foundry.

Berikut adalah proses evaluasi Azure AI Foundry.

![Arsitektur tutorial.](../../../../../../translated_images/architecture.10bec55250f5d6a4e1438bb31c5c70309908e21e7ada24a621bbfdd8d0f834f4.id.png)

*Sumber Gambar: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> Untuk informasi lebih rinci dan sumber daya tambahan tentang Phi-3 / Phi-3.5, silakan kunjungi [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723).

### Prasyarat

- [Python](https://www.python.org/downloads)
- [Langganan Azure](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- Model Phi-3 / Phi-3.5 yang sudah di-fine-tune

### Daftar Isi

1. [**Skenario 1: Pengenalan evaluasi Prompt flow di Azure AI Foundry**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Pengenalan evaluasi keamanan](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Pengenalan evaluasi kinerja](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [**Skenario 2: Mengevaluasi model Phi-3 / Phi-3.5 di Azure AI Foundry**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Sebelum memulai](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Mendeploy Azure OpenAI untuk mengevaluasi model Phi-3 / Phi-3.5](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Evaluasi model fine-tuned Phi-3 / Phi-3.5 menggunakan evaluasi Prompt flow Azure AI Foundry](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [Selamat!](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## **Skenario 1: Pengenalan evaluasi Prompt flow di Azure AI Foundry**

### Pengenalan evaluasi keamanan

Untuk memastikan model AI Anda etis dan aman, sangat penting untuk mengevaluasinya berdasarkan Prinsip Responsible AI Microsoft. Di Azure AI Foundry, evaluasi keamanan memungkinkan Anda menilai kerentanan model terhadap serangan jailbreak dan potensi model menghasilkan konten berbahaya, yang secara langsung sejalan dengan prinsip-prinsip tersebut.

![Evaluasi keamanan.](../../../../../../translated_images/safety-evaluation.083586ec88dfa9500d3d25faf0720fd99cbf07c8c4b559dda5e70c84a0e2c1aa.id.png)

*Sumber Gambar: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Prinsip Responsible AI Microsoft

Sebelum memulai langkah teknis, penting untuk memahami Prinsip Responsible AI Microsoft, sebuah kerangka etika yang dirancang untuk membimbing pengembangan, penerapan, dan pengoperasian sistem AI secara bertanggung jawab. Prinsip-prinsip ini mengarahkan desain, pengembangan, dan penerapan sistem AI secara bertanggung jawab, memastikan teknologi AI dibangun dengan cara yang adil, transparan, dan inklusif. Prinsip-prinsip ini menjadi dasar untuk mengevaluasi keamanan model AI.

Prinsip Responsible AI Microsoft meliputi:

- **Keadilan dan Inklusivitas**: Sistem AI harus memperlakukan semua orang secara adil dan menghindari perlakuan berbeda terhadap kelompok orang yang berada dalam situasi serupa. Misalnya, ketika sistem AI memberikan panduan tentang pengobatan medis, aplikasi pinjaman, atau pekerjaan, sistem harus memberikan rekomendasi yang sama kepada semua orang yang memiliki gejala, kondisi keuangan, atau kualifikasi profesional yang serupa.

- **Keandalan dan Keamanan**: Untuk membangun kepercayaan, sangat penting bahwa sistem AI beroperasi secara andal, aman, dan konsisten. Sistem ini harus mampu beroperasi sesuai desain awal, merespons dengan aman terhadap kondisi yang tidak terduga, dan tahan terhadap manipulasi berbahaya. Cara mereka berperilaku dan berbagai kondisi yang dapat mereka tangani mencerminkan berbagai situasi dan kondisi yang diperkirakan pengembang selama desain dan pengujian.

- **Transparansi**: Ketika sistem AI membantu mengambil keputusan yang berdampak besar pada kehidupan orang, sangat penting agar orang memahami bagaimana keputusan tersebut dibuat. Misalnya, sebuah bank mungkin menggunakan sistem AI untuk menentukan apakah seseorang layak mendapatkan kredit. Sebuah perusahaan mungkin menggunakan sistem AI untuk menentukan kandidat paling memenuhi syarat untuk dipekerjakan.

- **Privasi dan Keamanan**: Seiring AI semakin meluas, melindungi privasi dan mengamankan informasi pribadi serta bisnis menjadi semakin penting dan kompleks. Dengan AI, privasi dan keamanan data memerlukan perhatian khusus karena akses ke data sangat penting agar sistem AI dapat membuat prediksi dan keputusan yang akurat dan tepat tentang orang.

- **Akuntabilitas**: Orang yang merancang dan menerapkan sistem AI harus bertanggung jawab atas cara sistem mereka beroperasi. Organisasi harus mengacu pada standar industri untuk mengembangkan norma akuntabilitas. Norma ini dapat memastikan bahwa sistem AI bukan otoritas akhir dalam setiap keputusan yang memengaruhi kehidupan orang. Norma ini juga dapat memastikan manusia tetap memiliki kontrol bermakna atas sistem AI yang sangat otonom.

![Fill hub.](../../../../../../translated_images/responsibleai2.c07ef430113fad8c72329615ecf51a4e3df31043fb0d918f868525e7a9747b98.id.png)

*Sumber Gambar: [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> Untuk mempelajari lebih lanjut tentang Prinsip Responsible AI Microsoft, kunjungi [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723).

#### Metrik keamanan

Dalam tutorial ini, Anda akan mengevaluasi keamanan model fine-tuned Phi-3 menggunakan metrik keamanan Azure AI Foundry. Metrik ini membantu Anda menilai potensi model dalam menghasilkan konten berbahaya dan kerentanannya terhadap serangan jailbreak. Metrik keamanan meliputi:

- **Konten terkait Self-harm**: Mengevaluasi apakah model cenderung menghasilkan konten yang berhubungan dengan self-harm.
- **Konten Kebencian dan Tidak Adil**: Mengevaluasi apakah model cenderung menghasilkan konten yang penuh kebencian atau tidak adil.
- **Konten Kekerasan**: Mengevaluasi apakah model cenderung menghasilkan konten kekerasan.
- **Konten Seksual**: Mengevaluasi apakah model cenderung menghasilkan konten seksual yang tidak pantas.

Evaluasi aspek-aspek ini memastikan model AI tidak menghasilkan konten yang berbahaya atau menyinggung, sehingga sesuai dengan nilai sosial dan standar regulasi.

![Evaluasi berdasarkan keamanan.](../../../../../../translated_images/evaluate-based-on-safety.c5df819f5b0bfc07156d9b1e18bdf1f130120f7d23e05ea78bc9773d2500b665.id.png)

### Pengenalan evaluasi kinerja

Untuk memastikan model AI Anda berperforma sesuai harapan, penting untuk mengevaluasi kinerjanya berdasarkan metrik kinerja. Di Azure AI Foundry, evaluasi kinerja memungkinkan Anda menilai efektivitas model dalam menghasilkan respons yang akurat, relevan, dan koheren.

![Evaluasi keamanan.](../../../../../../translated_images/performance-evaluation.48b3e7e01a098740c7babf1904fa4acca46c5bd7ea8c826832989c776c0e01ca.id.png)

*Sumber Gambar: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Metrik kinerja

Dalam tutorial ini, Anda akan mengevaluasi kinerja model fine-tuned Phi-3 / Phi-3.5 menggunakan metrik kinerja Azure AI Foundry. Metrik ini membantu Anda menilai efektivitas model dalam menghasilkan respons yang akurat, relevan, dan koheren. Metrik kinerja meliputi:

- **Groundedness**: Mengevaluasi seberapa baik jawaban yang dihasilkan sesuai dengan informasi dari sumber input.
- **Relevansi**: Mengevaluasi keterkaitan respons yang dihasilkan dengan pertanyaan yang diberikan.
- **Koherensi**: Mengevaluasi kelancaran alur teks yang dihasilkan, apakah terbaca alami dan menyerupai bahasa manusia.
- **Kelancaran (Fluency)**: Mengevaluasi kemampuan bahasa dari teks yang dihasilkan.
- **Kesamaan GPT (GPT Similarity)**: Membandingkan respons yang dihasilkan dengan ground truth untuk kesamaan.
- **Skor F1**: Menghitung rasio kata yang sama antara respons yang dihasilkan dan data sumber.

Metrik-metrik ini membantu Anda mengevaluasi efektivitas model dalam menghasilkan respons yang akurat, relevan, dan koheren.

![Evaluasi berdasarkan kinerja.](../../../../../../translated_images/evaluate-based-on-performance.3e801c647c7554e820ceb3f7f148014fe0572c05dbdadb1af7205e1588fb0358.id.png)

## **Skenario 2: Mengevaluasi model Phi-3 / Phi-3.5 di Azure AI Foundry**

### Sebelum memulai

Tutorial ini merupakan kelanjutan dari posting blog sebelumnya, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" dan "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)." Dalam posting tersebut, kami membahas proses fine-tuning model Phi-3 / Phi-3.5 di Azure AI Foundry dan mengintegrasikannya dengan Prompt flow.

Dalam tutorial ini, Anda akan mendeploy model Azure OpenAI sebagai evaluator di Azure AI Foundry dan menggunakannya untuk mengevaluasi model fine-tuned Phi-3 / Phi-3.5 Anda.

Sebelum memulai tutorial ini, pastikan Anda memiliki prasyarat berikut, seperti yang dijelaskan dalam tutorial sebelumnya:

1. Dataset yang sudah disiapkan untuk mengevaluasi model fine-tuned Phi-3 / Phi-3.5.
1. Model Phi-3 / Phi-3.5 yang sudah di-fine-tune dan dideploy ke Azure Machine Learning.
1. Prompt flow yang terintegrasi dengan model fine-tuned Phi-3 / Phi-3.5 Anda di Azure AI Foundry.

> [!NOTE]
> Anda akan menggunakan file *test_data.jsonl*, yang terletak di folder data dari dataset **ULTRACHAT_200k** yang diunduh pada posting blog sebelumnya, sebagai dataset untuk mengevaluasi model fine-tuned Phi-3 / Phi-3.5.

#### Integrasi model kustom Phi-3 / Phi-3.5 dengan Prompt flow di Azure AI Foundry (Pendekatan kode terlebih dahulu)
> [!NOTE]  
> Jika Anda mengikuti pendekatan low-code yang dijelaskan dalam "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)", Anda bisa melewati latihan ini dan langsung ke latihan berikutnya.  
> Namun, jika Anda mengikuti pendekatan code-first yang dijelaskan dalam "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" untuk melakukan fine-tune dan menerapkan model Phi-3 / Phi-3.5 Anda, proses menghubungkan model Anda ke Prompt flow sedikit berbeda. Anda akan mempelajari proses ini dalam latihan ini.
Untuk melanjutkan, Anda perlu mengintegrasikan model Phi-3 / Phi-3.5 yang sudah disesuaikan ke dalam Prompt flow di Azure AI Foundry.

#### Buat Azure AI Foundry Hub

Anda perlu membuat Hub sebelum membuat Proyek. Hub berfungsi seperti Resource Group, memungkinkan Anda mengatur dan mengelola beberapa Proyek dalam Azure AI Foundry.

1. Masuk ke [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Pilih **All hubs** dari tab sisi kiri.

1. Pilih **+ New hub** dari menu navigasi.

    ![Create hub.](../../../../../../translated_images/create-hub.5be78fb1e21ffbf1aa9ecc232c2c95d337386f3cd0f361ca80c4475dc8aa2c7b.id.png)

1. Lakukan tugas berikut:

    - Masukkan **Hub name**. Harus berupa nilai yang unik.
    - Pilih **Subscription** Azure Anda.
    - Pilih **Resource group** yang akan digunakan (buat baru jika perlu).
    - Pilih **Location** yang ingin Anda gunakan.
    - Pilih **Connect Azure AI Services** yang akan digunakan (buat baru jika perlu).
    - Pilih **Connect Azure AI Search** ke **Skip connecting**.

    ![Fill hub.](../../../../../../translated_images/fill-hub.baaa108495c71e3449667210a8ec5a0f3206bf2724ebacaa69cb09d3b12f29d3.id.png)

1. Pilih **Next**.

#### Buat Proyek Azure AI Foundry

1. Di Hub yang Anda buat, pilih **All projects** dari tab sisi kiri.

1. Pilih **+ New project** dari menu navigasi.

    ![Select new project.](../../../../../../translated_images/select-new-project.cd31c0404088d7a32ee9018978b607dfb773956b15a88606f45579d3bc23c155.id.png)

1. Masukkan **Project name**. Harus berupa nilai yang unik.

    ![Create project.](../../../../../../translated_images/create-project.ca3b71298b90e42049ce8f6f452313bde644c309331fd728fcacd8954a20e26d.id.png)

1. Pilih **Create a project**.

#### Tambahkan koneksi kustom untuk model Phi-3 / Phi-3.5 yang sudah disesuaikan

Untuk mengintegrasikan model Phi-3 / Phi-3.5 kustom Anda dengan Prompt flow, Anda perlu menyimpan endpoint dan kunci model dalam koneksi kustom. Pengaturan ini memastikan akses ke model Phi-3 / Phi-3.5 kustom Anda di Prompt flow.

#### Atur api key dan endpoint uri dari model Phi-3 / Phi-3.5 yang sudah disesuaikan

1. Kunjungi [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Navigasikan ke workspace Azure Machine learning yang Anda buat.

1. Pilih **Endpoints** dari tab sisi kiri.

    ![Select endpoints.](../../../../../../translated_images/select-endpoints.ee7387ecd68bd18d35cd7f235f930ebe99841a8c8c9dea2f608b7f43508576dd.id.png)

1. Pilih endpoint yang Anda buat.

    ![Select endpoints.](../../../../../../translated_images/select-endpoint-created.9f63af5e4cf98b2ec92358f15ad36d69820e627c048f14c7ec3750fdbce3558b.id.png)

1. Pilih **Consume** dari menu navigasi.

1. Salin **REST endpoint** dan **Primary key** Anda.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/copy-endpoint-key.0650c3786bd646ab0b5a80833917b7b8f32ee011c09af0459f3830dc25b00760.id.png)

#### Tambahkan Koneksi Kustom

1. Kunjungi [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Navigasikan ke proyek Azure AI Foundry yang Anda buat.

1. Di Proyek yang Anda buat, pilih **Settings** dari tab sisi kiri.

1. Pilih **+ New connection**.

    ![Select new connection.](../../../../../../translated_images/select-new-connection.fa0f35743758a74b6c5dca5f37ca22939163f5c89eac47d1fd0a8c663bd5904a.id.png)

1. Pilih **Custom keys** dari menu navigasi.

    ![Select custom keys.](../../../../../../translated_images/select-custom-keys.5a3c6b25580a9b67df43e8c5519124268b987d8cb77d6e5fe5631f116714bd47.id.png)

1. Lakukan tugas berikut:

    - Pilih **+ Add key value pairs**.
    - Untuk nama kunci, masukkan **endpoint** dan tempel endpoint yang Anda salin dari Azure ML Studio ke kolom nilai.
    - Pilih **+ Add key value pairs** lagi.
    - Untuk nama kunci, masukkan **key** dan tempel kunci yang Anda salin dari Azure ML Studio ke kolom nilai.
    - Setelah menambahkan kunci, pilih **is secret** untuk mencegah kunci terekspos.

    ![Add connection.](../../../../../../translated_images/add-connection.ac7f5faf8b10b0dfe6679422f479f88cc47c33cbf24568da138ab19fbb17dc4b.id.png)

1. Pilih **Add connection**.

#### Buat Prompt flow

Anda telah menambahkan koneksi kustom di Azure AI Foundry. Sekarang, mari buat Prompt flow dengan langkah-langkah berikut. Kemudian, Anda akan menghubungkan Prompt flow ini ke koneksi kustom untuk menggunakan model yang sudah disesuaikan dalam Prompt flow.

1. Navigasikan ke proyek Azure AI Foundry yang Anda buat.

1. Pilih **Prompt flow** dari tab sisi kiri.

1. Pilih **+ Create** dari menu navigasi.

    ![Select Promptflow.](../../../../../../translated_images/select-promptflow.18ff2e61ab9173eb94fbf771819d7ddf21e9c239f2689cb2684d4d3c739deb75.id.png)

1. Pilih **Chat flow** dari menu navigasi.

    ![Select chat flow.](../../../../../../translated_images/select-flow-type.28375125ec9996d33a7d73eb77e59354e1b70fd246009e30bdd40db17143ec83.id.png)

1. Masukkan **Folder name** yang akan digunakan.

    ![Select chat flow.](../../../../../../translated_images/enter-name.02ddf8fb840ad4305ba88e0a804a5198ddd8720ebccb420d65ba13dcd481591f.id.png)

1. Pilih **Create**.

#### Atur Prompt flow untuk mengobrol dengan model Phi-3 / Phi-3.5 kustom Anda

Anda perlu mengintegrasikan model Phi-3 / Phi-3.5 yang sudah disesuaikan ke dalam Prompt flow. Namun, Prompt flow yang ada saat ini tidak dirancang untuk tujuan ini. Oleh karena itu, Anda harus merancang ulang Prompt flow agar dapat mengintegrasikan model kustom tersebut.

1. Di Prompt flow, lakukan tugas berikut untuk membangun ulang flow yang ada:

    - Pilih **Raw file mode**.
    - Hapus semua kode yang ada di file *flow.dag.yml*.
    - Tambahkan kode berikut ke *flow.dag.yml*.

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

    - Pilih **Save**.

    ![Select raw file mode.](../../../../../../translated_images/select-raw-file-mode.06c1eca581ce4f5344b4801da9d695b3c1ea7019479754e566d2df495e868664.id.png)

1. Tambahkan kode berikut ke *integrate_with_promptflow.py* untuk menggunakan model Phi-3 / Phi-3.5 kustom di Prompt flow.

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

    ![Paste prompt flow code.](../../../../../../translated_images/paste-promptflow-code.cd6d95b101c0ec2818291eeeb2aa744d0e01320308a1fa6348ac7f51bec93de9.id.png)

> [!NOTE]
> Untuk informasi lebih rinci tentang penggunaan Prompt flow di Azure AI Foundry, Anda dapat merujuk ke [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Pilih **Chat input**, **Chat output** untuk mengaktifkan fitur obrolan dengan model Anda.

    ![Select Input Output.](../../../../../../translated_images/select-input-output.c187fc58f25fbfc339811bdd5a2285589fef803aded96b8c58b40131f0663571.id.png)

1. Sekarang Anda siap untuk mengobrol dengan model Phi-3 / Phi-3.5 kustom Anda. Pada latihan berikutnya, Anda akan belajar cara memulai Prompt flow dan menggunakannya untuk mengobrol dengan model Phi-3 / Phi-3.5 yang sudah disesuaikan.

> [!NOTE]
>
> Flow yang dibangun ulang harus terlihat seperti gambar di bawah ini:
>
> ![Flow example](../../../../../../translated_images/graph-example.82fd1bcdd3fc545bcc81d64cb6542972ae593588ab94564c8c25edf06fae27fc.id.png)
>

#### Mulai Prompt flow

1. Pilih **Start compute sessions** untuk memulai Prompt flow.

    ![Start compute session.](../../../../../../translated_images/start-compute-session.9acd8cbbd2c43df160358b6be6cad3e069a9c22271fd8b40addc847aeca83b44.id.png)

1. Pilih **Validate and parse input** untuk memperbarui parameter.

    ![Validate input.](../../../../../../translated_images/validate-input.c1adb9543c6495be3c94da090ce7c61a77cc8baf0718552e3d6e41b87eb96a41.id.png)

1. Pilih **Value** dari **connection** ke koneksi kustom yang Anda buat. Contohnya, *connection*.

    ![Connection.](../../../../../../translated_images/select-connection.1f2b59222bcaafefe7ac3726aaa2a7fdb04a5b969cd09f009acfe8b1e841efb6.id.png)

#### Mengobrol dengan model Phi-3 / Phi-3.5 kustom Anda

1. Pilih **Chat**.

    ![Select chat.](../../../../../../translated_images/select-chat.0406bd9687d0c49d8bf2b8145f603ed5616b71ba82a0eadde189275b88e50a3f.id.png)

1. Berikut contoh hasilnya: Sekarang Anda dapat mengobrol dengan model Phi-3 / Phi-3.5 kustom Anda. Disarankan untuk mengajukan pertanyaan berdasarkan data yang digunakan untuk fine-tuning.

    ![Chat with prompt flow.](../../../../../../translated_images/chat-with-promptflow.1cf8cea112359ada4628ea1d3d9f563f3e6df2c01cf917bade1a5eb9d197493a.id.png)

### Deploy Azure OpenAI untuk mengevaluasi model Phi-3 / Phi-3.5

Untuk mengevaluasi model Phi-3 / Phi-3.5 di Azure AI Foundry, Anda perlu melakukan deploy model Azure OpenAI. Model ini akan digunakan untuk menilai performa model Phi-3 / Phi-3.5.

#### Deploy Azure OpenAI

1. Masuk ke [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Navigasikan ke proyek Azure AI Foundry yang Anda buat.

    ![Select Project.](../../../../../../translated_images/select-project-created.5221e0e403e2c9d6a17c809ad9aee8de593cd48717f157cc3eb2b29a37aa02ae.id.png)

1. Di Proyek yang Anda buat, pilih **Deployments** dari tab sisi kiri.

1. Pilih **+ Deploy model** dari menu navigasi.

1. Pilih **Deploy base model**.

    ![Select Deployments.](../../../../../../translated_images/deploy-openai-model.95d812346b25834b05b20fe43c20130da7eae1e485ad60bb8e46bbc85a6c613a.id.png)

1. Pilih model Azure OpenAI yang ingin Anda gunakan. Contohnya, **gpt-4o**.

    ![Select Azure OpenAI model you'd like to use.](../../../../../../translated_images/select-openai-model.959496d7e311546d66ec145dc4e0bf0cc806e6e5469b17e776788d6f5ba7a221.id.png)

1. Pilih **Confirm**.

### Evaluasi model Phi-3 / Phi-3.5 yang sudah disesuaikan menggunakan evaluasi Prompt flow di Azure AI Foundry

### Mulai evaluasi baru

1. Kunjungi [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Navigasikan ke proyek Azure AI Foundry yang Anda buat.

    ![Select Project.](../../../../../../translated_images/select-project-created.5221e0e403e2c9d6a17c809ad9aee8de593cd48717f157cc3eb2b29a37aa02ae.id.png)

1. Di Proyek yang Anda buat, pilih **Evaluation** dari tab sisi kiri.

1. Pilih **+ New evaluation** dari menu navigasi.

    ![Select evaluation.](../../../../../../translated_images/select-evaluation.2846ad7aaaca7f4f2cd3f728b640e64eeb639dc5dcb52f2d651099576b894848.id.png)

1. Pilih evaluasi **Prompt flow**.

    ![Select Prompt flow evaluation.](../../../../../../translated_images/promptflow-evaluation.cb9758cc19b4760f7a1ddda46bf47281cac59f2b1043f6a775a73977875f29a6.id.png)

1. Lakukan tugas berikut:

    - Masukkan nama evaluasi. Harus berupa nilai yang unik.
    - Pilih **Question and answer without context** sebagai tipe tugas. Karena, dataset **ULTRACHAT_200k** yang digunakan dalam tutorial ini tidak mengandung konteks.
    - Pilih prompt flow yang ingin Anda evaluasi.

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting1.4aa08259ff7a536e2e0e3011ff583f7164532d954a5ede4434fe9985cf51047e.id.png)

1. Pilih **Next**.

1. Lakukan tugas berikut:

    - Pilih **Add your dataset** untuk mengunggah dataset. Misalnya, Anda dapat mengunggah file dataset uji, seperti *test_data.json1*, yang disertakan saat Anda mengunduh dataset **ULTRACHAT_200k**.
    - Pilih **Dataset column** yang sesuai dengan dataset Anda. Misalnya, jika Anda menggunakan dataset **ULTRACHAT_200k**, pilih **${data.prompt}** sebagai kolom dataset.

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting2.07036831ba58d64ee622f9ee9b1c70f71b51cf39c3749dcd294414048c5b7e39.id.png)

1. Pilih **Next**.

1. Lakukan tugas berikut untuk mengonfigurasi metrik performa dan kualitas:

    - Pilih metrik performa dan kualitas yang ingin Anda gunakan.
    - Pilih model Azure OpenAI yang Anda buat untuk evaluasi. Contohnya, pilih **gpt-4o**.

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting3-1.d1ae69e3bf80914e68a0ad38486ca2d6c3ee5a30f4275f98fd3bc510c8d8f6d2.id.png)

1. Lakukan tugas berikut untuk mengonfigurasi metrik risiko dan keamanan:

    - Pilih metrik risiko dan keamanan yang ingin Anda gunakan.
    - Pilih ambang batas untuk menghitung tingkat cacat yang ingin Anda gunakan. Contohnya, pilih **Medium**.
    - Untuk **question**, pilih **Data source** ke **{$data.prompt}**.
    - Untuk **answer**, pilih **Data source** ke **{$run.outputs.answer}**.
    - Untuk **ground_truth**, pilih **Data source** ke **{$data.message}**.

    ![Prompt flow evaluation.](../../../../../../translated_images/evaluation-setting3-2.d53bd075c60a45a2fab8ffb7e4dc28e8e544d2a093fbc9f63449a03984df98d9.id.png)

1. Pilih **Next**.

1. Pilih **Submit** untuk memulai evaluasi.

1. Evaluasi akan memakan waktu beberapa saat untuk selesai. Anda dapat memantau kemajuan di tab **Evaluation**.

### Tinjau Hasil Evaluasi
> [!NOTE]
> Hasil yang disajikan di bawah ini dimaksudkan untuk mengilustrasikan proses evaluasi. Dalam tutorial ini, kami menggunakan model yang telah disesuaikan dengan dataset yang relatif kecil, yang mungkin menghasilkan hasil yang kurang optimal. Hasil sebenarnya dapat bervariasi secara signifikan tergantung pada ukuran, kualitas, dan keberagaman dataset yang digunakan, serta konfigurasi spesifik dari model tersebut.
Setelah evaluasi selesai, Anda dapat meninjau hasil untuk metrik kinerja dan keamanan.

1. Metrik kinerja dan kualitas:

    - menilai efektivitas model dalam menghasilkan respons yang koheren, lancar, dan relevan.

    ![Evaluation result.](../../../../../../translated_images/evaluation-result-gpu.85f48b42dfb7425434ec49685cff41376de3954fdab20f2a82c726f9fd690617.id.png)

1. Metrik risiko dan keamanan:

    - Pastikan output model aman dan sesuai dengan Prinsip Responsible AI, menghindari konten yang berbahaya atau menyinggung.

    ![Evaluation result.](../../../../../../translated_images/evaluation-result-gpu-2.1b74e336118f4fd0589153bf7fb6269cd10aaeb10c1456bc76a06b93b2be15e6.id.png)

1. Anda dapat menggulir ke bawah untuk melihat **Hasil metrik terperinci**.

    ![Evaluation result.](../../../../../../translated_images/detailed-metrics-result.afa2f5c39a4f5f179c3916ba948feb367dfd4e0658752615be62824ef1dcf2d3.id.png)

1. Dengan mengevaluasi model kustom Phi-3 / Phi-3.5 Anda berdasarkan metrik kinerja dan keamanan, Anda dapat memastikan bahwa model tidak hanya efektif, tetapi juga mematuhi praktik AI yang bertanggung jawab, sehingga siap untuk digunakan di dunia nyata.

## Selamat!

### Anda telah menyelesaikan tutorial ini

Anda telah berhasil mengevaluasi model Phi-3 yang telah disesuaikan dan terintegrasi dengan Prompt flow di Azure AI Foundry. Ini adalah langkah penting untuk memastikan bahwa model AI Anda tidak hanya berkinerja baik, tetapi juga mematuhi prinsip Responsible AI Microsoft agar Anda dapat membangun aplikasi AI yang dapat dipercaya dan andal.

![Architecture.](../../../../../../translated_images/architecture.10bec55250f5d6a4e1438bb31c5c70309908e21e7ada24a621bbfdd8d0f834f4.id.png)

## Bersihkan Sumber Daya Azure

Bersihkan sumber daya Azure Anda untuk menghindari biaya tambahan pada akun Anda. Buka portal Azure dan hapus sumber daya berikut:

- Resource Azure Machine learning.
- Endpoint model Azure Machine learning.
- Resource Azure AI Foundry Project.
- Resource Azure AI Foundry Prompt flow.

### Langkah Selanjutnya

#### Dokumentasi

- [Assess AI systems by using the Responsible AI dashboard](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [Evaluation and monitoring metrics for generative AI](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Azure AI Foundry documentation](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Prompt flow documentation](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### Konten Pelatihan

- [Introduction to Microsoft's Responsible AI Approach](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Introduction to Azure AI Foundry](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### Referensi

- [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [Announcing new tools in Azure AI to help you build more secure and trustworthy generative AI applications](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.