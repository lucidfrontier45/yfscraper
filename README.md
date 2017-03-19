# yfscraper
Yahoo Finance (JP) Scraper

## install

```bash
pip install yfscraper
```

## usage

`get_data` is the entrypoint API. You need to pass `tick_id`, `start_dt`, `end_dt`. You can optionally pass valid BeautifulSoup4 `html_parser`.

```python
def get_data(tick_id: str,
             start_dt: datetime.date,
             end_dt: datetime.date,
             html_parser="html.parser"):
```

### example

```python
import datetime
from yfscraper import get_data

tick_id = 998405
start_dt = datetime.date(2017, 1, 1)
end_dt = datetime.date(2017, 2, 1)
resp = get_data(tick_id, start_dt, end_dt)

for data in resp:
    print(data)
```

This will output the following

```python
{'low_v': 1508.21, 'close_v': 1527.77, 'open_v': 1511.26, 'high_v': 1528.59, 'date': datetime.date(2017, 2, 1)}
{'low_v': 1520.95, 'close_v': 1521.67, 'open_v': 1526.06, 'high_v': 1533.04, 'date': datetime.date(2017, 1, 31)}
{'low_v': 1535.97, 'close_v': 1543.77, 'open_v': 1542.62, 'high_v': 1543.99, 'date': datetime.date(2017, 1, 30)}
{'low_v': 1545.45, 'close_v': 1549.25, 'open_v': 1551.58, 'high_v': 1553.28, 'date': datetime.date(2017, 1, 27)}
{'low_v': 1535.25, 'close_v': 1545.01, 'open_v': 1536.6, 'high_v': 1546.08, 'date': datetime.date(2017, 1, 26)}
```

## compatibility

This package is tested for python 3.5 or later but should be work on python 3.4 with `typing` package installed.