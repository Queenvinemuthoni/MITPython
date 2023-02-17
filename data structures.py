#list in python
myclassmate=["Muthoni","Tumaini","Michael","Raheen"]
myclassmate[0]="Queenvine"
#append means add
myclassmate.append("Masika")# adding at the end of the list
myclassmate.insert(2, "Kristy") #adding at a specific position
myclassmate.insert(5, "Hillary")
myclassmate.append("Harry")
myclassmate.sort()
print(type(myclassmate))
print(myclassmate)
print(myclassmate[0])
print(myclassmate[3])
#start counting the positions from 0
print("My name is "+myclassmate[0])

#tuple in python
myfavfruit=("mangoes","passion","apples","oranges","passion")
mynumbers=[2,3,6,8,1,7,5]
#tuple and list accepts a duplicate
#in tupple you cannot reassign a value or append
mynumbers.sort()
print(myfavfruit)
print(myfavfruit[0])

#sets datastructure
myfavecars={"beemer","bentley","mercedes"}
myfavecars.add("discovery")
print(myfavecars)
#its unorganised and accepts additional varables

#dictionaries in python
magari={
    "name":"toyota",
    "model":"premio",
    "year": 2004
}
print(magari)
print(magari["model"                      xz])