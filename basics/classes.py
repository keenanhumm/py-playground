class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f"Hey there, my name is {self.name}.\n")


person1 = Person("Lebron", 27)
person2 = Person("Isaac", 34)
person1.speak()
person2.speak()
