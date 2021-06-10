#3. Vytvořte program, který od uživatele vezme vstup v podobě n slov a vrátí počet palindromů
#(dopředu známý počet slov, nejdřív např. Zadat číslo a pak načítat slova)


def countPalindroms():
    howMany = input("Enter how many words you wanna add: ")
    lst = []
    count = 0
    for i in range(int(howMany)):
        addWord = input("Enter word number " + str(i+1) +" :")
        lst.insert(i, addWord)

    for i in range(int(howMany)):
        if lst[i] == lst[i][::-1]:
            count += 1

    print(count)

     

