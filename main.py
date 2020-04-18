from plyer import notification
import requests
from bs4 import BeautifulSoup
import time
def notifyMe(title,message):
    notification.notify(
        title=title,
        message=message,
        app_icon=None,
        timeout=10
    )

def getData(url):
    r=requests.get(url)
    return r.text
if __name__=="__main__":
    while True:
        #notifyMe("Nishan","hii")
        myHtmlData=getData("https://www.mohfw.gov.in/")
        soup=BeautifulSoup(myHtmlData,'html.parser')
        #print(soup.prettify())
        myData=""
        for tr in soup.find_all('tbody')[0].find_all('tr'):
            myData+=tr.get_text()
        myData=myData[1:]
        itemList=  myData.split("\n\n")
        s=itemList[33].split("\n")
        notifyMe(s[0],s[1])

        states=['West Bengal','Jharkhand']
        for item in itemList[0:36]:
            dataList=item.split("\n")
            print(dataList)
            if dataList[1] in states:
                print(dataList)
                nTitle="Cases of Covid 19"
                nText=f"States {dataList[1]}\n Total Confirmed cases :{dataList[2]}\n Cured:{dataList[3]}\n Deaths:{dataList[4]}"
                notifyMe(nTitle,nText)
                time.sleep(2)

        time.sleep(10)
