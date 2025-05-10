<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e08ce816e23ad813244a09ca34ebb8ac",
  "translation_date": "2025-05-09T10:15:37+00:00",
  "source_file": "md/01.Introduction/03/AIPC_Inference.md",
  "language_code": "tr"
}
-->
# **AI PC'de Phi-3 Çıkarımı**

Üretken yapay zekâdaki ilerlemeler ve uç cihaz donanım kapasitelerindeki gelişmelerle birlikte, artık daha fazla sayıda üretken yapay zekâ modeli kullanıcıların Kendi Cihazını Getir (BYOD) cihazlarına entegre edilebiliyor. AI PC’ler de bu modeller arasında yer alıyor. 2024 itibarıyla Intel, AMD ve Qualcomm, PC üreticileriyle iş birliği yaparak donanım değişiklikleriyle yerel üretken yapay zekâ modellerinin dağıtımını kolaylaştıran AI PC’leri tanıttı. Bu yazıda, Intel AI PC’lerine odaklanarak Phi-3 modelinin Intel AI PC üzerinde nasıl çalıştırılacağını inceleyeceğiz.

### NPU Nedir?

NPU (Sinir İşlem Birimi), sinir ağı işlemlerini ve yapay zekâ görevlerini hızlandırmak için tasarlanmış, daha büyük bir SoC üzerindeki özel bir işlemci veya işlem birimidir. Genel amaçlı CPU ve GPU'lardan farklı olarak, NPU'lar veri odaklı paralel hesaplama için optimize edilmiştir; bu da onları video ve resim gibi büyük multimedya verilerini ve sinir ağları için verileri işleme konusunda son derece verimli kılar. Konuşma tanıma, video görüşmelerde arka plan bulanıklığı ve nesne tespiti gibi fotoğraf veya video düzenleme işlemleri gibi yapay zekâ ile ilgili görevlerde özellikle başarılıdırlar.

## NPU ve GPU Karşılaştırması

Birçok yapay zekâ ve makine öğrenimi işi GPU’lar üzerinde çalışırken, GPU ve NPU arasında önemli bir fark vardır.  
GPU’lar paralel hesaplama yetenekleriyle bilinir, ancak tüm GPU’lar grafik işlemenin ötesinde aynı verimlilikte değildir. NPU’lar ise sinir ağı işlemlerinde yer alan karmaşık hesaplamalar için özel olarak tasarlanmıştır ve bu nedenle yapay zekâ görevlerinde çok daha etkilidir.

Özetle, NPU’lar yapay zekâ hesaplamalarını hızlandıran matematik uzmanlarıdır ve AI PC’lerin yükselen döneminde önemli bir rol oynarlar!

***Bu örnek, Intel’in en yeni Intel Core Ultra İşlemcisi temel alınarak hazırlanmıştır***

## **1. Phi-3 Modelini Çalıştırmak için NPU Kullanımı**

Intel® NPU cihazı, Intel® Core™ Ultra nesil CPU’lardan itibaren (önceden Meteor Lake olarak bilinen) Intel istemci CPU’larına entegre edilmiş bir yapay zekâ çıkarım hızlandırıcısıdır. Yapay sinir ağı görevlerinin enerji verimli şekilde yürütülmesini sağlar.

![Latency](../../../../../translated_images/aipcphitokenlatency.446d244d43a98a99f001e6eb55b421ab7ebc0b5d8f93fad8458da46cf263bfad.tr.png)

![Latency770](../../../../../translated_images/aipcphitokenlatency770.862269853961e495131e9465fdb06c2c7b94395b83729dc498cfc077e02caade.tr.png)

**Intel NPU Hızlandırma Kütüphanesi**

Intel NPU Hızlandırma Kütüphanesi [https://github.com/intel/intel-npu-acceleration-library](https://github.com/intel/intel-npu-acceleration-library), Intel Sinir İşlem Birimi’nin (NPU) gücünden yararlanarak uyumlu donanım üzerinde yüksek hızlı hesaplamalar yapmanızı sağlayan bir Python kütüphanesidir.

Intel® Core™ Ultra işlemcilerle güçlendirilmiş AI PC’de Phi-3-mini örneği.

![DemoPhiIntelAIPC](../../../../../imgs/01/03/AIPC/aipcphi3-mini.gif)

Python Kütüphanesini pip ile kurun

```bash

   pip install intel-npu-acceleration-library

```

***Not*** Proje hâlâ geliştirme aşamasında, ancak referans model oldukça tamamlanmış durumda.

### **Intel NPU Hızlandırma Kütüphanesi ile Phi-3’ü Çalıştırmak**

Intel NPU hızlandırması kullanılırken, bu kütüphane geleneksel kodlama sürecini etkilemez. Sadece orijinal Phi-3 modelini FP16, INT8, INT4 gibi formatlarda kuantize etmek için bu kütüphaneyi kullanmanız gerekir.

```python
from transformers import AutoTokenizer, pipeline,TextStreamer
from intel_npu_acceleration_library import NPUModelForCausalLM, int4
from intel_npu_acceleration_library.compiler import CompilerConfig
import warnings

model_id = "microsoft/Phi-3-mini-4k-instruct"

compiler_conf = CompilerConfig(dtype=int4)
model = NPUModelForCausalLM.from_pretrained(
    model_id, use_cache=True, config=compiler_conf, attn_implementation="sdpa"
).eval()

tokenizer = AutoTokenizer.from_pretrained(model_id)

text_streamer = TextStreamer(tokenizer, skip_prompt=True)
```

Kuantizasyon başarılı olduktan sonra, Phi-3 modelini çalıştırmak için NPU’yu çağırmaya devam edin.

```python
generation_args = {
   "max_new_tokens": 1024,
   "return_full_text": False,
   "temperature": 0.3,
   "do_sample": False,
   "streamer": text_streamer,
}

pipe = pipeline(
   "text-generation",
   model=model,
   tokenizer=tokenizer,
)

query = "<|system|>You are a helpful AI assistant.<|end|><|user|>Can you introduce yourself?<|end|><|assistant|>"

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    pipe(query, **generation_args)
```

Kod çalışırken, Görev Yöneticisi üzerinden NPU’nun çalışma durumunu izleyebiliriz.

![NPU](../../../../../translated_images/aipc_NPU.f047860f84f5bb5b183756f23b4b8506485e862ea34c6a53c58988707c23bc80.tr.png)

***Örnekler*** : [AIPC_NPU_DEMO.ipynb](../../../../../code/03.Inference/AIPC/AIPC_NPU_DEMO.ipynb)

## **2. Phi-3 Modelini Çalıştırmak için DirectML + ONNX Runtime Kullanımı**

### **DirectML Nedir**

[DirectML](https://github.com/microsoft/DirectML), makine öğrenimi için yüksek performanslı, donanım hızlandırmalı bir DirectX 12 kütüphanesidir. DirectML, AMD, Intel, NVIDIA ve Qualcomm gibi üreticilerin tüm DirectX 12 destekli GPU’ları dahil olmak üzere geniş bir donanım ve sürücü yelpazesinde yaygın makine öğrenimi görevlerine GPU hızlandırması sağlar.

Tek başına kullanıldığında, DirectML API’si düşük seviyeli bir DirectX 12 kütüphanesidir ve framework’ler, oyunlar ve diğer gerçek zamanlı uygulamalar gibi yüksek performanslı, düşük gecikmeli uygulamalar için uygundur. DirectML’in Direct3D 12 ile sorunsuz çalışması, düşük yükü ve donanım genelinde uyumluluğu, yüksek performans ve donanımda güvenilirlik gerektiren makine öğrenimi hızlandırmaları için ideal kılar.

***Not*** : En son DirectML sürümü artık NPU desteği sunmaktadır (https://devblogs.microsoft.com/directx/introducing-neural-processor-unit-npu-support-in-directml-developer-preview/)

### DirectML ve CUDA'nın Yetkinlikleri ve Performansları

**DirectML**, Microsoft tarafından geliştirilen bir makine öğrenimi kütüphanesidir. Windows cihazlarda, masaüstü, dizüstü ve uç cihazlar dahil olmak üzere makine öğrenimi iş yüklerini hızlandırmak için tasarlanmıştır.  
- DX12 Tabanlı: DirectML, DirectX 12 (DX12) üzerine inşa edilmiştir ve NVIDIA ile AMD dahil olmak üzere geniş GPU desteği sunar.  
- Daha Geniş Destek: DX12 kullandığı için, DirectML DX12 destekleyen tüm GPU’larla, entegre GPU’lar dahil, çalışabilir.  
- Görüntü İşleme: DirectML, görüntü tanıma, nesne tespiti gibi görevler için sinir ağlarıyla görüntü ve diğer verileri işler.  
- Kurulum Kolaylığı: DirectML kurulumu basittir ve GPU üreticilerinden özel SDK veya kütüphane gerektirmez.  
- Performans: Bazı durumlarda, özellikle belirli iş yüklerinde CUDA’dan daha hızlı çalışabilir.  
- Sınırlamalar: Float16 büyük partiler için ise bazen daha yavaş olabilir.

**CUDA**, NVIDIA’nın paralel hesaplama platformu ve programlama modelidir. Geliştiricilerin NVIDIA GPU’ların gücünü genel amaçlı hesaplamalar için kullanmasını sağlar.  
- NVIDIA’ya Özel: CUDA, NVIDIA GPU’larla sıkı entegredir ve özel olarak onlar için tasarlanmıştır.  
- Yüksek Optimizasyon: GPU hızlandırmalı görevlerde, özellikle NVIDIA GPU’larda mükemmel performans sağlar.  
- Yaygın Kullanım: TensorFlow ve PyTorch gibi birçok makine öğrenimi framework’ü CUDA desteğine sahiptir.  
- Özelleştirme: Geliştiriciler, CUDA ayarlarını belirli görevler için optimize edebilir, bu da en iyi performansı sağlar.  
- Sınırlamalar: Ancak, CUDA’nın NVIDIA donanımına bağımlılığı, farklı GPU’larla geniş uyumluluğu kısıtlayabilir.

### DirectML ve CUDA Arasında Seçim Yapmak

DirectML ve CUDA arasında seçim, kullanım senaryonuza, donanımınıza ve tercihinize bağlıdır.  
Daha geniş uyumluluk ve kolay kurulum istiyorsanız, DirectML iyi bir seçenek olabilir. Ancak NVIDIA GPU’larınız varsa ve yüksek optimize performans gerekiyorsa, CUDA güçlü bir tercih olmaya devam eder. Özetle, her iki teknoloji de güçlü ve zayıf yönlere sahip; karar verirken gereksinimlerinizi ve mevcut donanımınızı göz önünde bulundurun.

### **ONNX Runtime ile Üretken Yapay Zekâ**

Yapay zekâ çağında, AI modellerinin taşınabilirliği çok önemlidir. ONNX Runtime, eğitilmiş modelleri farklı cihazlara kolayca dağıtabilir. Geliştiriciler, çıkarım framework’üne odaklanmadan, tek bir API kullanarak model çıkarımı yapabilir. Üretken yapay zekâ çağında, ONNX Runtime kod optimizasyonu da gerçekleştirmiştir (https://onnxruntime.ai/docs/genai/). Optimizasyonlu ONNX Runtime sayesinde, kuantize edilmiş üretken yapay zekâ modelleri farklı cihazlarda çıkarım yapabilir. ONNX Runtime ile üretken yapay zekâda, Python, C#, C / C++ üzerinden model çıkarımı yapılabilir. Elbette, iPhone üzerinde dağıtımda C++’ın ONNX Runtime API’sinden faydalanılabilir.

[Örnek Kod](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx)

***ONNX Runtime üretken yapay zekâ kütüphanesini derleyin***

```bash

winget install --id=Kitware.CMake  -e

git clone https://github.com/microsoft/onnxruntime.git

cd .\onnxruntime\

./build.bat --build_shared_lib --skip_tests --parallel --use_dml --config Release

cd ../

git clone https://github.com/microsoft/onnxruntime-genai.git

cd .\onnxruntime-genai\

mkdir ort

cd ort

mkdir include

mkdir lib

copy ..\onnxruntime\include\onnxruntime\core\providers\dml\dml_provider_factory.h ort\include

copy ..\onnxruntime\include\onnxruntime\core\session\onnxruntime_c_api.h ort\include

copy ..\onnxruntime\build\Windows\Release\Release\*.dll ort\lib

copy ..\onnxruntime\build\Windows\Release\Release\onnxruntime.lib ort\lib

python build.py --use_dml


```

**Kütüphaneyi yükleyin**

```bash

pip install .\onnxruntime_genai_directml-0.3.0.dev0-cp310-cp310-win_amd64.whl

```

Çalıştırma sonucu bu şekildedir

![DML](../../../../../translated_images/aipc_DML.dd810ee1f3882323c131b39065ed0cf41bbe0aaa8d346a0d6d290c20f5c0bf75.tr.png)

***Örnekler*** : [AIPC_DirectML_DEMO.ipynb](../../../../../code/03.Inference/AIPC/AIPC_DirectML_DEMO.ipynb)

## **3. Phi-3 Modelini Çalıştırmak için Intel OpenVino Kullanımı**

### **OpenVINO Nedir**

[OpenVINO](https://github.com/openvinotoolkit/openvino), derin öğrenme modellerini optimize etmek ve dağıtmak için açık kaynaklı bir araç setidir. TensorFlow, PyTorch gibi popüler framework’lerden gelen görsel, ses ve dil modelleri için artırılmış derin öğrenme performansı sağlar. OpenVINO ile başlayın. OpenVINO ayrıca CPU ve GPU ile birlikte Phi-3 modelini çalıştırmak için de kullanılabilir.

***Not***: Şu anda OpenVINO NPU desteği sağlamamaktadır.

### **OpenVINO Kütüphanesini Kurma**

```bash

 pip install git+https://github.com/huggingface/optimum-intel.git

 pip install git+https://github.com/openvinotoolkit/nncf.git

 pip install openvino-nightly

```

### **OpenVINO ile Phi-3’ü Çalıştırmak**

NPU gibi, OpenVINO da üretken yapay zekâ modellerinin çağrısını kuantize modelleri çalıştırarak tamamlar. Öncelikle Phi-3 modelini kuantize etmemiz gerekir ve optimum-cli aracılığıyla komut satırında model kuantizasyonunu tamamlarız.

**INT4**

```bash

optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code ./openvinomodel/phi3/int4

```

**FP16**

```bash

optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format fp16 --trust-remote-code ./openvinomodel/phi3/fp16

```

Dönüştürülmüş format şu şekildedir

![openvino_convert](../../../../../translated_images/aipc_OpenVINO_convert.bd70cf3d87e65a923d2d663f559a03d86227ab71071802355a6cfeaf80eb7042.tr.png)

Model yollarını (model_dir), ilgili konfigürasyonları (ov_config = {"PERFORMANCE_HINT": "LATENCY", "NUM_STREAMS": "1", "CACHE_DIR": ""}) ve donanım hızlandırmalı cihazları (GPU.0) OVModelForCausalLM üzerinden yükleyin

```python

ov_model = OVModelForCausalLM.from_pretrained(
     model_dir,
     device='GPU.0',
     ov_config=ov_config,
     config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
     trust_remote_code=True,
)

```

Kod çalışırken, Görev Yöneticisi üzerinden GPU’nun çalışma durumunu izleyebiliriz

![openvino_gpu](../../../../../translated_images/aipc_OpenVINO_GPU.142b31f25c5ffcf8802077629d11fbae275e53aeeb0752e0cdccf826feca6875.tr.png)

***Örnekler*** : [AIPC_OpenVino_Demo.ipynb](../../../../../code/03.Inference/AIPC/AIPC_OpenVino_Demo.ipynb)

### ***Not*** : Yukarıdaki üç yöntemin her birinin kendi avantajları vardır, ancak AI PC çıkarımı için NPU hızlandırması kullanılması önerilir.

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucunda ortaya çıkabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.