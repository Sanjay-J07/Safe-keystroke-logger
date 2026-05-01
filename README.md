# 🔐 Safe Keystroke Logger (Educational)

## 📌 Description

A Python-based keystroke logger designed for **educational purposes**. This application captures and logs key presses **only within its own window** and requires explicit user interaction (start/stop). It demonstrates event handling, file logging, and user-consent-based design in cybersecurity.

---

## 🚀 Features

* ⌨️ Captures key presses inside the application window only
* ▶️ Start and Stop logging controls
* 🕒 Logs each key press with timestamp
* 📄 Saves output to a text file (`keystrokes.txt`)
* 🔐 Privacy-safe and user-controlled
* 🖥️ Simple GUI using Tkinter

---

## 🧠 How It Works

1. User launches the application
2. Clicks **Start Logging**
3. Types inside the application window
4. Key presses are recorded with timestamps
5. Clicks **Stop Logging** to end session
6. Logs are saved in a local file

---

## 🛠️ Technologies Used

* Python
* Tkinter (GUI)
* File Handling
* Event Binding

---

## ▶️ How to Run

```bash id="ydps04"
python keystroke_logger.py
```

---

## 🧪 Sample Usage

1. Click **Start Logging**
2. Type:

```id="3nrywc"
hello123
```

3. Click **Stop Logging**
4. Open `keystrokes.txt`

---

## 📌 Sample Output

```id="6k93pl"
2026-05-01 10:21:33 - h
2026-05-01 10:21:34 - e
2026-05-01 10:21:35 - l
2026-05-01 10:21:36 - l
2026-05-01 10:21:37 - o
```

---

## 📘 What You Learn

* Event-driven programming
* Keyboard input handling
* Logging data to files
* Ethical and privacy-aware design
* Basics of cybersecurity concepts

---

## ⚠️ Disclaimer

This project is strictly for educational purposes.
It only logs keystrokes within the application window and does not capture input from other applications or systems.

---

## 🔮 Future Improvements

* Display logs in GUI
* Encrypt stored keystrokes
* Add clear/reset log option
* Export logs to CSV
* Session-based logging

---

## 👨‍💻 Author

Sanjay
