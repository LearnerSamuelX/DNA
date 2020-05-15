# specs:
#     - correct number of command-line arguments
#     - two command-line arguments:1st argument - CSV file, 2nd argument - text file
#     - the program reads DNA sequences.and stores its contents into memory
#     - copy this line when RUN: python dna.py databases/small.csv sequences/4.txt
import sys
from sys import argv, exit
import csv

if len(argv) != 3 :
    print("ERROR...missing command-line argument")
    exit(1)


csvOpen = open(sys.argv[1],"r")  #CSV file containing STR counts
txtOpen = open(sys.argv[2],"r")  #DNA sequences

# To get rid of the name column but keep the dna bases to be checked
csvFile=csv.reader(csvOpen)
info = [] #everything from the csv file
for row in csvFile:
    info.append(row)
givenDNA=(info[0][1:])


csvFile=csvOpen.read()
txtFile=txtOpen.read()


L = len(txtFile)
dna = givenDNA
# two for loops
# first loop, looping through dna array
# second loop, looping through txt file

STR=0 # the highest number of continous repeat of ONE base
STRnum=[]  # An array, in which numbers of STR for the selected DNA bases are stored
ranking=[] # An array, in which the numbers of STR of a selected bases, is recorded. with 'max'method, the highest number of repeat can be determied
buffer_arr=[]

#grab a dna base from the given csv file by sequence
for i in range (len(dna)):
    r=1 # r acts more like a cursor
    base=dna[i]
    s=len(base) #length of the selected dna base

    #looping in the txt file
    for j in range (L):
        #found a matching base
        if txtFile[j:j+s]==base:
            # to check the next adjacent unit making sure the unit repeats
            if txtFile[j+s:j+s+s]==txtFile[j:j+s]:
                r=r+1
                j=j+s
            # source of all evil right here
            # else:
            #     r=1
            #fix the above part
    ranking.append(str(r))

STRnum=ranking
# print(ranking)

name = []
#looping through info
for k in range(1,len(info)):
    if info[k][1:]==STRnum:
        name.append(info[k][0])

if name!=[]:
    print(name[0])
else:
    print("No match.")