from binance.client import Client
from binance.exceptions import BinanceAPIException  # <--- FIXED IMPORT
from trading_bot.config import API_KEY, SECRET_KEY
from trading_bot.logging_config import logger

class BinanceClientWrapper:
    def __init__(self):
        # Initialize the client.
        # We assume you are using the "Demo" keys.
        self.client = Client(API_KEY, SECRET_KEY, testnet=True)
        
        # OVERRIDE the API URL to match the "Demo" environment
        # If this URL fails later, we can try removing this line.
        self.client.FUTURES_URL = 'https://demo-fapi.binance.com/fapi'
        
        logger.info("Binance Client Initialized")

    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            params = {
                'symbol': symbol,
                'side': side.upper(),
                'type': order_type.upper(),
                'quantity': quantity,
            }

            # Add price only if it's a LIMIT order
            if order_type.upper() == 'LIMIT':
                if price is None:
                    raise ValueError("Price is required for LIMIT orders.")
                params['price'] = price
                params['timeInForce'] = 'GTC'  # Good Till Cancelled

            logger.info(f"Sending Order: {params}")

            # API Call
            response = self.client.futures_create_order(**params)
            
            logger.info(f"Order Success: ID {response.get('orderId')}")
            return response

        except BinanceAPIException as e:  # <--- FIXED EXCEPTION HANDLING
            logger.error(f"Binance API Error: {e.message}")
            return {"error": e.message}
        except Exception as e:
            logger.error(f"Unexpected Error: {str(e)}")
            return {"error": str(e)}