import xlsxwriter

from datetime import datetime, timedelta

days = [(datetime.now() + timedelta(days=x)).strftime('%Y%m%d') for x in range(0, 7)]

times = ['0{}'.format(str(x)) if x < 10 else str(x) for x in range(0, 26)]

columns = [[chr(x * 2 + 66), chr(x * 2 + 67)] for x in range(len(days))]

workbook = xlsxwriter.Workbook('result.xlsx')
# 셀 스타일 수정시 add_format으로 스타일 추가 후 각 셀에 적용
head_format = workbook.add_format({'bold': True, 'align': 'center', 'valign': 'vcenter'})
align_format = workbook.add_format({'valign': 'vcenter'})

worksheet = workbook.add_worksheet()
worksheet.set_column(0, 1, 5)

shops = ['GS', 'CJ', 'NS', 'HD']
shops_len = len(shops)

def run_common():
	for index_day, day in enumerate(days):
		# 가장 윗줄에 날짜를 표시
		worksheet.merge_range('{}1:{}1'.format(columns[index_day][0], columns[index_day][1]), day, head_format)
		worksheet.set_column(index_day * 2 + 1, index_day * 2 + 2, 50)
		worksheet.set_column(index_day * 2 + 2, index_day * 2 + 3, 5)

	for index in range(len(times)):
		# 가장 왼쪽 열에 시간대를 표시
		worksheet.merge_range('A{}:A{}'.format(str(index * shops_len +2), str(index * shops_len + shops_len + 1)) , times[index], head_format)
		for column in columns:
			for index_shop, shop in enumerate(shops):
				# 각 시간대별 쇼핑몰 텍스트 추가
				worksheet.write(column[0] + str(index * shops_len + index_shop + 2), shop, head_format)
