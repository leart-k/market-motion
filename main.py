# yfinance - financial data from Yahoo Finance
# ipyvuetify - interactive web UI with Vuetify components
# cufflinks - simplified data visualization
# mercury - notebook to web app

# libraries
import pandas as pd
import cufflinks as cf
cf.go_offline() # offline mode config
import numpy as np
import yfinance as yf
from datetime import date
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import mercury as mr
from dateutil.relativedelta import relativedelta

# mercury app intialisation
app = mr.App(title="📈 Market Motion", description="Dashboard with financial data", show_code=False)

# picking some stocks
ticker = mr.Select(label="Select ticker", value='NVDA', choices=['NVDA', 'INTC', 'AMD', 'TSM', 'MU'])

mr.Md(f"# Selected ticker: {ticker.value}")

# custom time period
period = mr.Numeric(label="Past Month(s)", value=3, min=1, max=12)

# NVIDIA stock data
stock_data = yf.download(ticker.value, start=date.today() - relativedelta(months=+period.value), end=date.today(), auto_adjust=False)
stock_data

print(stock_data)

# Plots of NVDA's Adjusted Close Prices
stock_data['Adj Close'].iplot(title='Adjusted Close', colors=['rgb(0,128,0)'])

stock_data[['Adj Close']].iplot(title='Adjusted Close (Filled Area)', fill=True, colors=['rgb(0,128,0)'])

stock_data['Adj Close'].iplot(title='Returns', bestfit=True, bestfit_colors=['black'])
