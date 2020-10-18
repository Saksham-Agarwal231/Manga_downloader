import requests
import urllib.request, urllib.parse, urllib.error
import webbrowser
from bs4 import BeautifulSoup
import ssl
import re

class scrapy:
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    inp = input('Enter your input here: ')
    website = 'http://www.mangareader.net/search/?'
    main_website = 'http://www.mangareader.net'

    search_ = urllib.parse.urlencode({'nsearch':inp})
    #webbrowser.open(website + search_)
    search_thingie = website + search_
    
    flip = requests.get(search_thingie)
    flip.raise_for_status()
    soup = BeautifulSoup(flip.text, 'html.parser')
    alt = []
    count = []

    def search_list(this):
        tags = this.soup.findAll('div', attrs = {'class': "d57"})
        sno = 1
        for n in tags:
            print(sno, ' ', n.getText())
            sno += 1
            this.alt.append(n('a')[0].get('href', None))
        
        return this.alt

    def manga_open(this, takein):
        webpage = requests.get(this.main_website + this.alt[takein - 1])
        webpage.raise_for_status()
        code = BeautifulSoup(webpage.text, 'html.parser')
        column = code('td')
        
        for n in column:
            try:
                this.count.append(n('a')[0].get('href', None))
            except:
                pass

        this.count.pop(0)
        this.count.pop(len(this.count) - 1)
        this.count.pop(len(this.count) - 1)
        iTrial = 1  
        sHow = 0
        tooMany = []
        for nnn in this.count:  #if you dont understand this, leave it, even i dont know what i wrote there, its just important
            x = int(re.findall('[0-9]+', nnn)[0])
            if iTrial == x:
                iTrial= x + 1
            else:
                tooMany.append(iTrial)
                iHecks = x - iTrial
                for  n in range(0, iHecks):
                    print('chapter no {} is missing'.format(iTrial))
                    iTrial += 1       
                iTrial += 1
                sHow += 1      

        for n in tooMany:
            this.count.insert(n - 1, 'flip')
        print('The manga has {} chapters'.format(len(this.count) + sHow))

        return this.count
    
    





    
