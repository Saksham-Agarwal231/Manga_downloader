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
        chapLast = self.manga_chapter[self.endNumber]
        MangaDataTry = self.MangaData
        anotherVariable = 0
        add = 0

        for n in self.Pages:
            add = add + n
        
        while chapFirst != chapLast:

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

                chapFirst = self.manga_chapter[self.startNumber]
                self.startNumber += 1
                anotherVariable += 1


class pdf_conveter:

    def __init__(self,Pages, manga_chapter, startNumber, endNumber, MangaData):
        self.startNumber = startNumber
        self.endNumber = endNumber
        self.MangaData = MangaData
        self.manga_chapter = manga_chapter
        self.Pages = Pages

    def pdf_conv(self):
        chapFirst = self.manga_chapter[self.startNumber - 1]
        chapLast = self.manga_chapter[self.endNumber]
        MangaDataTry = self.MangaData
        anotherVariable = 0
        add = 0
        PagesNo = self.Pages[anotherVariable]
        lastVariable = []
        secondLastVariable = []

        for n in self.Pages:
            add = add + n
        
        while chapFirst != chapLast:

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
                        lastVariable.append(MangaDataTry[0])
                        MangaDataTry.pop(0)    
                    f = open("Manga_downloads/{}/{}.pdf".format(spilleted[1], spilleted[2]),"ab")

                for nn in lastVariable:
                    f.write(img2pdf.convert(bytes(nn)))
                    
                lastVariable.clear()
                f.close()
                
                chapFirst = self.manga_chapter[self.startNumber]
                self.startNumber += 1
                anotherVariable += 1