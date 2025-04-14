# 🕒 1337 Auto Check-In Bot

A simple Python script to **automate the check-in process** for [1337.ma](https://candidature.1337.ma/), checking every 30 seconds for available check-in slots.

## 📌 Features

- Automatic login to the [candidature.1337.ma](https://candidature.1337.ma) platform
- Periodic check every 30 seconds for available check-in times
- Auto-refresh and re-login if disconnected
- Option to run in headless mode

## 💻 Requirements

- Python 3.7+
- Google Chrome installed

## 📦 Dependencies

Install required dependencies using:

```bash
pip install -r requirements.txt
```

**requirements.txt**:
```
selenium
webdriver-manager
```

## 🚀 How to Use

1. Clone the repo:

```bash
git clone https://github.com/your-username/1337-auto-checkin.git
cd 1337-auto-checkin
```

2. Run the script:

```bash
python checkin.py
```

3. Enter your email and password when prompted (or hardcode them in the script if preferred).

The bot will:
- Log into your account
- Wait and check for check-in availability every 30 seconds
- Re-login if disconnected

---

## 🔐 Disclaimer

This script is for educational purposes only.  
Use responsibly and at your own risk.  
We are **not affiliated with 1337.ma** or 42 Network.

---

## 🛠️ To-Do

- Add GUI or config file support
- Telegram/Discord notifications on successful check-in
- Support for multiple accounts

---

## 📄 License

MIT License
