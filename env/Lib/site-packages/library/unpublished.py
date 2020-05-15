
class Unpublished:
    def __init__(self, pk, author, title, note, month='', year='', key=''):
        self.pk = str(pk)
        self.author = str(author)
        self.title = str(title)
        self.note = str(note)
        self.year = str(year)
        self.month = str(month)
        self.key = str(key)

    def convert_to_bibtex(self):
        self.bibtex = '@unpublished{'+ self.pk +',\n   author = "'+self.author+'",\n   title = "'+self.title+'"'

        if(self.year != '' and self.year is not None):
           self.bibtex += ',\n   year = "'+self.year+'"'
        if(self.month != '' and self.month is not None):
           self.bibtex += ',\n   month = "'+self.month+'"'
        if(self.key != '' and self.key is not None):
            self.bibtex += ',\n   key = "'+self.key+'"'
            
        self.bibtex+='\n}\n'

        return self.bibtex

    def save_to_file(self,path):
        with open(path,'a') as file:
            file.write(self.bibtex)


