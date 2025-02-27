import requests
from common_util import make_request_with_retry


class CoinAPIClient:
    """
    A client for fetching on-chain and market-related data from CoinAPI.
    See: https://www.coinapi.io/
    """
    BASE_URL = "https://rest.coinapi.io/v1/"

    def __init__(self, api_key):
        """
        Initializes the CoinAPI client with the provided API key.

        Args:
            api_key (str): The API key for authentication.
        """
        self.api_key = api_key
        self.headers = {"X-CoinAPI-Key": self.api_key}

    def get_ohlcv(self, symbol_id, period_id="1DAY", time_start=None, time_end=None):
        """
        Retrieve historical OHLCV data for a given symbol.

        Args:
            symbol_id (str): The unique symbol identifier, e.g., 'BITSTAMP_SPOT_BTC_USD'.
            period_id (str): The period for the OHLCV data (e.g., '1DAY', '1HRS').
            time_start (str): ISO8601 formatted start time (e.g., '2023-01-01T00:00:00').
            time_end (str): ISO8601 formatted end time.

        Returns:
            dict: A JSON object with the OHLCV data, or error information.
        """
        endpoint = f"{self.BASE_URL}ohlcv/{symbol_id}/history"
        params = {"period_id": period_id}
        if time_start:
            params["time_start"] = time_start
        if time_end:
            params["time_end"] = time_end
        try:
            # Make API request with retry logic
            response = make_request_with_retry(endpoint, params=params, headers=self.headers)
            response.raise_for_status()
            data = response.json()
            # Handle API errors or rate limits
            if "Error Message" in data or "Note" in data:
                return {"error": data.get("Error Message") or data.get("Note")}
            return data
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}

    def get_asset_info(self, asset_id):
        """
        Fetches metadata for a given asset.

        Args:
            asset_id (str): The symbol of the asset to retrieve metadata for (e.g., 'BTC').

        Returns:
            dict: JSON response containing asset metadata such as name, type, and other relevant information.
        """
        endpoint = f"{self.BASE_URL}assets/{asset_id}"
        try:
            # Make API request with retry logic
            response = make_request_with_retry(endpoint, headers=self.headers)
            response.raise_for_status()
            data = response.json()
            # Handle API errors or rate limits
            if "Error Message" in data or "Note" in data:
                return {"error": data.get("Error Message") or data.get("Note")}
            return data
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}

    def get_exchange_rate(self, asset_id_base, asset_id_quote):
        """
        Fetches real-time exchange rate between two assets.

        Args:
            asset_id_base (str): Base asset symbol (e.g., BTC).
            asset_id_quote (str): Quote asset symbol (e.g., USD).

        Returns:
            dict: JSON response containing exchange rate data.
        """
        endpoint = f"{self.BASE_URL}exchangerate/{asset_id_base}/{asset_id_quote}"
        try:
            # Make API request with retry logic
            response = make_request_with_retry(endpoint, headers=self.headers)
            response.raise_for_status()
            data = response.json()
            # Handle API errors or rate limits
            if "Error Message" in data or "Note" in data:
                return {"error": data.get("Error Message") or data.get("Note")}
            return data
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}
