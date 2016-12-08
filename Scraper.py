
from urllib.request import urlopen
import urllib
from bs4 import BeautifulSoup
import bs4
#import requests
#from lxml import etree

class Scraper():
    def __init__(self, cnt):
        self.mainUrl = "http://www.zoomit.ir/page/"
        self.id = 1
        self.cnt = cnt
        self.file = open("test.xml", 'a')

    def scrapePage(self, pageUrl):
        pageHtml = urllib.request.urlopen(pageUrl)
        soup = bs4.BeautifulSoup(pageHtml, "html.parser")
        mainDiv = soup.find("div", {"class" :"bg-white clearfix mrg15B pad20A"})
        if(mainDiv != None):
            newsDiv = mainDiv.find_all("div", {"class" : "item-list-row"})

            for newDiv in newsDiv:
                newTitle = newDiv.find('h3').find('a').string
                newLink = newDiv.find('h3').find('a')['href']
                self.scrapeNew(self.id, newTitle, newLink)

    def scrapeNew(self, newId, newTitle, newLink):
        newHtml = urllib.request.urlopen(newLink)
        soup = bs4.BeautifulSoup(newHtml, "html.parser")

        newDiv = soup.find("div" ,{"class":"article-section"})
        if(newDiv != None):
            descs = newDiv.find_all('p')
            newDesc = ""
            for desc in descs:
                newDesc += desc.text

            self.writeXML2([newId, newTitle, newLink, newDesc])
            self.id += 1

    def writeXML2(self, contains):
        print (contains)
        self.file.write("<news>" + "\n\t<id>\n\t\t" + str(contains[0]) + "\n\t</id>" + \
                        "\n\t<title>\n\t\t" + str(contains[1]) + "\n\t</title>" + \
                        "\n\t<link>\n\t\t" + str(contains[2]) + "\n\t</link>" + \
                        "\n\t<desc>\n\t\t" + str(contains[3]) + "\n\t</desc>\n</news>\n")

    def main(self):
        for pageCnt in range(1, self.cnt + 1):
            self.scrapePage(self.mainUrl + str(pageCnt))
        self.file.close()
        print ("Finished")

pagesCount = int(input("Enter number of pages you want to scrape : "))
x = Scraper(pagesCount)
x.main()
