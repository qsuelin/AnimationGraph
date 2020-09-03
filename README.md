# Visual-coin
Python console application for visualizing metrics of different blockchain asset(s) in customized form(s) of picture or animation. It meant to offer an easy monitor tool for the assets' performance. The data sources from coinmetrics api V2.
Default x-axis: Days from the network first got launched.
Default y-axis: Cumulative Transaction Count.

## API reference
### Synopsis
`visual-coin.py [-h] --asset ASSET [ASSET ...] (--output OUTPUT [OUTPUT ...] | --show) [--dir DIR] [--name NAME]`


### Options
<dl>
  <dt>-asset | -a opt1 [opt2 ...]
  <dd>Input asset(s) to be visualized into a single graph. If many, separated with space
  <dd> Check coinmetrics for supported assets. If asset is invalid or failed to connect to the server, exception will be raised.

  <dt>--output | -o opt1 [ opt2 ...]
  <dd>Input the file type(s) to export as. If many, separated with space.
  <dd>Supported format: png, pdf, mp4, gif, mov, avi

  <dt>--dir | -d DIR
  <dd>Input destination directory to export files into.

  <dt>--name | -n NAME
  <dd>Input desired filename. Default: assetid1_assetid2_...%y%m%d.filetype

  <dt>--show | -s
  <dd>If specify, the graph will be shown.
<dl>

## Sample
![alt text](https://github.com/qsuelin/visual-coin/blob/master/sample/eos_etc_btc200902.png "Sample PNG for EOS, ETC, BTC till 2020/09/02")
![Sample GIF for EOS, ETC, BTC till 2020/09/02](https://github.com/qsuelin/visual-coin/blob/master/sample/eos_etc_btc200902.gif)
