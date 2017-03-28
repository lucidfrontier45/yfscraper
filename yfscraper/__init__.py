import datetime
import requests
import logging
from urllib.parse import urlencode
import bs4

from .parser import parse_html

logger = logging.getLogger("yf_parser")
page_url = "http://info.finance.yahoo.co.jp/history/"


def get_data(tick_id: str,
             start_dt: datetime.date,
             end_dt: datetime.date,
             html_parser="html.parser"):

    session = requests.Session()
    page = 1
    while True:
        params = {
            "code": tick_id,
            "sy": start_dt.year,
            "sm": start_dt.month,
            "sd": start_dt.day,
            "ey": end_dt.year,
            "em": end_dt.month,
            "ed": end_dt.day,
            "tm": "d",
            "p": page
        }
        logger.info(page_url + "?" + urlencode(params))
        resp = session.get(page_url, params=params)
        if not resp.ok:
            break
        html_soup = bs4.BeautifulSoup(resp.text, html_parser)
        stop = yield from parse_html(html_soup)
        if stop:
            break
        page = page + 1
