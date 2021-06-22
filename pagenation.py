import requests
from bs4 import BeautifulSoup


def get_pagenation_urls(toppage):
    r = requests.get(toppage)

    soup = BeautifulSoup(r.content, "html.parser")

    result = [toppage]

    pagenations = soup.find_all('ul', {'pagination'})
    # 1ページしかなかった場合
    if pagenations == []:
        return result
    else:
        pagenations_urls = pagenations[0].find_all("a")

        # pagenation の最後のページ番号を取得する。
        lastpage_url = pagenations_urls[-1].get("href")
        lastpage_num = lastpage_url.split("/")[-1]

        # toppage の URL にページ番号をつける
        # 2page目から取得
        for i in range(2, int(lastpage_num)+1):
            result.append("{0}/{1}".format(toppage, i))

        return result


if __name__ == "__main__":
    url = input()
    print(get_pagenation_urls(url))
