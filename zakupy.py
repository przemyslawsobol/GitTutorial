lista_zakupów = {}
lista_zakupów["mediamarkt"] = ["ps4", "tablet", "słuchawki"]
lista_zakupów["decathlon"] = ["rower", "kurtka", "buty"]


for sklep, produkt in lista_zakupów.items():
    sklepy = str(sklep)
    supersklepy = sklepy.title()
    produkty = str(produkt)
    superprodukty = produkty.title()
    print(f"Idę do {supersklepy} i kupuję tam {superprodukty}")

wszystkie_produkty = lista_zakupów["mediamarkt"] + lista_zakupów["decathlon"]
suma = len(wszystkie_produkty)
print(f"W sumie kupuję {suma} produktów")