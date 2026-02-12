import argparse
import sys
from trading_bot.client import BinanceClientWrapper
from rich.console import Console
from rich.table import Table

console = Console()

def print_result(response):
    """
    Prints a clear summary of the order execution [cite: 27-29].
    """
    if "error" in response:
        console.print(f"[bold red]Failed:[/bold red] {response['error']}")
        return

    # Create a pretty table for the output
    table = Table(title="Order Execution Details")
    table.add_column("Field", style="cyan")
    table.add_column("Value", style="magenta")

    table.add_row("Order ID", str(response.get('orderId')))
    table.add_row("Symbol", response.get('symbol'))
    table.add_row("Status", response.get('status'))
    table.add_row("Side", response.get('side'))
    table.add_row("Type", response.get('type'))
    table.add_row("Executed Qty", str(response.get('executedQty', '0')))
    
    console.print(table)
    console.print("[bold green]Order Placed Successfully![/bold green]")

def main():
    # Setup CLI arguments [cite: 20-26]
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")
    
    parser.add_argument("--symbol", type=str, required=True, help="Trading pair (e.g., BTCUSDT)")
    parser.add_argument("--side", type=str, required=True, choices=["BUY", "SELL"], help="Order side")
    parser.add_argument("--type", type=str, required=True, choices=["MARKET", "LIMIT"], help="Order type")
    parser.add_argument("--qty", type=float, required=True, help="Quantity to trade")
    parser.add_argument("--price", type=float, help="Price (Required for LIMIT orders)")

    args = parser.parse_args()

    try:
        # Initialize Client
        bot = BinanceClientWrapper()

        # Place Order
        console.print(f"[yellow]Placing {args.side} {args.type} order for {args.symbol}...[/yellow]")
        result = bot.place_order(args.symbol, args.side, args.type, args.qty, args.price)
        
        # Show Output
        print_result(result)

    except Exception as e:
        console.print(f"[bold red]Critical Error:[/bold red] {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()