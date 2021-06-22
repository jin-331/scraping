import requests
from bs4 import BeautifulSoup


#  企業名の取得
def get_company_name(ranking_page_url):

    r = requests.get(ranking_page_url)

    soup = BeautifulSoup(r.content, "html.parser")

    # 企業の名前取得
    company_names = soup.find_all('div', {'rank-item row'})

    # 企業の業種取得
    company_industries = soup.find_all('div', {'industry'})

    company_industries_result = []
    for industry in company_industries:
        company_industries_result.append(industry.find("a", {}).text)

    company_names_result = []
    for name in company_names:
        company_names_result.append(name.find("a", {"name"}).text)

    result = []

    # いい書き方が思い浮かばない。
    for i, name in enumerate(company_names_result):
        result.append(
            {"company_name": company_names_result[i], "industry": company_industries_result[i]})

    return result


if __name__ == "__main__":
    print(get_company_name(
        "https://www.itjob.tokyo/ranking/%E5%8D%83%E4%BB%A3%E7%94%B0/2"))
