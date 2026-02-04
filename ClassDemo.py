# Mammal feature details

class Mammal:
    def __init__(self):
        print("Mammal class")

    def eat(self,species):
        if(species=="dog"):
            print(f'{species} is a meat eating animal.')
        elif (species =="bird"):
            print(f'{species} is neither an animal nor a meat eater.')
        else:
            print('Not able to identify')

class dog(Mammal):
    def bark(self):
        print("Dog barks")


m=Mammal()
d=dog()
print(d.eat("dog"))
print(d.bark())
