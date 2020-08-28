#!/bin/bash

type=$1
shift

while [[ $# -gt 0 ]]; do
  if [ $type == "json" ]; then
    curl "https://community-api.coinmetrics.io/v2/assets/${1}/metricdata?metrics=TxCnt" > "${1}.json"
  else
    curl "https://community-api.coinmetrics.io/v2/assets/${1}/metricdata.csv?metrics=TxCnt" > "${1}.csv"
  fi
  shift
done
