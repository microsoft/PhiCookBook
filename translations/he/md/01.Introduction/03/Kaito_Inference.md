<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e46691923dca7cb2f11d32b1d9d558e0",
  "translation_date": "2025-05-09T11:55:49+00:00",
  "source_file": "md/01.Introduction/03/Kaito_Inference.md",
  "language_code": "he"
}
-->
## הסקה עם Kaito

[Kaito](https://github.com/Azure/kaito) הוא אופרטור שמבצע אוטומציה לפריסת מודלים של הסקה בינה מלאכותית/למידת מכונה בתוך אשכול Kubernetes.

ל-Kaito יש הבדלים מרכזיים בהשוואה לרוב שיטות הפריסה הרגילות שמבוססות על תשתיות של מכונות וירטואליות:

- ניהול קבצי מודל באמצעות תמונות קונטיינר. מסופק שרת HTTP לביצוע קריאות הסקה דרך ספריית המודל.
- הימנעות מכיוונון פרמטרי פריסה כדי להתאים לחומרת GPU, באמצעות תצורות מוגדרות מראש.
- אספקת צמתים עם GPU באופן אוטומטי בהתאם לדרישות המודל.
- אחסון תמונות מודל גדולות ברישום הציבורי של Microsoft Container Registry (MCR) במידה והרישיון מאפשר זאת.

באמצעות Kaito, תהליך ההטמעה של מודלים גדולים להסקה בתוך Kubernetes הופך לפשוט בהרבה.


## ארכיטקטורה

Kaito פועל לפי דפוס העיצוב הקלאסי של Kubernetes Custom Resource Definition (CRD) ושל בקר (controller). המשתמש מנהל משאב מותאם אישית `workspace` שמתאר את דרישות ה-GPU ואת מפרט ההסקה. בקרי Kaito יבצעו אוטומציה לפריסה באמצעות התאמת המשאב המותאם `workspace`.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

האיור למעלה מציג סקירה של ארכיטקטורת Kaito. הרכיבים המרכזיים שלו כוללים:

- **בקר Workspace**: מבצע התאמה של המשאב המותאם `workspace`, יוצר משאבים מותאמים של `machine` (מוסבר בהמשך) כדי להפעיל אספקת צמתים אוטומטית, ויוצר את עומס העבודה של ההסקה (`deployment` או `statefulset`) בהתבסס על התצורות המוגדרות מראש של המודל.
- **בקר אספקת צמתים**: שם הבקר הוא *gpu-provisioner* ב-[gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). הוא משתמש ב-CRD של `machine` שמקורו ב-[Karpenter](https://sigs.k8s.io/karpenter) כדי לתקשר עם בקר ה-Workspace. הוא משתלב עם APIs של Azure Kubernetes Service (AKS) להוספת צמתים עם GPU חדשים לאשכול AKS.
> [!NOTE]  [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) הוא רכיב בקוד פתוח. ניתן להחליפו בבקרים אחרים אם הם תומכים ב-APIs של [Karpenter-core](https://sigs.k8s.io/karpenter).


## התקנה

אנא עיינו בהנחיות ההתקנה [כאן](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## התחלה מהירה הסקה Phi-3
[קוד דוגמה להסקה Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

```
apiVersion: kaito.sh/v1alpha1
kind: Workspace
metadata:
  name: workspace-phi-3-mini
resource:
  instanceType: "Standard_NC6s_v3"
  labelSelector:
    matchLabels:
      apps: phi-3
inference:
  preset:
    name: phi-3-mini-4k-instruct
    # Note: This configuration also works with the phi-3-mini-128k-instruct preset
```

```sh
$ cat examples/inference/kaito_workspace_phi_3.yaml

apiVersion: kaito.sh/v1alpha1
kind: Workspace
metadata:
  name: workspace-phi-3-mini
resource:
  instanceType: "Standard_NC6s_v3"
  labelSelector:
    matchLabels:
      app: phi-3-adapter
tuning:
  preset:
    name: phi-3-mini-4k-instruct
  method: qlora
  input:
    urls:
      - "https://huggingface.co/datasets/philschmid/dolly-15k-oai-style/resolve/main/data/train-00000-of-00001-54e3756291ca09c6.parquet?download=true"
  output:
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Tuning Output ACR Path
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3.yaml
```

ניתן לעקוב אחרי מצב ה-Workspace על ידי הרצת הפקודה הבאה. כאשר העמודה WORKSPACEREADY הופכת ל-`True`, המודל הוטמע בהצלחה.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

לאחר מכן, ניתן למצוא את כתובת ה-IP של שירות ההסקה באשכול ולהשתמש בפוד `curl` זמני כדי לבדוק את נקודת הקצה של השירות באשכול.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## התחלה מהירה הסקה Phi-3 עם מתאמים

לאחר התקנת Kaito, ניתן לנסות את הפקודות הבאות כדי להפעיל שירות הסקה.

[קוד דוגמה להסקה Phi-3 עם מתאמים](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

```
apiVersion: kaito.sh/v1alpha1
kind: Workspace
metadata:
  name: workspace-phi-3-mini-adapter
resource:
  instanceType: "Standard_NC6s_v3"
  labelSelector:
    matchLabels:
      apps: phi-3-adapter
inference:
  preset:
    name: phi-3-mini-128k-instruct
  adapters:
    - source:
        name: "phi-3-adapter"
        image: "ACR_REPO_HERE.azurecr.io/ADAPTER_HERE:0.0.1"
      strength: "1.0"
```

```sh
$ cat examples/inference/kaito_workspace_phi_3_with_adapters.yaml

apiVersion: kaito.sh/v1alpha1
kind: Workspace
metadata:
  name: workspace-phi-3-mini-adapter
resource:
  instanceType: "Standard_NC6s_v3"
  labelSelector:
    matchLabels:
      app: phi-3-adapter
tuning:
  preset:
    name: phi-3-mini-128k-instruct
  method: qlora
  input:
    urls:
      - "https://huggingface.co/datasets/philschmid/dolly-15k-oai-style/resolve/main/data/train-00000-of-00001-54e3756291ca09c6.parquet?download=true"
  output:
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Tuning Output ACR Path
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3_with_adapters.yaml
```

ניתן לעקוב אחרי מצב ה-Workspace על ידי הרצת הפקודה הבאה. כאשר העמודה WORKSPACEREADY הופכת ל-`True`, המודל הוטמע בהצלחה.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

לאחר מכן, ניתן למצוא את כתובת ה-IP של שירות ההסקה באשכול ולהשתמש בפוד `curl` זמני כדי לבדוק את נקודת הקצה של השירות באשכול.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור שלו צריך להיחשב כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי אנושי. אנו לא נושאים באחריות לכל אי הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.