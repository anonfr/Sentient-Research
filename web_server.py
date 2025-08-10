import os
from flask import Flask
import threading
from src.agent import main

app = Flask(__name__)

@app.route('/')
def health_check():
    return "Sentient Discord Research Agent is running! 🤖"

@app.route('/status')
def status():
    return {"status": "online", "service": "Discord Research Agent"}

if __name__ == "__main__":
    # Start the Discord bot in a separate thread
    bot_thread = threading.Thread(target=main.main)
    bot_thread.daemon = True
    bot_thread.start()
    
    # Start the web server for Render
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
