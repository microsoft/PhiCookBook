<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a1c62bf7d86d6186bf8d3917196a92a0",
  "translation_date": "2025-07-17T06:23:33+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Kaito.md",
  "language_code": "he"
}
-->
## כיוונון עדין עם Kaito

[Kaito](https://github.com/Azure/kaito) הוא אופרטור שמאוטומט את פריסת מודלי AI/ML להסקת מסקנות בתוך אשכול Kubernetes.

ל-Kaito יש הבדלים מרכזיים לעומת רוב שיטות הפריסה המקובלות המבוססות על תשתיות של מכונות וירטואליות:

- ניהול קבצי המודל באמצעות תמונות קונטיינר. שרת http מסופק לביצוע קריאות הסקה באמצעות ספריית המודל.
- הימנעות מכיוונון פרמטרי פריסה להתאמה לחומרת GPU על ידי מתן תצורות מוגדרות מראש.
- פריסה אוטומטית של צמתים עם GPU בהתאם לדרישות המודל.
- אחסון תמונות מודל גדולות ברישום הקונטיינרים הציבורי של מיקרוסופט (MCR) אם הרישיון מאפשר זאת.

באמצעות Kaito, תהליך העלאת מודלי הסקה גדולים ל-Kubernetes הופך לפשוט בהרבה.

## ארכיטקטורה

Kaito פועל לפי דפוס העיצוב הקלאסי של Kubernetes Custom Resource Definition (CRD) ושל בקר (controller). המשתמש מנהל משאב מותאם אישית מסוג `workspace` שמתאר את דרישות ה-GPU ואת מפרט ההסקה. בקרי Kaito יאוטומטו את הפריסה על ידי התאמת משאב ה-`workspace`.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

התמונה למעלה מציגה סקירה של ארכיטקטורת Kaito. הרכיבים המרכזיים שלה כוללים:

- **בקר Workspace**: מתאם את משאב ה-`workspace`, יוצר משאבים מותאמים אישית מסוג `machine` (מוסבר בהמשך) כדי להפעיל פריסה אוטומטית של צמתים, ויוצר את עומס העבודה של ההסקה (`deployment` או `statefulset`) בהתבסס על תצורות המודל המוגדרות מראש.
- **בקר Node provisioner**: שם הבקר הוא *gpu-provisioner* ב-[gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). הוא משתמש ב-CRD מסוג `machine` שמקורו ב-[Karpenter](https://sigs.k8s.io/karpenter) כדי לתקשר עם בקר ה-workspace. הוא משתלב עם ממשקי ה-API של Azure Kubernetes Service (AKS) להוספת צמתים עם GPU חדשים לאשכול AKS.
> הערה: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) הוא רכיב בקוד פתוח. ניתן להחליפו בבקרים אחרים אם הם תומכים בממשקי ה-API של [Karpenter-core](https://sigs.k8s.io/karpenter).

## סרטון סקירה  
[צפו בדמו של Kaito](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)

## התקנה

אנא עיינו במדריך ההתקנה [כאן](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## התחלה מהירה

לאחר התקנת Kaito, ניתן לנסות את הפקודות הבאות כדי להתחיל שירות כיוונון עדין.

```
apiVersion: kaito.sh/v1alpha1
kind: Workspace
metadata:
  name: workspace-tuning-phi-3
resource:
  instanceType: "Standard_NC6s_v3"
  labelSelector:
    matchLabels:
      app: tuning-phi-3
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
```

```sh
$ cat examples/fine-tuning/kaito_workspace_tuning_phi_3.yaml

apiVersion: kaito.sh/v1alpha1
kind: Workspace
metadata:
  name: workspace-tuning-phi-3
resource:
  instanceType: "Standard_NC6s_v3"
  labelSelector:
    matchLabels:
      app: tuning-phi-3
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
    

$ kubectl apply -f examples/fine-tuning/kaito_workspace_tuning_phi_3.yaml
```

ניתן לעקוב אחרי מצב ה-workspace על ידי הרצת הפקודה הבאה. כאשר העמודה WORKSPACEREADY הופכת ל-`True`, המודל הוצב בהצלחה.

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

לאחר מכן, ניתן למצוא את כתובת ה-IP של שירות ההסקה באשכול ולהשתמש בפוד `curl` זמני כדי לבדוק את נקודת הקצה של השירות בתוך האשכול.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור שלו נחשב למקור הסמכותי. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אנושי. אנו לא נושאים באחריות לכל אי-הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.