# 企業問い合わせ URL の取得

## 概要

1. [ITJOB 東京 23 区](https://www.itjob.tokyo/)から企業名リストを取得。

- requests
- bs4

2. 「\$企業名+"お問い合わせ"」で検索

- Google Custom Search

### Google Custom Search

GCP の API サービスの一つ。[コンソール](https://console.cloud.google.com/apis/api/customsearch.googleapis.com/quotas?hl=ja&project=scraping-company-contact&supportedpurview=project)で詳細情報を確認できる。

API の上限は 1 日 100 件 。それ以上は有料となる。  
使用料は [IAM の割り当てページ](https://console.cloud.google.com/iam-admin/quotas?hl=ja&project=scraping-company-contact&supportedpurview=project&service=customsearch.googleapis.com)から確認できる。

毎日の割り当ては、太平洋時間の午前 0 時にリセットされる。日本時間の 17 時くらい。


## 環境構築
- Python
- pip 
- RemoteContainer


