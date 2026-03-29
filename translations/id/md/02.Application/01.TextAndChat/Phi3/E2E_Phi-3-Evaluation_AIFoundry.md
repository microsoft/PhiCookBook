# Evaluasi Model Phi-3 / Phi-3.5 Fine-tuned di Microsoft Foundry dengan Fokus pada Prinsip Responsible AI Microsoft

Contoh end-to-end (E2E) ini didasarkan pada panduan "[Evaluate Fine-tuned Phi-3 / 3.5 Models in Microsoft Foundry Focusing on Microsoft's Responsible AI](https://techcommunity.microsoft.com/blog/educatordeveloperblog/evaluate-fine-tuned-phi-3--3-5-models-in-azure-ai-studio-focusing-on-microsofts-/4227850?WT.mc_id=aiml-137032-kinfeylo)" dari Microsoft Tech Community.

## Ikhtisar

### Bagaimana Anda dapat mengevaluasi keamanan dan kinerja model Phi-3 / Phi-3.5 yang telah di-fine-tune di Microsoft Foundry?

Fine-tuning model terkadang dapat menyebabkan respon yang tidak diinginkan atau tidak sengaja. Untuk memastikan model tetap aman dan efektif, penting untuk mengevaluasi potensi model dalam menghasilkan konten berbahaya serta kemampuannya menghasilkan jawaban yang akurat, relevan, dan koheren. Dalam tutorial ini, Anda akan mempelajari cara mengevaluasi keamanan dan kinerja model Phi-3 / Phi-3.5 yang telah di-fine-tune dan diintegrasikan dengan Prompt flow di Microsoft Foundry.

Berikut adalah proses evaluasi Microsoft Foundry.

![Architecture of tutorial.](../../../../../../translated_images/id/architecture.10bec55250f5d6a4.webp)

*Sumber Gambar: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> Untuk informasi lebih rinci dan menjelajahi sumber daya tambahan tentang Phi-3 / Phi-3.5, silakan kunjungi [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723).

### Prasyarat

- [Python](https://www.python.org/downloads)
- [Langganan Azure](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- Model Phi-3 / Phi-3.5 yang sudah di-fine-tune

### Daftar Isi

1. [**Skenario 1: Pengenalan Evaluasi Prompt flow di Microsoft Foundry**](#scenario-1-introduction-to-azure-ai-studios-prompt-flow-evaluation)

    - [Pengenalan evaluasi keamanan](#pengenalan-evaluasi-keamanan)
    - [Pengenalan evaluasi kinerja](#pengenalan-evaluasi-kinerja)

1. [**Skenario 2: Mengevaluasi model Phi-3 / Phi-3.5 di Microsoft Foundry**](#scenario-2-evaluating-the-phi-3--phi-35-model-in-azure-ai-studio)

    - [Sebelum memulai](#sebelum-memulai)
    - [Deploy Azure OpenAI untuk mengevaluasi model Phi-3 / Phi-3.5](#deploy-azure-openai-to-evaluate-the-phi-3--phi-35-model)
    - [Evaluasi model Phi-3 / Phi-3.5 yang sudah di-fine-tune menggunakan evaluasi Prompt flow Microsoft Foundry](#evaluate-the-fine-tuned-phi-3--phi-35-model-using-azure-ai-studios-prompt-flow-evaluation)

1. [Selamat!](#selamat)

## **Skenario 1: Pengenalan Evaluasi Prompt flow di Microsoft Foundry**

### Pengenalan evaluasi keamanan

Untuk memastikan model AI Anda etis dan aman, sangat penting untuk mengevaluasinya berdasarkan Prinsip Responsible AI Microsoft. Di Microsoft Foundry, evaluasi keamanan memungkinkan Anda menilai kerentanan model terhadap serangan jailbreak dan potensinya dalam menghasilkan konten berbahaya, yang sesuai langsung dengan prinsip-prinsip ini.

![Safaty evaluation.](../../../../../../translated_images/id/safety-evaluation.083586ec88dfa950.webp)

*Sumber Gambar: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Prinsip Responsible AI Microsoft

Sebelum memulai langkah teknis, penting untuk memahami Prinsip Responsible AI Microsoft, sebuah kerangka etika yang dirancang untuk membimbing pengembangan, penerapan, dan pengoperasian sistem AI secara bertanggung jawab. Prinsip-prinsip ini memandu desain, pengembangan, dan penerapan AI secara bertanggung jawab, memastikan teknologi AI dibangun secara adil, transparan, dan inklusif. Prinsip-prinsip ini menjadi dasar untuk mengevaluasi keamanan model AI.

Prinsip Responsible AI Microsoft meliputi:

- **Keadilan dan Inklusivitas**: Sistem AI harus memperlakukan semua orang secara adil dan menghindari perlakuan berbeda terhadap kelompok orang yang berada dalam situasi serupa. Misalnya, saat sistem AI memberikan panduan pengobatan medis, aplikasi pinjaman, atau pekerjaan, sistem harus memberikan rekomendasi yang sama kepada semua orang dengan gejala, kondisi keuangan, atau kualifikasi profesional yang serupa.

- **Keandalan dan Keamanan**: Untuk membangun kepercayaan, sangat penting bahwa sistem AI beroperasi secara andal, aman, dan konsisten. Sistem ini harus dapat beroperasi sesuai desain awal, merespons dengan aman terhadap kondisi tak terduga, dan tahan terhadap manipulasi berbahaya. Cara perilaku dan rentang kondisi yang dapat mereka tangani mencerminkan berbagai situasi dan kondisi yang diperkirakan pengembang selama desain dan pengujian.

- **Transparansi**: Saat sistem AI membantu pengambilan keputusan yang berdampak besar pada kehidupan seseorang, sangat penting orang memahami bagaimana keputusan tersebut dibuat. Contohnya, bank mungkin menggunakan sistem AI untuk menilai kelayakan kredit seseorang. Perusahaan mungkin menggunakan AI untuk menentukan kandidat paling memenuhi syarat yang akan dipekerjakan.

- **Privasi dan Keamanan**: Seiring AI menjadi lebih umum, perlindungan privasi dan keamanan informasi pribadi serta bisnis menjadi semakin penting dan kompleks. Dengan AI, privasi dan keamanan data membutuhkan perhatian khusus karena akses ke data sangat penting agar sistem AI dapat membuat prediksi dan keputusan yang akurat serta informasi tentang orang.

- **Akuntabilitas**: Orang yang merancang dan menerapkan sistem AI harus bertanggung jawab atas cara sistem mereka beroperasi. Organisasi harus menggunakan standar industri untuk mengembangkan norma-norma akuntabilitas. Norma ini dapat memastikan sistem AI bukan otoritas final untuk keputusan yang memengaruhi kehidupan orang. Mereka juga memastikan manusia mempertahankan kendali bermakna atas sistem AI yang sangat otonom.

![Fill hub.](../../../../../../translated_images/id/responsibleai2.c07ef430113fad8c.webp)

*Sumber Gambar: [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> Untuk mempelajari lebih lanjut tentang Prinsip Responsible AI Microsoft, kunjungi [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723).

#### Metrik keamanan

Dalam tutorial ini, Anda akan mengevaluasi keamanan model Phi-3 yang telah di-fine-tune menggunakan metrik keamanan Microsoft Foundry. Metrik ini membantu Anda menilai potensi model untuk menghasilkan konten berbahaya dan kerentanan terhadap serangan jailbreak. Metrik keamanan meliputi:

- **Konten Terkait Bahaya pada Diri Sendiri**: Mengevaluasi apakah model cenderung menghasilkan konten terkait bahaya terhadap diri sendiri.
- **Konten Kebencian dan Tidak Adil**: Mengevaluasi apakah model cenderung menghasilkan konten yang penuh kebencian atau tidak adil.
- **Konten Kekerasan**: Mengevaluasi apakah model cenderung menghasilkan konten kekerasan.
- **Konten Seksual**: Mengevaluasi apakah model cenderung menghasilkan konten seksual yang tidak pantas.

Evaluasi aspek-aspek ini memastikan model AI tidak menghasilkan konten berbahaya atau menyinggung, serta selaras dengan nilai sosial dan standar regulasi.

![Evaluate based on safety.](../../../../../../translated_images/id/evaluate-based-on-safety.c5df819f5b0bfc07.webp)

### Pengenalan evaluasi kinerja

Untuk memastikan model AI Anda berperforma seperti yang diharapkan, penting mengevaluasi kinerjanya berdasarkan metrik kinerja. Di Microsoft Foundry, evaluasi kinerja memungkinkan Anda menilai efektivitas model dalam menghasilkan respon yang akurat, relevan, dan koheren.

![Safaty evaluation.](../../../../../../translated_images/id/performance-evaluation.48b3e7e01a098740.webp)

*Sumber Gambar: [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Metrik kinerja

Dalam tutorial ini, Anda akan mengevaluasi kinerja model Phi-3 / Phi-3.5 yang sudah di-fine-tune menggunakan metrik kinerja Microsoft Foundry. Metrik ini membantu Anda menilai efektivitas model dalam menghasilkan jawaban yang akurat, relevan, dan koheren. Metrik kinerja meliputi:

- **Keterdasaran (Groundedness)**: Mengevaluasi seberapa baik jawaban yang dihasilkan selaras dengan informasi dari sumber input.
- **Relevansi**: Mengevaluasi kesesuaian respon yang dihasilkan dengan pertanyaan yang diberikan.
- **Koherensi**: Mengevaluasi seberapa lancar teks yang dihasilkan mengalir, terbaca alami, dan menyerupai bahasa manusia.
- **Kelancaran (Fluency)**: Mengevaluasi kemahiran bahasa dari teks yang dibuat.
- **Kesamaan GPT (GPT Similarity)**: Membandingkan respon yang dihasilkan dengan kebenaran dasar untuk kesamaan.
- **Skor F1**: Menghitung rasio kata yang sama antara respon yang dihasilkan dan data sumber.

Metrik-metrik ini membantu Anda menilai efektivitas model dalam menghasilkan respon yang akurat, relevan, dan koheren.

![Evaluate based on performance.](../../../../../../translated_images/id/evaluate-based-on-performance.3e801c647c7554e8.webp)

## **Skenario 2: Mengevaluasi model Phi-3 / Phi-3.5 di Microsoft Foundry**

### Sebelum memulai

Tutorial ini merupakan lanjutan dari posting blog sebelumnya, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" dan "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)." Dalam posting tersebut, kami membahas proses fine-tuning model Phi-3 / Phi-3.5 di Microsoft Foundry dan mengintegrasikannya dengan Prompt flow.

Dalam tutorial ini, Anda akan menerapkan model Azure OpenAI sebagai evaluator di Microsoft Foundry dan menggunakannya untuk mengevaluasi model Phi-3 / Phi-3.5 yang sudah di-fine-tune.

Sebelum memulai tutorial ini, pastikan Anda telah memenuhi prasyarat berikut, seperti yang dijelaskan dalam tutorial sebelumnya:

1. Dataset yang sudah dipersiapkan untuk mengevaluasi model Phi-3 / Phi-3.5 yang sudah di-fine-tune.
1. Model Phi-3 / Phi-3.5 yang telah di-fine-tune dan diterapkan di Azure Machine Learning.
1. Prompt flow yang terintegrasi dengan model Phi-3 / Phi-3.5 yang sudah di-fine-tune di Microsoft Foundry.

> [!NOTE]
> Anda akan menggunakan file *test_data.jsonl*, yang terletak di folder data dari dataset **ULTRACHAT_200k** yang diunduh pada posting blog sebelumnya, sebagai dataset untuk mengevaluasi model Phi-3 / Phi-3.5 yang sudah di-fine-tune.

#### Integrasikan model kustom Phi-3 / Phi-3.5 dengan Prompt flow di Microsoft Foundry (Pendekatan berbasis kode)

> [!NOTE]
> Jika Anda mengikuti pendekatan low-code yang dijelaskan dalam "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)", Anda dapat melewati latihan ini dan melanjutkan ke latihan berikutnya.
> Namun, jika Anda mengikuti pendekatan code-first yang dijelaskan dalam "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" untuk melakukan fine-tuning dan deployment model Phi-3 / Phi-3.5, proses menghubungkan model Anda dengan Prompt flow sedikit berbeda. Anda akan mempelajari proses ini dalam latihan ini.

Untuk melanjutkan, Anda perlu mengintegrasikan model Phi-3 / Phi-3.5 yang sudah di-fine-tune ke dalam Prompt flow di Microsoft Foundry.

#### Membuat Microsoft Foundry Hub

Anda perlu membuat Hub sebelum membuat Proyek. Hub berfungsi seperti Resource Group, memungkinkan Anda mengorganisir dan mengelola beberapa Proyek di Microsoft Foundry.
1. Masuk ke [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Pilih **All hubs** dari tab sisi kiri.

1. Pilih **+ New hub** dari menu navigasi.

    ![Create hub.](../../../../../../translated_images/id/create-hub.5be78fb1e21ffbf1.webp)

1. Lakukan tugas-tugas berikut:

    - Masukkan **Hub name**. Nilainya harus unik.
    - Pilih **Subscription** Azure Anda.
    - Pilih **Resource group** yang akan digunakan (buat yang baru jika perlu).
    - Pilih **Location** yang ingin Anda gunakan.
    - Pilih **Connect Azure AI Services** yang akan digunakan (buat yang baru jika perlu).
    - Pilih **Connect Azure AI Search** ke **Skip connecting**.

    ![Fill hub.](../../../../../../translated_images/id/fill-hub.baaa108495c71e34.webp)

1. Pilih **Next**.

#### Buat Proyek Microsoft Foundry

1. Di Hub yang Anda buat, pilih **All projects** dari tab sisi kiri.

1. Pilih **+ New project** dari menu navigasi.

    ![Select new project.](../../../../../../translated_images/id/select-new-project.cd31c0404088d7a3.webp)

1. Masukkan **Project name**. Nilainya harus unik.

    ![Create project.](../../../../../../translated_images/id/create-project.ca3b71298b90e420.webp)

1. Pilih **Create a project**.

#### Tambahkan koneksi khusus untuk model Phi-3 / Phi-3.5 yang telah di-fine-tune

Untuk mengintegrasikan model custom Phi-3 / Phi-3.5 Anda dengan Prompt flow, Anda perlu menyimpan endpoint dan kunci model dalam koneksi khusus. Pengaturan ini memastikan akses ke model custom Phi-3 / Phi-3.5 Anda di Prompt flow.

#### Atur kunci api dan URI endpoint model Phi-3 / Phi-3.5 yang telah di-fine-tune

1. Kunjungi [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Navigasikan ke workspace Azure Machine Learning yang Anda buat.

1. Pilih **Endpoints** dari tab sisi kiri.

    ![Select endpoints.](../../../../../../translated_images/id/select-endpoints.ee7387ecd68bd18d.webp)

1. Pilih endpoint yang Anda buat.

    ![Select endpoints.](../../../../../../translated_images/id/select-endpoint-created.9f63af5e4cf98b2e.webp)

1. Pilih **Consume** dari menu navigasi.

1. Salin **REST endpoint** dan **Primary key** Anda.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/id/copy-endpoint-key.0650c3786bd646ab.webp)

#### Tambahkan Koneksi Khusus

1. Kunjungi [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Navigasikan ke proyek Microsoft Foundry yang Anda buat.

1. Di proyek yang Anda buat, pilih **Settings** dari tab sisi kiri.

1. Pilih **+ New connection**.

    ![Select new connection.](../../../../../../translated_images/id/select-new-connection.fa0f35743758a74b.webp)

1. Pilih **Custom keys** dari menu navigasi.

    ![Select custom keys.](../../../../../../translated_images/id/select-custom-keys.5a3c6b25580a9b67.webp)

1. Lakukan tugas berikut:

    - Pilih **+ Add key value pairs**.
    - Untuk nama kunci, masukkan **endpoint** dan tempel endpoint yang Anda salin dari Azure ML Studio ke dalam kolom nilai.
    - Pilih **+ Add key value pairs** lagi.
    - Untuk nama kunci, masukkan **key** dan tempel kunci yang Anda salin dari Azure ML Studio ke dalam kolom nilai.
    - Setelah menambahkan kunci, pilih **is secret** untuk mencegah kunci terekspos.

    ![Add connection.](../../../../../../translated_images/id/add-connection.ac7f5faf8b10b0df.webp)

1. Pilih **Add connection**.

#### Buat Prompt flow

Anda telah menambahkan koneksi khusus di Microsoft Foundry. Sekarang, mari buat Prompt flow menggunakan langkah-langkah berikut. Kemudian, Anda akan menghubungkan Prompt flow ini ke koneksi khusus untuk menggunakan model fine-tuned di dalam Prompt flow.

1. Navigasikan ke proyek Microsoft Foundry yang Anda buat.

1. Pilih **Prompt flow** dari tab sisi kiri.

1. Pilih **+ Create** dari menu navigasi.

    ![Select Promptflow.](../../../../../../translated_images/id/select-promptflow.18ff2e61ab9173eb.webp)

1. Pilih **Chat flow** dari menu navigasi.

    ![Select chat flow.](../../../../../../translated_images/id/select-flow-type.28375125ec9996d3.webp)

1. Masukkan **Folder name** yang akan digunakan.

    ![Select chat flow.](../../../../../../translated_images/id/enter-name.02ddf8fb840ad430.webp)

1. Pilih **Create**.

#### Siapkan Prompt flow untuk mengobrol dengan model Phi-3 / Phi-3.5 custom Anda

Anda perlu mengintegrasikan model Phi-3 / Phi-3.5 yang telah di-fine-tune ke dalam Prompt flow. Namun, Prompt flow yang ada saat ini tidak dirancang untuk tujuan ini. Oleh karena itu, Anda harus merancang ulang Prompt flow agar memungkinkan integrasi model custom tersebut.

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

    ![Select raw file mode.](../../../../../../translated_images/id/select-raw-file-mode.06c1eca581ce4f53.webp)

1. Tambahkan kode berikut ke *integrate_with_promptflow.py* untuk menggunakan model custom Phi-3 / Phi-3.5 dalam Prompt flow.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Pengaturan pencatatan
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

        # "connection" adalah nama Koneksi Kustom, "endpoint", "key" adalah kunci dalam Koneksi Kustom
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
            
            # Catat respons JSON lengkap
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

    ![Paste prompt flow code.](../../../../../../translated_images/id/paste-promptflow-code.cd6d95b101c0ec28.webp)

> [!NOTE]
> Untuk informasi lebih rinci tentang penggunaan Prompt flow di Microsoft Foundry, Anda dapat merujuk ke [Prompt flow in Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Pilih **Chat input**, **Chat output** untuk mengaktifkan chat dengan model Anda.

    ![Select Input Output.](../../../../../../translated_images/id/select-input-output.c187fc58f25fbfc3.webp)

1. Sekarang Anda siap mengobrol dengan model custom Phi-3 / Phi-3.5 Anda. Pada latihan berikutnya, Anda akan belajar cara memulai Prompt flow dan menggunakannya untuk mengobrol dengan model Phi-3 / Phi-3.5 yang sudah di-fine-tune.

> [!NOTE]
>
> Flow yang dibangun ulang seharusnya terlihat seperti gambar di bawah ini:
>
> ![Flow example](../../../../../../translated_images/id/graph-example.82fd1bcdd3fc545b.webp)
>

#### Mulai Prompt flow

1. Pilih **Start compute sessions** untuk memulai Prompt flow.

    ![Start compute session.](../../../../../../translated_images/id/start-compute-session.9acd8cbbd2c43df1.webp)

1. Pilih **Validate and parse input** untuk memperbarui parameter.

    ![Validate input.](../../../../../../translated_images/id/validate-input.c1adb9543c6495be.webp)

1. Pilih **Value** dari **connection** ke koneksi khusus yang Anda buat. Misalnya, *connection*.

    ![Connection.](../../../../../../translated_images/id/select-connection.1f2b59222bcaafef.webp)

#### Obrolan dengan model Phi-3 / Phi-3.5 custom Anda

1. Pilih **Chat**.

    ![Select chat.](../../../../../../translated_images/id/select-chat.0406bd9687d0c49d.webp)

1. Berikut contoh hasilnya: Sekarang Anda dapat mengobrol dengan model Phi-3 / Phi-3.5 custom Anda. Disarankan untuk mengajukan pertanyaan berdasarkan data yang digunakan untuk fine-tuning.

    ![Chat with prompt flow.](../../../../../../translated_images/id/chat-with-promptflow.1cf8cea112359ada.webp)

### Deploy Azure OpenAI untuk mengevaluasi model Phi-3 / Phi-3.5

Untuk mengevaluasi model Phi-3 / Phi-3.5 di Microsoft Foundry, Anda perlu melakukan deploy model Azure OpenAI. Model ini akan digunakan untuk mengevaluasi performa model Phi-3 / Phi-3.5.

#### Deploy Azure OpenAI

1. Masuk ke [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Navigasikan ke proyek Microsoft Foundry yang Anda buat.

    ![Select Project.](../../../../../../translated_images/id/select-project-created.5221e0e403e2c9d6.webp)

1. Di proyek yang Anda buat, pilih **Deployments** dari tab sisi kiri.

1. Pilih **+ Deploy model** dari menu navigasi.

1. Pilih **Deploy base model**.

    ![Select Deployments.](../../../../../../translated_images/id/deploy-openai-model.95d812346b25834b.webp)

1. Pilih model Azure OpenAI yang ingin Anda gunakan. Contoh, **gpt-4o**.

    ![Select Azure OpenAI model you'd like to use.](../../../../../../translated_images/id/select-openai-model.959496d7e311546d.webp)

1. Pilih **Confirm**.

### Evaluasi model Phi-3 / Phi-3.5 yang telah di-fine-tune menggunakan evaluasi Prompt flow di Microsoft Foundry

### Mulai evaluasi baru

1. Kunjungi [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Navigasikan ke proyek Microsoft Foundry yang Anda buat.

    ![Select Project.](../../../../../../translated_images/id/select-project-created.5221e0e403e2c9d6.webp)

1. Di proyek yang Anda buat, pilih **Evaluation** dari tab sisi kiri.

1. Pilih **+ New evaluation** dari menu navigasi.

    ![Select evaluation.](../../../../../../translated_images/id/select-evaluation.2846ad7aaaca7f4f.webp)

1. Pilih evaluasi **Prompt flow**.

    ![Select Prompt flow evaluation.](../../../../../../translated_images/id/promptflow-evaluation.cb9758cc19b4760f.webp)

1. Lakukan tugas berikut:

    - Masukkan nama evaluasi. Harus merupakan nilai unik.
    - Pilih **Question and answer without context** sebagai tipe tugas. Karena dataset **ULTRACHAT_200k** yang digunakan dalam tutorial ini tidak berisi konteks.
    - Pilih prompt flow yang ingin dievaluasi.

    ![Prompt flow evaluation.](../../../../../../translated_images/id/evaluation-setting1.4aa08259ff7a536e.webp)

1. Pilih **Next**.

1. Lakukan tugas berikut:

    - Pilih **Add your dataset** untuk mengunggah dataset. Misalnya, Anda bisa mengunggah file dataset uji seperti *test_data.json1* yang disertakan saat Anda mengunduh dataset **ULTRACHAT_200k**.
    - Pilih kolom **Dataset** yang sesuai dengan dataset Anda. Misalnya, jika menggunakan dataset **ULTRACHAT_200k**, pilih **${data.prompt}** sebagai kolom dataset.

    ![Prompt flow evaluation.](../../../../../../translated_images/id/evaluation-setting2.07036831ba58d64e.webp)

1. Pilih **Next**.

1. Lakukan tugas berikut untuk mengonfigurasi metrik performa dan kualitas:

    - Pilih metrik performa dan kualitas yang ingin digunakan.
    - Pilih model Azure OpenAI yang Anda buat untuk evaluasi. Misalnya, pilih **gpt-4o**.

    ![Prompt flow evaluation.](../../../../../../translated_images/id/evaluation-setting3-1.d1ae69e3bf80914e.webp)

1. Lakukan tugas berikut untuk mengonfigurasi metrik risiko dan keselamatan:

    - Pilih metrik risiko dan keselamatan yang ingin digunakan.
    - Pilih ambang batas untuk menghitung tingkat cacat yang ingin digunakan. Contohnya, pilih **Medium**.
    - Untuk **question**, pilih **Data source** menjadi **{$data.prompt}**.
    - Untuk **answer**, pilih **Data source** menjadi **{$run.outputs.answer}**.
    - Untuk **ground_truth**, pilih **Data source** menjadi **{$data.message}**.

    ![Prompt flow evaluation.](../../../../../../translated_images/id/evaluation-setting3-2.d53bd075c60a45a2.webp)

1. Pilih **Next**.

1. Pilih **Submit** untuk memulai evaluasi.

1. Evaluasi akan memakan waktu beberapa saat untuk selesai. Anda dapat memantau kemajuan di tab **Evaluation**.

### Tinjau Hasil Evaluasi

> [!NOTE]
> Hasil yang disajikan di bawah ini dimaksudkan untuk mengilustrasikan proses evaluasi. Dalam tutorial ini, kami menggunakan model yang di-fine-tune pada dataset yang relatif kecil, yang mungkin menghasilkan hasil yang kurang optimal. Hasil aktual dapat sangat bervariasi tergantung pada ukuran, kualitas, dan keberagaman dataset yang digunakan, serta konfigurasi spesifik dari model tersebut.

Setelah evaluasi selesai, Anda dapat meninjau hasil untuk metrik performa dan keselamatan.
1. Metrik kinerja dan kualitas:

    - mengevaluasi efektivitas model dalam menghasilkan respons yang koheren, lancar, dan relevan.

    ![Evaluation result.](../../../../../../translated_images/id/evaluation-result-gpu.85f48b42dfb74254.webp)

1. Metrik risiko dan keselamatan:

    - Memastikan bahwa keluaran model aman dan sesuai dengan Prinsip AI yang Bertanggung Jawab, menghindari konten yang berbahaya atau ofensif.

    ![Evaluation result.](../../../../../../translated_images/id/evaluation-result-gpu-2.1b74e336118f4fd0.webp)

1. Anda dapat menggulir ke bawah untuk melihat **Hasil metrik terperinci**.

    ![Evaluation result.](../../../../../../translated_images/id/detailed-metrics-result.afa2f5c39a4f5f17.webp)

1. Dengan mengevaluasi model khusus Phi-3 / Phi-3.5 Anda menggunakan metrik kinerja dan keselamatan, Anda dapat memastikan bahwa model tidak hanya efektif, tetapi juga mematuhi praktik AI yang bertanggung jawab, sehingga siap untuk diterapkan di dunia nyata.

## Selamat!

### Anda telah menyelesaikan tutorial ini

Anda telah berhasil mengevaluasi model Phi-3 yang telah disesuaikan dan terintegrasi dengan Prompt flow di Microsoft Foundry. Ini adalah langkah penting untuk memastikan bahwa model AI Anda tidak hanya berkinerja baik, tetapi juga mematuhi prinsip AI Bertanggung Jawab dari Microsoft guna membantu Anda membangun aplikasi AI yang tepercaya dan andal.

![Architecture.](../../../../../../translated_images/id/architecture.10bec55250f5d6a4.webp)

## Bersihkan Sumber Daya Azure

Bersihkan sumber daya Azure Anda untuk menghindari biaya tambahan pada akun Anda. Pergi ke portal Azure dan hapus sumber daya berikut:

- Sumber daya Azure Machine Learning.
- Endpoint model Azure Machine Learning.
- Sumber daya Proyek Microsoft Foundry.
- Sumber daya Prompt flow Microsoft Foundry.

### Langkah Selanjutnya

#### Dokumentasi

- [Menilai sistem AI dengan menggunakan dasbor Responsible AI](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [Metrik evaluasi dan pemantauan untuk AI generatif](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Dokumentasi Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Dokumentasi Prompt flow](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### Konten Pelatihan

- [Pengenalan Pendekatan AI Bertanggung Jawab Microsoft](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Pengenalan Microsoft Foundry](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### Referensi

- [Apa itu AI Bertanggung Jawab?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [Mengumumkan alat baru di Azure AI untuk membantu Anda membangun aplikasi AI generatif yang lebih aman dan tepercaya](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [Evaluasi aplikasi AI generatif](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya mencapai akurasi, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau kesalahan tafsir yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->