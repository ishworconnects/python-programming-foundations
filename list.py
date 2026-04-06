#what is list -> to store multiple variables

fruits = ["apple", "banana", "cherry"]

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

print(fruits)

#Indexing
print(fruits[0]) #apple
print(fruits[1]) #banana
print(fruits[2]) #cherry

print(days[0]) #Monday  
print(days[4]) #Friday
print(days[-3]) 

#Slicing positive and negative -first is included and last is not

print(days[1:3])
print(days[-4:-1])
print(days[-4:])


#Change the value of list/single element
#days[1]="I"
#print(days)

#Changing multiple elements
#days[1:4] = ["love", "python", "programming"]
#print(days)

#length of list

print(len(days))

#sorted gives sorted list in alphabetical order or numerical order
print(sorted(days))

#sum( and max( and min() functions work only for numerical values
weights = [50, 100, 70, 63, 90]
print(sorted(weights))
print(sum(weights))
print(max(weights))
print(min(weights))

#add item to list-append() method adds an item to the end of the list
days.append("Holiday")
print(days) 

#remove item from list-remove() method removes the first occurrence of the specified value
days.pop() #removes last item
days.remove("Tuesday")
print(days)

#check if item exists in list
print("Monday" in days) #True
print("Rday" in days) #False

if "Wednesday" in days:
    print("Yes, Wednesday is in the list of days.")


#List is a collection which is ordered and changeable. Allows duplicate members.[]
#Tuple is a collection which is ordered and unchangeable. Allows duplicate members.()

#Set is a collection which is unordered , unchangeable * and unindexed. No duplicate members.{}