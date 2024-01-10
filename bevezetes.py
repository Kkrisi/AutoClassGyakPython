



def AutoBekeres():
	tipus = str(input("Addj meg egy autó típust: "))
	ev = int(input("Add meg az autód évjáratát: "))

	if ev == 2024:
		szoveg = "friss gyártás"
	elif 2000 > ev:
		szoveg = "öreg autó"
	else:
		szoveg = "átlagos korú"

	print(f"\nI/A:\n\tAutó  neve: {tipus}\n\tGyártási dátum: {ev}")
	print(f"\nI/B:\n\tEz az {tipus} {szoveg}.")






























