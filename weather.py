# weather.py

from configparser import ConfigParser
import argparse


def _get_api_key():
    """
    Fetch the API key from your configuration file.

    Expects a configuration file named "secrets.ini" with sttrcuture:

        [openweather]
        api_key=<YOUR-OPENWEATHER-API-KEY>
    """
    config = ConfigParser()
    config.read("secrets.ini")
    return config["openweather"]["api_key"]


def read_user_cli_args():
    """
    Handles the CLI user interactions.

    Returns:
        argparse.Namespace: Populated namespace object
    """
    parser = argparse.ArgumentParser(
        description="gets weather and temperature information for a city"
    )
    
    parser.add_argument(
        "city", nargs="+", type=str, help="enter the city name"
    )

    parser.add_argument(
        "-i",
        "--imperial",
        action="store_true",
        help="display the temperature in imperial units",
    )
    return parser.parse_args()




if __name__ == "__main__":
    read_user_cli_args()