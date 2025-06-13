def goal(c):
  if c >= 10:
    return "Number of goals: " + "many"
  else:
    return "Number of goals: " + str(c)

print(goal(4))
print(goal(9))
print(goal(10))
print(goal(99))