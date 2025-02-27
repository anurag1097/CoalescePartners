import requests
import time


import requests
import time

def make_request_with_retry(url, params=None, headers=None, data=None, method="GET", max_retries=3, backoff_factor=1):
    """
    Helper function to perform HTTP requests (GET or POST) with retry logic for handling rate limits.
    If the API responds with HTTP 429 (Too Many Requests), the function waits for a calculated
    delay before retrying.

    Args:
        url (str): The API endpoint URL.
        params (dict, optional): Query parameters for GET requests.
        headers (dict, optional): Headers for the request.
        data (str, optional): Payload for POST requests (should be JSON string).
        method (str, optional): HTTP method ("GET" or "POST"). Defaults to "GET".
        max_retries (int, optional): Maximum number of retry attempts.
        backoff_factor (int, optional): Factor to determine wait time between retries.

    Returns:
        response: The final HTTP response object.
    """
    for attempt in range(max_retries):
        try:
            if method.upper() == "POST":
                response = requests.post(url, params=params, headers=headers, data=data)
            else:  # Default to GET request
                response = requests.get(url, params=params, headers=headers)

        except requests.exceptions.RequestException as e:
            if attempt == max_retries - 1:
                raise e
            time.sleep(backoff_factor * (attempt + 1))
            continue

        if response.status_code == 429:
            # Rate limit encountered. Wait and then retry.
            wait_time = backoff_factor * (attempt + 1)
            print(f"Rate limit hit. Retrying in {wait_time} seconds... (Attempt {attempt + 1}/{max_retries})")
            time.sleep(wait_time)
        else:
            return response

    return response  # Return last response after retries are exhausted

