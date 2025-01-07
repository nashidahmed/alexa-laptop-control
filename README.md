# Alexa Laptop Control

A simple Flask server to let Alexa shut down or hibernate your laptop via voice commands.

## Features

- Shut down or hibernate your laptop using Alexa.
- Supports Windows, Mac, and Linux.

## Prerequisites

1. **Python 3.6+**
2. **pip**
3. **Administrator/root access** (required for shutdown/hibernate commands).
4. **ngrok** (to expose the local server to Alexa).

## Setup Instructions

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/alexa-laptop-control.git
   cd alexa-laptop-control
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up scripts**

   - Edit the scripts (`shutdown.bat`, `hibernate.bat`, etc.) to suit your OS.
   - Ensure scripts are executable (Linux/Mac):
     ```bash
     chmod +x scripts/*.sh
     ```

4. **Run the server**

   ```bash
   python server/app.py
   ```

5. **Expose the server Use [ngrok](https://ngrok.com/) to expose the server:**

   ```bash
   ngrok http 5000
   ```

   Note the generated URL (e.g., `https://1234abcd.ngrok.io`).

6. **Connect Alexa to the server**
   - Use [IFTTT](https://ifttt.com/) or create a custom Alexa skill to send POST requests to:
     - `https://1234abcd.ngrok.io/shutdown`
     - `https://1234abcd.ngrok.io/hibernate`

## Security Considerations

- Implement token-based authentication in the Flask app.
- Avoid exposing your ngrok URL publicly.
