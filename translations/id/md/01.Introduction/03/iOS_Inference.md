<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "82af197df38d25346a98f1f0e84d1698",
  "translation_date": "2025-05-09T11:02:35+00:00",
  "source_file": "md/01.Introduction/03/iOS_Inference.md",
  "language_code": "id"
}
-->
# **Inference Phi-3 di iOS**

Phi-3-mini adalah seri model baru dari Microsoft yang memungkinkan penerapan Large Language Models (LLMs) pada perangkat edge dan perangkat IoT. Phi-3-mini tersedia untuk deployment iOS, Android, dan Edge Device, memungkinkan AI generatif dijalankan di lingkungan BYOD. Contoh berikut menunjukkan cara menerapkan Phi-3-mini di iOS.

## **1. Persiapan**

- **a.** macOS 14+
- **b.** Xcode 15+
- **c.** iOS SDK 17.x (iPhone 14 A16 atau lebih tinggi)
- **d.** Instal Python 3.10+ (Conda direkomendasikan)
- **e.** Instal library Python: `python-flatbuffers`
- **f.** Instal CMake

### Semantic Kernel dan Inference

Semantic Kernel adalah framework aplikasi yang memungkinkan Anda membuat aplikasi yang kompatibel dengan Azure OpenAI Service, model OpenAI, bahkan model lokal. Mengakses layanan lokal melalui Semantic Kernel memudahkan integrasi dengan server model Phi-3-mini yang Anda hosting sendiri.

### Memanggil Model Quantized dengan Ollama atau LlamaEdge

Banyak pengguna lebih memilih menggunakan model quantized untuk menjalankan model secara lokal. [Ollama](https://ollama.com) dan [LlamaEdge](https://llamaedge.com) memungkinkan pengguna memanggil berbagai model quantized:

#### **Ollama**

Anda bisa menjalankan `ollama run phi3` secara langsung atau mengonfigurasinya secara offline. Buat Modelfile dengan path ke file `gguf` Anda. Contoh kode untuk menjalankan model Phi-3-mini quantized:

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

#### **LlamaEdge**

Jika Anda ingin menggunakan `gguf` di cloud dan perangkat edge secara bersamaan, LlamaEdge adalah pilihan yang tepat.

## **2. Mengompilasi ONNX Runtime untuk iOS**

```bash

git clone https://github.com/microsoft/onnxruntime.git

cd onnxruntime

./build.sh --build_shared_lib --ios --skip_tests --parallel --build_dir ./build_ios --ios --apple_sysroot iphoneos --osx_arch arm64 --apple_deploy_target 17.5 --cmake_generator Xcode --config Release

cd ../

```

### **Perhatian**

- **a.** Sebelum mengompilasi, pastikan Xcode sudah dikonfigurasi dengan benar dan atur sebagai direktori pengembang aktif di terminal:

    ```bash
    sudo xcode-select -switch /Applications/Xcode.app/Contents/Developer
    ```

- **b.** ONNX Runtime perlu dikompilasi untuk berbagai platform. Untuk iOS, Anda bisa mengompilasi untuk `arm64` or `x86_64`.

- **c.** Disarankan menggunakan iOS SDK terbaru untuk kompilasi. Namun, Anda juga bisa menggunakan versi SDK yang lebih lama jika membutuhkan kompatibilitas dengan SDK sebelumnya.

## **3. Mengompilasi Generative AI dengan ONNX Runtime untuk iOS**

> **Note:** Karena Generative AI dengan ONNX Runtime masih dalam tahap preview, harap waspadai kemungkinan perubahan.

```bash

git clone https://github.com/microsoft/onnxruntime-genai
 
cd onnxruntime-genai
 
mkdir ort
 
cd ort
 
mkdir include
 
mkdir lib
 
cd ../
 
cp ../onnxruntime/include/onnxruntime/core/session/onnxruntime_c_api.h ort/include
 
cp ../onnxruntime/build_ios/Release/Release-iphoneos/libonnxruntime*.dylib* ort/lib
 
export OPENCV_SKIP_XCODEBUILD_FORCE_TRYCOMPILE_DEBUG=1
 
python3 build.py --parallel --build_dir ./build_ios --ios --ios_sysroot iphoneos --ios_arch arm64 --ios_deployment_target 17.5 --cmake_generator Xcode --cmake_extra_defines CMAKE_XCODE_ATTRIBUTE_CODE_SIGNING_ALLOWED=NO

```

## **4. Membuat aplikasi App di Xcode**

Saya memilih Objective-C sebagai metode pengembangan App, karena menggunakan Generative AI dengan ONNX Runtime C++ API, Objective-C lebih kompatibel. Tentu saja, Anda juga bisa melakukan pemanggilan terkait melalui bridging Swift.

![xcode](../../../../../translated_images/xcode.6c67033ca85b703e80cc51ecaa681fbcb6ac63cc0c256705ac97bc9ca039c235.id.png)

## **5. Menyalin model ONNX quantized INT4 ke proyek aplikasi App**

Kita perlu mengimpor model quantization INT4 dalam format ONNX, yang harus diunduh terlebih dahulu

![hf](../../../../../translated_images/hf.b99941885c6561bb3bcc0155d409e713db6d47b4252fb6991a08ffeefc0170ec.id.png)

Setelah diunduh, tambahkan ke direktori Resources proyek di Xcode.

![model](../../../../../translated_images/model.f0cb932ac2c7648211fbe5341ee1aa42b77cb7f956b6d9b084afb8fbf52927c7.id.png)

## **6. Menambahkan API C++ di ViewControllers**

> **Perhatian:**

- **a.** Tambahkan file header C++ yang sesuai ke proyek.

  ![Header File](../../../../../translated_images/head.2504a93b0be166afde6729fb193ebd14c5acb00a0bb6de1939b8a175b1f630fb.id.png)

- **b.** Sertakan `onnxruntime-genai` dynamic library in Xcode.

  ![Library](../../../../../translated_images/lib.86e12a925eb07e4e71a1466fa4f3ad27097e08505d25d34e98c33005d69b6f23.id.png)

- **c.** Use the C Samples code for testing. You can also add additional features like ChatUI for more functionality.

- **d.** Since you need to use C++ in your project, rename `ViewController.m` to `ViewController.mm` untuk mengaktifkan dukungan Objective-C++.

```objc

    NSString *llmPath = [[NSBundle mainBundle] resourcePath];
    char const *modelPath = llmPath.cString;

    auto model =  OgaModel::Create(modelPath);

    auto tokenizer = OgaTokenizer::Create(*model);

    const char* prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>Can you introduce yourself?<|end|><|assistant|>";

    auto sequences = OgaSequences::Create();
    tokenizer->Encode(prompt, *sequences);

    auto params = OgaGeneratorParams::Create(*model);
    params->SetSearchOption("max_length", 100);
    params->SetInputSequences(*sequences);

    auto output_sequences = model->Generate(*params);
    const auto output_sequence_length = output_sequences->SequenceCount(0);
    const auto* output_sequence_data = output_sequences->SequenceData(0);
    auto out_string = tokenizer->Decode(output_sequence_data, output_sequence_length);
    
    auto tmp = out_string;

```

## **7. Menjalankan Aplikasi**

Setelah pengaturan selesai, Anda dapat menjalankan aplikasi untuk melihat hasil inference model Phi-3-mini.

![Running Result](../../../../../translated_images/result.7ebd1fe614f809d776c46475275ec72e4ab898c4ec53ae62b29315c064ca6839.id.jpg)

Untuk kode contoh lebih lengkap dan petunjuk detail, kunjungi [Phi-3 Mini Samples repository](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios).

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau kesalahan interpretasi yang timbul dari penggunaan terjemahan ini.