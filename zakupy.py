lista_zakupów = {}
lista_zakupów["mediamarkt"] = ["ps4", "tablet", "słuchawki"]
lista_zakupów["decathlon"] = ["rower", "kurtka", "buty"]
print(lista_zakupów)

for sklep, produkt in lista_zakupów:
    sklepy = str(sklep)
    supersklepy = sklepy.title()
    produkty = str(produkt)
    superprodukty = produkty.title()
    zakupy = f"Idę do {supersklepy} i kupuję tam {superprodukty}"
    print(zakupy)