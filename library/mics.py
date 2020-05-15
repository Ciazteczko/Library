
class Mics:
    def __init__(self, pk, author='', title='', howpublished='', month='', year='', note='', key=''):
        self.pk = str(pk)
        self.author = str(author)
        self.title = str(title)
        self.howpublished = str(howpublished)
        self.year = str(year)
        self.month = str(month)
        self.note = str(note)
        self.key = str(key)

    def convert_to_bibtex(self):
        self.bibtex = '@mics{'+ self.pk

        if(self.author != '' and self.author is not None):
            self.bibtex += ',\n   author = "'+self.author+'"'
        if(self.title != '' and self.title is not None):
            self.bibtex += ',\n   title = "'+self.title+'"'
        if(self.howpublished != '' and self.howpublished is not None):
            self.bibtex += ',\n   howpublished = "'+self.howpublished+'"'
        if(self.year != '' and self.year is not None):
           self.bibtex += ',\n   year = "'+self.year+'"'
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


