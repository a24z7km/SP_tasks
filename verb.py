def verb_ing(s):
    if len(s) <= 3:
        return s + "ing"
    elif s[-3:] == "ing":
        return s + "ly"
    elif len(s) >= 2:
        return s
print(verb_ing("hail"))
print(verb_ing("swimming"))
print(verb_ing("do"))