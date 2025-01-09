import os
# from alpaca.trading.client import TradingClient
from dotenv import load_dotenv

# from alpaca.data.historical import CryptoHistoricalDataClient
# from alpaca.data.requests import CryptoLatestQuoteRequest
from alpaca.data.live.crypto import CryptoDataStream

load_dotenv()
API_KEY=os.getenv("API_KEY")
SECRET=os.getenv("SECRET")

# keys are required for live data
crypto_stream = CryptoDataStream(API_KEY, SECRET)

async def my_print(data):
    # quote data will arrive here
    print(data)

crypto_stream.subscribe_quotes(my_print, "BTC/USD")
crypto_stream.run()
# no keys required
# client = CryptoHistoricalDataClient()

# single symbol request
# request_params = CryptoLatestQuoteRequest(symbol_or_symbols="ETH/USD")

# latest_quote = client.get_crypto_latest_quote(request_params)

# must use symbol to access even though it is single symbol
# latest = latest_quote["ETH/USD"].ask_price


# trading_client = TradingClient(API_KEY, SECRET)
# print(latest)
# print(trading_client.get_account().account_number)
# print(trading_client.get_account().buying_power)