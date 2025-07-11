import tkinter as tk
from tkinter import messagebox
import yfinance as yf


def fetch_stock_data(symbol):
    try:
        ticker = yf.Ticker(symbol)
        data = ticker.history(period="1d")
        if data.empty:
            return None
        latest = data.iloc[-1]
        return {
            "symbol": symbol.upper(),
            "open": latest["Open"],
            "high": latest["High"],
            "low": latest["Low"],
            "close": latest["Close"],
            "volume": int(latest["Volume"]),
        }
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None


def on_scan():
    symbol = entry.get().strip()
    if not symbol:
        messagebox.showwarning("Input Error", "Please enter a ticker symbol")
        return
    result = fetch_stock_data(symbol)
    if not result:
        messagebox.showerror("Error", f"No data found for {symbol}")
        return
    output_text.set(
        f"Symbol: {result['symbol']}\n"
        f"Open: {result['open']:.2f}\n"
        f"High: {result['high']:.2f}\n"
        f"Low: {result['low']:.2f}\n"
        f"Close: {result['close']:.2f}\n"
        f"Volume: {result['volume']}"
    )


root = tk.Tk()
root.title("Stock Scanner")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

entry_label = tk.Label(frame, text="Ticker Symbol:")
entry_label.grid(row=0, column=0, sticky="e")
entry = tk.Entry(frame)
entry.grid(row=0, column=1)
scan_button = tk.Button(frame, text="Scan", command=on_scan)
scan_button.grid(row=0, column=2, padx=5)

output_text = tk.StringVar()
output_label = tk.Label(frame, textvariable=output_text, justify="left")
output_label.grid(row=1, column=0, columnspan=3, pady=10)

root.mainloop()
