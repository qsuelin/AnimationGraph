import requests


# default return daily from raw data
def get_assets_daily(assets: list) -> dict:
    assets_daily = {}
    for asset in assets:
        URL = f'https://community-api.coinmetrics.io/v2/assets/{asset}/metricdata?metrics=TxCnt'
        # print(URL)
        response = requests.get(URL)
        if not response:
            if response.status_code == 404:
                raise AssetError("Invalid asset(s). Check spelling and Coinmetrics for supported assets.")
            else:
                raise RequestError("Requests not supported.")
        else:
            json_response = response.json()
            assets_daily[asset] = parse_response(json_response)
    return assets_daily


def parse_response(json_response) -> list:
    res = []
    for record in json_response['metricData']['series']:
        res.append(int(float(record['values'][0])))
    return res


def get_assets_accumulation(assets: list) -> dict:
    assets_daily = get_assets_daily(assets)
    assets_accumulation = {}
    for asset, asset_daily in assets_daily.items():
        assets_accumulation[asset] = accumulate_asset_daily(asset_daily)
    return assets_accumulation


def accumulate_asset_daily(asset_daily: list):
    sum = 0
    asset_accumulation = []
    for i in range(len(asset_daily)):
        sum = sum+asset_daily[i]
        asset_accumulation.append(sum)

    return asset_accumulation


class Error(Exception):
    """base error."""


class AssetError(Error):
    """invalid asset. Raised with 404"""

    def __init__(self, message):
        self.message = message


class RequestError(Error):
    """400-403 from server"""

    def __init__(self, message):
        self.message = message


if __name__ == '__main__':
    try:
        print(get_assets_accumulation(['eos', 'btc']))
    except AssetError as e:
        print(e)
    except RequestError as e:
        print(e)
    except Exception as e:
        print(e)