#4. Napište funkci, která vypočítá počet výskytů slov v poskytnutém listu a vrátí jej v podobě slovníku (viz. Example výstupu)
#vstup:
#barvy = ['Orange', 'Black', 'Black', 'White', 'Orange', 'Green', 'Red', 'Blue', 'Red']
#výstup:
#{'Red': 2, 'Orange': 2, 'Black': 2, 'Green': 1, 'Blue': 1, 'White': 1}



def countWords(barvy):
    dictionary = {}
    for x in barvy:
        if x in dictionary:
            dictionary[x] += 1
        else:
            dictionary[x] = 1

    print(dictionary)

