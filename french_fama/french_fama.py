import numpy as np
import pandas as pd

import pandas_datareader as pdr
import yfinance as yf

import statsmodels.api as sm
from statsmodels import regression
from statsmodels.regression.rolling import RollingOLS

# download the data
factors = pdr.get_data_famafrench(
    'F-F_Research_Data_Factors',
    start='2000-01-01'
)[0][1:]

SMB = factors.SMB
HML = factors.HML

# SMB is “small minus big” representing the size factor. HML is “high minus low” representing the style factor. 
# This also downloads a third factor, Rm-Rf, which is the market excess return. I only use SMB and HML for this analysis.

# Now get the stock price data for your portfolio. You can pick any stocks you want. (Make sure to include a benchmark like SPY.)

data = yf.download(
    ['SPY', 'MSFT', 'AAPL', 'TSLA'], 
    start="2000-01-01", 
    interval="1mo"
)['Adj Close']

monthly_returns = data.pct_change().to_period("M")

#The factor data is monthly so to align with the stock data, you need to get monthly closing prices and resample to monthly labels. pandas makes it easy.

# Step 2: Compute the sensitivities to the factors
# Next, compute the active return of the portfolio. The active return is the portfolio return minus the benchmark return.

bench = monthly_returns.pop("SPY")
R = monthly_returns.mean(axis=1)
active = R - bench

# “Pop” the benchmark return off the returns data frame. Then, calculate the portfolio returns and subtract the benchmark.

# Use regression to compute the sensitivities to the factors.

df = pd.DataFrame({
    'R': active,
    'F1': SMB,
    'F2': HML,
}).dropna()

b1, b2 = regression.linear_model.OLS(
    df.R, 
    df[['F1', 'F2']]
).fit().params

print(f'Sensitivities of active returns to factors:\nSMB: {b1}\nHML: {b2}')

# Put the active returns and factors into a DataFrame to make it easy to align the dates. Then run a regression with the active returns as the dependent variable on the factors. Fitting the model gives you the two coefficients that determine the sensitivities of the portfolio’s active returns to the factors.

# The sensitivities are estimates so it’s important to see how they evolve through time with their confidence intervals.

exog_vars = ["SMB", "HML"]
exog = sm.add_constant(factors[exog_vars])
rols = RollingOLS(df.R, exog, window=12)
rres = rols.fit()
fig = rres.plot_recursive_coefficient(variables=exog_vars)

# Step 3: Figure out the risk contribution of the factors
# Marginal Contribution To Active Risk (MCTAR) measures the incremental active risk each additional factor introduces to your portfolio.

F1 = df.F1
F2 = df.F2

cov = np.cov(F1, F2)
ar_squared = (active.std())**2
mcar1 = (b1 * (b2 * cov[0,1] + b1 * cov[0,0])) / ar_squared
mcar2 = (b2 * (b1 * cov[0,1] + b2 * cov[1,1])) / ar_squared
print (f'SMB risk contribution: {mcar1}')
print (f'HML risk contribution: {mcar2}')
print (f'Unexplained risk contribution: {1 - (mcar1 + mcar2)}')

# To figure out the factors' MCTAR, multiply the factor sensitivity by the covariance between the factors. 
# Then divide by the standard deviation of the active returns, squared.

# This tells you how much risk you take on by being exposed to each factor given the other factors you’re already exposed to. 
# The unexplained risk contribution is the exposure you have to other factors outside of the two you analyzed.

# You can use this analysis to increase or decrease your exposure to these factors. 
# You would do this by under- or overweighting the stocks that represent these factors (e.g. large cap or value).