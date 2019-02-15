import requests
from bs4 import BeautifulSoup

from .common import days, worksheet, columns, align_format, shops_len

urls = list(map(lambda day: 'https://www.hyundaihmall.com/front/bmc/brodPordPbdv.do?cnt=0&date=' + day, days))

def run_hyundai():
	for index_url, url in enumerate(urls):
			html = requests.get(url).text
			soup = BeautifulSoup(html, 'html.parser')

			for tag in soup.select('#brodListTop > li'):
					time = tag.find(class_='time').text

					names = '\n'.join(['({}) {}'.format(time, item.select('.prod_tit > a')[0].text.strip()) for item in tag.select('.cell2 > div')])

					worksheet.write(columns[index_url][1] + str(int(time[0:2]) * shops_len + 5), names, align_format)
