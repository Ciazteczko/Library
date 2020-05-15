
class Book:
    def __init__(self, pk, author, title, publisher, year, volume ='', series='', address='', edition='', month='', note='', key=''):
        self.pk = str(pk)
        self.author = str(author)
        self.title = str(title)
        self.publisher = str(publisher)
        self.year = str(year)
        self.volume = str(volume)
        self.series = str(series)
        self.address = str(address)
        self.edition = str(edition)
        self.month = str(month)
        self.note = str(note)
        self.key = str(key)

    def convert_to_bibtex(self):
        self.bibtex = '@book{'+ self.pk +',\n   author = "'+self.author+'",\n   title = "'+self.title+'",\n   publisher = "'+self.publisher +'",\n   year = "'+self.year+'"'

        if(self.volume != '' and self.volume is not None):
            self.bibtex += ',\n   volume = "'+self.volume+'"'
        if(self.series != '' and self.series is not None):
            self.bibtex += ',\n   series = "'+self.series+'"'
        if(self.address != '' and self.address is not None):
            self.bibtex += ',\n   address = "'+self.address+'"'
        if(self.edition != '' and self.edition is not None):
            self.bibtex += ',\n   edition = "'+self.edition+'"'
        if(self.month != '' and self.month is not None):
           self.bibtex += ',\n   month = "'+self.month+'"'
        if(self.note != '' and self.note is not None):
            self.bibtex += ',\n   note = "'+self.note+'"'
        if(self.key != '' and self.key is not None):
            self.bibtex += ',\n   key = "'+self.key+'"'
            
        self.bibtex+='\n}\n'

        return self.bibtex

    def save_to_file(self,path):
        with open(path,'a') as file:
            file.write(self.bibtex)


