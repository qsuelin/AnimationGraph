# visual-coin
visual-coin is a Python console application for visualizing metrics of different blockchain asset(s) in customized form(s) of picture or animation. It meant to offer an easy monitor tool for the assets' performance. The data sources from [Coinmetrics API V2](https://docs.coinmetrics.io/api/v2/).               
Default x-axis: Days from the network first got launched.   
Default y-axis: Cumulative Transaction Count.

## API reference
### Synopsis
    visual-coin.py [-h] --asset ASSET [ASSET ...] (--output OUTPUT [OUTPUT ...] | --show) [--dir DIR] [--name NAME]


### Options
<dl>
  <dt>-asset | -a ASSET [ASSET ...]
  <dd>Input asset(s) to be visualized into a single graph. If many, separated with space.
  <dd> Check <a href=https://community-api.coinmetrics.io/v2/assets/>Coinmetrics</a> for supported assets. If asset is invalid or failed to connect to the server, exception will be raised.

  <dt>--output | -o OUTPUT [OUTPUT ...]
  <dd>Input the file type(s) to export as. If many, separated with space.
  <dd>Supported format: png, pdf, mp4, gif, mov, avi

  <dt>--dir | -d DIR
  <dd>Input destination directory to export files into.   
  <dd>Default location: <code>current script directory/out</code>.

  <dt>--name | -n NAME
  <dd>Input desired filename.
  <dd>Default: <code>asset_asset_...YYMMDD</code>    

    $ date
    Thu Sep  3 09:08:19 CDT 2020
    $ visual-coin.py -a eos etc btc -o png
    # output: eos_etc_btc200903.png

  <dt>--show | -s
  <dd>If specify, the graph will be shown.
<dl>

## Sample
![Sample PNG for EOS, ETC, BTC till 2020/09/02](https://github.com/qsuelin/visual-coin/blob/master/sample/eos_etc_btc200902.png)

![Sample GIF for EOS, ETC, BTC till 2020/09/02](https://github.com/qsuelin/visual-coin/blob/master/sample/eos_etc_btc200902.gif)
