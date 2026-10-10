string=input("Enter a word:")

character=input("Enter a single character ")

i=0

count=0
 
while i<len(string):
    if character==string[i]:
        count=count+1
    i=i+1
print(count)