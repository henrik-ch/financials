#! /usr/bin/env nix-shell
#! nix-shell --pure -i python


import matplotlib
import matplotlib.pyplot as plt
import yfinance as yf
import sys

#print('Number of arguments:', len(sys.argv), 'arguments.')
#print('Argument List:', str(sys.argv))


#symbol = sys.argv[1]
#print('Symbol: ', symbol)

#start_date_str = sys.argv[2]
#end_date_str = sys.argv[3]

#print('StartDate : EndDate: ', start_date_str, ':', end_date_str)

matplotlib.use("TkAgg")
plt.ion()

vti_ticker = yf.Ticker("VTI")
vti_df = vti_ticker.history(period="max")

dji_ticker = yf.Ticker("^DJI")
dji_df = dji_ticker.history(period="max")

spy_ticker = yf.Ticker("SPY")
spy_df = spy_ticker.history(period="max")

#airx_ticker = yf.Ticker("AIRX.OL")
#airx_df = airx_ticker.history(period="max")


plt.figure(1)
dji_df.loc["2001-06-15":]["Close"].plot(title="^DJI")
plt.savefig('DJI.png')

plt.figure(2)
spy_df.loc["2001-06-15":]["Close"].plot(title="SPY")
plt.savefig('SPY.png')

plt.figure(3)
vti_df["Close"].plot(title="VTI")
plt.savefig('VTI.png')

