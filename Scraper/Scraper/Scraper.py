#!/usr/bin/env python
# -*- coding: utf-8 -*-
from urllib.request import urlopen
import urllib
import bs4
import Database


class Scraper():
    def __init__(self, cnt):
        self.mainUrl = "http://www.zoomit.ir/page/"
        self.id = 1
        self.cnt = cnt
        self.file = open("test.xml", 'w', encoding="utf-8")
        self.db = Database.ScraperDB()

    def scrapePage(self, pageUrl):
        pageHtml = urllib.request.urlopen(pageUrl)
        soup = bs4.BeautifulSoup(pageHtml, "html.parser")
        mainDiv = soup.find("div", {"class" :"bg-white clearfix mrg15B pad20A"})
        #print (mainDiv)
        if(mainDiv != None):
            print (mainDiv)
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
            newContent = soup.find("div", {"class" : "article-content"})
            self.writeXML2([newId, newTitle, newLink, newDesc])
            print(self.db.insertNew([newTitle, newLink, newDesc, newContent]))
            self.id += 1

    def writeXML2(self, contains):
        print (contains)
        self.file.write("<news>" + "\n\t<id>\n\t\t" + str(contains[0]) + "\n\t</id>" + \
                        "\n\t<title>\n\t\t" + str(contains[1]) + "\n\t</title>" + \
                        "\n\t<link>\n\t\t" + str(contains[2]) + "\n\t</link>" + \
                        "\n\t<desc>\n\t\t" + str(contains[3]) + "\n\t</desc>\n</news>+\n")
    def writeXML(self, contains):
        news = etree.Element("news")
        '''string = "<id>" + str(contains[0]) + "</id>" + \
                "<title>" + str(contains[1]) + "</title>" + \
                "<link>" + str(contains[2]) + "</link>" + \
                "<desc>" + str(contains[3]) + "</desc>"
                '''
        #print (str(contains[1]))
        a = "salam"
        string = """<id>""" + str(contains[0]) + """</id>"""
        news.append(etree.fromstring(string))
        string = ""
        string = """<title>""" + str(contains[1]) + """</title>"""
        news.append(etree.fromstring(string.encode('utf-8')))
        string = ""
        string = """<link>""" + str(contains[2]) + """</link>"""
        news.append(etree.fromstring(string))
        string = ""
        string = """<desc>""" + str(contains[3]) + """</desc>"""
        news.append(etree.fromstring(string))
        print(str(etree.tostring(news, encoding='utf-8', pretty_print=True)))
        '''
        id = etree.SubElement(news, "id")
        #id.text = str(contains[0])
        #id.text = {0}.
        string = str(contains[0])
        id.append(etree.fromstring(string))

        title = etree.SubElement(news, "title")
        #title.text = str(contains[1])
        string = str(contains[1])
        title.append(etree.fromstring(string))

        link = etree.SubElement(news, "link")
        #link.text = str(contains[2])
        string = str(contains[2])
        link.append(etree.fromstring(string))

        desc = etree.SubElement(news, "desc")
        #desc.text = str(contains[3])
        string = str(contains[3])
        desc.append(etree.fromstring(string))

        self.file.write(str(etree.tostring(news, pretty_print=True)))
        print(etree.tostring(news,pretty_print=True))
        '''

    def main(self):
        for pageCnt in range(1, self.cnt + 1):
            self.scrapePage(self.mainUrl + str(pageCnt))
        self.file.close()
        print ("Finished")

pagesCount = int(input("Enter number of pages you want to scrape : "))
x = Scraper(pagesCount)
x.main()