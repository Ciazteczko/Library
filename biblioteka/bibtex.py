from converter import Converter

class Azon:
    def __init__(self, pk, title, entry_type, partner, scientific_domain, authors, co_creators, attachments_number):
        self.conv = Converter()
        self.pk = str(pk)
        self.authors = authors
        self.title = str(title)
        self.entry_type = str(entry_type)
        self.partner = str(partner)
        self.scientific_domain = str(scientific_domain)
        self.co_creators = co_creators
        self.attachments_number = str(attachments_number)

    def convert_to_bibtex(self):
        auto = ''
        for i in range (len(self.authors)):
            auto+=str(self.authors[i]['first_name'])
            auto+=' '
            auto+=str(self.authors[i]['last_name'])
            if i != len(self.authors)-1:
                auto+=', '

        co = ''
        for i in range (len(self.co_creators)):
            co+=str(self.co_creators[i]['full_name'])
            if i != len(self.co_creators)-1:
                co+=', '

        self.entry_type = self.conv.remove_space(self.entry_type)
        self.entry_type = self.conv.change_characters(self.entry_type)

        self.bibtex = '@' + self.entry_type + '{' + self.pk +',\n   authors = "'+auto+'",\n   co_creators = "'+co
        self.bibtex += '",\n   partner = "'+self.partner +'",\n   title = "'+self.title+'"'
        self.bibtex += '",\n   scientific_domain = "'+self.scientific_domain +'",\n   attachments_number = "'+self.attachments_number+'"'    
        self.bibtex+='\n}\n'
        return self.bibtex

    def save_to_file(self,path):
        with open(path,'a', encoding='utf-8') as file:
            file.write(self.bibtex)


