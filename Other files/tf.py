def isinorder(word):
    if len(word) == 1:
        return True
    else:
        firstchar = word[0]
        restofword = word[1:]
        if firstchar > restofword:
            return False
        else:
            return isinorder(restofword)



print(isinorder('APE'))
