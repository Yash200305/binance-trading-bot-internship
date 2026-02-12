import logging
import os

def setup_logger():
    # Create a logs directory if it doesn't exist
    if not os.path.exists('logs'):
        os.makedirs('logs')

    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("logs/trading_bot.log"),  # Writes to file
            logging.StreamHandler()  # Writes to console
        ]
    )
    return logging.getLogger("TradingBot")

# This is the variable that client.py is trying to import
logger = setup_logger()