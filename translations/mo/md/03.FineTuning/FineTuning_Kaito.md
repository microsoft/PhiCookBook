<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a1c62bf7d86d6186bf8d3917196a92a0",
  "translation_date": "2025-05-07T13:38:53+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Kaito.md",
  "language_code": "mo"
}
-->
## Fine-Tuning with Kaito 

[Kaito](https://github.com/Azure/kaito) הוא אופרטור שמבצע אוטומציה לפריסת מודלים של AI/ML בקלאסטר Kubernetes.

ל-Kaito יש הבדלים מרכזיים בהשוואה לרוב שיטות הפריסה הנפוצות המבוססות על תשתיות וירטואליות:

- ניהול קבצי מודל באמצעות תמונות קונטיינר. שרת HTTP מסופק לביצוע קריאות אינפרנס באמצעות ספריית המודל.
- הימנעות מכוונון פרמטרי פריסה לפי חומרת GPU על ידי מתן תצורות מוגדרות מראש.
- פריסה אוטומטית של צמתים עם GPU בהתאם לדרישות המודל.
- אחסון תמונות מודל גדולות ברישום הציבורי של Microsoft Container Registry (MCR) אם הרישיון מאפשר זאת.

באמצעות Kaito, תהליך העלאת מודלים גדולים של אינפרנס ב-Kubernetes הופך לפשוט בהרבה.


## ארכיטקטורה

Kaito פועל לפי דפוס העיצוב הקלאסי של Kubernetes Custom Resource Definition (CRD) ושל בקר (controller). המשתמש מנהל משאב מותאם אישית `workspace` שמתאר את דרישות ה-GPU ואת מפרט האינפרנס. בקרי Kaito מבצעים אוטומציה של הפריסה על ידי פיוס המשאב המותאם אישית `workspace`.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

התמונה למעלה מציגה את סקירת הארכיטקטורה של Kaito. הרכיבים העיקריים כוללים:

- **Workspace controller**: מבצע פיוס של המשאב המותאם אישית `workspace`, יוצר משאבים מותאמים אישית `machine` (מוסבר למטה) כדי להפעיל פריסה אוטומטית של צמתים, ויוצר את עומס העבודה לאינפרנס (`deployment` או `statefulset`) בהתבסס על תצורות המודל המוגדרות מראש.
- **Node provisioner controller**: שם הבקר הוא *gpu-provisioner* ב-[gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). הוא משתמש ב-CRD `machine` שמקורו ב-[Karpenter](https://sigs.k8s.io/karpenter) כדי לתקשר עם בקר ה-workspace. הוא משתלב עם ממשקי ה-API של Azure Kubernetes Service (AKS) כדי להוסיף צמתים עם GPU חדשים לקלאסטר AKS. 
> Note: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) הוא רכיב בקוד פתוח. ניתן להחליפו בבקרים אחרים אם הם תומכים בממשקי ה-API של [Karpenter-core](https://sigs.k8s.io/karpenter).

## סרטון סקירה
[צפו בדמו של Kaito](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)

## התקנה

אנא עיינו במדריך ההתקנה [כאן](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## התחלה מהירה

לאחר התקנת Kaito, ניתן לנסות את הפקודות הבאות כדי להפעיל שירות כוונון עדין.

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

ניתן לעקוב אחרי מצב ה-workspace על ידי הרצת הפקודה הבאה. כאשר העמודה WORKSPACEREADY הופכת ל-`True`, המודל הותקן בהצלחה.

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

בהמשך, ניתן למצוא את כתובת ה-IP של שירות האינפרנס בקלאסטר ולהשתמש בפוד `curl` זמני כדי לבדוק את נקודת הקצה של השירות בתוך הקלאסטר.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Disclaimer**:  
This document has been translated using AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.

---

Could you please clarify what you mean by "mo"? Are you referring to a specific language or dialect? For example, "mo" could refer to Moldovan, a language code, or something else. Providing more details will help me give you the correct translation.