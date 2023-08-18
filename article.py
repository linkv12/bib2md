import reff_parser

class Article :
    def __init__(self, id:int, mandatory_field:dict, optional_field=None) -> None:
        self.id = id
        self.mandatory_field = mandatory_field

        # print('article', self.mandatory_field)
        if optional_field == None :
            optional_field = {}
        self.optional_field = optional_field

        self.ieee_standard()
        self.ieee_md_convert()

    
    def ieee_md_convert(self) :
        _ieee_md = "<a id=\"%i\">[%i]</a>" % (self.id, self.id)
        _ieee_md = "%s %s" % (_ieee_md, self.ieee_reff)
        _ieee_md = str(_ieee_md)
        self.ieee_md = _ieee_md

    def ieee_standard(self) :
        #Author initials. Last name, 
        # “Article title,” Journal Name, vol. Volume, no. Number, 
        # pp. Page range, Month Year, DOI. 
        ieee_reff = "%s, \"%s,\"" % (reff_parser.author_formatter(self.mandatory_field['author']), 
                                     self.mandatory_field['title'])
        ieee_reff = "%s %s," % (ieee_reff, self.mandatory_field['journal'])

        # not all have volume unfortunate
        if 'volume' in self.optional_field:
            ieee_reff = "%s vol. %s," % (ieee_reff, self.optional_field['volume'])

        # check wheter issue is on optional
        if 'issue' in self.optional_field :
            ieee_reff = "%s no. %s," % (ieee_reff, self.optional_field['issue'])
        # check if page range exist 
        if 'page' in self.optional_field :
            ieee_reff = "%s pp. %s," % (ieee_reff, self.optional_field['page'])

        # if doi exist
        if 'doi' in self.optional_field :
            ieee_reff = "%s %s," % (ieee_reff, self.mandatory_field['year'])
            ieee_reff = "%s %s." % (ieee_reff, self.optional_field['doi'])
        else :
            ieee_reff = "%s %s." % (ieee_reff, self.mandatory_field['year'])
        # print(ieee_reff)
        self.ieee_reff = ieee_reff

    def __str__(self) -> str:
        return "Article %i: %s" % (self.id, self.mandatory_field['title'])
    
    def __repr__(self) -> str:
        return self.__str__()
           
# if __name__ == "__main__" :
#     article_info = {'author' : "Dyan Yuliana and Catur Supriyanto",
#                     'journal' : "Jurnal KomTekInfo",
#                     'doi'    : "10.29165/komtekinfo.v5i2",
#                     'issn'   : "2502-8758",
#                     'issue'  : 3,
#                     'page'   : "92-116",
#                     'title'  : "Klasifikasi Teks Pengaduan Masyarakat Dengan Menggunakan Algoritma Neural Network",
#                     'volume' : 5,
#                     'url'    : "https://doi.org/10.29165/komtekinfo.v5i2",
#                     'year'   : 2019
#                     }
#     m, o = reff_parser.split_article_dict(article_info)
#     # pprint(m)
#     # pprint(o)

#     a = Article(id=0, mandatory_field=m, optional_field=o)
#     pprint(a.ieee_md)
#     # a.set_optional_field(optional_field=o)