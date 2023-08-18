from article import Article
from inproceeding import Inproceeding
from book import Book
from bibparser import BibParser
import reff_parser
import codecs

from pprint import pprint
class Refference:
    def __init__(self, parsedBib:list) -> None:
        self.parsedBib = parsedBib

        # list containing article, inproceeding or book object
        self.reffEntry = self.processBib()


    def processBib(self) :
        entry = []
        entryAmount = len(self.parsedBib)
        for i in range(entryAmount) :
            # print(self.parsedBib[i]['id'])
            id = self.parsedBib[i]['id']
            type = self.parsedBib[i]['type']
            # pprint(self.parsedBib[i]['info'])
            match type :
                case 'article' :
                    m,o = reff_parser.split_article_dict(self.parsedBib[i]['info'])
                    entry.append(Article(id, m, o))
                case 'inproceeding' :
                    m,o = reff_parser.split_inproceeding_dict(self.parsedBib[i]['info'])
                    entry.append(Inproceeding(id, m, o))
                case 'book' :
                    m,o = reff_parser.split_book_dict(self.parsedBib[i]['info'])
                    entry.append(Book(id, m, o))
        return entry

    # print ieee, and md
    # save it to output.txt or .md

    def print_ieee(self):
        text = ""
        entryAmount = len(self.reffEntry)
        for i in range(entryAmount):
            if i == 0 :
                text = self.reffEntry[i].ieee_reff
            else :
                text = "%s\n%s" % (text, self.reffEntry[i].ieee_reff)

        return text
    
    def print_md(self):
        text = ""
        entryAmount = len(self.reffEntry)
        for i in range(entryAmount):
            if i == 0 :
                text = self.reffEntry[i].ieee_md
            else :
                text = "%s\n\n%s" % (text, self.reffEntry[i].ieee_md)

        return text        
    
    def output_ieee(self, fileName='output.txt'):
        with codecs.open(fileName, mode='w', encoding='utf-8') as fileWriter :
            texts = self.print_ieee()
            fileWriter.write(texts)

    def output_md(self, fileName='output.md'):
        with codecs.open(fileName, mode='w', encoding='utf-8') as fileWriter :
            texts = self.print_md()
            fileWriter.write(texts)




# if __name__ == "__main__" :
#     fName = "export.bib"
#     bP = BibParser(fName)

#     ref = Refference(bP.parsedBib)
#     print(ref.print_md())
#     ref.output_md()