from place_ranking_url import get_place_rankig_url
from company_name import get_company_name
from pagenation import get_pagenation_urls
import csv


def output_to_csv(data):
    with open("./data/data.csv", mode="a") as f:
        witer = csv.writer(f)
        witer.writerows(data)


if __name__ == "__main__":
    l = [["google", "it", "https://google.com/contact"]]
    sample = [['株式会社リヴァンプ・アウトソーシング', 'ソフトウェア/ハードウェア開発'], ['株式会社ワークスシステムズ', 'ソフトウェア/ハードウェア開発'], ['株式会社協同システムエンジニアリング', 'ソフトウェア/ハードウェア開発'],
              ['株式会社流機エンジニアリング', 'メーカー/製造系'], ['株式会社電通リテールマーケティング', 'マスコミ/広告/デザイン/ゲーム/エンターテイメント系'], ['株式会社Ｕｉ２', 'ソフトウェア/ハードウェア開発']]
    output_to_csv(sample)
