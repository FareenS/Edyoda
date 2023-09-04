string=str(input("enter word that need to be reversed"))
revstring=""
for i in reversed(string):
    revstring+=i
print(revstring)