# Accent Classification Webapp

A simple Flask web application that takes a URL of a video and responds with the most probable accent used in the video.

---

## 🧰 Features

- Simple HTML frontend served via Flask templates
- JSON API endpoint for handling POST requests
- Clean separation of frontend and backend logic
- Using API of Existing Classifiers (commonaccent_cpa: https://huggingface.co/Jzuluaga/accent-id-commonaccent_ecapa)

---

## 🚀 Getting Started

### 1. Clone the repository

`````bash
git clone https://github.com/Ahmed-Eloraby/REMWaste-Technical-Assessment-Accent-Classification
cd REMWaste-Technical-Assessment-Accent-Classification

### 2. Create a virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

### 3. Install dependencies
```bash
pip install -r requirements.txt

### 4. Run the app locally
```bash
python app.py

Visit http://localhost:5000 in your browser.
Enter your url in the textbox to get the result.


🤝 License
MIT License. Feel free to fork, use, and modify.
