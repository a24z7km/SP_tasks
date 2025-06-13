s1 = "The quick brown fox jumps over the lazy dog."
s2 = s1.split(" ")
s2 = s2[0]
print(s2) # The

s2 = s1.split(" ")
s2 = s2[3]
print(s2) # fox

s2 = s1.split(" ")
s2 = s2[1] + " " + s2[-1].rstrip(".")
print(s2) # quick dog

s2 = s1.split(" ")
s2 = s2[0] + " " + s2[-2] + " " + s2[2] + " " + s2[3] + "."
print(s2) # The lazy brown fox.