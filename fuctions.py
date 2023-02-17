def hello():
    print("this is my first function.")
hello()
def calculate():
    x=7
    y=8
    print(x*y)
calculate()
#adding parameters/arguements
def majina(fname,lname):
    print(fname+" "+lname)
majina("Queenvine","Muthoni")
majina("Lily","Jewel")
majina("Mary","Muthoni")
majina("lenny","Mwangi")

def greetings(name, greeting="hello"):
    print(greeting+" "+name)
greetings("Queenvine")
greetings("Niaje","Joan")

def performance(position,name):
    print("position "+position+": "+name)
performance("10","Mariah")

def student(name,grade,stream):
    print("I'm "+name+" in grade "+grade+" "+stream)
student("Mariah","11","blue")
#printing max value
def maximum(a,b,c,d,e,f):
    return max(a,b,c,d,e,f)
result=maximum(4,9,5,6,2,7)
print(result)
#printing min value
def minimum(a,b,c,d,e,f):
    return min(a,b,c,d,e,f)
result=minimum(7,54,8,4,5,9)
print(result)
# sorting a list
def sort_list(lst):
    return sorted(lst)
answer=sort_list([3,8,5,7,9,4,2])
print(answer)
# printing a range of numbers: use for loop
def print_num(n):
    for i in range(n):
        print(i)
print_num(5)