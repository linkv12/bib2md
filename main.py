# based on mendeley export
# https://www.scribbr.com/ieee/ieee-reference-page/
# https://en.wikipedia.org/wiki/BibTeX

# @article
# @inproceedings
# @book

from refference import Refference
from bibparser import BibParser

if __name__ == "__main__" :
    bibFileName = 'export.bib'
    # md output
    outputFileName = 'output.md'

    # create a BibParser class instance
    bP = BibParser(bibFileName)
    
    # use parsedBib property from bP as parameter for Refference Class Instance
    ref = Refference(bP.parsedBib)
    
    # call output_md function from ref object to output to output.md
    ref.output_md(fileName=outputFileName)
