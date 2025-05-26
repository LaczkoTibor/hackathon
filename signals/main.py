def dekod(adat):
  dekodolo = {}
  for szam,betu in zip(adat[0],adat[1]):
    dekodolo[szam] = betu
  
  for x,y in dekodolo.items():
    print(f"{x}:{y}")


with open('./input.txt', 'r') as f:
  input = f.read()

lista = eval(input)

for i in lista:
  dekod(i)
