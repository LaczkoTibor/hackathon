def mennyi(eredmeny):
  alap = [3,3,3]
  mozdulatok = []

  right = [0,1,1]
  left = [1,1,0]

  for i in range(len(eredmeny)):
    if eredmeny[i] == "":
      break
    else:
      eredmeny[i] = int(eredmeny[i])


  maximum = None
  if eredmeny[3] != "":
    maximum = int(eredmeny[3])
  eredmeny.pop(3)
  
  for i in eredmeny:
    while (maximum is None or maximum > 0) and eredmeny[0] != alap[0]:
      for x in range(len(eredmeny)):
        alap[x] = alap[x] + left[x]
        if alap[x] == 4:
          alap[x] = 1
        if maximum != None:
          maximum -= 1
      mozdulatok.append("left")
    while maximum != 0 and eredmeny[2] != alap[2]:
      for x in range(len(eredmeny)):
        alap[x] = alap[x] + right[x]
        if alap[x] == 4:
          alap[x] = 1
        if maximum != None:
          maximum -= 1
      mozdulatok.append("right")
  if alap != eredmeny:
    print("Megoldhatatlan")
  else:
    print(" ".join(mozdulatok))

with open('./input.txt', 'r') as f:
  input = f.read()

print(input)


sorok = input.splitlines()
sorok = [i.replace("[","") for i in sorok]
olvashato = []

for i in sorok:
  i = i.replace("]",",")
  olvashato.append(i.strip().split(","))
  
for adat in olvashato:
  mennyi(adat)
