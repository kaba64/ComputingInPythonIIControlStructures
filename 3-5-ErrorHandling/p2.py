def sort_characters(string):
    dig = ""
    uper = ""
    lower = ""
    pun = ""
    for i in string:
        if(i.isupper()):
            uper+=i
        if(i.islower()):
            lower+=i
        if(i.isdigit()):
            dig+=i
        if(i.punctuation):
            pun+=i
    return uper+lower+dig+pun
