import os, img2pdf
class ImgConvert:

    def __init__(self,Pages, manga_chapter, startNumber, endNumber, MangaData):
        self.startNumber = startNumber
        self.endNumber = endNumber
        self.MangaData = MangaData
        self.manga_chapter = manga_chapter
        self.Pages = Pages

    def convert_func(self):
        chapFirst = self.manga_chapter[self.startNumber - 1]
        chapLast = self.manga_chapter[self.endNumber - 1]
        MangaDataTry = self.MangaData
        anotherVariable = 0
        add = 0

        for n in self.Pages:
            add = add + n
        
        while self.startNumber - 1 != self.endNumber:

            if chapFirst == 'flip':
                self.startNumber += 1

            else:
                if not os.path.exists("Manga_downloads{}".format(chapFirst)):
                    os.makedirs("Manga_downloads{}".format(chapFirst))
                
                PagesNo = self.Pages[anotherVariable]
                for n in range(add - 1):
                    if n == PagesNo - 1:
                        add = add - PagesNo
                        break
                    else:
                        files = open("Manga_downloads{}/{}.jpg".format(chapFirst, n), 'wb')
                        files.write(MangaDataTry[0])
                        MangaDataTry.pop(0)
                        files.close()
                try:
                    chapFirst = self.manga_chapter[self.startNumber]
                except IndexError:
                    break
                self.startNumber += 1
                anotherVariable += 1


    def pdf_conv(self):
        chapFirst = self.manga_chapter[self.startNumber - 1]
        chapLast = self.manga_chapter[self.endNumber - 1]
        MangaDataTry = self.MangaData
        anotherVariable = 0
        add = 0
        PagesNo = self.Pages[anotherVariable]
        lastVariable = []

        for n in self.Pages:
            add = add + n
        
        while self.startNumber - 1 != self.endNumber:

            if chapFirst == 'flip':
                self.startNumber += 1

            else:
                spilleted = chapFirst.split("/")

                if not os.path.exists("Manga_downloads/{}".format(spilleted[1])):
                    os.makedirs("Manga_downloads/{}".format(spilleted[1]))

                
                for n in range(add - 1):
                    if n == PagesNo - 1:
                        add = add - PagesNo
                        break
                    else:
                        lastVariable.append(bytes(MangaDataTry[0]))
                        MangaDataTry.pop(0)   
                
                f = open("Manga_downloads/{}/{}.pdf".format(spilleted[1], spilleted[2]),"wb")
             
                f.write(img2pdf.convert(lastVariable))
                lastVariable.clear()
                f.close()
                
                try:
                    chapFirst = self.manga_chapter[self.startNumber]
                except IndexError:
                    break
                self.startNumber += 1
                anotherVariable += 1


