#! /usr/bin/env nix-shell
#! nix-shell --pure -i python


import matplotlib
import matplotlib.pyplot as plt
import yfinance as yf
import sys

#print('Number of arguments:', len(sys.argv), 'arguments.')
#print('Argument List:', str(sys.argv))

#print('StartDate : EndDate: ', start_date_str, ':', end_date_str)

matplotlib.use("TkAgg")
plt.ion()


if len(sys.argv) == 4:
    # symbol, start date and end date input
    symbol = sys.argv[1]
    #print('Symbol: ', symbol)

    start_date_str = sys.argv[2]
    end_date_str = sys.argv[3]
elif len(sys.argv) == 3:
  # symbol, start date  input
    symbol = sys.argv[1]
    start_date_str = sys.argv[2]
    end_date_str = None
elif len(sys.argv) == 2:
    # symbol input
    symbol = sys.argv[1]
    start_date_str = None
    end_date_str = None
else:
  # do Y
  print("No symbol provided - aborting")
  exit()


def get_combined_mask(in_start_date, in_end_date, in_dataframe):
    if in_start_date is not None and in_end_date is not None:
        start_mask = in_dataframe.index > in_start_date
        end_mask = in_dataframe.index < in_end_date
        combined_mask = start_mask & end_mask
    elif in_start_date is not None:
        start_mask = in_dataframe.index > in_start_date
        combined_mask = start_mask
    else:
        combined_mask = in_dataframe.index == in_dataframe.index
    
    return combined_mask


symbol_ticker = yf.Ticker(symbol)
symbol_df = symbol_ticker.history(period="max")

used_mask = get_combined_mask(start_date_str, end_date_str, symbol_df)

#print('used mask: ')
#print(used_mask)
#print("symb debug line")
#print(symbol_df.head())

plt.figure(1)
symbol_df.loc[used_mask]["Close"].plot(title=symbol)
#print("before savefig")
plt.savefig(symbol + '.png')
#print("after savefig")


'''
vti_ticker = yf.Ticker("VTI")
vti_df = vti_ticker.history(period="max")

dji_ticker = yf.Ticker("^DJI")
dji_df = dji_ticker.history(period="max")

spy_ticker = yf.Ticker("SPY")
spy_df = spy_ticker.history(period="max")

airx_ticker = yf.Ticker("AIRX.OL")
airx_df = airx_ticker.history(period="max")

plt.figure(1)
dji_df.loc["2001-06-15":]["Close"].plot(title="^DJI")
plt.savefig('DJI.png')

plt.figure(2)
spy_df.loc["2001-06-15":]["Close"].plot(title="SPY")
plt.savefig('SPY.png')

plt.figure(3)
vti_df["Close"].plot(title="VTI")
plt.savefig('VTI.png')

plt.figure(4)
airx_df["Close"].plot(title="AIRX.OL")
plt.savefig('AIRXOL.png')
'''