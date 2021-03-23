print("Lista zakupów")
lista_zakupów = ["Chleb","Pączek","Bułki","Marchew","Seler","Rukola"]
shopping_dict = {
    "piekarnia" : ["Chleb","Pączek","Bułki"],
    "warzywniak" : ["Marchew","Seler","Rukola"]
}
for key , values in shopping_dict.items():
        print(f"Idę do {key.capitalize()}, kupuję tu nastepujące rzeczy: {values}" )
print(f"W sumie kupuje {len(lista_zakupów)} produktów. ")