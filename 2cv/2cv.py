import textFix as TF
import RSP
import PalindromCount as PC
import filterList as FL
import countWordsIntoDic as CW

#1. Rock, scissors, paper
RSP.RSP()
print("\n")


#2. filter list where datatype is arg

list = [1, 2, "string", True ,5 ]
dataType = bool
FL.filter_list(list,dataType)
print(list)
print("\n")


#3. Count palindroms from entered words
PC.countPalindroms()
print("\n")


#4.Count how many same words is in dictionary
barvy = ['Orange', 'Black', 'Black', 'White', 'Orange', 'Green', 'Red', 'Blue', 'Red']
CW.countWords(barvy)
print("\n")


#5. Fix text
text = "ahojTotoJeŠpatněVygenerovanýText"
print(TF.fixText(text))


