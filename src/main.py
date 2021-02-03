#!/usr/bin/env python3
import cira
import random
import time

"""
Description of your project
"""

__author__ = "Your Name"
__version__ = "0.1.0"
__license__ = "MIT"

cira.alpaca.KEY_FILE = "/home/axel/Programs/repositories/paper-trader/key.json"

portfolio = cira.Portfolio()
exchange = cira.Exchange()

DEBUG = True


def main():
    while exchange.is_open:
        print(exchange.symbols)
        for stk in random.choices(exchange.stocks, k=1):
            stk.buy(1)
        for stk in portfolio.owned_stocks:
            if stk.plpc < -0.5 or stk.plpc > 1.5: # cut your losses and take your gains
                stk.sell(1)
        time.sleep(60*30) # 30 min timer 


if __name__ == "__main__":
    main()