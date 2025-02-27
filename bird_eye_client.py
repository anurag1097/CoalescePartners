import requests
from common_util import make_request_with_retry


class BirdeyeClient:
    """
    A client for fetching sentiment and token data from Birdeye.
    See: https://public-api.birdeye.so/
    """
    BASE_URL = "https://public-api.birdeye.so/defi"

    def __init__(self, api_key):
        """
        Initializes the Birdeye client with the provided API key.

        Args:
            api_key (str): The API key for authentication.
        """
        self.api_key = api_key
        self.headers = {"X-API-KEY": api_key, "Accept": "application/json"}

    def get_token_list(self, x_chain="solana", sort_by="v24hUSD", sort_type="desc"):
        """
        Fetches a list of available tokens from Birdeye.

        Args:
            x_chain (str, optional): The blockchain network (default is "solana").
            sort_by (str, optional): The field to sort by (default is "v24hUSD").
            sort_type (str, optional): The sorting order (default is "desc").

        Returns:
            dict: JSON response containing token list data or an error message.
        """
        endpoint = f"{self.BASE_URL}/tokenlist"
        params = {"sort_by": sort_by, "sort_type": sort_type}
        headers = self.headers.copy()
        headers.update({"x-chain": x_chain})
        try:
            # Make API request with retry logic
            response = make_request_with_retry(endpoint, params=params, headers=headers)
            response.raise_for_status()
            data = response.json()
            # Handle API errors
            if "error" in data:
                return {"error": data.get("error")}
            return data
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}

    def get_token_price(self, token_address, x_chain="solana"):
        """
        Fetches real-time price of a given token.

        Args:
            token_address (str): The address of the token.
            x_chain (str, optional): The blockchain network (default is "solana").

        Returns:
            dict: JSON response containing token price data or an error message.
        """
        endpoint = f"{self.BASE_URL}/price"
        params = {"address": token_address}
        headers = self.headers.copy()
        headers.update({"x-chain": x_chain})
        try:
            # Make API request with retry logic
            response = make_request_with_retry(endpoint, params=params, headers=headers)
            response.raise_for_status()
            data = response.json()
            # Handle API errors
            if "error" in data:
                return {"error": data.get("error")}
            return data
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}

    def get_trending_tokens(self, sort_by="rank", sort_type="asc", x_chain="solana"):
        """
        Fetches trending tokens from Birdeye.

        Args:
            sort_by (str, optional): The field to sort by (default is "rank").
            sort_type (str, optional): The sorting order (default is "asc").
            x_chain (str, optional): The blockchain network (default is "solana").

        Returns:
            dict: JSON response containing trending token data or an error message.
        """
        endpoint = f"{self.BASE_URL}/token_trending"
        params = {"sort_by": sort_by, "sort_type": sort_type}
        headers = self.headers.copy()
        headers.update({"x-chain": x_chain})
        try:
            # Make API request with retry logic
            response = make_request_with_retry(endpoint, params=params, headers=headers)
            response.raise_for_status()
            data = response.json()
            # Handle API errors
            if "error" in data:
                return {"error": data.get("error")}
            return data
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}
