#! /usr/bin/env nix-shell
#! nix-shell --pure -i python


#import matplotlib
#import matplotlib.pyplot as plt
import yfinance as yf
import sys

#print('Number of arguments:', len(sys.argv), 'arguments.')
#print('Argument List:', str(sys.argv))
#print('StartDate : EndDate: ', start_date_str, ':', end_date_str)

#matplotlib.use("TkAgg")
#plt.ion()

if len(sys.argv) == 5:
    # symbol, start date, end date and interval input
    symbol = sys.argv[1]
    #print('Symbol: ', symbol)

    start_date_str = sys.argv[2]
    end_date_str = sys.argv[3]
    interval_str = sys.argv[4]

    print('Symbol: ', symbol)
    print('start date: ', start_date_str)
    print('end date: ', end_date_str)
    print('interval: ', interval_str)

elif len(sys.argv) == 4:
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
    interval_str = '1d'
elif len(sys.argv) == 2:
    # symbol input
    symbol = sys.argv[1]
    start_date_str = None
    end_date_str = None
    interval_str = '1d'
else:
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


# useful place to see what type of intervals that are allowed
# https://stackoverflow.com/questions/65254272/yfinance-dont-see-time-on-day-when-choosing-one-hour-intervals

symbol_ticker = yf.Ticker(symbol)

if(start_date_str is not None and end_date_str is not None and interval_str != '1d'):
    symbol_df = symbol_ticker.history(start=start_date_str, end=end_date_str, interval=interval_str)
else:
    symbol_df = symbol_ticker.history(period="max")

used_mask = get_combined_mask(start_date_str, end_date_str, symbol_df)

#print('used mask: ')
# print(used_mask)
#print("symb debug line")
# print(symbol_df.head())

#plt.figure(1)
symbol_df.loc[used_mask].to_csv(symbol + '.csv')
#print("before savefig")
#plt.savefig(symbol + '.png')
#print("after savefig")
