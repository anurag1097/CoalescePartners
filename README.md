# CoalescePartners

**CoalescePartners** is a Python-based project designed to fetch and process market data from various financial APIs. It integrates with services like Alpha Vantage, CoinAPI, and Birdeye to retrieve financial and cryptocurrency data, facilitating analysis and decision-making processes.

## Approach

The project is structured to modularly interact with different financial APIs using dedicated client classes. Each client handles authentication, request formation, and response parsing for a specific API. A utility function with retry logic (`make_request_with_retry`) is used to handle rate limits and network failures efficiently.

## Features

- **Alpha Vantage Integration**: Fetches stock market data, including time series data and technical indicators.
- **CoinAPI Integration**: Retrieves comprehensive cryptocurrency data, encompassing real-time prices, historical data, and exchange rates.
- **Birdeye Integration**: Obtains trending tokens and token prices, particularly focusing on the Solana blockchain ecosystem.
- **Robust Error Handling**: Implements retry logic to manage rate limits and ensure reliable data retrieval.

## Dependencies

The project requires the following dependencies:

- Python 3.7+
- `requests` (for making API calls)
- `python-dotenv` (for managing environment variables)

To install dependencies, run:
```bash
pip install -r requirements.txt
```

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/anurag1097/CoalescePartners.git
   cd CoalescePartners
   ```

2. **Set Up a Virtual Environment** (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**:
   - Create a `.env` file in the project root directory.
   - Add your API keys for Alpha Vantage, CoinAPI, and Birdeye:
     ```
     ALPHA_VANTAGE_KEY=your_alpha_vantage_api_key
     COINAPI_KEY=your_coinapi_api_key
     BIRDEYE_KEY=your_birdeye_api_key
     ```

## How to Run the Script

The primary script, `main.py`, initializes the API clients and fetches data from the integrated services.

To execute the script:

```bash
python main.py
```

This will output data fetched from Alpha Vantage, CoinAPI, and Birdeye based on the implemented API calls.

## Project Structure

- `alpha_vantage_client.py`: Contains the `AlphaVantageClient` class for interacting with the Alpha Vantage API.
- `coin_api_client.py`: Defines the `CoinAPIClient` class for accessing CoinAPI data.
- `bird_eye_client.py`: Implements the `BirdeyeClient` class to fetch data from the Birdeye API.
- `common_util.py`: Includes utility functions, such as `make_request_with_retry`, to handle HTTP requests with retry logic.
- `main.py`: The entry point of the application, orchestrating data fetching from all integrated services.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your_feature_name`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature/your_feature_name`.
5. Open a pull request.

