
class Article:
    def __init__(self, pk, author, title, journal, year, volume ='', number='', pages='', month='', note='', key=''):
        self.pk = str(pk)
        self.author = str(author)
        self.title = str(title)
        self.journal = str(journal)
        self.year = str(year)
        self.volume = str(volume)
        self.number = str(number)
        self.pages = str(pages)
        self.month = str(month)
        self.note = str(note)
        self.key = str(key)

    def convert_to_bibtex(self):
        self.bibtex = '@article{'+ self.pk +',\n   author = "'+self.author+'",\n   title = "'+self.title+'",\n   journal = "'+self.journal +'",\n   year = "'+self.year+ '"'

        if(self.volume != '' and self.volume is not None):
            self.bibtex += ',\n   volume = "'+self.volume + '"'
        if(self.number != '' and self.number is not None):
            self.bibtex += ',\n   number = "'+self.number+ '"'
        if(self.pages != '' and self.pages is not None):
            self.bibtex += ',\n   pages = "'+self.pages+ '"'
        if(self.month != '' and self.month is not None):
           self.bibtex += ',\n   month = "'+self.month+ '"'
        if(self.note != '' and self.note is not None):
            self.bibtex += ',\n   note = "'+self.note+ '"'
        if(self.key != '' and self.key is not None):
            self.bibtex += ',\n   key = "'+self.key+ '"'
        
        self.bibtex+='\n}\n'

        return self.bibtex

    def save_to_file(self,path):
        with open(path,'a') as file:
            file.write(self.bibtex)


