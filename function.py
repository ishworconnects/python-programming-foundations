#What is function in python?-it does a specific task and reusable block of code
#A function is a block of code that performs a specific task. It is reusable and can be called multiple times in a program. 
#defining a function

def greet():
    print("Hello, welcome to Python programming!")
#calling a function
greet() #function call


#function with parameters -- someone increased marks of students

def increase_marks(marks):
    marks = marks + 30
    return marks

# calling the function
#new_marks = increase_marks(20)
new_marks = increase_marks(int(input("Enter the marks: ")))

print(new_marks)