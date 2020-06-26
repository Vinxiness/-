a = input("first number : ")
b = input("secon number: " )
c = input("third number: ")
d = input("fourth number:")
e = input ("fifth number:")
a = int(a)
b=int(b)
c = int(c)
d = int(d)
e = int(e)


s = [a,b,c,d,e]
k = len(s)
for i in range (0,k):
   for j in range(i+1,k):
      if s[i] > s[j]:
         t = s[j]
         s[j] = s[i]
         s[i] = t
print(s)

   
