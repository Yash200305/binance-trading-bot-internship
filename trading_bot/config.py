import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv("BINANCE_TESTNET_API_KEY")
SECRET_KEY = os.getenv("BINANCE_TESTNET_SECRET_KEY")

# Assignment Requirement: Use Testnet Base URL [cite: 10-11]
BASE_URL = "https://testnet.binancefuture.com"

if not API_KEY or not SECRET_KEY:
    raise ValueError("API credentials not found. Please check your .env file.")