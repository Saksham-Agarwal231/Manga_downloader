from scrape import scrapy
from page_download import page_download
from image_comverter import ImgConvert

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


#the file conversion part
def choiced():
    ImgConv = ImgConvert(mangaPagesList, manga_chapter,startNumber,endNumber,mangaDATA)

    choice = int(input("\n\nDo you want to save in image format or pdf format\n1)Img format\n2)pdf format\n\nEnter your choice here: "))
    if choice == 1:
        print("\n\nRoger that senpai ヾ(≧▽≦*)o")
        ImgConv.convert_func()
    elif choice == 2:
        print("\n\nOK SENSEI!!!!! ψ(｀∇´)ψ")
        ImgConv.pdf_conv()
    else:
        choiced()

choiced()

inp = input("Now, all your downloads are done!!!!!!!!! enjoy :)\nPress enter to leave: ")






