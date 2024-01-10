
import random


def Szambekeres():
	global lista
	lista = []
	for i in range(5):
		szam = random.randint(1,101)
		lista.append(szam)

	print(f"\nII/A, B, C:\n\t")
	szamlalo = 0
	for eredmeny in lista:
		szamlalo += 1
		if szamlalo == len(lista):
			print(eredmeny,end="")
		else:
			if szamlalo == 1:
				print("\t",eredmeny,end=";")
			else:
				print(eredmeny,end=";")
	return lista








def egyjegyuek_szama():
	szamlalo = 0
	for szam in lista:
		if szam < 10:
			szamlalo += 1
	return round(szamlalo)




def konzol_kiir():
	eredmeny = egyjegyuek_szama()
	print(f"\n\nII/D, E:\n\n\tAz egyjegyűek száma : {eredmeny}") 




def file_kiir():
	eredmeny = egyjegyuek_szama()
	f = open('szamok.txt','w')
	f.write(f"\n\nII/D, E:\n\n\tAz egyjegyűek száma : {eredmeny}")
	f.close()


















