import requests
import urllib.request
import requests
import urllib.parse
import sys
def send_msg(msg):
    LINE_ACCESS_TOKEN="LRCy0QpDagq4F8bCbYlTZT2GnnXDWPxKxuZ3Rb30AIA"
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

