import os
import requests
from bs4 import BeautifulSoup
import re

class page_download:

    def __init__(self, manga_chapter, startNumber, endNumber):
        self.manga_chapter = manga_chapter
        self.startNumber = startNumber
        self.endNumber = endNumber
        self.main_website = 'http://www.mangareader.net'
        self.MangaData = []
        self.Pages = []

    
    def chapter_select(self):
        chapFirst = self.manga_chapter[self.startNumber - 1]
        chapLast = self.manga_chapter[self.endNumber - 1]
        while self.startNumber - 1 != self.endNumber:
            if chapFirst == 'flip':
                print("There is no data for this chapter on the site, i beg for forgiveness!!!")
                self.startNumber += 1

            else:
                chapNumber = 1 #sorry for defining this many variables, i am nub
                chapCount = 2
                fg = 0
                currentSite = self.main_website + chapFirst
                while fg == 0:
                    page = requests.get(currentSite)
                    page.raise_for_status

                    pageSoup = BeautifulSoup(page.text, 'html.parser')
                    Img = pageSoup('img')
                    next_page = pageSoup.findAll('a', attrs = {'class': "d61 d63"})
                    Imghref = Img[2].get('src', None)
                    
                    data = bytearray()
                    for chunk in requests.get("https:" + Imghref).iter_content(10000):
                        data.extend(chunk)
                        
                    self.MangaData.append(data)
                    currentSite = self.main_website + chapFirst + "/{}".format(chapCount)
                    chapCount += 1
                    if len(self.MangaData) > 2 and self.MangaData[len(self.MangaData) - 1] == self.MangaData[len(self.MangaData) - 2]:
                        fg = 1
                        self.MangaData.pop(len(self.MangaData) - 1)
                    else:
                        print('{}/{} page downloaded'.format(chapFirst, chapNumber))
                        chapNumber += 1
                self.Pages.append(chapNumber)

            self.startNumber += 1
            try:
               chapFirst = self.manga_chapter[self.startNumber - 1]

            except IndexError:
                break


