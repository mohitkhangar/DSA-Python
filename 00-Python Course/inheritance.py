class Animal:
    location="australia"
    def __init__(self,name):
        self.name=name
    def speak(self):
        print("generic Animal sound")
        
class Dog(Animal):
    def speak(self):
        print("woof!")
        
class Cat(Animal):
    def speak(self):
        print("meow!")
        
#a= animal("dog")
#a.speak()
d = Dog("Bruno")
d.speak()
print(d.location)

c = Cat("pussy")
c.speak()