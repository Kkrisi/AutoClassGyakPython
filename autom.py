
from AutoClass import Auto


def fajlbeolvasas():
	file = open("auto.txt","r",encoding="UTF-8")
	file.readline()
	sorokLista = file.readlines()
	file.close()

	autoLista = []
	for i in range(len(sorokLista)):
		aktElem = sorokLista[i]
		sorLista = aktElem.strip().split("$")
		nev = str(sorLista[0])
		datum = int(sorLista[1])

		auto = Auto(nev,datum)
		autoLista.append(auto)

	return autoLista






def flotta():
	lista = fajlbeolvasas()
	db = 0
	for auto in lista:
		db += 1

	print(f"\nIII/Flotta:\n\n\tAutók száma: {db}.")
	return db




def Legfiatalabb():
	lista = fajlbeolvasas()
	legf, ev = "", 2024
	for i in range(len(lista)):
		if lista[i].datum < ev:
			ev, legf = lista[i].datum, lista[i].nev 
	print(f"\nIII/Legfiatalabb\n\n\tA legfiatalabb autó: {legf} ({ev}).")
	return legf, ev





def AtlagosKor():
	lista = fajlbeolvasas()
	szamlalo, osszeg = 0, 0
	for i in range(len(lista)):
		osszeg += (2024 - lista[i].datum)
		szamlalo += 1
	atlag = round(osszeg / szamlalo, 2)
	print(f"\nIII/Átlag kor\n\n\tAz autók átlagos kora: {atlag} év.")
	return atlag
















