#for loop to extract items from a list
fruits = ["apple", "banana", "cherry" , "grapes", "orange"]
for fruit in fruits:
    print(fruit)    

#Explain importance of for loop with an example of birtday candy
friends = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heidi", "Ivan", "Judy", "Karl", "Leo", "Mallory", "Nina", "Oscar", "Peggy", "Quentin", "Rupert", "Sybil", "Trent"  , "Uma", "Victor", "Walter", "Xavier", "Yvonne", "Zara" ]

for friend in friends:
    print(f"{friend} eats candy.")

#using range() function to generate a sequence of numbers
for i in range(15):
    print(i) #0,1,2,3,4
    print(i+1) #1,2,3,4,5

#while loop
i = 0
while i < 10:
    print(i)
    i += 1 #i = i + 1


#list comphrension before and after

numbers = [25, 10,60, 45, 90,57, 80, 15, 30, 5 ]
#pass_marks =[]

#for number in numbers:
  ##  if number >= 40:
     #   pass_marks.append(number)
#print(pass_marks)

pass_marks1 = [number for number in numbers if number >= 40]
print(pass_marks1)

