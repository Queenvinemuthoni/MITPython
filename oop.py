class EmobilisStudent:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def hello_me(self):
        print(f"My name is {self.name} and I'm {self.age} years old")
#creating an object
myobject=EmobilisStudent("Queenvine",18)
myobject2=EmobilisStudent("Queenvine",18)
myobject.hello_me()
myobject2.hello_me()

class Magari:
    def __init__(self,model,make,year):
        self.model=model
        self.make=make
        self.year=year
    def cars(self):
        print(f"{self.model} {self.make} {self.year}")
obj=Magari("Toyota","Premio","2015")
obj2=Magari("Nissan","Note","2019")
obj3=Magari("Mazda","CX5","2021")
obj.cars()
obj2.cars()
obj3.cars()

class Cities:
    def __init__(cities,country,city,attribute):
        cities.country=country
        cities.city=city
        cities.attribute=attribute
    def unique(cities):
        print(f"{cities.city} is located in {cities.country}"
              f" and it's known for {cities.attribute}")
object=Cities("Kenya","Nairobi","being the only capital with a national park "
                                "within it")
object2=Cities("Japan","Kyoto","its beautiful scenery during the spring season")
object.unique()
object2.unique()