import ssl
from scrape import scrapy
import requests
import urllib.request, urllib.parse, urllib.error
import webbrowser
from bs4 import BeautifulSoup
from page_download import page_download
from image_comverter import ImgConvert, pdf_conveter

#all the scraping part code
scrapeData = scrapy()
alt =scrapeData.search_list()
takein = int(input('Whats ya no: '))
manga_chapter =scrapeData.manga_open(takein)


#all the page downloading part code
startNumber = int(input("Enter the starting number: "))
endNumber = int(input("Enter the ending number: "))
pageDownl = page_download(manga_chapter, startNumber, endNumber)
pageDownl.chapter_select()
mangaDATA = pageDownl.MangaData
mangaPagesList = pageDownl.Pages
import base64
help = open("sdvfg.pdf", "wb")

#the file conversion part
ImgConv = ImgConvert(mangaPagesList, manga_chapter,startNumber,endNumber,mangaDATA)
pdfConv = pdf_conveter(mangaPagesList, manga_chapter,startNumber,endNumber,mangaDATA)
#ImgConv.convert_func()
pdfConv.pdf_conv()



