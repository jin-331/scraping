import csv
import pandas as pd


def read_target_company(search_count):
    """
    csv ファイルから、contact_url が non の company_name を取得する。
    検索数が index を超えた場合は、条件に一致したものすべてを返す。

    Args:
        search_count(int): 検索件数

    Returns:
        list: 検索数の company_name のリスト
    """
    df = pd.read_csv("./data/data.csv", index_col=0)

    non_url_company_names = df[df["contact_url"].isnull()]
    target_company_names_list = non_url_company_names.iloc[:search_count, [
        0, 1]].index.values

    return target_company_names_list


def write_target_company(data):
    """
    csv ファイルに書き込む。

    Args:
        data(object): 検索結果

    Returns:
        void:
    """

    df = pd.read_csv("./data/data.csv", index_col=0)
    # 1つでも項目その列のデータが入ってないと NaN になって値を代入できないから、1行でも何か入れとくを書き込める。
    df.at[data["name"], "contact_url"] = data["link"]
    df.to_csv("./data/data.csv")


if __name__ == "__main__":
    data = {"name": "株式会社宣伝会議", "link": "https://"}
    write_target_company(data)
