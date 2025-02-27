import os
from dotenv import load_dotenv

from alpha_vantage_client import AlphaVantageClient
from coin_api_client import CoinAPIClient
from bird_eye_client import BirdeyeClient
from coin_api_naas_client import CoinAPINaaSClient


def main():
    """
    Main function to initialize API clients and fetch market data.
    Loads API keys from the environment and makes example API calls.
    """
    # Load environment variables from .env file
    load_dotenv()

    # Access API keys from environment variables
    alpha_vantage_api_key = os.getenv("ALPHA_VANTAGE_KEY")
    coinapi_api_key = os.getenv("COINAPI_KEY")
    coinapi_naas_api_key = os.getenv("COINAPI_NAAS_KEY")
    birdeye_api_key = os.getenv("BIRDEYE_KEY")

    if not all([alpha_vantage_api_key, coinapi_api_key, birdeye_api_key, coinapi_naas_api_key]):
        print("Error: One or more API keys are missing. Please check your .env file.")
        return

    # Initialize API clients
    alpha_client = AlphaVantageClient(alpha_vantage_api_key)
    coinapi_client = CoinAPIClient(coinapi_api_key)
    coinapi_naas_client = CoinAPINaaSClient(coinapi_naas_api_key)
    birdeye_client = BirdeyeClient(birdeye_api_key)

    # Fetch data using Alpha Vantage API
    print("Fetching daily time series for BTC...")
    print(alpha_client.get_daily_time_series("BTC"))

    print("Fetching intraday time series for BTC...")
    print(alpha_client.get_intraday_time_series("BTC"))

    print("Fetching BTC to USD exchange rate...")
    print(alpha_client.get_crypto_price("BTC", "USD"))

    # Fetch data using CoinAPI
    print("Fetching asset info for BTC...")
    print(coinapi_client.get_asset_info("BTC"))

    print("Fetching BTC to USD exchange rate...")
    print(coinapi_client.get_exchange_rate("BTC", "USD"))

    print("Fetching OHLCV data for BTC...")
    print(coinapi_client.get_ohlcv("BITSTAMP_SPOT_BTC_USD"))

    # Example usage
    print("Fetching block details for block number 17000000...")
    print(coinapi_naas_client.get_block_by_number(17000000))

    print("Fetching transaction details for a sample hash...")
    print(coinapi_naas_client.get_transaction_by_hash("0xSampleTransactionHash"))

    print("Fetching account balance for a sample address...")
    print(coinapi_naas_client.get_account_balance("0xSampleEthereumAddress"))

    # Fetch data using Birdeye API
    print("Fetching trending tokens...")
    print(birdeye_client.get_trending_tokens())

    print("Fetching token list...")
    print(birdeye_client.get_token_list())

    print("Fetching token price for SOL...")
    print(birdeye_client.get_token_price("So11111111111111111111111111111111111111112"))


if __name__ == "__main__":
    main()
