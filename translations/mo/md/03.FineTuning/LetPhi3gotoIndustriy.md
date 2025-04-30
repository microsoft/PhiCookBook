<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ef0e3b9f4e65cc05e80efb30723aed40",
  "translation_date": "2025-04-04T13:34:46+00:00",
  "source_file": "md\\03.FineTuning\\LetPhi3gotoIndustriy.md",
  "language_code": "mo"
}
-->
# **Phi-3 ko ek udyojak visheshagya banayein**

Phi-3 model ko kisi udhyog mein lagane ke liye, aapko Phi-3 model mein udhyog ke vyaparik data ko jodna hoga. Iske liye do alag-alag vikalp hain: pehla hai RAG (Retrieval Augmented Generation) aur doosra hai Fine-Tuning.

## **RAG aur Fine-Tuning ke beech antar**

### **Retrieval Augmented Generation**

RAG ek data retrieval aur text generation ka sanyojan hai. Udhyog ke sanrachit aur asanrachit data ko vector database mein rakha jata hai. Jab sambandhit samagri ki khoj hoti hai, to ek prasang banane ke liye sambandhit sankshipt aur samagri ko dhundha jata hai, aur LLM/SLM ki text completion kshamata ke saath samagri utpadan kiya jata hai.

### **Fine-Tuning**

Fine-Tuning ek model ke sudhar par adharit hai. Ismein model algorithm se shuruaat karne ki zarurat nahi hoti, lekin data ko nirantar ikattha karna padta hai. Agar aapko udhyogik upyog mein zyada sahi terminology aur bhaasha vyaktikaran chahiye, to Fine-Tuning behtar vikalp hai. Lekin agar aapka data aksar badalta hai, to Fine-Tuning kathin ho sakta hai.

### **Kaise chunenge**

1. Agar humare jawab mein baahari data ka parichay zaruri ho, to RAG sabse behtar vikalp hai.

2. Agar aapko sthir aur sahi udhyogik gyaan ka nirmaan karna ho, to Fine-Tuning ek accha vikalp hoga. RAG pramukh roop se sambandhit samagri ko prapt karta hai, lekin hamesha vishesh nuances ko sahi nahi kar pata.

3. Fine-Tuning ke liye ek uch-gunvaatta wala data set zaruri hota hai, aur agar data ka kshetra chhota ho, to iska zyada antar nahi padta. RAG zyada lachakdaar hota hai.

4. Fine-Tuning ek "black box" hai, ek metaphysics hai, aur iska antarik mechanism samajhna kathin hota hai. Lekin RAG data ke source ko dhundhne mein asaanai karta hai, jiski wajah se hallucinations ya samagri ki galtiyon ko sudharna aur transparency badhane mein madad milti hai.

### **Prayog ke sthiti**

1. Vertical udhyogon mein vishesh vyavsayik shabdavali aur vyaktikaran ki zarurat hoti hai, ***Fine-Tuning*** sabse behtar vikalp hoga.

2. QA system, jo alag-alag gyaan binduon ke synthesis mein laga ho, ***RAG*** sabse behtar vikalp hoga.

3. Automated vyapar pravah ke sanyojan mein ***RAG + Fine-Tuning*** sabse behtar vikalp hoga.

## **RAG ka upyog kaise karein**

![rag](../../../../translated_images/rag.36e7cb856f120334d577fde60c6a5d7c5eecae255dac387669303d30b4b3efa4.mo.png)

Ek vector database ek sangrah hai jo data ko ganitiya roop mein rakhta hai. Vector database machine learning models ko pehle ke inputs ko yaad rakhne mein asaanai karta hai, jo search, recommendations, aur text generation jaise upyogon ko samarthan karne ke liye machine learning ka upyog karta hai. Data ko exact matches ke bajaye similarity metrics ke aadhar par pahchana ja sakta hai, jo computer models ko data ke prasang ko samajhne mein madad karta hai.

Vector database RAG ko sakriya karne ka mool hai. Hum text-embedding-3, jina-ai-embedding jaise vector models ke madhyam se data ko vector storage mein parivartit kar sakte hain.

RAG application banane ke baare mein adhik jankari ke liye [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?WT.mc_id=aiml-138114-kinfeylo) par jaayein.

## **Fine-Tuning ka upyog kaise karein**

Fine-Tuning mein commonly upyog kiye jaane wale algorithms hain Lora aur QLora. Kaise chunenge?
- [Is sample notebook ke madhyam se adhik seekhein](../../../../code/04.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python FineTuning Sample ka udaharan](../../../../code/04.Finetuning/FineTrainingScript.py)

### **Lora aur QLora**

![lora](../../../../translated_images/qlora.6aeba71122bc0c8d56ccf0bc36b861304939fee087f43c1fc6cc5c9cb8764725.mo.png)

LoRA (Low-Rank Adaptation) aur QLoRA (Quantized Low-Rank Adaptation) dono techniques hain jo bade bhaasha models (LLMs) ko Parameter Efficient Fine Tuning (PEFT) ke madhyam se fine-tune karte hain. PEFT techniques models ko traditional methods se zyada prabhavit roop se train karne ke liye design ki gayi hain.  
LoRA ek standalone finetuning technique hai jo weight update matrix par ek low-rank approximation lagakar memory footprint ko kam karta hai. Ye tezi se training karta hai aur performance ko traditional fine-tuning methods ke kareeb rakhta hai.  

QLoRA LoRA ka ek extended version hai jo quantization techniques ko shamil karta hai, memory usage ko aur kam karne ke liye. QLoRA pre-trained LLM ke weight parameters ko 4-bit precision mein quantize karta hai, jo LoRA se zyada memory efficient hai. Lekin QLoRA training LoRA training ke mukable lagbhag 30% dheema hota hai quantization aur dequantization steps ke karan.  

QLoRA LoRA ka upyog karta hai quantization errors ko sudharne ke liye. QLoRA massive models ko, jo billion parameters rakhte hain, relatively chhoti aur aasani se uplabdh GPUs par fine-tune karne mein saksham banata hai. Udaharan ke roop mein, QLoRA ek 70B parameter model ko fine-tune kar sakta hai jo 36 GPUs ki zarurat karta hai sirf 2 GPUs ke saath.

It seems you would like this text translated to "mo." Could you clarify what "mo" refers to? Are you referring to a specific language or dialect? For example, it could mean Māori, Mandarin, or something else entirely. Let me know so I can assist you effectively!