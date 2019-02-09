import json
import requests

from datetime import datetime

from common import days, worksheet, columns, align_format, shops_len

urls = list(map(lambda day: 'http://display.cjmall.com/c/rest/tv/tvSchedule?bdDt='+day+'&isMobile=false&broadType=live&isEmployee=false', days))

for index_url, url in enumerate(urls):
    value = requests.get(url)
    programList = json.loads(value.text).get('result').get('programList')
    for program in programList:
        hour = datetime.fromtimestamp(program.get('bdStrDtm')/1000.0).strftime('%H')
        date = '{} ~ {}'.format(datetime.fromtimestamp(program.get('bdStrDtm')/1000.0).strftime('%H:%M'), datetime.fromtimestamp(program.get('bdEndDtm')/1000.0).strftime('%H:%M'))
        names = ['({}) {}'.format(date, item.get('itemNm')) for item in program.get('itemList')]
        worksheet.write(columns[index_url][1] + str(int(hour) * shops_len + 3), '\n'.join(names), align_format)
