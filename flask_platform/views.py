from flask import render_template
from flask_platform import app
import systeminfo
@app.route('/')
def index():
     returnDict = {}
     returnDict['user'] = systeminfo.get_platform_info()
     returnDict['title'] = 'Home'
     return render_template("index.html", **returnDict)
