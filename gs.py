import requests
from bs4 import BeautifulSoup

from common import days, worksheet, columns, align_format, shops_len

urls = list(map(lambda day: 'https://www.gsshop.com/shop/tv/tvScheduleDetail.gs?today='+day, days))

for index_url, url in enumerate(urls):
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    result = {}
    for index_tag, tag in enumerate(soup.select('.items')):
        times_tag = tag.find(class_='times').text
        time_before = times_tag[0:2]
        if (time_before not in result):
            result[time_before] = []
        for item in tag.select('.prd-item'):
            if item.select('.prd-name a'):
                name = item.select('.prd-name a')[0].text
            elif item.select('.prd-name'):
                for i in item.findAll('i'):
                    i.extract()
                name = item.select('.prd-name')[0].text.strip()
            result[time_before].append('({}) {}'.format(times_tag, name))
    for key, value in result.items():
        worksheet.write(columns[index_url][1] + str(int(key) * shops_len + 2), '\n'.join(value), align_format)
