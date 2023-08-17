
from pprint import pprint
import reff_parser

class Inproceeding:
    def __init__(self, id:int, mandatory_field:dict, optional_field=None) -> None:
        self.id = id
        self.mandatory_field = mandatory_field
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
        ieee_reff = "%s, \"%s,\"" % (reff_parser.author_formatter(self.mandatory_field['author']), 
                                     self.mandatory_field['title'])
        ieee_reff = "%s %s," % (ieee_reff, self.mandatory_field['journal'])

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
        return "Inproceeding %i: %s" % (self.id, self.mandatory_field['title'])
    
    def __repr__(self) -> str:
        return self.__str__()


if __name__ == "__main__" :
    #    An article in a conference proceedings.
    # Required fields: author, title, booktitle, year
    # Optional fields: editor, volume/number, series, pages, address, month, organization, publisher, note, key
    inproceding_info = {'author' : "Gurinder Singh and Bhawna Kumar and Loveleen Gaur and Akriti Tyagi",
                        'journal': "2019 International Conference on Automation, Computational and Technology Management (ICACTM)",
                        'page'   : "593-596",
                        'title'  : "Comparison between multinomial and Bernoulli na\"\ive Bayes for text classification",
                        'year'   : 2019}
    
    # pprint(inproceding_info)
    m, o = reff_parser.split_inproceeding_dict(inproceding_info)
    i = Inproceeding(id=1, mandatory_field=m, optional_field=o)
    # pprint(i.ieee_md)
    # print(i.ieee_md)

    print(reff_parser.author_formatter(inproceding_info['author']))
    pprint(reff_parser.author_formatter("Ana Margarida de Jesus Cardoso Cachopo and others"))