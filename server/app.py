from flask import Flask, request, jsonify
import os
import platform

app = Flask(__name__)

# Configurable script paths
SHUTDOWN_SCRIPT = "scripts/shutdown.bat" if platform.system() == "Windows" else "scripts/shutdown.sh"
HIBERNATE_SCRIPT = "scripts/hibernate.bat" if platform.system() == "Windows" else "scripts/hibernate.sh"

@app.route('/shutdown', methods=['POST'])
def shutdown():
    try:
        os.system(SHUTDOWN_SCRIPT)
        return jsonify({"message": "Shutting down"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/hibernate', methods=['POST'])
def hibernate():
    try:
        os.system(HIBERNATE_SCRIPT)
        return jsonify({"message": "Hibernating"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
