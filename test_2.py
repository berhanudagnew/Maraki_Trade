# import asyncio
# from get_live_data import GetLiveData
# from order import Order

# order_1  = Order()

# symbol, interval, limit = order_1.my_order()
# update_api_data = GetLiveData(symbol, interval, limit)
# asyncio.run(update_api_data.market_data())

import threading
import time
import schedule
from get_live_data import GetLiveData
from live_test_strategy import LiveMethodOne

def get_live_data(num):
    live_data = GetLiveData()
    live_data.live_test_data()
def get_live_print():
    print('Stratagy running ... ')
    start_time_stratagy = time.perf_counter()
    t2 = threading.Thread(target=live_stratagy, args=(10,))
    t2.start()
    t2.join()
    end_time_stratagy = time.perf_counter()
    print(f'stratagy waits {end_time_stratagy - start_time_stratagy} seconds')
    print('Done Stratagy !')
    return

def live_stratagy(num):
    live_method = LiveMethodOne()
    live_method.live_method()
    

def start_bot():
    print('API running ... ')
    start_time_get_data = time.perf_counter()
    # creating threade
    t1 = threading.Thread(target=get_live_data, args=(10,))
    # start trade 1
    t1.start()

    

    # wait untill threade 1 is completly excuted
    t1.join()

    end_time_get_data = time.perf_counter()
    print(f'API waits {end_time_get_data - start_time_get_data} seconds')
    print('Done API !')
    return

schedule.every(0.01).seconds.do(start_bot)
schedule.every(0.01).seconds.do(get_live_print)

while True:
    start_bot_time = time.perf_counter()
    schedule.run_pending()
    time.sleep(0.01) # wait one seconds
    end_bot_time = time.perf_counter()
    print(f'Total time : {end_bot_time - start_bot_time: 0.2f} seconds')