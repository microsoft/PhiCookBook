<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aca91084bc440431571e00bf30d96ab8",
  "translation_date": "2026-01-05T08:47:21+00:00",
  "source_file": "md/01.Introduction/03/Kaito_Inference.md",
  "language_code": "he"
}
-->
## הסקה עם Kaito

[Kaito](https://github.com/Azure/kaito) הוא אופרטור שמאוטומט את פריסת מודל ההסקה AI/ML בקלסטר Kubernetes.

ל-Kaito יש את ההבדלים המרכזיים הבאים לעומת רוב שיטות פריסת המודלים הפופולריות המבוססות על תשתיות מכונות וירטואליות:

- ניהול קבצי מודל באמצעות תמונות קונטיינרים. שרת http מסופק לביצוע קריאות הסקה תוך שימוש בספריית המודל.
- הימנעות מכיוון פרמטרי פריסה כדי להתאים לחומרת GPU באמצעות מתכונות מוגדרות מראש.
- פרוביזיה אוטומטית של צמתי GPU בהתבסס על דרישות המודל.
- אירוח תמונות מודל גדולות ברגיסטרי הקונטיינרים הציבורי של מיקרוסופט (MCR) אם הרישיון מאפשר זאת.

באמצעות Kaito, זרימת העבודה של שימוש במודלים גדולים של הסקת AI ב-Kubernetes הופכת לפשוטה בהרבה.

## ארכיטקטורה

Kaito עוקב אחר תבנית עיצוב קלאסית של Kubernetes Custom Resource Definition(CRD)/controller. המשתמש מנהל משאב מותאם אישית מסוג `workspace` שמתאר את דרישות ה-GPU ומפרט את ההסקה. הבקרים של Kaito יאוטומטו את הפריסה על ידי פיוס משאב מותאם אישית `workspace`.

<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/website/static/img/ragarch.png" width=80% title="KAITO RAGEngine architecture" alt="KAITO RAGEngine architecture">
</div>

האיור מעלה מציג סקירת ארכיטקטורה של Kaito. הרכיבים המרכזיים שלו כוללים:

- **לוח הבקרה של Workspace**: הוא מתאם את משאב ה`workspace` המותאם אישית, יוצר משאבים מותאמים אישית מסוג `machine` (הוסבר להלן) כדי להפעיל פרוביזיה אוטומטית של הצמתים, ויוצר את עומס העבודה של ההסקה (`deployment` או `statefulset`) בהתבסס על מתכונת המודל המוגדרת מראש.
- **לוח בקרה של פרוביזיה לצמתים**: שם הלוח הוא *gpu-provisioner* ב-[gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). הוא משתמש ב-CRD מסוג `machine` שמקורו ב-[Karpenter](https://sigs.k8s.io/karpenter) כדי לתקשר עם לוח הבקרה של workspace. הוא משתלב עם APIs של Azure Kubernetes Service (AKS) כדי להוסיף צמתים חדשים עם GPU לקלסטר AKS.
> הערה: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) הוא רכיב קוד פתוח. ניתן להחליפו בלוחות בקרה אחרים אם הם תומכים ב-[Karpenter-core](https://sigs.k8s.io/karpenter) APIs.

## התקנה

אנא עיין בהנחיות ההתקנה [כאן](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## התחלה מהירה של הסקה Phi-3
[דוגמת קוד הסקה Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # כיוון נתיב הפלט ACR
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3.yaml
```

ניתן לעקוב אחרי סטטוס ה-workspace על ידי הרצת הפקודה הבאה. כאשר העמודה WORKSPACEREADY הופכת ל`True`, המודל פורסם בהצלחה.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

לאחר מכן, ניתן למצוא את כתובת ה-ip של שירות ההסקה בקלסטר ולהשתמש ב-pod זמני `curl` כדי לבדוק את נקודת הקצה של השירות בקלאסטר.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## התחלה מהירה של הסקה Phi-3 עם מתאמים

לאחר התקנת Kaito, ניתן לנסות את הפקודות הבאות כדי להפעיל שירות הסקה.

[דוגמת קוד הסקה Phi-3 עם מתאמים](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # כיוונון נתיב יציאת ACR
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3_with_adapters.yaml
```

ניתן לעקוב אחרי סטטוס ה-workspace על ידי הרצת הפקודה הבאה. כאשר העמודה WORKSPACEREADY הופכת ל`True`, המודל פורסם בהצלחה.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

לאחר מכן, ניתן למצוא את כתובת ה-ip של שירות ההסקה בקלסטר ולהשתמש ב-pod זמני `curl` כדי לבדוק את נקודת הקצה של השירות בקלאסטר.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**הצהרת נושים**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדייק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור יש להיחשב למקור הסמכותי. עבור מידע קריטי מומלץ שימוש בתרגום מקצועי אנושי. איננו אחראים לכל אי-הבנות או פרשנויות שגויות הנובעות משימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->