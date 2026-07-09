"""Main entry point for Railway deployment
Runs both user_bot and admin_bot as separate tasks"""

import asyncio
import sys
from typing import NoReturn

from utils.logger import get_logger
from config.settings import settings

logger = get_logger(__name__)


async def run_user_bot() -> None:
    """
    Run user bot
    TODO: Implement actual user bot logic
    """
    logger.info("User Bot started")
    try:
        # User bot logic will go here
        # For now, keep running indefinitely
        while True:
            await asyncio.sleep(1)
    except asyncio.CancelledError:
        logger.info("User Bot stopped")
        raise


async def run_admin_bot() -> None:
    """
    Run admin bot
    TODO: Implement actual admin bot logic
    """
    logger.info("Admin Bot started")
    try:
        # Admin bot logic will go here
        # For now, keep running indefinitely
        while True:
            await asyncio.sleep(1)
    except asyncio.CancelledError:
        logger.info("Admin Bot stopped")
        raise


async def main() -> NoReturn:
    """
    Main entry point for Railway deployment
    Runs both bots concurrently
    """
    logger.info(f"Starting VPN Store Bot (Environment: {settings.environment})")
    logger.info(f"Database: {settings.database_url}")
    
    # Verify critical settings
    if not settings.user_bot_token.get_secret_value():
        logger.error("USER_BOT_TOKEN not configured!")
        sys.exit(1)
    
    if not settings.admin_bot_token.get_secret_value():
        logger.error("ADMIN_BOT_TOKEN not configured!")
        sys.exit(1)
    
    logger.info("All required settings verified ✓")
    
    try:
        # Create tasks for both bots
        async with asyncio.TaskGroup() as tg:
            logger.info("Launching User Bot...")
            tg.create_task(run_user_bot())
            
            logger.info("Launching Admin Bot...")
            tg.create_task(run_admin_bot())
            
            logger.info("Both bots are running...")
    
    except KeyboardInterrupt:
        logger.info("Received interrupt signal, shutting down gracefully...")
        sys.exit(0)
    except Exception as e:
        logger.error(f"Fatal error in main: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Application terminated by user")
        sys.exit(0)
    except Exception as e:
        logger.critical(f"Unhandled exception: {str(e)}")
        sys.exit(1)
