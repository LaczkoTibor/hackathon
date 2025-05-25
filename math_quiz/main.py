#1. feladat




print('1.:')
#2. feladat
print('2.:')
#3. feladat
megoldas3 = 0
szam_alap = 1

while szam_alap != 100:
    megoldas3 += 1/(szam_alap ** 0.5 + (szam_alap+1)**0.5)
    szam_alap += 1



print(f'3.:{megoldas3}')


#4. feladat
n = 1
Egyenlet = None
while Egyenlet != 0:
    Egyenlet = n**(2*n)-2*n**n+1
    if Egyenlet != 0:
        n += 1

print(f'4.:{n}')

#5. feladat

eset5_1 = 170 #Azstal + macska - egér =  170
eset5_2 = 130 #Asztal + egér - macska = 130

megoldás5 = (eset5_1 +eset5_2) / 2 # Mivel a macskát és az egeret is kivonjuk az össze adott képlwtwkben, így a két asztal az összege az eset5_1 és eset5_2, amit elosztunk 2-vel.


print(f'5.:{int(megoldás5)}')
#6. feladat
eset6_1 = 10 #Macska + Egér
eset6_2 = 20 #Kutya + Egér
eset6_3 = 24 #Kutya + Macska

macska = (eset6_3-(eset6_2-eset6_1))/2 #Kiszámolom a macskát úgy, hogy kiszámolom a macska - kutya különbséget aztán kivonom a kutya + macskábol, ami így olyan lesz, mintha 2 macska lenne, ezért elosztom 2-vel.
kutya = eset6_3 - macska #A 3.esetből kiszámolom a kutya súlyát
egér = eset6_1 - macska # Az első esetből kiszámolom az egér súlyát.

összes_kg = macska + kutya + egér

print(f'6.:{int(összes_kg)}')
#7. feladat



print('7.:')
