<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e46691923dca7cb2f11d32b1d9d558e0",
  "translation_date": "2025-07-16T20:51:51+00:00",
  "source_file": "md/01.Introduction/03/Kaito_Inference.md",
  "language_code": "he"
}
-->
## הסקה עם Kaito

[Kaito](https://github.com/Azure/kaito) הוא אופרטור שמבצע אוטומציה לפריסת מודלים של AI/ML להסקה בתוך אשכול Kubernetes.

ל-Kaito יש הבדלים מרכזיים לעומת רוב שיטות הפריסה המקובלות המבוססות על תשתיות של מכונות וירטואליות:

- ניהול קבצי המודל באמצעות תמונות קונטיינר. שרת http מסופק לביצוע קריאות הסקה באמצעות ספריית המודל.
- הימנעות מכוונון פרמטרי פריסה להתאמה לחומרת GPU על ידי מתן תצורות מוגדרות מראש.
- פריסה אוטומטית של צמתים עם GPU בהתאם לדרישות המודל.
- אחסון תמונות מודל גדולות ברישום הקונטיינרים הציבורי של מיקרוסופט (MCR) אם הרישיון מאפשר זאת.

באמצעות Kaito, תהליך העלאת מודלים גדולים להסקת AI ב-Kubernetes הופך לפשוט הרבה יותר.

## ארכיטקטורה

Kaito פועל לפי דפוס העיצוב הקלאסי של Kubernetes Custom Resource Definition (CRD) ושל בקר (controller). המשתמש מנהל משאב מותאם אישית מסוג `workspace` שמתאר את דרישות ה-GPU ואת מפרט ההסקה. בקרי Kaito מבצעים אוטומציה לפריסה על ידי סינכרון משאב ה-`workspace`.

<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

התמונה למעלה מציגה סקירה של ארכיטקטורת Kaito. הרכיבים המרכזיים שלה כוללים:

- **בקר Workspace**: מסנכרן את משאב ה-`workspace`, יוצר משאבים מותאמים אישית מסוג `machine` (כפי שמוסבר בהמשך) כדי להפעיל פריסה אוטומטית של צמתים, ויוצר את עומס העבודה של ההסקה (`deployment` או `statefulset`) בהתבסס על תצורות המודל המוגדרות מראש.
- **בקר פריסת צמתים**: שמו של הבקר הוא *gpu-provisioner* ב-[טבלת helm של gpu-provisioner](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). הוא משתמש ב-CRD מסוג `machine` שמקורו ב-[Karpenter](https://sigs.k8s.io/karpenter) כדי לתקשר עם בקר ה-workspace. הוא משתלב עם ממשקי ה-API של Azure Kubernetes Service (AKS) להוספת צמתים עם GPU לאשכול AKS.
> Note: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) הוא רכיב בקוד פתוח. ניתן להחליפו בבקרים אחרים אם הם תומכים בממשקי ה-API של [Karpenter-core](https://sigs.k8s.io/karpenter).

## התקנה

אנא עיינו במדריך ההתקנה [כאן](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## התחלה מהירה להסקה Phi-3  
[קוד לדוגמה להסקה Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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

ניתן לעקוב אחרי מצב ה-workspace על ידי הרצת הפקודה הבאה. כאשר העמודה WORKSPACEREADY הופכת ל-`True`, המודל הוצב בהצלחה.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

לאחר מכן, ניתן למצוא את כתובת ה-IP של שירות ההסקה באשכול ולהשתמש בפוד זמני עם `curl` כדי לבדוק את נקודת הקצה של השירות באשכול.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## התחלה מהירה להסקה Phi-3 עם מתאמים

לאחר התקנת Kaito, ניתן לנסות את הפקודות הבאות כדי להפעיל שירות הסקה.

[קוד לדוגמה להסקה Phi-3 עם מתאמים](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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

ניתן לעקוב אחרי מצב ה-workspace על ידי הרצת הפקודה הבאה. כאשר העמודה WORKSPACEREADY הופכת ל-`True`, המודל הוצב בהצלחה.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

לאחר מכן, ניתן למצוא את כתובת ה-IP של שירות ההסקה באשכול ולהשתמש בפוד זמני עם `curl` כדי לבדוק את נקודת הקצה של השירות באשכול.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור שלו נחשב למקור הסמכותי. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אנושי. אנו לא נושאים באחריות לכל אי-הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.