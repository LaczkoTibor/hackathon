def fibonacci(N):
  lista = []
  vegleges = []
  if  not str(N).replace('.', '', 1).isdigit() or float(N) < 0 :
    print("N/A")
  else:
    if lista == []:
        lista.append(0)
    if len(lista) < 2:
        lista.append(1)

    while float(N) > lista[-1] + lista[-2]:
      lista.append(lista[-1] + lista[-2])
    
    for i in lista:
      if i % 3 == 0:
          vegleges.append(i)
      
    print(", ".join(str(elem) for elem in vegleges))



with open('./input.txt', 'r') as f:
  input = f.read()

print(input)


adat = input.split("\n")

for i in adat:
  fibonacci(i)
