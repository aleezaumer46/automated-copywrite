# ✍️ AI Copywriter Pro

A Streamlit app that generates three platform-specific marketing copy variations with Groq's Llama 3.3 model. Choose LinkedIn, Instagram, or Email, select a tone, and adjust the model's temperature and top-p settings.

---

## 🚀 Features

- 🤖 AI-powered marketing copy generation
- ⚡ Powered by Groq API + Llama 3.3 70B Versatile
- Support for multiple platforms:
  - LinkedIn
  - Instagram
  - Email

- Multiple writing tones:
  - Professional
  - Friendly
  - Casual
  - Formal
  - Persuasive
  - Excited

- Adjustable AI creativity:
  - Temperature control
  - Top P control

- 📋 One-click Copy to Clipboard
- 📄 Download generated copy as TXT
- 📑 Download generated copy as PDF
- 📜 Copy History Management
- 🌙 Dark/Light Theme Toggle
- ✅ Input validation
- ⏳ Loading spinner during AI generation
- 🎉 Success notification after content generation

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Groq API
- Llama 3.3 70B Versatile
- Python-dotenv
- FPDF
- Streamlit Copy to Clipboard

---

## 📂 Project Structure

```text
automated-copywriter/
│
├── app.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Requirements

- Python 3.10 or newer
- A Groq API key

## Run locally

1. Clone the repository and open its directory.
2. Create and activate a virtual environment:

    ```powershell
    py -m venv .venv
    .venv\Scripts\Activate.ps1
    ```

  On macOS or Linux, use `python3 -m venv .venv` and `source .venv/bin/activate`.

3. Install dependencies:

    ```shell
    python -m pip install -r requirements.txt
    ```

4. Copy `.env.example` to `.env` and add your Groq API key to `GROQ_API_KEY`.
5. Start the app with `python -m streamlit run app.py`.

Streamlit prints the local URL in the terminal. Keep `.env` private; it is excluded from Git.