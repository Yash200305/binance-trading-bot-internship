# Binance Futures Trading Bot (Testnet)

A simplified command-line interface (CLI) trading bot for the Binance Futures Testnet. This application allows users to place BUY and SELL orders (Market and Limit) directly from the terminal, with automated logging and error handling.

## Features
* [cite_start]**Order Types:** Supports both **MARKET** and **LIMIT** orders[cite: 18].
* [cite_start]**Sides:** Supports **BUY** (Long) and **SELL** (Short)[cite: 19].
* **Security:** API keys are loaded securely from a `.env` file.
* [cite_start]**Logging:** All requests, responses, and errors are logged to `logs/trading_bot.log`[cite: 32].
* **Validation:** robust input validation for symbols, quantities, and prices.

## Prerequisites
* [cite_start]Python 3.x [cite: 16]
* A Binance Futures Testnet Account (or Demo Account)

## [cite_start]Installation & Setup [cite: 39]

1.  **Clone or Download the Repository**
    ```bash
    # If using git
    git clone <repository-url>
    cd binance_trading_bot
    ```

2.  **Install Dependencies**
    Install the required Python libraries using `pip`:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure API Keys**
    Create a file named `.env` in the root directory and add your Testnet API credentials:
    ```ini
    BINANCE_TESTNET_API_KEY=your_api_key_here
    BINANCE_TESTNET_SECRET_KEY=your_secret_key_here
    ```

## [cite_start]Usage [cite: 40]

Run the bot using `main.py` with the required arguments.

### 1. Place a MARKET Order
Executes immediately at the current market price.
```bash
python main.py --symbol BTCUSDT --side BUY --type MARKET --qty 0.002
```

### 1. Place a LIMIT order
Places an order at a specific price. Requires the --price argument.
```bash
python main.py --symbol BTCUSDT --side SELL --type LIMIT --qty 0.002 --price 95000
```

---

### **Chunk 2: The Rest of the File (Paste this BELOW the Usage section)**
This part contains the table and project structure.

```markdown
### Command Line Arguments

| Argument | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `--symbol` | str | Yes | Trading pair (e.g., BTCUSDT, ETHUSDT) |
| `--side` | str | Yes | Order side: `BUY` or `SELL` |
| `--type` | str | Yes | Order type: `MARKET` or `LIMIT` |
| `--qty` | float | Yes | Quantity to trade (Must be > $100 value on Testnet) |
| `--price` | float | No | Target price (Required only for `LIMIT` orders) |

## Project Structure

```text
binance_trading_bot/
│
├── .env                    # Environment variables (API Keys)
├── requirements.txt        # Python dependencies
├── main.py                 # CLI Entry point
├── README.md               # Project documentation
├── logs/                   # Log files directory
│   └── trading_bot.log     # Records of all API interactions
│
└── trading_bot/            # Main source code package
    ├── __init__.py
    ├── client.py           # Binance API wrapper & logic
    ├── config.py           # Configuration loader
    └── logging_config.py   # Logging setup
```
Assumptions
Environment: The bot is configured for the Binance Futures Testnet/Demo environment. It will not execute trades on the mainnet.

Network: The user has a stable internet connection to reach https://testnet.binancefuture.com or https://demo-fapi.binance.com.

Minimum Order Size: The Binance Testnet often rejects orders smaller than 100 USDT in value. The user must ensure --qty is sufficient (e.g., 0.002 BTC).

Time in Force: All LIMIT orders use GTC (Good Till Cancelled) by default.

Logs
Detailed logs of every operation can be found in: logs/trading_bot.log
