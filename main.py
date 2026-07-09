# Start script for Railway deployment
# Runs both user_bot and admin_bot as separate threads

import asyncio
import sys
from typing import NoReturn
import signal

from utils.logger import get_logger
from config.settings import settings

logger = get_logger(__name__)


async def run_user_bot() -> None:
    """
    Run user bot (placeholder for actual implementation)
    
    TODO: Import and run the actual user bot
    from user_bot import main as user_bot_main
    await user_bot_main()
    """
    logger.info("User Bot started")
    # await user_bot_main()


async def run_admin_bot() -> None:
    """
    Run admin bot (placeholder for actual implementation)
    
    TODO: Import and run the actual admin bot
    from admin_bot import main as admin_bot_main
    await admin_bot_main()
    """
    logger.info("Admin Bot started")
    # await admin_bot_main()


async def main() -> NoReturn:
    """
    Main entry point for Railway deployment
    Runs both bots concurrently using asyncio.TaskGroup
    """
    logger.info(f"Starting VPN Store Bot (Environment: {settings.environment})")
    logger.info(f"Database: {settings.database_url}")
    
    # Verify critical settings
    if not settings.get_user_bot_token():
        logger.error("USER_BOT_TOKEN not configured!")
        sys.exit(1)
    
    if not settings.get_admin_bot_token():
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
