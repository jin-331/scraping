#!/usr/bin/env python
# -*- coding: utf-8 -*-
from place_ranking_url import get_place_rankig_url
from company_name import get_company_name
from pagenation import get_pagenation_urls
from output_csv import output_to_csv


# 指定地区の全データ取得
if __name__ == "__main__":
    num = int(input())
    place_ranking_urls = get_place_rankig_url()
    pagenation_urls = get_pagenation_urls(num)

    company_names = []
    for pagenation_url in pagenation_urls:
        page_company_names = get_company_name(pagenation_url)
        for page_company_name in page_company_names:
            company_names.append(page_company_name)

    output_datas = []
    for company_name in company_names:
        company_data = [company_name["company_name"], company_name["industry"]]
        output_datas.append(company_data)

    output_to_csv(output_datas)
