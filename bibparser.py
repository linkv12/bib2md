# handle parsing bib
# output -> list of neat dict ordered asc by id
#           with id added
#       {type : book, id: 1, info: {key: val}}
#       info -> {author: bla, year: 2017, publisher: O'Reilly Media Inc., title: book_title}

import re
from pprint import pprint
class BibParser :

    def __init__(self, file_name:str) -> None:
        self.fileName = file_name
        self.parsedBib = self.parse()

    def parse(self) :
        # in bib it is binary?
        # special int
        specialType = ['issue', 'year']
        lines = []
        
        with open(file=self.fileName, mode='rb') as fileHandler :
            line = fileHandler.readline().decode().removesuffix('\n')
            while line :
                lines.append(line)
                line = fileHandler.readline().decode().removesuffix('\n')

        # lines contain all line from .bib
        # traversing through list of lines

        # starting id
        id = 1
        # only check @article etc when start_flag is false
        start_flag = False

        entry = []
        entryDict = {}
        entry_info = {}
        for i in range(len(lines)) :
            # looking for @type
            if not start_flag :
                if "@article" in lines[i] :
                    entryDict['id'] = id
                    id += 1
                    entryDict['type'] = 'article'
                    start_flag = True
                elif "@inproceedings" in lines[i] :
                    entryDict['id'] = id
                    id += 1
                    entryDict['type'] = 'inproceeding'
                    start_flag = True
                elif "@book" in lines[i] :
                    entryDict['id'] = id
                    id += 1
                    entryDict['type'] = 'book'
                    start_flag = True
            else :
                # parsing it here
                # try catch ending -> }
                if '}' == lines[i] :
                    start_flag = False
                    entryDict['info'] = entry_info
                    entry.append(entryDict)

                    entryDict = {}
                    entry_info = {}
                # not ending or starting
                else :
                    # remove whitespace prefix
                    text = re.sub("(^ *)", "", lines[i])
                    # remove { or }, 
                    text = re.sub("({|},)","",text)

                    # split it to key, value
                    key, values = text.split(' = ')
                    if key in specialType :
                        entry_info[key] = int(values)
                    else :
                        entry_info[key] = values
        
        return entry

# if __name__ == "__main__" :
#     fName = "export.bib"
#     bP = BibParser(fName)
#     print("you have %s entry in bib file" % len(bP.parse()))

    # tex = '   author = {Bruce G Marcot and Anca M Hanea},'
    # # remove whitespace prefix
    # tex = (re.sub("(^ *)", "", tex))

    # # remove { or },
    # tex = re.sub("({|},)","",tex)

    # print(tex.split(' = '))
