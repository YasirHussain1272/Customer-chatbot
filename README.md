# 🤖 AI Arabic-English Customer Support Chatbot

A bilingual (Arabic 🇸🇦 + English 🇬🇧) AI customer support chatbot built for the Saudi market — powered by **Groq LLaMA3**, styled like **WhatsApp**, and deployed free on **Render**.

![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat-square)
![Flask](https://img.shields.io/badge/Flask-3.0-green?style=flat-square)
![Groq](https://img.shields.io/badge/LLM-Groq%20LLaMA3-orange?style=flat-square)
![Deploy](https://img.shields.io/badge/Deploy-Render-purple?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-lightgrey?style=flat-square)

---

## ✨ Features

| Feature | Details |
|---|---|
| 🌐 Bilingual | Arabic + English auto-detection |
| 💬 WhatsApp UI | Familiar chat bubbles, timestamps, read receipts |
| 🎤 Voice Input | Speech-to-text (Arabic & English) |
| ⚡ Fast AI | Groq's LLaMA3-8B (sub-second responses) |
| 📱 Mobile-First | Fully responsive design |
| 🆓 Free Deploy | Render free tier |

---

## 🏢 Target Industries (Saudi Market)

- 🛍️ **Retail** — Order tracking, returns, payments
- 🏥 **Healthcare** — Appointment booking, FAQs  
- 📦 **Logistics** — Shipment tracking, delivery ETA
- 🏛️ **Government Portals** — Citizen service queries

---

## 🚀 Quick Start

### 1. Clone the repo
```bash
git clone [https://github.com/YOUR_USERNAME/arabic-chatbot.git](https://github.com/YasirHussain1272/Customer-chatbot.git)
cd arabic-chatbot
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set your Groq API key
Get a **free** API key from [console.groq.com](https://console.groq.com)

```bash
export GROQ_API_KEY=your_key_here
```

### 4. Run locally
```bash
python app.py
```
Open: [http://localhost:5000](http://localhost:5000)

---


## 📁 Project Structure

```
arabic-chatbot/
├── app.py              # Flask backend + Groq AI
├── requirements.txt    # Python dependencies
├── Procfile            # Render/Heroku start command
├── render.yaml         # Render deployment config
└── templates/
    └── index.html      # WhatsApp-style chat UI
```

---

## 🔧 Customization

Edit the `SYSTEM_PROMPT` in `app.py` to match your business:
- Add your company name
- Update FAQ topics
- Adjust tone (formal/casual)
- Add specific product/service knowledge

---

## 📸 Screenshots

> WhatsApp-style UI with RTL Arabic support and real-time AI responses

---

## 🤝 Contributing

PRs welcome! Fork → Feature branch → PR

---

## 📄 License

MIT License — free to use and modify

---

*Built with ❤️ for the Saudi tech community 🇸🇦*
