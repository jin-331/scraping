#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import datetime
import json

from time import sleep
from googleapiclient.discovery import build
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
CUSTOM_SEARCH_ENGINE_ID = os.environ.get("CUSTOM_SEARCH_ENGINE_ID")


def getSearchResponse(keyword):
    contact_keyword = keyword + " お問い合わせ"

    service = build("customsearch", "v1", developerKey=GOOGLE_API_KEY)

    response = {}

    try:
        sleep(1)
        response = (service.cse().list(
            q=contact_keyword,
            cx=CUSTOM_SEARCH_ENGINE_ID,
            lr="lang_ja",
            num=1,
            start=1,
        ).execute())
    except Exception as e:
        print(e)

    company_name_and_contact_link = {
        "name": keyword, "link": response["items"][0]["link"]}

    return company_name_and_contact_link


if __name__ == '__main__':

    target_keyword = '株式会社一休'

    print(getSearchResponse(target_keyword))
