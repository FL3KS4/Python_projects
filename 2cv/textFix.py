#5. Napište funkci, která „opraví“ texty psané tímto stylem:
#„ahojTotoJeŠpatněVygenerovanýText“ na:
#„Ahoj toto je špatně vygenerovaný text.“
#Správné řešení splňuje:
#a) Velké písmeno na začátku věty.
#b) Nahradit velké písmena na začátku slov (kromě prvního) malými písmeny.
#c) Doplnit mezery na místa, kam patří (pozn. Vždy před velké písmeno).
#d) Vždy doplní tečku na konec věty.


def fixText(text):
    completeText = " "

    textList = [x for x in text]

    for c in textList:
        if c == textList[0] and c.islower():
            textList[textList.index(c)] = c.upper()
        if c != textList[0] and c.isupper():
            textList[textList.index(c)] = ' ' + c.lower()

    createList = ''.join(textList).split(' ')

    return(completeText.join(createList)+ '.')
