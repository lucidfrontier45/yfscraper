import datetime
from typing import List, Dict
import bs4

fmt = "%Y年%m月%d日"


def _parse_fund(data: List[str]) -> Dict:
    return {
        "date": datetime.datetime.strptime(data[0], fmt).date(),
        "share_value": float(data[1]),
        "total_value": float(data[2]),
    }


def _parse_index(data: List[str]) -> Dict:
    return {
        "date": datetime.datetime.strptime(data[0], fmt).date(),
        "open_v": float(data[1]),
        "high_v": float(data[2]),
        "low_v": float(data[3]),
        "close_v": float(data[4])
    }


def _parse_stock(data: List[str]) -> Dict:
    return {
        "date": datetime.datetime.strptime(data[0], fmt).date(),
        "open_v": float(data[1]),
        "high_v": float(data[2]),
        "low_v": float(data[3]),
        "close_v": float(data[4]),
        "volume": float(data[5]),
        "final_v": float(data[6])
    }


def parse_html(html_soup: bs4.BeautifulSoup) -> bool:
    table = html_soup.find("table", {"class": "boardFin yjSt marB6"})
    table_rows = table.find_all("tr")
    header = table_rows[0]
    data_rows = table_rows[1:]
    if len(data_rows) == 0:
        return True
    n_cols = len(header.find_all("th"))
    if n_cols == 3:
        _parse_f = _parse_fund
    elif n_cols == 5:
        _parse_f = _parse_index
    elif n_cols > 5:
        _parse_f = _parse_stock
    else:
        raise ValueError("invalid table, n_cols = {}".format(n_cols))

    for row in data_rows:
        data = [t.text.replace(",", "") for t in row.find_all("td")]
        yield _parse_f(data)
    return False
