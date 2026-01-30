# Phi3 finomhangolása Olive segítségével

Ebben a példában az Olive-t fogod használni, hogy:

1. Finomhangolj egy LoRA adaptert, amely a kifejezéseket Sad, Joy, Fear, Surprise kategóriákba sorolja.
1. Egyesítsd az adapter súlyait az alapmodellbe.
1. Optimalizáld és kvantáld a modellt `int4` formátumba.

Megmutatjuk azt is, hogyan lehet a finomhangolt modellt az ONNX Runtime (ORT) Generate API segítségével használni.

> **⚠️ A finomhangoláshoz megfelelő GPU szükséges – például A10, V100, A100.**

## 💾 Telepítés

Hozz létre egy új Python virtuális környezetet (például `conda` használatával):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Ezután telepítsd az Olive-t és a finomhangoláshoz szükséges függőségeket:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Phi3 finomhangolása Olive segítségével
Az [Olive konfigurációs fájl](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json) egy *workflow*-t tartalmaz a következő *lépésekkel*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

Magas szinten ez a folyamat a következőket végzi el:

1. Finomhangolja a Phi3-at (150 lépésig, amit módosíthatsz) a [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json) adatok alapján.
1. Egyesíti a LoRA adapter súlyait az alapmodellbe. Így egyetlen ONNX formátumú modell áll majd rendelkezésedre.
1. A Model Builder optimalizálja a modellt az ONNX runtime-hoz *és* kvantálja `int4` formátumba.

A workflow futtatásához használd a következőt:

```bash
olive run --config phrase-classification.json
```

Amikor az Olive befejezte, az optimalizált, `int4` finomhangolt Phi3 modell elérhető itt: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 A finomhangolt Phi3 integrálása az alkalmazásodba

Az alkalmazás futtatásához:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

A válasznak egyetlen szó szerinti osztályozásnak kell lennie a kifejezésre (Sad/Joy/Fear/Surprise).

**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén szakmai, emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.