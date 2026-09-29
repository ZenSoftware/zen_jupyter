## 🧰 **Step‑by‑step: Regenerate `.venv`**

### **1. Create a fresh virtual environment**

```bash
python3 -m venv .venv
```

Or on Windows:

```powershell
python -m venv .venv
```

---

### **2. Activate the environment**

macOS/Linux:

```bash
source .venv/bin/activate
```

Windows:

```powershell
.\.venv\Scripts\activate
```

---

### **4. Reinstall your dependencies**

If you have a `requirements.txt`:

```bash
pip install -r requirements.txt
```
