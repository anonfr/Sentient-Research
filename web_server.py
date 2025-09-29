import os
import subprocess
import threading
from flask import Flask

app = Flask(__name__)

@app.route('/')
def health_check():
    return "Sentient Discord Research Agent is running! 🤖"

@app.route('/status')
def status():
    return {"status": "online", "service": "Discord Research Agent"}

def run_discord_bot():
    """Run the Discord bot using subprocess"""
    subprocess.run(["python", "-m", "src.agent"])

if __name__ == "__main__":
    # Start the Discord bot in a separate thread as given
    bot_thread = threading.Thread(target=run_discord_bot)
    bot_thread.daemon = True
    bot_thread.start()
    
    # Start the web server for Render
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
