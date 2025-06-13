def reverse(s):
    result = ""
    for char in s:
        result = char + result
    return result

orig = input("Type a phrase: ")
result = reverse(orig)
if orig == result:
        print("** palindrome **")
else:
    print("reverse =", result)



#Type a phrase: alice
#reverse = ecila

#Type a phrase: anna
#** palindrome **

#Type a phrase: 
#** palindrome **