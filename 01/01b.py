a=0
k=["one","two","three","four","five","six","seven","eight","nine"]
for i in open("01.txt","r").readlines():
 r=[]
 for j,h in enumerate(i):
  if h.isnumeric():r+=[int(h)]
  for c in k:
   if i[j:].startswith(c):r+=[k.index(c)+1]
 a+=r[0]*10+r[-1]
print(a)

a=0
for i in open("1").readlines():
 r=[]
 for j,h in enumerate(i):
  if h.isdigit():r+=[int(h)]
  for c in range(9):
   if i[j:].startswith(["one","two","three","four","five","six","seven","eight","nine"][c]):r+=[c+1]
 a+=r[0]*10+r[-1]
print(a)