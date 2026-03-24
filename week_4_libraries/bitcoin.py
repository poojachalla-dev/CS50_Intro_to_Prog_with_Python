import requests
import sys


def main():
    # Validate command-line argument
    if len(sys.argv) != 2:
        sys.exit("Usage: python bitcoin.py <number of bitcoins>")

    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Error: argument must be a numeric value.")

    # Query CoinCap API
    try:
        response = requests.get(
            "https://rest.coincap.io/v3/assets/bitcoin",
            params={"apiKey": "74da3fe2d4fef462252572b88fb3e864a1b051fdea3c67082bb30b0ab33b973c"},
            timeout=10,
        )
        response.raise_for_status()
        data = response.json()
        price = float(data["data"]["priceUsd"])
    except requests.RequestException:
        sys.exit("Error: could not retrieve Bitcoin price.")

    # Compute and display cost
    cost = n * price
    print(f"${cost:,.4f}")


if __name__ == "__main__":
    main()