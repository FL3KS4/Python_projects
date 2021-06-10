#1. Multiplicate unknown args
def multiplication(*n):
    temp = 1
    for x in n:
        temp *= x
    return temp  

print(multiplication(5,2,3,4))

#2. Lambda for true, false
def my_lambda(name, char):
    x = lambda x,y: "False" if x[0]!= str(y) else "True"
    return x(name,char)

print(str(my_lambda('Tom', 'T')))

#3.map list comprehention
def comprehention(x):
    return "!" + x + "!"


def my_map(func, list_vole):
     newlist = [func(x) for x in list_vole ]
     return newlist
    

print(my_map(comprehention, ["a","b","c"]))

#4. sort file then return new file
def sort_file(filename, output):
    my_file = open(filename, "rt")

    a = []

    for line in my_file:
        a.append(line)

    my_file.close()   

    a.sort()

    my_file = open(output, "x")

    for x in a:
        my_file.write(x)

    my_file.close()

    return True
    
#Je to zakomentovano protože pro spustění je třeba smazat původní output soubor nebo ho přejmenovat ve funkci
#sort_file("input.txt", "output.txt")  

#5. Int to String made with map
def int_to_string(listT, tupleT):
    newlist = map(str, listT)
    newtuple = map(str,tupleT)
    return list(newlist),tuple(newtuple)

listN, tupleN = int_to_string([1,2,3], (1,2,3))

print(listN)
print(tupleN)