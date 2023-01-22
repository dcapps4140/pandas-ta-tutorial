from datetime import datetime
# import module sys to get the type of exception
import sys, time
import yfinance as yf
import pandas_ta as ta
import pandas as pd
from yahoo_fin import stock_info as si

# Define non-default RSI parameters
rsi_period = 7
rsi_wilder = False

# Set custom MACD parameters
fast_period = 12
slow_period = 26
signal_period = 9
#
n = 0
# Get Data
stocklist = si.tickers_sp500()
date = datetime.today().strftime('%Y-%m-%d-%H-%M')

try:

    for stock in stocklist:
        print('Process started.')
        try:  # run the procedure inside of an error trap
        #
            n += 1
            time.sleep(1)

            print ("\npulling {} with index {}".format(stock, n))
            ticker = yf.Ticker(stock)
            df = ticker.history(period="1y")
            # 
            #print(df)

            adx = ta.adx(df['High'], df['Low'], df['Close'])

            adx = df.ta.adx()

            stoch = ta.stoch(df['High'], df['Low'], df['Close'], 14, 3, 3)#STOCHk_14_3_3  STOCHd_14_3_3

            macd = df.ta.macd(fast=fast_period, slow=slow_period, signal=signal_period)#MACD_12_26_9  MACDh_12_26_9  MACDs_12_26_9

            rsi = df.ta.rsi(rsi_period)

            df = pd.concat([df, adx, stoch, macd, rsi], axis=1)

            df = df[df['RSI_7'] < 30]

            print()
            last_row = df.iloc[-1]

            if last_row['STOCHk_14_3_3'] >= 50:
                message = f"!Possible Uptrend: The Stoch %k is {last_row['STOCHk_14_3_3']:.2f}"
                print(message)
            else:
                message = f"The Stoch %k is {last_row['STOCHk_14_3_3']:.2f}"
                print(message)

            if last_row['RSI_7'] >= 50:
                message = f"!Possible Uptrend: The RSI_7 is {last_row['RSI_7']:.2f}"
                print(message)
            else:
                message = f"The RSI_7 is {last_row['RSI_7']:.2f}"
                print(message)

            if last_row['MACD_12_26_9'] > last_row['MACDs_12_26_9']:
                message = f"!Possible Uptrend: The MACD > Sig is {last_row['MACD_12_26_9']:.2f}"
                print(message)
            else:
                message = f"The MACD_12_26_9 is {last_row['MACD_12_26_9']:.2f}"
                print(message)
        #
        # what happens when we have an error
        except ConnectionError as e:
            print("There was a ConnectionError", e)
            pass
        except FileNotFoundError as e:
            print("There was a FileNotFoundError", e)
            pass
        except KeyboardInterrupt as e:
            print("There was a KeyboardInterrupt", e)
            pass
        except KeyError as e:
            print("There was a KeyError", e)
            pass
        except NameError as e:
            print("There was a NameError", e)
            pass
        except IOError as e:
            print("There was a I/O error", e)
            pass
        except RuntimeError as e:
            print("There was a RuntimeError", e)
            pass
        except SyntaxError as e:
            print("There was a SyntaxError", e)
            pass
        except SystemError as e:
            print("There was a SystemErrors", e)
            pass
        except TypeError as e:
            print("There was a TypeError", e)
            pass
        except ValueError as e:
            print("There was a ValueError", e)
            pass
        except ZeroDivisionError as e:
            print("There was a ZeroDivisionError", e)
            pass
        except:
            print("Exception ", sys.exc_info()[0], "occurred!")
            #
        else:  # what happens when we don't have an error
            #
            print()
            print('No exception occured for this ticker.')
            #
        finally:  # what happpens no matter what
            #print('Processing complete.')
            #print(date)
            pass
except:
    print("Exception ", sys.exc_info()[0], "occurred!")
    #
else:  # what happens when we don't have an error
    #
    print("**************************")
    print('No exception occured and was passed to top level try.')
    #
finally:  # what happpens no matter what
    print('Processing complete.')
    print(date)
