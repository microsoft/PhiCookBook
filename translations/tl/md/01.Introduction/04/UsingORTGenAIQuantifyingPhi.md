# **Pag-Quantize ng Phi Family gamit ang Generative AI extensions para sa onnxruntime**

## **Ano ang Generative AI extensions para sa onnxruntime**

Ang extension na ito ay tumutulong sa iyo upang patakbuhin ang generative AI gamit ang ONNX Runtime( [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)). Nagbibigay ito ng generative AI loop para sa mga ONNX model, kabilang ang inference gamit ang ONNX Runtime, pagpoproseso ng logits, paghahanap at sampling, at pamamahala ng KV cache. Maaaring tawagan ng mga developer ang high level generate() method, o patakbuhin ang bawat pag-ulit ng modelo sa loop, lumilikha ng isang token sa bawat pagkakataon, at opsyonal na ina-update ang mga parameter ng generation sa loob ng loop. May suporta ito para sa greedy/beam search at TopP, TopK sampling upang makabuo ng mga token sequence at built-in na pagpoproseso ng logits tulad ng repetition penalties. Maaari ka ring madaling magdagdag ng custom scoring.

Sa antas ng aplikasyon, maaari mong gamitin ang Generative AI extensions para sa onnxruntime upang bumuo ng mga aplikasyon gamit ang C++/ C# / Python. Sa antas ng modelo, maaari mo itong gamitin upang pagsamahin ang mga fine-tuned na modelo at gawin ang mga kaugnay na quantitative deployment na gawain.


## **Pag-Quantize ng Phi-3.5 gamit ang Generative AI extensions para sa onnxruntime**

### **Mga Sinusuportahang Modelo**

Sinusuportahan ng Generative AI extensions para sa onnxruntime ang conversion ng quantization ng Microsoft Phi, Google Gemma, Mistral, Meta LLaMA。


### **Model Builder sa Generative AI extensions para sa onnxruntime**

Malaki ang pabilisin ng model builder sa paggawa ng mga optimized at na-quantize na ONNX model na tumatakbo gamit ang ONNX Runtime generate() API.

Sa pamamagitan ng Model Builder, maaari mong i-quantize ang modelo sa INT4, INT8, FP16, FP32, at pagsamahin ang iba't ibang hardware acceleration methods tulad ng CPU, CUDA, DirectML, Mobile, atbp.

Upang magamit ang Model Builder kailangan mong i-install

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

Pagkatapos ng pag-install, maaari mong patakbuhin ang Model Builder script mula sa terminal upang isagawa ang pag-convert ng format ng modelo at quantization.


```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

Unawain ang mga kaugnay na parameter

1. **model_name** Ito ang modelo sa Hugging face, tulad ng microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct, atbp. Maaari rin itong ang path kung saan mo iniimbak ang modelo

2. **path_to_output_folder** Path ng pag-save ng quantized na conversion

3. **execution_provider** Iba't ibang suporta sa hardware acceleration, tulad ng cpu, cuda, DirectML

4. **cache_dir_to_save_hf_files** Dina-download namin ang modelo mula sa Hugging face at kino-cache ito locally




***Tandaan：*** <ul>Bagaman ang Generative AI extensions para sa onnxruntime ay nasa preview pa, ito ay isinama na sa Microsoft Olive, at maaari mo ring tawagan ang mga function ng Generative AI extensions para sa onnxruntime Model Builder sa pamamagitan ng Microsoft Olive.</ul>

## **Paano gamitin ang Model Builder para mag-quantize ng Phi-3.5**

Suportado ng Model Builder ngayon ang ONNX model quantization para sa Phi-3.5 Instruct at Phi-3.5-Vision

### **Phi-3.5-Instruct**


**CPU accelerated conversion ng quantized INT 4**


```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**CUDA accelerated conversion ng quantized INT 4**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```



```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```


### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. Itakda ang environment sa terminal

```bash

mkdir models

cd models 

```

2. I-download ang microsoft/Phi-3.5-vision-instruct sa models folder
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. Mangyaring i-download ang mga file na ito sa iyong Phi-3.5-vision-instruct folder

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)


4. I-download ang file na ito sa models folder
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. Pumunta sa terminal

    I-convert ang ONNX support gamit ang FP32


```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```


### **Tandaan：**

1. Sa kasalukuyan, sinusuportahan ng Model Builder ang conversion para sa Phi-3.5-Instruct at Phi-3.5-Vision, ngunit hindi para sa Phi-3.5-MoE

2. Upang magamit ang quantized na modelo ng ONNX, maaari mo itong gamitin sa pamamagitan ng Generative AI extensions para sa onnxruntime SDK

3. Kailangan nating isaalang-alang ang mas responsableng AI, kaya pagkatapos ng pag-quantize ng modelo, inirerekomenda na magsagawa ng mas epektibong pagsusuri ng resulta

4. Sa pamamagitan ng pag-quantize ng CPU INT4 na modelo, maaari natin itong i-deploy sa Edge Device, na may mas magagandang senaryo ng aplikasyon, kaya nakumpleto na natin ang Phi-3.5-Instruct sa paligid ng INT 4


## **Mga Resources**

1. Matuto nang higit pa tungkol sa Generative AI extensions para sa onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Generative AI extensions para sa onnxruntime GitHub Repo [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->