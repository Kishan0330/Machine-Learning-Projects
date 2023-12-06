# Stock Price Prediction using LSTM Model

## Overview

This project focuses on predicting stock prices using a Long Short-Term Memory (LSTM) model. The LSTM model is implemented using the Keras library, and the project includes a web dashboard built with Dash for visualizing stock data.

## Prerequisites

Make sure you have the necessary libraries installed. You can install them using the following:

```bash
pip install dash dash-core-components dash-html-components pandas plotly keras scikit-learn
```

## Data Sources

1. **NSE-Tata-Global-Beverages-Limited.csv:** Historical stock data for Tata Global Beverages Limited.

2. **stock_data.csv:** Additional stock data for analysis.

## Web Dashboard

The project includes a web dashboard with two tabs:

### 1. NSE-TATAGLOBAL Stock Data

This tab displays the actual closing price history and LSTM-predicted closing prices for NSE-TATAGLOBAL stock.

- **Actual closing price:** A scatter plot showing the actual closing prices over time.
- **LSTM Predicted closing price:** A scatter plot displaying the predicted closing prices using the LSTM model.

### 2. Facebook Stock Data

This tab presents visualizations for Facebook stock data, allowing you to select multiple stocks (Tesla, Apple, Facebook, Microsoft) for analysis.

- **High vs Lows:** Line charts comparing the high and low prices for the selected stocks over time.
- **Market Volume:** Line chart representing the transaction volume for the chosen stocks.

## LSTM Model

### Model Training

The LSTM model is trained using historical stock data, specifically the closing prices of NSE-TATAGLOBAL stock. The training data is scaled using MinMaxScaler to ensure uniformity.

The model architecture includes:
- Two LSTM layers with 50 units each.
- One Dense layer with a single unit.

The model is compiled using the Adam optimizer and trained for one epoch.

### Model Prediction

The trained LSTM model is then used to predict future stock prices. The web dashboard visualizes the actual and predicted closing prices, allowing for easy comparison.

### Saving the Model

The trained LSTM model is saved for future use, using the HDF5 file format. Note: It is recommended to use the native Keras format for newer applications.

## Instructions

1. Ensure all required libraries are installed.
2. Run the Dash application using the provided code.
3. Navigate to the provided local server (e.g., http://127.0.0.1:8050/) to access the web dashboard.
4. Explore the NSE-TATAGLOBAL stock data and Facebook stock data tabs for insights into stock prices and predictions.

## Notes

- The project demonstrates proficiency in time series analysis, LSTM model implementation, and web dashboard creation.
- It is essential to have a reliable internet connection to fetch stock data.
- Keep the project dependencies updated for optimal performance.

