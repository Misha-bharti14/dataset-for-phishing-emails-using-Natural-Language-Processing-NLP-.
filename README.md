# dataset-for-phishing-emails-using-Natural-Language-Processing-NLP-.
# 🧠 Phishing Email Detection — Data Generator

## 📝 Overview  
This module creates a small, labeled dataset for a **Phishing Email Detection System** using **NLP** and **Logistic Regression**.  
The script `generate_sample_dataset.py` produces a sample CSV dataset and a metadata file to maintain transparency and reproducibility.

---

## 🚀 Quick Start  

```bash
python generate_sample_dataset.py
```

### Requirements  
```bash
pip install pandas
```

---

## 📁 Files Generated  

| File | Description |
|------|--------------|
| **phishing_emails.csv** | Contains sample emails labeled as phishing or legitimate. |
| **dataset_metadata.json** | Stores creation details and label mapping. |

---

## 💻 Script Summary  

```python
import pandas as pd, json
from datetime import datetime

samples = [
    ("Your account has been locked due to suspicious activity...", 1),
    ("Update your payment method to avoid interruption.", 1),
    ("You have won $500,000! Reply to claim your prize.", 1),
    ("Team meeting tomorrow at 10 AM", 0),
    ("Please find attached the monthly invoice", 0)
]

df = pd.DataFrame(samples, columns=['text','label'])
df.to_csv('phishing_emails.csv', index=False)

metadata = {
    "generated_by": "<Your Name / Roll No.>",
    "generated_at": datetime.utcnow().isoformat() + "Z",
    "num_samples": len(df),
    "label_map": {"1": "phishing", "0": "legitimate"}
}

json.dump(metadata, open('dataset_metadata.json','w'), indent=2)
print("✅ Dataset and metadata saved.")
```

---

## 🔄 Next Steps  
- Clean text data (remove URLs, stop words, etc.)  
- Vectorize using TF-IDF  
- Train and test the Logistic Regression model  
