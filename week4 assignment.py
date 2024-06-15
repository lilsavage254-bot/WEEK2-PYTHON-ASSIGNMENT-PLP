<<<<<<< HEAD
class Person :
    def __init__(self, name, age, gender) :
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self) :
        print(f"NAME : {self.name} AGE : {self.age} GENDER : {self.gender}")

display = Person("HASHIM", 18, "MALE")
=======
class Person :
    def __init__(self, name, age, gender) :
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self) :
        print(f"NAME : {self.name} AGE : {self.age} GENDER : {self.gender}")

display = Person("HASHIM", 18, "MALE")
>>>>>>> e0323a1ddc73c8762807ff50153f36c1a8248443
print(display.introduce())