# 🤖 Sentient Discord Research Agent

**AI-powered Discord bot with advanced research capabilities built for the Sentient Builder Program.**

## ✨ Features
- 🔍 **Deep Research** - Comprehensive analysis on any topic
- 📊 **Data Analysis** - Advanced insights and recommendations  
- 📋 **Professional Reports** - Business-ready documentation
- 📝 **Smart Summarization** - Intelligent content condensation
- 🧠 **Conversation Memory** - Context-aware interactions

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- Discord Developer Account
- Fireworks AI API Key

### Setup
```bash
git clone https://github.com/anonfr/Sentient-Research.git
cd Sentient-Research
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your API keys
python -m src.agent
```

### Environment Variables
```env
MODEL_API_KEY=your_fireworks_api_key
DISCORD_TOKEN=your_discord_bot_token
```

## 🎯 Commands
- `!research [topic]` - Deep research on any subject
- `!analyze [subject]` - Data analysis with insights
- `!report [topic]` - Generate comprehensive reports
- `!summarize [text]` - Intelligent summarization
- `!help` - Show all commands

## 🌐 24/7 Deployment

### Deploy on Render (Free)
1. Fork this repo
2. Sign up at [Render.com](https://render.com)
3. Create new web service from your GitHub repo
4. Add environment variables in Render dashboard
5. Deploy - your bot runs 24/7!

## 🔧 Discord Bot Setup
1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Create new application and bot
3. Copy bot token to `.env`
4. Enable privileged intents:
   - ✅ Message Content Intent
   - ✅ Server Members Intent
   - ✅ Presence Intent
5. Invite bot with permissions:
   - ✅ View Channels
   - ✅ Send Messages
   - ✅ Read Messages
   - ✅ Read Message History

## 🏆 Built for Sentient Builder Program
High-value research agent demonstrating:
- ✅ Advanced AI integration
- ✅ Production-ready architecture
- ✅ Real-world utility
- ✅ Professional quality

## 📊 Example Usage
```
User: !research blockchain technology 2024
Bot: 📊 Research Report: blockchain technology 2024
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
     
     🔍 Key Findings:
     • Enterprise adoption increasing 40% year-over-year
     • Major focus on sustainability and energy efficiency
     • Integration with AI and IoT technologies expanding
     
     📈 Current Trends:
     • Central Bank Digital Currencies (CBDCs) development
     • DeFi protocols maturing with better security
     • NFT utility expanding beyond digital art
     
     🚀 Future Implications:
     • Supply chain transparency becoming standard
     • Smart contracts automating complex agreements
     • Cross-chain interoperability solving fragmentation
```

## 🛠️ Customization
Edit `src/agent/agent_tools/discord/discord_config.py` to modify bot behavior.

## 📄 License
MIT License - see LICENSE file for details.

## 🤝 Contributing
1. Fork the repository
2. Create feature branch
3. Make changes
4. Submit pull request

---

**⭐ Star this repo if you find it useful!**

Built with ❤️ for the AI community
