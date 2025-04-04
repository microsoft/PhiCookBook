<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ffeb840575ff03dea81d2b2214f2e000",
  "translation_date": "2025-04-04T12:00:29+00:00",
  "source_file": "md\\01.Introduction\\03\\iOS_Inference.md",
  "language_code": "mo"
}
-->
# **Inference Phi-3 in iOS**

Phi-3-mini adalah seri model baru dari Microsoft yang memungkinkan penerapan Large Language Models (LLMs) pada perangkat edge dan perangkat IoT. Phi-3-mini tersedia untuk penerapan di iOS, Android, dan perangkat edge, memungkinkan AI generatif diterapkan dalam lingkungan BYOD. Contoh berikut menunjukkan cara menerapkan Phi-3-mini di iOS.

## **1. Persiapan**

- **a.** macOS 14+
- **b.** Xcode 15+
- **c.** iOS SDK 17.x (iPhone 14 A16 atau lebih tinggi)
- **d.** Instal Python 3.10+ (disarankan menggunakan Conda)
- **e.** Instal pustaka Python: `python-flatbuffers`
- **f.** Instal CMake

### Semantic Kernel dan Inferensi

Semantic Kernel adalah kerangka kerja aplikasi yang memungkinkan Anda membuat aplikasi yang kompatibel dengan Azure OpenAI Service, model OpenAI, dan bahkan model lokal. Mengakses layanan lokal melalui Semantic Kernel mempermudah integrasi dengan server model Phi-3-mini yang Anda host sendiri.

### Memanggil Model Kuantisasi dengan Ollama atau LlamaEdge

Banyak pengguna lebih suka menggunakan model kuantisasi untuk menjalankan model secara lokal. [Ollama](https://ollama.com) dan [LlamaEdge](https://llamaedge.com) memungkinkan pengguna untuk memanggil berbagai model kuantisasi:

#### **Ollama**

Anda dapat menjalankan `ollama run phi3` langsung atau mengonfigurasinya secara offline. Buat Modelfile dengan path ke file `gguf` Anda. Contoh kode untuk menjalankan model kuantisasi Phi-3-mini:

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

#### **LlamaEdge**

Jika Anda ingin menggunakan `gguf` di perangkat cloud dan edge secara bersamaan, LlamaEdge adalah pilihan yang bagus.

## **2. Mengompilasi ONNX Runtime untuk iOS**

```bash

git clone https://github.com/microsoft/onnxruntime.git

cd onnxruntime

./build.sh --build_shared_lib --ios --skip_tests --parallel --build_dir ./build_ios --ios --apple_sysroot iphoneos --osx_arch arm64 --apple_deploy_target 17.5 --cmake_generator Xcode --config Release

cd ../

```

### **Catatan**

- **a.** Sebelum mengompilasi, pastikan Xcode dikonfigurasi dengan benar dan atur sebagai direktori pengembang aktif di terminal:

    ```bash
    sudo xcode-select -switch /Applications/Xcode.app/Contents/Developer
    ```

- **b.** ONNX Runtime perlu dikompilasi untuk berbagai platform. Untuk iOS, Anda dapat mengompilasi untuk `arm64` or `x86_64`.

- **c.** Disarankan menggunakan SDK iOS terbaru untuk kompilasi. Namun, Anda juga dapat menggunakan versi yang lebih lama jika membutuhkan kompatibilitas dengan SDK sebelumnya.

## **3. Mengompilasi AI Generatif dengan ONNX Runtime untuk iOS**

> **Catatan:** Karena AI Generatif dengan ONNX Runtime masih dalam tahap pratinjau, harap perhatikan kemungkinan adanya perubahan.

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

Saya memilih Objective-C sebagai metode pengembangan aplikasi, karena menggunakan API C++ ONNX Runtime untuk AI Generatif, Objective-C lebih kompatibel. Tentu saja, Anda juga dapat menyelesaikan pemanggilan terkait melalui bridging Swift.

![xcode](../../../../../translated_images/xcode.6c67033ca85b703e80cc51ecaa681fbcb6ac63cc0c256705ac97bc9ca039c235.mo.png)

## **5. Menyalin model ONNX kuantisasi INT4 ke proyek aplikasi App**

Kita perlu mengimpor model kuantisasi INT4 dalam format ONNX, yang harus diunduh terlebih dahulu.

![hf](../../../../../translated_images/hf.b99941885c6561bb3bcc0155d409e713db6d47b4252fb6991a08ffeefc0170ec.mo.png)

Setelah diunduh, Anda perlu menambahkannya ke direktori Resources proyek di Xcode.

![model](../../../../../translated_images/model.f0cb932ac2c7648211fbe5341ee1aa42b77cb7f956b6d9b084afb8fbf52927c7.mo.png)

## **6. Menambahkan API C++ di ViewControllers**

> **Catatan:**

- **a.** Tambahkan file header C++ yang sesuai ke proyek.

  ![Header File](../../../../../translated_images/head.2504a93b0be166afde6729fb193ebd14c5acb00a0bb6de1939b8a175b1f630fb.mo.png)

- **b.** Sertakan `onnxruntime-genai` dynamic library in Xcode.

  ![Library](../../../../../translated_images/lib.86e12a925eb07e4e71a1466fa4f3ad27097e08505d25d34e98c33005d69b6f23.mo.png)

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

Setelah pengaturan selesai, Anda dapat menjalankan aplikasi untuk melihat hasil inferensi model Phi-3-mini.

![Running Result](../../../../../translated_images/result.7ebd1fe614f809d776c46475275ec72e4ab898c4ec53ae62b29315c064ca6839.mo.jpg)

Untuk lebih banyak contoh kode dan petunjuk rinci, kunjungi [Phi-3 Mini Samples repository](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios).

It seems like "mo" isn't a recognized language or abbreviation. Could you clarify what language you're referring to? For example, do you mean Maori, Mongolian, or something else? Let me know so I can assist you better!