from flask import Flask, Response

from scrapers.run import run
from scrapers.common import output

from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
	return '''
<html>
  <form action='/download'>
    <button type='submit'>데이터</button>
  </form>
</html>
'''

@app.route('/download', methods=['GET'])
def download():
	run()
	output.seek(0)
	return Response(
		output.read(),
		mimetype="text/csv",
		headers={
			"Content-Disposition":
			"attachment;filename=%s.csv" % datetime.now()
		}
	) 

if __name__ == '__main__':
	app.run()
