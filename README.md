# 📧 AI Email Generator using Google Gemini API

A web-based application that generates professional, tone-appropriate emails automatically using Google's Gemini 2.5 Flash AI model. Built with Flask and a modern glassmorphism UI.

---

## 🌟 Features

- ✅ AI-powered email generation using Google Gemini 2.5 Flash
- ✅ Customize Tone — Formal / Friendly / Professional
- ✅ Customize Recipient — Boss / Client / Colleague / Professor
- ✅ Customize Length — Short / Medium / Long
- ✅ Multi-language support — English, Hindi, French, Spanish, German, Arabic, Japanese
- ✅ Session-based history (last 5 emails)
- ✅ Copy to Clipboard functionality
- ✅ Modern Glassmorphism UI design
- ✅ Secure API key management with `.env`

---

## 🗂️ Project Structure

```
GenAI/
├── static/
│   └── style.css          # External stylesheet
├── templates/
│   └── index.html         # Jinja2 HTML template
├── app.py                 # Flask backend (main file)
├── check_models.py        # Utility to list Gemini models
├── requirements.txt       # Python dependencies
├── .env                   # Secret keys (never share this)
└── .gitignore             # Files to exclude from Git
```

---

## ⚙️ Requirements

- Python 3.8 or higher
- A valid **Google Gemini API Key** → Get it from [https://aistudio.google.com](https://aistudio.google.com)
- Visual Studio Code (recommended)

---

## 🚀 Setup & Installation

### Step 1 — Clone or Download the Project

```bash
git clone https://github.com/your-username/ai-email-generator.git
cd ai-email-generator
```

Or simply download and extract the ZIP, then open the folder in VS Code.

---

### Step 2 — Create a Virtual Environment

```bash
python -m venv venv
```

---

### Step 3 — Activate the Virtual Environment

**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

---

### Step 4 — Install Dependencies

```bash
pip install -r requirements.txt
```

Or manually:
```bash
pip install flask google-generativeai python-dotenv
```

---

### Step 5 — Create the `.env` File

Create a file named `.env` in the root project folder and add:

```
GEMINI_API_KEY=your_gemini_api_key_here
SECRET_KEY=your_random_secret_key_here
```

To generate a secure SECRET_KEY, run this in your terminal:

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

Copy the output and paste it as your `SECRET_KEY` value.

---

### Step 6 — Run the Application

```bash
python app.py
```

---

### Step 7 — Open in Browser

```
http://127.0.0.1:5000
```

---

## 📦 Dependencies

| Package | Version | Purpose |
|--------|---------|---------|
| Flask | latest | Web framework |
| google-generativeai | latest | Gemini AI SDK |
| python-dotenv | latest | Environment variable loader |

Install all at once:
```bash
pip install flask google-generativeai python-dotenv
```

---

## 🔐 Environment Variables

| Variable | Description |
|----------|-------------|
| `GEMINI_API_KEY` | Your Google Gemini API key from AI Studio |
| `SECRET_KEY` | Random secret string for Flask session encryption |

> ⚠️ **Never share your `.env` file or push it to GitHub.**

---

## 🛡️ .gitignore

Make sure your `.gitignore` includes:

```
.env
venv/
__pycache__/
*.pyc
```

---

## 🖥️ How It Works

1. User fills in the form — topic, tone, recipient, length, language
2. Flask reads the form data on POST request
3. A detailed prompt is constructed and sent to Gemini API
4. Gemini returns a generated email
5. Email is displayed on screen with copy option
6. Email is saved to session history (max 5 entries)

---

## 📸 Project Preview

> The app features a purple gradient background with a frosted-glass card, smooth animations, collapsible history cards, and a loading spinner while the AI generates the email.

---

## 🔮 Future Improvements

- [ ] User authentication & persistent database history
- [ ] Email sending via SMTP integration
- [ ] Edit generated email before copying
- [ ] More tone and language options
- [ ] Deploy to Render / Railway / AWS

---

## 👨‍💻 Author

**Sahil Sagar Gupta**
Chandigarh University

---

## 📄 License

This project is for educational purposes only."Email Generator" 
"AI-Email-Generator " 
