def dobas(min_val,max_val):
  min_val = int(min_val)
  max_val = int(max_val)

  dobokackak = [2,3,4,6,8,10,20]
  fajta = []
  maximum = 0
  darabok = []
  vegeredmeny = []
  db = 1
  n = 0

  while min_val <= 0:
    n += 1
    min_val += 1
    max_val += 1
  if n > 0:
    max_val += 1
    n += 1

  if (max_val-min_val)+1 >= 20:
    db += ((max_val-min_val)+1) // 20
  if (max_val-min_val)+1 >= 10 and (max_val-min_val)+1 < 20:
    db += 1

  szam = (max_val-min_val)+1

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
  if max_val-maximum != 0:
    vegeredmeny.append(str(f"{(max_val-maximum)-n:+}"))

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



