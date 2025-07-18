<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9481b07dda8f9715a5d1ff43fb27568b",
  "translation_date": "2025-07-16T20:15:05+00:00",
  "source_file": "md/01.Introduction/03/Android_Inference.md",
  "language_code": "ms"
}
-->
# **Inferens Phi-3 di Android**

Mari kita terokai bagaimana anda boleh melakukan inferens dengan Phi-3-mini pada peranti Android. Phi-3-mini adalah siri model baru dari Microsoft yang membolehkan penyebaran Large Language Models (LLMs) pada peranti edge dan peranti IoT.

## Semantic Kernel dan Inferens

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) adalah rangka kerja aplikasi yang membolehkan anda mencipta aplikasi yang serasi dengan Azure OpenAI Service, model OpenAI, dan juga model tempatan. Jika anda baru dengan Semantic Kernel, kami cadangkan anda melihat [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo).

### Untuk Mengakses Phi-3-mini Menggunakan Semantic Kernel

Anda boleh menggabungkannya dengan Hugging Face Connector dalam Semantic Kernel. Rujuk [Sample Code](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo).

Secara lalai, ia merujuk kepada model ID di Hugging Face. Namun, anda juga boleh menyambung ke pelayan model Phi-3-mini yang dibina secara tempatan.

### Memanggil Model Quantized dengan Ollama atau LlamaEdge

Ramai pengguna lebih suka menggunakan model quantized untuk menjalankan model secara tempatan. [Ollama](https://ollama.com/) dan [LlamaEdge](https://llamaedge.com) membolehkan pengguna individu memanggil pelbagai model quantized:

#### Ollama

Anda boleh terus menjalankan `ollama run Phi-3` atau mengkonfigurasikannya secara offline dengan membuat `Modelfile` yang mengandungi laluan ke fail `.gguf` anda.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Sample Code](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

Jika anda ingin menggunakan fail `.gguf` di awan dan pada peranti edge secara serentak, LlamaEdge adalah pilihan yang baik. Anda boleh rujuk [sample code](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) untuk memulakan.

### Pasang dan Jalankan pada Telefon Android

1. **Muat turun aplikasi MLC Chat** (Percuma) untuk telefon Android.  
2. Muat turun fail APK (148MB) dan pasang pada peranti anda.  
3. Lancarkan aplikasi MLC Chat. Anda akan melihat senarai model AI, termasuk Phi-3-mini.

Secara ringkas, Phi-3-mini membuka peluang menarik untuk AI generatif pada peranti edge, dan anda boleh mula meneroka kemampuannya di Android.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.