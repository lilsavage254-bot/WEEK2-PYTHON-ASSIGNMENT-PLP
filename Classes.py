class Point :
    def __init__(self, x, y) :
        self.x = x 
        self.y = y
        
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point = Point(10, 20)
print(point.x)

point.draw()

class Person :
    def __init__(self, name) :
        self.name = name

    def talk(self) :
        print(f"Hi, I am {self.name}")


hashim= Person("HASHIM BAYA")
hashim.talk()

#INHERITANCE

class Mammal :
    def walk (self) :
        print("Walk")

class Dog(Mammal) :
    def bark(self) :
        print("Bark")

class Cat(Mammal) :
    def meoow(self) :
        print("Meoow")

dog1 = Dog()
dog1.walk()
dog1.bark()

cat1 = Cat()
cat1.walk()
cat1.meoow()