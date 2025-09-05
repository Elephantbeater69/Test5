dict={'Yashas':98,'Jaga':99,'Keerthan':100,'Davana':99,'Pboss':100}
name=input("Enter the students's name: ")
if name in dict:
    print("{}'s marks: {}".format(name,dict[name]))
else:
    print("Student not found.")
