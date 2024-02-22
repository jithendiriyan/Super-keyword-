class a():                 #class 1
    def __init__(self):   #constructor
        print("A")
    def display(self):
        print("You are in A")
class b():               #class 2
    def __init__(self):  #constructor
        super().__init__() #calling the class 1 constructor using the super keyword
        print("B")
    def display(self):
        print("You are in B")
class c(a,b):               #class 3
    #output is A C because the class 1 is only, which 1st or in left
    def __init__(self):  #constructor
        super().__init__()  # calling the class 2 constructor using the super keyword
        print("C")
    def display(self):
        print("You are in C")
out=c()