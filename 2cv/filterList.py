#2. Vytvořte funkci filter_list, která bude mít dva parametry. List a datový typ. Funkce vrátí list BEZ prvků zadaného datového typu.
#list = [1, 2, "string", True ,5 ]
#dataType = bool
#filter_list(list, dataType)
#výsledek: [1, 2, "string", 5]


def filter_list(list, dataType):
    for x in reversed(range(len(list))):
        if type(list[x]) == dataType:
            list.pop(x)
                  
