# FileShare
A simple **local file sharing app** built with **Flask + PyWebView** in **Python**.  
It allows you to upload, delete, and share files over LAN with a QR code.  
Packaged into a desktop app using **PyInstaller**, so users can run it without installing Python.

---

## Features
- Upload multiple files from browser
- Remove uploaded files
- Automatically generates a QR code for LAN access to scan and connect
- Cross-platform (Windows/Linux/Android)
- Packaged into `.exe` with PyInstaller
- Embedded WebView instead of external browser
- Independent of number of device connected

---

## 📦 Installation (Development)

1. Clone the repo:
   ```bash
   git clone https://github.com/KCoder-programming/FileShare.git
   cd FileShare
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run:
   ```bash
   python app.py
   ```

### Note (for advance users and developers)

This app uses Flask’s development server, which is fine for local/LAN usage.

Do not expose it directly to the internet. If you want to host it, use a production WSGI server

---

### Screenshots:
<img width="686" height="551" alt="image" src="https://github.com/user-attachments/assets/79e48e10-9b57-4e7d-a2f3-5ec348f78043" />
<img width="686" height="631" alt="image" src="https://github.com/user-attachments/assets/129edc3a-efc2-4a7a-ba5a-98cd012a7214" />

---

## License
**MIT License**

Copyright (c) 2025 KCoder-programming
