#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from binance.client import Client




def main(api_key, api_secret, list_of_coin_pairs_to_trade_with, base_currency, polling_delay):
    client = Client(api_key, api_secret)
    all_prices = client.get_all_tickers()

    print(all_prices)

    print("Starting Main Execution")

    # Keep on polling until we want to exit the program
    while True:

        # Read Prices
        price_list = getPrices(client)

        # Determine if we need to execute order
        isProfitable = isThreewayTradeProfitable(price_list, base_currency, list_of_coin_pairs_to_trade_with)

        if isProfitable:
            orders_to_execute_tuple = calculateOrdersToExecutee(price_list, base_currency, list_of_coin_pairs_to_trade_with)

        # Execute orders - Future implementation; make this MULTI-THREADED
        all_orders_executed = False
        time_limit = 60000
        start_time = time.time()

        # Issue orders


        # NOTE: THIS IS ONLY VERSION 1, WE WILL MAKE A SMARTER ALGORITHM LATER
        # Poll until orders execute
        while (not all_orders_executed) or (time.time() - start_time) < time_limit:
            # Verify all orders execute, or accept loss

            all_orders_executed = checkIfAllOrdersExecuted(orders_to_execute_tuple)

        # Report updated balances
        displayBalances(list_of_coin_pairs_to_trade_with)

        print("Pausing for {} seconds".format(polling_delay))

        pass

def getPrices(client):
    # TODO
    pass

def isThreewayTradeProfitable(client, price_list, base_currency, list_of_coin_pairs_to_trade_with):
    # TODO
    pass

def calculateOrdersToExecutee(client, price_list, base_currency, list_of_coin_pairs_to_trade_with):
    # TODO
    pass

def checkIfAllOrdersExecuted(client, orders_to_execute_tuple):
    # TODO
    pass

def displayBalances(client, list_of_coin_pairs_to_trade_with):
    # TODO
    pass

if __name__ == '__main__':

    # Hard-code variables for now, will use commandline input later
    trading_pairs_list = ['ETHUSDT', 'EOSUSDT', 'EOSETH']
    base_currency = 'USDT'
    polling_delay = 5

    api_file = '../../keys.txt'

    with open(api_file, 'r', encoding='utf-8') as f:
        api_key = f.readline().strip()
        api_secret = f.readline().strip()

    print("key: {}".format(api_key))
    print("secret: {}".format(api_secret))

    main(api_key, api_secret, trading_pairs_list, base_currency, polling_delay)
