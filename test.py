import requests
import urllib.request
import requests
import urllib.parse
import sys
def send_msg(msg):
    LINE_ACCESS_TOKEN="hF4n9ndtL9yw2ip40tPF7iPulbrkypL4KFxs0DSsd9NS"
    url = "https://notify-api.line.me/api/notify"
    file = {'imageFile':open('./upload.jpg','rb')}
    data = ({
        'message':msg
    })
    LINE_HEADERS = {"Authorization":"Bearer "+LINE_ACCESS_TOKEN}
    session = requests.Session()
    r=session.post(url, headers=LINE_HEADERS, files=file, data=data)
    print(r.text)
send_msg("hello my first msg with line notify api")

