from requests_html import HTMLSession
import time

headers = { 'Accept':'*/*',
            'Accept-Language':'en-US,en;q=0.8',
            'Cache-Control':'max-age=0',
            'Connection':'keep-alive',
            'Proxy-Authorization':'Basic ZWRjZ3Vlc3Q6ZWRjZ3Vlc3Q=',
            'If-Modified-Since':'Fri, 13 Nov 2015 17:47:23 GMT',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36'
            }

session = HTMLSession()
session.headers = headers

def mvc():
    url = 'https://telegov.njportal.com/njmvc/AppointmentWizard/7'
    r = session.get(url)
    if not r.ok:
        print("Error Code")
        return False
    r.html.render()
    bigString = r.html.find(".input-group", first=True).text
    if re.search("06/0[1-6]/....", bigString):
        #playsound('ding.mp3')
        dates = re.findall(r"06/0[1-6]/.............", bigString)
        for date in dates:
            print(date)
    return True

while mvc():
    localtime = time.localtime()
    result = time.strftime("%I:%M:%S %p", localtime)
    print("Updated at:", result)
    time.sleep(10)
