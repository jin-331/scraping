import os
from operation_csv import read_target_company
from operation_csv import write_target_company
from google_custom_search import getSearchResponse


if __name__ == "__main__":
    search_count = int(input("検索件数を入力してください。"))
    target_company = read_target_company(search_count)
    target_company_datas = []
    for target in target_company:
        target_company_datas.append(getSearchResponse(target))

    for target_company_data in target_company_datas:
        write_target_company(target_company_data)

    print(target_company_datas)
