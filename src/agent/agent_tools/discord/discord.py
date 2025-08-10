import discord
import logging
from .discord_config import DiscordConfig
from .discord_research import DiscordResearchAgent

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logging.basicConfig(format="%(levelname)s: %(message)s")

class Discord:
    def __init__(self, token, model):
        logger.info("[DISCORD] Initializing Discord Research Agent...")
        self.research_agent = DiscordResearchAgent(token, model)
    
    def run(self):
        logger.info("[DISCORD] Starting Discord Research Agent...")
        self.research_agent.run()