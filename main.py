from plyer import notification
import requests
from bs4 import BeautifulSoup
import time


def notifyme(title, message):
    """
    This method trigers an alert which pops up everytime you run the code.
    app_icon takes the image for the logo from the path you have mentioned. yours would be different in your system.
    You can give the path where you have kept the image. Make sure image is in ico format. png or jpeg may not work here.


    """
    notification.notify(
        title=title,
        message=message,
        app_icon=r"C:\Users\Chaudhary\Desktop\c.ico",
        timeout=10

    )


def getData(url):
    """
    url is any website where you want to get the html data from

    """
    r = requests.get(url)
    return r.text


if __name__ == "__main__":
    while True:
        myHtmlData = getData('https://www.mohfw.gov.in/')

        soup = BeautifulSoup(myHtmlData, 'html.parser')
        myDatastr = ""
        for tr in soup.find_all('tbody')[0].find_all('tr'):
            myDatastr += tr.get_text()
        myDatastr = myDatastr[1:]
        itemList = myDatastr.split("\n\n")

        states = ['Mumbai', 'Delhi', 'Punjab']
        for item in itemList[0:29]:
            datalist = item.split('\n')
            if datalist[1] in states:
                nTitle = 'Cases of COVOID-19'
                nText = f"State - {datalist[1]}\nTotal case: {datalist[2]}\n Cured: {datalist[3]}\n Deaths: {datalist[4]}"
                notifyme(nTitle, nText)
                time.sleep(2)
        time.sleep(120)