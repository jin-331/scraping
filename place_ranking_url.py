import requests
from bs4 import BeautifulSoup


def get_place_rankig_url():

    r = requests.get("https://www.itjob.tokyo/#ranking-area")

    soup = BeautifulSoup(r.content, "html.parser")

    all_ranking = soup.find_all('dl', {'class':'medium-4 columns'})

    # 東京IT企業ランキングの地域別リスト
    tokyo_ranking_urls = [url.get("href") for url in all_ranking[0].find_all("a")]
    tokyo_ranking_names = [names.text for names in all_ranking[0].find_all('dd')]

    result = []

    for index, url in enumerate(tokyo_ranking_urls):
        result.append({"url": url, "name": tokyo_ranking_names[index]})

    return result

if __name__ == "__main__":
    print(get_place_rankig_url())


