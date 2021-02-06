class Car:
    wheels = 4
    def __init__(self,color,mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return f'The {self.color} car has {self.mileage} miles'

    def description(self):
        print(f'The {self.color} car has {self.mileage} miles')

Ford = Car('red','20,000')
Tata = Car('blue','30,000')

print(Ford)
Tata.description()


class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"


class GoldenRetriever(Dog):
    def speak(self, sound='bark'):
        return super().speak(sound)

goldenretriever = GoldenRetriever('Jack',4)

c = goldenretriever.speak()
print(c)

class Person:

    def __init__(self,name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")

pranjal = Person('Pranjal Parmar')
bob = Person('Bob Smith')

print(pranjal.name)
pranjal.talk()
bob.talk()
print(Ford.__dict__)