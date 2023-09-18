#(5/5 points) Initial comments with your name, class and project at the top of your .py file.
# INF601 - Advanced Programming in Python
# Derrick Aragon
# Mini Project 1

#(5/5 points) Proper import of packages used.
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


#(20/20 points) Using an API of your choice (yfinance works), collect the closing price of 5 of your favorite stock tickers for the last 10 trading days.


def getClosing(ticker):
    # Gets last 10 closing prices
    stock = yf.Ticker(ticker)
    # Get historical market data
    hist = stock.history(period="10d")

    # Creates closing list for msft
    closingList = []

    # Loops through closing prices and adds them to the list
    for price in hist['Close']:
        closingList.append(price)

    print(closingList)

    return closingList

# Creates the charts folder
try
    Path("charts").mkdir()
except FileExistsError:
    pass

#(10/10 points) Store this information in a list that you will convert to a array in NumPy.

stocks = ["MSFT", "NVDA", "AMC", "WMT", "NTDOY"]

for stock in stocks:

    stockClosing = np.array(getClosing(stock))

    days = list(range(1, len(stockClosing)+1))

    # (10/10 points) Plot these 5 graphs. Feel free to add as much information to the graphs as you like exploring the documentation for matplotlib. At minimum it just needs to show 10 data points.

    # Plots the graph
    plt.plot(days, stockClosing)

    # Gets min and max for Y
    prices = getClosing(stock)
    prices.sort()
    low_price = prices[0]
    high_price = prices[-1]

    # X form [xmin, xmax, ymin, ymax]
    plt.axis([1,10, low_price-2, high_price+2])


    # Labels for the graph
    plt.xlabel(days)
    plt.ylabel("Closing Price")
    plt.title("Closing Price for " + stock)

    # (10/10 points) Save these graphs in a folder called charts as PNG files. Do not upload these to your project folder, the project should save these when it executes. You may want to add this folder to your .gitignore file.

    # Saves the charts before showing so it doesn't appear blank
    savefile = "charts/" + stock + ".png"
    plt.savefig(savefile)

    # Shows the actual graphs
    plt.show()



#(10/10 points) There should be a minimum of 5 commits on your project, be sure to commit often!
#(10/10 points) I will be checking out the master branch of your project. Please be sure to include a requirements.txt file which contains all the packages that need installed. You can create this fille with the output of pip freeze at the terminal prompt.
#(20/20 points) There should be a README.md file in your project that explains what your project is, how to install the pip requirements, and how to execute the program. Please use the GitHub flavor of Markdown.


