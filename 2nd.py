string=input("string1 = ")
s=string.lower()
p=s.replace(" ","")
uniq=set(p)
r=','.join(uniq)
print('uniqueLetters =',r)




