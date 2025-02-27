import requests
import json
from common_util import make_request_with_retry


class CoinAPINaaSClient:
    """
    A client for fetching on-chain blockchain data using CoinAPI NaaS.
    See: https://docs.coinapi.io/naas-api/
    """
    BASE_URL = "https://ethereum-mainnet-geth-archive.node.coinapi.io"

    def __init__(self, api_key):
        """
        Initializes the CoinAPI NaaS client with the provided API key.

        Args:
            api_key (str): The API key for authentication.
        """
        self.api_key = api_key
        self.headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "X-CoinAPI-Key" : self.api_key

        }

    def get_block_by_number(self, block_number):
        """
        Fetches block details by block number.

        Args:
            block_number (int): The block number to retrieve.

        Returns:
            dict: JSON response containing block details.
        """
        payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "eth_getBlockByNumber",
            "params": [hex(block_number), True]
        }
        return self._make_request(payload)

    def get_transaction_by_hash(self, tx_hash):
        """
        Fetches transaction details by transaction hash.

        Args:
            tx_hash (str): The transaction hash.

        Returns:
            dict: JSON response containing transaction details.
        """
        payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "eth_getTransactionByHash",
            "params": [tx_hash]
        }
        return self._make_request(payload)

    def get_account_balance(self, address):
        """
        Fetches the account balance of a given Ethereum address.

        Args:
            address (str): The Ethereum address.

        Returns:
            dict: JSON response containing the balance in Wei.
        """
        payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "eth_getBalance",
            "params": [address, "latest"]
        }
        return self._make_request(payload)

    def _make_request(self, payload):
        """
        Helper method to send a JSON-RPC request to the CoinAPI NaaS endpoint.

        Args:
            payload (dict): The JSON-RPC request payload.

        Returns:
            dict: JSON response from the API or error message.
        """
        try:
            # Convert the JSON payload to a string and send it via the `data` parameter
            response = make_request_with_retry(
                self.BASE_URL,
                headers=self.headers,
                params=None,
                data=json.dumps(payload)  # Send JSON payload as raw string
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}
