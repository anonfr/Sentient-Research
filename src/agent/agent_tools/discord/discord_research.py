import discord
import logging
import requests
import json
import asyncio
from datetime import datetime
from .discord_config import DiscordConfig

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logging.basicConfig(format="%(levelname)s: %(message)s")

class DiscordResearchAgent(discord.Client):
    def __init__(self, token, model):
        logger.info("[DISCORD-RESEARCH] Initializing Discord Research Agent...")
        self.token = token
        self.model = model
        self.config = DiscordConfig()
        self.conversation_history = {}  # Store conversation context per channel
        self.processed_messages = set()  # Track processed message IDs to prevent duplicates
        self.bot_user_id = None  # Store bot's user ID for better filtering
        
        # Research capabilities
        self.research_commands = {
            "!research": self.handle_research_command,
            "!analyze": self.handle_analysis_command,
            "!summarize": self.handle_summarize_command,
            "!report": self.handle_report_command,
            "!help": self.handle_help_command
        }
    
    def run(self):
        logger.info("[DISCORD-RESEARCH] Starting Discord Research Agent...")
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(intents=intents)
        super().run(self.token, log_level=logging.WARNING)

    async def on_ready(self):
        self.bot_user_id = self.user.id  # Store bot's user ID
        logging.info(f"[DISCORD-RESEARCH] Connected to research bot {self.user.name} with id {self.user.id}.")
        
        # Set bot status to show it's a research assistant
        await self.change_presence(
            status=discord.Status.online,
            activity=discord.Activity(
                type=discord.ActivityType.watching,
                name="for research requests | !help"
            )
        )

    async def on_message(self, message):
        # Simple but effective bot filtering
        if message.author.bot:  # This catches ALL bots including ourselves
            return
        if message.author == self.user:  # Extra safety
            return
            
        logging.info(f"[DISCORD-RESEARCH] Message from {message.author.name}: {message.content}")
        
        # Store conversation history
        channel_id = str(message.channel.id)
        if channel_id not in self.conversation_history:
            self.conversation_history[channel_id] = []
        
        self.conversation_history[channel_id].append({
            "author": message.author.name,
            "content": message.content,
            "timestamp": datetime.now().isoformat()
        })
        
        # Keep only last 10 messages for context
        if len(self.conversation_history[channel_id]) > 10:
            self.conversation_history[channel_id] = self.conversation_history[channel_id][-10:]
        
        try:
            # Check for research commands
            if message.content.startswith('!'):
                await self.handle_command(message)
            else:
                # Regular conversation with research context
                await self.handle_regular_message(message)
                
        except Exception as e:
            logging.exception(f"[DISCORD-RESEARCH] Error processing message: {e}")
            await message.channel.send("❌ Sorry, I encountered an error processing your request. Please try again.")

    async def handle_command(self, message):
        """Handle research commands"""
        command_parts = message.content.split(' ', 1)
        command = command_parts[0].lower()
        query = command_parts[1] if len(command_parts) > 1 else ""
        
        if command in self.research_commands:
            await self.research_commands[command](message, query)
        else:
            await message.channel.send("❓ Unknown command. Use `!help` to see available commands.")

    async def handle_research_command(self, message, query):
        """Handle !research command for deep research"""
        if not query:
            await message.channel.send("📚 Please provide a research topic. Example: `!research artificial intelligence trends 2024`")
            return
            
        await message.channel.send(f"🔍 **Researching:** {query}\n⏳ Gathering information...")
        
        # Simulate research process (in real implementation, you'd use web search APIs)
        research_prompt = f"""
        You are a deep research assistant. Conduct thorough research on: {query}
        
        Provide a comprehensive analysis including:
        1. Key findings and insights
        2. Current trends and developments  
        3. Important statistics or data points
        4. Expert opinions or notable quotes
        5. Future implications or predictions
        6. Reliable sources and references
        
        Format your response in a clear, structured manner with bullet points and sections.
        """
        
        try:
            response = self.model.query(research_prompt)
            
            # Format the response nicely
            formatted_response = f"""
📊 **Research Report: {query}**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

{response}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🕒 Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
🤖 Powered by Sentient Research Agent
"""
            
            # Split long messages if needed
            if len(formatted_response) > 2000:
                chunks = [formatted_response[i:i+1900] for i in range(0, len(formatted_response), 1900)]
                for i, chunk in enumerate(chunks):
                    if i == 0:
                        await message.channel.send(chunk)
                    else:
                        await message.channel.send(f"**Continued ({i+1}/{len(chunks)}):**\n{chunk}")
            else:
                await message.channel.send(formatted_response)
                
        except Exception as e:
            await message.channel.send(f"❌ Research failed: {str(e)}")

    async def handle_analysis_command(self, message, query):
        """Handle !analyze command for data analysis"""
        if not query:
            await message.channel.send("📈 Please provide something to analyze. Example: `!analyze market trends in renewable energy`")
            return
            
        await message.channel.send(f"📊 **Analyzing:** {query}\n⏳ Processing data...")
        
        analysis_prompt = f"""
        You are an expert data analyst. Provide a detailed analysis of: {query}
        
        Include:
        1. Data breakdown and key metrics
        2. Patterns and correlations
        3. Comparative analysis
        4. Risk assessment
        5. Actionable insights
        6. Recommendations
        
        Use analytical thinking and provide specific, data-driven insights.
        """
        
        try:
            response = self.model.query(analysis_prompt)
            formatted_response = f"📊 **Analysis Report**\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n{response}"
            await message.channel.send(formatted_response)
        except Exception as e:
            await message.channel.send(f"❌ Analysis failed: {str(e)}")

    async def handle_summarize_command(self, message, query):
        """Handle !summarize command"""
        if not query:
            # Summarize recent conversation
            channel_id = str(message.channel.id)
            if channel_id in self.conversation_history and len(self.conversation_history[channel_id]) > 1:
                conversation = "\n".join([f"{msg['author']}: {msg['content']}" for msg in self.conversation_history[channel_id][-5:]])
                summary_prompt = f"Summarize this conversation concisely:\n{conversation}"
            else:
                await message.channel.send("📝 No recent conversation to summarize. Provide text to summarize: `!summarize [text]`")
                return
        else:
            summary_prompt = f"Provide a concise, well-structured summary of: {query}"
        
        await message.channel.send("📝 **Summarizing...**")
        
        try:
            response = self.model.query(summary_prompt)
            await message.channel.send(f"📄 **Summary**\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n{response}")
        except Exception as e:
            await message.channel.send(f"❌ Summarization failed: {str(e)}")

    async def handle_report_command(self, message, query):
        """Handle !report command for comprehensive reports"""
        if not query:
            await message.channel.send("📋 Please specify a report topic. Example: `!report cryptocurrency market analysis`")
            return
            
        await message.channel.send(f"📋 **Generating Report:** {query}\n⏳ This may take a moment...")
        
        report_prompt = f"""
        Create a comprehensive professional report on: {query}
        
        Structure the report with:
        1. Executive Summary
        2. Introduction and Background
        3. Current State Analysis
        4. Key Findings
        5. Challenges and Opportunities
        6. Recommendations
        7. Conclusion
        
        Make it detailed, professional, and actionable.
        """
        
        try:
            response = self.model.query(report_prompt)
            formatted_response = f"""
📋 **COMPREHENSIVE REPORT**
**Topic:** {query}
**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

{response}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🤖 **Sentient Research Agent** | Built for Sentient Builder Program
"""
            
            # Handle long reports
            if len(formatted_response) > 2000:
                chunks = [formatted_response[i:i+1900] for i in range(0, len(formatted_response), 1900)]
                for i, chunk in enumerate(chunks):
                    await message.channel.send(chunk)
                    if i < len(chunks) - 1:
                        await asyncio.sleep(1)  # Small delay between chunks
            else:
                await message.channel.send(formatted_response)
                
        except Exception as e:
            await message.channel.send(f"❌ Report generation failed: {str(e)}")

    async def handle_help_command(self, message, query):
        """Handle !help command"""
        help_text = """
🤖 **Sentient Research Agent - Commands**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔍 **!research [topic]** - Deep research on any topic
📊 **!analyze [subject]** - Detailed analysis with insights  
📝 **!summarize [text]** - Summarize text or recent conversation
📋 **!report [topic]** - Generate comprehensive professional report
❓ **!help** - Show this help message

**Examples:**
• `!research blockchain technology trends 2024`
• `!analyze Tesla stock performance`
• `!summarize` (summarizes recent chat)
• `!report artificial intelligence in healthcare`

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🚀 **Built for Sentient Builder Program**
💡 Powered by advanced AI research capabilities
"""
        await message.channel.send(help_text)

    async def handle_regular_message(self, message):
        """Handle regular conversation with research context"""
        channel_id = str(message.channel.id)
        
        # Build context from conversation history
        context = ""
        if channel_id in self.conversation_history:
            recent_messages = self.conversation_history[channel_id][-3:]
            context = "Recent conversation:\n" + "\n".join([f"{msg['author']}: {msg['content']}" for msg in recent_messages])
        
        enhanced_prompt = f"""
        You are a Sentient Research Assistant - an intelligent, helpful AI that specializes in research, analysis, and providing detailed information.
        
        {context}
        
        User message: {message.content}
        
        Respond helpfully and mention that you can do deep research with commands like !research, !analyze, !summarize, and !report.
        Be knowledgeable, professional, and engaging.
        """
        
        try:
            response = self.model.query(enhanced_prompt)
            await message.channel.send(response)
        except Exception as e:
            logging.exception(f"[DISCORD-RESEARCH] Error in regular message: {e}")
            await message.channel.send("I'm having trouble processing that. Try using one of my research commands: !help")
