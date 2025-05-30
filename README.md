# Accent Classification Webapp

A simple Flask web application that takes a URL of a video and responds with the most probable accent used in the video.

---

## 🧰 Features

- Simple HTML frontend served via Flask templates
- JSON API endpoint for handling POST requests
- Clean separation of frontend and backend logic
- Classifying Accent using a pretrained classifier: https://huggingface.co/Jzuluaga/accent-id-commonaccent_ecapa
- Use of Generative AI to describe the prediction

---

## 🚀 Getting Started

### 1. Clone the repository

`````bash
git clone https://github.com/Ahmed-Eloraby/REMWaste-Technical-Assessment-Accent-Classification
cd REMWaste-Technical-Assessment-Accent-Classification
`````
### 2. Create a virtual environment (optional but recommended)
`````bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
`````
### 3. Install dependencies
`````bash
pip install -r requirements.txt
`````
### 4. Run the app locally
`````bash
python app.py
`````

Visit http://localhost:5000 in your browser.
Enter your url in the textbox to get the result.

![Screenshot 2025-05-30 031512](https://github.com/user-attachments/assets/eb83b748-fe83-4b3f-ab10-d6e1c72a52c5)


🤝 License
MIT License. Feel free to fork, use, and modify.
