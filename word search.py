'''with open('Path/to/file', 'r') as content_file:
    content = content_file.read()
	
f = open("C:/Users/Superman/Desktop/krypton.log")
data = f.read()

#f=open("C:\Users\venkat\Desktop\searches.txt",'r')
import csv
data= csv.reader(open('search.txt', 'r'))
for x in data:
	print x 
#data=f.read()'''





file = open('search.txt', 'r')
words = list(file.read().split())
#print words
count=0
inputword=raw_input("Enter the word:")
print words.count(inputword)









'''for x in words:
	if x==inputword:
		count++
print count

import csv
my_reader = csv.reader(open('search.txt'))

#inputword=raw_input("Enter the word:")
ctr = 0
wordlist=[]
wordlist.append(my_reader.split(' '))
print wordlist


with open('search.txt', 'r') as f:
    mySearch = [line.strip().split(' ') for line in f]
print mySearch'''


