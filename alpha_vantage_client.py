import requests
from common_util import make_request_with_retry


class AlphaVantageClient:
    """
    A client for fetching market data from Alpha Vantage.
    See: https://www.alphavantage.co/documentation/
    """

    def __init__(self, api_key):
        """
        Initializes the Alpha Vantage client with the provided API key.

        Args:
            api_key (str): The API key for authentication.
        """
        self.api_key = api_key
        self.base_url = "https://www.alphavantage.co/query"

    def get_crypto_price(self, symbol, market="USD"):
        """
        Fetches real-time cryptocurrency exchange rate.

        Args:
            symbol (str): The cryptocurrency symbol (e.g., BTC).
            market (str, optional): The currency to convert to (default is USD).

        Returns:
            dict: JSON response containing exchange rate data or an error message.
        """
        params = {
            "function": "CURRENCY_EXCHANGE_RATE",
            "from_currency": symbol,
            "to_currency": market,
            "apikey": self.api_key
        }
        try:
            # Make API request with retry logic
            response = make_request_with_retry(self.base_url, params=params)
            response.raise_for_status()
            data = response.json()
            # Handle API errors or rate limits
            if "Error Message" in data or "Note" in data:
                return {"error": data.get("Error Message") or data.get("Note")}
            return data
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}

    def get_daily_time_series(self, symbol):
        """
        Retrieve daily market data for a given stock symbol.

        Args:
            symbol (str): The stock symbol (e.g., AAPL).

        Returns:
            dict: JSON response containing daily time series data or an error message.
        """
        params = {
            "function": "TIME_SERIES_DAILY",
            "symbol": symbol,
            "apikey": self.api_key
        }
        try:
            # Make API request with retry logic
            response = make_request_with_retry(self.base_url, params=params)
            response.raise_for_status()
            data = response.json()
            # Handle API errors or rate limits
            if "Error Message" in data or "Note" in data:
                return {"error": data.get("Error Message") or data.get("Note")}
            return data
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}

    def get_intraday_time_series(self, symbol, interval="5min"):
        """
        Retrieve intraday market data for a given stock symbol.

        Args:
            symbol (str): The stock symbol (e.g., AAPL).
            interval (str, optional): Time interval between data points (default is "5min").

        Returns:
            dict: JSON response containing intraday time series data or an error message.
        """
        params = {
            "function": "TIME_SERIES_INTRADAY",
            "symbol": symbol,
            "interval": interval,
            "apikey": self.api_key
        }
        try:
            # Make API request with retry logic
            response = make_request_with_retry(self.base_url, params=params)
            response.raise_for_status()
            data = response.json()
            # Handle API errors or rate limits
            if "Error Message" in data or "Note" in data:
                return {"error": data.get("Error Message") or data.get("Note")}
            return data
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}
