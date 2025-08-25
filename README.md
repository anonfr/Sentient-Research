# 🤖 Sentient Discord Research Agent

**Transform your Discord server into an AI-powered research hub!**

## 🚀 **Try It Now - Add Our Bot to Your Server!**

<div align="center">

### **[🤖 INVITE BOT TO YOUR SERVER](https://discord.com/oauth2/authorize?client_id=1403894961048387604&permissions=2147682368&integration_type=0&scope=bot+applications.commands)**



<img width="989" height="823" alt="image" src="https://github.com/user-attachments/assets/95393733-d4c9-49a9-af7f-b9f1258b88b0" />




*Ready to use instantly - no setup required!*

</div>

---

## ✨ **What Can It Do?**
- 🔍 **Deep Research** - Get comprehensive analysis on any topic
- 📊 **Data Analysis** - Receive insights with actionable recommendations  
- 📋 **Professional Reports** - Generate business-ready documentation
- 📝 **Smart Summarization** - Condense content intelligently
- 🧠 **Conversation Memory** - Maintains context across discussions

## 🎯 **Commands**
| Command | What It Does | Example |
|---------|-------------|---------|
| `!research [topic]` | Deep research with analysis | `!research AI trends 2024` |
| `!analyze [subject]` | Data insights & recommendations | `!analyze Tesla stock` |
| `!report [topic]` | Professional comprehensive reports | `!report crypto market` |
| `!summarize [text]` | Smart content summarization | `!summarize` (recent chat) |
| `!help` | Show all commands | `!help` |

## 🛠️ **Want Your Own Bot?**

### **Option 1: Deploy on Render (Free & Easy)**
1. **Fork this repo** → **Sign up at [Render.com](https://render.com)**
2. **Create Web Service** → **Connect your GitHub repo**
3. **Add Environment Variables**: `MODEL_API_KEY` + `DISCORD_TOKEN`
4. **Set Start Command**: `python web_server.py`
5. **Deploy** → Your bot runs 24/7!

### **Option 2: Run Locally**
```bash
git clone https://github.com/anonfr/Sentient-Research.git
cd Sentient-Research && python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt && cp .env.example .env
# Add your API keys to .env, then:
python -m src.agent
```

## 🔑 **Need API Keys?**

**For Fireworks AI:**
1. Visit [Fireworks.ai](https://fireworks.ai) → Sign up → Get API key
2. Add to `.env` as `MODEL_API_KEY=your_key_here`

**For Discord Bot:**
1. [Discord Developer Portal](https://discord.com/developers/applications) → New Application → Bot
2. Copy Bot Token → Add to `.env` as `DISCORD_TOKEN=your_token_here`
3. Enable: **Message Content Intent**, **Server Members Intent**, **Presence Intent**

## 💡 **See It In Action**
```
User: !research quantum computing 2024
Bot: 🔍 Research Report: quantum computing 2024
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
     
     📊 Key Findings:
     • IBM achieves 1000+ qubit milestone with error correction
     • Google's quantum advantage in optimization problems confirmed
     • $2.4B invested globally, 40% increase from 2023
     
     🚀 Future Impact:
     • Drug discovery timelines reduced from years to months
     • Cryptography revolution expected by 2030
     • Financial modeling accuracy improvements of 300%
     
     💡 Recommendations:
     • Monitor IBM and Google partnerships closely
     • Consider quantum-safe encryption migration plans
     • Explore quantum cloud services for R&D
```

## 🏆 **Built for Sentient Builder Program**
*High-value AI agent showcasing production-ready research capabilities*

---

<div align="center">

**⭐ [Star this repo](https://github.com/anonfr/Sentient-Research) • 🤖 [Add to Discord](https://discord.com/oauth2/authorize?client_id=1403894961048387604&permissions=2147682368&integration_type=0&scope=bot+applications.commands) • 🚀 [Deploy on Render](https://render.com)**

*Built with ❤️ for the AI community*

</div>
