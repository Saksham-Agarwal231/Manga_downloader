import os
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
        
        while chapFirst != ch   apLast:

            if chapFirst == 'flip':
                self.startNumber += 1

            else:
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

    


    

    
