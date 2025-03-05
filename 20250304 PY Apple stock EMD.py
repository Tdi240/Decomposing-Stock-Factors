#!pip install EMD-signal
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
from PyEMD import EMD

# Fetch Apple stock data from Yahoo Finance
def fetch_stock_data(ticker, start_date, end_date):
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data

# Calculate daily returns and drop NaNs
def calculate_returns(stock_data):
    stock_data['Daily Return'] = stock_data['Close'].pct_change()  # This introduces NaN in the first row
    return stock_data['Daily Return'].dropna()

# Perform EMD on the returns
def perform_emd(returns):
    emd = EMD()
    IMFs = emd(returns.values)
    return IMFs

# Plot the results
def plot_results(returns, IMFs):
    plt.figure(figsize=(12, 10), facecolor='none')  # Transparent background

    # Plot the original returns
    plt.subplot(len(IMFs) + 1, 1, 1)
    plt.plot(returns.index, returns, label='Apple Daily Returns', color='blue', linewidth=2.5)
    plt.legend()
    plt.title('Apple Daily Returns')

    # Plot each IMF
    for i, imf in enumerate(IMFs):
        plt.subplot(len(IMFs) + 1, 1, i + 2)
        plt.plot(returns.index, imf, label=f'IMF {i + 1}', color='orange', linewidth=2.5)
        plt.legend()

    plt.tight_layout()

    # Save the plot with a transparent background
    plt.savefig('AAPL_EMD_plot.png', transparent=True)

    # Show the plot
    plt.show()

# Main script
if __name__ == "__main__":
    # Define parameters
    ticker = 'AAPL'  # Apple stock ticker
    start_date = '2020-01-01'
    end_date = '2023-01-01'

    # Fetch stock data
    stock_data = fetch_stock_data(ticker, start_date, end_date)

    # Calculate daily returns
    returns = calculate_returns(stock_data)

    # Perform EMD
    IMFs = perform_emd(returns)

    # Plot the results
    plot_results(returns, IMFs)

