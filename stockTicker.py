#Given a string representing a stock ticker:

"AAPL 313 GOOG 513 TSLA 58 BBY 22"

# ["AAPL", "GOOG", "TSLA", "BBY"]

# Write a function that returns the stocks alphabetized

def alphabetical_stocks(a):
  stock_arr = a.split(' ')
  i = 0
  stocks = []
  for i in range(0, len(stock_arr), 2):
    stock = stock_arr[i]
    stocks.append(stock)
  return ' '.join(sorted(stocks))


## Stretch

# Write a function that returns the cheapest priced stock symbol

test_1 = "AAPL 313 GOOG 513 TSLA 58 BBY 22" # BBY
test_2 = "NBA 12 AAPL 313 GOOG 513 TSLA 58 BBY 222" #NBA
test_3 = "NBA 11 AAPL 55 GOOG 22 TSLA 44 BBY 22" # NBA

print(alphabetical_stocks(test_1))


def cheapest_stock(a):
  stock_arr = a.split(' ')
  i = 0
  stocks = []
  d = {}
  cheapest = None
  for i in range(0, len(stock_arr), 2):
    stock = stock_arr[i]
    value = stock_arr[i+1]
    if cheapest is None or value < cheapest:
      cheapest = value
  return cheapest
  
print(cheapest_stock(test_3))

## Stretch 2

# Given an array of stock ticker strings, where one string represents a day of trading, 
# Write a function that finds the greatest window of return between two stocks
# and return the stock, the buy index, and the sell index
def greatest_return(trading):
  d = {}
  for a in trading:
    stock_arr = a.split(' ')
    i = 0
    stocks = []
    cheapest = None
    for i in range(0, len(stock_arr), 2):
      stock = stock_arr[i]
      value = int(stock_arr[i+1])
      if stock in d:
        d[stock].append(value)
      else:
        d[stock] = [value]
  
  best_overall_return = -1
  for key, stock_arr in d.items():
    best_return = 0
    min_price = float('inf')
    for p in stock_arr:
      min_price = min(min_price, p)
      profit = p - min_price
      best_return = max(best_return, profit)
    
    best_overall_return = max(best_return, best_overall_return)
  return  best_overall_return


test_3 = ["AAPL 114 GOOG 545 TSLA 33",
"AAPL 113 GOOG 533 TSLA 23",
"AAPL 112 GOOG 556 TSLA 34"]
print(greatest_return(test_3))
#[114, 113, 112]
#[545, 533, 556]

# "1 2 TSLA" - buy TSLA on day 1 and sell on day 2 for a 47% increase 
# https://coolconversion.com/math/percentage-change-calculator/_23_to_34_percent-increase-or-decrease
