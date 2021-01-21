#     Author : MR.Arijit Paine     #
# Email : arijitpaine647@gmail.com #

import maya
import datetime
import requests

url = "https://api.clashroyale.com/v1/clans/ LCC0JUG9"

my_key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImYwMzQ1ZTA1LTBkMWQtNDk2OS1hNDdiLTZmNjIzMzIyZDk3ZCIsImlhdCI6MTYxMTIxMjE5Niwic3ViIjoiZGV2ZWxvcGVyLzU5NzM1ZTFiLWYxNDYtMTY4Ny01M2E5LTlhMGQ5MDYwYThkNSIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIxMTcuMjI3LjEyLjIxNCIsIjExNy4yMjYuMTQwLjIxNCJdLCJ0eXBlIjoiY2xpZW50In1dfQ.IVN1SGuyyQ4lqVpSdFAFWMBbHBdpnZlRjcE35AnlDS-DSXA6S3JzSmnJ5O4s6dAyo202txQgi0rJNjPMW6b8Fg"

headers = {
    'Accept': "application/json",
    'authorization': "Bearer %s" % my_key
    }

response = requests.request("GET", url, headers=headers)

data = response.json()
print(data)

lsArr = []
#print(data)
members = data['memberList']
for member in members:
    lastSeen = member['lastSeen']
    lastSeen2 = maya.parse(lastSeen).datetime()
    now = datetime.datetime.now()
    now2 = maya.parse(now).datetime()
    time = now2 - lastSeen2
    name = member['name']
    arr = [time,name]
    lsArr.append(arr)
    
print(lsArr)

