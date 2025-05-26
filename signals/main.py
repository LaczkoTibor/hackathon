def dekod(adat):
  dekodolo = {}
  for i in adat:
    for szam,betu in zip(i[0],i[1]):
      dekodolo[szam] = betu
  
  return dekodolo


with open('./input.txt', 'r') as f:
  input = f.read()
  
print(input)

lista = eval(input)
forras = []

for i in lista:
  forras.append(i)

eredmeny = dekod(forras)

print("{")
for k in sorted(eredmeny.keys()):
  print(f'\t"{k}": "{eredmeny[k]}",')
print("}")
