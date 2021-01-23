from flask import Flask, render_template
import requests
import datetime
from datetime import timedelta
import maya

app = Flask(__name__)

@app.route("/")
def hello():
    url = "https://api.clashroyale.com/v1/clans/ LCC0JUG9"
    my_key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjkwYTZmZTc3LWM3OTYtNDQ3OS04ODM4LWE0MDNkNjkyZjRhNSIsImlhdCI6MTYxMTM5NzkxNywic3ViIjoiZGV2ZWxvcGVyLzYxYmY3NmVkLTJlNGEtODFjZS1kYjJlLTlmOGE1NzBhY2UzNiIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyI1NC4xODkuMTY5LjE0MyJdLCJ0eXBlIjoiY2xpZW50In1dfQ.G32C848y9O86hguvoriFEcnnrDkddGzcZZtpf-RfTAwM8j65HblVfMLv4ze_lqLNEaVB6oGo69Esla0qZ22oyQ"
    headers = {
        'Accept': "application/json",
        'authorization': "Bearer %s" % my_key
        }
#arijit
    response = requests.request("GET", url, headers=headers)
    data = response.json()
    print(data)
    mArrey = data['memberList']
    now = datetime.datetime.now()
    now2 = maya.parse(now).datetime()
    i = 0
    lsArr = []
    dayArr = []
    Min_Arr = []
    while i < data['members']:
        lastSeen = mArrey[i]['lastSeen']
        lastSeen2 = maya.parse(lastSeen).datetime()
        lastOnline = now2 - lastSeen2 
        i += 1
        dayArr.append(lastOnline.days) 
        Min_Arr.append(int(((lastOnline.seconds)/60)/60))
    print(dayArr,"\n",Min_Arr)
    return render_template('index.html', data = data,mArrey = mArrey, dayArr = dayArr,Min_Arr = Min_Arr) 
 
    #________errorhandlers_________#
@app.errorhandler(404) 
def invalid_route(e): 
    return render_template('404.html')

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html')

app.run(debug=False,host="0.0.0.0")
