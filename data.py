import requests
from console import ConsoleArgs

# get assets from console, list of str
assets = ConsoleArgs.assets

# default return daily from raw data
def get_assets_daily(assets: list) -> dict:
    assets_daily = {}
    for asset in assets:
        URL = f'https://community-api.coinmetrics.io/v2/assets/{asset}/metricdata?metrics=TxCnt'
        # print(URL)
        response = requests.get(URL)
        json_response = response.json()
        # print(json_response)
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


if __name__ == '__main__':
    print(get_assets_accumulation(['eos', 'btc']))