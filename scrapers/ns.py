import requests
from bs4 import BeautifulSoup

from .common import days, worksheet, columns, align_format, shops_len

urls = list(map(lambda day: 'http://www.nsmall.com/TVHomeShoppingBrodcastingList?selectDay=' + day, days))

def run_ns():
    for index_url, url in enumerate(urls):
        html = requests.get(url, headers={'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 OPR/57.0.3098.106'}).text
        soup = BeautifulSoup(html, 'lxml')
        result = dict()

        for index_row, row in enumerate(soup.select('.tv_table.mt40 tbody > tr')):
            times = row.select('.air > em')
            product = row.select('td.al > .item_info > p.name > span > a')
            if times:
                time_text = times[0].text
                time_text_splitted = time_text.split(':')[0]
                hour = int(time_text_splitted.split(' ')[1])
                if (hour == 12):
                    hour = 0
                if (time_text_splitted[0:2] == '오후'):
                    hour += 12
                elif (time_text_splitted[0:2] == '오전' and hour < 2 and index_row > 40):
                    hour += 24
                if (hour not in result):
                    result[hour] = []
            elif product:
                result[hour].append('({}) {}'.format(time_text, product[0].text.strip().replace('[TV]', '')))
        for key, value in result.items():
            worksheet.write(columns[index_url][1] + str(int(key) * shops_len + 4), '\n'.join(value), align_format)
