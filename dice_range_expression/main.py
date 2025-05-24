def dobas(a,b):
  a = int(a)
  b = int(b)
  
  dobokackak = [20,10,8,6,4,3,2]
  szam = (b-a)+1
  seged = []
  fajta = []
  maximum = 0
  darabok = []
  vegeredmeny = []
  db = 1
  while szam > 20:
    db += 1
    seged.append(20)
    szam -= 20
  if seged == []:
    seged.append(szam)
  else:
    seged.append(szam+(db-1))
  
  szam = (b-a)+1

  for dobas in seged:
    for kocka in range(len(dobokackak)):
      if dobas <= dobokackak[kocka] and dobas > dobokackak[kocka+1]:
        fajta.append(dobokackak[kocka])

  for i in fajta:
    darabok.append(fajta.count(i))
    maximum += i
  
  for x,y in zip(darabok,fajta[::-1]):
    vegeredmeny.append(str(x) + str(f"d{y}"))
  if b-maximum != 0:
    vegeredmeny.append(str(f"{b-maximum:+}"))
     

  print("+".join(vegeredmeny[:-1])+"".join(vegeredmeny[-1]))


with open('./input.txt', 'r') as f:
  input = f.read()

print(input)

sorok = input.splitlines()
olvashato = []

for i in sorok:
  olvashato.append(i.strip().split(" "))

for i in range(len(olvashato)):
  dobas(olvashato[i][0],olvashato[i][1])



