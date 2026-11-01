# Estudiante: Julián Fernando Bravo Parra
# Código: 2503120
# Fecha de elaboración: 28/10/2026

import yfinance as yf
from datetime import date
import sys


def get_stock_data(sd, stock, ed=date.today()):
    return yf.download(stock, sd, ed)


def test(ticker="GOOGL"):
    start_date = "2020-01-01"
    return get_stock_data(start_date, ticker)


if __name__ == "__main__":
    ticker = "GOOGL"
    if len(sys.argv) == 2:
        ticker = sys.argv[1]

    print(f"Se recuperará información del stock {ticker}")
    data = test(ticker)
    print(data.tail())
    print("Promedio de Close:", data["Close"].mean().item())
