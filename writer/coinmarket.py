from typing import List
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from dotenv import load_dotenv
import os

load_dotenv()

url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
parameters = {"start": "1", "limit": "5000", "convert": "USD"}
headers = {
    "Accepts": "application/json",
    "X-CMC_PRO_API_KEY": os.getenv("COINMARKETCAP_KEY"),
}

session = Session()
session.headers.update(headers)


def get_top_coins(count: int = 50) -> List[str]:
    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        return list(map(lambda x: x["symbol"], data["data"]))[0:count]
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)

