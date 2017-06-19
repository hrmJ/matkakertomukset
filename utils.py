import string

def BuildString(words):
    """Constructs a printable sentence"""
    printstring = ''
    isqmark = False
    #POISTA NONE-arvon saaneet sanat:
    words = list(filter(None.__ne__, words))
    for idx, word in enumerate(words):
        spacechar = ' '
        if idx>0:
            previous_word = words[idx-1]
            #if previous tag is a word:
            if  previous_word not in string.punctuation:
                #...and the current tag is a punctuation mark. Notice that exception is made for hyphens, since in mustikka they are often used as dashes
                if word in string.punctuation and word != '-':
                    #..don't insert whitespace
                    spacechar = ''
                    #except if this is the first quotation mark
                    if word == '\"' and not isqmark:
                        isqmark = True
                        spacechar = ' '
                    elif word == '\"' and isqmark:
                        isqmark = False
                        spacechar = ''
            #if previous tag was not a word
            elif previous_word in string.punctuation:
                #...and this tag is a punctuation mark
                if (word in string.punctuation and word != '-' and word != '\"') or isqmark:
                    #..don't insert whitespace
                    spacechar = ''
                if previous_word == '\"':
                    spacechar = ''
                    isqmark = True
                else:
                    spacechar = ' '
        else:
            #if this is the first word
            spacechar = ''

        printstring += spacechar + word

    return printstring
