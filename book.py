import reff_parser

class Book:
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
        # check if city exist
        if 'city' in self.optional_field :
            ieee_reff = "%s %s," % (ieee_reff, self.mandatory_field['city'])
        # check if country exist
        if 'country' in self.optional_field :
            ieee_reff = "%s %s," % (ieee_reff, self.mandatory_field['country'])

        # add publisher
        ieee_reff = "%s %s," % (ieee_reff, self.mandatory_field['publisher'])

        # check if page range exist 
        if 'page' in self.optional_field :
            ieee_reff = "%s pp. %s," % (ieee_reff, self.optional_field['page'])

        # add year
        ieee_reff = "%s %s." % (ieee_reff, self.mandatory_field['year'])
        # print(ieee_reff)
        self.ieee_reff = ieee_reff

    def __str__(self) -> str:
        return "Inproceeding %i: %s" % (self.id, self.mandatory_field['title'])
    
    def __repr__(self) -> str:
        return self.__str__()
