def verb_ing(s):
    if s[-3:] == "ing":
        return s + "ly"
    elif len(s) > 2:
        return s + "ing"
    else:
        return s
print(verb_ing("hail"))     #hailing
print(verb_ing("swimming")) #swimmingly
print(verb_ing("do"))       #do