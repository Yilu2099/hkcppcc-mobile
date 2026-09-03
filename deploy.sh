#!/bin/bash
# 一鍵上線：重新打包 → 上傳到 gsl.t2099.com → 校驗 MD5
set -e
cd "$(dirname "$0")"
python3 build.py
scp -q docs/index.html t2099-collector:/www/wwwroot/gsl.t2099.com/index.html
echo "遠端 $(ssh t2099-collector 'md5sum /www/wwwroot/gsl.t2099.com/index.html' | cut -c1-32)"
echo "本地 $(md5 -q docs/index.html)"
echo "已上線：https://gsl.t2099.com/"
