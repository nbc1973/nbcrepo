# GUI Stock Scanner Plan

This document outlines a basic plan for building a graphical stock scanner with prediction capabilities.

## 1. Goals

- Provide a user-friendly GUI that lists recommended stocks to buy.
- Display interactive historical price charts for selected stock symbols.
- Integrate an AI-based model to predict future stock prices.

## 2. Key Components

1. **Data Retrieval**
   - Use a stock market API (e.g., Alpha Vantage or IEX Cloud) to fetch historical and real-time prices.
   - Store data locally (CSV or lightweight database) for quick access.

2. **GUI Framework**
   - Python with a toolkit such as Tkinter, PyQt, or Kivy for cross-platform compatibility.
   - Main window: list of tracked stocks with basic metrics (price, change %, volume, etc.).
   - Chart window or panel using a plotting library (e.g., Matplotlib or Plotly) to visualize price history.

3. **AI Prediction Model**
   - Collect historical price data for training.
   - A simple approach: use LSTM (Long Short-Term Memory) neural networks for time series forecasting.
   - Train the model offline; use the trained model in the GUI to generate short-term predictions.
   - Provide disclaimers that predictions are for informational purposes only, not financial advice.

4. **Stock Selection Logic**
   - Basic filtering based on moving averages, volume, or momentum indicators.
   - Optionally allow the user to input their own criteria or upload a list of symbols.

5. **Architecture Outline**
   - `data/` — handles fetching and caching stock data.
   - `models/` — AI prediction code and saved models.
   - `ui/` — all GUI code and event handling.
   - `main.py` — entry point tying components together.

## 3. Implementation Steps

1. Set up project structure (`data`, `models`, `ui`).
2. Implement data-fetching functions with API keys stored in environment variables.
3. Build a basic GUI to display a stock list and open a chart window when a symbol is selected.
4. Integrate Matplotlib or Plotly to plot historical data.
5. Train a simple LSTM model on historical prices and export it.
6. Add a prediction pane or overlay in the chart to show future price estimates.
7. Package the app so users can run it easily (PyInstaller or a Docker setup).

## 4. Considerations

- Respect API usage limits and cache data to avoid unnecessary calls.
- Keep the model simple to start, then iterate with additional indicators (e.g., RSI, MACD).
- UI design should prioritize clarity and not overwhelm the user with details.
- Provide a disclaimer about financial risk and that predictions are not guaranteed.

