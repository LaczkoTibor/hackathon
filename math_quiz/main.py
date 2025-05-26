import math

#1. feladat

print(f"1.:")
#2. feladat
def f(x):
    return 4**x + 6**x - 9**x


minimum = 0 #A szám amitől indulunk
maximum = 10 #A szám ameddig nézzük
pontossag = 1e-7 #Megadom hogy mennyire legyen pontos

while maximum - minimum > pontossag: ##Addig ad igaz értéket, amég el nem érik a kívánt pontosságot
    kozep = (minimum + maximum) / 2 #Megkeresem a kető közepét
    if f(kozep) > 0: #Megnézi melyiktől van meszebb, azt egyenlővé teszi vele (igy felváltva mindkettő kap egy értéket, ami végül az eredmény nél kisebb és nagyobb lesz)
        minimum = kozep
    else:
        maximum = kozep

print(f"2.:{(minimum + maximum) / 2}") #Össze adom a kettőt és elosztom 2 vel, mivel így megkapom a kellő eredményt.

#3. feladat
megoldas3 = 0
szam_alap = 1 #A gyök alatt lévő szám

while szam_alap != 100:  # Addig meg végig, amég nem lesz 100 a gyök alatti szám
    megoldas3 += 1/(szam_alap ** 0.5 + (szam_alap+1)**0.5) # Az egyenlet, amit mindig hozzá ad
    szam_alap += 1



print(f'3.:{megoldas3}')


#4. feladat
n = 1
Egyenlet = None
while Egyenlet != 0: #Addig probálja amég 0 nem  lesz a megoldás.
    Egyenlet = n**(2*n)-2*n**n+1
    if Egyenlet != 0:
        n += 1

print(f'4.:{n}')

#5. feladat

eset5_1 = 170 #Azstal + macska - egér =  170
eset5_2 = 130 #Asztal + egér - macska = 130

megoldás5 = (eset5_1 +eset5_2) / 2 # Mivel a macskát és az egeret is kivonjuk az össze adott képlwtwkben, így a két asztal az összege az eset5_1 és eset5_2, amit elosztunk 2-vel.


print(f'5.:{int(megoldás5)}cm')
#6. feladat
eset6_1 = 10 #Macska + Egér
eset6_2 = 20 #Kutya + Egér
eset6_3 = 24 #Kutya + Macska

macska = (eset6_3-(eset6_2-eset6_1))/2 #Kiszámolom a macskát úgy, hogy kiszámolom a macska - kutya különbséget aztán kivonom a kutya + macskábol, ami így olyan lesz, mintha 2 macska lenne, ezért elosztom 2-vel.
kutya = eset6_3 - macska #A 3.esetből kiszámolom a kutya súlyát
egér = eset6_1 - macska # Az első esetből kiszámolom az egér súlyát.

összes_kg = macska + kutya + egér

print(f'6.:{int(összes_kg)}kg')
#7. feladat
dobhato_szam = 6 #Ennyi szám van
Anna = 1 #ennyi esélye van 6 ot dobni
Balazs = 1 #ennyi esélye van 6 ot dobni
Anna_esélye = Anna / dobhato_szam * ((dobhato_szam**2) / ((Anna+Balazs)*dobhato_szam - 1)) # Anna hatosdobási esélyét (1/6) megszoroztam mindkettőjük össszes lehetősége / kivéve amikor balázs dob 6 ot(36/11)

print(f'7.:{Anna_esélye}')
