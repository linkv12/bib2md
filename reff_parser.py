
def split_article_dict(di:dict) :
    """
    Mandatory info : 
    @author  : str
    @year    : int
    @title   : str
    @journal : str
    @volume  : str

    Optional Info :
    @doi    : str
    @issn   : str
    @issue  : int
    @page   : str
    @url    : str
    """
    art_mandatory_key = ["author", "year", "title", "journal"]
    art_optional_key  = ["doi", "issn", "issue", "page", "url", "volume"]

    mandatory_ = {}
    for m_key in art_mandatory_key :
        try :
            m_val = di[m_key]
            mandatory_[m_key] = m_val
        except KeyError as ke :
            print(di['title'], "is missing mandatory key %s" % (ke))
    
    optional_ = {}
    for o_key in art_optional_key :
        o_val = di.get(o_key, None)
        if o_val != None :
            optional_[o_key] = o_val

    return mandatory_, optional_

def split_inproceeding_dict(di:dict) :
    """
    Mandatory info : 
    @author  : str
    @year    : int
    @title   : str
    @journal : str

    Optional Info :
    @page   : str
    """
    inpr_mandatory_key = ["author", "year", "title", "journal"]
    inpr_optional_key  = ["doi", "issn", "issue", "page", "url"]

    mandatory_ = {}
    for m_key in inpr_mandatory_key :
        try :
            m_val = di[m_key]
            mandatory_[m_key] = m_val
        except KeyError as ke :
            print(di['title'], "is missing mandatory key %s" % (ke))
    
    optional_ = {}
    for o_key in inpr_optional_key :
        o_val = di.get(o_key, None)
        if o_val != None :
            optional_[o_key] = o_val

    return mandatory_, optional_

def split_book_dict(di:dict) :
    book_mandatory_key = ["author", "year", "title", "publisher"]
    book_optional_key  = ["country", "city"]

    mandatory_ = {}
    for m_key in book_mandatory_key :
        try :
            m_val = di[m_key]
            mandatory_[m_key] = m_val
        except KeyError as ke :
            print(di['title'], "is missing mandatory key %s" % (ke))
    
    optional_ = {}
    for o_key in book_optional_key :
        o_val = di.get(o_key, None)
        if o_val != None :
            optional_[o_key] = o_val

    return mandatory_, optional_

def _name_abrv(name:str) :
    special_word = ['de']
    abbrv_name = name.split(' ')
    word_amount = len(abbrv_name)
    res = ''
    for i in range(word_amount):
        if i < word_amount-1 :
            if abbrv_name[i] in special_word :
                res = '%s %s' % (res, abbrv_name[i])
            else :
                ab_word = abbrv_name[i][:1] + "."
                res = '%s %s' % (res, ab_word)
        else :
            res = '%s %s' % (res, abbrv_name[i])
    return res[1::]


def author_formatter(author:str) :
    # parsing based on ieee standard
    # 
    res = author.split(" and ")
    author_amnt = len(res)
    # replace other in author list
    replacement_for = 'et al.'

    temp = None
    if author_amnt == 1 :
        # one author
        temp = _name_abrv(res[0])
    elif author_amnt == 2 :
        # two author
        temp = _name_abrv(res[0])
        if res[1].find('others')>= 0 :
            temp = "%s %s" % (temp, replacement_for)
        else :
            temp = "%s and %s" % (temp, _name_abrv(res[1]))
    elif author_amnt >= 3 or author_amnt <= 6 :
        # 3-6 author
        temp = _name_abrv(res[0])
        for i in range(1, author_amnt) :
            if i == author_amnt -1 :
                if res[i].find('others')>= 0 :
                    temp = "%s %s" % (temp, replacement_for)
                else :
                    temp = "%s and %s" % (temp, _name_abrv(res[i]))
            else :
                if res[i].find('others')>= 0 :
                    temp = "%s %s" % (temp, replacement_for)
                else :
                    temp = "%s, %s" % (temp, _name_abrv(res[i]))
    else :
        # more than 6 author
        temp = _name_abrv(res[0])
        temp = "%s %s" % (temp, replacement_for)

    return temp