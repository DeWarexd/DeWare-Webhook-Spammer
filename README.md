# Discord Webhook Spammer

## 📋 Overview
Discord Webhook Spammer is a Python application designed for sending automated messages to Discord webhooks. This tool provides users with the ability to customize message content, sender information, and delivery timing.

## 🔧 Installation
To use this application, you'll need to install the required Python packages. Use the package manager [pip](https://pip.pypa.io/en/stable/) for installation:

```bash
pip install discord_webhook 
pip install fade 
```

## ✨ Features
- **Multiple Messages**: Send various text messages sequentially
- **Custom Identity**: Set custom username and avatar for the webhook sender
- **Timing Control**: Define custom intervals between message deliveries

## 🚀 Executable Creation
To convert the script into a standalone executable:

1. Install PyInstaller:
```bash
pip install pyinstaller
```

2. Navigate to the project directory in your command prompt and run:
```bash
pyinstaller main.py --onefile --icon=NONE
```

## ⚠️ Important Notice
Please be aware that this is a legacy project that may require updates to function with current versions of its dependencies. The application was developed using an older version of the pyfade library, and compatibility issues may arise. Users with Python development experience are encouraged to review and update the code as needed.
