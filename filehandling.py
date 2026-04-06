#dictionary
#fruits =["apple", "banana", "cherry"]
#print(fruits)

fruits = {
    "apple" : 20,
    "banana" : 30,
    "cherry" : 15
}

print(fruits)

#add item to dictionary
fruits["grapes"] = 25
print(fruits)

#edit item in dictionary
fruits["banana"] = 10
print(fruits)

#delete item using popitem() method- note: in versions before 3.7, random item is removed, in 3.7 and later, the last item is removed
fruits.popitem()
print(fruits)

#open file
f = open("Man.txt")

#read file
print(f.read()) #after reading once, the file pointer is at the end of the file, so it returns empty string
#close file
f.close()
#write to file - a and w modes
f = open("Man.txt", "a") #a mode will append to the file, w mode will overwrite the file
f.write("This is a new line.")

f = open("Man.txt", "w")
f.write("This is a w line.") 

#create a new file - x will create a new file as well as a and w
#but if the file already exists, x will raise an error while a and w will overwrite the file

#f = open("NewFile.txt", "x")
#f.write("This is a new file created using x mode.")

#delete file -import os module and use os.remove() function
import os
os.remove("NewFile.txt")    
