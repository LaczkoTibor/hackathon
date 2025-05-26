def dobas(a,b):
  a = int(a)
  b = int(b)
  
  dobokackak = [2,3,4,6,8,10,20]
  fajta = []
  maximum = 0
  darabok = []
  vegeredmeny = []
  db = 1
  n = 0

  while a <= 0:
    n += 1
    a += 1
    b += 1
  if n != 0:
    n -= 1
    
  if (b-a)+1 > 20:
    db += ((b-a)+1) // 20

  szam = (b-a)+1

  if db > 1:
    szam += db-1

  while szam > 0:
    for kocka in range(len(dobokackak)):
      if szam >= dobokackak[kocka] and szam < dobokackak[kocka+1]:
        szam -= dobokackak[kocka]
        fajta.append(dobokackak[kocka])
      elif szam > 20:
        szam -= dobokackak[-1]
        fajta.append(dobokackak[-1])
      elif szam == 1:
        szam -= dobokackak[0]
        fajta.append(dobokackak[0])

  fajta_adat = []

  for i in fajta:
    if i not in fajta_adat:
      darabok.append(fajta.count(i))
      fajta_adat.append(i)
    maximum += i
    
  
  for x,y in zip(darabok[::-1],fajta[::-1]):
    vegeredmeny.append(str(x) + str(f"d{y}"))
  if b-maximum != 0:
    vegeredmeny.append(str(f"{(b-maximum)-n:+}"))

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



